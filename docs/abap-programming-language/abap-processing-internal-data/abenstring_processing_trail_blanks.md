---
title: "Trailing Blanks in Character String Processing"
source_file: abenstring_processing_trail_blanks.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Character String and Byte String Processing, Overview"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Trailing Blanks in Character String Processing

There is a major difference between data types of fixed length and text strings regarding the treatment of blanks:

- All blanks are generally preserved in operations with operands of the data type `string`.

- In assignments and statements for character string processing, leading blanks for operands of data types with fixed lengths (`c`, `n`, `d`, and `t` or character-like structures) are generally preserved and trailing blanks are truncated. Exceptions to this rule are explained in the affected statements.

If the result of a statement for character string processing is assigned to an operand, it is generally padded on the right with blanks if the result is shorter than the length of the operand. Assignments to a string generally adapt the string length to the length of the result. Exceptions to this rule are explained in the affected statements.

## Hints

- Truncating trailing blanks especially affects the [text field literal](../../abap-glossary/abentext_field_literal_glosry.md) `' '` and the constant [`space`](../abap-built-in-types-data-objects-functions-and-constructors/abenspace.md). These should therefore never be listed in operand positions where trailing blanks are truncated.

- In result fields that are too long, padding with blanks can produce invalid values, if the fields have the type `n`, `d`, or `t`.

- The preservation of trailing blanks can be forced for assignments using the addition `RESPECTING BLANKS` of the statement [`CONCATENATE`](abapconcatenate.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following [concatenation](abapconcatenate.md) is a string with exactly one blank. The blank characters in `space` and `' '` are ignored. At the operand position after `SEPARATED BY` however, the blank character that is contained explicitly in `''` is not ignored. If the addition `RESPECTING BLANKS` was used, the result would be a string with three blanks.

``` abap
DATA text TYPE string. 
 
CONCATENATE space ' ' INTO text SEPARATED BY ''.
```
