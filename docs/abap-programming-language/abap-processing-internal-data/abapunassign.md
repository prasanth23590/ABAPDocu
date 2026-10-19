---
title: "UNASSIGN"
source_file: abapunassign.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning References > Assigning Field Symbols"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# UNASSIGN

## Syntax

``` abap
UNASSIGN <fs>.  
```

## Description

This statement initializes the field symbol `<fs>`. After the statement, the field symbol does not reference a memory area and the [predicate expression](../../abap-glossary/abenpredicate_expression_glosry.md) [`<fs> IS ASSIGNED`](../abap-program-flow-logic/abenlogexp_assigned.md) is false.

## Hints

- The statement [`CLEAR <fs>`](abapclear.md) does not initialize the field symbol and the memory area that is assigned to the field symbol is initialized instead.

- Unlike the initialization of reference variables, the statement `UNASSIGN` does not affect the [Garbage Collector](../../abap-glossary/abengarbage_collector_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A field symbol to which a memory area is assigned is initialized with `UNASSIGN`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FIELD-SYMBOLS <fs> TYPE string. 
 
ASSIGN `text` TO <fs>. 
IF <fs> IS ASSIGNED. 
  out->write( 'assigned' ). 
ENDIF. 
 
UNASSIGN <fs>. 
IF <fs> IS NOT ASSIGNED. 
  out->write( 'unassigned' ). 
ENDIF. 
 
out->display( ).
```
