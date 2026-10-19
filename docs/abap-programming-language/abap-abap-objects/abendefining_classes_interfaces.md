---
title: "ABAP Objects - Statements for Defining Classes and Interfaces"
source_file: abendefining_classes_interfaces.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Statements in ABAP Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Statements for Defining Classes and Interfaces

These statements are used to define classes and interfaces and their components. They can be used in any ABAP program where classes and interfaces can be defined.

## Statements for Defining Classes

****Defining the Declaration Part****

``` abap
CLASS ... DEFINITION ... 
 ... 
ENDCLASS ...
```

****Defining the Implementation Part****

``` abap
CLASS ... IMPLEMENTATION ... 
 ... 
ENDCLASS ...
```

## Statements for Defining Components of Classes

****Statements in the Declaration Part****

``` abap
PUBLIC SECTION. 
PROTECTED SECTION. 
PRIVATE SECTION. 
 
TYPES ... 
 
INTERFACES ... 
ALIASES ... 
 
CONSTANTS ... 
 
CLASS-DATA ... 
DATA ... 
 
CLASS-METHODS ... 
METHODS ... 
 
CLASS-EVENTS ... 
EVENTS ...
```

****Statements in the Implementation Part****

``` abap
METHOD ... 
 ... 
ENDMETHOD.
```

## Statements for Defining Interfaces

****Declaring the Interface****

``` abap
INTERFACE ... 
 ... 
ENDINTERFACE ...
```

## Statements for Declaring Components of Interfaces

The same statements can be used to declare components in interfaces as in the declaration part of classes.

## Note

The components of classes or interfaces, that is, their attributes, methods, and events) are declared in their declaration parts. `TYPES` can also be used to declare local data types. `ALIASES` can be used to declare alias names for the components of implemented interfaces. In a class, all declarations must be assigned to one of the four [visibility sections](../../abap-glossary/abenvisibility_section_glosry.md) defined by the corresponding statements.

The implementation part of a class can only contain method implementations between `METHOD - ENDMETHOD`. In methods, only the [statements for method implementations](abendefining_methods.md) can be used.

**No** statements other than those specified above are necessary for defining classes or interfaces and therefore no other statements are allowed between `CLASS - ENDCLASS` or `INTERFACE - ENDINTERFACE` outside of methods.
