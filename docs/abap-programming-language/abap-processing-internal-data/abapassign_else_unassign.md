---
title: "ASSIGN, ELSE UNASSIGN"
source_file: abapassign_else_unassign.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning References > Assigning Field Symbols > ASSIGN"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ASSIGN, ELSE UNASSIGN

## Syntax

``` abap
... ELSE UNASSIGN ...  
```

## Description

This addition to the statement [`ASSIGN`](abapassign.md) unassigns the field symbol if the assignment is not successful. The addition can be specified for the following variants of the `ASSIGN` statement:

- [dynamic assignments](abapassign_mem_area_dynamic_dobj.md)

- [assignments of dynamic components](abapassign_dynamic_components.md)

- [dynamic access](abapassign_mem_area_dynamic_access.md)

- [assignment of a table expression](abapassign_mem_area_writable_exp.md)

These variants set `sy-subrc`. If the assignment is not successful, and `sy-subrc` is set to 4 or 8, then:

- If `ELSE UNASSIGN` is specified, no memory area is assigned to the field symbol. The field symbol has the state unassigned after the `ASSIGN` statement.

- If `ELSE UNASSIGN` is not specified, the field symbol keeps its previous state.

## Hints

- For the [static variant](abapassign_mem_area_static_dobj.md) of the `ASSIGN` statement, the addition `ELSE UNASSIGN` is implicitly set and cannot be used explicitly.

- Using the addition for the variants listed above harmonizes their behavior with the behavior of the static variant.

- Setting a field symbol to unassigned in case of an unsuccessful assignment prevents unintentional use of a previous assignment.

- Using the addition allows the success of the assignment to be checked using the predicate [`IS ASSIGNED`](../abap-program-flow-logic/abenlogexp_assigned.md) as well as checking `sy-subrc`.

- The assignment variants for constructor expressions [`NEW`](abapassign_mem_area_writable_exp.md) or [`CASE`](abapassign_mem_area_writable_exp.md) are either successful or lead to an exception and the addition `ELSE UNASSIGN` is not possible.

- If the addition is specified, but the assignment is interrupted by an exception and `sy-subrc` is not set, the field symbol keeps its previous state.

- The addition is not possible for obsolete variants of the `ASSIGN` statement.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After a successful assignment, the next assignment is not successful because of a wrong dynamic specification. `sy-subrc` is set to 4 and the field symbol that was assigned before is unassigned.

``` abap
FINAL(field) = `exists`. 
 
ASSIGN ('field') TO FIELD-SYMBOL(<fs>) ELSE UNASSIGN. 
ASSERT sy-subrc = 0 AND <fs> IS ASSIGNED. 
 
ASSIGN ('exists') TO <fs> ELSE UNASSIGN. 
ASSERT sy-subrc = 4 AND <fs> IS NOT ASSIGNED.
```
