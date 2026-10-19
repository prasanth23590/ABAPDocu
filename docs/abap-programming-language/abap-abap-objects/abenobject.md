---
title: "ABAP Objects - Objects"
source_file: abenobject.html
section: "ABAP Programming Language > ABAP - ABAP Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Objects

Objects are instances of classes. There can be any number of objects or instances in a class. Each object has a unique identity and its own attributes.

By default, all objects have the same priority in the [data area](../../abap-glossary/abendata_area_glosry.md) of an [internal session](../../abap-glossary/abeninternal_session_glosry.md). This means that objects can only be accessed within an internal session.

## Creating Objects

To create an object, an [object reference variable](abenreferences.md) is required that can point to the required class:

- After a class reference variable `obj` is declared for a class `class`, an object of that class can be created using the statement [`CREATE OBJECT obj`](../abap-creating-objects-and-values/abapcreate_object.md). This statement creates an instance of the class `class` and the reference variable `obj` contains a [reference](abenreferences.md) to this object.

- After a class reference variable `obj` is declared for a superclass of the class `class` or an interface reference variable `obj` for an interface implemented by the class `class`, the addition `TYPE class` of the statement [`CREATE OBJECT obj`](../abap-creating-objects-and-values/abapcreate_object.md) can be used to create an instance of the class `class`.

The instance operator [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) enables objects to be created in [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md).

## Access to Instance Components

A program can access the visible instance components of an object only by using references in [reference variables](abenreferences.md). For the corresponding syntax, see [Accessing Components of Classes](abenclass_components_addressing.md).

## Lifetime of Objects

An object lives for as long as it is used in the internal session (known as the [heap](../../abap-glossary/abenheap_glosry.md)). An object is used for as long as at least one [heap reference](../../abap-glossary/abenheap_reference_glosry.md) points to the object, to an instance attribute, or to a part of the instance attribute or as long as at least one method of the object is registered as an [event handler](../../abap-glossary/abenevent_handler_glosry.md). Field symbols to which an instance attribute or part of an instance attribute is assigned, have the same effect as data references.

As soon as an object has no more references and none of its methods are registered as an event handler, it can be deleted by the [Garbage Collector](../../abap-glossary/abengarbage_collector_glosry.md). This releases the identity of the object to be taken by a new object.
