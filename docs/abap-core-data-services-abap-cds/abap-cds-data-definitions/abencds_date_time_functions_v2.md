---
title: "CDS DDL - CDS View Entity, Date Functions and Time Functions"
source_file: abencds_date_time_functions_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Expressions > CDS DDL - CDS View Entity, Built-In Functions > CDS DDL - CDS View Entity, Special Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, Date Functions and Time Functions

[Date Functions and Time Functions](../../abap-dictionary-ddic/ddic-built-in-functions/abenddic_date_time_functions.md) in a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md):

- [Date Functions](abencds_date_functions_v2.md)

- [Time Functions](abencds_time_functions_v2.md)

- [Time Stamp Functions](abencds_timestamp_functions_v2.md)

- [Time Zone Functions](abencds_timezone_functions_v2.md)

- [Date/Time Conversions](abencds_date_time_conversions_v2.md)

## Hints

- The session variable [`$session.system_date`](abencds_session_variable_v2.md) is used in a CDS view entity to provide direct access to the current system date.

- There is not yet a session variable for the current system time and a CDS view entity can be given an appropriate [input parameter](abencds_parameter_list_v2.md) instead. The special annotation [`@Environment.systemField`](abencds_f1_parameter_annotations.md) makes it possible to pass the value of the [ABAP system field](../../abap-glossary/abensystem_field_glosry.md) `sy-uzeit` to a parameter of this type.
