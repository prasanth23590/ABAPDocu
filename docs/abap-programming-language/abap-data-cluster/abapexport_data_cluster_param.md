---
title: "EXPORT, parameter_list"
source_file: abapexport_data_cluster_param.html
section: "ABAP Programming Language > ABAP - Data Cluster > EXPORT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# EXPORT, parameter_list

## Syntax

``` abap
... {p1 = dobj1 p2 = dobj2 ...}   
  | {p1 FROM dobj1 p2 FROM dobj2 ...}   
  | (ptab) ...  
```

### Addition

[1. `... p1 = dobj1 p2 = dobj2 ...`](abapexport_data_cluster_param.md#addition-1)

[2. `... p1 FROM dobj1 p2 FROM dobj2 ...`](abapexport_data_cluster_param.md#addition-2)

[3. `... (ptab)`](abapexport_data_cluster_param.md#addition-3)

## Overview

### Description

A [data cluster](../../abap-glossary/abendata_cluster_glosry.md) can be defined statically by a parameter list in the form `p1 = dobj1 p2 = dobj2 ...` or `p1 FROM dobj1 p2 FROM dobj2 ...` and dynamically by specifying a parenthesized internal table `ptab`. Here the system searches for the data stored in the data cluster under the names `p1`, `p2`, .... The case of the names in the data clusters depends on how they are specified in the ABAP runtime framework. If specified statically (`b1`, `b2`, ...), uppercase is used. If specified dynamically in `rtab`, the case used there is used.

If the data cluster is too big for the memory, an exception is raised.

## Addition 1

`... p1 = dobj1 p2 = dobj2 ...`

## Addition 2

`... p1 FROM dobj1 p2 FROM dobj2 ...`

### Description

In static cases, the content of the data objects `dobj` is stored under the names `p1`, `p2`, ... in the cluster. The name of a parameter `p1`, `p2`, ... is converted to uppercase letters and can have a maximum of 255 characters. The specifications `p1 = dobj1 p2 = dobj2 ...` and `p1 FROM dobj1 p2 FROM dobj2 ...` have the same meaning. All data types can be used for the data object `dobj`, except reference types or data types that contain reference types as components. When an [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) is used, the enumerated value is flagged as an enumerated type and saved in the basic type.

### Hints

- The use of `=` is recommended rather than `FROM`, since `=` is also used by other ABAP statements to pass data.

- To export objects referenced by reference variables, these can first be serialized using the statement [`CALL TRANSFORMATION`](../abap-data-interchange-formats/abapcall_transformation.md) and then exported. In instances of classes, the class must implement the interface `IF_SERIALIZABLE_OBJECT`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Export of three numbers to a byte string `buffer` and import of the same three numbers to the components of a structure.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA buffer TYPE xstring. 
EXPORT num1 = 1 num2 = 2 num3 = 3 
       TO DATA BUFFER buffer. 
 
... 
 
DATA: 
  BEGIN OF wa, 
    num1 TYPE i, 
    num2 TYPE i, 
    num3 TYPE i, 
  END OF wa. 
IMPORT num1 = wa-num1 num2 = wa-num2 num3 = wa-num3 
  FROM DATA BUFFER buffer. 
 
out->write( wa ). 
 
out->display( ).
```

## Addition 3

`... (ptab)`

### Description

In the dynamic case, the parameter list is specified in an index table `ptab` with two columns. These columns can have any name and must be of the type *character*. The first column in `ptab` must contain the names of the parameters, and the second must list the data objects in any case. The names of the data objects are used exactly as specified in the first column of `ptab`. If the second column is initial, the name of the parameter in the first column must match the name of a data object. The data object is then stored under its name in the cluster. If the first column of `ptab` is initial, an uncatchable exception is raised.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Dynamic export of data to a byte string `buffer`. The names in the first column of `ptab` contain lowercase letters, which means that the data can only be imported by being specified dynamically. The second column, on the other hand, is not case-sensitive.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA buffer TYPE xstring. 
TYPES: 
  BEGIN OF pline, 
    name TYPE string, 
    dobj TYPE string, 
  END OF pline, 
  ptab TYPE TABLE OF pline WITH EMPTY KEY. 
 
DATA: 
  num1 TYPE i VALUE 1, 
  num2 TYPE i VALUE 2, 
  num3 TYPE i VALUE 3. 
 
DATA(ptab) = VALUE ptab( 
  ( name = `Num1` dobj = `NUM1` ) 
  ( name = `Num2` dobj = `NUM2` ) 
  ( name = `Num3` dobj = `NUM3` ) ). 
 
EXPORT (ptab) 
       TO DATA BUFFER buffer. 
 
... 
 
DATA: 
  BEGIN OF wa, 
    num1 TYPE i, 
    num2 TYPE i, 
    num3 TYPE i, 
  END OF wa. 
 
ptab = VALUE ptab( 
  ( name = `Num1` dobj = `wa-num1` ) 
  ( name = `Num2` dobj = `wa-num2` ) 
  ( name = `Num3` dobj = `wa-num3` ) ). 
 
IMPORT (ptab) 
  FROM DATA BUFFER buffer. 
 
out->write( wa ). 
 
out->display( ).
```
