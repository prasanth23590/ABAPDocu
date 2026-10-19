---
title: "itab_func - line_index"
source_file: abenline_index_function.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > itab - Built-in Functions (itab_func)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab_func - line_index

## Syntax

``` abap
... line_index( table_exp  ) ...  
```

[`table_exp`](abentable_expressions.md)

## Description

The [built-in](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) function `line_index` returns the number of the line found using the [table expression](../../abap-glossary/abentable_expression_glosry.md) [`table_exp`](abentable_expressions.md) with respect to the [table index](../../abap-glossary/abentable_index_glosry.md) used. The return value has the type `i`.

The line [`itab_line`](abentable_exp_itab_line.md) to be searched for using the table expression must be determined by a key specification. An index cannot be specified. For `table_exp`, in addition to individual table expressions, all [chainings](abentable_exp_chaining.md) whose result is a line of an internal table, that is, they are closed using angle brackets, can also be specified. The result always refers to the line specified in the final angle bracket and the key access restrictions apply only to this angle bracket.

Within `line_index`, an explicitly specified table key in the table line [`table_line`](abentable_exp_itab_line.md) of the table expression is handled in the same way as a [free search key](abapread_table_free.md) specified for this table key.

The table index used depends on the specified key as follows:

- If a search key is specified without a table key being specified explicitly, the number of a found line is returned with respect to the [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md) and, in the case of a [hashed table](../../abap-glossary/abenhashed_table_glosry.md), the value *-1*.

- If a [table key](../../abap-glossary/abentable_key_glosry.md) is specified explicitly after `KEY`, the number of a found line is returned with respect to the assigned [table index](../../abap-glossary/abentable_index_glosry.md). If the key is a [hash key](../../abap-glossary/abenhash_key_glosry.md), the value *-1* is returned.

If the line searched for is not found, no exception is raised. The value 0 is returned instead. In the case of [chainings](abentable_exp_chaining.md), of table expressions, the first unsuccessful from the left produces this value.

## Hints

- An index specified in [`itab_line`](abentable_exp_itab_line.md) of the table expression is not possible here, since it does not make sense.

- The table expression is only used to check the existence of the line number specified line. No temporary [result](abentable_exp_result.md) is created.

- The function `line_index` can be understood as a short form of the statement [`READ TABLE`](abapread_table.md) with the addition [`TRANSPORTING NO FIELDS`](abapread_table_outdesc.md) followed by the evaluation of `sy-tabix`. If a line is not found, `0` is always returned. `sy-tabix`, on the other hand, has the value where the line would be found after a binary search using `READ TABLE`.

- If a search key specified in [`table_line`](abentable_exp_itab_line.md) in the table expression covers the initial part of a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) without being specified explicitly after `KEY`, a syntax check warning is produced that can be hidden by a pragma, since the function is generally quicker if the secondary key is specified explicitly.

- As in other use cases for table expressions, it is important that no duplicate selections are made, especially in the case of `line_index`. Generally speaking, it is best not to first check the line number using `line_index` and then read the line immediately using the index.

- The [predicate function](../../abap-glossary/abenpredicate_function_glosry.md) [`line_exists`](../abap-program-flow-logic/abenline_exists_function.md) can be used to check the existence of a line. The function `line_index` can also be used to check whether a line exists. If the line is found, the result is not equal to 0 for every table category. A check on a value greater than 0, on the other hand, is sufficient only for [index tables](../../abap-glossary/abenindex_table_glosry.md) or when using [sorted keys](../../abap-glossary/abensorted_key_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The index function can be used on chained table expressions as follows, where the nested internal table accessed is taken from the example for [Chainings with Table Expressions](abentable_exp_chaining.md). The first read returns the value *1* for the first line of the innermost table. The second read returns the value *0*, since there is no line available for the index read on the outermost table.

``` abap
DATA(idx1) = line_index( 
               itab[ 2 ][ 2 ][ KEY primary_key table_line = 7 ] ). 
 
DATA(idx2) = line_index( 
               itab[ 9 ][ 2 ][ KEY primary_key table_line = 7 ] ).
```

## Executable Example

[Internal Tables, Index Function](abenline_index_abexa.md)
