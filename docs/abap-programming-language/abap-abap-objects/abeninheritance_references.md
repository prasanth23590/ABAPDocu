---
title: "ABAP Objects - Inheritance and Polymorphism"
source_file: abeninheritance_references.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Inheritance"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Inheritance and Polymorphism

Since a subclass contains all components of all superclasses along the inheritance tree and the interfaces of methods cannot be changed, a reference variable that is typed with reference to a superclass or with reference to an interface implemented by a superclass may contain references to objects of all subclasses of this superclass. This means that the content of a reference variable typed with reference to a subclass can always be assigned to reference variables typed with reference to one of its superclasses or their interfaces ([upcast](../../abap-glossary/abenup_cast_glosry.md)). In particular, the target variable can always be typed with reference to the class `object`.

A static user can use a reference variable to address those components that are visible to it that are already in the superclass to which the reference variable refers. This means that it cannot address any specializations that have been added to the subclasses. In [dynamic accesses](abenclass_components_addressing.md), however, all components can be addressed.

When an instance method is redefined in one or more subclasses, different implementations of the method can be executed after a method call using the same reference variable, depending on where the class of the referenced object is located in the inheritance tree. This property, that different classes can have the same interface and can therefore be addressed using reference variables of one type is called [polymorphism](../../abap-glossary/abenpolymorphism_glosry.md).
