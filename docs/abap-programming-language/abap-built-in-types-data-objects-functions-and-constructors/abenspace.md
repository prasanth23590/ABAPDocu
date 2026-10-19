---
title: "The Constant space"
source_file: abenspace.html
section: "ABAP Programming Language > ABAP - Built-In Types, Data Objects, Functions, and Constructors > Built-In Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# The Constant space

The program-global constant `space` has the data type `c`, length 1, and contains a blank character.

## Hints

- For the constant `space`, trailing blanks are ignored in most operand positions, as for all character-like fields with fixed lengths. The constant `space` should therefore not be used in such positions.

- The name `space` is reserved and cannot be used in any context for other data objects, structure components, attributes, or formal parameters.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following [concatenation](../abap-processing-internal-data/abapconcatenate.md) is a string with exactly one blank. The blanks in the first two `spaces` specified are ignored. Blanks are only respected after `SEPARATED BY`. Except for `space`, this example also applies to a [text field literal](../../abap-glossary/abentext_field_literal_glosry.md) `' '` with exactly one blank character.

``` abap
DATA text TYPE string. 
 
CONCATENATE space space INTO text SEPARATED BY space.
```
