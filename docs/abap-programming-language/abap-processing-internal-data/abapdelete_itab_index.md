---
title: "DELETE itab, index"
source_file: abapdelete_itab_index.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > DELETE itab > DELETE itab, itab_line"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DELETE itab, index

## Syntax

``` abap
...   { itab INDEX idx [USING KEY keyname] } 
    | { itab [USING KEY loop_key]} ...  
```

[`keyname`](abenkeyname.md)

### Alternative

[1. `... itab INDEX idx [USING KEY keyname]`](abapdelete_itab_index.md#alternative-1)

[2. `... itab [USING KEY loop_key]`](abapdelete_itab_index.md#alternative-2)

## Overview

### Description

These alternatives specify the lines to be deleted using the specification of a line number relating to a table index.

## Alternative 1

`... itab INDEX idx`

### Addition

[`... USING KEY keyname`](abapdelete_itab_index.md#addition)

### Description

If the `INDEX` addition is used, the `DELETE` statement deletes the line in the line number specified in `idx` in a table index. `idx` is a [numeric expression position](../../abap-glossary/abennumerical_expr_position_glosry.md) with the operand type `i`. If `idx` contains the value 0 or less, an uncatchable exception is raised.

If the addition `USING KEY` is not used, the addition `INDEX` can only be used with [index tables](../../abap-glossary/abenindex_table_glosry.md) and determines the line to be deleted from the [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Deletion of the table line that has the same value as the input field `carrid` in the key field `carrid`, by using the primary table index.

``` abap
DATA carrid TYPE scarr-carrid. 
cl_demo_input=>request( CHANGING field = carrid ). 
 
DATA scarr_tab TYPE SORTED TABLE OF scarr 
               WITH UNIQUE KEY carrid. 
SELECT * 
       FROM scarr 
       INTO TABLE @scarr_tab. 
 
FINAL(idx) = line_index( scarr_tab[ KEY primary_key carrid = carrid ] ). 
 
IF idx is NOT INITIAL. 
  DELETE scarr_tab INDEX idx. 
ENDIF.
```

### Executable Example

[Deleting Lines Using an Index](abendelete_line_idx_abexa.md)

## Addition

`... USING KEY keyname`

### Description

The addition `USING KEY` can be used to specify a table key can be specified in [`keyname`](abenkeyname.md) to specify the table index to be used explicitly.

If the table has a [sorted](../../abap-glossary/abensorted_key_glosry.md) [secondary key](../../abap-glossary/abensecondary_table_key_glosry.md), this can be specified in `keyname`. The line to be deleted is then determined from its [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md). A secondary [hash key](../../abap-glossary/abenhash_key_glosry.md) cannot be specified.

If the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) is specified under its name `primary_key`, the table must be an index table, and the behavior is the same as when `USING KEY` is not specified.

### Hint

If a sorted secondary key exists, the `INDEX` addition can be used for all table types, if `USING KEY` is used.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The `DELETE` statement deletes the third line of the internal table, since this has the line number 1 in the secondary table index belonging to the secondary table key `skey`.

``` abap
DATA itab TYPE TABLE OF i WITH EMPTY KEY 
          WITH UNIQUE SORTED KEY skey COMPONENTS TABLE_LINE. 
 
itab = VALUE #( ( 3 ) ( 2 ) ( 1 ) ). 
 
DELETE itab INDEX 1 USING KEY skey.
```

## Alternative 2

`... itab`

### Addition

[`... USING KEY loop_key`](abapdelete_itab_index.md#addition)

### Description

This variant is only possible within a [`LOOP`](abaploop_at_itab.md) across the same internal table. The current table line of the `LOOP` is then deleted implicitly. If the addition [`USING KEY`](abaploop_at_itab_cond.md) is specified in `LOOP`, the addition `USING KEY loop_key` must be specified for this variant.

If the current line was already deleted in the same loop, however, the behavior is undefined.

This variant is not allowed outside of a `LOOP` and raises a warning in the syntax check if it is not known statically that is executed in a loop.

### Hint

This alternative is not recommended. Instead, use the addition `INDEX` to specify the line number explicitly.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following loop deletes all lines of an internal table, since the short form of the statement [`DELETE`](abapdelete_itab.md) always deletes the current first line.

``` abap
DATA itab TYPE TABLE OF i WITH EMPTY KEY. 
itab = VALUE #( ( 1 ) ( 2 ) ( 3 ) ). 
 
LOOP AT itab ASSIGNING FIELD-SYMBOL(<fs>). 
  DELETE itab. 
ENDLOOP.
```

## Addition

`... USING KEY loop_key`

### Description

This addition is required if the table key used by the `LOOP` is specified explicitly in the statement `LOOP`. It states explicitly that the current table line is deleted by the `LOOP`. No other key can be specified apart from the predefined name [`loop_key`](abaploop_at_itab_cond.md). If no explicit table key is specified for `LOOP`, the addition `USING KEY loop_key` is optional.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Since the primary table key is specified explicitly for the `LOOP` loop, `USING KEY loop_key` must be specified for `DELETE` as well.

``` abap
DATA itab TYPE SORTED TABLE OF i WITH UNIQUE KEY table_line. 
itab = VALUE #( ( 1 ) ( 2 ) ( 3 ) ). 
 
LOOP AT itab USING KEY primary_key 
             ASSIGNING FIELD-SYMBOL(<fs>). 
  DELETE itab USING KEY loop_key. 
ENDLOOP.
```
