---
title: "ASSIGN, dynamic_dobj"
source_file: abapassign_mem_area_dynamic_dobj.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning References > Assigning Field Symbols > ASSIGN > ASSIGN, mem_area"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ASSIGN, dynamic_dobj

## Syntax

``` abap
... { (dobj_name) }   
  | { dref->* }   
  | { dobj INCREMENT inc } ...  
```

### Alternative

[1. `... (dobj_name)`](abapassign_mem_area_dynamic_dobj.md#alternative-1)

[2. `... dref->*`](abapassign_mem_area_dynamic_dobj.md#alternative-2)

[3. `... dobj INCREMENT inc`](abapassign_mem_area_dynamic_dobj.md#alternative-3)

## Overview

### Description

These variants for specifying the memory area [`mem_area`](abapassign_mem_area.md) of the statement [`ASSIGN`](abapassign.md) dynamically are used to dynamically access data objects.

In an inline declaration of the field symbol using [`FIELD-SYMBOL(<fs>)`](../abap-declarations/abenfield-symbol_inline.md), its typing is performed with the generic type `data`.

In these variants, the statement `ASSIGN` sets the return code `sy-subrc`. If the assignment is successful, `sy-subrc` is set to 0, otherwise to 4. In these variants, no exception occurs in case of an unsuccessful assignment. If the assignment is not successful, the state of the field symbol depends on the addition [`ELSE UNASSIGN`](abapassign_else_unassign.md):

- If `ELSE UNASSIGN` is not specified, the field symbol keeps its previous state.

- If `ELSE UNASSIGN` is specified, no memory area is assigned to the field symbol. The field symbol has the state unassigned after the `ASSIGN` statement.

### Hint

If `ELSE UNASSIGN` is not specified, it is not sufficient to evaluate the [predicate expression](../../abap-glossary/abenpredicate_expression_glosry.md) [`<fs> IS ASSIGNED`](../abap-program-flow-logic/abenlogexp_assigned.md) but `sy-subrc` must be checked. If `ELSE UNASSIGN` is specified, the predicate expression as well as `sy-subrc` can be evaluated.

## Alternative 1

`... (dobj_name)`

\*\*\*This syntax is only supported temporarily in the current ABAP language version and must be replaced with valid syntax for that version.\*\*\*.

### Description

In this dynamic variant of `mem_area`, the memory area is not specified [directly](abapassign_mem_area_static_dobj.md), but as content of a character-like data object `(dobj_name)` in parentheses. The following can be specified for `dobj_name`:

- Literal or constants

  If the data object `dobj_name` is specified as a character literal or as a constant, it can be evaluated statically, and the specified data object is recognized as the used object.

- Variable

  If the data object `dobj_name` is specified as a variable, it is specified only dynamically, and the content is not evaluated statically.

When the statement is executed, `dobj_name` is not evaluated until runtime in both cases. The name in `dobj_name` is structured in exactly the same way as if specified directly: When executing the statement, the content of `dobj_name` must be the name of a data object which may contain offsets and lengths, structure component selectors, and other [component selectors](../../abap-glossary/abencomponent_selector_glosry.md) for assigning structure components, attributes in classes or attributes in objects. The content of `dobj_name` does not have to be in uppercase letters.

`dobj_name` can contain a chain of names consisting of component selectors. For an individual name or if the first name is followed by an object component selector (`->`), the specified data object is searched for according to the following hierarchy:

1.  If the statement is located in a [procedure](../../abap-glossary/abenprocedure_glosry.md), the system searches for the local data objects of the procedure.

2.  If the statement is located in a [method](../../abap-glossary/abenmethod_glosry.md), the system searches in the visible attributes of a class in the method. In instance methods, this means a search of the [static type](../../abap-glossary/abenstatic_type_glosry.md) of `me` (special case of `cref->(attr_name)` in [`dynamic_access`](abapassign_mem_area_dynamic_access.md)).

3.  The system searches in the global data of the current program.

4.  If the statement is in an [instance method](../../abap-glossary/abeninstance_method_glosry.md), the system searches in the [dynamic type](../../abap-glossary/abendynamic_type_glosry.md) of `me` (special case of `cref->(attr_name)` in [`dynamic_access`](abapassign_mem_area_dynamic_access.md)).

If the data object is found and the name is followed by an object component selector (`->`), the search for the following names is continued from left to right, as described under [`dynamic_access`](abapassign_mem_area_dynamic_access.md).

If the first name is followed by a class component selector (`=>`), the specified class is searched for, as described under [`dynamic_access`](abapassign_mem_area_dynamic_access.md), and the search is then continued accordingly from left to right.

### Hints

- This variant should not be used any more. Especially for accessing structure components, [other variants](abapassign_dynamic_components.md) are preferable.

- Writable expressions [`writable_exp`](abapassign_mem_area_writable_exp.md) cannot be specified dynamically in `dobj_name`.

- For internal use only, the name in `dobj_name` can also have the form *(PROG)DOBJ*, where *PROG* is the name of an ABAP program and *DOBJ* the name of a global data object of this program, whereby the name is not case-sensitive. In ABAP for Cloud Development no assignment is executed and `sy-subrc` is set to *4*.

- Dynamically specifying a structure component using a structure component selector is less effective than using the addition `COMPONENT OF STRUCTURE`.

## Alternative 2

`... dref->*`

### Description

When specifying a dereferenced data reference `dref` for `mem_area` using the dereferencing operator `->*`, the memory area of the data object is assigned to the field symbol to which `dref` points. If the reference variable `dref` does not reference a data object, the assignment is not performed and `sy-subrc` is set to 4.

Unlike all other operand positions, where a data reference that does not point to a data object raises an exception, no exception occurs in the statement `ASSIGN` and `sy-subrc` is set to 4.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Assigning a dereferenced data reference that is initial. Here, no exception occurs.

``` abap
DATA dref TYPE REF TO data. 
 
ASSIGN dref->* TO FIELD-SYMBOL(<fs>) ELSE UNASSIGN. 
 
IF sy-subrc <> 0. 
  ... 
ENDIF.
```

## Alternative 3

`... dobj INCREMENT inc`

\*\* This syntax is not available in the current ABAP language version.\*\*
