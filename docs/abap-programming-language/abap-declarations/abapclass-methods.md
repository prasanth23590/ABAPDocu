---
title: "CLASS-METHODS"
source_file: abapclass-methods.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS-METHODS

## Syntax Forms

**[General Static Methods](abapclass-methods_general.md)**

``` abap
1. CLASS-METHODS meth [DEFAULT IGNORE|FAIL] 
    [IMPORTING parameters [PREFERRED PARAMETER p]] 
    [EXPORTING parameters] 
    [CHANGING parameters] 
    [{RAISING exc1|RESUMABLE(exc1) exc2|RESUMABLE(exc2) ...} 
    |{EXCEPTIONS exc1 exc2 ...}]. 
```

**[Functional Static Methods](abapclass-methods_functional.md)**

``` abap
2. CLASS-METHODS meth [DEFAULT IGNORE|FAIL] 
    [IMPORTING parameters [PREFERRED PARAMETER p]] 
    [EXPORTING parameters] 
    [CHANGING  parameters] 
    RETURNING VALUE(r) typing 
    [{RAISING exc1|RESUMABLE(exc1) exc2|RESUMABLE(exc2) ...} 
    |{EXCEPTIONS exc1 exc2 ...}].
```

**[Static Constructors](abapclass-methods_constructor.md) (Only in Classes)**

``` abap
3. CLASS-METHODS class_constructor. 
```

**[Event Handlers](abapclass-methods_event_handler.md)**

``` abap
4. CLASS-METHODS meth [DEFAULT IGNORE|FAIL] 
     FOR EVENT evt OF {class|intf} 
     [IMPORTING p1 p2 ... [sender]]. 
```

**[AMDP - Methods](../abap-database-access/abapmethods_amdp_options.md)**

``` abap
5. CLASS-METHODS meth [DEFAULT IGNORE|FAIL] 
                     [AMDP OPTIONS [READ-ONLY] 
                        [CDS SESSION CLIENT DEPENDENT|CURRENT|clnt] 
                      | [CLIENT INDEPENDENT]] 
    [IMPORTING parameters [PREFERRED PARAMETER p]] 
    [EXPORTING parameters] 
    [CHANGING  parameters] 
    [RETURNING VALUE(r) typing] 
    [{RAISING exc1|RESUMABLE(exc1) exc2|RESUMABLE(exc2) ...}]
```

**[AMDP Function Implementations for CDS Table Functions](../abap-database-access/abapclass-methods_for_tabfunc.md) (Only in Classes)**

``` abap
6. CLASS-METHODS meth FOR TABLE FUNCTION cds_tabfunc.
```

[`DEFAULT IGNORE|FAIL`](abapmethods_default.md) · [`parameters`](abapmethods_parameters.md) · [`parameters`](abapmethods_parameters.md) · [`parameters`](abapmethods_parameters.md) · [`DEFAULT IGNORE|FAIL`](abapmethods_default.md) · [`parameters`](abapmethods_parameters.md) · [`parameters`](abapmethods_parameters.md) · [`parameters`](abapmethods_parameters.md) · [`DEFAULT IGNORE|FAIL`](abapmethods_default.md) · [`DEFAULT IGNORE|FAIL`](abapmethods_default.md) · [`AMDP OPTIONS [READ-ONLY]`](../abap-database-access/abapmethods_amdp_options.md) · [`[CDS SESSION CLIENT DEPENDENT|CURRENT|clnt]`](../abap-database-access/abapmethods_amdp_options_client.md) · [`[CLIENT INDEPENDENT]`](../abap-database-access/abapmethods_amdp_options_client.md) · [`parameters`](abapmethods_parameters.md) · [`parameters`](abapmethods_parameters.md) · [`parameters`](abapmethods_parameters.md)

## Description

The statement `CLASS-METHODS` declares a [static method](../../abap-glossary/abenstatic_method_glosry.md) `meth`. The [naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md) apply to the name `meth`.

Using the class component selector (`=>`), static methods can be used independently of objects. In static methods, the static components of the personal class or their superclasses can be accessed only if the component selector is not used.

The variants of the statement `CLASS-METHODS` distinguish the following types of method declaration:

- [General static methods](abapclass-methods_general.md)

  The most general form of the statement `CLASS-METHODS` allows static methods in classes and interfaces to be declared with any number of input and output parameters.

- [Functional Static Methods](abapclass-methods_functional.md)

  [Functional methods](../../abap-glossary/abenfunctional_method_glosry.md) of classes and interfaces have exactly one return value and any other formal parameters.

- [Static constructors](abapclass-methods_constructor.md)

  Static constructors of classes are methods with the predefined name `class_constructor` that are called automatically before their class is first used. Static constructors do not have a parameter interface and cannot be declared in interfaces.

- [Static event handlers](abapclass-methods_event_handler.md)

  Static [event handlers](../../abap-glossary/abenevent_handler_glosry.md) are static methods of classes and interfaces that are called by an event of a class or an interface. The only possible formal parameters of an event handler are input parameters that were defined as output parameters of the event.

- [Static AMDP methods](../abap-database-access/abapmethods_amdp_options.md)

  In general, the same rules apply to declarations of static [AMDP methods](../../abap-glossary/abenamdp_method_glosry.md) for [AMDP procedure implementations](../../abap-glossary/abenamdp_procedure_method_glosry.md) and [AMDP function implementations](../../abap-glossary/abenamdp_function_method_glosry.md) that do not implement [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md) as to all static methods. There is, however, one special optional addition, [`AMDP OPTIONS`](../abap-database-access/abapmethods_amdp_options.md), and no non-class-based exceptions can be declared using `EXCEPTIONS`.

- [AMDP function implementations](../abap-database-access/abapclass-methods_for_tabfunc.md)

  [AMDP function implementations](../../abap-glossary/abenamdp_function_method_glosry.md) declared using the addition `FOR TABLE FUNCTION` implement a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md) in an [AMDP class](../../abap-glossary/abenamdp_class_glosry.md). The formal parameters are determined using the CDS table function. An AMDP function implementation cannot be declared in an interface.

## Hints

- Like all [static components in the inheritance](../abap-abap-objects/abeninheritance_statical.md), the static methods of a superclass exist in all subclasses. A static method is always executed in the class in which it was declared. A static method that is visible externally can be called using the class component selector and all names of classes in which it exists. However, the class in which it was declared is always the one that is addressed, which affects the execution of the [static constructor](../../abap-glossary/abenstatic_constructor_glosry.md) or the [event handlers](../../abap-glossary/abenevent_handler_glosry.md).

- In the methods of a class, a method of the class [hides](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions_syntax.md) a [built-in function](../../abap-glossary/abenbuiltin_function_glosry.md) with the same name. This hiding is independent of the type and number of method parameters and the type and number of parameters of the function. This means that a method should not have the same name as a built-in function.
