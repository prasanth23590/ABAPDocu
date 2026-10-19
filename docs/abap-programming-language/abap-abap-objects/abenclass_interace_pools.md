---
title: "ABAP Objects - Statements in Class Pools and Interface Pools"
source_file: abenclass_interace_pools.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Statements in ABAP Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Statements in Class Pools and Interface Pools

Class pools and interface pools are the ABAP programs where [global classes](../../abap-glossary/abenglobal_class_glosry.md) and [global interfaces](../../abap-glossary/abenglobal_interface_glosry.md) of the class library are defined. They are created in the [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md).

Each class pool or interface pool can only contain one global class or one global interface. The global class or global interfaces are declared using the following statements:

- [`CLASS ... PUBLIC.` ... `ENDCLASS.`](../abap-declarations/abapclass.md)

- [`INTERFACE ... PUBLIC.` ... `ENDINTERFACE.`](../abap-declarations/abapinterface.md)

## Further Statements in Class Pools

In addition to the declaration of the global class, a class pool can only contain the following statements:

- Declaration of local data types using the statement [`TYPES`](../abap-declarations/abaptypes.md). These data types can be used by the global class in the private visibility section and in the implementation part.

- Declaration of local constants using the statement [`CONSTANTS`](../abap-declarations/abapconstants.md). These data types can be used by the global class in the private visibility section and in the implementation part.

- Declaration of local interfaces using the statements [`INTERFACE` ... `ENDINTERFACE`](../abap-declarations/abapinterface.md). These can be used by the global class in the private visibility section and in the implementation part.

- Declaration and implementation of local classes using the statements [`CLASS` ... `ENDCLASS`](../abap-declarations/abapclass.md). These can be used by the global class in the private visibility section and in the implementation part.

Locally defined types, classes, and interfaces in class pools can be used in the following ways:

- Only the methods of the global class access the local declarations and implementations in the program. These provide auxiliary methods, for example, which should not be visible in the interface of the global class. This is the most common scenario. Any changes made to local declarations in the program do not affect the interface of the global class.

- Apart from the methods of the global class, declarations in the private visibility section of the class also refer to the local declarations in the program. This is a more unusual scenario, in which changes made to the local declarations affect the interface of the global class and [subclasses](../../abap-glossary/abensubclass_glosry.md), and [friends](../../abap-glossary/abenfriend_glosry.md) of the global class are recompiled before the next execution.

## Further Statements in Interface Pools

In addition to the declaration of the global interface, an interface pool cannot contain its own declarations or implementations.

## Program Organization

Like any other ABAP program, class and interface pools consist of a global declaration part for declarations and an implementation part for implementations (procedures).

- The global declaration part of a class pool can therefore contain the declarations of local data types, local interfaces, and local classes, in addition to the actual declaration part of the global class. The implementation part of a class pool can contain the implementation parts of local classes in addition to the implementation part of the global class.

- The global declaration part of an interface pool can only contain the declaration of the global interface and the implementation part of an interface pool is always empty.

The [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md) organize the various declarations and implementations of a class or interface pool in [include programs](../../abap-glossary/abeninclude_program_glosry.md) whose names are usually not visible to the developer. Include programs exist for:

- Each visibility section in the declaration part of the global class

- Each implementation of a method of the global class

- Local declarations and implementations ([CCIMP include](../../abap-glossary/abenccimp_glosry.md) and [CCDEF include](../../abap-glossary/abenccdef_glosry.md)).

- Test classes in ABAP Unit

## Restrictions

Apart from the statements listed above, no statements other than `CLASS - ENDCLASS` and `INTERFACE - ENDINTERFACE` are required and are therefore not allowed in class pools.
