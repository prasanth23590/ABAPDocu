---
title: "IMPORT, parameter_list"
source_file: abapimport_parameterlist.html
section: "ABAP Programming Language > ABAP - Data Cluster > IMPORT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# IMPORT, parameter_list

## Syntax

``` abap
... {p1 = dobj1 p2 = dobj2 ...}   
  | {p1 TO dobj1  p2 TO dobj2 ...}   
  | (ptab) ...  
```

### Addition

[1. `... p1 = dobj1 p2 = dobj2 ...`](abapimport_parameterlist.md#addition-1)

[2. `... p1 TO dobj1 p2 TO dobj2 ...`](abapimport_parameterlist.md#addition-2)

[3. `... (ptab)`](abapimport_parameterlist.md#addition-3)

## Overview

### Description

A [data cluster](../../abap-glossary/abendata_cluster_glosry.md) can be read statically using a parameter list in the form `p1 = dobj1 p2 = dobj2 ...` or `p1 TO dobj1 p2 TO dobj2 ...` and dynamically by specifying a parenthesized internal table `ptab`. Here the system searches the data cluster for data stored under the names `p1`, `p2`, .... If specified statically as `b1`, `b2`, ..., the system searches for the names in uppercase letters. If specified dynamically in `rtab`, the system searches for the names in the case used there.

If a parameter `p1`, `p2`, ... is specified that is not stored in the data cluster, the specification is ignored and the data object `dobj` retains its current value. By default, the data objects `dobj` must have the same data type as the parameter `p1`, `p2`, ... of the cluster. In internal tables, only the row type and not the table category is relevant. The following exceptions apply:

- With data objects of the type `c`, different lengths are allowed. In this case, the appropriate conversion rule from the [conversion table for source field type `c`](../abap-processing-internal-data/abenconversion_type_c.md) applies.

- Data of type `n` can be imported into data objects of type `c` if they have the same length.

- If the data types of all components of a structure, except for the last one, match and this component is of the type `c`, it can be lengthened or shortened in accordance with the conversion rule from the conversion table for source field type `c`. [Alignment gaps](../../abap-glossary/abenalignment_gap_glosry.md) in front of this component are considered part of the component.

- In the case of structures, it is enough that the initial part of a target structure has the same type as the source structure in the data cluster. After this, the target structure can contain further components at the highest level. In imports, the surplus components are filled with their [initial values](../../abap-glossary/abeninitial_value_glosry.md). A substructure of the target structure must not, however, have more components than the corresponding substructure in the source structure.

- Data objects of the [base type](../../abap-glossary/abenbase_type_glosry.md) of an [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) stored in the cluster can be imported into an enumerated variable if the imported value is a valid [enumerated value](../../abap-glossary/abenenumerated_value_glosry.md) of the [enumerated type](../../abap-glossary/abenenum_type_glosry.md). This includes any stored enumerated objects and regular elementary data objects of the basic type. But stored enumerated objects cannot be imported into data objects of their base type.

When structures are exported, the information indicating whether the structure contains components inherited using the statement [`INCLUDE`](../abap-declarations/abapinclude_type.md) or inherited from other substructures in the ABAP Dictionary is stored. A structure into which data is imported must also match the structure in the data cluster with respect to the components applied using `INCLUDE`. Only for structures that were stored prior to ABAP release 6.10 and structures where all the components of the uppermost hierarchy level were transferred using `INCLUDE` does the target structure not necessarily need to be set up with the same `INCLUDE` statements.

When importing from internal tables with non-unique [table keys](../abap-data-types-and-data-objects/abenitab_key.md), the order of duplicate rows in relation to these keys is not retained.

The additions specified under [`conversion_options`](abapimport_conversion.md) allow additional conversions and define other conversion rules.

### Hint

The rule that a target structure at the highest level may have more components than the source structure can cause problems in relation to structures defined in the ABAP Dictionary if the structure there is marked as enhanceable. Therefore, this situation raises a warning from the extended program check.

## Addition 1

`... p1 = dobj1 p2 = dobj2 ...`

## Addition 2

`... p1 TO dobj1 p2 TO dobj2 ...`

### Description

In the static case, the content is read from the data objects stored in the data cluster under the names `p1`, `p2`, ..., and these content is passed to the `dobj` data objects. The system searches for the names `p1`, `p2`, ... in uppercase letters in the data cluster. The specifications `p1 = dobj1 p2 = dobj2 ...` and `p1 TO dobj1 p2 TO dobj2 ...` have the same meaning.

### Hints

- The use of `=` is recommended rather than `TO`, since `=` is also used by other ABAP statements to inherit data.

- In the static case, it is not possible to read any data objects with names containing lowercase letters. These names can be defined using the dynamic variant of the [parameter list](abapexport_data_cluster_param.md) for statement `EXPORT`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Static import of data stored using the dynamic variant of the [parameter list](abapexport_data_cluster_param.md) of the statement `EXPORT`. The data can be read with the static variant of the parameter list for the statement `IMPORT`, because the data names only contain uppercase characters.

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
 
FINAL(ptab) = VALUE ptab( 
  ( name = `NUM1` dobj = `num1` ) 
  ( name = `NUM2` dobj = `num2` ) 
  ( name = `NUM3` dobj = `num3` ) ). 
 
EXPORT (ptab) 
       TO DATA BUFFER buffer. 
 
... 
 
IMPORT num1 = num1 num2 = num2 num3 = num3 
  FROM DATA BUFFER buffer. 
 
out->write( |{ num1 }, { num2 }, { num3 }| ). 
 
out->display( ).
```

## Addition 3

`... (ptab)`

### Description

In the dynamic case, the parameter list is inherited from the two-column internal table `ptab`, whose columns must be character-like. The first column in `ptab` must list the names of the parameters, and the second must list the data objects in any case. The system searches in the data cluster for the exact names and cases specified in the first column of `ptab`. If the second column is initial, the name of the parameter in the first column must match the name of a data object. Then the content found under this name is assigned to the corresponding data object. If the first column of `ptab` is initial or an object name occurs twice, an uncatchable exception is raised.

### Hints

- To read data objects with the dynamic variant that were stored using the static variant of the [parameter list](abapexport_data_cluster_param.md) of the statement `EXPORT`, the names of these data objects must be specified in uppercase letters. Any names containing lowercase letters can only be read and written with the dynamic variants.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Dynamic import of data stored using the static variant of the [parameter list](abapexport_data_cluster_param.md) of the statement `EXPORT`. To read data with the dynamic variant of the parameter list of the statement `IMPORT`, the names must be specified in uppercase letters in the first column of `ptab`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA buffer TYPE xstring. 
 
DATA: 
  num1 TYPE i VALUE 1, 
  num2 TYPE i VALUE 2, 
  num3 TYPE i VALUE 3. 
 
EXPORT num1 = num1 num2 = num2 num3 = num3 
       TO DATA BUFFER buffer. 
 
... 
 
TYPES: 
  BEGIN OF pline, 
    name TYPE string, 
    dobj TYPE string, 
  END OF pline, 
  ptab TYPE TABLE OF pline WITH EMPTY KEY. 
 
FINAL(ptab) = VALUE ptab( 
  ( name = `NUM1` dobj = `num1` ) 
  ( name = `NUM2` dobj = `num2` ) 
  ( name = `NUM3` dobj = `num3` ) ). 
 
IMPORT (ptab) 
  FROM DATA BUFFER buffer. 
 
out->write( |{ num1 }, { num2 }, { num3 }| ). 
 
out->display( ).
```
