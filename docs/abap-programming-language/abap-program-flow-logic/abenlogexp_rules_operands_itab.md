---
title: "rel_exp - Comparing Internal Tables"
source_file: abenlogexp_rules_operands_itab.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Rules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparing Internal Tables

Internal tables can be compared with other internal tables if their line types are comparable. Internal tables are compared based on the following hierarchy:

1.  The internal table that has more lines than the other internal table is the larger table.

2.  Internal tables with the same number of lines are compared line by line. If an internal table contains nested internal tables, these are compared recursively. Two internal tables are identical if the content of each corresponding line matches. If two internal tables are not identical, the first non-matching pair of lines determines the result of the comparison.

## Hint

If an internal table with a [header line](../../abap-glossary/abenheader_line_glosry.md) is specified as the operand of an assignment, the header line is addressed in nearly all [operand positions](../abap-operands/abenoperands_data_objects.md) and not the [table body](../../abap-glossary/abentable_body_glosry.md). To address the table body of a table with a header, `[]` must be appended to the name.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

`itab2` is greater than `itab1`, despite having the same number of lines, because the content of its second line is greater than that of `itab1`.

``` abap
DATA: 
  itab1 TYPE TABLE OF i WITH EMPTY KEY, 
  itab2 TYPE TABLE OF i WITH EMPTY KEY. 
 
itab1 = VALUE #( ( 1 ) ( 2 ) ( 3 ) ). 
itab2 = VALUE #( ( 1 ) ( 3 ) ( 3 ) ). 
 
ASSERT itab2 > itab1.
```

## Executable Example

[Comparing Internal Tables](abencompare_table_abexa.md).
