---
title: "REPLACE substring WITH"
source_file: abapreplace_obsolete.html
section: "ABAP Programming Language > ABAP - Obsolete Language Elements > Obsolete Processing of Internal Data > Obsolete Character String and Byte String Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# REPLACE substring WITH

## Obsolete, deprecated Syntax

``` abap
REPLACE substring WITH new INTO dobj 
        [IN {BYTE|CHARACTER} MODE] 
        [LENGTH len].  
```

### Addition

[1. `... IN {CHARACTER|BYTE} MODE`](abapreplace_obsolete.md#addition-1)

[2. `... LENGTH len`](abapreplace_obsolete.md#addition-2)

**Caution**

***This syntax is only supported temporarily in the current ABAP language version and must be replaced with valid syntax for that version.***

## Overview

### Description

This statement searches a character string or byte chain `dobj` for the substring specified in `substring` and replaces the first character string or byte string in `dobj` that matches `substring` with the content of the data object `new`.

The memory areas of `substring` and `new` must not overlap, otherwise the result is undefined. If `substring` is an empty string, the position in front of the first character or byte of the search range is found and the content of `new` is inserted in front of the first character.

If the length of the intermediate result is longer than the length of `dobj`, data objects with fixed lengths are truncated on the right. If the length of the intermediate result is shorter than the length of `dobj`, data objects of fixed length are padded on the right with blanks or hexadecimal zeros. Data objects of variable length are adjusted accordingly.

In character string processing, the trailing blanks are respected for data objects `dobj`, `substring`, and `new` of type `c`, `d`, `n`, or `t`.

### System Fields

| **`sy-subrc`** | **Meaning**                                                                                            |
|----------------|--------------------------------------------------------------------------------------------------------|
| 0              | The substring in `substring` was replaced in the target field `dobj` by the content of `new`.          |
| 4              | The substring in `substring` could not be replaced in the target field `dobj` by the content of `new`. |

### Hint

This variant of the `REPLACE` statement has been replaced by the variant [`REPLACE`](../abap-processing-internal-data/abapreplace_in_pattern.md).

## Addition 1

`... IN {CHARACTER|BYTE} MODE`

### Description

The optional addition `IN {CHARACTER|BYTE} MODE` determines whether [character string or byte string processing](../abap-processing-internal-data/abenstring_processing_statements.md) is performed. If the addition is not specified, character string processing is carried out. Depending on the processing type, the data objects `substring`, `new`, and `dobj` must be character-like or byte-like.

## Addition 2

`... LENGTH len`

### Description

If the addition `LENGTH` is not specified, all the data objects involved are evaluated in their entire length. If the addition `LENGTH` is specified, only the first `len` characters or bytes of `substring` are used for the search. `len` expects a data object of the type `i`.
