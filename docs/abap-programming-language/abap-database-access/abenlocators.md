---
title: "ABAP SQL - Locators"
source_file: abenlocators.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Streaming and Locators"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Locators

ABAP SQL supports [locators](../../abap-glossary/abenlocator_glosry.md) for [LOBs](../../abap-glossary/abenlob_glosry.md) in data sources.

- [System Classes for Locators](abenlocators.md#system-classes-for-locators)

  - [Important Methods](abenlocators.md#important-methods)

- [Creating Locators for LOBs](abenlocators.md#creating-locators-for-lobs)

- [Closing Locators](abenlocators.md#closing-locators)

- [Examples](abenlocators.md#examples)

## System Classes for Locators

The associated [system classes](../../abap-glossary/abensystem_class_glosry.md) for the two types of LOBs are:

- `CL_ABAP_DB_C_LOCATOR` for [CLOBs](../../abap-glossary/abenclob_glosry.md).

- `CL_ABAP_DB_X_LOCATOR` for [BLOBs](../../abap-glossary/abenblob_glosry.md).

The instances of the classes are [LOB handles](../../abap-glossary/abenlob_handle_glosry.md) and implement the [corresponding interfaces](abenlob_interfaces.md). Their use in ABAP SQL involves reference variables that point to LOB handles of this type.

### Important Methods

Locators contain the following methods. The actual access to LOBs is performed by the ABAP runtime framework.

**Methods in Both Locator Types**

- `GET_LENGTH` returns the length of the LOB that is bound to a locator.

- `FIND` searches from an offset for a substring of an LOB which is bound to a locator, and returns its position. The length of a character-like substring that can be found using `FIND` is limited to 1333 characters. The length of a binary substring is limited to 2666 bytes.

Methods from the `IF_ABAP_CLOSE_RESOURCE` interface:

- `CLOSE` closes the locator.

- `IS_CLOSED` returns *X*, if the locator is closed.

**Methods in Character-Like Locators**

- `GET_SUBSTRING` returns the substring specified using offset and length, of a CLOB which is bound to a locator.

**Methods in Binary Locators**

- `GET_BYTES` returns the substring, specified using offset and length, of a BLOB which is bound to a locator.

## Creating Locators for LOBs

A locator bound to an LOB, that is, an instance of the class `CL_ABAP_DB_C_LOCATOR` or `CL_ABAP_DB_X_LOCATOR`, can only be created by assigning a LOB from the result set to a reference variable for a locator in the [`INTO`](abapinto_clause.md) clause of the statement [`SELECT`](abapinto_clause.md).

See [`SELECT` - LOB Handles](abenselect_into_lob_handles.md).

### Hint

Locators cannot be created in modifying ABAP SQL statements. Locators created in a read statement can, however, be used to make changes.

## Closing Locators

Due to high resource consumption, locators must always be closed as soon as possible using their `CLOSE` method. Especially when creating locators in `SELECT` loops, it must be ensured that locators are not closed implicitly using `ENDSELECT`, unlike reader streams, and must be closed explicitly. Furthermore, locators are closed implicitly at the end of a database LUW.

## Examples

## Executable Examples

- [Locator, copy column](abendb_copy_abexa.md)
