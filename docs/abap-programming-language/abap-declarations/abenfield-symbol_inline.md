---
title: "FIELD-SYMBOL, Inline Declaration for Field Symbols"
source_file: abenfield-symbol_inline.html
section: "ABAP Programming Language > ABAP - Declarations > Inline Declarations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FIELD-SYMBOL, Inline Declaration for Field Symbols

## Syntax

``` abap
... FIELD-SYMBOL(<fs>) ...  
```

## Description

A declaration expression with the declaration operator `FIELD-SYMBOL` declares a [field symbol](../../abap-glossary/abenfield_symbol_glosry.md) `<fs>` to which a memory area is assigned in the current operand position. The declared field symbol is visible statically in the program from `FIELD-SYMBOL(<fs>)` and is valid in the current [context](../../abap-glossary/abenobj_context_glosry.md). The declaration is made when the program is compiled, regardless of whether the statement is actually executed.

The declaration operator `FIELD-SYMBOL` can be specified in every valid [declaration position](../abap-syntax-elements-of-an-abap-program/abendeclaration_positions.md), which involves assignments of the memory area only. The typing of the field symbol is determined using the statically known type of the assigned memory area. It can be generic or complete.

A field symbol `<fs>` declared inline cannot be used in a read position of the same statement.

## Hints

- A valid statement with an inline declaration of a field symbol can generally be interpreted as a short form for a declaration statement used as a direct prefix.

  `FIELD-SYMBOLS <fs> TYPE ...`

  `... <fs> ...` Exceptions to this rule occur only if an identically named field symbol from a more global context is used in the same statement. This data object is still valid in the statement and is only hidden after the statement.

- Just like the statement `FIELD-SYMBOLS`, an inline declaration does not open a local context for the current statement block. An inline declaration for a field symbol can only be made once within a context and the field symbol must not have been declared there using `FIELD-SYMBOLS`.

- If the type of the assigned memory area is defined by reference to a data type of the ABAP Dictionary, it is inherited with its semantic properties, such as field help, input help, or conversion exits.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Inline declaration of a field symbol for an internal table in an `ASSIGN` statement and inline declaration of a field symbol for the lines of the table in a `LOOP`.

``` abap
TYPES t_itab TYPE TABLE OF i 
             WITH NON-UNIQUE KEY table_line. 
 
FINAL(itab) = VALUE t_itab( ( 1 ) ( 2 ) ( 3 ) ). 
 
ASSIGN itab TO FIELD-SYMBOL(<itab>). 
 
LOOP AT <itab> ASSIGNING FIELD-SYMBOL(<line>). 
  ... 
ENDLOOP.
```
