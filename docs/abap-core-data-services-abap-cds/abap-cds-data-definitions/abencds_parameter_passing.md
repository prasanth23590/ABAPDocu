---
title: "CDS DDL - Parameter Passing in Scalar Functions"
source_file: abencds_parameter_passing.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Function Definitions > ABAP CDS - Scalar Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - Parameter Passing in Scalar Functions

## Syntax

``` abap
... ( pname1 => act1, pname2 => act2, ... ) ...  
```

## Description

Passes the actual parameters `act1`, `act2`, ... to the input parameters `pname1`, `pname2`, ... of an [SQL-based scalar function](../../abap-glossary/abencds_sql_scalar_glosry.md).

The following can be specified as actual parameters:

- [Literals](abencds_literal_v2.md) (typed or untyped)

- [Parameters](abencds_parameter_v2.md)

- [Session variables](abencds_session_variable_v2.md)

- [Fields](abencds_field_v2.md) of a data source

- [Built-in functions](abencds_builtin_functions_v2.md) if they return a suitable data type

- [Arithmetic expressions](abencds_arithmetic_expression_v2.md)

- [Aggregate functions](abencds_aggregate_functions_v2.md)

- [Cast expressions](abencds_cast_expression_v2.md)

- [Case distinctions](abencds_case_expression_v2.md)

- Another SQL-based scalar function

- A reuse expression using [`$projection.fieldName`](abencds_reusable_expression_v2.md)

  **Note:** Reuse expressions defined with `$projection` lose their reference information. `$projection` fields do not inherit annotations, so the references to [currency keys](../../abap-glossary/abencurrency_key_glosry.md) or [unit keys](../../abap-glossary/abenunit_glosry.md) are lost.

- A [path expression](abencds_path_expression_v2.md)

The data types of the actual parameters must exactly match the [typing](abencds_typing.md) of the input parameters. The reference type specification [`WITH REFERENCE TYPE`](abencds_with_reference_type.md), if any, must be followed. Otherwise, a syntax check error occurs.

If an input parameter requires one of the reference types `#CUKY`, `#UNIT`, or `#CALC`, fewer operands are possible for the actual parameters because not all operands can provide the required reference information. The possible operands are:

- Fields of a data source that are annotated with the required reference information.

- Scalar functions that return a value of a suitable data type and that are annotated with the required reference information.

- Path expressions that are annotated with the required reference information.

- `$projection` fields that derive their reference information from the data source.

  **Note:** Reuse expressions defined with `$projection` use their reference information, if it is specified locally. However, if a reference type can be derived from the underlying data source, the reference information is preserved and a `$projection` field can be specified as an input parameter.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity passes a field of a data source, a typed literal and an input parameter as actual parameters to the input parameters of the CDS scalar function `DEMO_CDS_SCALAR_REF_CASE`.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, scalar func'

define view entity DEMO_CDS_SCALAR_USE_REF_CASE
  with parameters
    p1 : abap.dec(4,2)
  as select from DEMO_CDS_SCALAR_HELPER
{
  key Id,
      Unit2,
      @Semantics.quantity.unitOfMeasure: 'Unit2'
      DEMO_CDS_SCALAR_REF_CASE(
      p1 => Int4,
      p2 => abap.int4'22',
      p3 => $parameters.p1) as ScalarResult
}
```
