---
title: "Operands in Character String and Byte String Processing"
source_file: abenstring_processing_operands.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Character String and Byte String Processing, Overview"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Operands in Character String and Byte String Processing

- [Operands in Character String Processing](abenstring_processing_operands.md#operands-in-character-string-processing)

- [Operands in Byte String Processing](abenstring_processing_operands.md#operands-in-byte-string-processing)

## Operands in Character String Processing

In character string processing, which is defined by the addition `IN CHARACTER MODE` in overloaded statements, and in statements that only support character string processing, the relevant operands must be character-like because the operands are processed by character and the storage of the characters in the memory depends on the [code page](../../abap-glossary/abencodepage_glosry.md) used. This condition is vital to ensure that character string processing functions correctly.

In Standard ABAP, only data objects, return values, or results with the character-like data types `c`, `n`, and `string`, and the date/time types `d` and `t`, or structures with exclusively flat character-like components are allowed as character-like operands. Data objects with the types `n`, `d`, and `t` and structures with exclusively character-like components are handled like data objects with the type `c`.

### Hints

- If the character-like data objects `n`, `d`, and `t` are used in character string processing, it must be noted that the type-compliant conversion rules do not apply to the assignment of interim results to target fields and instead the conversion rules for data type `c` apply.

- No structures can be used as character-like operands in [string expressions](abapcompute_string.md) and [string functions](abenstring_functions.md) with named parameters.

## Operands in Byte String Processing

In byte string processing, which is triggered by the addition `IN BYTE MODE` in overloaded statements, and in the statements `GET BIT` and `SET BIT`, the relevant operands must be byte-like. This is because the operands are processed by byte.
