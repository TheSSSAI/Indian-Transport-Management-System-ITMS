# 1 Diagram Info

## 1.1 Diagram Name

High-Level System Architecture Diagram

## 1.2 Diagram Type

graph

## 1.3 Purpose

To provide a high-level overview of the TMS system architecture, showing the main components, their interactions, and the key technologies and AWS services used for deployment, based on requirements REQ-1-013, REQ-1-014, and REQ-1-400.

## 1.4 Target Audience

- developers
- product managers
- QA engineers
- DevOps/SRE

## 1.5 Complexity Level

medium

## 1.6 Estimated Review Time

3-5 minutes

# 2.0 Mermaid Implementation

| Property | Value |
|----------|-------|
| Mermaid Code | graph TD
    subgraph "User Space"
        User["A... |
| Syntax Validation | Mermaid syntax verified and tested for rendering. |
| Rendering Notes | Uses subgraphs to visually group components. Best ... |

# 3.0 Diagram Elements

## 3.1 Actors Systems

- Admin/Manager/Finance Officer
- Driver
- Odoo TMS Monolith
- GPS Ingestion Microservice
- GST Suvidha Provider (GSP) API
- 3rd Party GPS Provider API
- AWS Services (ALB, EKS, RDS, S3, MQ, Secrets Manager)
- Observability Stack

## 3.2 Key Processes

- User Interaction via Web/Mobile
- Trip & Financial Management (Odoo)
- E-Invoice Generation (GSP Integration)
- GPS Data Ingestion (Microservice)
- Asynchronous Communication (RabbitMQ)

## 3.3 Decision Points

- N/A for this architectural level

## 3.4 Success Paths

- User requests to Odoo application
- GPS data flow from external provider to Odoo
- E-invoicing flow to GSP API

## 3.5 Error Scenarios

- N/A for this architectural level, covered in sequence diagrams

## 3.6 Edge Cases Covered

- N/A for this architectural level

# 4.0 Accessibility Considerations

| Property | Value |
|----------|-------|
| Alt Text | A system architecture diagram of the Transport Man... |
| Color Independence | Information is primarily conveyed through text lab... |
| Screen Reader Friendly | All nodes and components have descriptive text lab... |
| Print Compatibility | Diagram uses standard shapes and lines, rendering ... |

# 5.0 Technical Specifications

| Property | Value |
|----------|-------|
| Mermaid Version | 10.0+ compatible |
| Responsive Behavior | Diagram is vertically oriented (TD) and uses subgr... |
| Theme Compatibility | Works with default, dark, and neutral themes. Cust... |
| Performance Notes | The diagram is of moderate complexity and should r... |

# 6.0 Usage Guidelines

## 6.1 When To Reference

During project onboarding, architectural reviews, and when discussing system integrations or deployment strategy.

## 6.2 Stakeholder Value

| Property | Value |
|----------|-------|
| Developers | Provides a clear map of the system's components an... |
| Designers | N/A for this diagram type. |
| Product Managers | Helps understand the technical landscape and depen... |
| Qa Engineers | Identifies key integration points that require tes... |

## 6.3 Maintenance Notes

Update this diagram if new microservices are added, major AWS services are changed, or a new external integration is introduced.

## 6.4 Integration Recommendations

Embed this diagram in the project's primary README file and in high-level design documentation.

# 7.0 Validation Checklist

- ✅ All critical system components and actors documented
- ✅ Key interactions and data flows are included
- ✅ Architectural boundaries are clearly marked with subgraphs
- ✅ Mermaid syntax validated and renders correctly
- ✅ Diagram provides a clear overview for technical and semi-technical audiences
- ✅ Visual hierarchy (grouping) supports easy comprehension
- ✅ Styling enhances rather than distracts from content
- ✅ Accessible to users with different visual abilities

