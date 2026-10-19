---
title: "AMDP - Glossary"
source_file: abenamdp_glossary.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - Glossary

In the following, terms of the [ABAP Glossary](../../abap-glossary/abenabap_glossary.md) are listed, that are relevant for [AMDP](abenamdp.md).

**ABAP Managed Database Procedures**

AMDP for short. Class-based framework for managing and calling [stored procedures](../../abap-glossary/abenstored_procedure_glosry.md) or [database procedures](../../abap-glossary/abendatabase_procedure_glosry.md) as [AMDP procedures](../../abap-glossary/abenamdp_procedure_glosry.md) in [AS ABAP](../../abap-glossary/abenas_abap_glosry.md).

**AMDP**

*-\>* [ABAP Managed Database Procedures](../../abap-glossary/abenabap_managed_db_proc_glosry.md)

**AMDP BAdI**

Special [BAdI](../../abap-glossary/abenbadi_glosry.md) for [AMDP procedure implementations](../../abap-glossary/abenamdp_procedure_method_glosry.md). If the associated [AMDP procedure](../../abap-glossary/abenamdp_procedure_glosry.md) is called from a different [AMDP method](../../abap-glossary/abenamdp_method_glosry.md), this takes place based on the switch-based rules of the ABAP Enhancement Framework.

**AMDP class**

[Global class](../../abap-glossary/abenglobal_class_glosry.md) with one or more [tag interfaces](../../abap-glossary/abentag_interface_glosry.md) `IF_AMDP_MARKER_ ...` for [ABAP Managed Database Procedures](../../abap-glossary/abenabap_managed_db_proc_glosry.md). An AMDP class can contain [AMDP methods](../../abap-glossary/abenamdp_method_glosry.md) for different [database systems](../../abap-glossary/abendatabase_system_glosry.md).

**AMDP function**

[Database function](../../abap-glossary/abendatabase_function_glosry.md) of the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) that is implemented in an [AMDP function implementation](../../abap-glossary/abenamdp_function_method_glosry.md) of an [AMDP class](../../abap-glossary/abenamdp_class_glosry.md) and is replicated from there to the [database system](../../abap-glossary/abendatabase_system_glosry.md). There are [AMDP table functions](../../abap-glossary/abenamdp_table_function_glosry.md) or [AMDP scalar functions](../../abap-glossary/abenamdp_scalar_function_glosry.md). See also [AMDP procedure](../../abap-glossary/abenamdp_procedure_glosry.md).

**AMDP function implementation**

[AMDP method](../../abap-glossary/abenamdp_method_glosry.md) with [return value](../../abap-glossary/abenreturn_value_glosry.md) that is indicated by [`BY DATABASE FUNCTION`](abapmethod_by_db_proc.md) in the [implementation part](../../abap-glossary/abenimplementation_part_glosry.md) of the [class](../../abap-glossary/abenclass_glosry.md). AMDP functions are implemented in an [AMDP function](../../abap-glossary/abenamdp_function_glosry.md) implementation. An AMDP function implementation for an [AMDP scalar function](../../abap-glossary/abenamdp_scalar_function_glosry.md) can be called in ABAP programs like a regular [functional method](../../abap-glossary/abenfunctional_method_glosry.md). An AMDP function implementation for an [AMDP table function](../../abap-glossary/abenamdp_table_function_glosry.md), on the other hand, is generally used to implement a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md). It can be used as a data source of [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) read statements using the [CDS entity](../../abap-glossary/abencds_entity_glosry.md), but cannot be called in ABAP programs. See also [AMDP procedure implementation](../../abap-glossary/abenamdp_procedure_method_glosry.md).

**AMDP macro**

Syntax specified in the implementation of an [AMDP method](../../abap-glossary/abenamdp_method_glosry.md) in [SQLScript](../../abap-glossary/abensql_script_glosry.md), which is replaced by the [ABAP runtime framework](../../abap-glossary/abenabap_runtime_frmwk_glosry.md) when the [database procedure](../../abap-glossary/abendatabase_procedure_glosry.md) is generated on the [database](../../abap-glossary/abendatabase_glosry.md) in compliance with the assigned rules.

**AMDP method**

[Method](../../abap-glossary/abenmethod_glosry.md) of an [AMDP class](../../abap-glossary/abenamdp_class_glosry.md) that is flagged as an [AMDP procedure implementation](../../abap-glossary/abenamdp_procedure_method_glosry.md) using [`BY DATABASE PROCEDURE`](abapmethod_by_db_proc.md) or as an [AMDP function implementation](../../abap-glossary/abenamdp_function_method_glosry.md) using [`BY DATABASE FUNCTION`](abapmethod_by_db_proc.md) in the [implementation part](../../abap-glossary/abenimplementation_part_glosry.md) of the class.

**AMDP procedure**

[Database procedure](../../abap-glossary/abendatabase_procedure_glosry.md) implemented in an [AMDP procedure implementation](../../abap-glossary/abenamdp_procedure_method_glosry.md) of an [AMDP class](../../abap-glossary/abenamdp_class_glosry.md) and replicated from there to the [database system](../../abap-glossary/abendatabase_system_glosry.md). See [AMDP function](../../abap-glossary/abenamdp_function_glosry.md).

**AMDP procedure implementation**

[AMDP method](../../abap-glossary/abenamdp_method_glosry.md) without [return value](../../abap-glossary/abenreturn_value_glosry.md) that is indicated by [`BY DATABASE PROCEDURE`](abapmethod_by_db_proc.md) in the [implementation part](../../abap-glossary/abenimplementation_part_glosry.md) of the class. In an AMDP procedure implementation, [AMDP procedures](../../abap-glossary/abenamdp_procedure_glosry.md) are implemented in a database-specific language as [ABAP Managed Database Procedures](../../abap-glossary/abenabap_managed_db_proc_glosry.md). AMDP procedure implementations are called in ABAP just like regular methods and passed to the database system using the Native SQL interface and executed here. See also [AMDP function implementation](../../abap-glossary/abenamdp_procedure_glosry.md).

**AMDP scalar function**

[Scalar function](../../abap-glossary/abenscalar_function_glosry.md) of the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) implemented in an [AMDP function implementation](../../abap-glossary/abenamdp_function_method_glosry.md) of an [AMDP class](../../abap-glossary/abenamdp_class_glosry.md) and replicated from here to the [database system](../../abap-glossary/abendatabase_system_glosry.md).

**AMDP table function**

[Table function](../../abap-glossary/abentable_function_glosry.md) of the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) implemented in an [AMDP function implementation](../../abap-glossary/abenamdp_function_method_glosry.md) of an [AMDP class](../../abap-glossary/abenamdp_class_glosry.md) and replicated from here to the [database system](../../abap-glossary/abendatabase_system_glosry.md).

**C4 contract, use in ABAP-Managed Database Procedures**

[Release contract](../../abap-glossary/abenrelease_contract_glosry.md) that ensures a stable public interface of [released APIs](../../abap-glossary/abenreleased_api_glosry.md) for use in [ABAP Managed Database Procedures](../../abap-glossary/abenabap_managed_db_proc_glosry.md) (AMDP).

**client handling**

Processing of the application data of a [client](../../abap-glossary/abenclient_glosry.md). When accessing [client-dependent](../../abap-glossary/abenclient_dependent_glosry.md) [DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md) or [views](../../abap-glossary/abenview_glosry.md), [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statements use [implicit client](abenabap_sql_client_handling.md) handling, which by default accesses the [current client](../../abap-glossary/abencurrent_client_glosry.md). By using additions to the ABAP SQL statements, the implicit client handling can be switched to other clients. The client handling of [AMDP methods](../../abap-glossary/abenamdp_method_glosry.md) can be defined with special [AMDP options](abapmethods_amdp_options_client.md).

**graph procedure**

A graph procedure is an [ABAP Managed Database Procedure](../../abap-glossary/abenabap_managed_db_proc_glosry.md). It refers to [graph workspace](../../abap-glossary/abengraph_workspace_glosry.md) and operates on [graph](../../abap-glossary/abengraph_glosry.md) models. It is a read-only procedure that is written in [GraphScript](../../abap-glossary/abengraphscript_glosry.md).
