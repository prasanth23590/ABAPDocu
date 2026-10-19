---
title: "CLASS, class_options"
source_file: abapclass_options.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > CLASS > CLASS, DEFINITION"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS, class_options

## Syntax

``` abap
 ... [PUBLIC] 
    [INHERITING FROM superclass] 
    [ABSTRACT] 
    [FINAL] 
    [CREATE {PUBLIC|PROTECTED|PRIVATE}] 
    [FOR TESTING] 
    [FOR BEHAVIOR OF] 
    [[GLOBAL] FRIENDS class1 class2 ... 
                      intf1  intf2  ...] ...  
```

[`FOR TESTING`](../abap-program-maintenance/abapclass_for_testing.md) · [`FOR BEHAVIOR OF`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapclass_for_behavior_of.md)

### Addition

[1. `... PUBLIC`](abapclass_options.md#addition-1)

[2. `... INHERITING FROM superclass`](abapclass_options.md#addition-2)

[3. `... ABSTRACT`](abapclass_options.md#addition-3)

[4. `... FINAL`](abapclass_options.md#addition-4)

[5. `... CREATE {PUBLIC|PROTECTED|PRIVATE}`](abapclass_options.md#addition-5)

[7. `... [GLOBAL] FRIENDS class1 class2 ... intf1 intf2 ...`](abapclass_options.md#addition-7)

## Overview

### Description

Definition of the properties of a class. The following additions define special classes:

- [`FOR TESTING`](../abap-program-maintenance/abapclass_for_testing.md) defines a [test class](../../abap-glossary/abentest_class_glosry.md) for [ABAP Unit](../../abap-glossary/abenabap_unit_glosry.md).

- [`FOR BEHAVIOR OF`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapclass_for_behavior_of.md) defines the global class of an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md).

## Addition 1

`... PUBLIC`

### Description

The addition `PUBLIC` makes the class `class` a [global class](../../abap-glossary/abenglobal_class_glosry.md) in the class library. The addition `PUBLIC` can only be applied to one class of a [class pool](../../abap-glossary/abenclass_pool_glosry.md). Any class without the addition `PUBLIC` applied to it is a local class in its program.

### Hints

- References to public data types can only be made in the [public](../../abap-glossary/abenpublic_glosry.md) [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) of a global class.

- Data types and constants declared in the [public](../../abap-glossary/abenpublic_glosry.md) [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) of global classes using the statements `TYPES` and `CONSTANTS` replace their declarations in [type pools](../../abap-glossary/abentype_pool_glosry.md).

- A global class is a global [object type](../../abap-glossary/abenobject_type_glosry.md) and is in the same namespace as all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of the global class `CL_DEMO_SPFLI`.

``` abap
CLASS cl_demo_spfli DEFINITION 
  PUBLIC 
  FINAL 
  CREATE PUBLIC.
```

## Addition 2

`... INHERITING FROM superclass`

### Description

The addition `INHERITING FROM` is used to derive the class `class` by inheriting from the superclass `superclass` and thus to its direct subclass. The superclass `superclass` can be any non-final class that is visible at this point.

Each class can only have one superclass, but multiple direct subclasses (single inheritance). Every class without the addition `INHERITING FROM` inherits implicitly from the predefined empty and abstract class `object`. All classes in [ABAP Objects](../../abap-glossary/abenabap_objects_glosry.md) form an inheritance tree in which each class has a unique path to the root object `object`.

The class `class` inherits all components of `superclass`, without changing their visibility sections. Only the components of [public](../../abap-glossary/abenpublic_glosry.md) and [protected](../../abap-glossary/abenprotected_glosry.md) visibility sections of the superclass are visible in the subclass. The properties of the inherited components cannot be changed. In the subclass, additional components can be declared and inherited methods redefined, which means that they can be reimplemented without interface modification.

### Hint

The public and protected components of all classes within a path of the inheritance tree are in the same namespace. New components in a subclass must not have the same name as a public or protected component that was inherited from the superclasses.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Subclass `cls2` inherits from a superclass `cls1`. `cls1` is an implicit subclass of the empty class `object`.

``` abap
CLASS cls1 DEFINITION. 
  ... 
ENDCLASS. 
 
CLASS cls2 DEFINITION 
           INHERITING FROM cls1. 
  ... 
ENDCLASS.
```

## Addition 3

`... ABSTRACT`

### Description

The addition `ABSTRACT` defines an abstract class `class`. No instances can be created from an abstract class. To use the instance components of an abstract class, a [concrete](../../abap-glossary/abenconcrete_glosry.md) subclass of the class must be instantiated.

### Hint

Abstract classes are not supported by the [ABAP Test Double Framework](https://help.sap.com/docs/ABAP_PLATFORM_NEW/c238d694b825421f940829321ffa326a/804c251e9c19426cadd1395978d3f17b).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Subclass `cls2` inherits from an abstract superclass `cls1`.

``` abap
CLASS cls1 DEFINITION ABSTRACT. 
  ... 
ENDCLASS. 
 
CLASS cls2 DEFINITION 
           INHERITING FROM cls1. 
  ... 
ENDCLASS.
```

## Addition 4

`... FINAL`

### Description

The addition `FINAL` defines a final class `class`. No subclasses can be derived from a final class. All methods of a final class are implicitly final and cannot be explicitly declared as final.

### Hints

- Final classes complete an inheritance tree.

- In classes that are both abstract and final, only the static components can be used. Although instance components can be declared, they cannot be used. Specifying `ABSTRACT` and `FINAL` together, therefore, is useful only for [static classes](../../abap-glossary/abenstatic_class_glosry.md).

- Final classes are not supported by the [ABAP Test Double Framework](https://help.sap.com/docs/ABAP_PLATFORM_NEW/c238d694b825421f940829321ffa326a/804c251e9c19426cadd1395978d3f17b).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In this example, an abstract class `c1` and a final class `c2` are defined, whereby `c2` inherits from `c1`. In `c2`, `m1` can be accessed but not `a1`.

``` abap
CLASS c1 DEFINITION ABSTRACT. 
  PROTECTED SECTION. 
    METHODS m1. 
  PRIVATE SECTION. 
    DATA a1 TYPE string VALUE `Attribute A1 of class C1`. 
ENDCLASS. 
 
CLASS c2 DEFINITION INHERITING FROM c1 FINAL. 
  PUBLIC SECTION. 
    METHODS m2. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD m1. 
    cl_demo_output=>new( 
     )->write_text( a1 
     )->display( ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS c2 IMPLEMENTATION. 
  METHOD m2. 
    m1( ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA oref TYPE REF TO c2. 
    CREATE OBJECT oref. 
    oref->m2( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Addition 5

`... CREATE {PUBLIC|PROTECTED|PRIVATE}`

### Description

The addition `CREATE` specifies the context in which the class `class` can be instantiated, that is, where the statement [`CREATE OBJECT`](../abap-creating-objects-and-values/abapcreate_object.md) can be executed for this class and in which visibility section the [instance constructor](../../abap-glossary/abeninstance_constructor_glosry.md) of the class can be declared.

- A class with the addition `CREATE PUBLIC` can be instantiated anywhere where the class is visible within the framework of the [package concept](../../abap-glossary/abenpackage_concept_glosry.md). `CREATE PUBLIC` is the default, i.e. not specifying the addition `CREATE ...` means the class is implicitly specified with `CREATE PUBLIC`.

- A class with the addition `CREATE PROTECTED` can only be instantiated in methods of its subclasses, of the class itself, and of its [friends](../../abap-glossary/abenfriend_glosry.md).

- A class with the addition `CREATE PRIVATE` can only be instantiated in methods of the class itself or of its [friends](../../abap-glossary/abenfriend_glosry.md). This means, in particular, that it cannot be instantiated as an inherited component of subclasses.

The instantiability of a subclass depends on the direct superclass as follows:

- Immediate subclasses of `object`, or classes with the addition `CREATE PUBLIC` inherit the addition `CREATE PUBLIC` implicitly. All `CREATE` additions that then overwrite the inherited addition can be specified explicitly.

- Immediate subclasses of classes with the addition `CREATE PROTECTED` inherit the addition `CREATE PROTECTED` implicitly. All `CREATE` additions that then overwrite the inherited addition can be specified explicitly.

- Immediate subclasses of classes with the addition `CREATE PRIVATE` that are not [friends](../../abap-glossary/abenfriend_glosry.md) of the class inherit the addition `CREATE NONE` implicitly. They cannot be instantiated and no explicit `CREATE` additions can be specified. Immediate subclasses that are friends of the class inherit the addition `CREATE PRIVATE` implicitly. All `CREATE` additions can be specified explicitly for friends of superclasses that can be instantiated privately.

The statement [`METHODS constructor`](abapmethods_constructor.md) used to declare the instance constructor of a local class can be specified in all [visibility sections](../../abap-glossary/abenvisibility_section_glosry.md) that are more general than or the same as the instantiability specified in the addition `CREATE`. In global classes, the declaration is only possible in the public visibility section for technical reasons.

### Hints

- It is recommended that a class that can be instantiated privately is specified as a final class, since its subclasses cannot be instantiated unless they are friends of the class.

- it is further recommended that the instance constructor of local classes is declared in the visibility section of the class that matches its instantiability, since this enables the components declared there to be used in the constructor interface.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The class `cls` can only be privately instantiated. The separate method `factory` is allowed to perform an instantiation and returns a reference to the generated object.

``` abap
CLASS cls DEFINITION CREATE PRIVATE. 
  PUBLIC SECTION. 
    CLASS-METHODS factory RETURNING VALUE(ref) TYPE REF TO cls. 
    ... 
ENDCLASS. 
 
CLASS cls IMPLEMENTATION. 
  METHOD factory. 
    ref = NEW #( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Addition 7

`... [GLOBAL] FRIENDS class1 class2 ... intf1 intf2 ...`

### Description

The addition `FRIENDS` makes the classes `class1 class2 ...` or the interfaces `intf1 intf2 ...` into [friends](../abap-abap-objects/abenfriends.md) of the class `class`. At the same time, all subclasses of `class1 class2 ...`, all classes that implement one of the interfaces `intf1 intf2 ...`, and all interfaces that contain one of the interfaces `intf1 intf2 ...` as a component interface become friends of the class `class`. At least one class or one interface must be specified.

The [friends](../../abap-glossary/abenfriend_glosry.md) of a class have unrestricted access to all components of the class, regardless of the [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) or the addition [`READ-ONLY`](abapdata_options.md), and can create instances of the class without any restrictions.

The friends of `class` are not automatically made friends of the subclasses of `class`. The addition `FRIENDS` does not make the class `class` a friend of its friends.

Without the addition `GLOBAL`, all classes and interfaces that are visible at this point can be specified for `class1 class2...` and `intf1 intf2 ...` If global classes and interfaces of the Class Library are made friends, it should be ensured that the local classes of other ABAP programs are not visible in these global classes. The components of a local class `class` cannot be accessed statically by these friends.

The addition `GLOBAL` is only allowed if the addition `PUBLIC` is also used, namely for a global class of a [class pool](../../abap-glossary/abenclass_pool_glosry.md). Other global classes and interfaces from the class library can be specified after `GLOBAL FRIENDS`.

### Hint

The addition `FRIENDS` must be specified as the last addition after the other additions.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In this example, the interface `i1` and therefore the implementing class `c2` are friends of the class `c1`. The class `c2` can instantiate `c1` and access its private component `a1`.

``` abap
INTERFACE i1. 
  ... 
ENDINTERFACE. 
 
CLASS c1 DEFINITION CREATE PRIVATE FRIENDS i1. 
  PRIVATE SECTION. 
    DATA a1 TYPE c LENGTH 10 VALUE 'Class 1'. 
ENDCLASS. 
 
CLASS c2 DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES i1. 
    METHODS m2. 
ENDCLASS. 
 
CLASS c2 IMPLEMENTATION. 
  METHOD m2. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    DATA oref TYPE REF TO c1. 
    CREATE OBJECT oref. 
    out->write_text( oref->a1 ). 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```

### Executable Example

[Friendship](../abap-abap-objects/abenfriends_abexa.md)
