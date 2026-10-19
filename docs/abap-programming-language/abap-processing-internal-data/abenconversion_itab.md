---
title: "Conversion Rules for Internal Tables"
source_file: abenconversion_itab.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Conversion Rules for Internal Tables

Internal tables can only be assigned to internal tables. Whether or not assignment is possible depends exclusively on the line type, and it is independent of table type, table key, and number of lines. Internal tables can be assigned to each other if their line types are [compatible](../../abap-glossary/abencompatible_glosry.md) or [convertible](../../abap-glossary/abenconvertible_glosry.md).

When assigning an internal table to another, the lines of the target table are deleted. A new line is created in the target table for each line in the source table and then filled with the line content of the source table. The lines are stored according to the table category. For assignments to a [sorted table](../../abap-glossary/abensorted_table_glosry.md), the content is automatically sorted, and [hashed tables](../../abap-glossary/abenhashed_table_glosry.md) are stored according to the hash algorithm.

The content of the individual lines in the source table is assigned to the lines of the target table according to the same rules as between individual data objects of the corresponding line types. The same basic rule as for all conversions applies: The converted content of the single lines in the source table must be within the [value range](../../abap-glossary/abenvalue_range_glosry.md) of the line type in the target table.

Assignments between internal tables and data objects that are not internal tables lead to a syntax error or the runtime error `OBJECTS_MOVE_NOT_SUPPORTED`.

## Hints

- In internal tables with compatible or convertible line types, an uncatchable exception can be raised during assignment if, for example, in the target table a [duplicate](../abap-data-types-and-data-objects/abenitab_key_duplicates.md) of a unique [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) or [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) would be created.

- Internal tables with elementary line types can raise the same catchable exceptions as assignments between the associated elementary data types. After an exception of this type, the target table contains all lines assigned until this point.

- In assignments of an initial internal table to a filled internal table, the target table is initialized in the same way as with the statement [`CLEAR`](abapclear.md). This releases the memory space required for the table, except for the [initial memory requirement](../../abap-glossary/abeninitial_mem_req_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A standard table `text_tab` with line type `c` of length 20 is converted to a sorted table of type `string`.

``` abap
TYPES: 
  text       TYPE c LENGTH 20. 
DATA: 
  text_tab   TYPE STANDARD TABLE OF text WITH EMPTY KEY, 
  string_tab TYPE SORTED TABLE OF string WITH NON-UNIQUE KEY table_line. 
 
text_tab = VALUE #( 
  ( 'Perl' ) ( 'C' ) ( 'Visual Basic' ) ( 'Java' ) 
  ( 'ABAP' ) ( 'Pascal' ) ( 'Python' )  ( 'Lisp' ) ). 
 
string_tab = text_tab. 
 
cl_demo_output=>new( )->write( text_tab )->display( string_tab ).
```
