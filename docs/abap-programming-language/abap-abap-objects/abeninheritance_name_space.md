---
title: "ABAP Objects - Inheritance and the Component Namespace"
source_file: abeninheritance_name_space.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Inheritance"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Inheritance and the Component Namespace

A subclass contains all components of all its superclasses. Only the public and the protected components are visible. This is why all public and protected components of a path of an inheritance tree are located in a single namespace and must have unique names. Private components, on the other hand, must have unique names within a class.

When methods are [redefined](abeninheritance_redefinition.md), the newly implemented method hides the identically named method of the superclass. As soon as the method is redefined, it replaces the old method to ensure that the name remains unique. The [pseudo reference](../../abap-glossary/abenpseudo_reference_glosry.md) [`super->`](../abap-calling-and-exiting-program-units/abapcall_method_meth_super.md) can be used in subclasses to access a method of the direct superclass hidden by a redefinition.
