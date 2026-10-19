---
title: "METHODS, constructor"
source_file: abapmethods_constructor.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Methods > METHODS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# METHODS, constructor

## Syntax

``` abap
METHODS constructor [FINAL]   
  [IMPORTING parameters [PREFERRED PARAMETER p]]   
  [{RAISING exc1|RESUMABLE(exc1) exc2|RESUMABLE(exc2) ...}   
  |{EXCEPTIONS exc1 exc2 ...}].  
```

[`FINAL`](abapmethods_abstract_final.md) · [`parameters`](abapmethods_parameters.md)

### Addition

[1. `... IMPORTING parameters`](abapmethods_constructor.md#addition-1)

[2. `... RAISING exc1|RESUMABLE(exc1) exc2|RESUMABLE(exc2) ...`](abapmethods_constructor.md#addition-2)

[3. `... EXCEPTIONS exc1 exc2 ...`](abapmethods_constructor.md#addition-3)

[4. `... FINAL`](abapmethods_constructor.md#addition-4)

## Overview

### Description

This statement declares the instance constructor `constructor` of a class. In a local class, it can be specified in all [visibility sections](../../abap-glossary/abenvisibility_section_glosry.md) that are more general than or equal to the instantiability specified in the [`CREATE`](abapclass_options.md) addition of the statement [`CLASS DEFINITION`](abapclass_definition.md):

\| \|`CREATE PUBLIC`\|`CREATE PROTECTED`\| `CREATE PRIVATE`\|

\|`PUBLIC SECTION`\|X\|X\|X\| \|`PROTECTED SECTION`\|-\|X\|X\| \|`PRIVATE SECTION`\|-\|-\|X\|

In a global class, the instance constructor must always be declared in the public visibility section, for technical reasons. In principle, the declaration can be made in the same visibility sections as in the table above, however the internal organization of a global class can cause incorrect syntax errors when the class is used.

Each class has a predefined method called `constructor`. By declaring this explicitly, the interface of the method `constructor` can be defined as class-specific, and its functions can be implemented. Without explicit declaration, the instance constructor assumes the parameter interface of the direct superclass and calls it implicitly.

If the instance constructor is implemented in a subclass, the instance constructor of the superclass must be called explicitly using [`super->constructor`](../abap-calling-and-exiting-program-units/abapcall_method_meth_super.md), even if the latter is not explicitly declared. The exception to this are direct subclasses of the root node `object`. The following restrictions apply before the superclass constructor is called:

- The instance constructor does not have access to the instance components of its class. The self-reference [`me->`](../abap-built-in-types-data-objects-functions-and-constructors/abenme.md) must not be used. The static components of its class can be accessed, but not using `me->`.

- Before the superclass constructor is called, an instance constructor cannot be exited using statements such as `RETURN` or `CHECK`.

After the superclass constructor has been called, the self-reference `me->` can be used and instance components can be accessed.

For each instance of a class, the instance constructor is called only once using the statement [`CREATE OBJECT`](../abap-creating-objects-and-values/abapcreate_object.md) immediately after it has been created. Here, appropriate actual parameters must be assigned to all non-optional input parameters, return values can be assigned to non-class-based exceptions, and class-based exceptions can be declared. It is not possible to call the instance constructor explicitly, unless the superclass constructor is called using `super->constructor` in the redefined constructor of a subclass.

When an instance constructor is executed, the current instance is temporarily the type of the class in which the constructor is defined. This has the following effects:

- If methods are called when a superclass constructor is executed, the implementations of the superclass are executed and not the redefinitions of subclasses. The specification of `me->` to address a redefined method in the new subclass has no effect.

- Abstract methods of the same class cannot be called in an instance constructor.

- When a superclass constructor is executed, attempts to access components of the subclass using a [downcast](../../abap-glossary/abendown_cast_glosry.md) produce a runtime error.

- While the superclass constructor is being executed, the predicate expression [`IS INSTANCE OF`](../abap-program-flow-logic/abenlogexp_instance_of.md) is true for the current superclass and not true for the subclass that has just been created.

### Hints

- Instance constructors are an exception to the rule that all non-private components on a path in the inheritance hierarchy are in the same namespace. The instance constructor of each class has its own interface and its own implementation. An instance constructor cannot be redefined.

- Instance constructors are declared in the public [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) of a class purely for technical reasons. The actual visibility is controlled by the addition `CREATE {PUBLIC|PROTECTED|PRIVATE}` of the statement [`CLASS DEFINITION`](abapclass_definition.md). It is recommended that the instance constructor of a local class is declared in the visibility section that corresponds to the instantiability, because this allows the components declared there to be used in the constructor interface. However, for global classes, only the public section is possible.

- Before the superclass constructor is called, static components of the same class cannot be accessed using `me->` in the instance constructor of a subclass. However, access to the components without using `me->` or using the class name and the class component selector `=>` is always possible.

## Addition 1

`... IMPORTING parameters`

## Addition 2

`... RAISING exc1|RESUMABLE(exc1) exc2|RESUMABLE(exc2) ...`

## Addition 3

`... EXCEPTIONS exc1 exc2 ...`

### Description

The addition `IMPORTING` can be used to define input parameters according to the same rules as for general methods. The additions `RAISING` and `EXCEPTIONS` for the declaration of class-based exceptions or the definition of non-class-based exceptions also have the same meaning as for general methods.

### Hint

When the instance constructor is executed, the same applies to [resumable exceptions](../../abap-glossary/abenresumable_exception_glosry.md) as to all other methods. If processing can be resumed successfully, the system continues to create the object.

## Addition 4

`... FINAL`

### Description

Instance constructors are implicitly final. The addition [`FINAL`](abapmethods_abstract_final.md) can be specified, but it is not necessary.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The class `c3` inherits from class `c2`, which inherits from class `c1`. The instance constructor `constructor` is explicitly declared in all classes and must be implemented in all classes, whereby the implementation in a subclass must contain the call of the superclass constructor. The predicate expression [`IS INSTANCE OF`](../abap-program-flow-logic/abenlogexp_instance_of.md) shows that every instance constructor for an instance of its own class is executed when an object of class `c3` is instantiated.

``` abap
CLASS output DEFINITION. 
  PUBLIC SECTION. 
    CLASS-DATA out TYPE REF TO if_demo_output. 
    CLASS-METHODS class_constructor. 
ENDCLASS. 
 
CLASS output IMPLEMENTATION. 
  METHOD class_constructor. 
    out = cl_demo_output=>new( ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    METHODS constructor. 
ENDCLASS. 
 
CLASS c2 DEFINITION INHERITING FROM c1. 
  PUBLIC SECTION. 
    METHODS constructor. 
ENDCLASS. 
 
CLASS c3 DEFINITION INHERITING FROM c2. 
  PUBLIC SECTION. 
    METHODS constructor. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD constructor. 
    IF me IS INSTANCE OF c1. 
      output=>out->write( 'C1' ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS c2 IMPLEMENTATION. 
  METHOD constructor. 
    super->constructor( ). 
    IF me IS INSTANCE OF c2. 
      output=>out->write( 'C2' ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS c3 IMPLEMENTATION. 
  METHOD constructor. 
    super->constructor( ). 
    IF me IS INSTANCE OF c3. 
      output=>out->write( 'C3' ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    NEW c3( ). 
    output=>out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```
