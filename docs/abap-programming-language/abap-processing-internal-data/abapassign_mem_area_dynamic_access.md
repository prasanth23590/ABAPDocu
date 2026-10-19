---
title: "ASSIGN, dynamic_access"
source_file: abapassign_mem_area_dynamic_access.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning References > Assigning Field Symbols > ASSIGN > ASSIGN, mem_area"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ASSIGN, dynamic_access

## Syntax

``` abap
 ... { cref->(attr_name) }   
  | { iref->(attr_name) }   
  | { (clif_name)=>(attr_name) }   
  | { (clif_name)=>attr }   
  | { clif=>(attr_name) } ...  
```

### Alternative

[1. `... cref->(attr_name)`](abapassign_mem_area_dynamic_access.md#alternative-1)

[2. `... iref->(attr_name)`](abapassign_mem_area_dynamic_access.md#alternative-2)

[3. `... (clif_name)=>(attr_name)`](abapassign_mem_area_dynamic_access.md#alternative-3)

[4. `... (clif_name)=>attr`](abapassign_mem_area_dynamic_access.md#alternative-4)

[5. `... clif=>(attr_name)`](abapassign_mem_area_dynamic_access.md#alternative-5)

## Overview

### Description

These variants for specifying the memory area [`mem_area`](abapassign_mem_area.md) of the statement [`ASSIGN`](abapassign.md) dynamically are designed especially for dynamic access to attributes of classes or interfaces (Dynamic Access). The same syntax as for alternatives 1 and 2 is also possible for [components of structures](abapassign_dynamic_components.md).

In an inline declaration of the field symbol using [`FIELD-SYMBOL(<fs>)`](../abap-declarations/abenfield-symbol_inline.md), its typing is performed with the generic type `data`.

In these variants, the statement `ASSIGN` sets the return code `sy-subrc`. If the assignment is successful, `sy-subrc` is set to 0. If the assignment is not successful, `sy-subrc` is set to 4. In these variants, no exception occurs in case of an unsuccessful assignment. If `sy-subrc` is set to 4, the state of the field symbol depends on the addition [`ELSE UNASSIGN`](abapassign_else_unassign.md):

- If `ELSE UNASSIGN` is not specified, the field symbol keeps its previous state.

- If `ELSE UNASSIGN` is specified, no memory area is assigned to the field symbol. The field symbol has the state unassigned after the `ASSIGN` statement.

### Hints

- Field symbols to which instance attributes or parts of instance attributes are assigned have a memory-preserving effect on the associated object.

- If `ELSE UNASSIGN` is not specified, it is not sufficient to evaluate the [predicate expression](../../abap-glossary/abenpredicate_expression_glosry.md) [`<fs> IS ASSIGNED`](../abap-program-flow-logic/abenlogexp_assigned.md) but `sy-subrc` must be checked. If `ELSE UNASSIGN` is specified, the predicate expression as well as `sy-subrc` can be evaluated.

## Alternative 1

`... cref->(attr_name)`

### Description

This form is possible for all visible attributes of objects. `cref` can be any [class reference variable](../../abap-glossary/abenclass_reference_variabl_glosry.md) that points to an object that contains the attribute specified in a character-like field `attr_name`. The attribute is searched for first in the [static type](../../abap-glossary/abenstatic_type_glosry.md) of `cref` and then in the [dynamic type](../../abap-glossary/abendynamic_type_glosry.md).

The attribute name does not have to be in uppercase letters. It can contain offsets/lengths, structure component selectors, object component selectors, and class component selectors, in order to assign parts of the attribute or referenced objects of the attribute.

Unlike all other operand positions, where an object reference that does not point to an object raises an exception, no exception occurs in the statement `ASSIGN` and `sy-subrc` is set to 4.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Dynamic assignment of an object attribute of an object to a field symbol. The assignment is made via an object reference variable of the static type of the root class `object`, which can point to any object.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    METHODS meth IMPORTING oref TYPE REF TO object 
                           attr TYPE string. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD meth. 
    ASSIGN oref->(attr) TO FIELD-SYMBOL(<attr>). 
    ... 
  ENDMETHOD. 
ENDCLASS.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Behavior for an initial reference. No exception occurs but `sy-subrc` is set to 4 for dynamic access.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    DATA attr TYPE string VALUE 'foo'. 
ENDCLASS. 
 
CLASS example DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS example IMPLEMENTATION. 
  METHOD main. 
    DATA(oref) = NEW demo( ). 
    ASSIGN oref->('attr') TO FIELD-SYMBOL(<attr>) 
           ELSE UNASSIGN. 
    ASSERT <attr> IS ASSIGNED. 
 
    CLEAR oref. 
    ASSIGN oref->('attr') TO <attr> 
           ELSE UNASSIGN. 
    ASSERT sy-subrc = 4 AND <attr> IS NOT ASSIGNED. 
  ENDMETHOD. 
ENDCLASS.
```

## Alternative 2

`... iref->(attr_name)`

### Description

This form may be used for all interface attributes of objects. `iref` can be any [interface reference variable](../../abap-glossary/abeninterface_ref_variable_glosry.md) that points to an object that contains the interface attribute specified in a character-like field `attr_name`. The attribute is searched for only in the [static type](../../abap-glossary/abenstatic_type_glosry.md) of `iref`.

The attribute name does not have to be in uppercase letters. It can contain offsets/lengths, structure component selectors, object component selectors, and class component selectors, in order to assign parts of the attribute or referenced objects of the attribute.

Unlike all other operand positions, where an object reference that does not point to an object raises an exception, no exception occurs in the statement `ASSIGN` and `sy-subrc` is set to 4.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Dynamic assignment of an object attribute to a field symbol. The assignment is made via an interface reference variable.

``` abap
INTERFACE intf. 
  CONSTANTS attr TYPE string VALUE `interface attribute`. 
ENDINTERFACE. 
 
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES intf. 
ENDCLASS. 
 
CLASS example DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS example IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    DATA iref TYPE REF TO intf. 
    iref = NEW demo( ). 
 
    ASSIGN iref->('attr') TO FIELD-SYMBOL(<fs>). 
 
    out->write( <fs> ). 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Alternative 3

`... (clif_name)=>(attr_name)`

## Alternative 4

`... (clif_name)=>attr`

### Description

These forms may be used for all visible static attributes. Classes and interfaces and also attributes can be specified dynamically in character-like fields `clif_name` or `attr_name`. The attribute `attr` can, however, also be specified directly. The system searches for the class or interface first and then the attribute.

The content of `attr_name` and `clif_name` does not have to be in uppercase letters. `attr_name` can contain offsets/lengths, structure component selectors, object component selectors, and class component selectors, in order to assign parts of the attribute or referenced objects of the attribute. Here, no offsets/lengths or object component selectors can be specified after a directly specified attribute `attr`.

## Alternative 5

`... clif=>(attr_name)`

### Description

This form may be used for all visible static attributes. The class or interfaces is specified directly, and the attribute specified dynamically in a character-like field `attr_name`. The system searches for the attribute in the specified class or interface.

The content of `attr_name` does not have to be in uppercase letters. `attr_name` can contain offsets/lengths, structure component selectors, object component selectors, and class component selectors, in order to assign parts of the attribute or referenced objects of the attribute.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Different dynamic assignments of a static class attribute to field symbols.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(clif_name) = `cl_abap_browser`. 
FINAL(attr_name) = `xlarge`. 
 
ASSIGN (clif_name)=>(attr_name) TO FIELD-SYMBOL(<fs1>). 
ASSIGN (clif_name)=>xlarge TO FIELD-SYMBOL(<fs2>). 
ASSIGN cl_abap_browser=>(attr_name) TO FIELD-SYMBOL(<fs3>). 
 
out->write( 
  |(clif_name)=>(attr_name):     { <fs1> }\n| && 
  |(clif_name)=>xlarge:          { <fs2> }\n| && 
  |cl_abap_browser=>(attr_name): { <fs3> }\n| ). 
 
out->display( ).
```
