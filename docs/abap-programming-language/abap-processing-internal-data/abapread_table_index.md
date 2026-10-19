---
title: "READ TABLE, index"
source_file: abapread_table_index.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > READ TABLE itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# READ TABLE, index

## Syntax

``` abap
... INDEX idx [USING KEY keyname] ...  
```

[`keyname`](abenkeyname.md)

### Addition

[`... USING KEY keyname`](abapread_table_index.md#addition)

## Overview

### Description

Using the `INDEX` addition, the `READ` statement reads the line in the line number specified in `idx` in a table index. `idx` is a [numeric expression position](../../abap-glossary/abennumerical_expr_position_glosry.md) with the operand type `i`. If the value of `idx` is less than or equal to 0 or greater than the number of table lines, no line is read and `sy-subrc` is set to 4. After a successful read, the system field `sy-tabix` contains the line number specified in `idx` in the primary or secondary table index used.

If the addition `USING KEY` is not used, the addition `INDEX` can only be specified for [index tables](../../abap-glossary/abenindex_table_glosry.md) and determines the line to be read from the [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md).

### Hint

[Table expressions](../../abap-glossary/abentable_expression_glosry.md) allow corresponding reads to also be performed in operand positions. The syntax shown here can be mapped to a [line specification](abentable_exp_itab_line.md) in a table expression.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of the first ten lines of the internal table `sflight_tab` using the primary table index. Instead of the `DO` loop, a [`LOOP`](abaploop_at_itab.md) or a corresponding iteration expression with [`FOR`](abenfor_itab.md) is used for this purpose.

``` abap
DATA: sflight_tab TYPE SORTED TABLE OF sflight 
                  WITH NON-UNIQUE KEY seatsocc, 
      sflight_wa  LIKE LINE OF sflight_tab. 
 
... 
 
SELECT * 
       FROM sflight 
       WHERE carrid = 'LH' AND 
             connid = '400' 
       INTO TABLE @sflight_tab. 
 
... 
 
DO 10 TIMES. 
  READ TABLE sflight_tab INDEX sy-index INTO sflight_wa. 
  IF sy-subrc <> 0. 
    EXIT. 
  ENDIF. 
  ... 
ENDDO.
```

## Addition

`... USING KEY keyname`

### Description

The addition `USING KEY` can be used to specify a table key in [`keyname`](abenkeyname.md) to specify the table index to be used explicitly.

If the table has a [sorted](../../abap-glossary/abensorted_key_glosry.md) [secondary key](../../abap-glossary/abensecondary_table_key_glosry.md), this can be specified in `keyname` and the line to be read is then determined from its [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md). A secondary [hash key](../../abap-glossary/abenhash_key_glosry.md) cannot be specified.

If the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) is specified using its name `primary_key`, the table must be an index table, and the behavior is the same as if `USING KEY` was not specified.

### Hints

- If a sorted secondary key exists, the addition `INDEX` can be used for all table categories, if `USING KEY` is used.

- [Table expressions](../../abap-glossary/abentable_expression_glosry.md) allow corresponding reads to also be performed in operand positions. The table key for an index is specified using [`KEY keyname INDEX`](abentable_exp_itab_line.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of the first ten lines of the internal table `sflight_tab` using a secondary table index. Instead of the `DO` loop, a [`LOOP`](abaploop_at_itab.md) or a corresponding iteration expression with [`FOR`](abenfor_itab.md) is used for this purpose.

``` abap
DATA: sflight_tab TYPE HASHED TABLE OF sflight 
                  WITH UNIQUE KEY primary_key 
                       COMPONENTS carrid connid fldate 
                  WITH NON-UNIQUE SORTED KEY occupied_seats 
                       COMPONENTS seatsocc, 
      sflight_wa  LIKE LINE OF sflight_tab. 
 
... 
 
SELECT * 
       FROM sflight 
       WHERE carrid = 'LH' AND 
             connid = '400' 
       INTO TABLE @sflight_tab. 
 
... 
 
DO 10 TIMES. 
  READ TABLE sflight_tab 
       INDEX sy-index USING KEY occupied_seats 
       INTO sflight_wa. 
  IF sy-subrc <> 0. 
    EXIT. 
  ENDIF. 
  ... 
ENDDO.
```
