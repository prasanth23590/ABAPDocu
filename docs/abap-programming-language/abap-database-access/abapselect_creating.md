---
title: "SELECT, CREATING"
source_file: abapselect_creating.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, INTO, APPENDING > SELECT, LOB Handles"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, CREATING

## Syntax

``` abap
... CREATING {  READER|LOCATOR FOR { COLUMNS blob1 blob2 ... clob1 clob2 ... } 
                                 | { ALL [OTHER] [BLOB|CLOB] COLUMNS } 
               [READER|LOCATOR FOR ...] }   
           | {  (crea_syntax) }  ...  
```

### Addition

[1. `... READER|LOCATOR`](abapselect_creating.md#addition-1)

[2. `... [ALL [OTHER] [BLOB|CLOB]] COLUMNS [blob1 blob2 ... clob1 clob2 ...]`](abapselect_creating.html#addition-2)

[3. `... (crea_syntax)`](abapselect_creating.md#addition-3)

## Overview

### Description

The addition `CREATING` must be specified after [`INTO`](abapinto_clause.md) or [`APPENDING`](abapinto_clause.md) when a reference variable for a [LOB handle](../../abap-glossary/abenlob_handle_glosry.md) is assigned to a [LOB](../../abap-glossary/abenlob_glosry.md) of the result set as a target field and the [static type](../../abap-glossary/abenstatic_type_glosry.md) of this reference variable is one of the following three [LOB interfaces](abenlob_interfaces.md):

- `IF_ABAP_DB_LOB_HANDLE`

- `IF_ABAP_DB_CLOB_HANDLE`

- `IF_ABAP_DB_BLOB_HANDLE`

The specifications after `CREATING` determine the class from which the associated LOB handles are created. For all other possible static types, the class can be determined from the static type and the LOB type. `CREATING` cannot be specified in this case.

The `CREATING` addition can be specified either statically or dynamically. In the static variant, the class and columns are determined using additions. In the dynamic variant, the syntax of the static variants is specified in `crea_syntax`.

The syntax and the rules for the additions after `CREATING` correspond to the type and columns specified for the derivation of LOB handle structures with [`TYPES`](../abap-declarations/abaptypes_lob_handle.md). Unlike the statement [`TYPES`](../abap-declarations/abaptypes_lob_handle.md), the [type specified](../abap-declarations/abaptypes_lob_handle_type.md) is limited here to `READER` and `LOCATOR`, and only components that are typed with a LOB interface are respected. The types specified for the first two specifications after `CREATING` must be different.

### Hint

The addition `CREATING` cannot be used in combination with SQL expressions that return [LOBs](../../abap-glossary/abenlob_glosry.md). It can only be used with LOB fields directly.

## Addition 1

`... READER|LOCATOR`

### Description

These additions determine the LOB handle class for each of the columns specified after it.

- `READER` creates [reader streams](../../abap-glossary/abenreader_stream_glosry.md) for all of the columns specified.

- `LOCATOR` creates [locators](../../abap-glossary/abenlocator_glosry.md) for all of the columns specified after it.

The assignment to the classes is the same as the [type specified](../abap-declarations/abaptypes_lob_handle_type.md) in the derivation of a LOB handle structure using [`TYPES`](../abap-declarations/abaptypes_lob_handle.md), except that here it is the [dynamic type](../../abap-glossary/abendynamic_type_glosry.md) that is determined and not the static type.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After a row is read, the dynamic type of `reader` is `CL_ABAP_DB_X_READER`.

``` abap
DATA reader TYPE REF TO if_abap_db_lob_handle. 
 
SELECT SINGLE picture 
       FROM demo_blob_table 
       WHERE name = '...' 
       INTO @reader CREATING READER FOR COLUMNS picture.
```

## Addition 2

`... [ALL [OTHER] [BLOB|CLOB]] COLUMNS [blob1 blob2 ... clob1 clob2 ...]`

### Description

These additions assign the previous type specifications to the columns of the result set. The meaning of the additions is the same as the [columns specified](../abap-declarations/abaptypes_lob_handle_columns.md) in the derivation of an LOB handle structure using [`TYPES`](../abap-declarations/abaptypes_lob_handle.md). The difference is that the set of columns used consists exactly of those columns from the result set that were assigned to a reference variable whose static type is an [LOB interface](abenlob_interfaces.md):

- Individual columns for which this is not the case must not be specified.

- The specification of `ALL ... COLUMNS` only respects such columns.

The combination options for columns specified with one another and with types specified are the same as for [`TYPES`](../abap-declarations/abaptypes_lob_handle.md). Specifically, the column specified as `ALL OTHER ...` must be the last column specified.

### Hints

- The specification of `ALL ... COLUMNS` also respects columns which are added by later enhancements to the data sources.

- The actual names must be used for the columns specified as `blob1`, `blob2`, `clob1`, `clob2`, .... The alias names defined using [`AS`](abapselect_list.md) are ignored.

- Columns of the type [`GEOM_EWKB`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) are not supported as [BLOBs](../../abap-glossary/abenblob_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Like the previous example, but the column `PICTURE` is selected automatically here.

``` abap
DATA reader TYPE REF TO if_abap_db_blob_handle. 
 
SELECT SINGLE picture 
       FROM demo_blob_table 
       WHERE name = '...' 
       INTO @reader CREATING READER FOR ALL BLOB COLUMNS.
```

## Addition 3

`... (crea_syntax)`

### Description

As an alternative to static variants, a data object `crea_syntax` can be specified in parentheses which contains the syntax of the static additions or is initial when executing the statement. The same applies to `crea_syntax` as to `column_syntax` when specifying columns dynamically in the [`SELECT` list](abapselect_list.md). If the content of `crea_syntax` is initial, the addition `CREATING` is ignored.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Like the previous example, but the items after `CREATING` are specified dynamically here.

``` abap
DATA reader TYPE REF TO if_abap_db_blob_handle. 
 
FINAL(crea_syntax) = `READER FOR ALL BLOB COLUMNS`. 
 
SELECT SINGLE picture 
       FROM demo_blob_table 
       WHERE name = '...' 
       INTO @reader CREATING (crea_syntax).
```
