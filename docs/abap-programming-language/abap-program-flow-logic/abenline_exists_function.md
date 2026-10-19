---
title: "rel_exp - line_exists"
source_file: abenline_exists_function.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > rel_exp - Predicates > rel_exp - Predicate Functions > rel_exp - Predicate Functions for Table-Like Arguments"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - line_exists

## Syntax

``` abap
... line_exists( table_exp ) ...  
```

[`table_exp`](../abap-processing-internal-data/abentable_expressions.md)

## Description

The [built-in](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) [predicate function](../../abap-glossary/abenpredicate_function_glosry.md) `line_exists` checks whether a line of an internal table [specified](../abap-processing-internal-data/abentable_exp_itab_line.md) in the [table expression](../../abap-glossary/abentable_expression_glosry.md) [`table_exp`](../abap-processing-internal-data/abentable_expressions.md) exists and returns the corresponding [truth value](../../abap-glossary/abentruth_value_glosry.md). In addition to single table expressions, [chainings](../abap-processing-internal-data/abentable_exp_chaining.md) can also be specified for `table_exp`, whose result is a line of an internal table.

Within `line_exists`, an explicitly specified table key in the table line [`table_line`](../abap-processing-internal-data/abentable_exp_itab_line.md) of the table expression is handled in the same way as a [free search key](../abap-processing-internal-data/abapread_table_free.md) specified for this table key.

## Hints

- The table expression is only used to check the existence of the specified line. No temporary [result](../abap-processing-internal-data/abentable_exp_result.md) is created.

- The predicate function `line_exists` can be considered as a short form of the statement [`READ TABLE`](../abap-processing-internal-data/abapread_table.md) with the addition [`TRANSPORTING NO FIELDS`](../abap-processing-internal-data/abapread_table_outdesc.md) followed by `sy-subrc` being checked.

- The predicate function `line_exists` cannot be used to determine the line number in a table index of a search key used for the search, since table expressions do not fill the system field `sy-tabix`. The table function [`line_index`](../abap-processing-internal-data/abenline_index_function.md) can be used instead.

- If a search key specified in [`table_line`](../abap-processing-internal-data/abentable_exp_itab_line.md) in the table expression covers the initial part of a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) without being specified explicitly after `KEY`, a syntax check warning that can be hidden by a pragma occurs, since the function is generally more performant if the secondary key is specified explicitly.

- As in other use cases of table expressions, `line_exists` must be used carefully to avoid duplicate selections. Therefore, `line_exists` should not be used to first check the existence of a line and then read it. Instead, the table expression can be [assigned to a field symbol](../abap-processing-internal-data/abapassign_mem_area_writable_exp.md) and then `sy-subrc` checked. If the line in question usually exists, the table expression can be specified in the required operand position and the exception `CX_SY_ITAB_LINE_NOT_FOUND` caught.

- As well as assigning a table expression a [default value](../abap-processing-internal-data/abentable_exp_optional_default.md) for lines that are not found, there is also the option of checking the existence of lines.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Checks whether the line exists in the internal table *flight_tab*.

``` abap
DATA flight_tab TYPE HASHED TABLE OF spfli 
                     WITH UNIQUE KEY carrid connid. 
 
SELECT * 
       FROM spfli 
       INTO TABLE @flight_tab. 
 
IF line_exists( flight_tab[ carrid = 'LH' 
                            connid = '0400' ] ). 
  ... 
ENDIF.
```
