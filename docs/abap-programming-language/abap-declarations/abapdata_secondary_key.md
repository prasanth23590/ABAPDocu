---
title: "DATA, secondary_key"
source_file: abapdata_secondary_key.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects > DATA > DATA, TABLE OF > DATA, tabkeys"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DATA, secondary_key

## Syntax

``` abap
... {UNIQUE HASHED}|{UNIQUE SORTED}|{NON-UNIQUE SORTED}   
    KEY key_name [ALIAS alias_name] COMPONENTS comp1 comp2 ...  
```

## Description

Definition of a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) of an internal table. The syntax and semantics of the additions are the same as those for the statement [`TYPES`](abaptypes_secondary_key.md) for standalone table types.

## Hints

- When internal tables are accessed using the statements [`READ TABLE itab`](../abap-processing-internal-data/abapread_table.md), [`LOOP AT itab`](../abap-processing-internal-data/abaploop_at_itab.md), [`MODIFY itab`](../abap-processing-internal-data/abapmodify_itab.md), and [`DELETE itab`](../abap-processing-internal-data/abapdelete_itab.md) or using [table expressions](../abap-processing-internal-data/abentable_expressions.md) and in [mesh types](abaptypes_mesh.md) and [mesh paths](../abap-processing-internal-data/abenmesh_pathes.md), a secondary key can be used to specify the lines to be processed or the processing order. To do this, the additions `WITH [TABLE] KEY ... COMPONENTS` or `USING KEY` must be specified in the statements and the addition [`KEY`](../abap-processing-internal-data/abentable_exp_itab_line.md) must be used in table expressions. A secondary key is never used implicitly.

- The statement [`INSERT itab`](../abap-processing-internal-data/abapinsert_itab.md) determines the insert position using the primary key and primary index only. A secondary key can be specified only for the source table from which multiple lines are inherited. The latter also applies to the statement [`APPEND`](../abap-processing-internal-data/abapappend.md).

- If different table keys of an internal table contain the same components, a syntax check warning occurs, which can be hidden using a pragma. In the case of a reference to a non-generic table type defined using [`TYPES`](abaptypes_secondary_key.md), any pragma specified there is also applied to the `DATA` statement. In the case of a reference to a generic table type for which no primary table key is defined, the specified pragma is not applied to the `DATA` statement, since this statement uses a completed table type implicitly and the pragma must also be specified for `DATA`.

- For more information, see [`TYPES`](abaptypes_secondary_key.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of an internal table with one primary key and two secondary keys.

``` abap
DATA sbook_tab 
     TYPE STANDARD TABLE 
     OF sbook 
     WITH NON-UNIQUE KEY carrid connid fldate bookid 
     WITH UNIQUE HASHED KEY hash_key 
          COMPONENTS carrid connid fldate bookid 
     WITH NON-UNIQUE SORTED KEY sort_key 
          COMPONENTS customid.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

As in the previous example but with explicit naming of the primary key.

``` abap
DATA sbook_tab 
     TYPE STANDARD TABLE 
     OF sbook 
     WITH NON-UNIQUE KEY primary_key 
          COMPONENTS carrid connid fldate bookid 
     WITH UNIQUE HASHED KEY hash_key 
          COMPONENTS carrid connid fldate bookid 
     WITH NON-UNIQUE SORTED KEY sort_key 
          COMPONENTS customid.
```
