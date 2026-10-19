---
title: "CALL METHOD, parameter_tables"
source_file: abapcall_method_parameter_tables.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > Method Calls > Dynamic Method Call > CALL METHOD"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CALL METHOD, parameter_tables

## Syntax

``` abap
... [PARAMETER-TABLE ptab]   
    [EXCEPTION-TABLE etab].  
```

### Addition

[1. `... PARAMETER-TABLE ptab`](abapcall_method_parameter_tables.md#addition-1)

[2. `... EXCEPTION-TABLE etab`](abapcall_method_parameter_tables.md#addition-2)

## Overview

### Description

In [dynamic method calls](abapcall_method_dynamic.md), these additions assign actual parameters and exceptions to the formal parameters and non-class-based exceptions using the special internal tables `ptab` and `etab`.

## Addition 1

`... PARAMETER-TABLE ptab`

### Description

`PARAMETER-TABLE` can be used to assign actual parameters to all formal parameters of a dynamically called method. `ptab` expects a [hashed table](../../abap-glossary/abenhashed_table_glosry.md) of table type `abap_parmbind_tab` or line type `abap_parmbind` from the [type pool](../../abap-glossary/abentype_pool_glosry.md) `ABAP`. When the statement `CALL METHOD` is executed, the table must contain exactly one line for each non-optional formal parameter. For each optional formal parameter, the table can contain one line. The table columns are:

- `NAME` of type `c` and length 30

  For the name of the relevant formal parameter in uppercase letters. If a nonexistent formal parameter is specified, a catchable exception is raised.

- `KIND` of type `c` of length 1.

  For the type of the formal parameter. This column is used to verify the interface. The type of the formal parameter is determined in the declaration of the called method. If `KIND` is initial, no check is performed. If `KIND` contains the value of a constant `EXPORTING`, `IMPORTING`, `CHANGING`, or `RECEIVING` of the class `CL_ABAP_OBJECTDESCR`, the system checks (from the perspective of the caller) whether the formal parameter specified in `NAME` is an input, output, input/output parameter, or a return value, and raises the catchable exception `CX_SY_DYN_CALL_ILLEGAL_TYPE` if an error occurs.

- `VALUE` of the type `REF TO data`

  For a pointer to an appropriate actual parameter. The data object to which the reference variable in `VALUE` points is assigned to the formal parameter specified in `NAME`.

The column `NAME` is the unique key of the table `ptab`. The table must not contain a line with a parameter name that does not exist in the method's parameter interface.

## Addition 2

`... EXCEPTION-TABLE etab`

### Description

`EXCEPTION-TABLE` can be used to assign return values to all [non-class-based exceptions](../abap-program-flow-logic/abenexceptions_non_class.md) of a dynamically called method. `etab` expects a [hashed table](../../abap-glossary/abenhashed_table_glosry.md) of table type `abap_excpbind_tab` or of line type `abap_excpbind` from the [type pool](../../abap-glossary/abentype_pool_glosry.md) `ABAP`. When the statement `CALL METHOD` is executed, this table can contain exactly one line for every non-class-based exception of the method. The table columns are:

- `NAME` of type `c` and length 30

  For the name of the respective exception or [`OTHERS`](abapcall_method_parameters.md) in uppercase letters.

- `VALUE` of type `i`

  For the numeric value that is to be available in `sy-subrc` after the exception specified in `NAME` is raised.

The column `NAME` is the unique key of table `etab`. The table must not contain a line with a exception name that does not exist in the method's parameter interface.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Dynamic method call with parameter and exception table. In ABAP for Cloud Development, non-class-based exceptions cannot be defined anymore. Passing an exception table is necessary when calling methods of classes written in Standard ABAP.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(class) = `CLS`. 
FINAL(meth) = `METH`. 
 
FINAL(ptab) = VALUE abap_parmbind_tab( 
  ( name  = 'P' 
    kind  = cl_abap_objectdescr=>exporting 
    value = REF #( `Hello method!` ) ) ). 
 
FINAL(etab) = VALUE abap_excpbind_tab( 
  ( name = 'E' value = 4 ) ). 
 
CALL METHOD (class)=>(meth) 
  PARAMETER-TABLE ptab 
  EXCEPTION-TABLE etab. 
IF sy-subrc <> 0. 
  out->write( `Exception caught ...` ). 
ENDIF. 
 
out->display( ).
```
