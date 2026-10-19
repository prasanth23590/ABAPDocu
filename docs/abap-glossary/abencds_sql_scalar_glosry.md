---
title: "SQL-based scalar function"
source_file: abencds_sql_scalar_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SQL-based scalar function

[CDS](../abap-core-data-services-abap-cds/abencds_glossary.md)

## Definition

[CDS scalar function](abencds_scalar_function_glosry.md) that is evaluated by an SQL environment. SQL-based scalar functions can be used in [CDS view entities](abencds_v2_view_glosry.md) in operand positions that expect scalar values.

SQL-based scalar functions can be [user-defined functions](abencds_user_func_glosry.md) or [system functions](abencds_system_func_glosry.md).

A CDS scalar function consists of three development objects:

- A [CDS entity](abencds_entity_glosry.md) defined using [`DEFINE SCALAR FUNCTION`](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_scalar_function.md) in a [CDS data definition](abencds_data_definition_glosry.md).

- A [scalar function implementation reference](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_scalar_func_impl_ref.md) that binds the scalar function to the SQL environment and to an [AMDP function implementation](abenamdp_function_method_glosry.md).

- An [AMDP function](abenamdp_function_glosry.md) that implements the scalar function as [database function](abendatabase_function_glosry.md).

[***-\>* More about**](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_sql_scalar_function.md)
