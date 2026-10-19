---
title: "EXPORT, medium"
source_file: abapexport_data_cluster_medium.html
section: "ABAP Programming Language > ABAP - Data Cluster > EXPORT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# EXPORT, medium

## Syntax

``` abap
... { DATA BUFFER xstr } 
  | { INTERNAL TABLE itab } 
 ...  
```

### Alternative

[1. `... DATA BUFFER xstr`](abapexport_data_cluster_medium.md#alternative-1)

[2. `... INTERNAL TABLE itab`](abapexport_data_cluster_medium.md#alternative-2)

## Overview

### Description

The exported [data cluster](../../abap-glossary/abendata_cluster_glosry.md) can be stored in a byte string `xstr` or in an internal table `itab`.

## Alternative 1

`... DATA BUFFER xstr`

### Description

If `DATA BUFFER` is specified, the data cluster is written to the elementary data object `xstr`, which must be of the type `xstring`. The previous content of `xstr` is overwritten completely.

### Hints

- A data object `xstr` filled by `EXPORT TO DATA BUFFER` contains exactly one data cluster.

- A common application of the addition `DATA BUFFER` is to store the new data cluster in a field of a DDIC database table with the corresponding data type. In this case, compressing the data cluster using the addition [`COMPRESSION`](abapexport_data_cluster.md) should be considered, since, by default, compression as a medium is only activated if `DATABASE` is specified directly.

- Another application is to pass data clusters to an `xstring` typed procedure parameter and evaluate them there. This can be used for example in RFC in order to pass large amounts of complex data to remote systems.

- The content of a data object filled by `EXPORT TO DATA BUFFER` can only be evaluated using `IMPORT FROM DATA BUFFER`. In other evaluations, for example when comparing data clusters, the result is undefined. For example, the undefined content of [alignment gaps](../../abap-glossary/abenalignment_gap_glosry.md) in structures can produce different data clusters with structures that otherwise have the same content.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Export of an internal table to a byte string and storing it in a database table. After the byte string is read from the DDIC database table, the content of the data cluster can be imported into another internal table.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT * 
       FROM scarr 
       INTO TABLE @FINAL(itab). 
 
DATA buffer TYPE xstring. 
EXPORT itab = itab TO DATA BUFFER buffer. 
 
MODIFY demo_expressions FROM @( 
  VALUE #( id = 'B' xstring1 = buffer ) ). 
 
... 
 
DATA jtab TYPE TABLE OF scarr WITH EMPTY KEY. 
SELECT SINGLE xstring1 
       FROM demo_expressions 
       WHERE id = 'B' 
       INTO @buffer. 
 
IF sy-subrc = 0. 
  IMPORT itab = jtab FROM DATA BUFFER buffer. 
ENDIF. 
IF sy-subrc = 0. 
  out->write( jtab ). 
ENDIF. 
 
out->display( ).
```

## Alternative 2

`... INTERNAL TABLE itab`

### Description

If `INTERNAL TABLE` is specified, the data cluster is stored in the internal table `itab`. The previous content of `itab` is overwritten completely.

The first column of `itab` must have the data type [`s`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) or [`i`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md) and the second column must have the type `x`. Depending on the width of the second column, the data is stored across multiple table lines if necessary. The first column contains the length occupied in the second column. The only table category allowed for `itab` are [standard tables](../../abap-glossary/abenstandard_table_glosry.md) without [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md).

### Hints

- An internal table `itab` filled by `EXPORT TO INTERNAL TABLE` contains exactly one data cluster.

- The content of an internal table filled by `EXPORT TO INTERNAL TABLE` can only be evaluated using `IMPORT FROM INTERNAL TABLE` for the same reasons as for `EXPORT TO DATA BUFFER`.

- The variant `EXPORT TO DATA BUFFER` is preferred over the variant `EXPORT TO INTERNAL TABLE` because it is easier to handle. An export to an internal table is beneficial only for very large data clusters and if the available [memory](../abap-data-types-and-data-objects/abenmemory_consumption_2.md) is almost used up. This is because its memory is requested block by block, while the memory for a string must always be available in one piece.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Export of an internal table to a data cluster in an internal table and importing it into another internal table.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF bline, 
    id    TYPE i, 
    clstr TYPE x LENGTH 100, 
  END OF bline. 
 
SELECT * 
       FROM scarr 
       INTO TABLE @FINAL(itab). 
 
DATA buffer TYPE TABLE OF bline WITH EMPTY KEY. 
EXPORT itab = itab TO INTERNAL TABLE buffer. 
 
... 
 
DATA jtab TYPE TABLE OF scarr WITH EMPTY KEY. 
IMPORT itab = jtab FROM INTERNAL TABLE buffer. 
IF sy-subrc = 0. 
  out->write( jtab ). 
ENDIF. 
 
out->display( ).
```

,, This syntax is not available in the current ABAP language version. ,, This syntax is not available in the current ABAP language version. ,, This syntax is not available in the current ABAP language version.
