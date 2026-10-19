---
title: "TYPES, TABLE OF"
source_file: abaptypes_itab.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPES, TABLE OF

## Syntax

``` abap
TYPES table_type { {TYPE tabkind OF [REF TO] type}   
                 | {LIKE tabkind OF dobj} }   
                 [tabkeys]   
                 [INITIAL SIZE n].   
```

[`tabkind`](abaptypes_tabcat.md) · [`tabkind`](abaptypes_tabcat.md) · [`tabkeys`](abaptypes_keydef.md)

### Addition

[`... INITIAL SIZE n`](abaptypes_itab.md#addition)

## Overview

### Description

This statement defines a table type `table_type` with a specific line type, a table category `tabkind`, and table keys `tabkeys`.

The line type is determined by entering the data type `type` after `TYPE` and data type `dobj` after `LIKE`:

- `type` can be a non-generic data type from ABAP Dictionary, a non-generic public data type of a public data type of a global class, a non-generic data type local to a program, a [CDS simple type](../../abap-glossary/abencds_simple_type_glosry.md), or any ABAP type from the [tables](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) of [built-in ABAP types](../../abap-glossary/abenbuiltin_abap_type_glosry.md). The generic ABAP types `c`, `n`, `p`, and `x` are extended implicitly to the standard length without [decimal places](../../abap-glossary/abendecimal_place_glosry.md) from the [tables](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) of built-in ABAP types.

  If the addition `REF TO` is specified before `type` or `dobj`, the line type is a reference type. The information specified in the section [reference types](abaptypes_references.md) can then be specified for `type` and `dobj`.

- The same applies to `dobj` as to [`TYPES ... LIKE`](abaptypes_referring.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of a non-generic sorted table type. The line type corresponds to the structure of the database table `SPFLI`. Two key fields are defined for the primary table key.

``` abap
TYPES spfli_sort TYPE SORTED TABLE OF spfli 
      WITH UNIQUE KEY carrid connid.
```

## Addition

`... INITIAL SIZE n`

### Description

The optional addition `INITIAL SIZE` has two meanings:

- **Initial Memory Requirement**

  The addition `INITIAL SIZE` affects the [initial memory requirement](../../abap-glossary/abeninitial_mem_req_glosry.md) of an internal table of the table type. A number of lines `n` can be specified directly as a positive number without +/- sign or as a numeric constant to give the ABAP runtime framework a hint for the size of the initial memory requirement. In the following cases, the ABAP runtime framework allocates the initial memory area implicitly by itself:

  - The addition `INITIAL SIZE` is not used.

  - A value of 0 is specified for `n`.

  - If the value of `n` would cause the initial blocks to become too big.

- **Size of Ranking Lists**

  To create a ranking list in the internal table using the addition [`SORTED BY`](../abap-processing-internal-data/abapappend.md) of the statement [`APPEND`](../abap-processing-internal-data/abapappend.md), a value greater than 0 must be specified after `INITIAL SIZE`. This value determines the size of the ranking list.

### Hints

- Specifying the initial memory requirement is only recommended if the number of entries in the table has been determined in advance and the initial main memory requirement is to be dimensioned in the most suitable way. This can be especially important for internal tables that are components of table types and only contain a few lines.

- Instead of `APPEND SORTED BY`, the statement `SORT` should be used so that the addition `INITIAL SIZE` is no longer necessary.
