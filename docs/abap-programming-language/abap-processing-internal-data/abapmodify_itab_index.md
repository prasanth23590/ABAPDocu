---
title: "MODIFY itab, index"
source_file: abapmodify_itab_index.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > MODIFY itab > MODIFY itab, itab_line"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MODIFY itab, index

## Syntax

``` abap
...   { itab INDEX idx [USING KEY keyname] } 
    | { itab [USING KEY loop_key]} ...  
```

[`keyname`](abenkeyname.md)

### Alternative

[1. `... itab INDEX idx [USING KEY keyname]`](abapmodify_itab_index.md#alternative-1)

[2. `... itab [USING KEY loop_key]`](abapmodify_itab_index.md#alternative-2)

## Overview

### Description

These alternatives specify the lines to be changed using the specification of a line number relating to a table index.

## Alternative 1

`... itab INDEX idx`

### Addition

[`... USING KEY keyname`](abapmodify_itab_index.md#addition-1)

### Description

Using the addition `INDEX`, the statement `MODIFY` modifies the line in the line number specified in `idx` in a table index. `idx` is a [numeric expression position](../../abap-glossary/abennumerical_expr_position_glosry.md) with the operand type `i`. If `idx` contains the value 0 or less, an uncatchable exception is raised.

If the addition `USING KEY` is not used, the addition `INDEX` can only be used with [index tables](../../abap-glossary/abenindex_table_glosry.md) and determines the line to be modified from its [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md).

If a line specified using `INDEX` is modified without the addition [`TRANSPORTING`](abapmodify_itab_single.md), all components of the line are transported. If it is known statically that write-protected [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md) would be overwritten by this, a syntax error occurs. If it can only be determined at runtime, the corresponding runtime error occurs.

If the components of a primary sorted table key are modified in a line specified using `INDEX`, however, a runtime error occurs only if the value of the component changes.

### Hint

The addition `INDEX` can also be positioned after `FROM wa`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Conversion of the local currency of an airline in the internal table `scarr_tab` by accessing the index. The addition `TRANSPORTING` ensures that only the component `currcode` is modified and only this component is filled in the structure constructed by the value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md).

``` abap
DATA: carrid   TYPE scarr-carrid   VALUE 'LH', 
      currcode TYPE scarr-currcode VALUE 'EUR'. 
cl_demo_input=>new( 
  )->add_field( CHANGING field = carrid 
  )->add_field( CHANGING field = currcode )->request( ). 
 
DATA scarr_tab TYPE SORTED TABLE OF scarr 
               WITH UNIQUE KEY carrid. 
 
SELECT * 
       FROM scarr 
       INTO TABLE @scarr_tab. 
 
FINAL(idx) = line_index( scarr_tab[ carrid = carrid ] ). 
 
IF idx IS NOT INITIAL. 
  MODIFY scarr_tab 
         INDEX idx 
         FROM VALUE #( currcode = currcode ) 
         TRANSPORTING currcode. 
ENDIF.
```

## Addition

`... USING KEY keyname`

### Description

The addition `USING KEY` can be used to specify a table key in [`keyname`](abenkeyname.md) to specify the table index to be used explicitly.

If the table has a [sorted](../../abap-glossary/abensorted_key_glosry.md) [secondary key](../../abap-glossary/abensecondary_table_key_glosry.md), this can be specified in `keyname`. The line to be modified is then determined from its [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md). A secondary [hash key](../../abap-glossary/abenhash_key_glosry.md) cannot be specified.

If the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) is specified under its name `primary_key`, the table must be an index table, and the behavior is the same as if `USING KEY` were not specified.

### Hint

If a sorted secondary key exists, the addition `INDEX` can be used for all table types if `USING KEY` is used.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In this example, the letter *D* is replaced by *X* in the fourth line, since this line has the index value 1 in the sorted key `skey`.

``` abap
TYPES: 
  BEGIN OF line, 
    col1 TYPE c LENGTH 1, 
    col2 TYPE i, 
  END OF line. 
 
DATA itab TYPE STANDARD TABLE OF line 
               WITH EMPTY KEY 
               WITH NON-UNIQUE SORTED KEY skey COMPONENTS col2. 
 
itab = VALUE #( ( col1 = 'A' col2 = 6 ) 
                ( col1 = 'B' col2 = 4 ) 
                ( col1 = 'B' col2 = 7 ) 
                ( col1 = 'D' col2 = 1 ) 
                ( col1 = 'E' col2 = 3 ) 
                ( col1 = 'F' col2 = 9 ) 
                ( col1 = 'G' col2 = 2 ) 
                ( col1 = 'H' col2 = 5 ) 
                ( col1 = 'I' col2 = 8 ) ). 
 
MODIFY itab INDEX 1 
            USING KEY skey 
            FROM VALUE #( col1 = 'X' ) 
            TRANSPORTING col1.
```

## Alternative 2

`... itab`

### Addition

[`... USING KEY loop_key`](abapmodify_itab_index.md#addition-2)

### Description

This variant is only possible within a [`LOOP`](abaploop_at_itab.md) across the same internal table. The current table line of the `LOOP` is modified implicitly. If the addition [`USING KEY`](abaploop_at_itab_cond.md) is specified in `LOOP`, the addition `USING KEY loop_key` must be specified for this variant.

If the current lines were already deleted in the same loop pass, the behavior is undefined.

This variant is not allowed outside of `LOOP` statements. A syntax check warning occurs if it cannot be known statically whether the variant is specified in a loop.

### Hint

The use of this alternative is not recommended. Instead, the addition `INDEX` should be used to specify the line number explicitly.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The internal table contains the numbers 11 to 20 after the loop. Each existing number is raised by 10 in the loop.

``` abap
DATA itab TYPE TABLE OF i WITH EMPTY KEY. 
 
itab = VALUE #( FOR i = 1 UNTIL i > 10 ( i ) ). 
 
LOOP AT itab INTO FINAL(wa). 
  MODIFY itab FROM wa + 10. 
ENDLOOP.
```

## Addition

`... USING KEY loop_key`

### Description

This addition is required if the table key used by the `LOOP` is specified explicitly in the statement `LOOP`. It states explicitly that the current table line of the `LOOP` is modified. No other key can be specified apart from the predefined name [`loop_key`](abaploop_at_itab_cond.md). If no explicit table key is specified for `LOOP`, the addition `USING KEY loop_key` is optional.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In this example, the letters of the first column are replaced by the letters whose position in `sy-abcde` is given by the value `sy-tabix`. The table is processed in the order of the secondary index, which produces the same order with respect to this index in the first column as in the second column.

``` abap
TYPES: 
  BEGIN OF line, 
    col1 TYPE c LENGTH 1, 
    col2 TYPE i, 
  END OF line. 
 
DATA itab TYPE STANDARD TABLE OF line 
               WITH EMPTY KEY 
               WITH NON-UNIQUE SORTED KEY skey COMPONENTS col2. 
 
itab = VALUE #( ( col1 = 'A' col2 = 6 ) 
                ( col1 = 'B' col2 = 4 ) 
                ( col1 = 'B' col2 = 7 ) 
                ( col1 = 'D' col2 = 1 ) 
                ( col1 = 'E' col2 = 3 ) 
                ( col1 = 'F' col2 = 9 ) 
                ( col1 = 'G' col2 = 2 ) 
                ( col1 = 'H' col2 = 5 ) 
                ( col1 = 'I' col2 = 8 ) ). 
 
FINAL(abcde) = `abcdefghijklmnopqrstuvwxyz`. 
LOOP AT itab INTO FINAL(wa) USING KEY skey. 
  MODIFY itab 
         USING KEY loop_key 
         FROM VALUE #( col1 = substring( val = abcde 
                                         off = sy-tabix - 1 
                                         len = 1 ) ) 
         TRANSPORTING col1. 
ENDLOOP.
```
