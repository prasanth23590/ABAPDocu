---
title: "CDS DDL - DDIC-Based View, Date Functions and Time Functions"
source_file: abencds_date_time_functions_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Expressions > CDS DDL - DDIC-Based View, Built-In Functions > CDS DDL - DDIC-Based View, Special Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, Date Functions and Time Functions

[Date Functions and Time Functions](../../abap-dictionary-ddic/ddic-built-in-functions/abenddic_date_time_functions.md) in a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md):

- [Date Functions](abencds_date_functions_v1.md)

- [Time Functions](abencds_time_functions_v1.md)

- [Time Stamp Functions](abencds_timestamp_functions_v1.md)

- [Time Zone Functions](abencds_timezone_functions_v1.md)

- [Date/Time Conversions](abencds_date_time_conversions_v1.md)

## Hints

- The session variable [`$session.system_date`](abencds_session_variable_v1.md) is used in a CDS view to provide direct access to the current system date.

- There is not yet a session variable for the current system time and a CDS view can be given an appropriate [input parameter](abencds_parameter_list_v1.md) instead. The special annotation [`@Environment.systemField`](../abap-cds-data-definitions/abencds_f1_parameter_annotations.md) makes it possible to pass the value of the [ABAP system field](../../abap-glossary/abensystem_field_glosry.md) `sy-uzeit` to a parameter of this type.
