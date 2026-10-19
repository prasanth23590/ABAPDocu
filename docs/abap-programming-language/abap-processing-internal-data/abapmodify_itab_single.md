---
title: "MODIFY itab, itab_line"
source_file: abapmodify_itab_single.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > MODIFY itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MODIFY itab, itab_line

## Syntax

``` abap
... { table_key  | index } FROM wa   
                          [TRANSPORTING comp1 comp2 ...]   
                          [result].  
```

[`table_key`](abapmodify_itab_table_key.md) · [`index`](abapmodify_itab_index.md) · [`result`](abapmodify_itab_result.md)

### Addition

[`... TRANSPORTING comp1 comp2 ...`](abapmodify_itab_single.md#addition)

## Overview

### Description

In this variant, the statement `MODIFY` assigns the content of work area `wa` to a line specified by a table key in [`table_key`](abapmodify_itab_table_key.md) or a line number in [`index`](abapmodify_itab_index.md). `wa` is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md).

`TRANSPORTING` can be used to restrict the components `comp` to be modified. `result` can be used when changing a single line to set a reference to the changed line in the form of a field symbol or a data reference.

For access using table keys, index access to [sorted tables](../../abap-glossary/abensorted_table_glosry.md) and when the addition `TRANSPORTING` is used, the `wa` work area must be [compatible](../../abap-glossary/abencompatible_glosry.md) with the line type of the internal table. Only when inserting using the primary table index in [standard tables](../../abap-glossary/abenstandard_table_glosry.md) without the addition `TRANSPORTING` can `wa` be incompatible with the line type of the internal table and is converted to the line type in accordance with the [conversion rules](abenconversion_rules.md). If a conversion error occurs here, the exception cannot be handled using `CX_SY_CONVERSION_ERROR` and the associated runtime error occurs instead. If an [arithmetic expression](../../abap-glossary/abenarithmetic_expression_glosry.md) is specified for `wa`, the line type of the internal table is used to determine the [calculation type](../../abap-glossary/abencalculation_type_glosry.md).

### Hints

- When modifying a line in a table, the table keys that are read-only must be respected. While the overwriting of protected key fields in the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) is not checked until runtime, this always produces a syntax error for the [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md). If a line whose [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) is read only is changed, `FROM wa` can therefore only be specified together with `TRANSPORTING`, and no key fields of the secondary key can be specified after `TRANSPORTING`.

- Specifying a [calculation expression](../../abap-glossary/abencalculation_expression_glosry.md) for `wa` is usually only a good idea for elementary line types.

- The statement `MODIFY itab FROM wa` has the statement [`MODIFY dbtab FROM wa`](../abap-database-access/abapmodify_dbtab.md) with identical syntax. If an internal table has the same name as a database table, a statement like this accesses the internal table.

## Addition

`... TRANSPORTING comp1 comp2 ...`

### Description

The addition `TRANSPORTING` has the effect that only the specified components [`comp1`](abenitab_components.md), [`comp2`](abenitab_components.md), ... of the work area are assigned to the corresponding components of the lines to be changed. For [sorted tables](../../abap-glossary/abensorted_table_glosry.md) and [hashed tables](../../abap-glossary/abenhashed_table_glosry.md), no primary table key components can be specified after `TRANSPORTING`.

The components [`comp1`](abenitab_components.md), [`comp2`](abenitab_components.md), ... are specified in accordance with the rules in [Specifying Components](abenitab_components.md), with the restriction that, after `TRANSPORTING`, no attributes of classes can be addressed using the object component selector.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The position of letters from the first column of an internal table is determined in the system field `sy-abcde` and this value is assigned to the second column. The column is accessed using the table index and the statement `MODIFY` modifies the second column only.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF line, 
    key TYPE c LENGTH 1, 
    pos TYPE i, 
  END OF line, 
  itab TYPE TABLE OF line WITH EMPTY KEY. 
 
DATA(itab) = VALUE itab( ( key = 'U' ) ( key = 'H' ) ( key = 'K' ) ). 
 
FINAL(abcde) = `abcdefghijklmnopqrstuvwxyz`. 
LOOP AT itab INTO DATA(wa). 
  FINAL(idx) = sy-tabix. 
  wa = 
    VALUE #( BASE wa pos = find( val = abcde sub = wa-key ) + 1 ). 
  MODIFY itab 
         FROM wa 
         INDEX idx 
         TRANSPORTING pos. 
ENDLOOP. 
 
out->write( itab ). 
 
out->display( ).
```
