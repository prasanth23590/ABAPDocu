---
title: "rel_exp - IS BOUND"
source_file: abenlogexp_bound.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > rel_exp - Predicates > rel_exp - Predicate Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - IS BOUND

## Syntax

``` abap
... ref IS [NOT] BOUND ...  
```

## Description

This predicate expression checks whether a reference variable contains a valid reference. A [reference variable](../../abap-glossary/abenreference_variable_glosry.md) must be specified for `ref`. This is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md).

- A data reference is valid if it can be dereferenced.

- An object reference is valid if it points to an object.

With the addition `NOT`, the expression is true if the reference variable does not contain a valid reference. In this case, the reference variable is either initial and contains the [null reference](../../abap-glossary/abennull_reference_glosry.md), or it is not initial and contains an invalid reference that does not point to an object.

## Hint

A non-initial reference variable that contains a [heap reference](../../abap-glossary/abenheap_reference_glosry.md) is generally always valid since it keeps an object alive. Only [heap references](../../abap-glossary/abenheap_reference_glosry.md) that point to lines of internal tables can become invalid when lines are deleted. A data reference variable that contains a [stack reference](../../abap-glossary/abenstack_reference_glosry.md), on the other hand, can also become invalid if the referenced data object is removed from the stack.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The logical expression in the `IF` statement is false. The data reference `dref` contains a reference to an already deleted table line.

``` abap
DATA: dref TYPE REF TO data, 
      itab TYPE TABLE OF ... 
 
FIELD-SYMBOLS <fs> TYPE ANY. 
 
dref = REF #( itab[ ... ] ). 
 
... 
 
CLEAR itab. 
 
... 
 
IF dref IS BOUND. 
  ASSIGN dref->* TO <fs>. 
ENDIF.
```

## Executable Example

[Predicate Expression `IS NOT BOUND`](abenbound_abexa.md)
