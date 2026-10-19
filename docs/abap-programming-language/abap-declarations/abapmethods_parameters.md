---
title: "METHODS, parameters"
source_file: abapmethods_parameters.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Methods > METHODS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# METHODS, parameters

## Syntax

``` abap
... { VALUE(p1) | REFERENCE(p1) | p1 } 
        typing   [OPTIONAL|{DEFAULT def1}]   
    { VALUE(p2) | REFERENCE(p2) | p2 } 
        typing   [OPTIONAL|{DEFAULT def2}]   
    ...  
```

[`typing`](abentyping_syntax.md) · [`typing`](abentyping_syntax.md)

### Addition

[`... OPTIONAL|{DEFAULT def}`](abapmethods_parameters.md#addition)

## Overview

### Description

Definition of formal parameters `p1 p2 ...` for methods.

`VALUE` or `REFERENCE` determine whether a parameter `p1 p2 ...` is passed by [value](../../abap-glossary/abenpass_by_value_glosry.md) or by [reference](../../abap-glossary/abenpass_by_reference_glosry.md). If only one name `p1 p2 ...` is specified, the parameter is passed by reference by default. An input parameter passed by reference cannot be changed in the method.

The addition `typing` must be used to type every formal parameter. The syntax of `typing` is described in [Typing Syntax](abentyping_syntax.md). The typing of a formal parameter causes the data type to be [checked](abentyping_check.md) against the typing when an actual parameter is passed. The typing also defines in which operand positions the formal parameter can be used in the method.

### Hint

If a formal parameter is typed as a reference variable and cannot be changed in the [procedure](../../abap-glossary/abenprocedure_glosry.md), the type check is performed as for an [upcast](../../abap-glossary/abenup_cast_glosry.md). If it can be changed in the procedure, the actual parameter must be compatible with the formal parameter.

## Addition

`... OPTIONAL|{DEFAULT def}`

### Description

`OPTIONAL` or `DEFAULT` can be used to define input parameters and input/output parameters as optional parameters, where `DEFAULT` can be used to specify a replacement parameter `def1`, `def2`, ... No actual parameter needs to be specified for an optional parameter when the method is called.

The addition `OPTIONAL` is used to initialize a formal parameter in a type-compliant way, but the addition `DEFAULT` passes the value and type of the replacement parameter `def1 def2 ...` to the formal parameter. Any data object that is visible here that complies with the rules for [checking typing](abentyping_check.md) can be specified as replacement parameters `def1 def2 ...`, with the exception of the components of [boxed components](../../abap-glossary/abenboxed_component_glosry.md).

If no actual parameter is specified for a generically typed formal parameter using the addition `OPTIONAL` when it is called, the type of the formal parameter is completed according to the [rules for generic types](abentyping_generic.md).

### Hint

If a literal is specified after `DEFAULT`, the same special rules apply as to [literals as actual parameters](abentyping_literals.md). Afterwards, the compatibility may not then be checked completely. Instead, in method calls where no actual parameter is specified for the formal parameter, a literal is converted to the data type of the formal parameter and an exception can be raised if the value of the literal does not fit in the value range of this data type.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of a method with two different specifications of input parameters. The specification of `REFERENCE(p2)` has the same meaning as `p2`.

``` abap
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    METHODS 
      meth 
        IMPORTING 
          p1            TYPE i 
          REFERENCE(p2) TYPE i DEFAULT 111 
          VALUE(p3)     TYPE i OPTIONAL. 
    ... 
ENDCLASS. 
 
CLASS cls IMPLEMENTATION. 
  METHOD meth. 
    ... 
  ENDMETHOD. 
  ... 
ENDCLASS.
```
