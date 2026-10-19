---
title: "ABAP Objects - Constructors of Classes"
source_file: abenconstructor.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Classes > ABAP Objects - Components of Classes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Constructors of Classes

Constructors are special methods that produce a defined initial state for objects and classes. The state of an object or class is determined by its [instance attributes](../../abap-glossary/abeninstance_attribute_glosry.md) and [static attributes](../../abap-glossary/abenstatic_attribute_glosry.md). The content of attributes can be pre-assigned statically using the addition `VALUE` of the statement `DATA`. Constructors are always necessary if the initial state of an object needs to be defined dynamically.

Like regular methods, there are two types of constructors: instance constructors and static constructors.

Special rules apply to constructors in inheritance that are not described in the following, but can be found [here](abeninheritance_constructors.md).

- [Instance Constructors](abenconstructor.md#instance-constructors)

- [Static Constructors](abenconstructor.md#static-constructors)

## Instance Constructors

Each class has exactly one instance constructor. This constructor is a predefined instance method of the class called `constructor`. To use the instance constructor, the method `constructor` must be declared in a visibility section of the class using the [`METHODS`](../abap-declarations/abapmethods_constructor.md) statement, and implemented in the implementation part. In global classes, the instance constructor can only be declared in the public visibility section, for technical reasons. In local classes, the visibility section in which the instance constructor can be declared must be more general or equal to the instantiability defined by the addition [`CREATE`](../abap-declarations/abapclass_options.md) of the statement [`CLASS`](../abap-declarations/abapclass.md). Here, the most specialized area is recommended. Unless it is explicitly declared, the instance constructor is an implicit method that inherits and accesses the interface of the instance constructor of the superclass.

Instance constructors are called once for each instance. They are called automatically, immediately after an instance is created using the statement [`CREATE OBJECT`](../abap-creating-objects-and-values/abapcreate_object.md). It is not possible to call an instance constructor directly using [`constructor( ... )`](../abap-calling-and-exiting-program-units/abapcall_method_static_short.md), but see [`super->constructor( ... )`](../abap-calling-and-exiting-program-units/abapcall_method_meth_super.md) in inheritance.

An instance constructor can contain an interface with `IMPORTING` parameters and exceptions. The interface is defined using the same syntax as for regular methods in the statement [`METHODS`](../abap-declarations/abapmethods.md). The lack of output parameters shows that constructors only exist to define the state of an object and have no other function. The additions `EXPORTING` and `EXCEPTIONS` of the statement [`CREATE OBJECT`](../abap-creating-objects-and-values/abapcreate_object.md) are used to pass actual parameters and handle classical exceptions.

## Static Constructors

Each class has exactly one static constructor. This constructor is a predefined public [static method](../../abap-glossary/abenstatic_method_glosry.md) of the `class_constructor` class. To use the static constructor, the static method `class_constructor` must be declared in the public section of the declaration part of the class using the statement [`CLASS-METHODS`](../abap-declarations/abapclass-methods_constructor.md) and implemented in the implementation part. The static constructor has no interface parameters and cannot raise exceptions. Unless implemented it explicitly, it is merely an empty method.

The static constructor is called once for each class and [internal session](../../abap-glossary/abeninternal_session_glosry.md). The static constructor of a class `class` is called automatically before the class is first accessed. The class is accessed when an instance of the class is created, or a component of the class is used, apart from types and constants. It is not necessary to execute the static constructor to access a type or a constant of the class.

The static constructor is always called immediately before access, with one exception: the static constructor is called at the start of the [processing block](../../abap-glossary/abenprocessing_block_glosry.md) in which the class is accessed, if the static variable is addressed in the first access to the class.

### Hints

- The point at which the static constructor is executed is not definitely fixed. The only guarantee is that it will be called before the class is accessed for the first time.

- A static constructor can call static methods of its class. Such a method must be implemented accordingly and must not rely on the static constructor being fully executed.

- The order in which the static constructors are executed depends on the program flow. Static constructors must be implemented so that they can be executed in any order.
