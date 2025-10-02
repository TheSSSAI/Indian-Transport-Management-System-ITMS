sequenceDiagram
    participant "SRE" as SRE
    participant "Grafana" as Grafana
    participant "OpenSearch Cluster" as OpenSearchCluster
    participant "Prometheus Server" as PrometheusServer
    participant "Fluentbit Agent" as FluentbitAgent
    participant "EKS Node / Container Runtime" as EKSNodeContainerRuntime
    participant "Odoo Application Pod" as OdooApplicationPod

    activate OdooApplicationPod
    OdooApplicationPod->>OdooApplicationPod: 1. 1. Application event occurs (e.g., Trip status changes).
    OdooApplicationPod->>EKSNodeContainerRuntime: 2. 2. Writes structured JSON log to stdout.
    EKSNodeContainerRuntime-->>OdooApplicationPod: Container runtime captures log.
    activate FluentbitAgent
    EKSNodeContainerRuntime->>FluentbitAgent: 3. 3. Tailing container log file.
    FluentbitAgent->>FluentbitAgent: 4. 4. Enriches log with Kubernetes metadata.
    FluentbitAgent->>OpenSearchCluster: 5. 5. Forwards enriched log batch.
    OpenSearchCluster-->>FluentbitAgent: 6. 200 OK
    PrometheusServer->>OdooApplicationPod: 7. 7. Scrape metrics endpoint.
    OdooApplicationPod-->>PrometheusServer: 8. Prometheus exposition format text.
    activate Grafana
    SRE->>Grafana: 9. 9. Accesses 'TMS System Health' dashboard.
    Grafana-->>SRE: 10. Renders dashboard UI.
    Grafana->>PrometheusServer: 11. 11. Queries for metrics data.
    PrometheusServer-->>Grafana: 12. Time-series data (JSON).
    Grafana->>OpenSearchCluster: 13. 13. Queries for log data.
    OpenSearchCluster-->>Grafana: 14. Log documents (JSON).
    Grafana->>SRE: 15. 15. Presents unified view with correlated logs and metrics.


    deactivate Grafana
    deactivate FluentbitAgent
    deactivate OdooApplicationPod
