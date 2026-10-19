---
title: "TYPES, tabkind"
source_file: abaptypes_tabcat.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES > TYPES, TABLE OF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPES, tabkind

## Syntax

``` abap
... { {[STANDARD] TABLE} 
    | {SORTED TABLE} 
    | {HASHED TABLE} 
    | {ANY TABLE} 
    | {INDEX TABLE} } ...  
```

### Addition

[1. `... [STANDARD] TABLE`](abaptypes_tabcat.md#addition-1)

[2. `... SORTED TABLE`](abaptypes_tabcat.md#addition-2)

[3. `... HASHED TABLE`](abaptypes_tabcat.md#addition-3)

[4. `... ANY TABLE`](abaptypes_tabcat.md#addition-4)

[5. `... INDEX TABLE`](abaptypes_tabcat.md#addition-5)

## Overview

### Description

Defines the table category of an internal table. Possible specifications:

- Non-generic table categories

  - `STANDARD TABLE` for [standard tables](../../abap-glossary/abenstandard_table_glosry.md)

  - `SORTED TABLE` for [sorted tables](../../abap-glossary/abensorted_table_glosry.md)

  - `HASHED TABLE` for [hashed tables](../../abap-glossary/abenhashed_table_glosry.md)

- Generic table categories

  - `ANY TABLE` covers all table categories

  - `INDEX TABLE` of [index tables](../../abap-glossary/abenindex_table_glosry.md) ([standard tables](../../abap-glossary/abenstandard_table_glosry.md) and [sorted tables](../../abap-glossary/abensorted_table_glosry.md))

The addition `STANDARD` is optional for standard tables.

### Hint

The additions of the statement `TYPES` listed above are language element additions for defining table categories. They are not to be confused with the [generic ABAP types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) with the same name.

## Addition 1

`[STANDARD] TABLE`

## Addition 2

`SORTED TABLE`

## Addition 3

`HASHED TABLE`

### Description

The non-generic table categories specify the internal administration and primary access type for an internal table in ABAP programs:

- Standard tables are managed internally in the system using a [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md). New lines are either appended to the table or inserted at specific positions.

- Like standard tables, sorted tables are also managed using a [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md). The entries in this index are always sorted by the primary table key. The sort order is ascending and corresponds to the result of the statement [`SORT`](../abap-processing-internal-data/abapsort_itab.md) with no additions. The sorting is based on the [comparison rules](../abap-program-flow-logic/abenlogexp_rules.md) for the data types of the key fields.

- Hashed tables are managed by a hash algorithm. There is no [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md). The entries are not ordered in the memory. The position of a line is calculated from a key specification using a hash function.

### Hint

For non-generic table categories, the definition of the table key [`key`](abaptypes_keydef.md) determines whether the defined table type is generic.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of two internal tables with the elementary line type `string`. The table `words` is a standard table with an empty key. The table `sorted_words` is a sorted table with the explicitly defined primary key `table_line`, that is, the entire table line. When the table `words` is assigned to the table `sorted_words`, the lines are sorted in ascending order according to their content.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: words        TYPE STANDARD TABLE OF string 
                   WITH EMPTY KEY, 
      sorted_words TYPE SORTED TABLE OF string 
                   WITH NON-UNIQUE KEY table_line. 
 
SPLIT `This short text contains some short words` 
      AT ` ` INTO TABLE words. 
out->write( words ). 
 
sorted_words = words. 
out->write( sorted_words ). 
 
out->display( ).
```

## Addition 4

`ANY TABLE`

## Addition 5

`INDEX TABLE`

### Description

The generic table categories define a generic table type that can only be used for [typing](../../abap-glossary/abentyping_glosry.md) formal parameters and field symbols:

- `ANY TABLE` covers all table categories

- `INDEX TABLE` covers standard tables and sorted tables

### Hint

A generic table type must not be used as a component of a [structured type](abaptypes_struc.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of a generic table type `index_table` for index tables. In the method `meth`, an index access can be performed on the parameter `para` typed using this type. Only index tables can be passed to this parameter. If there is not at least one line in the internal table, the method is exited.

``` abap
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    TYPES index_table TYPE INDEX TABLE OF scarr. 
    METHODS meth IMPORTING para TYPE index_table. 
ENDCLASS. 
 
CLASS cls IMPLEMENTATION. 
  METHOD meth. 
    IF NOT line_exists( para[ 1 ] ). 
      RETURN. 
    ENDIF. 
    ... 
  ENDMETHOD. 
ENDCLASS.
```
