---
title: "ABAP Objects - Friends, Friendship Between Classes"
source_file: abenfriends.html
section: "ABAP Programming Language > ABAP - ABAP Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Friends, Friendship Between Classes

There is normally a strict separation between external (`PUBLIC`) and internal (`PROTECTED` and `PRIVATE`) classes. A user can only access the public components of a class. This allows the internal implementation of a class to be changed without invalidating its users.

In rare cases, however, classes must work so closely together that they require access to their mutually invisible components. The concept of friendship between classes was developed so that these components do not need to be made available to all users at the same time.

## Friends

A class can grant friendship to other classes and interfaces (and thus to all classes that implement the interface). To do this, the `FRIENDS` additions of the [`CLASS ... DEFINITION`](../abap-declarations/abapclass_definition.md) statement must be used, which lists all of the classes and interfaces to which friendship should be granted. These friends are given access to all components of the class granting the friendship, regardless of their [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) or the addition [`READ-ONLY`](../abap-declarations/abapdata_options.md), and can always create instances of this class regardless of the addition `CREATE` of the statement [`CLASS`](../abap-declarations/abapclass.md).

### Hint

Caution is advised when granting friendship to a global interface. Each class that implements the interface becomes a friend of the class granting the friendship. The use of a global interface should be limited by means like the [package concept](../../abap-glossary/abenpackage_concept_glosry.md) in order to restrict this group.

## Friendship is Unilateral

Granting friendship is a unilateral principle. A class that grants friendship is not automatically a friend of its friends. If the class that grants friendship wants to access the non-public components of a friend, the latter must also explicitly grant friendship.

## Inheritance, Interfaces, and Friendship

Heirs of [friends](../../abap-glossary/abenfriend_glosry.md) and interfaces that contain a friend as a component interface also become friends. For this reason, extreme care should be taken when offering a friendship. The higher a friend is in the inheritance tree, the more subclasses are given access to all of the components of the class granting friendship. A class that grants friendship to the root class `object` is given all classes from ABAP Objects as friends and therefore has no privacy whatsoever. Conversely, it is relatively safe to grant friendship to a final class since only this class is specified as a friend.

Granting friendship is not inherited, in contrast to the [friend](../../abap-glossary/abenfriend_glosry.md) property. A friend of a superclass is, therefore, not automatically a friend of its subclasses.

## The FRIENDS Additions

The `CLASS ... DEFINITION` statement has three different `FRIENDS` additions:

- [`... FRIENDS cif1 ... cifn`](../abap-declarations/abapclass_options.md)

  This addition can be specified when defining any local class of a program. Friendship can be granted to all classes or interfaces of the same program and to the classes and interfaces of the class library. In particular, the local classes of a class pool can grant friendship to the global class of that class pool.

- [`... GLOBAL FRIENDS cif1 ... cifn`](../abap-declarations/abapclass_options.md)

  This addition can only be used with global classes. Friendship can be granted to all other global classes and interfaces.

- [`... LOCAL FRIENDS cif1 ... cifn`](../abap-declarations/abapclass_local_friends.md)

  This addition is not specified when the class is declared, but instead defines its own statement. In a class pool, the global class can use this statement to grant friendship to the local classes and interfaces of its own class pool. While the `CLASS` statement for the actual class declaration is valid for the entire class, the statement `CLASS ... DEFINITION LOCAL FRIENDS cif1 ... cifn.` is specified directly in the include program for defining local classes and interfaces.

### Executable Example

[Friendship](abenfriends_abexa.md)
