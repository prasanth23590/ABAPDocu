---
title: "DATA, key"
source_file: abapdata_primary_key.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects > DATA > DATA, TABLE OF > DATA, tabkeys"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DATA, key

## Syntax

``` abap
... { [UNIQUE | NON-UNIQUE]   
      { {KEY [primary_key [ALIAS alias_name] COMPONENTS] comp1 comp2 ...}   
      | {DEFAULT KEY} }  }   
  | { EMPTY KEY } ...  
```

### Alternative

[1. `... [UNIQUE|NON-UNIQUE] {KEY ...}|{DEFAULT KEY}`](abapdata_primary_key.md#alternative-1)

[2. `... EMPTY KEY`](abapdata_primary_key.md#alternative-2)

## Alternative 1

`... [UNIQUE|NON-UNIQUE] {KEY ...}|{DEFAULT KEY}`

### Description

Definition of the primary table key of an internal table by specifying components or defines it as a standard key. The syntax and semantics of the additions are the same as for the statement [`TYPES`](abaptypes_primary_key.md) for standalone table types, except that the primary key of a [bound](../../abap-glossary/abenbound_data_type_glosry.md) table type must always be fully specified.

- In [standard tables](../../abap-glossary/abenstandard_table_glosry.md), only the addition `NON-UNIQUE KEY` can be specified. If uniqueness is not specified, this addition is added implicitly. The addition `UNIQUE KEY` cannot be specified.

- In [sorted tables](../../abap-glossary/abensorted_table_glosry.md), one of the additions `UNIQUE KEY` or `NON-UNIQUE KEY` must be specified.

- In [hashed tables](../../abap-glossary/abenhashed_table_glosry.md), the addition `UNIQUE KEY` must be specified.

If no primary key is specified for `DATA` using `WITH`, the addition `WITH NON-UNIQUE DEFAULT KEY` is added implicitly for standard tables. This gives the table a [standard key](../../abap-glossary/abenstandard_key_glosry.md), which can be empty. In sorted tables and hashed tables, the primary key must be specified explicitly and cannot be empty.

### Hint

The declaration of the primary table key as a [standard key](../abap-data-types-and-data-objects/abenitab_standard_key.md) can be critical for various reasons. It is best to specify key fields explicitly instead. In particular, it must be ensured that the declaration of the standard key is not added by mistake because the key was not specified explicitly.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of a sorted table with a primary key without an explicit name specification.

``` abap
DATA sbook_tab 
     TYPE SORTED TABLE 
     OF sbook 
     WITH UNIQUE KEY carrid connid fldate bookid.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of a sorted table with a primary key and an explicit name specification.

``` abap
DATA sbook_tab 
     TYPE SORTED TABLE 
     OF sbook 
     WITH UNIQUE KEY primary_key 
                 COMPONENTS carrid connid fldate bookid.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of a sorted table with a primary key for which an alias name is defined.

``` abap
DATA sbook_tab 
     TYPE SORTED TABLE 
     OF sbook 
     WITH UNIQUE KEY primary_key ALIAS full_table_key 
                 COMPONENTS carrid connid fldate bookid.
```

## Alternative 2

`... EMPTY KEY`

### Description

Definition of an [empty primary key](../abap-data-types-and-data-objects/abenitab_empty_key.md) for an internal table. This variant is possible for standard tables only. The syntax and semantics are the same as for the statement [`TYPES`](abaptypes_primary_key.md).

### Hints

- The addition `EMPTY KEY` can provide clarity in all situations in which the definition of a table key is not important.

- In general, it is recommended that the addition `EMPTY KEY` is used instead of not specifying a key definition, since otherwise the [standard key](../abap-data-types-and-data-objects/abenitab_standard_key.md) is used, which often produces unexpected results.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of a table with an empty primary key. Using the [`SORT`](../abap-processing-internal-data/abapsort_itab.md) statement without specifying a sort criterion would have no effect for this table.

``` abap
DATA unsorted_carrier_list 
     TYPE STANDARD TABLE 
     OF scarr 
     WITH EMPTY KEY.
```
