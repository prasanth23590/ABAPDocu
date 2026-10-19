---
title: "ABAP Objects - Redefining Methods"
source_file: abeninheritance_redefinition.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Inheritance"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Redefining Methods

Each subclass contains the components of all classes that are located between this class and the root node in the inheritance tree. The visibility of a component is always the same and cannot be changed. However, it is possible to redefine the public and protected instance methods of all preceding superclasses using the addition [`REDEFINITION`](../abap-declarations/abapmethods_redefinition.md) of the statement [`METHODS`](../abap-declarations/abapmethods.md), to adapt them to the required level of specialization. The interface of a redefined method cannot be changed. The method is merely reimplemented with the same name. Constructors cannot be redefined and [special rules](abeninheritance_constructors.md) apply.

The method declaration remains in the superclass, and its previous implementation is also retained there. The implementation of the redefinition is also generated for the subclass and hides the implementation of the superclass. A redefined method works with the private attributes of the subclass and not with any private superclass attributes with the same name.

Each reference that points to a subclass object uses the redefined method, even if it was typed with reference to a superclass. In particular, this also applies to the [self-reference](../../abap-glossary/abenself_reference_glosry.md) `me`. For example, if a superclass method `m1` contains a call `[me->]m2( )` and if `m2` is redefined in a subclass, the call of `m1` in an instance of the superclass causes the original method `m2` to be executed and the call of `m1` in an instance of the subclass causes the redefined method `m2` to be executed.

Within a redefined method, [`super->meth`](../abap-calling-and-exiting-program-units/abapcall_method_meth_super.md) can be used to access the hidden method, for example, to adapt and supplement its functions.
