---
title: "CALL METHOD, parameter_list"
source_file: abapcall_method_parameter_list.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > Method Calls > Dynamic Method Call > CALL METHOD"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CALL METHOD, parameter_list

## Syntax

``` abap
... [EXPORTING  p1 = a1 p2 = a2 ...]   
    [IMPORTING  p1 = a1 p2 = a2 ...]   
    [CHANGING   p1 = a1 p2 = a2 ...]   
    [RECEIVING  r  = a  ]   
    [EXCEPTIONS [exc1 = n1 exc2 = n2 ...]   
                [OTHERS = n_others] ].  
```

## Description

The syntax and meaning of `parameter_list` of the [dynamic method call](abenmethod_calls_dynamic.md) is the same as for the explicit parameter specification of the [static method call](abapcall_method_static_short.md).

Other than for the static method call, the parameter names are not checked statically for the dynamic method call. Any wrongly written parameter name is recognized at runtime only and leads to an exception of class `CX_SY_DYN_CALL_PARAM_NOT_FOUND`. Also, the [typing](../abap-declarations/abentyping.md) rules cannot be checked statically but at runtime only.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following code snippet is syntactically correct but leads to an exception. The specification `(name)` gives the impression of a dynamic parameter specification but is nothing more than a misspelled parameter name.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(name) = `html_string`. 
 
TRY. 
    CALL METHOD ('CL_ABAP_BROWSER')=>('SHOW_HTML') 
      EXPORTING 
        (name) = `<html><body>Oh no ...</html></body>`. 
  CATCH cx_sy_dyn_call_param_not_found INTO FINAL(exc). 
    out->write( exc->get_text( ) ). 
ENDTRY. 
 
out->display( ).
```
