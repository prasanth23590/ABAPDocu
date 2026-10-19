---
title: "METHODS, IMPORTING, EXPORTING, CHANGING, RAISING"
source_file: abapmethods_general.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Methods > METHODS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# METHODS, IMPORTING, EXPORTING, CHANGING, RAISING

## Syntax

``` abap
METHODS meth [ABSTRACT|FINAL] 
            |[DEFAULT IGNORE|FAIL]   
  [IMPORTING parameters [PREFERRED PARAMETER p]]   
  [EXPORTING parameters]   
  [CHANGING  parameters]   
  [{RAISING exc1|RESUMABLE(exc1) exc2|RESUMABLE(exc2) ...}   
  |{EXCEPTIONS exc1 exc2 ...}].  
```

[`ABSTRACT|FINAL`](abapmethods_abstract_final.md) · [`DEFAULT IGNORE|FAIL`](abapmethods_default.md) · [`parameters`](abapmethods_parameters.md) · [`parameters`](abapmethods_parameters.md) · [`parameters`](abapmethods_parameters.md)

### Addition

[1. `... IMPORTING parameters [PREFERRED PARAMETER p]`](abapmethods_general.md#addition-1)

[2. `... EXPORTING parameters`](abapmethods_general.md#addition-2)

[3. `... CHANGING parameters`](abapmethods_general.md#addition-3)

[4. `... RAISING exc1|RESUMABLE(exc1) exc2|RESUMABLE(exc2) ...`](abapmethods_general.md#addition-4)

[5. `... EXCEPTIONS exc1 exc2 ...`](abapmethods_general.md#addition-5)

## Overview

### Description

This statement declares a general instance method `meth`. The additions [`ABSTRACT`](abapmethods_abstract_final.md) and [`FINAL`](abapmethods_abstract_final.md) can be used to make the method of a class abstract or final. The addition [`DEFAULT`](abapmethods_default.md) is used to make an interface method optional.

The additions `IMPORTING`, `EXPORTING`, and `CHANGING` define the [parameter interface](../abap-program-structure/abenformal_parameters_oview.md) of the method. After every addition, the corresponding formal parameters are defined by specifying a list [`parameters`](abapmethods_parameters.md). The order of the additions is fixed.

The remaining additions determine which exceptions are propagated or raised by the method.

### Hint

Within a method, the [predicate expression](../../abap-glossary/abenpredicate_expression_glosry.md) [`IS SUPPLIED`](../abap-program-flow-logic/abenlogexp_supplied.md) can be used to check whether an optional formal parameter was assigned an actual parameter when it was called.

## Addition 1

`... IMPORTING parameters [PREFERRED PARAMETER p]`

### Description

`IMPORTING` defines input parameters. When the method is called, an appropriate actual parameter must be specified for each non-optional input parameter. The content of the actual parameter is passed to the input parameter when it is called. The content of an input parameter for which pass-by-reference is defined cannot be changed in the method.

`PREFERRED PARAMETER` can be used to flag an input parameter `p1 p2 ...` from the list [`parameters`](abapmethods_parameters.md) after `IMPORTING` as a preferred parameter. This specification is only possible if all input parameters and input/output parameters are optional. The parameter specified after `PREFERRED PARAMETER` is implicitly set to optional. If the method is called using the syntax `meth( a )` (as [standalone](../abap-calling-and-exiting-program-units/abapcall_method_static_short.md) or [functional](../abap-calling-and-exiting-program-units/abapcall_method_functional.md) syntax), the actual parameter `a` is assigned to the preferred input parameter `p`.

### Hint

Although `PREFERRED PARAMETER` makes the parameter `p` optional implicitly, this parameter should be made optional explicitly using `OPTIONAL` or `DEFAULT`, which is required by a syntax check warning.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of a method with exclusively optional input parameters, of which one is flagged as a preferred parameter.

``` abap
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    METHODS 
      meth 
        IMPORTING 
          p1 TYPE i DEFAULT 111 
          p2 TYPE i OPTIONAL 
          p3 TYPE i OPTIONAL 
          PREFERRED PARAMETER p1. 
    ... 
ENDCLASS.
```

## Addition 2

`... EXPORTING parameters`

### Description

`EXPORTING` defines output parameters. When the method is called, an appropriate actual parameter can be specified for each output parameter. The content of an output parameter that is defined for pass-by-value is passed to the actual parameter if the method is completed without errors.

### Hint

An output parameter that is defined for pass-by-reference behaves like an input/output parameter, which means that it is not initialized when the method is called. For this reason, there should be no read access before the first write access. In addition, be careful when adding content to such parameters as, for example, when inserting lines into internal tables.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The method `read_spfli_into_table` of this example has an input and an output parameter, which are typed completely by reference to the ABAP Dictionary.

``` abap
CLASS flights DEFINITION. 
  PUBLIC SECTION. 
    METHODS read_spfli_into_table 
       IMPORTING VALUE(id)  TYPE spfli-carrid 
       EXPORTING flight_tab TYPE spfli_tab. 
       ... 
ENDCLASS.
```

## Addition 3

`... CHANGING parameters`

### Description

`CHANGING` defines input/output parameters. When the method is called, an appropriate actual parameter must be specified for each non-optional input/output parameter. The content of the actual parameter is passed to the input/output parameter when it is called and the content of the input/output parameter is passed to the actual parameter after the method has ended.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of a method with input and input/output parameters.

``` abap
CLASS html DEFINITION. 
  PUBLIC SECTION. 
    TYPES html_table TYPE ... 
    ... 
    METHODS 
      append_text_to_html 
        IMPORTING 
          text TYPE string 
        CHANGING 
          html TYPE html_table. 
    ... 
ENDCLASS.
```

## Addition 4

`... RAISING exc1|RESUMABLE(exc1) exc2|RESUMABLE(exc2) ...`

### Description

The addition `RAISING` is used to declare the [class-based exceptions](../../abap-glossary/abenclass_based_exception_glosry.md) `exc1 exc2 ...` that can be propagated from the method to the caller.

For `exc1 exc2 ...`, all exception that are classes and that are visible at this point can be specified here. The exception classes must be specified in ascending order with respect to their inheritance hierarchy. Each exception class may only be specified once.

The addition `RESUMABLE` declares an exception that can be propagated as a [resumable exception](../../abap-glossary/abenresumable_exception_glosry.md). This means:

- A resumable exception is propagated as such.

- The addition does not have any effect on a non-resumable exception.

- If a resumable exception is propagated in `RAISING` without the addition `RESUMABLE`, it becomes non-resumable.

If a superclass is declared as resumable, all of the simultaneously listed subclasses must also be declared as resumable.

Exceptions of the categories `CX_STATIC_CHECK` and `CX_DYNAMIC_CHECK` must be explicitly declared, otherwise a propagation leads to an interface violation. A violation of the interface raises the catchable exception `CX_SY_NO_HANDLER`. Exceptions of the category `CX_NO_CHECK` are always declared implicitly with the addition `RESUMABLE` but can also be declared explicitly with or without `RESUMABLE`.

### Hints

- The declaration of exceptions of the category `CX_STATIC_CHECK` is checked statically in the syntax check. For exceptions of the category `CX_DYNAMIC_CHECK`, the check is not performed until runtime. For exceptions of the category `CX_NO_CHECK` no check is performed.

- Exceptions of the category `CX_NO_CHECK` can be declared explicitly with or without the addition `RESUMABLE`. Implicitly the addition `RESUMABLE` is always added. An explicit declaration of an exception of the category `CX_NO_CHECK` has no effect but it documents for the user of a method the probability that this exception can be expected. Furthermore, it allows the category of existing exceptions to be changed into `CX_NO_CHECK` without leading to a syntax error.

- An exception that is raised as resumable in the method with [`RAISE RESUMABLE EXCEPTION`](../abap-program-flow-logic/abapraise_exception_class.md) should also be declared as resumable in the interface, otherwise the exception would lose this property when the method is exited.

- See also [Class-Based Exceptions in Procedures](../abap-program-flow-logic/abenexceptions_procedures.md).

## Addition 5

`... EXCEPTIONS exc1 exc2 ...`

\*\*\*This syntax is only supported temporarily in the current ABAP language version and must be replaced with valid syntax for that version.\*\*\*.

### Description

The addition `EXCEPTIONS` is used to define a list of [non-class-based exceptions](../abap-program-flow-logic/abenexceptions_non_class.md) `exc1 exc2...` that can be raised by the statements [`RAISE`](../abap-program-flow-logic/abapraise_exception.md) or [`MESSAGE RAISING`](../abap-program-flow-logic/abapmessage_raising.md) in the method. The names `exc1 exc2 ...` for the exceptions that are to be defined are freely definable and specified directly. Exceptions defined in this way are bound to the method, similar to formal parameters, and cannot be propagated.

If such an exception is raised in a method and no return code was assigned to it with the addition `EXCEPTIONS` in the [method call](../abap-calling-and-exiting-program-units/abenmethod_calls.md), a runtime error occurs.

The additions `RAISING` and `EXCEPTIONS` cannot be used simultaneously. In addition, in a method in whose interface non-class-based exceptions are defined, the statement [`RAISE EXCEPTION`](../abap-program-flow-logic/abapraise_exception_class.md) or the addition [`THROW`](../abap-program-flow-logic/abenconditional_expression_result.md) in a [conditional expression](../abap-program-flow-logic/abenconditional_expressions.md) must not be used to raise class-based exceptions.
