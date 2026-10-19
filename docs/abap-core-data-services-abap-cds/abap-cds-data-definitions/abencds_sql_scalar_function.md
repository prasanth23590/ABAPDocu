---
title: "ABAP CDS - SQL-Based Scalar Functions"
source_file: abencds_sql_scalar_function.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Function Definitions > ABAP CDS - Scalar Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - SQL-Based Scalar Functions

[SQL-based scalar functions](../../abap-glossary/abencds_sql_scalar_glosry.md) are [scalar functions](../../abap-glossary/abencds_scalar_function_glosry.md) that are evaluated by an SQL environment. They can be used in [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) in operand positions that expect scalar values, similar to [built-in functions](abencds_builtin_functions_v2.md). They can also be used as operands in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md). This is described in the topic [`sql_exp` - `cds_scalar_func`](../../abap-programming-language/abap-database-access/abensql_cds_scalar_func.md).

While [analytical scalar functions](abencds_ana_scalar_function.md) are defined and implemented by SAP, SQL-based scalar functions can also be defined and implemented by customers and partners. SQL-based scalar functions make user-defined [AMDP scalar functions](../../abap-glossary/abenamdp_scalar_function_glosry.md) known to the ABAP Dictionary and available in ABAP CDS.

An SQL-based scalar function consists of three development objects:

- A [scalar function definition](../../abap-glossary/abencds_dsfd_glosry.md) defined using [`DEFINE SCALAR FUNCTION`](abencds_define_scalar_function.md) in a [CDS function definition](../../abap-glossary/abencds_function_definition_glosry.md). It is located in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP.

- A [scalar function implementation reference](abencds_scalar_func_impl_ref.md) that binds the scalar function to the SQL environment and to an [AMDP function implementation](../../abap-glossary/abenamdp_function_method_glosry.md). The scalar function implementation reference is defined in a form-based editor in the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md). It must refer to an existing CDS scalar function. It is a standalone repository object that is transported and has its own editor in ADT.

- An [AMDP function](../../abap-glossary/abenamdp_function_glosry.md) that implements the CDS scalar function using [SQLScript](../../abap-glossary/abensql_script_glosry.md) in a special [AMDP method](../../abap-glossary/abenamdp_method_glosry.md). The implementation is managed as an [AMDP scalar function](../../abap-glossary/abenamdp_table_function_glosry.md) by the [AMDP](../../abap-glossary/abenamdp_glosry.md) in the database system. The AMDP method must be declared as a special [AMDP function implementation](../../abap-programming-language/abap-database-access/abenamdp_function_methods.md) for exactly one CDS scalar function using the addition [`FOR SCALAR FUNCTION`](../../abap-programming-language/abap-database-access/abapclass-methods_for_scalfunc.md). The parameter interface of the AMDP scalar function is defined by the input parameters and the scalar result type of the CDS scalar function.

[Client handling](../../abap-glossary/abenclient_handling_glosry.md) has not yet been implemented for CDS scalar functions, so only [client-independent](../../abap-glossary/abenclient_independent_glosry.md) scalar functions are supported. The AMDP method that implements a scalar function can only access client-independent objects. However, when it is used, client dependency is ignored. A CDS scalar function can be used in both client-dependent and client-independent CDS entities.

The following topics describe the syntax for defining SQL-based scalar functions.

- [CDS DDL - `DEFINE SCALAR FUNCTION`](abencds_define_scalar_function.md)

## Hint

CDS SQL-based scalar functions cannot be processed by the [ABAP SQL in-memory engine](../../abap-programming-language/abap-database-access/abenabap_sql_inmemeng.md). An ABAP SQL statement that accesses a CDS scalar function bypasses the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table accessed by [`FROM @itab`](../../abap-programming-language/abap-database-access/abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

## More Information

For further details on user-defined scalar functions in ABAP CDS, see [*SQL-Based Scalar Functions*](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/7370f3f78a6d4940af29ab89abf7f1b0?version=sap_cross_product_abap) in the ABAP Data Models guide on SAP Help Portal.
