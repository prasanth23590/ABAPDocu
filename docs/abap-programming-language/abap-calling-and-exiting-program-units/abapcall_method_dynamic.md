---
title: "CALL METHOD"
source_file: abapcall_method_dynamic.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > Method Calls > Dynamic Method Call"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CALL METHOD

## Syntax

``` abap
CALL METHOD dynamic_meth { parameter_list   
                         | parameter_tables }.  
```

[`dynamic_meth`](abapcall_method_meth_ident_dyna.md) · [`parameter_list`](abapcall_method_parameter_list.md) · [`parameter_tables`](abapcall_method_parameter_tables.md)

## Description

This statement calls the method specified dynamically in [`dynamic_meth`](abapcall_method_meth_ident_dyna.md) (Dynamic Invoke). Actual parameters are assigned to the formal parameters of the method, either statically using [`parameter_list`](abapcall_method_parameter_list.md) or dynamically using [`parameter_tables`](abapcall_method_parameter_tables.md).

## System Fields

Each method call sets the system field `sy-subrc` to 0 in the moment the method is called. Handling [non-class-based exceptions](../abap-program-flow-logic/abenexceptions_non_class.md) can change this value.

## Hints

- In the dynamic method call, the parameters are not passed in parentheses. The syntax of the dynamic method call is like that of a [function module call](abapcall_function_general.md).

- The statement `CALL METHOD` should now only be used for the dynamic method call. It is unnecessary, and therefore [obsolete](../abap-obsolete-language-elements/abapcall_method_static.md), for the [static method call](abenmethod_calls_static.md).

## Security Hint

If the name of a program unit is specified dynamically when it is called, and this name is passed to a program from outside, this a serious security risk. Any names passed to a program from outside must be checked thoroughly before being used in calls. The system class `CL_ABAP_DYN_PRG`, for example, can be used to do this.

## System Fields

The system field `sy-subrc` is set to 0 when a method is called. If a [non-class-based exception](../abap-program-flow-logic/abenexceptions_non_class.md) is raised and is handled by then assigning a value, `sy-subrc` is set to this value.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Dynamic call. The names of the class and method are specified in the strings `class` and `meth`. The interface parameters are passed using the internal table `ptab` and return values are assigned to the exceptions of the method using the table `etab`. Exceptions that are raised at the method call itself are handled in a [`TRY`](../abap-program-flow-logic/abaptry.md) control structure with statement [`CATCH`](../abap-program-flow-logic/abaptry.md).

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: line     TYPE c LENGTH 80, 
      text_tab LIKE STANDARD TABLE OF line, 
      filename TYPE string, 
      filetype TYPE c LENGTH 10, 
      fleng    TYPE i. 
 
DATA: meth  TYPE string, 
      class TYPE string, 
      ptab  TYPE abap_parmbind_tab, 
      etab  TYPE abap_excpbind_tab. 
 
DATA: exc_ref TYPE REF TO cx_sy_dyn_call_error. 
 
class    = 'CL_GUI_FRONTEND_SERVICES'. 
meth     = 'GUI_DOWNLOAD'. 
filename = 'c:\temp\text.txt'. 
filetype = 'ASC'. 
 
ptab = VALUE #( ( name  = 'FILENAME' 
                  kind  = cl_abap_objectdescr=>exporting 
                  value = REF #( filename ) ) 
                ( name  = 'FILETYPE' 
                  kind  = cl_abap_objectdescr=>exporting 
                  value = REF #( filetype ) ) 
                ( name  = 'DATA_TAB' 
                  kind  = cl_abap_objectdescr=>changing 
                  value = REF #( text_tab ) ) 
                ( name  = 'FILELENGTH' 
                  kind  = cl_abap_objectdescr=>importing 
                  value = REF #( fleng ) ) ). 
 
etab = VALUE #( ( name = 'OTHERS' value = 4 ) ). 
 
TRY. 
    CALL METHOD (class)=>(meth) 
      PARAMETER-TABLE 
        ptab 
      EXCEPTION-TABLE 
        etab. 
    CASE sy-subrc. 
      WHEN 1. 
        ... 
      ... 
    ENDCASE. 
  CATCH cx_sy_dyn_call_error INTO exc_ref. 
    out->write( exc_ref->get_text( ) ). 
ENDTRY. 
 
out->display( ).
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_NO_HANDLER`

- See [Class-Based Exceptions in Procedures](../abap-program-flow-logic/abenexceptions_procedures.md).

  *Runtime error:* `UNCAUGHT_EXCEPTION`

`CX_SY_DYN_CALL_EXCP_NOT_FOUND`

- *Cause:* Exception does not exist

  *Runtime error:* `DYN_CALL_METH_EXCP_NOT_FOUND`

`CX_SY_DYN_CALL_ILLEGAL_CLASS`

- *Cause:* Specified class does not exist

  *Runtime error:* `DYN_CALL_METH_CLASS_NOT_FOUND`

`CX_SY_DYN_CALL_ILLEGAL_METHOD`

- *Cause:* Method cannot be accessed.

  *Runtime error:* `CALL_METHOD_NOT_ACCESSIBLE`

- *Cause:* The called method is not yet implemented.

  *Runtime error:* `CALL_METHOD_NOT_IMPLEMENTED`

- *Cause:* Call of the static constructor

  *Runtime error:* `DYN_CALL_METH_CLASSCONSTRUCTOR`

- *Cause:* Call of the instance constructor

  *Runtime error:* `DYN_CALL_METH_CONSTRUCTOR`

- *Cause:* Method does not exist

  *Runtime error:* `DYN_CALL_METH_NOT_FOUND`

- *Cause:* Method is not static

  *Runtime error:* `DYN_CALL_METH_NO_CLASS_METHOD`

- *Cause:* Call of a non-visible method

  *Runtime error:* `DYN_CALL_METH_PRIVATE`

- *Cause:* Call of a non-visible method

  *Runtime error:* `DYN_CALL_METH_PROTECTED`

`CX_SY_DYN_CALL_ILLEGAL_TYPE`

- *Cause:* Type conflict during method call.

  *Runtime error:* `CALL_METHOD_CONFLICT_GEN_TYPE`

- *Cause:* Type conflict during method call.

  *Runtime error:* `CALL_METHOD_CONFLICT_TAB_TYPE`

- *Cause:* Type conflict during method call.

  *Runtime error:* `CALL_METHOD_CONFLICT_TYPE`

- *Cause:* Incorrect parameter type

  *Runtime error:* `DYN_CALL_METH_PARAM_KIND`

- *Cause:* Actual parameter cannot be filled

  *Runtime error:* `DYN_CALL_METH_PARAM_LITL_MOVE`

- *Cause:* Incorrect table type for a parameter

  *Runtime error:* `DYN_CALL_METH_PARAM_TAB_TYPE`

- *Cause:* Incorrect parameter type

  *Runtime error:* `DYN_CALL_METH_PARAM_TYPE`

`CX_SY_DYN_CALL_PARAM_MISSING`

- *Cause:* Missing actual parameter

  *Runtime error:* `DYN_CALL_METH_PARAM_MISSING`

- *Cause:* Parameter reference is empty

  *Runtime error:* `DYN_CALL_METH_PARREF_INITIAL`

`CX_SY_DYN_CALL_PARAM_NOT_FOUND`

- *Cause:* Incorrect parameter name

  *Runtime error:* `DYN_CALL_METH_PARAM_NOT_FOUND`

`CX_SY_REF_IS_INITIAL`

- *Cause:* Reference variable is initial

  *Runtime error:* `DYN_CALL_METH_REF_IS_INITIAL`
