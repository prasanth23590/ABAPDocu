---
title: "INSERT, line_spec"
source_file: abapinsert_itab_linespec.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > INSERT itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INSERT, line_spec

## Syntax

``` abap
... wa   
  | {INITIAL LINE}   
  | {LINES OF jtab [FROM idx1] [TO idx2] [STEP n] [USING KEY keyname]} ...  
```

[`keyname`](abenkeyname.md)

### Alternative

[1. `... wa`](abapinsert_itab_linespec.md#alternative-1)

[2. `... INITIAL LINE`](abapinsert_itab_linespec.md#alternative-2)

[3. `... LINES OF jtab [FROM idx1] [TO idx2] [STEP n] [USING KEY keyname]`](abapinsert_itab_linespec.md#alternative-3)

## Overview

### Description

Either a work area `wa`, an initial line `INITIAL LINE`, or multiple lines of an internal table `jtab` can be appended.

## Alternative 1

`... wa`

### Description

A new line is created to which the content of the work area `wa` is assigned. `wa` is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md). The following applies here:

- When inserting using the table key, `wa` [must be compatible with](../../abap-glossary/abencompatible_glosry.md) the line type of the internal table. Exceptions to this rule are any [constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md) whose result type can be incompatible with the line type and whose result is converted to the line type if possible.

- When inserting using the table index, `wa` can be incompatible with the line type of the internal table and is, if necessary, converted to the relevant line type, in accordance with the [conversion rules](abenconversion_rules.md).

If a conversion error occurs in the conversion, the exception cannot be handled using `CX_SY_CONVERSION_ERROR` and the associated runtime error occurs instead. If an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md) is specified for `wa`, the line type of the internal table is used to determine [calculation type](../../abap-glossary/abencalculation_type_glosry.md).

When inserting individual lines into an internal table with non-unique [table keys](../abap-data-types-and-data-objects/abenitab_key.md), the order of the duplicate lines in relation to these keys is determined by the insertion order of the individual lines. In the case of secondary table keys, this occurs during the [lazy update](../../abap-glossary/abenlazy_update_glosry.md).

If there is a conflict with the existing unique primary table key, no line is inserted. If a key access occurs, `sy-subrc` is set to 4. In an index access, however, an uncatchable exception is raised. In the case of a conflict with a unique secondary table key, a catchable exception of the class `CX_SY_ITAB_DUPLICATE_KEY` is raised.

### Hints

- When inserting using the table key, incompatible work areas can be converted to the line type using the conversion operator [`CONV`](abenconstructor_expression_conv.md).

- Specifying a [calculation expression](../../abap-glossary/abencalculation_expression_glosry.md) for `wa` is usually only useful for elementary line types.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Insertion of a structure constructed using the value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) into an internal table.

``` abap
DATA itab TYPE HASHED TABLE OF scarr WITH UNIQUE KEY carrid. 
 
INSERT VALUE #( carrid   = 'XXX' 
                carrname = 'yyyyyyyyy' 
                currcode = 'ZZ' 
                url      = '...' ) INTO TABLE itab.
```

## Alternative 2

`... INITIAL LINE`

### Description

A new line is created in which every component contains its type-dependent [initial value](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Insertion of an initial line that is simultaneously linked to a field symbol using the addition [`ASSIGNING`](abapinsert_itab_result.md). This means that the initial line can be processed directly.

``` abap
DATA itab TYPE TABLE OF spfli. 
 
FIELD-SYMBOLS <line> LIKE LINE OF itab. 
 
INSERT INITIAL LINE INTO itab INDEX 1 ASSIGNING <line>. 
 <line>-carrid = '...'. 
...
```

## Alternative 3

`... LINES OF jtab [FROM idx1] [TO idx2] [STEP n] [USING KEY keyname]`

### Description

The lines of an internal table `jtab` are appended as a block. `jtab` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md). The line types of `itab` and `jtab` must be compatible when inserting using the table key and convertible when inserting using the index.

The lines to be inserted are taken sequentially from the table `jtab`. The order in which the lines are taken is the same as for the statement [`LOOP`](abaploop_at_itab.md) and can also be affected by specifying a table key [`keyname`](abenkeyname.md) after `USING KEY`. The additions `FROM idx1` and `TO idx2` have the same syntax and effect as for [`LOOP`](abaploop_at_itab_cond.md) with respect to `jtab`. `STEP n` has the same syntax and effect as for [`LOOP`](abaploop_at_itab_cond.md) with the exception that the value of `n` must be positive.

When inserting lines as a block into an internal table with non-unique [primary table keys](../../abap-glossary/abenprimary_table_key_glosry.md), the order of the duplicate lines in relation to this primary key is preserved. This does not apply to [secondary keys](../../abap-glossary/abensecondary_key_glosry.md).

- If there is already a duplicate entry in a sorted target table, the duplicates of the source block are inserted in their original order in front of the first duplicate in the target table.

- When inserting in standard tables, however, `INSERT` always works like the statement [`APPEND`](abapappend.md) and the lines are appended in their original order after the last line as in the addition [`LINES OF`](abapappend_linespec.md).

If there is a conflict with an existing unique table key, an uncatchable exception is raised when inserting multiple lines from an internal table. If a conversion error occurs when lines are inserted, the exception cannot be handled using `CX_SY_CONVERSION_ERROR` and the associated runtime error occurs instead.

### Hint

When an internal table is constructed, the constructor operators [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) and [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) can also insert multiple lines from a table into the target table using [`LINES OF`](../abap-creating-objects-and-values/abennew_constructor_params_lspc.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Insertion of the lines of an internal table `itab` into the same table. The lines are inserted in front of the existing first line and in ascending order due to the specification of the sorted secondary key `skey` being specified.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA itab TYPE TABLE OF i 
          WITH NON-UNIQUE SORTED KEY skey COMPONENTS table_line. 
 
itab = VALUE #( FOR i = 1 UNTIL i > 10 ( 11 - i ) ). 
 
INSERT LINES OF itab USING KEY skey INTO itab INDEX 1. 
 
out->write( itab ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Insertion of the lines of an internal table `itab` into the same table, defined by `FROM`, `TO`, and `STEP`. The lines are inserted in front of the existing first line and in ascending order due to the specification of the sorted secondary key `skey` being specified.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA itab TYPE TABLE OF i 
          WITH NON-UNIQUE SORTED KEY skey COMPONENTS table_line. 
 
itab = VALUE #( FOR i = 1 UNTIL i > 5 ( 6 - i ) ). 
 
INSERT LINES OF itab FROM 1 TO 5 STEP 2 
  USING KEY skey INTO itab INDEX 1. 
 
out->write( itab ). 
 
out->display( ).
```
