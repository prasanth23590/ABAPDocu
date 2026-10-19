---
title: "EXPORT"
source_file: abapexport_data_cluster.html
section: "ABAP Programming Language > ABAP - Data Cluster"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# EXPORT

## Syntax

``` abap
EXPORT parameter_list TO medium [COMPRESSION {ON|OFF}].  
```

[`parameter_list`](abapexport_data_cluster_param.md) · [`medium`](abapexport_data_cluster_medium.md)

### Addition

[`... COMPRESSION {ON|OFF}`](abapexport_data_cluster.md#addition)

## Overview

### Description

This statement stores a [data cluster](../../abap-glossary/abendata_cluster_glosry.md) defined using [`parameter_list`](abapexport_data_cluster_param.md) in a memory medium [`medium`](abapexport_data_cluster_medium.md). The addition `COMPRESSION` can be used to control whether the data is stored in the cluster in compressed form. A data cluster can be read from the memory medium using the statement [`IMPORT`](abapimport_data_cluster.md).

All data objects are archived according to the current [byte order](../../abap-glossary/abenbyte_order_glosry.md) (endian) and character-like data objects according to the [character format](../../abap-glossary/abenchar_representation_glosry.md) of the current [text environment](../../abap-glossary/abentext_environment_glosry.md). The ID of the data cluster indicates which byte order and character format have been used during the export. When the data cluster is imported using the `IMPORT` statement, this ID is evaluated, and the data is converted to the current byte order and character representation.

A data cluster can have a maximum of 2 GB. Any attempts to export more than 2 GB raise a catchable exception of the class `CX_SY_COMPRESSION_ERROR`. If a different resource bottleneck occurs earlier, however, its related exception can be raised first.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Export of an internal table to a byte string `buffer` and import of the content to another internal table.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA buffer TYPE xstring. 
SELECT * 
       FROM scarr 
       INTO TABLE @FINAL(itab). 
 
EXPORT scarr = itab TO DATA BUFFER buffer. 
 
... 
 
DATA jtab LIKE itab. 
IMPORT scarr = jtab FROM DATA BUFFER buffer. 
 
out->write( jtab ). 
 
out->display( ).
```

## Addition

`... COMPRESSION {ON|OFF}`

### Description

This addition determines whether the data in the data cluster is compressed. By default, compression is deactivated for all memory media [`medium`](abapexport_data_cluster_medium.md), except database tables. If compression is required, it must be switched on using `ON`. If stored in a database table, compression is switched on by default and is only switched off if `OFF` is specified.

### Hints

- When a data cluster is imported using [`IMPORT`](abapimport_data_cluster.md), the system automatically recognizes whether or not the data is compressed.

- Compression saves space, but it is more time-consuming.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Export of the compressed result of an XML serialization of an object to a byte string and then importing it.

``` abap
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES if_serializable_object. 
    DATA attr TYPE i. 
    METHODS constructor IMPORTING p TYPE i. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS cls IMPLEMENTATION. 
  METHOD constructor. 
    attr = p. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    DATA(oref) = NEW cls( 123 ). 
    DATA buffer TYPE xstring. 
    CALL TRANSFORMATION id SOURCE oref = oref 
                           RESULT XML DATA(xml). 
 
    EXPORT xml = xml TO DATA BUFFER buffer COMPRESSION ON. 
 
    ... 
 
    CLEAR oref. 
    IMPORT xml = xml FROM DATA BUFFER buffer. 
 
    CALL TRANSFORMATION id SOURCE XML xml 
                           RESULT oref = oref. 
 
    out->write( oref->attr ). 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```
