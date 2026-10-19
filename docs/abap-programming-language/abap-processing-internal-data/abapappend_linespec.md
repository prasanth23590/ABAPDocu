---
title: "APPEND, line_spec"
source_file: abapappend_linespec.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > APPEND"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# APPEND, line_spec

## Syntax

``` abap
... wa   
  | {INITIAL LINE}   
  | {LINES OF jtab [FROM idx1] [TO idx2] [STEP n] [USING KEY keyname]} ...  
```

[`keyname`](abenkeyname.md)

### Alternative

[1. `... wa`](abapappend_linespec.md#alternative-1)

[2. `... INITIAL LINE`](abapappend_linespec.md#alternative-2)

[3. `... LINES OF jtab [FROM idx1] [TO idx2] [STEP n] [USING KEY keyname]`](abapappend_linespec.md#alternative-3)

## Overview

### Description

Either a work area `wa`, an initial line `INITIAL LINE`, or multiple lines of an internal table `jtab` can be appended.

## Alternative 1

`... wa`

### Description

A new line is appended to which the content of the work area `wa` is assigned. `wa` is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md). `wa` may be incompatible with the line type of the internal table and, if necessary, is converted to the line type in accordance with the [conversion rules](abenconversion_rules.md). If a conversion error occurs here, the exception cannot be handled using `CX_SY_CONVERSION_ERROR` and the associated runtime error occurs instead. If an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md) is specified for `wa`, the line type of the internal table is used to determine the [calculation type](../../abap-glossary/abencalculation_type_glosry.md).

### Hints

- If a conflict occurs with an existing unique primary table type, this raises an uncatchable exception when appending a single line. In the case of a conflict with a unique secondary table key, a catchable exception of the class `CX_SY_ITAB_DUPLICATE_KEY` is raised.

- Specifying a [calculation expression](../../abap-glossary/abencalculation_expression_glosry.md) for `wa` is usually only useful for elementary line types.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Appending of square numbers to a [sorted table](../../abap-glossary/abensorted_table_glosry.md) with elementary line type.

``` abap
DATA: int  TYPE i, 
      itab LIKE SORTED TABLE OF int 
           WITH UNIQUE KEY table_line. 
 
DO 10 TIMES. 
  int = sy-index ** 2. 
  APPEND int TO itab. 
ENDDO.
```

## Alternative 2

`... INITIAL LINE`

### Description

A new line is appended in which every component contains the [type-dependent initial value](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Appending of an initial line that simultaneously is linked to a field symbol using the addition [`ASSIGNING`](abapappend_result.md). This means that initial lines can be processed directly.

``` abap
DATA itab TYPE TABLE OF spfli. 
 
FIELD-SYMBOLS <line> LIKE LINE OF itab. 
 
APPEND INITIAL LINE TO itab ASSIGNING <line>. 
 <line>-carrid = '...'. 
...
```

## Alternative 3

`... LINES OF jtab [FROM idx1] [TO idx2] [STEP n] [USING KEY keyname]`

### Description

The lines of an internal table `jtab` are appended as a block. `jtab` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md).

The lines to be inserted are taken sequentially from the table `jtab`. The line type of `jtab` can be incompatible with the line type of the internal table `itab` and is converted to the line type of the target table, if necessary, in accordance with the [conversion rules](abenconversion_rules.md). If a conversion error occurs here, the exception cannot be handled using `CX_SY_CONVERSION_ERROR` and the associated runtime error occurs instead.

The order in which the lines are taken is the same as for the statement [`LOOP`](abaploop_at_itab.md) and can also be affected by specifying a table key [`keyname`](abenkeyname.md) after ` USING KEY`. The additions `FROM idx1` and `TO idx2` have the same syntax and effect as for [`LOOP`](abaploop_at_itab_cond.md) with respect to `jtab`. `STEP n` has the same syntax and effect as for [`LOOP`](abaploop_at_itab_cond.md) with the exception that the value of `n` must be positive.

If a conflict with existing primary or secondary table keys occurs, this always raises an uncatchable exception when multiple lines are appended from an internal table.

### Hint

When a standard table is constructed, the constructor operators [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) and [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) can also append multiple lines from a table to the target table using [`LINES OF`](../abap-creating-objects-and-values/abennew_constructor_params_lspc.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Appending of the lines of an internal table `itab2` to the standard table `itab1`.

``` abap
SELECT * 
       FROM spfli 
       WHERE carrid = 'LH' 
       INTO TABLE @DATA(itab1). 
 
SELECT * 
       FROM spfli 
       WHERE carrid = 'UA' 
       INTO TABLE @FINAL(itab2). 
 
APPEND LINES OF itab2 TO itab1.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Appending of the lines of an internal table `jtab` to the standard table `itab` with the additions `FROM`, `TO`, and `STEP`.

``` abap
DATA: itab TYPE STANDARD TABLE OF i, 
      jtab LIKE itab. 
 
itab = VALUE #( FOR i = 1 UNTIL i > 10 ( i ) ). 
jtab = VALUE #( FOR j = 11 UNTIL j > 20 ( j ) ). 
 
APPEND LINES OF jtab FROM 1 TO 5 STEP 2 TO itab.
```
