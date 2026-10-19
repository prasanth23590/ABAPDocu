---
title: "rel_exp - Comparison Type of String Expressions"
source_file: abenlogexp_rules_expr_char.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Rules > rel_exp - Comparing Elementary Data Types > rel_exp - Comparison Type of Calculation Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparison Type of String Expressions

[String expressions](../../abap-glossary/abenstring_expression_glosry.md) can be used as operands of comparison expressions with the following operators:

- [Comparison operators for all data types](abenlogexp_compare_all.md)

- [Comparison operators for character-like data types](abenlogexp_strings.md)

It is possible to compare a [string expression](../../abap-glossary/abenstring_expression_glosry.md) with a single operand of any [elementary data type](../../abap-glossary/abenelementary_data_type_glosry.md) or with another string expression. With regard to the conversion of the expression by string, two cases can be distinguished:

- If a string expression is compared with an individual operand in a generic logical expression, the comparison type is `string`. The individual operand is implicitly regarded as an [embedded expression](../../abap-glossary/abenembedded_expression_glosry.md) of a [string template](../../abap-glossary/abenstring_template_glosry.md) and formatted as a text string before the comparison in accordance with the associated [predefined format](../abap-processing-internal-data/abenstring_templates_predef_format.md).

- If a string expression on the right side of a `WHERE` condition is used in a [processing statement for internal tables](../abap-processing-internal-data/abentable_processing_statements.md), the comparison type results from the [combination](abenlogexp_character.md) of `string` with the type on the left side. Both sides are [converted](../abap-processing-internal-data/abenconversion_elementary.md) to the comparison type as required.

## Hints

- A string expression cannot be specified as the operand of a [predicate expression](../../abap-glossary/abenpredicate_expression_glosry.md).

- The result of the formatting of an individual operand differs from the result of a simple [conversion](../abap-processing-internal-data/abenconversion_elementary.md) for some data types. An example is the type `decfloat34`.

- The results of general logical expressions and logical expressions in `WHERE` conditions for internal tables may differ for comparisons with string expressions, since both the formatting and the comparison type play a role.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the effect of different comparison types. The first comparison is true, since the character-like operand is converted to the type of the numeric operand in accordance with the rule for [comparing character-like data types](abenlogexp_character.md) and the numeric value is compared. However, the second comparison is also true, since the numeric operand is formatted as a text string and the internal representation of the code page used is compared.

``` abap
ASSERT `02` > 1. 
ASSERT |02| < 1.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the effect of different formatting and different rules. All comparisons are true. An operand of type `decfloat34` is compared with a text string and a string expression. For the comparison with the text string, the left side is also converted to the type `string` and the values of both sides are the same. For the comparison with the chain, the left-hand side is [formatted](../abap-processing-internal-data/abenstring_templates_predef_format.md) differently and the values of both sides are different. The third comparison shows explicitly how the operand is handled during the comparison with the chain. In contrast, the `WHERE` conditions [`LOOP`](../abap-processing-internal-data/abaploop_at_itab.md) statements convert both sides to the numeric [comparison type](abenlogexp_character.md) `decfloat34`. The output shows the difference between simple conversion and formatting as an embedded expression.

``` abap
DATA decf TYPE decfloat34 VALUE '0.00000004'. 
DATA itab LIKE TABLE OF decf. 
APPEND decf TO itab. 
 
ASSERT decf       =  CONV string( decf ). 
ASSERT decf       <> CONV string( decf ) && ``. 
ASSERT |{ decf }| <> CONV string( decf ) && ``. 
 
LOOP AT itab TRANSPORTING NO FIELDS 
             WHERE table_line = CONV string( decf ). 
ENDLOOP. 
ASSERT sy-subrc = 0. 
 
LOOP AT itab TRANSPORTING NO FIELDS 
             WHERE table_line = CONV string( decf ) && ``. 
ENDLOOP. 
ASSERT sy-subrc = 0. 
 
cl_demo_output=>display( 
  |CONV string( decf ):\t{ CONV string( decf ) }\n| && 
  |{ `|{ decf }|` }:\t\t{ decf }| ).
```
