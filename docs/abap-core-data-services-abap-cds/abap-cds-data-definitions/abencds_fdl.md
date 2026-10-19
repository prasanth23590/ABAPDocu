---
title: "ABAP CDS - Function Definitions"
source_file: abencds_fdl.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Function Definitions

CDS function definitions allow the definition of user-defined [CDS functions](../../abap-glossary/abencds_function_glosry.md) that encapsulate algorithms into reusable code which can be used operand positions of [CDS entities](../../abap-glossary/abencds_entity_glosry.md). CDS function definitions can be used to define the following [CDS functions](../../abap-glossary/abencds_function_glosry.md):

- [CDS scalar functions](../../abap-glossary/abencds_scalar_function_glosry.md)

## Hint

[CDS table functions](../../abap-glossary/abencds_table_function_glosry.md) are [CDS data definitions](../../abap-glossary/abencds_data_definition_glosry.md) defined in [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md). CDS table functions encapsulate AMDP functions, but they are [CDS entities](../../abap-glossary/abencds_entity_glosry.md) and they belong to the technical category of [CDS data definitions](../../abap-glossary/abencds_data_definition_glosry.md). CDS table functions have the characteristics of CDS data definitions: they can be used as data source in other CDS entities and for typing in ABAP using the `TYPE` statement. Despite the name, a CDS table function is not a CDS function definition.
