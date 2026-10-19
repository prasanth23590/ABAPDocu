---
title: "Function Module Interface"
source_file: abenfunction.html
section: "ABAP Programming Language > ABAP - Program Structure > Modularization Statements > Procedures > Function Modules > FUNCTION"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Function Module Interface

The [parameter interface](../../abap-glossary/abenparameter_interface_glosry.md) of a function module is defined in the [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md). It comprises the definition of interface parameters and the specification of exceptions that can be raised by a function module. ADT uses an editor with statements in ABAP pseudo syntax, which represent the interface of the function module as follows:

## Syntax

``` abap
... [IMPORTING parameters]   
    [EXPORTING parameters]   
    [TABLES table_parameters]   
    [CHANGING parameters]   
    [{RAISING exc1|RESUMABLE(exc1) exc2|RESUMABLE(exc2) ...}   
    |{EXCEPTIONS exc1 exc2 ...}]  
```

[`parameters`](abenfunction_parameters.md) · [`parameters`](abenfunction_parameters.md) · [`parameters`](abenfunction_parameters.md)

## Description

The syntax and semantics of `IMPORTING`, `EXPORTING`, `CHANGING`, `RAISING`, and `EXCEPTIONS` mainly correspond to the definition of method interfaces with [`[CLASS-]METHODS`](../abap-declarations/abapmethods_general.md). The additional option of defining table parameters using `TABLES` is obsolete.

## Hint

In the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md) the parameter interface of a function module is defined in ABAP pseudo syntax. These statements are not compiled like genuine ABAP statements and are not subject to the regular ABAP syntax checks.

### Interface Parameters

The interface parameters are defined in the ADT in ABAP pseudo syntax.

- `IMPORTING` parameters are input parameters. When the function module is called, a suitable actual parameter must be specified for each non-optional input parameter. The content of the actual parameter is passed to the input parameter when it is called. The content of an input parameter for which 'pass by reference' is defined cannot be changed in the function module.

- `EXPORTING` parameters are output parameters. When the function module is called, a suitable actual parameter can be specified for each output parameter. The content of an output parameter that is defined for 'pass by value' is passed to the actual parameter if the function module is completed without errors. An output parameter that is defined for pass by reference is not initialized when the function module is called.

- `TABLES` parameters are obsolete table parameters.

- `CHANGING` parameters are input and output parameters. When the function module is called, a suitable actual parameter must be specified for each non-optional input or output parameter. The content of the actual parameter is passed to the input/output parameter when the parameter is called, and the content of the input/output parameter is passed to the actual parameter when the function module is completed.

### Exceptions

The exceptions of a function module are defined in the ADT in ABAP pseudo syntax. When *exception classes* are selected, it is specified whether it is a declaration of a [class-based exception](../../abap-glossary/abenclass_based_exception_glosry.md) or a [non-class-based exception](../abap-program-flow-logic/abenexceptions_non_class.md). Class-based exceptions are represented in the above syntax by `RAISING` and non-class-based exceptions are represented by `EXCEPTIONS`.

- The addition `RAISING` is used to declare class-based exceptions that can be propagated from the function module to the caller. Exceptions of the categories `CX_STATIC_CHECK` and `CX_DYNAMIC_CHECK` must be declared explicitly, otherwise a propagation leads to an interface violation. A violation of the interface raises the catchable exception `CX_SY_NO_HANDLER`. Exceptions of the category `CX_NO_CHECK` are always declared implicitly with the addition `RESUMABLE`, but they can also be declared explicitly. The declaration of exceptions of the category `CX_STATIC_CHECK` is checked statically during syntax check. For exceptions of the category `CX_DYNAMIC_CHECK`, the check is not performed until runtime. For exceptions of the category `CX_NO_CHECK` no check is performed.

  The addition `RESUMABLE` declares an exception so that it can be propagated as a [resumable exception](../../abap-glossary/abenresumable_exception_glosry.md), which is then also propagated as such. The addition has no effect on a non-resumable exception. If a resumable exception is propagated in `RAISING` without the addition`RESUMABLE`, it becomes non-resumable. If a superclass is declared as resumable, all of the simultaneously listed subclasses must also be declared as resumable.

- \*\*\*This syntax is only supported temporarily in the current ABAP language version and must be replaced with valid syntax for that version.\*\*\*.

  The addition `EXCEPTIONS` is used to define a list of non-class-based exceptions that can be raised in the function module using the statements [`RAISE`](../abap-program-flow-logic/abapraise_exception.md) or [`MESSAGE RAISING`](../abap-program-flow-logic/abapmessage_raising.md). Exceptions defined in this way are bound to the function module, similarly to formal parameters, and cannot be propagated. If such an exception is raised in a function module, and no return value was assigned to it with the identically named addition `EXCEPTIONS` of the statement [`CALL FUNCTION`](../abap-calling-and-exiting-program-units/abapcall_function.md) during the call, a runtime error occurs. In a function module in whose interface non-class-based exceptions are defined, the statement [`RAISE EXCEPTION`](../abap-program-flow-logic/abapraise_exception_class.md) or the addition [`THROW`](../abap-program-flow-logic/abenconditional_expression_result.md) in a [conditional expression](../abap-program-flow-logic/abenconditional_expressions.md) cannot be used to raise class-based exceptions.

## Hint

See also [Class-Based Exceptions in Procedures](../abap-program-flow-logic/abenexceptions_procedures.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Comment lines generated by the tools for different types of actual parameters and a class-based resumable exception of a function module.

``` abap
*"---------------------------------------------------------------------- 
*"*"Local Interface: 
*"  IMPORTING 
*"     REFERENCE(P1) TYPE  I 
*"     REFERENCE(P2) TYPE  I OPTIONAL 
*"     REFERENCE(P3) TYPE  I DEFAULT 100 
*"  EXPORTING 
*"     REFERENCE(P4) TYPE  SCARR 
*"  CHANGING 
*"     VALUE(P5)     TYPE  SPFLI OPTIONAL 
*"  RAISING 
*"     RESUMABLE(CX_NO_FLIGHTS) 
*"----------------------------------------------------------------------
```
