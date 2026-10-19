---
title: "rel_exp - Tabular Comparison Operator IN"
source_file: abenlogexp_select_option.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Operators > rel_exp - Comparison Operators for All Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Tabular Comparison Operator IN

## Syntax

``` abap
... operand [NOT] IN range_tab ...  
```

## Description

In a comparison expression with the comparison operator `IN`, the conditions of a [ranges table](../../abap-glossary/abenranges_table_glosry.md) or a table of this structure are checked. This means whether an operand `operand` is checked to see whether it meets the conditions in the lines of the ranges table or not, if the addition `NOT` is specified. The tabular comparison expression is equivalent to a combination of [binary](abenlogexp_any_operand.md) or [ternary](abenlogexp_between.md) comparison expressions whose number is determined by the number of lines in the internal table.

Any internal table whose line type matches that of a ranges table or a [functional method](../../abap-glossary/abenfunctional_method_glosry.md) with the corresponding type of return value can be specified as a table `range_tab`. The ranges table can be of any table type. For the structure of a ranges tables, see [`TYPES RANGE OF`](../abap-declarations/abaptypes_ranges.md). The evaluation of a ranges table requires it to contain the valid values listed there in the columns `sign` and `option`. If the ranges table contains invalid values, an uncatchable exception is raised. If the ranges table is initial, the comparison expression is always true.

Each line of a non-initial ranges table is included in the combination using one of the following comparison expressions. Depending on the operator in the column `option`, this is a comparison between two operands using a [binary comparison operator](abenlogexp_any_operand.md) or an interval restriction using the [ternary operator](abenlogexp_between.md) `BETWEEN`.

- The operators *EQ*, *NE*, *GE*, *GT*, *LE*, and *LT* produce a size comparison:

  ... operand [`{EQ|NE|GE|GT|LE|LT}`](abenlogexp_any_operand.md) range_tab-low ... The comparison operator is derived from the content of the column `range_tab-option` and the content of the column `range_tab-low` is used as the right operand.

- The operators *CP* and *NP* produce a string comparison:

  ... operand [`{CP|NP}`](abenlogexp_strings.md) range_tab-low && range_tab-high The comparison operator is derived from the content of the column `range_tab-option` and the content of the columns `range_tab-low` and `range_tab-high` is concatenated as the right operand.

- The operators *BT* and *NB* produce a delimitation of an interval:

  ... operand \[NOT\] [`BETWEEN`](abenlogexp_between.md) range_tab-low AND range_tab-high ... The comparison is executed without the addition `NOT` if the content of the column `range_tab-option` is *BT* and with the addition `NOT` if the content is *NB*. The content of the columns `range_tab-low` and `range_tab-high` is used for the interval restrictions.

`operand` is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md) and the usual [comparison rules](abenlogexp_rules.md) apply to `operand` and the columns `low` and `high` of the ranges table. The comparison expressions of the individual lines are [combined](abenlogexp_boole.md) into a logical expression in accordance with the following hierarchy:

1.  The expressions of all lines that contain *I* in the column `sign` are combined using `OR`. If there are no lines that contain *E* in the column `sign`, this represents the entire logical expression.

2.  The expressions of all lines that contain *E* in the column `sign` are combined using `OR` and then negated using `NOT`. If there are no lines that contain *I* in the column `sign`, this represents the entire logical expression.

3.  If the content *I* and the content *E* are both in the column `sign`, `AND` is used to combine the logical expression that is produced by step 1 with the logical expression from step 2

## Hints

- The rules above can be interpreted in such a way that the lines containing *I* or *E* in the column `sign` describe two value sets. The set for *I* is the inclusive set and the set for *E* is the exclusive set. By subtracting the exclusive set from the inclusive set, a result set is calculated that contains all values for which the entire logical expression is true.

- The [comparison rules](abenlogexp_rules.md) are checked only at runtime and comparisons that are not allowed lead to exceptions.

- The operator `IN` is, due to its implementation using [binary comparison operators](abenlogexp_any_operand.md), not suitable for selecting natural-language text content.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Filling of a [ranges table](../../abap-glossary/abenranges_table_glosry.md) with a [`SELECT`](../abap-database-access/abapselect.md) statement and its use in a logical expression in the conditional operator [`COND`](abenconditional_expression_cond.md).

``` abap
DATA range_tab TYPE RANGE OF scarr-carrid. 
 
SELECT 'I' AS sign, 'EQ' AS option, carrid AS low 
       FROM scarr 
       INTO TABLE @range_tab. 
 
DATA carrid TYPE scarr-carrid. 
cl_demo_input=>request( CHANGING field = carrid ). 
 
cl_demo_output=>display( 
  COND #( WHEN to_upper( carrid ) IN range_tab THEN `Yes!` 
                                               ELSE `No!` ) ).
```

## Executable Examples

- [Comparison with Ranges Table](abenlogexp_in_ranges_abexa.md)
