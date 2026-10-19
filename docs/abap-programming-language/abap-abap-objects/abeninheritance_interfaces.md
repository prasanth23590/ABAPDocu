---
title: "ABAP Objects - Inheritance and Interfaces"
source_file: abeninheritance_interfaces.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Inheritance"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Inheritance and Interfaces

[Interfaces](abeninterfac.md) are standalone constructs in ABAP Objects that support [polymorphism](../../abap-glossary/abenpolymorphism_glosry.md) in classes. The polymorphism of interfaces is based on the fact that each class that implements an interface can implement its methods differently. All interface components look similar externally, which is why [interface reference variables](../../abap-glossary/abeninterface_ref_variable_glosry.md) can point to objects of all classes that implement the associated interface.

The interface concept exists completely independent of and in addition to the inheritance concept. The classes of an inheritance tree can implement any number of interfaces, but each interface can be implemented only once in each inheritance tree. This ensures that each interface component `comp` has a unique name across the entire inheritance tree `intf~icomp` and that it is contained in all subclasses starting with the class that implements it. [Interface reference variables](../../abap-glossary/abeninterface_ref_variable_glosry.md) that can point to a class of the inheritance tree can also point to all subclasses. Once they are implemented, interface methods are fully functioning components of a class and can be redefined in subclasses. In the case of interface methods defined as optional using [`DEFAULT`](../abap-declarations/abapmethods_default.md), and without explicit implementation, the default behavior is applied along a path of an inheritance tree until a redefinition with explicit implementation occurs.
