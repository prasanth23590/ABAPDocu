---
title: "rel_exp - Comparison Operators for Character-Like Data Types"
source_file: abenlogexp_strings.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Operators"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparison Operators for Character-Like Data Types

The following table shows the comparison operators for comparisons between character-like operands (single data objects and return values or [string expressions](../../abap-glossary/abenstring_expression_glosry.md)) in [comparison expressions](../../abap-glossary/abencomparison_expression_glosry.md). Trailing blanks are respected for operands of type `string`. Unless documented differently in the following table, trailing blanks are not respected for operands of types `c`, `d`, `n`, and `t`.

| **operator** | **Meaning**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CO`         | Contains Only: True if `operand1` only contains characters from `operand2`. Uppercase and lowercase characters and trailing blanks are respected for both operands. If `operand2` is of type `string` and initial, the comparison expression is false, unless `operand1` is also of type `string` and initial, in which case the comparison expression is always true, regardless of `operand2`. If the comparison is false, `sy-fdpos` contains the offset of the first character in `operand1` that is not contained in `operand2`. If the comparison is true, `sy-fdpos` contains the length of `operand1`.                                                                                                                                                                                                                                                                                                                                                               |
| `CN`         | Contains Not Only: True, if a comparison expression with `CO` is false, that is if `operand1` contains not only characters from `operand2`. `sy-fdpos` is set in the same way as for `CO`. If the comparison is true, `sy-fdpos` contains the offset of the first character in `operand1` that is not contained in `operand2`. If the comparison is false, `sy-fdpos` contains the length of `operand1`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `CA`         | Contains Any: True, if `operand1` contains at least one character from `operand2`. Uppercase and lowercase characters and trailing blanks are respected for both operands. If `operand1` or `operand2` is of type `string` and initial, the comparison expression is always false. If the comparison is true, `sy-fdpos` contains the offset of the first character in `operand1` that is also contained in `operand2`. If the comparison is false, `sy-fdpos` contains the length of `operand1`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `NA`         | Contains Not Any: True, if a comparison expression with `CA` is false, that is, `operand1` does not contain any characters from `operand2`. If the comparison is false, `sy-fdpos` contains the offset of the first character in `operand1` that is also contained in `operand2`. If the comparison is true, `sy-fdpos` contains the length of `operand1`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `CS`         | Contains String: True, if the content of `operand2` is contained in `operand1`. Trailing blanks in the left operand are respected. If `operand1` is of type `string` and initial, or of type `c` and contains only blank characters, the comparison expression is false, unless `operand2` is also of type `string` and initial, or of type `c` and only contains blank characters, in which case, the comparison expression is always true. If the comparison is true, `sy-fdpos` contains the offset of `operand2` in `operand1`. If the comparison is false, `sy-fdpos` contains the length of `operand1`.                                                                                                                                                                                                                                                                                                                                                                |
| `NS`         | Contains No String: True, if a comparison expression with `CS` is false, that is if `operand1` does not contain the content of `operand2`. If the comparison is false, `sy-fdpos` contains the offset of `operand2` in `operand1`. If the comparison is true, `sy-fdpos` contains the length of `operand1`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `CP`         | Conforms to Pattern: True, if the content of `operand1` matches the pattern in `operand2`. Wildcard characters can be used to form the `operand2` pattern, where *\** represents any character string, including an empty string, and *+* represents any character. It is not case-sensitive. Trailing blanks in the left operand are respected. If the comparison is true, `sy-fdpos` contains the offset of `operand2` in `operand1`, whereby leading wildcard characters *\** in `operand2` are ignored if `operand2` also contains other characters. If the comparison is false, `sy-fdpos` contains the length of `operand1`. Characters in `operand2` can be marked for direct comparisons by prefixing them with the [escape character](../../abap-glossary/abenescape_character_glosry.md) *\#*. For such characters in `operand2`, the operator is case-sensitive, wildcard characters and the escape character are not subject to special handling and trailing blanks are relevant. |
| `NP`         | Does Not Conform to Pattern: True, if a comparison expression with `CP` is false, that is, `operand1` does not fit the pattern in `operand2`. If the comparison is false, `sy-fdpos` contains the offset of `operand2` in `operand1`, whereby leading wildcard characters *\** in `operand2` are ignored if `operand2` also contains other characters. If the comparison is true, `sy-fdpos` contains the length of `operand1`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## Hints

- For the operators `CP` and `NP`, multiple wildcard characters *\** one after another have the same effect as the specification of a single wildcard *\** character. The wildcard character *+* does not represent an empty string.

- When using the operators `CP` and `NP`, patterns without wildcard characters in `operand2` are generally not useful. Instead, a comparison with [`=`](abenlogexp_any_operand.md) can be performed. In order to achieve case-insensitivity for comparisons with `=`, it is recommended using either [`to_upper`](../abap-processing-internal-data/abencase_functions.md) or [`to_lower`](../abap-processing-internal-data/abencase_functions.md) for both operands.

- Operands of byte-like data types cannot be compared using the comparison operators from this table. To perform corresponding comparisons for byte-like operands, [comparison operators for byte-like data types](abenlogexp_bytes.md) can be used.

- Instead of the comparison operators in this table [predicate functions](abenchar_comp_op_vs_funct.md) can also be used.

- The statement [`FIND`](../abap-processing-internal-data/abapfind.md) and the search functions [`find`](../abap-processing-internal-data/abensearch_functions.md) can be quicker than the comparison operator `CS` by some magnitude.

- When using comparison operators for character-like data types in a [conditional expression](../../abap-glossary/abenconditional_expression_glosry.md) or in a [Boolean function](../../abap-glossary/abenboole_function_glosry.md), the system field `sy-fdpos` has the value set in the expression once the expression is processed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Search for HTML tags in a text using the operator `CP`. This search finds the first HTML tag * at offset 8. It should be noted that it is not sufficient to specify a search pattern *\<\*\>*, since `CP` stands for Conforms to Pattern and not for Contains Pattern. The example also shows that the leading wildcard characters *\** of the pattern are ignored in `sy-fdpos`, to determine the occurrence found by this search.*

``` abap
DATA html TYPE string. 
 
html = `This is <i>italic</i>!`. 
 
IF html CP '*<*>*'. 
  cl_demo_output=>display_text( |Found HTML tag at { sy-fdpos }| ). 
ENDIF.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Display of the first position of a letter in a field. The operator `CS` is used in the conditional operator [`COND`](abenconditional_expression_cond.md), which returns the content of the system field `sy-fdpos`.

``` abap
FINAL(abcde) = `abcdefghijlmnopqrstuvwxyz`. 
cl_demo_output=>display( COND #( WHEN abcde CS 'H' THEN sy-fdpos ) ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following comparison is always true, regardless of the input.

``` abap
DATA(text) = `abcd1234`. 
cl_demo_input=>request( CHANGING field = text ). 
 
IF `` CO text. 
  cl_demo_output=>display( 'true' ). 
ENDIF.
```

### Executable Example

[Comparison Operators for Character-Like Data Types](abencharacter_comparisons_abexa.md)
