---
title: "ABAP Objects - Visibility Sections in Classes"
source_file: abenclass_visibility.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Classes > ABAP Objects - Components of Classes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Visibility Sections in Classes

The [declaration part](../../abap-glossary/abendeclaration_part_glosry.md) of a class can be split into up to three different visibility sections.

These sections define the external visibility of the [class components](abenclass_components.md) and therefore the interfaces of the class for all users allowed by the [package concept](../../abap-glossary/abenpackage_concept_glosry.md). Each component of a class must be explicitly assigned to one of the visibility sections. Only the [friends](../../abap-glossary/abenfriend_glosry.md) of a class are not affected by the associated restrictions.

- **Public visibility section**

  All components declared in the public visibility section defined using [`PUBLIC SECTION`](../abap-declarations/abappublic.md) are accessible to all users as well as in the methods of all inheritors and the class itself. The public components are the interface of the class and for all its users.

- **Protected visibility section**

  All components declared in the protected visibility section defined using [`PROTECTED SECTION`](../abap-declarations/abapprotected.md) are accessible in the methods of all inheritors and in the class itself. Protected components are a special interface of the class and its subclasses.

- **Private visibility section**

  All components declared in the private visibility section defined using [`PRIVATE SECTION`](../abap-declarations/abapprivate.md) are only accessible in the methods of the class itself and are also not visible to the inheritors. The private components are therefore not an interface to the users of the class.

The following table summarizes the visibilities of a class:

| **Visible for**            | **`PUBLIC SECTION`** | **`PROTECTED SECTION`** | **`PRIVATE SECTION`** |
|----------------------------|----------------------|-------------------------|-----------------------|
| Same class and its friends | X                    | X                       | X                     |
| Any subclasses             | X                    | X                       | \-                    |
| Any repository objects     | X                    | \-                      | \-                    |

## Hints

- A subclass can generally never access the protected components of a subclass of a different branch in the inheritance hierarchy, even if they are inherited from a common superclass. This rule can only be lifted by a friendship.

- For technical reasons a [global class](../../abap-glossary/abenglobal_class_glosry.md) that can be part of an inheritance tree that is

  - a [subclass](../../abap-glossary/abensubclass_glosry.md)

  - a non-[final](../../abap-glossary/abenfinal_glosry.md) class that is not a subclass but can be a [superclass](../../abap-glossary/abensuperclass_glosry.md)

    must contain the statements [`PROTECTED SECTION`](../abap-declarations/abapprotected.md) and [`PRIVATE SECTION`](../abap-declarations/abapprivate.md) also for empty protected and private sections.

## Encapsulation

The three visibility sections form the basis for the important feature of encapsulation in ABAP Objects. When declaring a class, as few components as possible should be declared in the public section and these public components must be carefully designed. For global classes, they cannot be changed once the class has been released.

### Hint

The class is the smallest encapsulation unit in ABAP Objects. A method can therefore use all components of all instances of the same class, except for the components of its own class. An exception to this rule are subclasses that cannot access the private components of superclasses if they are not their [friends](abenfriends.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the method `m1` of the class `c1`, reference variables of static type `c1` can be used to access the protected attribute `a11` and the private attribute `a12` of any objects of `c1`. In the method `m2` of the subclass `c2`, reference variables of static type `c1` or `c2` can similarly be used to access the protected attribute `a11`. It is not possible to access the private attribute of the superclass with either reference variable.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    METHODS m1. 
  PROTECTED SECTION. 
    DATA a11 TYPE i. 
  PRIVATE SECTION. 
    DATA a12 TYPE i. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD m1. 
 
    DATA lref1 TYPE REF TO c1. 
 
    lref1->a11 = 0. "OK 
 
    lref1->a12 = 0. "OK 
 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS c2 DEFINITION INHERITING FROM c1. 
  PUBLIC SECTION. 
    METHODS m2. 
ENDCLASS. 
 
CLASS c2 IMPLEMENTATION. 
  METHOD m2. 
 
    DATA: lref1 TYPE REF TO c1, 
          lref2 TYPE REF TO c2. 
 
    lref1->a11 = 0. "OK 
 
    lref2->a11 = 0. "OK 
 
    "lref1->a12 = 0. "Syntax error, access to a11 not allowed 
 
    "lref2->a12 = 0. "Syntax error, a12 is not visible 
 
  ENDMETHOD. 
ENDCLASS.
```
