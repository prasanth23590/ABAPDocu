---
title: "CREATE OBJECT, parameter_tables"
source_file: abapcreate_object_para_tables.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > CREATE OBJECT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CREATE OBJECT, parameter_tables

## Syntax

``` abap
 ... [PARAMETER-TABLE ptab] 
    [EXCEPTION-TABLE etab].  
```

## Description

The additions `PARAMETER-TABLE` and `EXCEPTION-TABLE` are used to pass actual parameters dynamically to the instance constructor or assign return codes to the non-class-based exceptions.

These additions can only be used if the instantiated class is specified dynamically in `name`. They use special internal tables `ptab` and `etab` to assign actual parameters to the input parameters of the instance constructor or return codes to the non-class-based exceptions.

The syntax and semantics are the same as in the dynamic method calls using the statement [`CALL METHOD`](../abap-calling-and-exiting-program-units/abapcall_method_dynamic.md). The internal tables `ptab` and `etab` in particular must be defined with reference to the tables `abap_parmbind_tab` and `abap_excpbind_tab` from the [type pool](../../abap-glossary/abentype_pool_glosry.md) `ABAP`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following program section dynamically creates an object of a class `SOME_CLASS` whose instance constructor expects a reference variable of the static type `ANY_CLASS`. The program has correct syntax, but the object is created only in systems in which the classes also exist.

``` abap
CONSTANTS: 
  anycls  TYPE string VALUE `ANY_CLASS`, 
  somecls TYPE string VALUE `SOME_CLASS`, 
  param   TYPE string VALUE `PARA`. 
 
DATA dref TYPE REF TO data. 
TRY. 
    CREATE DATA dref TYPE REF TO (anycls). 
    CREATE OBJECT dref->* TYPE (anycls). 
  CATCH cx_sy_create_data_error 
        cx_sy_create_object_error. 
    ... 
ENDTRY. 
 
IF dref IS BOUND. 
  FINAL(ptab) = VALUE abap_parmbind_tab( 
    ( name  = param 
      kind  = cl_abap_objectdescr=>exporting 
      value =  REF #( dref->* ) ) ). 
ENDIF. 
 
DATA oref TYPE REF TO object. 
TRY. 
    CREATE OBJECT oref TYPE (somecls) PARAMETER-TABLE ptab. 
  CATCH cx_sy_create_object_error 
        cx_sy_dyn_call_parameter_error INTO FINAL(exc). 
    ... 
ENDTRY.
```
