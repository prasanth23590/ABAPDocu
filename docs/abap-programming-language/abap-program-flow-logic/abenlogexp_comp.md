---
title: "Comparison Expressions (rel_exp)"
source_file: abenlogexp_comp.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Comparison Expressions (rel_exp)

## Syntax

``` abap
... { operand1   {=|EQ|<>|NE|>|GT|<|LT|>=|GE|<=|LE} 
               | {CO|CN|CA|NA|CS|NS|CP|NP} 
               | {BYTE-CO|BYTE-CN|BYTE-CA|BYTE-NA|BYTE-CS|BYTE-NS} 
               | {O|Z|M} operand2 } 
  | { operand [NOT] BETWEEN operand1 AND operand2 } 
  | { operand [NOT] IN range_tab }  ...  
```

[`{=|EQ|<>|NE|>|GT|<|LT|>=|GE|<=|LE}`](abenlogexp_any_operand.md) · [`{CO|CN|CA|NA|CS|NS|CP|NP}`](abenlogexp_strings.md) · [`{BYTE-CO|BYTE-CN|BYTE-CA|BYTE-NA|BYTE-CS|BYTE-NS}`](abenlogexp_bytes.md) · [`{O|Z|M}`](abenlogexp_bitmasks.md) · [`operand [NOT] BETWEEN operand1 AND operand2`](abenlogexp_between.md) · [`operand [NOT] IN range_tab`](abenlogexp_select_option.md)

## Description

In [Comparison expressions](../../abap-glossary/abencomparison_expression_glosry.md), two or more operands are combined to a [relational expression](../../abap-glossary/abenrelational_expression_glosry.md) using a [comparison operator](../../abap-glossary/abencomp_operator_glosry.md). A [truth value](../../abap-glossary/abentruth_value_glosry.md) is determined as the result of the comparison.

- The operands are compared using one of the [comparison operators](abenlogexp_op.md) shown here.

- The comparisons take place according to [comparison rules](abenlogexp_rules.md).

`operand1`, `operand2`, and `operand` are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md), which means that the following can be specified:

- [Data objects](../../abap-glossary/abendata_object_glosry.md)

- [Built-in functions](../../abap-glossary/abenbuiltin_function_glosry.md)

- [Functional methods](../../abap-glossary/abenfunctional_method_glosry.md)

- [Calculation expressions](../../abap-glossary/abencalculation_expression_glosry.md)

- [Constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md)

- [Table expressions](../../abap-glossary/abentable_expression_glosry.md)

When a built-in function, a functional method, or a constructor expression is specified, its return value or result is used as an operand. When a calculation expression is specified, its result is used. A single operand can be compared with all single operands listed in the [comparison rules for single operands](abenlogexp_rules_operands.md). A calculation expression can be compared with all single operands or comparisons listed in the [comparison rules for calculation expressions](abenlogexp_rules_expressions.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Typical use of a logical expression, here a comparison of a built-in function with a literal, in an `IF` statement.

``` abap
DATA flag TYPE c LENGTH 1. 
 
... 
 
IF to_upper( flag ) = 'X'. 
  ... 
ENDIF.
```
