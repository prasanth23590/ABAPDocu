---
title: "ABAP CDS - Scalar Functions"
source_file: abencds_scalar_functions.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Function Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Scalar Functions

A [CDS scalar function](../../abap-glossary/abencds_scalar_function_glosry.md) is defined in the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md) using the statement [`DEFINE SCALAR FUNCTION`](abencds_define_scalar_function.md). A CDS scalar function is a user-defined [CDS function](../../abap-glossary/abencds_function_glosry.md) that returns a scalar (that means [elementary](../../abap-glossary/abenelementary_data_type_glosry.md)) return value.

There are [analytical scalar functions](../../abap-glossary/abencds_ana_scalar_glosry.md) and [SQL-based scalar functions](../../abap-glossary/abencds_sql_scalar_glosry.md).

- [Analytical scalar functions](../../abap-glossary/abencds_ana_scalar_glosry.md)

  - Evaluated by an analytical runtime environment, such as the [ABAP Analytical Engine](../../abap-glossary/abenabap_ae_glosry.md).

  - The [scalar function implementation reference](../../abap-glossary/abencds_dsfi_glosry.md) has the suffix `_ANA`.

  - Can be used in [CDS analytical projection views](../../abap-glossary/abencds_analytical_pv_glosry.md) like built-in functions in operand positions that expect scalar values.

  - Analytical scalar functions can only be defined internally at SAP. They are available for internal and external use in [CDS analytical queries](../../abap-glossary/abencds_analytic_query_glosry.md).

  - For a list of analytical scalar functions delivered by SAP, see [ABAP CDS - Analytical Scalar Functions](abencds_ana_scalar_function.md).

- [SQL-based scalar functions](../../abap-glossary/abencds_sql_scalar_glosry.md)

  - Evaluated by an SQL environment.

  - The scalar function implementation reference has the suffix `_SQL`.

  - Can be used in [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) in operand positions that expect scalar values, similar to [built-in functions](../../abap-glossary/abenbuiltin_function_glosry.md).

  - An SQL-based scalar function consists of three development objects:

    \- A [scalar function definition](../../abap-glossary/abencds_dsfd_glosry.md) defined using [`DEFINE SCALAR FUNCTION`](abencds_define_scalar_function.md) in a [CDS function definition](../../abap-glossary/abencds_function_definition_glosry.md). - A [scalar function implementation reference](abencds_scalar_func_impl_ref.md) that binds the scalar function to the SQL environment and to an [AMDP function implementation](../../abap-glossary/abenamdp_function_method_glosry.md). The scalar function implementation reference is defined in a form-based editor in the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md). - An [AMDP function](../../abap-glossary/abenamdp_function_glosry.md) implementation where it is implemented using [SQLScript](../../abap-glossary/abensql_script_glosry.md) in a special [AMDP method](../../abap-glossary/abenamdp_method_glosry.md).

CDS scalar functions can be released as stable APIs under the [C1 release contract for system internal use](../../abap-glossary/abenc1_contract_glosry.md).

## Hints

- When creating a CDS scalar function, first the CDS scalar function definition must be activated, then the scalar function implementation reference must be activated, and finally the associated [AMDP function implementation](../../abap-glossary/abenamdp_function_method_glosry.md) is created.

- When a CDS scalar function is transported, first the CDS scalar function definition is transported at the same time as the dictionary transport objects, and then the AMDP function implementation is transported as part of the ABAP transport objects. Depending on the size of the transport, there may be a significant delay between these two phases during which the CDS scalar function is not in a usable state.

- [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md) and CDS scalar functions are both implemented in an [AMDP method](../../abap-glossary/abenamdp_method_glosry.md) as an [AMDP function implementation](../../abap-glossary/abenamdp_function_method_glosry.md). The differences between CDS table functions and CDS scalar functions are as follows:

  - CDS scalar functions return an elementary value, while CDS table functions return a tabular result type.

  - Different use cases:

    \- CDS table functions are used as a data sources in other CDS entities or in ABAP SQL read statements. - CDS scalar functions can be used in the same way as built-in functions, i.e. in operand positions that expect scalar values. Before the introduction of CDS scalar functions, users could define [AMDP scalar functions](../../abap-glossary/abenamdp_scalar_function_glosry.md), but they were not available in CDS entities. CDS scalar functions make scalar functions defined in AMDP known to [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md) and available in ABAP CDS.
