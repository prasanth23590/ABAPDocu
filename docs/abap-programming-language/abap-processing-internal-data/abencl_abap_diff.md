---
title: "itab - System Class CL_ABAP_DIFF"
source_file: abencl_abap_diff.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - System Classes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - System Class CL_ABAP_DIFF

The class `CL_ABAP_DIFF` compares the content of compatible [index tables](../../abap-glossary/abenindex_table_glosry.md) and returns information about any differences found.

- The static factory method `CREATE` creates an instance of the class and returns a reference for working with the instance methods. Its importing parameters adjust the granularity of the difference determination:

  - `CASING_MODE` determines whether the comparison of character strings is case sensitive or not.

  - `CASING_MODE` determines whether leading blanks of character strings are respected or not.

  - `TRAILING_SPACES_MODE` determines whether trailing blanks of character strings are respected or not.

  - `OUTPUT_MODE` determines whether the output is shown as insert/delete or insert/delete/update operations.

- The instance method `DIFF` compares the content of two compatible [index tables](../../abap-glossary/abenindex_table_glosry.md). If the content is different, it returns an internal table that shows how the content of the first internal table can be transformed to the content of the second internal table by insert/delete or optionally by insert/delete/update operations.

- The instance method `DIFF_WITH_LINE_REF` works as `DIFF` but returns an extended result with references to the original table lines.

## Executable Example

[itab -Using `CL_ABAP_DIFF`](abencl_abap_diff_abexa.md)
