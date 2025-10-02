# main.tf in modules/mq
# Provisions a high-availability Amazon MQ for RabbitMQ broker.
# Aligns with REQ-1-402, REQ-1-502, and the resilience requirements from sequence diagrams.

data "aws_secretsmanager_secret_version" "mq_user" {
  secret_id = var.mq_username_secret_arn
}

data "aws_secretsmanager_secret_version" "mq_password" {
  secret_id = var.mq_password_secret_arn
}

# Dead-Letter Queue (DLQ) and exchange configuration for RabbitMQ
# This configuration will be applied to the broker.
locals {
  rabbitmq_config = <<CONFIG
<rabbitmq>
  <users>
    <user>
      <name>${data.aws_secretsmanager_secret_version.mq_user.secret_string}</name>
      <password>${data.aws_secretsmanager_secret_version.mq_password.secret_string}</password>
      <tags>
        <tag>administrator</tag>
      </tags>
    </user>
  </users>
  <vhosts>
    <vhost>
      <name>/</name>
        <policies>
          <policy>
            <name>dead-letter-policy</name>
            <pattern>.*</pattern>
            <apply-to>queues</apply-to>
            <definition>
              <dead-letter-exchange>dlx.exchange</dead-letter-exchange>
            </definition>
          </policy>
        </policies>
    </vhost>
  </vhosts>
  <plugins>
    <plugin>rabbitmq_management</plugin>
  </plugins>
</rabbitmq>
CONFIG
}

resource "aws_mq_configuration" "main" {
  name           = "${var.project_name}-${var.environment}-mq-config"
  engine_type    = "RabbitMQ"
  engine_version = var.broker_engine_version
  data           = local.rabbitmq_config

  tags = merge(var.tags, {
    Name = "${var.project_name}-${var.environment}-mq-config"
  })
}

resource "aws_mq_broker" "main" {
  broker_name    = "${var.project_name}-${var.environment}-mq-broker"
  engine_type    = "RabbitMQ"
  engine_version = var.broker_engine_version
  host_instance_type = var.broker_instance_type
  deployment_mode    = var.multi_az ? "CLUSTER_MULTI_AZ" : "SINGLE_INSTANCE"
  subnet_ids         = var.multi_az ? var.private_subnet_ids : [var.private_subnet_ids[0]]
  security_groups    = [var.vpc_security_group_id]
  publicly_accessible = false

  user {
    username = data.aws_secretsmanager_secret_version.mq_user.secret_string
    password = data.aws_secretsmanager_secret_version.mq_password.secret_string
  }

  configuration {
    id       = aws_mq_configuration.main.id
    revision = aws_mq_configuration.main.latest_revision
  }

  logs {
    general = true
    audit   = false
  }

  maintenance_window_start_time {
    day_of_week = "SUNDAY"
    time_of_day = "03:00"
    time_zone   = "UTC"
  }

  tags = merge(var.tags, {
    Name = "${var.project_name}-${var.environment}-mq-broker"
  })
}