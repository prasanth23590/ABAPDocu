---
title: "CDS DDL - CDS View Entity, Coalesce Function"
source_file: abencds_coalesce_expression_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Expressions > CDS DDL - CDS View Entity, Built-In Functions > CDS DDL - CDS View Entity, sql_functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, Coalesce Function

## Syntax

``` abap
... COALESCE( arg1, arg2 ) ...  
```

## Description

[Coalesce function](../../abap-glossary/abencoalesce_glosry.md) in a [`SELECT` statement](abencds_select_statement_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). Can be used to check whether `arg1` contains a [null value](../../abap-glossary/abennull_value_glosry.md). In ABAP CDS, the coalesce function has two mandatory [positional parameters](../../abap-glossary/abenpositional_parameter_glosry.md) for arguments `arg1` and `arg2`. It checks whether `arg1` contains a null value. If yes, then it returns the value of `arg2`. If no, then it returns the value of `arg1`. If both `arg1` and `arg2` are null, then the null value is returned.

The following can be specified as the arguments `arg`:

- [Literals](abencds_literal_v2.md) of a suitable type.

- Suitable [fields](abencds_field_v2.md) of a data source [`data_source`](abencds_data_source_v2.md) of the current CDS view entity.

- [Path expressions](abencds_path_expression_v2.md) that identify a suitable field of a data source [`data_source`](abencds_data_source_v2.md).

- [Input parameters](abencds_parameter_v2.md) from the parameter list [`parameter_list`](abencds_parameter_list_v2.md).

- [Reuse expressions](abencds_reusable_expression_v2.md) using `$projection`

- [SQL-based scalar functions](abencds_sql_scalar_function.md) (if they return a matching type)

- The following built-in functions and expressions (if they return a matching type):

  - Other built-in [SQL functions](abencds_sql_functions_v2.md)

  - [Arithmetic expressions](abencds_arithmetic_expression_v2.md)

  - Type modifications using [`CAST`](abencds_cast_expression_v2.md)

The valid argument types for `arg1` and `arg2` are all [dictionary types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) except `ACCP`, `DF16_DEC`, `DF34_DEC`, `DF16_RAW`, `DF34_RAW`, `LCHR`, `LRAW`, `PREC`, `RAWSTRING`, `STRING`, and `GEOM_EWKB`.

The data types of both arguments must either be the same or the data type of one argument must represent the value of the other data type. The result has the dictionary type of the argument with the largest value range.

**Rules for Amounts and Quantities**

The arguments of a coalesce function can be [CDS amount fields](../../abap-glossary/abencds_amount_field_glosry.md), [CDS quantity fields](../../abap-glossary/abencds_quantity_glosry.md), or [CDS calculated quantities](../../abap-glossary/abencds_calculated_quantity_glosry.md). The following table shows how the result data type is calculated if one or more of the arguments are amount and/or quantity fields.

| **`arg1/arg2`**         | **Amount**          | \*\* Quantity\*\*   | \*\* Calculated Quantity\*\* | **Number**          |
|-------------------------|---------------------|---------------------|------------------------------|---------------------|
| **Amount**              | Amount              | Calculated Quantity | Calculated Quantity          | Calculated Quantity |
| **Quantity**            | Calculated Quantity | Quantity            | Calculated Quantity          | Calculated Quantity |
| **Calculated Quantity** | Calculated quantity | Calculated quantity | Calculated Quantity          | Calculated Quantity |
| **Number**              | Calculated Quantity | Calculated quantity | Calculated Quantity          | Number              |

- If the result is an amount or quantity field, a reference annotation must be assigned.

- It is not mandatory that the arguments and the result point to the same reference field.

- The following rules apply to amount fields of data type `CURR`:

  - Fields of data type `CURR` are compatible only to other amount fields of data type `CURR` and only if they have exactly the same number of decimal places.

  - To combine an amount field of data type `CURR` with a field of another data type, a conversion to data type `DECFLOAT34` using the conversion function [`CURR_TO_DECFLOAT_AMOUNT`](abencds_conv_func_unit_curr_v2.md) is required.

## Hint

The coalesce function is a short form of the following [complex case distinction](abencds_searched_case_expr_v2.md):

``` abap
CASE WHEN arg1 IS NOT NULL THEN arg1 
     ELSE arg2 
END
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity demonstrates the syntax of the coalesce function.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_COALESCE 
as select from demo_ddic_types 
{
  key id,
  coalesce(int1, int2) as coalesced
}
```
