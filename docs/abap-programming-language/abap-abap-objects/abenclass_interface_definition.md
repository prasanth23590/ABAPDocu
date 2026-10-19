---
title: "ABAP Objects - Definition of Classes and Interfaces"
source_file: abenclass_interface_definition.html
section: "ABAP Programming Language > ABAP - ABAP Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Definition of Classes and Interfaces

Classes and interfaces in ABAP Objects can be defined either globally or locally.

- Global classes and interfaces are stored centrally in the [class library](../../abap-glossary/abenclass_library_glosry.md) in the [repository](../../abap-glossary/abenrepository_glosry.md). From a technical perspective, global classes and interfaces are defined in [class pools](../../abap-glossary/abenclass_pool_glosry.md) or [interface pools](../../abap-glossary/abeninterface_pool_glosry.md). The global classes and interfaces are visible for all ABAP programs of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). Access is managed by the package check. Global classes and interfaces are stored in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP.

- Local classes and interfaces can be defined in any programs except [interface pools](../../abap-glossary/abeninterface_pool_glosry.md) and [type pools](../../abap-glossary/abentype_pool_glosry.md). They can only be used statically in the defining program. Dynamic access across program boundaries is possible, but not recommended. When a class is used in an ABAP program, the system first searches for a local class, then for a global class with the specified name. Otherwise, there is no differentiation between using global and local classes or interfaces.

In local classes that can only be used in a single program, it is usually sufficient to define the public interface, that is, the externally visible components, suitable for this program. However, global classes are available throughout the system, which means that its public interface can only be typed with reference to data types that are themselves visible throughout the system.

The syntax for defining classes and interfaces is essentially the same for local and global classes and interfaces. The only difference is in the addition `PUBLIC`, which makes a distinction between the global classes and interfaces and local declarations.

## Defining Classes

Classes consist of [ABAP source code](../../abap-glossary/abenabap_source_code_glosry.md), which is enclosed in the ABAP statements [`CLASS - ENDCLASS`](../abap-declarations/abapclass.md). A complete class definition consists of a declaration part and, if required, an implementation part.

The declaration part of a class named `class` consists of a statement block:

[`CLASS class DEFINITION.`](../abap-declarations/abapclass.md) ... [`ENDCLASS.`](../abap-declarations/abapendclass.md)

It contains the declaration of all [components](abenclass_components.md) (attributes, methods, or events) of a class. All the components of a class must be assigned explicitly to a [visibility section](abenclass_visibility.md) (`PUBLIC SECTION`, `PROTECTED SECTION`, or `PRIVATE SECTION`), which defines the location from where each component can be accessed. In local classes, the declaration part belongs to the global data declarations and should therefore also be at the beginning of the program.

If methods are declared in the declaration part of a class, the class also needs an implementation part. This consists of a statement block:

[`CLASS class IMPLEMENTATION.`](../abap-declarations/abapclass.md) ... [`ENDCLASS.`](../abap-declarations/abapendclass.md)

The implementation part of a class contains the implementation of all [methods](../../abap-glossary/abenmethod_glosry.md) of this class. Methods are [procedures](../../abap-glossary/abenprocedure_glosry.md), which makes them processing blocks of an ABAP program. The arrangement of the implementation part in the source code is therefore irrelevant. For clarity, all the implementation parts of local classes should be listed at the end of the program, or directly after the relevant definition part. In the latter case, however, it should be ensured that subsequent non-declarative statements must then be assigned explicitly to a [processing block](../../abap-glossary/abenprocessing_block_glosry.md) such as `START-OF-SELECTION`, so that they can be accessed.

## Defining Interfaces

The definition of an `intf` interface is enclosed in the following statements:

[`INTERFACE intf.`](../abap-declarations/abapinterface.md) ... [`ENDINTERFACE.`](../abap-declarations/abapendinterface.md)

The definition contains the declaration of all components (attributes, methods, events) of the interface. In interfaces, the same components can be defined as in class definitions. The components of an interface cannot be assigned explicitly to a [visibility section](../../abap-glossary/abenvisibility_section_glosry.md), because interface components always expand the public area of a class in which they are implemented. Interfaces do not have an implementation part since their methods must be implemented in the classes that implement the interface.
