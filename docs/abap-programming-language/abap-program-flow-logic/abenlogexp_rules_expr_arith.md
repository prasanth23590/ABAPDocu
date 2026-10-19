---
title: "rel_exp - Comparison Type of Arithmetic Expressions"
source_file: abenlogexp_rules_expr_arith.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Rules > rel_exp - Comparing Elementary Data Types > rel_exp - Comparison Type of Calculation Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparison Type of Arithmetic Expressions

[Arithmetic expressions](../../abap-glossary/abenarithmetic_expression_glosry.md) are possible as operands of comparison expressions using [comparison operators for all data types](abenlogexp_compare_all.md). It is possible to compare an [arithmetic expression](../abap-processing-internal-data/abapcompute_arith.md) with a single operand of a [numeric data type](../../abap-glossary/abennumeric_data_type_glosry.md) or with another arithmetic expression.

The [calculation type](../../abap-glossary/abencalculation_type_glosry.md) of all arithmetic expressions of a comparison expression is determined from all single operands of the entire comparison expression as well as by any operators `**` in accordance with the [usual rules](../abap-processing-internal-data/abenarith_type.md). The result of the involved arithmetic expressions involved exists in the calculation type. This calculation type is also the [comparison type](../../abap-glossary/abencomparison_type_glosry.md) whose [comparison rules](abencomparison_type.md) are used to perform the comparison. If necessary, single operands are [converted](../abap-processing-internal-data/abennumeric_source_fields.md) to the comparison type before comparison.

If multiple relational expressions are combined into a logical expression using [Boolean operators](abenlogexp_boole.md), the calculation type or comparison type are determined separately for each relational expression.

## Hints

- If a conversion error occurs in an arithmetic expression in a relational expression, the associated exception can be handled differently than in direct [comparisons of data objects](abenlogexp_rules_operands_dobj.md).

- To compare an arithmetic expression with a single non-numeric operand, the operand can be prefixed with the `+` sign to turn it into an arithmetic expression.

- An arithmetic expression cannot be specified as the operand of a [predicate expression](../../abap-glossary/abenpredicate_expression_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following comparisons are both true. In the first one, the calculation type is `i` and the result of the calculation is rounded to 1. In the second, the calculation type is `decfloat34` and there is no rounding.

``` abap
IF 4 / 3 = 1. 
  cl_demo_output=>write( '4 / 3 = 1' ). 
ENDIF. 
 
IF 4 / 3 > CONV decfloat34( 1 ). 
  cl_demo_output=>write( '4 / 3 > CONV decfloat34( 1 )' ). 
ENDIF. 
 
cl_demo_output=>display( ).
```
