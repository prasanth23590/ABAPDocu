---
title: "Contract Rules for API Consumers"
source_file: abenconsumer_rules.html
section: "ABAP APIs > Release Contracts"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Contract Rules for API Consumers

The provider rules for objects with a release contract ensure that released objects are changed only in a very restricted way and help to avoid errors and interruptions after an SAP upgrade. Nevertheless, the rules do not prescribe full downward compatibility and leave some room for necessary enhancements to released APIs. Therefore, users of released APIs still have to consider the allowed compatible changes and access the APIs in such a way that the following errors and interruptions are avoided:

- Problems during the upgrade.

- Syntax errors after the upgrade.

- Runtime errors after an upgrade.

- Wrong behavior after an upgrade.

The following sections list allowed changes to released APIs that must be considered when the APIs are accessed.

- [C0 Contract Rules for Consumers of DDIC Objects](abenc0_consumer_rules_ddic.md)

- [C0 Contract Rules for Consumers of CDS Entities](abenc0_consumer_rules_cds.md)

- [C0 Contract Rules for Consumers of RAP Behavior Definitions](abenc0_consumer_rules_bdef.md)

- [C1 Contract Rules for Consuming Elementary Types](abenc1_consumer_rules_elem.md)

- [C1 Contract Rules for Consuming Structures](abenc1_consumer_rules_struct.md)

- [Example: Consumption of APIs with C1 Contract](abenc1_demo_1.md)
