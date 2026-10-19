---
title: "ABAP Objects - Classes"
source_file: abenclasses.html
section: "ABAP Programming Language > ABAP - ABAP Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Classes

The type of an [object](../../abap-glossary/abenobject_glosry.md) is referred to as its class. A class is an abstract representation of an object or, visually speaking, a set of building instructions for objects. To describe the properties of objects, classes contain [components](abenclass_components.md) that define the status and behavior of objects.

## Global Classes and Local Classes

Classes can be [defined](abenclass_interface_definition.md) globally in the class library of the [repository](../../abap-glossary/abenrepository_glosry.md) or locally in an ABAP program.

[Global classes](../../abap-glossary/abenglobal_class_glosry.md) are coded in a special ABAP program, a [class pool](../../abap-glossary/abenclass_pool_glosry.md), whereas [local classes](../../abap-glossary/abenlocal_class_glosry.md) can be coded in almost every ABAP program. Global classes are visible in all ABAP programs. The usability depends on the package check. Local classes can be used statically only in their own program. Dynamic access is also possible beyond program boundaries, but it is not recommended. When a global class is first used, the class pool is loaded to the [internal session](../../abap-glossary/abeninternal_session_glosry.md) of the user. The local classes of a class pool can be used by its global class.

Except for the storage type and the visibility, there are hardly any conceptual differences between global and local classes. Those few differences include the fact that, in the public interface of a global class, only references to public types are possible and that a distinction is made between global and local [friends](../../abap-glossary/abenfriend_glosry.md).

In addition, it also does not make any difference whether a method of a local class or a global class is called. For this reason, classes used by multiple programs should be created exclusively in the class library. The reuse of local classes by using [include programs](../../abap-glossary/abeninclude_program_glosry.md) should be avoided.

### Executable Example

[Classes](abenclass_abexa.md)
