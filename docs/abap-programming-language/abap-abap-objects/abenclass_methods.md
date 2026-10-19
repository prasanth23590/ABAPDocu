---
title: "ABAP Objects - Methods of Classes"
source_file: abenclass_methods.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Classes > ABAP Objects - Components of Classes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Methods of Classes

Methods are internal [procedures](../../abap-glossary/abenprocedure_glosry.md) of a class that determine the behavior of an object. They can access all attributes of all instances of their class and can therefore change the status of an object. Methods have a parameter interface that is used to supply them with values when they are called, and which can be used to return values to the caller. The private attributes of a class can only be changed using methods of the same class.

- [Definition](abenclass_methods.md#definition)

- [Instance Methods](abenclass_methods.md#instance-methods)

- [Static Methods](abenclass_methods.md#static-methods)

- [Constructors](abenclass_methods.md#constructors)

- [Functional Methods](abenclass_methods.md#functional-methods)

- [Optional Methods](abenclass_methods.md#optional-methods)

- [Special Methods](abenclass_methods.md#special-methods)

  - [AMDP Methods](abenclass_methods.md#amdp-methods)

## Definition

A method `meth` is declared in the [declaration part](../../abap-glossary/abendeclaration_part_glosry.md) of a class using the statements [`METHODS`](../abap-declarations/abapmethods.md) and [`CLASS-METHODS`](../abap-declarations/abapclass-methods.md) and implemented in the [implementation part](../../abap-glossary/abenimplementation_part_glosry.md) of the class using the following [processing block](../../abap-glossary/abenprocessing_block_glosry.md):

``` abap
`METHOD meth.` 
`  ...` 
`ENDMETHOD.`
```

As in all procedures, local data types and data objects can be declared in methods. Methods are called [statically](../abap-calling-and-exiting-program-units/abenmethod_calls_static.md) using the expression `meth( ... )` or [dynamically](../abap-calling-and-exiting-program-units/abenmethod_calls_dynamic.md) using the statement [`CALL METHOD`](../abap-calling-and-exiting-program-units/abapcall_method_dynamic.md) (known as a dynamic invoke).

### Hint

In the methods of a class, one method of the class [hides](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions_syntax.md) a [built-in function](../../abap-glossary/abenbuiltin_function_glosry.md) with the same name. This hiding is independent of the type and number of method parameters and the type and number of parameters of the function. This means that a method should not have the same name as a built-in function.

## Instance Methods

Instance methods are declared using the statement [`METHODS`](../abap-declarations/abapmethods.md). They can access all the attributes of a class and can raise all of its events.

### Hint

Any attempt to call an instance method using an initial [object reference variable](../../abap-glossary/abenobject_refer_variable_glosry.md) raises a catchable exception.

## Static Methods

Static methods are declared using the statement [`CLASS-METHODS`](../abap-declarations/abapclass-methods.md). It can access [static attributes](../../abap-glossary/abenstatic_attribute_glosry.md) of a class and it can only raise [static events](../../abap-glossary/abenstatic_event_glosry.md).

## Constructors

In addition to the regular methods that are [called explicitly](../abap-calling-and-exiting-program-units/abenmethod_calls.md), there are two special methods called [`constructor` and `class_constructor`](abenconstructor.md), which are called implicitly when an object is created or when a class component is accessed for the first time.

## Functional Methods

Functional methods are methods with exactly one [`RETURNING`](../abap-declarations/abapmethods_functional.md) parameter and any number of other formal parameters. Functional methods cannot just be called as [standalone statements](../abap-calling-and-exiting-program-units/abapcall_method_static_short.md), but also as [functional method calls](../abap-calling-and-exiting-program-units/abapcall_method_functional.md) in [operand positions for expressions](../abap-syntax-elements-of-an-abap-program/abenexpression_positions.md). Here, they can be also be combined into [method chainings](../../abap-glossary/abenmethod_chaining_glosry.md).

## Optional Methods

In interfaces, methods can be made optional using the addition [`DEFAULT`](../abap-declarations/abapmethods_default.md) of the statements [`METHODS`](../abap-declarations/abapmethods.md) and [`CLASS-METHODS`](../abap-declarations/abapclass-methods.md). An optional interface method does not need to be implemented explicitly in a class when an interface is implemented. Instead, the definition defines a default behavior for calls of non-implemented methods. `DEFAULT IGNORE` calls an empty method and `DEFAULT FAIL` raises an exception.

## Special Methods

### AMDP Methods

[AMDP methods](../abap-database-access/abenamdp_methods.md) are implemented as [ABAP Managed Database Procedures](../../abap-glossary/abenabap_managed_db_proc_glosry.md) using the addition [`BY DATABASE PROCEDURE`](../abap-database-access/abapmethod_by_db_proc.md) or [`BY DATABASE FUNCTION`](../abap-database-access/abapmethod_by_db_proc.md) in a database-specific language and executed in the database system.
