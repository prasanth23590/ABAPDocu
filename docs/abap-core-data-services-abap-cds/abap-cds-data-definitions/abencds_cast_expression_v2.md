---
title: "CDS DDL - CDS View Entity, cast_expr"
source_file: abencds_cast_expression_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, cast_expr

## Syntax

``` abap
... CAST( operand AS dtype [PRESERVING TYPE]) ...  
```

## Description

Casting in a [`SELECT` statement](abencds_select_statement_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). The cast expression converts the value of the operand `operand` to the type specified by `dtype`. The result has the type `dtype`.

The following can be specified for `dtype`:

- A [CDS user-defined type](../../abap-glossary/abencds_user_defined_type_glosry.md). In this case, the optional addition `PRESERVING TYPE` can be specified.

- A [DDIC data element](../../abap-glossary/abendata_element_glosry.md). In this case, the optional addition `PRESERVING TYPE` can be specified. If this addition is specified, the built-in data type, the length of the operand and the number of decimal places, and the target data type must match exactly.

- A built-in data type from ABAP Dictionary. The addition `PRESERVING TYPE` cannot be specified in this case. All available data types are listed in the topic [ABAP CDS - Built-In Data Types](../abap-cds-data-types/abencds_overview_builtin_types.md).

The following can be specified for `operand`:

- A [literal](abencds_literal_v2.md)

- A [parameter](abencds_parameter_v2.md)

- A [session variable](abencds_session_variable_v2.md)

- A [field](abencds_field_v2.md) of a data source [`data_source`](abencds_data_source_v2.md) of the current CDS view entity

- An [aggregate expression](abencds_aggregate_functions_v2.md)

- A [path expression](abencds_path_expression_v2.md) that identifies a field of a data source [`data_source`](abencds_data_source_v2.md)

- A [built-in function](abencds_builtin_functions_v2.md)

- An [SQL-based scalar function](abencds_sql_scalar_function.md)

- An [arithmetic expression](abencds_arithmetic_expression_v2.md)

- A [case distinction](abencds_case_expression_v2.md)

- Another, nested, cast expression

Cast expressions can be specified in the [`SELECT` list](abencds_select_list_v2.md) and in operand positions of expressions.

The following table shows which combinations of built-in data types in ABAP Dictionary can currently be cast to each other and what the prerequisites are in each case. There is a special list of [conversion rules](abencds_cast_expression_rules_v2.md) for every combination.

| **from/to**      | **`INT1`** | **`INT2`** | **`INT4`** | **`INT8`** | **`DEC`** | **`CURR`** | **`QUAN`** | **`DECFLOAT16`** | **`DECFLOAT34`** | **`FLTP`** | **`CHAR`** | **`SSTRING`** | **`NUMC`** | **`DATS`** | **`TIMS`** | **`DATN`** | **`TIMN`** | **`UTCLONG`** | **`ACCP`** | **`CLNT`** | **`LANG`** | **`UNIT`** | **`CUKY`** | **`RAW`** | **`DF16_DEC`** | **`DF34_DEC`** |
|------------------|------------|------------|------------|------------|-----------|------------|------------|------------------|------------------|------------|------------|---------------|------------|------------|------------|------------|------------|---------------|------------|------------|------------|------------|------------|-----------|----------------|----------------|
| **`INT1`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | y          | y             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | x          | \-         | \-         | \-         | \-        | \-             | \-             |
| **`INT2`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | y          | y             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        | \-             | \-             |
| **`INT4`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | y          | y             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        | \-             | \-             |
| **`INT8`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | y          | y             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        | \-             | \-             |
| **`DEC`**        | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | y          | y             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        | \-             | \-             |
| **`CURR`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | y          | y             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        | \-             | \-             |
| **`QUAN`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | y          | y             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        | \-             | \-             |
| **`DECFLOAT16`** | x          | x          | x          | x          | x         | x          | x          | x                | x                | \-         | x          | \-            | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        | \-             | \-             |
| **`DECFLOAT34`** | x          | x          | x          | x          | x         | x          | x          | x                | x                | \-         | x          | \-            | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        | \-             | \-             |
| **`DF16_DEC`**   | \-         | \-         | \-         | \-         | \-        | \-         | \-         | x                | x                | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        | d              | \-             |
| **`DF34_DEC`**   | \-         | \-         | \-         | \-         | \-        | \-         | \-         | x                | x                | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        | \-             | d              |
| **`FLTP`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        | \-             | \-             |
| **`CHAR`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | \-         | x          | x             | x          | x          | x          | \-         | \-         | \-            | p          | x          | x          | x          | x          | \-        | \-             | \-             |
| **`SSTRING`**    | x          | x          | x          | x          | x         | x          | x          | x                | x                | \-         | x          | x             | x          | x          | x          | \-         | \-         | \-            | p          | x          | x          | x          | x          | \-        | \-             | \-             |
| **`NUMC`**       | y          | y          | y          | y          | x         | x          | x          | x                | x                | x          | x          | x             | z          | z          | z          | \-         | \-         | \-            | p          | z          | \-         | \-         | \-         | \-        | \-             | \-             |
| **`DATS`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | \-         | x          | x             | \-         | z          | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        | \-             | \-             |
| **`TIMS`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | \-         | x          | x             | \-         | \-         | z          | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        | \-             | \-             |
| **`DATN`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        | \-             | \-             |
| **`TIMN`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | \-         | x          | \-            | \-         | \-         | \-         | \-         | \-         | \-        | \-             | \-             |
| **`UTCLONG`**    | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | x             | \-         | \-         | \-         | \-         | \-         | \-        | \-             | \-             |
| **`ACCP`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | z          | z             | z          | \-         | \-         | \-         | \-         | \-            | p          | \-         | \-         | \-         | \-         | \-        | \-             | \-             |
| **`CLNT`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | d          | d             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | p          | \-         | \-         | \-         | \-        | \-             | \-             |
| **`LANG`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | d          | d             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | p          | \-         | \-         | \-        | \-             | \-             |
| **`UNIT`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | d          | d             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | p          | \-         | \-        | \-             | \-             |
| **`CUKY`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | d          | d             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | p          | \-        | \-             | \-             |
| **`RAW`**        | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | p         | \-             | \-             |

There are no further restrictions to note in combinations with *x*. The following rules apply to the other combinations:

- In combinations with *y*, the length of the target data type must be sufficient.

- In combinations with *z*, the lengths of the data types must match exactly.

- In the case of combinations with *p* or *d*, a CDS user-defined type or a data element must be specified as the target data type. It is not possible to specify a built-in data type from ABAP Dictionary.

  - In combinations with *d*, the CDS user-defined type or the data element can have a suitable target type in accordance with the table above and with any length.

  - In combinations with *p*, the CDS user-defined type or the data element must have the built-in data type and the same length as the data type of the operand.

In the case of incompatible types, the content of the operand is converted to the target type (exceptions can be raised if values are not suitable). For compatible types, a syntax check warning occurs (unless the target data type is specified as a CDS user-defined type or as a data element using the addition `PRESERVING TYPE`).

If the operand of a cast expression has the [null value](../../abap-glossary/abennull_value_glosry.md), the result of the expression is also the null value.

If the target type `dtype` is specified as `CURR` or `QUAN`, then a [`Semantics` reference annotation](abencds_f1_element_annotation.md) specifying a currency key or unit key is mandatory.

When casting to a [CDS enumerated type](../../abap-glossary/abencds_enum_type_glosry.md), the operand of the cast expression must be compatible with the [base type](../../abap-glossary/abenbase_type_glosry.md) of the CDS enumerated type. The cast matrix and the conversion rules for casting apply with respect to the base type.

## Hints

- If a CDS user-defined type is specified for `dtype`, the result of the expression inherits the semantic properties of the CDS user-defined type in question.

- If a data element is specified for `dtype`, the result of the expression inherits the semantic properties of the data element. An exception to this is the use of the `CAST` expression within a case distinction.

- If `operand` and `dtype` have the same data type and the same length, a syntax check warning occurs. This syntax check warning can be suppressed using the addition `PRESERVING TYPE`. If `dtype` is a CDS type or a data element and the addition `PRESERVING TYPE` is not available, the warning can be ignored. It is currently not possible to suppress the warning.

- If the addition `PRESERVING TYPE` is specified, the data type of the operand stays the same and only the semantic properties are changed.

- The characters in the [surrogate area](../../abap-glossary/abensurrogate_area_glosry.md) of the [system code page](../../abap-glossary/abensystem_codepage_glosry.md) [UTF-16](../../abap-glossary/abenutf16_glosry.md) are handled as two characters in cast expressions for strings. Care should be taken to avoid splitting these characters in truncation operations.

- When performing a conversion between [currency fields](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_currency_field.md) with type `CURR`, it should be noted that `CAST` respects the decimal places defined for the type. In ABAP applications, on the other hand, the position of the decimal point is usually ignored.

- A `CAST` expression should be platform-independent. Conversions from the type `FLTP` to other numeric types are not allowed because the result would be platform-dependent.

- Special built-in [conversion functions](abencds_conversion_functions_v2.md) are available for conversions that cannot be covered by a `CAST` expression:

  - [`FLTP_TO_DEC`](abencds_conv_func_types_v2.md) for converting `FLTP` to packed numbers.

  - [`BINTOHEX`](abencds_conv_func_types_v2.md) and [`HEXTOBIN`](abencds_conv_func_types_v2.md) for conversions of byte strings to character strings and back.

  - [Conversion functions for units and currencies](abencds_conv_func_unit_curr_v2.md)

  - [Conversion functions for dates, times, and time stamps](abencds_date_time_conversions_v2.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Cast expressions in a `SELECT` list.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_SALES_CDS_SO_CAST
  as select from
    DEMO_SALES_CDS_SO
    association to DEMO_SALES_CDS_SO_I as _item
      on DEMO_SALES_CDS_SO.so_key = _item.so_item_key
    {
      key so_key,
          currency_sum,
          @Semantics.amount.currencyCode: 'currency_sum'
          amount_sum                                   as original_amount,
          cast(amount_sum as abap.fltp) -
          (cast(amount_sum as abap.fltp) * 0.03)       as reduced_amount,
          cast(amount_sum as abap.fltp) * 0.03         as overall_savings,
          _item.currency,
          _item.posnr                                  as item_position,
          @Semantics.amount.currencyCode: 'currency'
          _item.gross_amount                           as item_amount,
          cast(_item.gross_amount as abap.fltp) * 0.97 as item_savings
    }
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following view entity, the column `char1` of the DDIC database table `DEMO_EXPRESSIONS` is cast to the simple type `DEMO_BT_CHAR_TEXT` with the same technical properties. In this case, it is advisable to specify the addition `PRESERVING TYPE`.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_CAST_SIMPLE_TYPE_VE
  as select from demo_expressions
{
  cast ( char1 as DEMO_BT_CHAR_TEXT preserving type)
                                as char_with_text
};
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following view, a literal is given the technical and semantic properties of the simple type `DEMO_BT_MANDT`.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_CAST_CLNT_VE
  as select from scarr
{
  key cast ( 'XXX' as s_mandt ) as pseudo_client,
  key carrid,
      carrname
}
```
