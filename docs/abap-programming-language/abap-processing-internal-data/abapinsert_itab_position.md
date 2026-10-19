---
title: "INSERT, itab_position"
source_file: abapinsert_itab_position.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > INSERT itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INSERT, itab_position

## Syntax

``` abap
... {TABLE itab}   
  | {itab INDEX idx}   
  | {itab} ...  
```

### Alternative

[1. `... TABLE itab`](abapinsert_itab_position.md#alternative-1)

[2. `... itab INDEX idx`](abapinsert_itab_position.md#alternative-2)

[3. `... itab`](abapinsert_itab_position.md#alternative-3)

## Overview

### Description

These alternatives specify the position in the internal table `itab` at which lines are inserted. In the variant with the addition `TABLE`, the position of the insert is specified using the primary table key. In any of the other variants, a line number from the primary table index is used. The latter is only possible for [index tables](../../abap-glossary/abenindex_table_glosry.md).

### Hint

The insert position is determined exclusively using either the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) or the [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md) only. For the [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md) in the internal table, the system checks for uniqueness and adds the new table line to the corresponding administration (hash administration, secondary table index). In the case of secondary keys, the administration is updated before the next access; for non-unique secondary keys, it is updated before the secondary key is used again.

## Alternative 1

`... TABLE itab`

### Description

The lines to be inserted [`line_spec`](abapinsert_itab_linespec.md) must be [compatible](../../abap-glossary/abencompatible_glosry.md) with the line type of the internal table. Depending on the table category, each line is inserted as follows:

- For [standard tables](../../abap-glossary/abenstandard_table_glosry.md), each new line is appended as the last line to the internal table regardless of the primary table key.

- For [sorted tables](../../abap-glossary/abensorted_table_glosry.md), each new line is inserted into the sort order of the internal table in accordance with its key values with respect to the primary key. The line numbers in the primary table index of the following lines are increased by one. If the internal table has a non-unique key, duplicate entries are inserted before the existing line.

- In [hashed tables](../../abap-glossary/abenhashed_table_glosry.md), each new line is inserted into the internal table by the hash administration in accordance with its key values with respect to the primary key.

If the internal table has one or more unique table keys, no entries are inserted that would produce duplicate entries in one of the unique table keys. When single lines are inserted, `sy-subrc` is set to 4 if a duplicate entry with respect to the primary key were to be produced, and a catchable exception of the class `CX_SY_ITAB_DUPLICATE_KEY` is raised if a duplicate entry with respect to a secondary key were to be produced. If multiple lines are inserted, an uncatchable exception is raised.

### Hint

If the primary table key is used, it should be noted that this key can be the [standard key](../../abap-glossary/abenstandard_key_glosry.md) that covers all character-like and byte-like components if the line type is structured. An empty standard key is possible only for standard tables. In these tables, `INSERT` always works like `APPEND` in this variant.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Filling of an internal table `connection_tab` with data from the database table `spfli`. Single lines are inserted using the primary table key and are filled with the content of the work area `connection`. Since the internal table has a unique primary key, any duplicate entries are discarded. The better performing [`SELECT`](../abap-database-access/abapselect.md) statement, in which the internal table is specified directly after [`INTO TABLE`](../abap-database-access/abapinto_clause.md), could raise an exception due to the uniqueness of the primary table key.

``` abap
SELECT cityfrom, cityto, distid, distance 
       FROM spfli 
       INTO @FINAL(connection). 
  DATA connection_tab LIKE SORTED TABLE OF connection 
                      WITH UNIQUE KEY cityfrom cityto 
                                      distid distance. 
  INSERT connection INTO TABLE connection_tab. 
ENDSELECT.
```

## Alternative 2

`... itab INDEX idx`

### Description

This variant can only be used for [standard tables](../../abap-glossary/abenstandard_table_glosry.md) and [sorted tables](../../abap-glossary/abensorted_table_glosry.md). Each of the lines to be inserted [`line_spec`](abapinsert_itab_linespec.md) is inserted before the line with the line number `idx` in the primary table index. The line numbers in the primary table index of the following lines are increased by one. `idx` is a [numeric expression position](../../abap-glossary/abennumerical_expr_position_glosry.md) of operand type `i`.

If `idx` contains a value that corresponds to the number of existing table lines plus one, the new line is appended as the last line to the internal table. If `idx` contains a greater value, no line is inserted and `sy-subrc` is set to 4.

An uncatchable exception is raised in the following cases:

- If `idx` contains a value less than or equal to 0.

- If a single line to be inserted would produce a duplicate entry in a unique primary or secondary table key.

- If a block of lines to be inserted would produce a duplicate entry in a unique primary table key.

- If a line to be inserted would disrupt the sort order of a sorted table.

  Modifying the sort order with respect to a sorted secondary key, however, never raises an exception. Instead, the associated secondary index is either updated directly ([direct update](../../abap-glossary/abendirect_update_glosry.md)) or updated after a delay ([lazy update](../../abap-glossary/abenlazy_update_glosry.md)).

If a single line to be inserted produces a duplicate entry in a unique secondary table key, a catchable exception of the class `CX_SY_ITAB_DUPLICATE_KEY` is raised.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Insertion of a line after a previously searched for line.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA html TYPE TABLE OF string WITH EMPTY KEY. 
 
html = VALUE #( ( `<html>` ) 
                ( `<body>` ) 
                ( `</body>` ) 
                ( `</html>` ) ). 
 
FIND `<body>` IN TABLE html MATCH LINE FINAL(idx). 
 
INSERT `<b>Text</b>` INTO html INDEX idx + 1. 
 
out->write_html( concat_lines_of( html ) ). 
 
out->display( ).
```

## Alternative 3

`... itab`

### Description

This variant is only possible within a [`LOOP`](abaploop_at_itab.md) across the same internal table and if the addition [`USING KEY`](abaploop_at_itab_cond.md) is not specified in the `LOOP`. Each line to be inserted can be inserted in front of the current line in the `LOOP`.

If the current line was already deleted in the same loop, however, the behavior is undefined.

### Hint

This alternative is not recommended. Instead, the addition `INDEX` should be used to specify the line number explicitly.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Conditional insertion of a line in front of every line in an internal table.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA itab TYPE TABLE OF string WITH EMPTY KEY. 
 
itab = VALUE #( FOR i = 1 UNTIL i > 10 ( CONV #( i ) ) ). 
 
LOOP AT itab ASSIGNING FIELD-SYMBOL(<fs>). 
  IF conv i( <fs> ) / 2 * 2 = CONV i( <fs> ). 
    INSERT 'Pair' INTO itab. 
  ELSE. 
    INSERT 'Impair' INTO itab. 
  ENDIF. 
ENDLOOP. 
 
out->write( itab ). 
 
out->display( ).
```
