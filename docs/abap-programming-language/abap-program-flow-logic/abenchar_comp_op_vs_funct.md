---
title: "rel_exp - Comparison Operators vs. Predicate Functions"
source_file: abenchar_comp_op_vs_funct.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Operators > rel_exp - Comparison Operators for Character-Like Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparison Operators vs. Predicate Functions

Instead of the [comparison operators for character-like data types](abenlogexp_strings.md), [predicate functions](abenpredicate_functions_strgs.md) can be used as shown in the following table:

| **Comparison Operator** | **Predicate Function**                                      |
|-------------------------|-------------------------------------------------------------|
| `o1 CO o2`              | `NOT contains_any_not_of( val = o1 sub = o2 )`              |
| `o1 CN o2`              | `contains_any_not_of( val = o1 sub = o2 )`                  |
| `o1 CA o2`              | `contains_any_of( val = o1 sub = o2 )`                      |
| `o1 NA o2`              | `NOT contains_any_of( val = o1 sub = o2 )`                  |
| `o1 CS o2`              | `contains( val = to_upper( o1 ) sub = to_upper( o2 ) )`     |
| `o1 NS o2`              | `NOT contains( val = to_upper( o1 ) sub = to_upper( o2 ) )` |

Since the comparison operators `CS` and `NS` are not case-sensitive, the arguments must be processed by the functions [`to_upper`](../abap-processing-internal-data/abencase_functions.md) (or `to_lower`). It should also be noted that the trailing blanks of character-like arguments of fixed length are always ignored in the predicate functions, whereas there are exceptions to this rule for operands of comparison operators.

The operators `CP` and `NP` can also be replaced by the predicate function `contains` or `matches` and a suitable [regular expression](../../abap-glossary/abenregular_expression_glosry.md). The differences in case handling must also be respected, whereby a simple mapping like in `CS` and `NS` is not possible, but usually not required.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following two relational expressions yield the same result.

``` abap
FINAL(text) = `xxxxaaayyyy`. 
 
ASSERT text CP `*aaa*` AND 
       matches( val = text pcre = `.*aaa.*` case = ' ' ).
```
