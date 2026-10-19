---
title: "DATA, LOB HANDLE"
source_file: abapdata_lob_handle.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects > DATA"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DATA, LOB HANDLE

## Syntax

``` abap
DATA dtype TYPE dbtab|view [READ-ONLY] 
                lob_handle_type FOR lob_handle_columns 
               [lob_handle_type FOR lob_handle_columns 
                ...                                   ].  
```

[`READ-ONLY`](abapdata_options.md) · [`lob_handle_type`](abaptypes_lob_handle_type.md) · [`lob_handle_columns`](abaptypes_lob_handle_columns.md) · [`lob_handle_type`](abaptypes_lob_handle_type.md) · [`lob_handle_columns`](abaptypes_lob_handle_columns.md)

## Description

Derivation of a [LOB handle structure](../../abap-glossary/abenlob_handle_structure_glosry.md) as a work area for working with [streaming and locators in ABAP SQL](../abap-database-access/abenstreams_locators.md). `dbtab` expects a transparent [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md) or a [DDIC database view](../../abap-glossary/abendatabase_view_glosry.md) defined for `view` in the ABAP Dictionary.

The column specification [`lob_handle_columns`](abaptypes_lob_handle_columns.md) is used to determine [LOBs](../../abap-glossary/abenlob_glosry.md) from `dbtab` or `view` for which [LOB handle components](../../abap-glossary/abenlob_handle_component_glosry.md) are created in that structure whose static type is determined by the type specification [`lob_handle_type`](abaptypes_lob_handle_type.md).

The syntax and meaning of the additions are identical to the definition of LOB handle structures using the corresponding variant of the statement [`TYPES`](abaptypes_lob_handle.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of work areas with LOB handle components for a writer stream and a reader stream for the column `PICTURE` and for locators for all LOBs of the DDIC database table `DEMO_BLOB_TABLE`.

``` abap
DATA wa1 TYPE demo_blob_table WRITER FOR COLUMNS picture. 
DATA wa2 TYPE demo_blob_table READER FOR COLUMNS picture. 
DATA wa3 TYPE demo_blob_table LOCATOR FOR ALL COLUMNS.
```
