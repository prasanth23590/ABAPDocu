---
title: "TYPES, lob_handle_type"
source_file: abaptypes_lob_handle_type.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES > TYPES, LOB HANDLE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPES, lob_handle_type

## Syntax

``` abap
  ... { READER|LOCATOR|{LOB HANDLE} } 
    | { WRITER|LOCATOR } ...  
```

## Description

These additions define the static type of the [LOB handle components](../../abap-glossary/abenlob_handle_component_glosry.md) when deriving a [LOB handle structure](../../abap-glossary/abenlob_handle_component_glosry.md) using the statement [`TYPES`](abaptypes_lob_handle.md).

- The addition `READER` defines the following:

  - The static type `CL_ABAP_DB_X_READER` for [BLOBs](../../abap-glossary/abenblob_glosry.md)

  - The static type `CL_ABAP_DB_C_READER` for [CLOBs](../../abap-glossary/abenclob_glosry.md)

- The addition `WRITER` defines the following:

  - The static type `CL_ABAP_DB_X_WRITER` for [BLOBs](../../abap-glossary/abenblob_glosry.md)

  - The static type `CL_ABAP_DB_C_WRITER` for [CLOBs](../../abap-glossary/abenclob_glosry.md)

- The addition `LOCATOR` defines the following:

  - The static type `CL_ABAP_DB_X_LOCATOR` for [BLOBs](../../abap-glossary/abenblob_glosry.md)

  - The static type `CL_ABAP_DB_C_LOCATOR` for [CLOBs](../../abap-glossary/abenclob_glosry.md)

- The addition `LOB HANDLE` defines the following:

  - The static type `IF_ABAP_DB_BLOB_HANDLE` for [BLOBs](../../abap-glossary/abenblob_glosry.md)

  - The static type `IF_ABAP_DB_CLOB_HANDLE` for [CLOBs](../../abap-glossary/abenclob_glosry.md)

The additions `READER` and `WRITER` cannot be used together in the statement [`TYPES`](abaptypes_lob_handle.md). Furthermore, `WRITER` cannot be used together with `LOB HANDLE`.

The combination options with the column specifications [`lob_handle_columns`](abaptypes_lob_handle_columns.md) are explained in the statement [`TYPES`](abaptypes_lob_handle.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of various LOB-Handle components for the individual columns of a database table `DEMO_LOB_TABLE`.

``` abap
TYPES lob_handle TYPE demo_lob_table 
                 READER FOR COLUMNS blob1 
                 LOCATOR FOR COLUMNS blob2 
                 LOB HANDLE FOR COLUMNS blob3.
```

## Executable Example

[Deriving LOB Handle Structures](abentypes_lob_handle_abexa.md)
