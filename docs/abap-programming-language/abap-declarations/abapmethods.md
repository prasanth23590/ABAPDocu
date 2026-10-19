---
title: "METHODS"
source_file: abapmethods.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# METHODS

## Syntax Forms

**[General Instance Methods](abapmethods_general.md)**

``` abap
1. METHODS meth [ABSTRACT|FINAL] 
              |[DEFAULT IGNORE|FAIL] 
    [IMPORTING parameters [PREFERRED PARAMETER p]] 
    [EXPORTING parameters] 
    [CHANGING  parameters] 
    [{RAISING exc1|RESUMABLE(exc1) exc2|RESUMABLE(exc2) ...} 
    |{EXCEPTIONS exc1 exc2 ...}].
```

**[Functional Instance Methods](abapmethods_functional.md)**

``` abap
2. METHODS meth [ABSTRACT|FINAL] 
              |[DEFAULT IGNORE|FAIL] 
    [IMPORTING parameters [PREFERRED PARAMETER p]] 
    [EXPORTING parameters] 
    [CHANGING  parameters] 
    RETURNING VALUE(r) typing 
    [{RAISING exc1|RESUMABLE(exc1) exc2|RESUMABLE(exc2) ...} 
    |{EXCEPTIONS exc1 exc2 ...}]. 
```

**[Instance Constructors](abapmethods_constructor.md) (Only in Classes)**

``` abap
3. METHODS constructor [FINAL] 
    [IMPORTING parameters [PREFERRED PARAMETER p]] 
    [{RAISING exc1|RESUMABLE(exc1) exc2|RESUMABLE(exc2) ...} 
    |{EXCEPTIONS exc1 exc2 ...}].
```

**[Event Handlers](abapmethods_event_handler.md)**

``` abap
4. METHODS meth [ABSTRACT|FINAL] 
              |[DEFAULT IGNORE|FAIL] 
     FOR EVENT evt OF {class|intf} 
     [IMPORTING p1 p2 ... [sender]].
```

**[Redefinition of Instance Methods](abapmethods_redefinition.md) (Only in Subclasses)**

``` abap
5. METHODS meth [FINAL] REDEFINITION.
```

**[AMDP Methods](../abap-database-access/abenamdp_methods.md)**

``` abap
6. METHODS meth [ABSTRACT|FINAL] 
              |[DEFAULT IGNORE|FAIL] 
               [AMDP OPTIONS [READ-ONLY] 
                 [CDS SESSION CLIENT DEPENDENT|CURRENT|clnt] 
               | [CLIENT INDEPENDENT]] 
    [IMPORTING parameters [PREFERRED PARAMETER p]] 
    [EXPORTING parameters] 
    [CHANGING  parameters] 
    [RETURNING VALUE(r) typing] 
    [{RAISING exc1|RESUMABLE(exc1) exc2|RESUMABLE(exc2) ...}]
```

**[Test Methods](../abap-program-maintenance/abapmethods_testing.md) (Only in Test Classes)**

``` abap
7. METHODS meth [ABSTRACT|FINAL] 
               [AMDP OPTIONS [READ-ONLY] 
                 [CDS SESSION CLIENT DEPENDENT|CURRENT|clnt] 
               | [CLIENT INDEPENDENT]] 
    FOR TESTING 
    [{RAISING exc1|RESUMABLE(exc1) exc2|RESUMABLE(exc2) ...}].
```

**[ABP Handler Methods](../../abap-rap-business-objects/abap-for-rap-business-objects/abapmethods_for_rap_behv.md) (Only in Handler Classes of ABAP Behavior Pools)**

``` abap
8. METHODS meth [FINAL] 
    FOR rap_behv ...
```

[`ABSTRACT|FINAL`](abapmethods_abstract_final.md) · [`DEFAULT IGNORE|FAIL`](abapmethods_default.md) · [`parameters`](abapmethods_parameters.md) · [`parameters`](abapmethods_parameters.md) · [`parameters`](abapmethods_parameters.md) · [`ABSTRACT|FINAL`](abapmethods_abstract_final.md) · [`DEFAULT IGNORE|FAIL`](abapmethods_default.md) · [`parameters`](abapmethods_parameters.md) · [`parameters`](abapmethods_parameters.md) · [`parameters`](abapmethods_parameters.md) · [`FINAL`](abapmethods_abstract_final.md) · [`parameters`](abapmethods_parameters.md) · [`ABSTRACT|FINAL`](abapmethods_abstract_final.md) · [`DEFAULT IGNORE|FAIL`](abapmethods_default.md) · [`FINAL`](abapmethods_abstract_final.md) · [`ABSTRACT|FINAL`](abapmethods_abstract_final.md) · [`DEFAULT IGNORE|FAIL`](abapmethods_default.md) · [`AMDP OPTIONS [READ-ONLY]`](../abap-database-access/abapmethods_amdp_options.md) · [`[CDS SESSION CLIENT DEPENDENT|CURRENT|clnt]`](../abap-database-access/abapmethods_amdp_options_client.md) · [`[CLIENT INDEPENDENT]`](../abap-database-access/abapmethods_amdp_options_client.md) · [`parameters`](abapmethods_parameters.md) · [`parameters`](abapmethods_parameters.md) · [`parameters`](abapmethods_parameters.md) · [`ABSTRACT|FINAL`](abapmethods_abstract_final.md) · [`AMDP OPTIONS [READ-ONLY]`](../abap-database-access/abapmethods_amdp_options.md) · [`[CDS SESSION CLIENT DEPENDENT|CURRENT|clnt]`](../abap-database-access/abapmethods_amdp_options_client.md) · [`[CLIENT INDEPENDENT]`](../abap-database-access/abapmethods_amdp_options_client.md) · [`FINAL`](abapmethods_abstract_final.md)

## Description

The statement `METHODS` declares or redefines an instance method `meth`. The [naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md) apply to the name `meth`.

Instance methods are bound to objects. To use instance methods, an object of the class must first be created. In instance methods, all components of the same class can be accessed without a component selector.

The variants of the statement `METHODS` are used to distinguish between the following kinds of method declarations:

- [General instance methods](abapmethods_general.md)

  The most general form of the `METHODS` statement allows instance methods to be defined with any input and output parameters.

- [Functional instance methods](abapmethods_functional.md)

  [Functional methods](../../abap-glossary/abenfunctional_method_glosry.md) have exactly one return value and any number of formal parameters.

- [Instance constructors](abapmethods_constructor.md)

  Instance constructors are methods with the given name `constructor`, which are called automatically when their class is instantiated. Constructors have any number of input parameters and no output parameters. They cannot be declared in interfaces.

- [Event handlers](abapmethods_event_handler.md)

  Event handlers are methods that can be called directly using or in [statements](../abap-calling-and-exiting-program-units/abenmethod_calls.md), but are mainly called when an event of a class or an interface is raised. The only possible formal parameters of an event handler are input parameters defined as the output parameters of the event.

- [Redefinition of Instance Methods](abapmethods_redefinition.md)

  A method declared in a superclass can be redefined in a subclass as long as it is not flagged as final in the superclass. In a [redefinition](../../abap-glossary/abenredefinition_glosry.md), the interface of the method is not changed.

- [AMDP Methods](../abap-database-access/abapmethods_amdp_options.md)

  In general, the same rules apply to declaring [AMDP methods](../../abap-glossary/abenamdp_method_glosry.md) as to all instance methods. There is, however, one special optional addition, [`AMDP OPTIONS`](../abap-database-access/abapmethods_amdp_options.md), and no non-class-based exceptions can be declared using `EXCEPTIONS`.

- [Definition of a test method](../abap-program-maintenance/abapmethods_testing.md)

  Test methods can be declared in test classes. They have no interface parameters and are called during [ABAP Unit](../../abap-glossary/abenabap_unit_glosry.md) tests by the ABAP runtime framework. They cannot be declared in interfaces.

- [ABP Handler Methods](../../abap-rap-business-objects/abap-for-rap-business-objects/abapmethods_for_rap_behv.md)

  ABP methods can be declared in the [handler classes](../../abap-glossary/abenabp_handler_class_glosry.md) of an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). They implement the CRUD operations of a [RAP business object](../../abap-glossary/abenrap_bo_glosry.md).

## Hint

In the methods of a class, one method of the class [hides](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions_syntax.md) a [built-in function](../../abap-glossary/abenbuiltin_function_glosry.md) with the same name. This hiding is independent of the type and number of method parameters and the type and number of parameters of the function. This means that a method should not have the same name as a built-in function.
