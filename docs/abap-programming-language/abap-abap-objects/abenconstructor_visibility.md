---
title: "ABAP Objects - Visibility of Instance Constructors"
source_file: abenconstructor_visibility.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Classes > ABAP Objects - Components of Classes > ABAP Objects - Constructors of Classes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Visibility of Instance Constructors

For technical reasons, the instance constructor of a class is declared in a [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) and is therefore theoretically visible to the corresponding consumers. However, an instance constructor is only executed when an object of this class is created using `CREATE OBJECT`. Therefore, the instance constructor is only visible to the users of a class that can also create objects of this class.

The additions `CREATE PUBLIC|PROTECTED|PRIVATE` of the statement [`CLASS`](../abap-declarations/abapclass.md) determine whether each user, only the heirs, or just the class itself can create objects of the class. This means that these additions define the actual visibility of the instance constructor implicitly. Therefore, the following applies:

- The instance constructor of a class defined using `CREATE PUBLIC` can be called by any user.

- The instance constructor of a class defined using `CREATE PROTECTED` can only be called by the class itself and its subclasses.

- The instance constructor of a class defined using `CREATE PRIVATE` can only be called by the class itself.

This has the following important consequence:

If a class was defined using `CREATE PRIVATE`, only the class itself can instantiate itself. Subclasses of this class cannot even instantiate themselves, because they would have to call the superclass constructor using [`CALL super->constructor`](../abap-calling-and-exiting-program-units/abapcall_method_meth_super.md) (see also [Inheritance and Instance Creation](abeninheritance_instantiation.md)).
