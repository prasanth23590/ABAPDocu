---
title: "ABAP Objects - Inheritance"
source_file: abeninheritance.html
section: "ABAP Programming Language > ABAP - ABAP Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Inheritance

The concept of inheritance makes it possible to derive new classes from existing classes. This is done using the addition [`INHERITING FROM`](../abap-declarations/abapclass_options.md) of the statement [`CLASS ... DEFINITION`](../abap-declarations/abapclass_definition.md). The new class adopts or inherits all components of the existing class. The new class is called the subclass and the existing class is called the superclass.

Without further declarations, a subclass contains exactly the components of the superclass. However, only the components of the public, protected, and package [visibility sections](../../abap-glossary/abenvisibility_section_glosry.md) of the superclass are visible in the subclass. Although the private components of the superclass also exist in the subclass, they are not visible. In a subclass, private components with the same name as in the superclass can be declared. Each class works with its private components. As long as a method inherited from the superclass is not redefined, it uses the private attributes of the superclass and not the possible subclass attributes of the same name.

If the superclass does not have a private visibility section, the subclass is an exact copy of the superclass. It is possible, however, to define further components in the subclass. These are used to specialize the subclass with respect to the superclass. If a subclass is used again as the superclass for a new class, it can be specialized further.

Each class can have multiple direct subclasses, but only one direct superclass. ABAP Objects implements [single inheritance](../../abap-glossary/abensingle_inheritance_glosry.md). If subclasses inherit from superclasses that are subclasses themselves, all classes involved form an inheritance tree whose specialization increases each time a hierarchy level is added. Conversely, the specialization decreases the closer a level is located to the root node of the inheritance tree. The root node of all inheritance trees in ABAP Objects is the predefined empty class `object`. This class is the most generic class possible because it does not contain attributes or methods. When a new class is defined, it must not be specified explicitly as a superclass because it always exists implicitly. In the inheritance tree, two adjacent nodes are known as the direct superclass and subclass, and all preceding and succeeding nodes are collectively referred to as superclasses and subclasses. The declaration of the components of a subclass is distributed across all superclasses of the inheritance tree.

## Executable Example

[Inheritance](abeninheritance_abexa.md)
