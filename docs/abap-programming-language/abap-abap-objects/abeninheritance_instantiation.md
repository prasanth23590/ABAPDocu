---
title: "ABAP Objects - Inheritance and Instantiation"
source_file: abeninheritance_instantiation.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Inheritance"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Inheritance and Instantiation

When a subclass is instantiated, all superclasses are instantiated simultaneously, whereby the initialization of superclass attributes is ensured by calling the superclass constructors, as described in [Inheritance and Constructors](abeninheritance_constructors.md).

In each individual class, the additions `CREATE PUBLIC|PROTECTED|PRIVATE` of the statement [`CLASS`](../abap-declarations/abapclass.md) control who can create an instance of the class or, in other words, can call its instance constructor.

This has the following consequences:

If a superclass was defined in a path of the inheritance tree using the addition `CREATE PRIVATE`, external users cannot instantiate a subclass, and a subclass cannot even instantiate itself because it has no access to the instance constructor of the superclass.

It would therefore be useful to assign the addition `FINAL` to a class that was defined using the addition `CREATE PRIVATE`, to prevent subclasses from being derived. Otherwise subclasses of these superclasses have an implicit addition `CREATE NONE`.

The only exception to this rule is if a superclass that can be privately instantiated offers its [friendship](abenfriends.md) to its subclasses. The direct path is rarely the case here because the superclass must know its subclasses for it to be possible. However, a superclass can also offer friendship to an interface which, in turn, can be implemented by its subclasses.

Conversely, objects of subclasses cannot be created in their superclass if these are declared using `CREATE PROTECTED` or `CREATE PRIVATE`, unless they are [friends](../../abap-glossary/abenfriend_glosry.md) of its subclasses.

## Overview of All Cases

### Superclass with No Addition or CREATE PUBLIC

Subclasses can have any `CREATE` addition, regardless of whether they are a friend of the superclass. Without an addition, they inherit the property `CREATE PUBLIC`. The instance constructor of the superclass is visible to everyone. The subclass controls the visibility of its own instance constructor, independently of the superclass.

### Superclass with Addition CREATE PROTECTED.

Subclasses can have any `CREATE` addition, regardless of whether they are a friend of the superclass. Without an addition, they inherit the attribute `CREATE PROTECTED`. The superclass allows its subclasses unlimited instantiation and therefore also allow its [protected](../../abap-glossary/abenprotected_glosry.md) instance constructor to be published.

### Superclass with Addition CREATE PRIVATE

**Subclass is Not a Friend of the Superclass**

The subclass has the implicit addition CREATE NONE. Nobody other than the superclass itself can call its instance constructor, which means that the subclass cannot be instantiated. None of the CREATE additions are allowed because this would definitely mean unauthorized publishing of the superclass constructor.

**Subclass is a Friend of the Superclass**

If the subclass has no addition, it inherits the attribute CREATE PRIVATE. However, all CREATE additions are allowed. As a friend, the subclass can publish the private constructor of the superclass in any form.
