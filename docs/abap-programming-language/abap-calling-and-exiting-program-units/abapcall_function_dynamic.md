---
title: "CALL FUNCTION, parameter_tables"
source_file: abapcall_function_dynamic.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > CALL FUNCTION > CALL FUNCTION func"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CALL FUNCTION, parameter_tables

## Syntax

``` abap
... [PARAMETER-TABLE ptab]   
    [EXCEPTION-TABLE etab] ...  
```

### Addition

[1. `... PARAMETER-TABLE ptab ...`](abapcall_function_dynamic.md#addition-1)

[2. `... EXCEPTION-TABLE etab ...`](abapcall_function_dynamic.md#addition-2)

## Overview

### Description

These additions use the special internal tables `ptab` and `etab` to assign actual parameters to the formal parameters of the function module and return values to the non-class-based exceptions dynamically.

## Addition 1

`... PARAMETER-TABLE ptab ...`

### Description

`PARAMETER-TABLE` can be used to assign actual parameters to all formal parameters of the called function module. `ptab` expects a [sorted table](../../abap-glossary/abensorted_table_glosry.md) of table type `abap_func_parmbind_tab` or line type `abap_func_parmbind` from the [type pool](../../abap-glossary/abentype_pool_glosry.md) `ABAP`. When the statement `CALL FUNCTION` is executed, the table must contain exactly one line for each non-optional formal parameter. This line is optional for each optional formal parameter. The table columns are:

- `name` of type `c` and length 30

  for the name of the corresponding formal parameter in uppercase letters. If a nonexistent formal parameter is specified, a catchable exception is raised.

- `kind` of type `i`

  for the type of the formal parameter. `kind` must contain the value of one of the following constants of the type pool `ABAP`:

  - `abap_func_exporting` for input parameters

  - `abap_func_importing` for output parameters

  - `abap_func_tables` for table parameters

  - `abap_func_changing` for input/output parameters

    If the type specified from the caller perspective does not match the actual type of the formal parameter, a catchable exception is raised.

- `value` of the type `REF TO data`

  as a pointer to an appropriate actual parameter. The data object to which the reference variable in `value` points is assigned to the formal parameter specified in `name`.

The columns `name` and `kind` form the unique key of the table `ptab`. A line with a parameter name that is not defined in the function module's parameter interface is ignored.

## Addition 2

`... EXCEPTION-TABLE etab ...`

### Description

`EXCEPTION-TABLE` can be used to assign return values to exceptions of the called function module that are not marked as exception classes. `etab` expects a [hashed table](../../abap-glossary/abenhashed_table_glosry.md) of table type `abap_func_excpbind_tab` or of line type `abap_func_excpbind` from the [type pool](../../abap-glossary/abentype_pool_glosry.md) `ABAP`. The table can contain exactly one line for each non-class-based exception of the function module when the statement `CALL FUNCTION` is executed. The table columns are:

- `name` of type `c` and length 30

  For the name of the respective exception, or `error_message`, or specifies `OTHERS` in uppercase letters.

- `value` of type `i`

  For the numeric value that is to be available in `sy-subrc` after the exception specified in `name` is handled

- `message` of type `REF TO data` (not used for general function call but for [remote function call](abapcall_function_destination_para.md))

The column `name` is the unique key of table `etab`. A line with an exception name that is not in the function module's parameter interface is ignored.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Call of the function module `GUI_DOWNLOAD` with dynamic pass by parameter The name of the function module is specified in the string `func` and the interface is supplied with data using the internal tables `ptab` and `etab`.

``` abap
DATA: line     TYPE c LENGTH 80, 
      text_tab LIKE STANDARD TABLE OF line, 
      filename TYPE string, 
      filetype TYPE c LENGTH 10, 
      fleng    TYPE i. 
 
DATA: func TYPE string, 
      ptab TYPE abap_func_parmbind_tab, 
      etab TYPE abap_func_excpbind_tab. 
 
func = 'GUI_DOWNLOAD'. 
filename = 'c:\temp\text.txt'. 
filetype = 'ASC'. 
 
ptab = VALUE #( ( name  = 'FILENAME' 
                  kind  = abap_func_exporting 
                  value = REF #( filename ) ) 
                ( name  = 'FILETYPE' 
                  kind  = abap_func_exporting 
                  value = REF #( filetype ) ) 
                ( name  = 'DATA_TAB' 
                  kind  = abap_func_tables 
                  value = REF #( text_tab ) ) 
                ( name  = 'FILELENGTH' 
                  kind  = abap_func_importing 
                  value = REF #( fleng ) ) ). 
 
etab = VALUE #( ( name = 'OTHERS' value = 10 ) ). 
 
CALL FUNCTION func 
  PARAMETER-TABLE ptab 
  EXCEPTION-TABLE etab. 
 
CASE sy-subrc. 
  WHEN 1. 
    ... 
  ... 
ENDCASE.
```
