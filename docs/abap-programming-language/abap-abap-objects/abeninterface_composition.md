---
title: "ABAP Objects - Nesting Interfaces"
source_file: abeninterface_composition.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Interfaces"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Nesting Interfaces

Interfaces of ABAP objects can be nested. An [interface](abeninterfac.md) can contain one or more interfaces as components, which themselves can contain interfaces. An interface that contains another interface is called a [nested interface](../../abap-glossary/abencompound_interface_glosry.md). An interface that is nested within an interface is called a component interface. An interface that does not contain any nested interfaces is called an elementary interface.

All interface components of a nested interface have the same level. If a nested interface `i3` contains interface components `i2` that themselves are nested, their interface components `i1` become interface components of `i3`. A nested interface contains each interface component exactly once. Even if a component interface is implemented again as a component of another component interface, it still exists only once.

The statement `INTERFACES` is used for nesting interfaces within an interface definition:

[`INTERFACE i3.`](../abap-declarations/abapinterface.md) [`INTERFACES: i1, i2 ...`](../abap-declarations/abapinterfaces.md) [`ENDINTERFACE.`](../abap-declarations/abapendinterface.md)

Here, the interface `i3` consists of its components and the interfaces `i1` and `i2`. In the nested interface, the components of the component interfaces are visible using the interface component selector (~). Within the above definition of `i3`, expressions such as `i1~comp` or `i2~comp` are possible. However, independent names can also be defined using the [`ALIASES`](../abap-declarations/abapaliases.md) statement.

## Using Alias Names

Within interface definitions, the statement [`ALIASES`](../abap-declarations/abapaliases.md) can be used to assign alias names to the components of component interfaces. This makes those that are nested deeper than one level visible within the interface definition.

``` abap
`INTERFACE i2.` 
`  INTERFACES i1.` 
`  ALIASES alias21 FOR i1~comp1.` 
`ENDINTERFACE.` 
 
`INTERFACE i3.` 
`  INTERFACES i2.` 
`  ALIASES alias31 FOR i2~alias21.` 
`  ALIASES alias32 FOR i2~comp2.` 
`ENDINTERFACE.`
```

## Accessing Interface Reference Variables

Reference variables typed with reference to a nested interface can be assigned reference variables typed with reference to one of the component interfaces (known as an [upcast](../../abap-glossary/abenup_cast_glosry.md)). The latter can be used to address the components of the component interfaces. The opposite case cannot be checked statically and must be done using the [casting operator](../../abap-glossary/abencasting_operator_glosry.md) (?= or `CAST`) (know as a [downcast](../../abap-glossary/abendown_cast_glosry.md)).

``` abap
`INTERFACE i1.` 
`  DATA comp1.` 
`ENDINTERFACE.` 
 
`INTERFACE i2.` 
`  DATA comp2.` 
`  INTERFACES i1.` 
`ENDINTERFACE.` 
 
`INTERFACE i3.` 
`  INTERFACES i2.` 
`ENDINTERFACE.` 
 
`DATA: iref1 TYPE REF TO i1,` 
`      iref2 TYPE REF TO i2,` 
`      iref3 TYPE REF TO i3.` 
 
`iref2 = iref3`\. 
`iref1 = iref2`\. 
 
`* recommended access:` 
 
`... iref1->comp1 ...` 
`... iref2->comp2 ...` 
 
`* this access is not recommended:` 
 
`... iref2->i1~comp1 ...` 
`... iref3->i2~comp2 ...` 
```

## Implementing Nested Interfaces in Classes

When a nested interface is implemented in a class, all involved interfaces are implemented in the class at the same level, regardless of their nesting hierarchy, and the class must implement each method only once.

``` abap
`INTERFACE i1.` 
`  DATA comp1.` 
`  METHODS meth1.` 
`ENDINTERFACE.` 
 
`INTERFACE i2.` 
`  DATA comp2.` 
`  INTERFACES i1.` 
`ENDINTERFACE.` 
 
`INTERFACE i3.` 
`  DATA comp3.` 
`  INTERFACES i2.` 
`ENDINTERFACE.` 
 
`CLASS class DEFINITION.` 
`  PUBLIC SECTION.` 
`    INTERFACES i3.` 
`ENDCLASS.` 
 
`CLASS class IMPLEMENTATION.` 
`  METHOD i1~meth.` 
`    ...` 
`  ENDMETHOD.` 
`ENDCLASS.` 
 
`DATA cref TYPE REF TO class.` 
`DATA iref1 TYPE REF TO i1.` 
`DATA iref2 TYPE REF TO i2.` 
`DATA iref3 TYPE REF TO i3.` 
 
`iref1 = iref2 = iref3 = cref.` 
 
`* recommended access:` 
 
`... iref1->comp1 ...` 
`... iref2->comp2 ...` 
`... iref3->comp3 ...` 
 
`* this access is not recommended:` 
 
`... cref->i1~comp1 ...` 
`... cref->i2~comp2 ...` 
`... cref->i3~comp3 ...` 
 
`... iref3->i1~comp1 ...` 
`... iref3->i2~comp2 ...` 
`... iref2->i1~comp1 ...`
```

Assignments using upcasts are always possible. Class reference variables for classes that implement a nested interface can be assigned to all interface reference variables that are typed with reference to an associated interface component. In the class, the interface reference variables know only the components of their interface. The same applies to assignments between interface reference variables. It is possible to access components using the interface component selector, but it is not recommended. Nested expressions such as `cref->i3~i2~comp2` or `cref->i3~i2~i3~comp3` are not possible.
