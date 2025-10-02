resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = merge(
    var.tags,
    {
      Name = "${var.project_name}-${var.environment}-vpc"
    }
  )
}

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = merge(
    var.tags,
    {
      Name = "${var.project_name}-${var.environment}-igw"
    }
  )
}

resource "aws_subnet" "public" {
  for_each = { for i, cidr in var.public_subnet_cidrs : i => cidr }

  vpc_id                  = aws_vpc.main.id
  cidr_block              = each.value
  availability_zone       = var.availability_zones[each.key]
  map_public_ip_on_launch = true

  tags = merge(
    var.tags,
    {
      Name                                = "${var.project_name}-${var.environment}-public-subnet-${each.key + 1}"
      "kubernetes.io/role/elb"            = "1"
      "kubernetes.io/cluster/${var.project_name}-${var.environment}-eks" = "shared"
    }
  )
}

resource "aws_subnet" "private" {
  for_each = { for i, cidr in var.private_subnet_cidrs : i => cidr }

  vpc_id                  = aws_vpc.main.id
  cidr_block              = each.value
  availability_zone       = var.availability_zones[each.key]
  map_public_ip_on_launch = false

  tags = merge(
    var.tags,
    {
      Name                                = "${var.project_name}-${var.environment}-private-subnet-${each.key + 1}"
      "kubernetes.io/role/internal-elb"   = "1"
      "kubernetes.io/cluster/${var.project_name}-${var.environment}-eks" = "shared"
    }
  )
}

resource "aws_eip" "nat" {
  count = length(var.public_subnet_cidrs)
  domain = "vpc"

  tags = merge(
    var.tags,
    {
      Name = "${var.project_name}-${var.environment}-nat-eip-${count.index + 1}"
    }
  )
}

resource "aws_nat_gateway" "main" {
  count         = length(var.public_subnet_cidrs)
  allocation_id = aws_eip.nat[count.index].id
  subnet_id     = values(aws_subnet.public)[count.index].id

  tags = merge(
    var.tags,
    {
      Name = "${var.project_name}-${var.environment}-nat-gw-${count.index + 1}"
    }
  )

  depends_on = [aws_internet_gateway.main]
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }

  tags = merge(
    var.tags,
    {
      Name = "${var.project_name}-${var.environment}-public-rt"
    }
  )
}

resource "aws_route_table" "private" {
  count  = length(var.private_subnet_cidrs)
  vpc_id = aws_vpc.main.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.main[count.index].id
  }

  tags = merge(
    var.tags,
    {
      Name = "${var.project_name}-${var.environment}-private-rt-${count.index + 1}"
    }
  )
}

resource "aws_route_table_association" "public" {
  for_each       = aws_subnet.public
  subnet_id      = each.value.id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "private" {
  count          = length(var.private_subnet_cidrs)
  subnet_id      = values(aws_subnet.private)[count.index].id
  route_table_id = aws_route_table.private[count.index].id
}