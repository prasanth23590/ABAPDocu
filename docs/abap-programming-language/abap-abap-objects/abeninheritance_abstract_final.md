---
title: "ABAP Objects - Abstract and Final Methods and Classes"
source_file: abeninheritance_abstract_final.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Inheritance"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Abstract and Final Methods and Classes

Abstract and final methods or classes can be defined using the additions **`ABSTRACT`** and **`FINAL`** of the statements [`METHODS`](../abap-declarations/abapmethods.md) and [`CLASS`](../abap-declarations/abapclass.md).

Abstract methods are declared in abstract classes and cannot be implemented in the same class, only in a subclass of the inheritance tree. Abstract classes cannot, therefore, be instantiated. A non-abstract method is a concrete method. With the exception of the instance constructor, concrete instance methods of a class can also call their abstract methods.

Final methods can no longer be redefined in subclasses. They cannot have any additional subclasses and close an inheritance tree definitively.

## Hints

- In classes that are both abstract and final, only the static components can be used. Although instance components can be declared, they cannot be used. Specifying `ABSTRACT` and `FINAL` together is therefore only useful for [static classes](../../abap-glossary/abenstatic_class_glosry.md).

- Private methods cannot be redefined and therefore cannot be abstract.
