---
title: "CDS DDL - DDIC-Based View, cast_expr"
source_file: abencds_cast_expression_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, cast_expr

## Syntax

``` abap
... CAST( operand AS dtype [PRESERVING TYPE]) ...  
```

## Description

Casting in a [`SELECT` statement](abencds_select_statement_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). The cast expression [converts](abencds_cast_expression_rules_v1.md) the value of the operand `operand` to the ABAP Dictionary type specified by `dtype`. The result has the type `dtype`. The following can be specified for `dtype`:

- A [DDIC data element](../../abap-glossary/abendata_element_glosry.md). In this case, the optional addition `PRESERVING TYPE` can be specified. If this addition is specified, the built-in data type, the length of the operand and the number of decimal places, and the target data type must match exactly.

- A built-in data type from ABAP Dictionary. The addition `PRESERVING TYPE` cannot be specified in this case. All available data types are listed in the topic [ABAP CDS - Built-In Data Types](../abap-cds-data-types/abencds_overview_builtin_types.md).

The following can be specified for `operand`:

- A [literal](abencds_literal_v1.md) without a domain prefix

- A [parameter](abencds_parameter_v1.md)

- A [session variable](abencds_session_variable_v1.md)

- A [field](abencds_field_v1.md) of a data source [`data_source`](abencds_data_source_v1.md) of the current CDS view

- An [aggregate expression](abencds_aggregate_functions_v1.md)

- A [path expression](abencds_path_expression_v1.md) that identifies a field of a data source [`data_source`](abencds_data_source_v1.md)

- A [built-in function](abencds_builtin_functions_v1.md)

- An [arithmetic expression](abencds_arithmetic_expression_v1.md)

- A case distinction with [`CASE`](abencds_case_expression_v1.md)

- A nested cast expression

Cast expressions can be specified in the [`SELECT` list](abencds_select_list_v1.md) and in operand positions of expressions.

The following table shows which combinations of built-in data types in ABAP Dictionary can currently be cast to each other and what the prerequisites are in each case. There is a special list of [conversion rules](abencds_cast_expression_rules_v1.md) for every combination.

| **from/to**      | **`INT1`** | **`INT2`** | **`INT4`** | **`INT8`** | **`DEC`** | **`CURR`** | **`QUAN`** | **`DECFLOAT16`** | **`DECFLOAT34`** | **`FLTP`** | **`CHAR`** | **`SSTRING`** | **`NUMC`** | **`DATS`** | **`TIMS`** | **`DATN`** | **`TIMN`** | **`UTCLONG`** | **`ACCP`** | **`CLNT`** | **`LANG`** | **`UNIT`** | **`CUKY`** | **`RAW`** |
|------------------|------------|------------|------------|------------|-----------|------------|------------|------------------|------------------|------------|------------|---------------|------------|------------|------------|------------|------------|---------------|------------|------------|------------|------------|------------|-----------|
| **`INT1`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | y          | y             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | x          | \-         | \-         | \-         | \-        |
| **`INT2`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | y          | y             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        |
| **`INT4`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | y          | y             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        |
| **`INT8`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | y          | y             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        |
| **`DEC`**        | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | y          | y             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        |
| **`CURR`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | y          | y             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        |
| **`QUAN`**       | x          | x          | x          | x          | x         | x          | x          | x                | x                | x          | y          | y             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        |
| **`DECFLOAT16`** | x          | x          | x          | x          | x         | x          | x          | x                | x                | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        |
| **`DECFLOAT34`** | x          | x          | x          | x          | x         | x          | x          | x                | x                | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        |
| **`FLTP`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        |
| **`CHAR`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | x          | x          | x          | \-         | \-         | \-            | p          | x          | x          | x          | x          | \-        |
| **`SSTRING`**    | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | x          | x          | x          | \-         | \-         | \-            | p          | x          | x          | x          | x          | \-        |
| **`NUMC`**       | y          | y          | y          | y          | x         | x          | x          | x                | x                | x          | x          | x             | z          | z          | z          | \-         | \-         | \-            | p          | z          | \-         | \-         | \-         | \-        |
| **`DATS`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | \-         | z          | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        |
| **`TIMS`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | x          | x             | \-         | \-         | z          | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        |
| **`DATN`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | x          | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-        |
| **`TIMN`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | \-         | x          | \-            | \-         | \-         | \-         | \-         | \-         | \-        |
| **`UTCLONG`**    | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | x             | \-         | \-         | \-         | \-         | \-         | \-        |
| **`ACCP`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | z          | z             | z          | \-         | \-         | \-         | \-         | \-            | p          | \-         | \-         | \-         | \-         | \-        |
| **`CLNT`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | d          | d             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | p          | \-         | \-         | \-         | \-        |
| **`LANG`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | d          | d             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | p          | \-         | \-         | \-        |
| **`UNIT`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | d          | d             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | p          | \-         | \-        |
| **`CUKY`**       | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | d          | d             | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | p          | \-        |
| **`RAW`**        | \-         | \-         | \-         | \-         | \-        | \-         | \-         | \-               | \-               | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | \-            | \-         | \-         | \-         | \-         | \-         | p         |

There are no further restrictions to note in combinations with *x*. The following rules apply to the other combinations:

- In combinations with *y*, the length of the target data type must be sufficient.

- In combinations with *z*, the lengths of the data types must match exactly.

- In the case of combinations with *p* or *d*, a data element must be specified as the target data type. It is not possible to specify a built-in data type from ABAP Dictionary.

  - In combinations with *d*, the data element can have a suitable target type in accordance with the table above and with any length.

  - In combinations with *p*, the data element must have the built-in data type and the same length as the data type of the operand.

In the case of incompatible types, the content of the operand is [converted](abencds_cast_expression_rules_v1.md) to the target type (exceptions can be raised if values are not suitable). In compatible types, a syntax check warning occurs (unless the target data type is specified as a data element using the addition `PRESERVING TYPE`).

## Hints

- If a data element is specified for `dtype`, the result of the expression inherits the semantic properties of the data element. An exception to this is the use of the `CAST` expression within a case distinction.

- If the addition `PRESERVING TYPE` is specified, the data type of the operand stays the same and only the semantic properties are changed.

- The characters in the [surrogate area](../../abap-glossary/abensurrogate_area_glosry.md) of the [system code page](../../abap-glossary/abensystem_codepage_glosry.md) [UTF-16](../../abap-glossary/abenutf16_glosry.md) are handled as two characters in cast expressions for strings. Care should be taken to avoid splitting these characters in truncation operations.

- When performing a [conversion](abencds_cast_expression_rules_v1.md) between [currency fields](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_currency_field.md) with type `CURR`, it should be noted that `CAST` respects the decimal places defined for the type. In ABAP applications, on the other hand, the position of the decimal point is usually ignored.

- A `CAST` expression should be platform-independent. Conversions from the type `FLTP` to other numeric types are not allowed because the result would be platform-dependent.

- An aggregate expression [`AVG`](abencds_aggregate_functions_v1.md) has the type `FLTP` by default. It can be specified as an operand but it is not possible to cast to other types. Therefore there is a separate addition for `AVG` [`AS dtype`](abencds_avg_as_v1.md).

- Special built-in [conversion functions](abencds_conversion_functions_v1.md) are available for special conversions that cannot be covered by a `CAST` expression:

  - [`FLTP_TO_DEC`](abencds_conv_func_types_v1.md) for converting `FLTP` to packed numbers.

  - [`BINTOHEX`](abencds_conv_func_types_v1.md) and [`HEXTOBIN`](abencds_conv_func_types_v1.md) for conversions of byte strings to character strings and back.

  - [Conversion functions for units and currencies](abencds_conv_func_unit_curr_v1.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Cast expressions in a `SELECT` list.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_SO_V1'
define view DEMO_CDS_SALES_ORDER_V1
  as select from snwd_so
  association [1..*] to snwd_so_i 
    as _item on snwd_so.node_key = _item.parent_key
{
  key snwd_so.node_key,
      gross_amount                                 as original_amount,
      cast(gross_amount as abap.fltp) +
        (cast( -gross_amount as abap.fltp) * 0.03) as reduced_amount,
      cast(gross_amount as abap.fltp) * 0.03       as overall_savings,
      _item.so_item_pos                            as item_position,
      _item.gross_amount                         as item_gross_amount,
      cast(_item.gross_amount as abap.fltp) * 0.97 as item_savings
}
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following view, the column `char1` of the DDIC database table `DEMO_EXPRESSIONS` is cast to the data element `demo_char_text` with the same technical properties. In this case, it is advisable to specify the addition `PRESERVING TYPE`.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_CAST_DE'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_cast_data_element
  as select from
    demo_expressions
    {
      cast ( char1 as demo_char_text preserving type)
                                    as char_with_text
    };
```

The following function module call returns the properties of the view field. The text shows that the semantic properties of the data element were applied. The column `char1` does not have its own text.

``` abap
DATA dfies_tab TYPE TABLE OF dfies. 
CALL FUNCTION 'DDIF_FIELDINFO_GET' 
  EXPORTING 
    tabname   = 'DEMO_CDS_CAST_DE' 
    fieldname = 'CHAR_WITH_TEXT' 
    langu     = sy-langu 
                TABLES 
                dfies_tab = dfies_tab. 
cl_demo_output=>display( dfies_tab[ 1 ]-fieldtext ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following view, a literal is given the technical and semantic properties of the data element `S_MANDT`.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_CSTCLNT'
@AccessControl.authorizationCheck: #NOT_REQUIRED 
define view demo_cds_cast_clnt
  as select from
    scarr
    {
      key cast ( 'XXX' as s_mandt )
          as pseudo_client,
      key carrid,
          carrname
    };
```
