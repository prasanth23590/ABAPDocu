---
title: "ABAP Objects - Interfaces"
source_file: abeninterfac.html
section: "ABAP Programming Language > ABAP - ABAP Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Interfaces

The components of a class use their [visibility sections](abenclass_visibility.md) to define the class-specific [interfaces](../../abap-glossary/abenintf_gen_glosry.md) of the class to the outside. For example, the public components form the public interface of the class, since all of its attributes and method parameters can be addressed by all users. The protected components form an interface between the class and its subclasses during inheritance.

[Interfaces](../../abap-glossary/abenoo_intf_glosry.md) of ABAP Objects are independent constructs that enable the class-specific [interfaces](../../abap-glossary/abenintf_gen_glosry.md) to be enhanced by implementing them in classes. Different classes that implement the same interface can all be addressed using identical interfaces. In addition to [inheritance](abeninheritance.md), Interfaces are a basis for the [polymorphism](../../abap-glossary/abenpolymorphism_glosry.md) of classes, since a method of an interface can behave differently in different classes. [Interface reference variables](../../abap-glossary/abeninterface_ref_variable_glosry.md) allow users to address different classes in the same way. Interfaces can also be [nested](abeninterface_composition.md).

- [Defining Interfaces](abeninterfac.md#defining-interfaces)

- [Interface Components](abeninterfac.md#interface-components)

- [Implementing Interfaces](abeninterfac.md#implementing-interfaces)

- [Interface Reference Variables](abeninterfac.md#interface-reference-variables)

- [Accessing Objects Using Interface References](abeninterfac.md#accessing-objects-using-interface-references)

- [Accessing the Static Components of Interfaces](abeninterfac.md#accessing-the-static-components-of-interfaces)

## Defining Interfaces

Like classes, interfaces can be [defined](abenclass_interface_definition.md) either [globally](../../abap-glossary/abenglobal_interface_glosry.md) in the [repository](../../abap-glossary/abenrepository_glosry.md) or [locally](../../abap-glossary/abenlocal_interface_glosry.md) in an ABAP program.

## Interface Components

Exactly the same [components](abenclass_components.md) can be defined in an interface as in a class.

## Implementing Interfaces

Unlike classes, interfaces do not have instances. Instead, they are implemented by classes. The statement [`INTERFACES`](../abap-declarations/abapinterfaces.md) in the declaration part of a class is used to implement these interfaces in a class. This statement may only be specified in the public visibility section of the class, that is, after `PUBLIC SECTION`. Here, some interface components can be adapted to the requirements of the class. For example, methods can be flagged as abstract or final, or [initial values](../../abap-glossary/abenstart_value_glosry.md) can be assigned to attributes.

When an interface is implemented in a class, the components of this interface are added to the other components of the public visibility section. A component `comp` of an implemented interface `intf` becomes a fully-fledged component of the class and is addressed with the name `intf~comp`. For use outside and inside the classes, [`ALIASES`](../abap-declarations/abapaliases.md) can be used to define alias names for these components.

The class must implement the methods of all implemented interfaces in it. The implementation part of the class must therefore contain a method implementation for each non-abstract and non-optional interface method `meth`:

``` abap
`METHOD intf~meth.` 
`  ...` 
`ENDMETHOD.`
```

Interface methods defined as optional using the addition [`DEFAULT`](../abap-declarations/abapmethods_default.md) do not need to be implemented explicitly and react with default behavior when they are called.

Interfaces can be implemented by different classes. Each of these classes is extended by the same set of components. However, the methods of the interface can be implemented differently in each class.

Interfaces enable different classes to be used in a uniform way using [interface reference variables](../../abap-glossary/abeninterface_ref_variable_glosry.md) (known as polymorphism). Interfaces that are implemented in different classes expand the public interfaces of each class by the same set of components. If a class does not have any class-specific public components, the interfaces define the entire public interface of the class.

## Interface Reference Variables

Object references are used in object reference variables to address [objects](abenobject.md). Instead of creating object reference variables with reference to a [class](abenclasses.md), they can also be created with reference to an interface. This kind of reference variable can contain references to objects of classes that implement the corresponding interface. A reference variable `obj` with reference to an interface `intf` is declared using the statement [`DATA obj TYPE REF TO intf`](../abap-declarations/abapdata_references.md). This reference variable allows programs access to exactly those components defined in the interface, that is, the components of an object that are added to the class-specific components by implementing the interface.

## Accessing Objects Using Interface References

To create an object of a class `class` that implements an interface `intf` to which an interface reference variable `iref` points initially, the name of the class must be specified:

`FINAL(iref) = NEW class( ).`

or

`CREATE OBJECT iref TYPE class`.

Also, a reference variable `cref` with reference to the class `class` that points to an object of the class can be used. A class reference variable `cref` of a class that implements an interface `intf` can be assigned to the interface reference variable `iref`:

`iref = cref`.

The reference in `iref` now points to the same object as the reference in `cref`.

If the interface `intf` contains an instance attribute `attr` and an instance method `meth`, the interface components can be addressed as follows:

Using the class reference variable (not recommended)

- Access to an attribute `attr`: `cref->intf~attr`

- Call of a method `meth`: `cref->intf~meth`

Using the interface reference variable (recommended):

- Access to an attribute `attr`: `iref->attr`

- Call of a method `meth`: `iref->meth( )`

## Accessing the Static Components of Interfaces

In the case of [static components](../../abap-glossary/abenstatic_component_glosry.md) of interfaces, the name of the interface can only be used to access constants.

- Accessing a constant `const`: `intf=>const`

All other static components of an interface, apart from object references, can be accessed using classes `class` that implement the interface.

- Access to a static attribute `attr`:`class=>intf~attr`

- Call of a static method `meth`: `class=>intf~meth( )`

### Executable Example

[Interfaces](abeninterface_abexa.md)
