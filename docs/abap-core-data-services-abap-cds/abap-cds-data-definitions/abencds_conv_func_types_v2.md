---
title: "CDS DDL - CDS View Entity, Type Conversion Functions"
source_file: abencds_conv_func_types_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Expressions > CDS DDL - CDS View Entity, Built-In Functions > CDS DDL - CDS View Entity, Special Functions > CDS DDL - CDS View Entity, Conversion Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, Type Conversion Functions

## Syntax

``` abap
... FLTP_TO_DEC( arg AS dtype ) ...   
... BINTOHEX( arg ) ...   
... HEXTOBIN( arg ) ...  
```

### Variant

[1. `... FLTP_TO_DEC( arg AS dtype )`](abencds_conv_func_types_v2.md#variant-1)

[2a. `... BINTOHEX( arg )`](abencds_conv_func_types_v2.md#variant-2a)

[2b. `... HEXTOBIN( arg )`](abencds_conv_func_types_v2.md#variant-2b)

## Overview

### Description

Functions for conversions between data types in a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md).

### Hints

- These functions execute special conversions that cannot be handled in a general [`CAST`](abencds_cast_expression_v2.md) expression.

- If an argument has the [null value](../../abap-glossary/abennull_value_glosry.md), the result of the conversion function is also the null value.

## Variant 1

`... FLTP_TO_DEC( arg AS dtype )`

### Description

Conversion of an argument `arg` of type [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) to a packed number. [Literals](abencds_literal_v2.md), [fields](abencds_field_v2.md) of a data source [`data_source`](abencds_data_source_v2.md), and [path expressions](abencds_path_expression_v2.md) can be specified for `arg`. `arg` must have the type [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

A target data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) must be specified with `dtype` for a packed number, as follows:

- Using a [CDS simple type](../../abap-glossary/abencds_simple_type_glosry.md) or a [DDIC data element](../../abap-glossary/abendata_element_glosry.md) with this type.

- Directly as a [built-in data type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) in ABAP Dictionary.

The following table shows the syntax for specifying built-in data types:

<table>
<thead>
<tr class="header">
<th><strong>dtype</strong></th>
<th><strong>Dictionary Type</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">abap.dec(len,decimals)</code></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">DEC</code></a> with length <code class="ph codeph">len</code> and <code class="ph codeph">decimals</code> decimal places</td>
</tr>
<tr class="even">
<td><code class="ph codeph">abap.curr(len,decimals)</code></td>
<td><p><a href="abenddic_builtin_types.html"><code class="ph codeph">CURR</code></a> with length <code class="ph codeph">len</code> and <code class="ph codeph">decimals</code> decimal places</p>
<p><strong>Note:</strong> The only valid value for <code class="ph codeph">decimals</code> is <em>2</em>.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">abap.quan(len,decimals)</code></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">QUAN</code></a> with length <code class="ph codeph">len</code> with <code class="ph codeph">decimals</code> decimal places</td>
</tr>
</tbody>
</table>

The value range of the data type `dtype` must cover the value range of the operand type. An exception occurs if the value range of the target data type is not sufficient. Any surplus decimal places are cut off without rounding.

### Hints

- If `arg` is assigned a currency key using the annotation [`Semantics.amount.currencyCode`](abencds_f1_element_annotation.md), then the result field must also be assigned a currency key using the same annotation.

- If `arg` is assigned a unit of measurement key using the annotation [`Semantics.quantity.unitofMeasure`](abencds_f1_element_annotation.md), then the result field must also be assigned a unit of measurement key using the same annotation.

- The conversion of type `FLTP` to a packed number using the function `FLTP_TO_DEC` is platform dependent and does not have to be reversible using a [`CAST`](abencds_cast_expression_v2.md).

- The general [`CAST`](abencds_cast_expression_v2.md) is designed to be platform-independent, which means it does not allow conversions of type `FLTP` to other numeric data types.

- Since a literal with a prefixed sign is interpreted as an arithmetic expression, the argument `arg` of the function `FLTP_TO_DEC` cannot be a negative literal. Instead, the sign can usually be specified before the function.

- The built-in conversion function `FLTP_TO_DEC` is especially useful for converting literals with a decimal point to a packed number.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity applies the function `FLTP_TO_DEC` in the `SELECT` list to columns of the DDIC database table `DEMO_EXPRESSIONS`. The class `CL_DEMO_CDS_FLTP_TO_DEC_VE` uses `SELECT` to access the view. Note that there is no rounding.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_FLTP_TO_DEC_VE
  as select from demo_expressions
  association to demo_ddic_types as _a
    on demo_expressions.id = _a.id
  {
    _a.cuky                                 as currencyCode,
    _a.unit3                                as unitOfMeasure,
    fltp_to_dec( fltp1 as abap.dec(10,0) )  as dec1_10_0,
    fltp_to_dec( fltp1 as abap.dec(10,3) )  as dec1_10_3,
    @Semantics.amount.currencyCode: 'currencyCode'
    fltp_to_dec( fltp2 as abap.curr(10,2) ) as curr_10_2,
    @Semantics.quantity.unitOfMeasure: 'unitOfMeasure'
    fltp_to_dec( fltp2 as abap.quan(10,3) ) as quan_10_3
  }
```

## Variant 2a

`... BINTOHEX( arg )`

## Variant 2b

`... HEXTOBIN( arg )`

### Description

The functions `BINTOHEX` and `HEXTOBIN` convert byte strings to character strings and back:

- `BINTOHEX` takes a byte string and converts it to a character string containing the half bytes of `arg`, converted to the hexadecimal characters *0* to *9* and *A* to *F* (left-aligned). The valid argument type is [`RAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with a maximum length of 255. The result has the type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with twice the length of `arg`. Only fields of data sources can be specified as arguments.

- `HEXTOBIN` converts a character string to a byte string whose half bytes are determined from the hexadecimal characters of `arg`. Any leading blanks are removed before the conversion from `arg` and all trailing blanks are then replaced by *0*. The valid argument types are is [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`NUMC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with a maximum length of 510. The result has the type [`RAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with half the length of `arg`. Fields of data sources, path expressions, and literals can be specified as arguments. The total of all characters must be even and it can contain only the hexadecimal characters *0* to *9* and *A* to *F* (uppercase or lowercase) and leading and trailing blanks. Literals cannot contain any leading blanks.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity applies the conversion functions for byte strings in the `SELECT` list to columns of the DDIC database table `DEMO_EXPRESSIONS`. The class `CL_DEMO_CDS_SQL_FNCTNS_BYTE_VE` uses `SELECT` to access the view.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_SQL_FUNCTIONS_BYTE_VE
  as select from demo_expressions
{
  bintohex(  raw1  ) as r_bintohex,
  hextobin(  char1 ) as r_hextobin
}
```
