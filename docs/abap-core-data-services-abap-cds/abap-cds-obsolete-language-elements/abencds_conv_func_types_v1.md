---
title: "CDS DDL - DDIC-Based View, Type Conversion Functions"
source_file: abencds_conv_func_types_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Operands and Expressions > CDS DDL - DDIC-Based View, Expressions > CDS DDL - DDIC-Based View, Built-In Functions > CDS DDL - DDIC-Based View, Special Functions > CDS DDL - DDIC-Based View, Conversion Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, Type Conversion Functions

## Syntax

``` abap
... FLTP_TO_DEC( arg AS dtype ) ...   
... BINTOHEX( arg ) ...   
... HEXTOBIN( arg ) ...  
```

### Variant

[1. `... FLTP_TO_DEC( arg AS dtype )`](abencds_conv_func_types_v1.md#variant-1)

[2a. `... BINTOHEX( arg )`](abencds_conv_func_types_v1.md#variant-2a)

[2b. `... HEXTOBIN( arg )`](abencds_conv_func_types_v1.md#variant-2b)

## Overview

### Description

Functions for conversions between data types in a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md).

### Hints

- These functions execute special conversions that cannot be handled in a general [`CAST`](abencds_cast_expression_v1.md) expression.

- If an argument has the [null value](../../abap-glossary/abennull_value_glosry.md), the result of the conversion function is also the null value.

## Variant 1

`... FLTP_TO_DEC( arg AS dtype )`

### Description

Conversion of an argument `arg` of type [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) to a packed number. [Literals](abencds_literal_v1.md), [fields](abencds_field_v1.md) of a data source [`data_source`](abencds_data_source_v1.md), and [path expressions](abencds_path_expression_v1.md) can be specified for `arg`. `arg` must have the type [`FLTP`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

A target data type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) must be specified with `dtype` for a packed number, as follows:

- Using a [DDIC data element](../../abap-glossary/abendata_element_glosry.md) with this type.

- Directly as a [built-in data type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) in ABAP Dictionary.

The following table shows the syntax for specifying built-in data types:

| **dtype**                 | **Dictionary Type**                                                                    |
|---------------------------|----------------------------------------------------------------------------------------|
| `abap.dec(len,decimals)`  | [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length `len` and `decimals` decimal places   |
| `abap.curr(len,decimals)` | [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length `len` and `decimals` decimal places  |
| `abap.quan(len,decimals)` | [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length `len` with `decimals` decimal places |

The value range of the data type `dtype` must cover the value range of the operand type. An exception occurs if the value range of the target data type is not sufficient. Any surplus decimal places are cut off without rounding.

### Hints

- The conversion of type `FLTP` to a packed number using the function `FLTP_TO_DEC` is platform dependent and does not have to be reversible using a [`CAST`](abencds_cast_expression_v1.md).

- The general [`CAST`](abencds_cast_expression_v1.md) is designed to be platform-independent, which means it does not allow conversions of type `FLTP` to other numeric data types.

- Since a literal with a prefixed sign is interpreted as an arithmetic expression, the argument `arg` of the function `FLTP_TO_DEC` cannot be a negative literal. Instead, the sign can usually be specified before the function.

- More specifically, the built-in conversion function `FLTP_TO_DEC` can be used to convert literals with a decimal point to a packed number.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view applies the function `FLTP_TO_DEC` in the `SELECT` list to columns of the DDIC database table `DEMO_EXPRESSIONS`. The class `CL_DEMO_CDS_FLTP_TO_DEC` uses `SELECT` to access the view. Note that there is no rounding.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_FLTPDEC'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_fltp_to_dec
  as select from
    demo_expressions
    {
      fltp_to_dec( fltp1 as abap.dec(10,0) ) as dec1_10_0,
      fltp_to_dec( fltp1 as abap.dec(10,3) ) as dec1_10_3,
      fltp_to_dec( fltp2 as abap.dec(10,0) ) as dec2_10_0,
      fltp_to_dec( fltp2 as abap.dec(10,3) ) as dec2_10_3
    } 
```

## Variant 2a

`... BINTOHEX( arg )`

## Variant 2b

`... HEXTOBIN( arg )`

### Description

The functions `BINTOHEX` and `HEXTOBIN` convert byte strings to character strings and back:

- `BINTOHEX` takes a byte string and converts it to a character string containing the half bytes of `arg`, converted to the hexadecimal characters *0* to *9* and *A* to *F* (left-aligned). The valid argument type is [`RAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with a maximum length of 255. The result has the type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with twice the length of `arg`. Only fields of data sources can be specified as arguments.

- `HEXTOBIN` converts a character string to a byte string whose half bytes are determined from the hexadecimal characters of `arg`. Any leading blanks are removed before the conversion from `arg` and all trailing blanks are then replaced by *0*. The valid argument types are is [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`NUMC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with a maximum length of 510. The result has the type [`RAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with half the length of `arg`. Only fields of data sources and literals can be specified as arguments. The total of all characters must be even and it can contain only the hexadecimal characters *0* to *9* and *A* to *F* (uppercase or lowercase) and leading and trailing blanks. Literals cannot contain any leading blanks.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view applies the conversion functions for byte strings in the `SELECT` list to columns of the DDIC database table `DEMO_EXPRESSIONS`. The class `CL_DEMO_CDS_SQL_FUNCTIONS_BYTE` uses `SELECT` to access the view.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_BINFUNC'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_sql_functions_byte
  as select from demo_expressions
{
  bintohex(  raw1  ) as r_bintohex,
  hextobin(  char1 ) as r_hextobin
}
```
