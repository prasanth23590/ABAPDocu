---
title: "sql_func - Type Conversion Functions"
source_file: abensql_type_conv_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_func > ABAP SQL - Built-In Functions sql_func > sql_func - Special Functions > sql_func - Conversion Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_func - Type Conversion Functions

## Syntax

``` abap
... BINTOHEX( sql_exp ) 
  | HEXTOBIN( sql_exp ) 
  | TO_CLOB( sql_exp ) 
  | TO_BLOB( sql_exp ) ...  
```

### Variant

[1a. `... BINTOHEX( sql_exp )`](abensql_type_conv_func.md#variant-1a)

[1b. `... HEXTOBIN( sql_exp )`](abensql_type_conv_func.md#variant-1b)

[2a. `... TO_CLOB( sql_exp )`](abensql_type_conv_func.md#variant-2a)

[2b. `... TO_BLOB( sql_exp )`](abensql_type_conv_func.md#variant-2b)

## Overview

### Description

Functions for conversions between data types in an ABAP SQL statement.

### Hints

- These SQL functions execute special conversions that cannot be handled in a general [`CAST`](abensql_cast.md) expression.

## Variant 1a

`... BINTOHEX( sql_exp )`

## Variant 1b

`... HEXTOBIN( sql_exp )`

### Description

The `BINTOHEX` and `HEXTOBIN` functions convert byte strings to character strings and vice versa. The argument `sql_exp` can be an [SQL expression](abapsql_expr.md), where literals are only possible to a limited extend:

- `BINTOHEX` takes a byte string and converts it to a character string that contains the half bytes of the value of `sql_exp` converted to the hexadecimal characters *0* to *9* and *A* to *F* left justified. The valid argument type is [`RAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with a maximum length of 255. The result has the type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with twice the length of the value of `sql_exp`.

- `HEXTOBIN` converts a character string to a byte string whose half bytes are determined from the hexadecimal characters of the value of `sql_exp`. Any leading blanks are removed before the conversion from the value of `sql_exp` and all trailing blanks are then replaced by *0*. The valid argument types are [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`NUMC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with a maximum length of 510. The result has the type [`RAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with half the length of the value of `sql_exp`. The number of characters in the argument must be even and can contain only the hexadecimal characters *0* to *9* and *A* to *F* in uppercase or lowercase and leading and trailing blanks. Character-like literals can be specified. If literals, host variables, or host expressions determine the argument directly, and not as part of a larger SQL expression, they cannot contain any leading blanks.

If the argument has a [null value](../../abap-glossary/abennull_value_glosry.md), the result of the entire conversion function is the null value.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The `ID` column of the DDIC database table `IWREFERENC` contains 32-character character-like [UUIDs](../../abap-glossary/abenuuid_glosry.md) in hexadecimal representation. The statement `SELECT` reads a UUID once directly and once as the result of the built-in function `HEXTOBIN`. The function produces the same result as a conversion using the class `CL_SYSTEM_UUID`. Of course, in ABAP the simple assignment `uuid16 = wa-uuid32` would be possible instead of the method call, since the [conversion](../abap-processing-internal-data/abenconversion_type_c.md) of `c` to `x` has the same result.

``` abap
SELECT SINGLE id AS uuid32, hextobin( id ) AS uuid16 
       FROM iwreferenc 
       WHERE tcode = 'SE38' 
       INTO @FINAL(wa). 
 
IF sy-subrc = 0. 
  TRY. 
      DATA uuid16 LIKE wa-uuid16. 
      cl_system_uuid=>convert_uuid_c32_static( 
        EXPORTING 
          uuid          =     wa-uuid32 
        IMPORTING 
          uuid_x16      =     uuid16 ). 
      ASSERT wa-uuid16 = uuid16. 
    CATCH cx_uuid_error. 
      ... 
  ENDTRY. 
ENDIF.
```

## Variant 2a

`... TO_CLOB( sql_exp )`

### Description

The `TO_CLOB` function converts the value of the operand `sql_exp` from a character string of fixed length of type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`SSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) to a [CLOB](../../abap-glossary/abenclob_glosry.md) of type [`STRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The argument `sql_exp` can be a [column](abenabap_sql_columns.md), a [literal](abenabap_sql_literals.md), a [host variable](abenabap_sql_host_variables.md), a [host constant](../../abap-glossary/abenhost_variable_glosry.md), or an [SQL expression](abapsql_expr.md). The data type of the argument must be [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) or [`SSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The result is a [CLOB](../../abap-glossary/abenclob_glosry.md) of type [`STRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

If the argument has a [null value](../../abap-glossary/abennull_value_glosry.md), the result of the conversion function is the null value.

### Hints

- After the conversion, [streaming and locators](abenstreams_locators.md) can be used on the result and length restrictions can be avoided. For example, when using `STRING_AGG` in combination with `TO_CLOB`, it is possible to read data strings that are much greater than the strings that can be read with `STRING_AGG` alone.

- When using [streaming and locators](abenstreams_locators.md) in combination with the conversion function `TO_CLOB`, it is not allowed to use [LOB interfaces](abenlob_interfaces.md) and the addition [`CREATING`](abapselect_creating.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The `SELECT`-statement reads the value of column `CHAR10` from the DDIC database table `DEMO_DDIC_TYPES` and converts it from type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) to a [CLOB](../../abap-glossary/abenclob_glosry.md) of type [`STRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). Then, a reader stream is created that reads the [CLOB](../../abap-glossary/abenclob_glosry.md) in chunks of two characters and returns a list of 2-digit numbers.

``` abap
DELETE FROM demo_ddic_types. 
INSERT demo_ddic_types 
  FROM @( VALUE #( id = 'X' char10 = '0123456789' ) ). 
 
DATA reader TYPE REF TO cl_abap_db_c_reader. 
 
SELECT SINGLE to_clob( char10 ) AS clob 
       FROM demo_ddic_types 
       WHERE id = 'X' 
       INTO @reader. 
 
DO. 
  cl_demo_output=>write( reader->read( 2 ) ). 
  IF NOT reader->data_available( ). 
    EXIT. 
  ENDIF. 
ENDDO. 
 
cl_demo_output=>display( ).
```

## Variant 2b

`... TO_BLOB( sql_exp )`

### Description

The `TO_BLOB` function converts the value of the operand `sql_exp` from a byte field of type [`RAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) to a byte string [(BLOB)](../../abap-glossary/abenblob_glosry.md) of type [`RAWSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The argument `sql_exp` can be a [column](abenabap_sql_columns.md), a [literal](abenabap_sql_literals.md), a [host variable](abenabap_sql_host_variables.md), a [host constant](../../abap-glossary/abenhost_variable_glosry.md), or an [SQL expression](abapsql_expr.md). The data type of the argument must be [`RAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). The result is a [BLOB](../../abap-glossary/abenblob_glosry.md) of type [`RAWSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

If the argument has a [null value](../../abap-glossary/abennull_value_glosry.md), the result of the entire conversion function is the null value.

### Hints

- After the conversion, [streaming and locators](abenstreams_locators.md) can be used on the result and possible length restrictions can be avoided.

- When using [streaming and locators](abenstreams_locators.md) in combination with the conversion function `TO_BLOB`, [LOB interfaces](abenlob_interfaces.md) and the addition [`CREATING`](abapselect_creating.md) cannot be used.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A variable of the built-in ABAP type [`x`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md), which maps to the ABAP Dictionary type [`RAWSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), is inserted into a database field, which requires type [`RAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), which maps to the ABAP type [`xstring`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md), using the conversion function `TO_BLOB`.

``` abap
DATA raw_value TYPE x LENGTH 255 VALUE '41424344'. 
 
DELETE FROM demo_ddic_types. 
INSERT demo_ddic_types FROM @( VALUE #( id = 1 raw10 = raw_value ) ). 
SELECT SINGLE 
       to_blob( raw10 ) AS blob 
       FROM demo_ddic_types 
       WHERE id = 1 
       INTO @FINAL(result).
```
