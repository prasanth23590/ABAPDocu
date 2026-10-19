---
title: "DATA, tabkeys"
source_file: abapdata_keydef.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects > DATA > DATA, TABLE OF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DATA, tabkeys

## Syntax

``` abap
... [ WITH key ]   
    [ WITH secondary_key1 ] [ WITH secondary_key2 ] ...  
```

[`key`](abapdata_primary_key.md) · [`secondary_key1`](abapdata_secondary_key.md) · [`secondary_key2`](abapdata_secondary_key.md)

## Description

Definition of the table keys of an internal table. The following can be defined:

- A [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) using [`key`](abapdata_primary_key.md).

  Every internal table has a primary key. The primary key must be defined explicitly for [sorted tables](../../abap-glossary/abensorted_table_glosry.md) and [hashed tables](../../abap-glossary/abenhashed_table_glosry.md). The specification for the primary key can only be omitted for [standard tables](../../abap-glossary/abenstandard_table_glosry.md). The primary table key is then defined automatically as a non-unique [standard key](../../abap-glossary/abenstandard_key_glosry.md).

- Multiple [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md) with [`secondary_key1`](abapdata_secondary_key.md), [`secondary_key2`](abapdata_secondary_key.md), `...`

  The specification of secondary keys is optional for all table categories. If no secondary key is specified, the internal table has only one primary key.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of a [hashed table](../../abap-glossary/abenhashed_table_glosry.md) with a unique primary key and two non-unique secondary [sorted keys](../../abap-glossary/abensorted_key_glosry.md), `cityfrom_to` and `airp_from_to`.

``` abap
DATA spfli_tab TYPE HASHED TABLE OF spfli 
  WITH UNIQUE KEY carrid connid 
  WITH NON-UNIQUE SORTED KEY cityfrom_to  COMPONENTS cityfrom cityto 
  WITH NON-UNIQUE SORTED KEY airp_from_to COMPONENTS airpfrom airpto.
```
