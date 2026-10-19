---
title: "TYPES, LOB HANDLE"
source_file: abaptypes_lob_handle.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPES, LOB HANDLE

## Syntax

``` abap
TYPES dtype TYPE dbtab|view 
                 lob_handle_type FOR lob_handle_columns 
                [lob_handle_type FOR lob_handle_columns 
                 ...                                   ].  
```

[`lob_handle_type`](abaptypes_lob_handle_type.md) · [`lob_handle_columns`](abaptypes_lob_handle_columns.md) · [`lob_handle_type`](abaptypes_lob_handle_type.md) · [`lob_handle_columns`](abaptypes_lob_handle_columns.md)

## Description

Derivation of a [LOB handle structure](../../abap-glossary/abenlob_handle_structure_glosry.md) as a work area for working with [streaming and locators in ABAP SQL](../abap-database-access/abenstreams_locators.md). `dbtab` expects a [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md) defined in the ABAP Dictionary or a [DDIC database view](../../abap-glossary/abendatabase_view_glosry.md) defined for `view` in ABAP Dictionary.

The column specifications [`lob_handle_columns`](abaptypes_lob_handle_columns.md) are used to determine [LOBs](../../abap-glossary/abenlob_glosry.md) from `dbtab`. The statement creates a deep structure that is constructed for all columns that are not among the specified columns exactly as it is constructed for a regular [`TYPE` reference](abaptypes_referring.md) to `dbtab`. For the LOBs included in the specified columns, a component with the same name is created as the [LOB handle component](../../abap-glossary/abenlob_handle_component_glosry.md). The [static type](../../abap-glossary/abenstatic_type_glosry.md) of the LOB handle components is a class or an interface that is determined by the type specification [`lob_handle_type`](abaptypes_lob_handle_type.md), to which the respective specified column is assigned.

The combination options of the additions specified under [`lob_handle_columns`](abaptypes_lob_handle_columns.md) and [`lob_handle_type`](abaptypes_lob_handle_type.md) are determined by the following rules:

- A LOB handle structure can be derived for either [reading](../abap-database-access/abenabap_sql_reading.md) or [writing](../abap-database-access/abenabap_sql_writing.md) ABAP SQL statements only.

  - A structure for reads can only contain the type specifications [`READER`](abaptypes_lob_handle_type.md), [`LOCATOR`](abaptypes_lob_handle_type.md), and [`LOB HANDLE`](abaptypes_lob_handle_type.md).

  - A structure for writes can only contain the type specifications [`WRITER`](abaptypes_lob_handle_type.md) and [`LOCATOR`](abaptypes_lob_handle_type.md).

- The definition of the LOB handle components must be mutually exclusive, which means that columns must not be assigned to inappropriate types or a column cannot be assigned to multiple types.

- The definition of LOB handle components must not contain redundancies. A set of LOB handle components must be produced for each specification of:

  ... [`lob_handle_type`](abaptypes_lob_handle_type.md) FOR [`lob_handle_columns`](abaptypes_lob_handle_columns.md) ... This set of LOB handle components must not overlap with another set of LOB handle components of a different specification.

- The definition of the LOB handle components must be specified with as few specifications as possible. If the same set of LOB handle components can be created by one rather than multiple specifications, the more comprehensive option must be used.

Apart from the rules specified under [`lob_handle_columns`](abaptypes_lob_handle_columns.md) and [`lob_handle_type`](abaptypes_lob_handle_type.md), the following general restrictions also apply:

- At least one column must be specified.

- The [type specifications](abaptypes_lob_handle_type.md) for the first three specified columns for LOB handle components for reads or the first two columns for LOB handle components for writes must be different

- In each case, only one [column specification](abaptypes_lob_handle_columns.md) `ALL ... COLUMNS` can be made, in which `BLOB` or `CLOB` are specified.

- The [column](abaptypes_lob_handle_columns.md) specification `ALL BLOB|CLOB COLUMNS` includes all BLOBs or CLOBs. When specified, a single BLOB or CLOB cannot be specified in a [column specification](abaptypes_lob_handle_columns.md) `COLUMNS ...` for the same [static type](abaptypes_lob_handle_type.md).

- The [column specification](abaptypes_lob_handle_columns.md) `ALL OTHER COLUMNS` includes all columns that are not specified individually. `ALL OTHER BLOB COLUMNS` or `ALL OTHER CLOB COLUMNS` cannot be specified at the same time.

- The [column specification](abaptypes_lob_handle_columns.md) `ALL COLUMNS` includes all LOBs and can therefore only be specified on its own.

## Hints

- LOB handle structures can also be defined using appropriate typing of components between [`BEGIN OF` and `END OF`](abaptypes_struc.md).

- If `dbtab` does not contain any LOBs that match the specified columns, no LOB handle components are created, and the statement creates a regular work area.

- If LOBs are added to `dbtab` that match the [specified columns](abaptypes_lob_handle_columns.md) `ALL [OTHER] ...`, LOB handle components are also created for these.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of types for work areas with LOB handle components for a writer stream and a reader stream for the column `PICTURE` and a locator for all LOBs in the DDIC database table `DEMO_BLOB_TABLE`.

``` abap
TYPES: 
  wa1 TYPE demo_blob_table WRITER FOR COLUMNS picture, 
  wa2 TYPE demo_blob_table READER FOR COLUMNS picture, 
  wa3 TYPE demo_blob_table LOCATOR FOR ALL COLUMNS.
```

## Executable Example

[Deriving LOB Handle Structures](abentypes_lob_handle_abexa.md)
