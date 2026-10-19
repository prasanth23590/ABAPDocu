---
title: "ABAP Objects - Methods"
source_file: abenmethods.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Methods

Methods are declared using the statements

- [`METHODS`](abapmethods.md) for instance methods

- [`CLASS-METHODS`](abapclass-methods.md) for static methods

These are only possible in the declaration part of classes and interfaces.

Methods determine the behavior of a class. [Instance methods](../../abap-glossary/abeninstance_method_glosry.md) are declared by the statement [`METHODS`](abapmethods.md), [static methods](../../abap-glossary/abenstatic_method_glosry.md) are declared by the statement [`CLASS-METHODS`](abapclass-methods.md). The declaration defines the interface of a method. For special tasks there are different types of methods:

- General [instance methods](abapmethods_general.md) and [static methods](abapclass-methods_general.md)

- Functional [instance methods](abapmethods_functional.md) and [static methods](abapclass-methods_functional.md)

- [Instance constructors](abapmethods_constructor.md) and [static constructors](abapclass-methods_constructor.md)

- [Event handlers](abapmethods_event_handler.md) and [static event handlers](abapclass-methods_event_handler.md)

The following methods are also available:

- [Test methods](../abap-program-maintenance/abapmethods_testing.md) of ABAP Unit, which can only be declared as instance methods.

- [AMDP](../abap-database-access/abenamdp_methods.md) methods, which are implemented in a database-specific language and not in ABAP.
