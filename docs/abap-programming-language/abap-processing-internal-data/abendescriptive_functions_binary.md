---
title: "bchain_func - xstrlen"
source_file: abendescriptive_functions_binary.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Byte Chain Processing > Byte Chains Functions (bchain_func)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# bchain_func - xstrlen

One length function is currently available for unnamed byte-like arguments.

## Syntax

``` abap
... xstrlen( arg ) ...  
```

## Description

The [built-in function](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) `xstrlen` returns the number of bytes in `arg`. The argument `arg` is a byte-like [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md). The return value has the type `i`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A six-character text in the code page [UTF-16](../../abap-glossary/abenutf16_glosry.md) is represented by 12 bytes.

``` abap
FINAL(text) = `Hello!`. 
FINAL(hex) = cl_abap_conv_codepage=>create_out( codepage = `UTF-16` 
              )->convert( text ). 
cl_demo_output=>display( 
  |Text length {   strlen( text ) 
  }\nByte length { xstrlen( hex )  }| ).
```
