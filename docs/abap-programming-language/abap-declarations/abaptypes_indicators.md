---
title: "TYPES, INDICATORS"
source_file: abaptypes_indicators.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPES, INDICATORS

## Syntax

``` abap
TYPES dtype TYPE struct WITH INDICATORS ind [{TYPE type} 
                                          | {AS BITFIELD}].  
```

### Addition

[1. `... TYPE type`](abaptypes_indicators.md#addition-1)

[2. `... AS BITFIELD`](abaptypes_indicators.md#addition-2)

## Overview

### Description

Derivation of a structured data type with an [indicator structure](../../abap-glossary/abenindicator_structure_glosry.md) with the name `ind`. For `struct`, an existing local or global [structured type](../../abap-glossary/abenstructured_type_glosry.md) must be specified. For `ind`, a name must be specified that follows the [naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md).

This variant of the statement [`TYPES`](abaptypes.md) defines a structured data type that has the same components as the structured type `struct` specified behind `TYPE`, as well as an additional last component named `ind` as an indicator structure. The last component `ind` is one of the following:

- An actual [indicator structure](../../abap-glossary/abenindicator_structure_glosry.md) realized by a [substructure](../../abap-glossary/abensubstructure_glosry.md) that contains the same number of first-level components as `struct`, in the same order as in `struct` and with the same names as in `struct`. The data type of each component is `x` of length 1 by default and can be defined explicitly with the optional addition `TYPE`.

- A [condensed indicator structure](../../abap-glossary/abencondensed_ind_structure_glosry.md) realized by a [byte field](../../abap-glossary/abenbyte_field_glosry.md) of type `x` with enough bits for each component of `struct`. A condensed indicator structure is defined with the addition `AS BITFIELD`.

### Hints

- The main purpose of an indicator structure is to serve as an [ABAP SQL indicator](../../abap-glossary/abenabap_sql_indicator_glosry.md). The addition `WITH INDICATORS` facilitates the definition of [null indicators](../../abap-glossary/abennull_indicator_glosry.md) or [set indicators](../../abap-glossary/abenset_indicator_glosry.md) for ABAP SQL statements. This is especially important for the [`UPDATE`](../abap-database-access/abapupdate.md) statement with the addition [`INDICATORS`](../abap-database-access/abapupdate_set_indicator.md), since no inline declarations can be used there. Only actual indicator structures can be used with `UPDATE` and no condensed indicator structures.

- The components of an actual indicator structure are created for each first-level component of `struct` independent of its type. This means that substructures, reference variables or tabular components of `struct` are handled in the same way as elementary components and are mirrored by one indicator of type `x` or the type defined with addition `TYPE`. Likewise, each component of `struct` is represented by a single bit of a condensed indicator structure independent from its type.

- It is recommended that you use a non-nested base type since `WITH INDICATORS` does not create nested structures. A syntax warning appears, which can be suppressed using the pragma `BAD_INDICATOR_STRUCT`. In case of nested structures, explicitly model the desired indicator structure and remove the `WITH INDICATORS` addition.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The structured type `ind_struct` has the same components with the same types as `struct` plus an additional substructure named `ind`. The substructure `ind` has the same components `col1` to `col10` as `struct` but all of them have type `x` of length 1.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF struct, 
    col1  TYPE i, 
    col2  TYPE i, 
    col3  TYPE i, 
    col4  TYPE i, 
    col5  TYPE i, 
    col6  TYPE i, 
    col7  TYPE i, 
    col8  TYPE i, 
    col9  TYPE REF TO i, 
    col10 TYPE TABLE OF demo_struc WITH EMPTY KEY, 
  END OF struct. 
 
TYPES ind_struct TYPE struct WITH INDICATORS ind. 
 
DATA ind_struct TYPE ind_struct. 
 
out->write( ind_struct ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

An internal table that has a line structure with an indicator structure is partly filled with today's flight data for a given flight connection from the DDIC database table `SFLIGHT`. In the internal table, the price is reduced by 80 %. The modified table is used to update the respective date in the database table. While the lines that are to be updated are selected by the content of key fields in the internal table, the column to be updated is indicated by marking the column `PRICE` of the indicator structure. Without using the [`INDICATORS`](../abap-database-access/abapupdate_set_indicator.md) addition of the [`UPDATE`](../abap-database-access/abapupdate.md) statement, all other non-key columns of the database table would be initialized since their values are initial in the internal table.

``` abap
TYPES wa TYPE sflight WITH INDICATORS ind. 
 
DATA itab TYPE TABLE OF wa WITH EMPTY KEY. 
 
SELECT carrid, connid, fldate, price 
       FROM sflight 
       WHERE carrid = char`LH` AND 
             connid = numc`0400` AND 
             fldate = @( cl_demo_date_time=>get_user_date( ) ) 
       INTO CORRESPONDING FIELDS OF TABLE @itab. 
 
IF sy-subrc  = 0. 
 
  LOOP AT itab ASSIGNING FIELD-SYMBOL(<wa>). 
    <wa>-price *= '0.8'. 
    <wa>-ind-price = '01'. 
  ENDLOOP. 
 
  UPDATE sflight FROM TABLE @itab INDICATORS SET STRUCTURE ind. 
 
ENDIF.
```

## Addition 1

`... TYPE type`

### Description

Definition of the data type of each component of an actual [indicator structure](../../abap-glossary/abenindicator_structure_glosry.md) `ind`. The same applies to `type` as to [`TYPES ... TYPE abap_type`](abaptypes_simple.md) and [`TYPES ... TYPE`](abaptypes_referring.md). Each non-generic local or global data type that is visible at the current position can be specified. The generic built-in ABAP types `c`, `n`, `p`, and `x` can also be specified and their [standard length](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) is used implicitly then,.

### Hint

For [ABAP SQL indicators](../../abap-glossary/abenabap_sql_indicator_glosry.md), only the types `c` and `x` of length 1 are relevant.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The structured type `ind_struct` has the same components with the same types as `struct` plus an additional substructure named `ind`. The substructure `ind` has the same components `col1` to `col10` as `struct` but all of them have type `itab` that is a table type with line type `i`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF struct, 
    col1  TYPE i, 
    col2  TYPE i, 
    col3  TYPE i, 
    col4  TYPE i, 
    col5  TYPE i, 
    col6  TYPE i, 
    col7  TYPE i, 
    col8  TYPE i, 
    col9  TYPE REF TO i, 
    col10 TYPE TABLE OF demo_struc WITH EMPTY KEY, 
  END OF struct. 
 
TYPES itab TYPE TABLE OF i WITH EMPTY KEY. 
TYPES ind_struct TYPE struct WITH INDICATORS ind TYPE itab. 
 
DATA ind_struct TYPE ind_struct. 
 
out->write( ind_struct ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

See examples for [`UPDATE ... FROM ... INDICATORS`](../abap-database-access/abapupdate_set_indicator.md).

## Addition 2

`... AS BITFIELD`

### Description

Defines `ind` as a [condensed indicator structure](../../abap-glossary/abencondensed_ind_structure_glosry.md) that is a [byte field](../../abap-glossary/abenbyte_field_glosry.md) of type `x`. The length of the byte field is calculated from the number of components `n` in `struct` as with ( n + 7 ) [`DIV`](../abap-processing-internal-data/abenarith_operators.md) 8.

### Hints

- The length of `ind` is derived in such a way that it contains enough bits to serve as indicators for the components of `struct`. The first bit should serve as indicator for the first component, the second bit should serve as indicator for the second component and so on.

- The bits can be set by function [`bit-set`](../abap-processing-internal-data/abenbit_functions.md), statement [`SET BIT`](../abap-processing-internal-data/abapset_bit.md) or more commonly by ABAP SQL statements using [`INDICATORS BITFIELD`](../abap-database-access/abapselect_indicators.md). For evaluating indicators represented by bits, the statement [`GET BIT`](../abap-processing-internal-data/abapget_bit.md) or [bit operators](../abap-processing-internal-data/abenbit_operators.md) can be used.

- A [condensed indicator structure](../../abap-glossary/abencondensed_ind_structure_glosry.md) needs less space than an actual [indicator structure](../../abap-glossary/abenindicator_structure_glosry.md), while the latter can be handled more comfortably.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The structured type `ind_struct` has the same components with the same types as `struct` plus an additional component `ind` of type `x` with length 2. The first 11 bits of that byte field can serve as indicators for the components `col1` to `col10` of `struct`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF struct, 
    col1  TYPE i, 
    col2  TYPE i, 
    col3  TYPE i, 
    col4  TYPE i, 
    col5  TYPE i, 
    col6  TYPE i, 
    col7  TYPE i, 
    col8  TYPE i, 
    col9  TYPE REF TO i, 
    col10 TYPE TABLE OF demo_struc WITH EMPTY KEY, 
  END OF struct. 
 
TYPES ind_struct TYPE struct WITH INDICATORS ind AS BITFIELD. 
 
DATA ind_struct TYPE ind_struct. 
 
out->write( ind_struct ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The structure `wa_ind` has a condensed indicator structure `null_ind` that is used as a [null indicator](../../abap-glossary/abennull_indicator_glosry.md) in a `SELECT` statement. It has length of 6 and thus consists of 48 bits that cover the 44 fields of database table `DEMO_EXPRESSIONS` used for declaring `wa_ind`. The three columns `num1`, `fltp1`, and `char1` of the result set of the `SELECT` statement contain the null value because the `WHEN` conditions of the `CASE` expressions are false and no `ELSE` is specified. Since the addition `INTO CORRESPONDING` is used, the positions of the bits of the null indicator correspond to the positions of the components of the target area that correspond to the columns of the result set. Accordingly, the third, the tenth and the sixteenth bit of the byte field `wa_ind-null_ind` have the value 1. While its hexadecimal value *204100000000* is not too informative, the `GET BIT` statement can be used to extract the positions of the columns that contain the null value.

``` abap
DELETE FROM demo_expressions. 
INSERT demo_expressions FROM @( VALUE #( id = 'X' num1 = 1 ) ). 
 
TYPES demo_ind TYPE demo_expressions 
  WITH INDICATORS null_ind AS BITFIELD. 
 
DATA wa_ind TYPE demo_ind. 
 
SELECT SINGLE 
  FROM demo_expressions 
  FIELDS 
    CAST( CASE WHEN num1 = 0 THEN 0 END AS INT4 ) AS num1, 
    CAST( CASE WHEN num1 = 0 THEN 0 END AS FLTP ) AS fltp1, 
    CAST( CASE WHEN num1 = 0 THEN 0 END AS CHAR ) AS char1 
  INTO CORRESPONDING FIELDS OF @wa_ind 
       INDICATORS NULL BITFIELD null_ind. 
 
DATA binary_ind TYPE string. 
DATA null_columns TYPE TABLE OF i WITH EMPTY KEY. 
WHILE sy-index <= xstrlen( wa_ind-null_ind ) * 8. 
  GET BIT sy-index OF wa_ind-null_ind INTO FINAL(bit). 
  binary_ind &&= bit. 
  IF bit = 1. 
    APPEND sy-index TO null_columns. 
  ENDIF. 
ENDWHILE. 
 
cl_demo_output=>new( 
 )->write( wa_ind 
 )->write( wa_ind-null_ind 
 )->write( binary_ind 
 )->write( null_columns 
 )->display( ).
```
