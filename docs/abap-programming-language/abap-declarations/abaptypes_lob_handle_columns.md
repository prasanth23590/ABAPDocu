---
title: "TYPES, lob_handle_columns"
source_file: abaptypes_lob_handle_columns.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES > TYPES, LOB HANDLE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPES, lob_handle_columns

## Syntax

``` abap
  ... { COLUMNS blob1 blob2 ... clob1 clob2 ... } 
    | { ALL [OTHER] [BLOB|CLOB] COLUMNS } ...  
```

## Description

These additions define which columns of the database table or the view `dbtab` are declared as [LOB handle components](../../abap-glossary/abenlob_handle_component_glosry.md) when deriving a [LOB handle structure](../../abap-glossary/abenlob_handle_component_glosry.md) using the statement [`TYPES`](abaptypes_lob_handle.md).

- `COLUMNS blob1 blob2 ... clob1 clob2 ...`

  specifies individual [BLOBs](../../abap-glossary/abenblob_glosry.md) `blob1`, `blob2`, ... or [CLOBs](../../abap-glossary/abenclob_glosry.md) `clob1`, `clob2`, ... These must exist in `dbtab`.

- `ALL OTHER BLOB|CLOB COLUMNS`

  This specifies all [BLOBs](../../abap-glossary/abenblob_glosry.md) or [CLOBs](../../abap-glossary/abenclob_glosry.md) in `dbtab` that are not covered when individual columns are specified. In the statement [`TYPES`](abaptypes_lob_handle.md), at least one individual column `blob` or `clob` must be specified using `COLUMNS ...`

- `ALL BLOB|CLOB COLUMNS`

  specifies all [BLOBs](../../abap-glossary/abenblob_glosry.md) or [CLOBs](../../abap-glossary/abenclob_glosry.md) of `dbtab`.

- `ALL OTHER COLUMNS`

  This specifies all [LOBs](../../abap-glossary/abenlob_glosry.md) in `dbtab` that are not covered when individual columns are specified. In the statement [`TYPES`](abaptypes_lob_handle.md), at least one individual column must be specified using `COLUMNS ...`

- `ALL COLUMNS`

  This specifies all [LOBs](../../abap-glossary/abenlob_glosry.md) in `dbtab`.

No other columns can be specified in the statement [`TYPES`](abaptypes_lob_handle.md) after the column specification `ALL OTHER ...`

The combination options of the column specifications with each other below and with the types specified using [`lob_handle_type`](abaptypes_lob_handle_type.md) are explained in the statement [`TYPES`](abaptypes_lob_handle.md).

## Hint

Columns of the data type [`GEOM_EWKB`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) are not supported as [BLOBs](../../abap-glossary/abenblob_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Demonstration of various column specifications in the definition of LOB-Handle components.

``` abap
TYPES lob_handle TYPE demo_lob_table 
                 READER FOR COLUMNS clob1 clob2 
                 LOB HANDLE FOR ALL BLOB COLUMNS 
                 LOCATOR FOR ALL OTHER CLOB COLUMNS.
```

## Executable Example

[Deriving LOB Handle Structures](abentypes_lob_handle_abexa.md)
