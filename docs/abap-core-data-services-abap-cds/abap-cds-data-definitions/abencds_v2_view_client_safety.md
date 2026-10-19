---
title: "ABAP CDS - Client Safety of CDS View Entities"
source_file: abencds_v2_view_client_safety.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > ABAP CDS - Client Handling in CDS View Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Client Safety of CDS View Entities

The annotation [`ClientHandling.clientSafe`](../abap-cds-annotations/abencds_1549616294_anno.md) declares a CDS view entity as [client-safe](../../abap-glossary/abenclient_safe_glosry.md). If the value `true` (default) is used for that annotation, the following prerequisites for client safety are checked implicitly:

- All used objects must be client-safe.

- It is not allowed to pass an actual parameter other than [`$session.client`](abencds_session_var_builtin_v2.md) to the input parameter for the client of built-in functions such as [`ABAP_USER_TIMEZONE`](../../abap-programming-language/abap-database-access/abensql_timezone_func.md) or [`CURRENCY_CONVERSION`](abencds_conv_func_unit_curr_v2.md).

## Hints

- If the view entity has the ABAP language version [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md) or is a [released API](../../abap-glossary/abenreleased_api_glosry.md), the checks are done implicitly and client safety is enforced where necessary.

- [Client safety](../../abap-glossary/abenclient_safe_glosry.md) is required, e.g. when using a client-dependent CDS view entity in a client-safe [AMDP method](../../abap-glossary/abenamdp_method_glosry.md),
