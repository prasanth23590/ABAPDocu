---
title: "FIELD-SYMBOLS"
source_file: abapfield-symbols.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Field Symbols"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FIELD-SYMBOLS

## Syntax

``` abap
FIELD-SYMBOLS <fs> typing.  
```

[`typing`](abentyping_syntax.md)

### Addition

[`... typing`](abapfield-symbols.md#addition)

## Overview

### Description

The statement `FIELD-SYMBOLS` declares a [field symbol](../../abap-glossary/abenfield_symbol_glosry.md) `<fs>`. The [naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md) apply to the name `fs`. The angle brackets distinguish field symbols from data objects and are mandatory. Field symbols can be declared in any [procedure](../../abap-glossary/abenprocedure_glosry.md) and in the global declaration part of an ABAP program, but not in the declaration part of a class or an interface. A field symbol can be used in all operand positions where it is visible and that fit the [typing](abentyping.md) defined using `typing`.

A field symbol is initial directly after its declaration, which means that it does not refer to a memory area. A memory area must be assigned to it (normally using the statement [`ASSIGN`](../abap-processing-internal-data/abapassign.md)) before it can be used as an operand. Otherwise an exception is raised.

### Hints

- An [inline declaration](../../abap-glossary/abeninline_declaration_glosry.md) of field symbols can be made using the declaration operator [`FIELD-SYMBOL`](abenfield-symbol_inline.md).

- The angle brackets are a part of the name, which means that a field symbol could potentially be called `<>`. Such a field symbol cannot be used at all operand positions and leads to syntax errors from case to case. Therefore, the name `<>` should be avoided.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaring a field symbol `<number>` and using it at operand positions.

``` abap
FIELD-SYMBOLS <number> TYPE i. 
 
ASSIGN 1 TO <number>. 
 
... 
 
IF <number> > 10. 
  CLEAR <number>. 
ENDIF.
```

## Addition

`... typing`

### Description

The addition `typing` is used to type the field symbol. The syntax of `typing` is described under [Typing](abentyping_syntax.md). The typing specifies which memory areas [can](abentyping_check_general.md) be assigned to the field symbol and in which operand positions it can be used.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Typing of a field symbol `<itab>` as an internal table and a field symbol `<wa>` with a completely generic type.

``` abap
FIELD-SYMBOLS: <itab> TYPE ANY TABLE, 
               <wa>   TYPE any. 
 
... 
 
ASSIGN <itab>[ KEY primary_key ('...') = '...' ] TO <wa>.
```
