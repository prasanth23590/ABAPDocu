---
title: "DATA, REF TO"
source_file: abapdata_references.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects > DATA"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DATA, REF TO

## Syntax

``` abap
DATA ref { {TYPE REF TO type}   
         | {LIKE REF TO dobj} }   
         [VALUE IS INITIAL]   
         [READ-ONLY].  
```

[`[VALUE IS INITIAL]`](abapdata_options.md) · [`[READ-ONLY]`](abapdata_options.md)

## Description

The addition `REF TO` declares a [reference variable](../../abap-glossary/abenreference_variable_glosry.md) `ref`. The static type of the reference variable is specified after `REF TO`. The static type limits the set of objects to which `ref` can point. The dynamic type of a reference variable is the data type or the class to which it currently points. The static type is always more general or the same as the dynamic type (see also the conversion rule for reference variables).

The syntax and meaning of the additions `TYPE` and `LIKE` are the same as the definition of reference types in the section [`TYPES` - `REF TO`](abaptypes_references.md), but here they are used to create a bound reference type.

Only `IS INITIAL` can be specified as a [start value](../../abap-glossary/abenstart_value_glosry.md) after the addition [`VALUE`](abapdata_options.md).

## Hints

- Reference variables are opaque, which means their content cannot be accessed directly. A reference consists of the address of an object and other administrative information.

- A [reference](../../abap-glossary/abenreference_glosry.md) in a reference variable is valid if it points to an object. In this case the predicate expression [`IS BOUND`](../abap-program-flow-logic/abenlogexp_bound.md) is true. A non-initial reference can be invalid if it points to deleted objects. A [heap reference](../../abap-glossary/abenheap_reference_glosry.md) that points to a line in an internal table can become invalid if the line is deleted. A [stack reference](../../abap-glossary/abenstack_reference_glosry.md) can become invalid if the referenced data object is removed from the stack.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In this example, an object reference `oref` and two data references `dref1` and `dref2` are declared. Both data reference variables are typed fully and can be dereferenced using the dereferencing operator `->*` in operand positions.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    DATA a1 TYPE i VALUE 1. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA: oref  TYPE REF TO c1, 
          dref1 LIKE REF TO oref, 
          dref2 TYPE REF TO i. 
    CREATE OBJECT oref. 
    dref1 = REF #( oref ). 
    CREATE DATA dref2. 
    dref2->* = dref1->*->a1. 
  ENDMETHOD. 
ENDCLASS.
```
