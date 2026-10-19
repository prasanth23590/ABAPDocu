---
title: "rel_exp - IS ASSIGNED"
source_file: abenlogexp_assigned.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > rel_exp - Predicates > rel_exp - Predicate Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - IS ASSIGNED

## Syntax

``` abap
... <fs> IS [NOT] ASSIGNED ...  
```

## Description

This predicate expression checks whether a memory area is assigned to a field symbol `<fs>`. The expression is true if the field symbol points to a memory area. `<fs>` expects a field symbol declared using [`FIELD-SYMBOLS`](../abap-declarations/abapfield-symbols.md) or declared inline using [`FIELD-SYMBOL( )`](../abap-declarations/abenfield-symbol_inline.md).

With the addition `NOT`, the expression is true if no memory area is assigned to the field symbol.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Assignment of a data object to a field symbol if no memory area has been assigned yet.

``` abap
FIELD-SYMBOLS <fs> TYPE c. 
 
... 
 
IF <fs> IS NOT ASSIGNED. 
  ASSIGN 'Standard Text' TO <fs>. 
ENDIF. 
 
...
```
