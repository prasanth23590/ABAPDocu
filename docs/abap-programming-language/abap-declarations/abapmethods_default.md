---
title: "METHODS, DEFAULT"
source_file: abapmethods_default.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Methods > METHODS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# METHODS, DEFAULT

## Syntax

``` abap
METHODS meth ... DEFAULT IGNORE|FAIL ...  
```

## Description

The addition `DEFAULT` makes the explicit implementation of an interface method optional and defines a default behavior for calls of non-implemented methods. It cannot be used in classes, only in interfaces. All instance methods and static methods can be defined as optional except for constructors and test methods.

A class that implements an interface with the statement [`INTERFACES`](abapinterfaces.md) can implement its optional methods, but this is not mandatory. The additions `IGNORE` or `FAIL` define the behavior that applies when an optional interface method of an object or class is called at runtime and this object or class is not implemented explicitly.

- When a non-implemented optional interface method defined with the addition `IGNORE` is called, the behavior is the same as when it is implemented with an empty body. In particular, all actual parameters are initialized that receive values from formal parameters using [pass by value](../../abap-glossary/abenpass_by_value_glosry.md).

- Calls of a non-implemented optional interface method defined using the addition `FAIL` raise an exception of the class `CX_SY_DYN_CALL_ILLEGAL_METHOD` and, if not handled, results in a runtime error `CALL_METHOD_NOT_IMPLEMENTED` occurs.

The default behavior defined using `DEFAULT` also applies to the redefinition of an inherited optional interface method using the addition [`REDEFINITION`](abapmethods_redefinition.md). A subclass that redefines an optional interface method does not need to implement it explicitly. If the implementation is missing, the default behavior is applied along a path of the inheritance tree until an explicit implementation occurs.

## Hints

- The `DEFAULT` addition can also be used for [BAdI methods](../../abap-glossary/abenbadi_method_glosry.md).

- The default behavior defined using `DEFAULT FAIL` that applies to calls of a non-implemented optional method matches the behavior of calling a non-implemented non-optional method of a regular global interface. In a [BAdI interface](../../abap-glossary/abenbadi_interface_glosry.md) on the other hand, `DEFAULT IGNORE` matches the default behavior of the [`CALL BADI`](../abap-enhancements/abapcall_badi.md) statement.

- If an optional interface method is redefined in a subclass, it should also be implemented explicitly in this subclass. The default behavior is usually not as expected.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The class `class` implements the interface `intf` without implementing its optional methods. A call of the non-implemented static method `m1` raises a handled exception, due to the addition `FAIL`. A call of the non-implemented instance method `m2` does not execute any statements due to the addition `IGNORE`, but sets their return value `r` to 0.

``` abap
INTERFACE intf. 
  CLASS-METHODS m1 DEFAULT FAIL. 
  METHODS       m2 DEFAULT IGNORE 
    RETURNING VALUE(r) TYPE i. 
ENDINTERFACE. 
 
CLASS class DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES intf. 
    ALIASES m1 FOR intf~m1. 
    ALIASES m2 FOR intf~m2. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS class IMPLEMENTATION. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    DATA oref TYPE REF TO class. 
    TRY. 
        class=>m1( ). 
      CATCH cx_sy_dyn_call_illegal_method INTO FINAL(exc). 
        out->write( exc->get_text( ) ). 
        return. 
    ENDTRY. 
 
    out->write( NEW class( )->m2( ) ). 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```
