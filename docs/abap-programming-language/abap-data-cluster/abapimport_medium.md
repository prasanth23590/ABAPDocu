---
title: "IMPORT, medium"
source_file: abapimport_medium.html
section: "ABAP Programming Language > ABAP - Data Cluster > IMPORT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# IMPORT, medium

## Syntax

``` abap
... { DATA BUFFER xstr }   
  | { INTERNAL TABLE itab }   
...
```

### Alternative

[1. `... DATA BUFFER xstr`](abapimport_medium.md#alternative-1)

[2. `... INTERNAL TABLE itab`](abapimport_medium.md#alternative-2)

## Overview

### Description

The [data cluster](../../abap-glossary/abendata_cluster_glosry.md) to be imported can be taken from an elementary data object `xstr` or an internal table `itab`.

## Alternative 1

`... DATA BUFFER xstr`

### Description

If `DATA BUFFER` is specified, the data cluster is taken from the elementary data object `xstr`, which must be of the type `xstring`. The data object must contain a data cluster that was created using the `DATA BUFFER` addition of the [`EXPORT`](abapexport_data_cluster_medium.md) statement. Otherwise, a [runtime error](abenrabax_import_from_database.md) occurs. The data object must not be initial.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

See the example for the addition [`DATA BUFFER`](abapexport_data_cluster_medium.md) of the statement `EXPORT`.

## Alternative 2

`... INTERNAL TABLE itab`

### Description

If `INTERNAL TABLE` is specified, the data cluster is taken from the internal table `itab`. The first column of `itab` must have the data type [`s`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) or [`i`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) and the second column must have the type [`x`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md). The only table category allowed for `itab` are [standard tables](../../abap-glossary/abenstandard_table_glosry.md) without [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md). The internal table must contain a data cluster created using the `INTERNAL TABLE` addition of the [`EXPORT`](abapexport_data_cluster_medium.md) statement; otherwise, a [runtime error](abenrabax_import_from_database.md) occurs. The internal table must not be empty.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

See the example for the addition [`INTERNAL TABLE`](abapexport_data_cluster_medium.md) of the statement `EXPORT`.

,, This syntax is not available in the current ABAP language version. ,, This syntax is not available in the current ABAP language version. ,, This syntax is not available in the current ABAP language version.
