---
title: "AMDP function implementation"
source_file: abenamdp_function_method_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP function implementation

[ABAP Language](../abap-programming-language/abenabala_glossary.md) [AMDP](../abap-programming-language/abap-database-access/abenamdp_glossary.md)

## Definition

[AMDP method](abenamdp_method_glosry.md) with [return value](abenreturn_value_glosry.md) that is indicated by [`BY DATABASE FUNCTION`](../abap-programming-language/abap-database-access/abapmethod_by_db_proc.md) in the [implementation part](abenimplementation_part_glosry.md) of the [class](abenclass_glosry.md). AMDP functions are implemented in an [AMDP function](abenamdp_function_glosry.md) implementation. An AMDP function implementation for an [AMDP scalar function](abenamdp_scalar_function_glosry.md) can be called in ABAP programs like a regular [functional method](abenfunctional_method_glosry.md). An AMDP function implementation for an [AMDP table function](abenamdp_table_function_glosry.md), on the other hand, is generally used to implement a [CDS table function](abencds_table_function_glosry.md). It can be used as a data source of [ABAP SQL](abenabap_sql_glosry.md) read statements using the [CDS entity](abencds_entity_glosry.md), but cannot be called in ABAP programs. See also [AMDP procedure implementation](abenamdp_procedure_method_glosry.md).

[***-\>* More about**](../abap-programming-language/abap-database-access/abenamdp_function_methods.md)
