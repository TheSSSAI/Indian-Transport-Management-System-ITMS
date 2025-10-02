# 1 Id

312

# 2 Section

Indian Transport Management System (ITMS) Specification

# 3 Section Id

SRS-001

# 4 Section Requirement Text

```javascript
As the owner of a growing Indian transport company, I require a robust, scalable, and user-friendly Transport Management System (TMS) to digitize and manage all aspects of logistics operations, including trip planning, vehicle tracking, freight management, invoicing, driver coordination, and customer service. This system will serve as the digital backbone of the business, helping us optimize vehicle utilization, reduce manual paperwork, and gain real-time visibility into our fleet and deliveries. It should be developed as a web-based application with a mobile-friendly interface for both internal staff and on-the-road drivers.

The platform must allow our dispatch team to create and manage trips by assigning vehicles, routes, and drivers. For each trip, we should be able to record the source, destination, material details (e.g., paper rolls, steel, cement), weight, customer details, rate per km or ton, expected delivery date, and payment status. The system should maintain a vehicle master with information such as truck number, model, capacity, owner details (if outsourced), service history, and document expiry reminders (e.g., PUC, insurance, fitness). Similarly, a driver master should track license details, performance, assigned vehicles, salary, and trip-wise incentives. Alerts for expiring documents. All documents have expiry. Documents can be attached to a vehicle. A type of document can be identifiable.

The backend must include trip status updates (assigned, in-transit, delivered, canceled), GPS integration for live tracking (via third-party API or GPS device sync), and geofencing options. The system should also maintain diesel and toll expense records, calculate trip profitability, and <<$Change>> allow for manual entry of FASTag and diesel card balances, and notify the team when the manually updated balance falls below a configurable threshold. <<$Change>>
Enhancement Justification:
The original requirement for automated notification of low FASTag or diesel card balances is technically infeasible due to the lack of universal, real-time API access from various card issuers. This change modifies the mechanism to a manual input process for balances, which is then used by the system to trigger notifications based on configurable thresholds. This preserves the core business need for alerting about low balances while addressing the technical limitations.

A financial module should allow for invoice generation, trip-wise expense vs. revenue tracking, and customer ledger maintenance. Integration with GST-compliant e-invoicing and the ability to export reports in Excel/PDF is essential. The driver can easily add a runtime expense from mobile mobile-friendly web interface for a trip. The backend office can add expenses like document renewal, maintenance, insurance, repair etc, these are not related to trip but only related to the vehicle.

<<$Change>> The mobile-friendly web interface for drivers must allow them to receive trip assignments, update delivery status with proof of delivery (photo or e-signature), view past trips, and request advances or leave. <<$Change>> Admins should have a powerful dashboard with filters to view pending deliveries, payment collection status, vehicle availability, and fuel efficiency reports.
Enhancement Justification:
The original requirements contained a contradiction regarding the driver interface, initially stating "mobile-friendly interface" and later "No mobile app required," while also referring to a "mobile app (for drivers)." This change clarifies that the driver interface will be a mobile-friendly web interface, consistent with the explicit statement "No mobile app required," ensuring a unified and unambiguous platform strategy without altering the intended driver functionalities.

Optional but future-ready features include: live load tracking for customers via link or login, integration with logistics marketplaces (e.g., BlackBuck, Rivigo), predictive maintenance alerts using AI, and a multilingual UI (Hindi, Marathi, etc.) for driver accessibility.

The system must be developed as an Odoo 18 addon. The frontend was also developed in Odoo18 addon, Front end app to be mobile-friendly. Drivers can access the assigned vehicle document from the web UI that is mobile-friendly. No mobile app required. Try to reuse pre-existing components.

The system must have all detail required reports.
Dashboards
Alerts

This TMS will not only reduce paperwork and manual errors but also bring professional control and transparency to our transport operations — ultimately helping us scale the business, improve customer trust, and stay competitive in the Indian logistics market.
```

# 5 Requirement Type

other

# 6 Priority

🔹 ❌ No

# 7 Original Text

❌ No

# 8 Change Comments

❌ No

# 9 Enhancement Justification

❌ No

