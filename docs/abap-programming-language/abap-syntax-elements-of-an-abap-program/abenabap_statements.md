---
title: "ABAP Statements"
source_file: abenabap_statements.html
section: "ABAP Programming Language > ABAP - Syntax Elements of an ABAP Program"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Statements

ABAP statements consist of the following [tokens](../../abap-glossary/abentoken_glosry.md) and always end with a period (`.`):

- [ABAP words](../../abap-glossary/abenabap_word_glosry.md)

  ABAP words are the vocabulary of the ABAP language. ABAP statements are composed of ABAP words, operands, and operators according to defined syntax rules. ABAP words are taken from the English language and are grouped into [ABAP language elements](../../abap-glossary/abenabap_language_element_glosry.md) and into [ABAP language element additions](../../abap-glossary/abenabap_language_elmnt_add_glosry.md) that express the semantics of a statement. In addition to letters, ABAP words can also contain hyphens (`-`) to form multiword expressions. In addition to the ABAP words, some [operators](../../abap-glossary/abenoperator_glosry.md) are also made up of letters. The first ABAP word of a statement is the [ABAP keyword](../../abap-glossary/abenabap_keyword_glosry.md). The remaining ABAP words are then additions to a keyword. A single ABAP word can be used both as a keyword and as a non-keyword. For example, `DATA` is used as a keyword as well as an addition to other keywords. Not all statements are introduced using a keyword or contain ABAP words. For example, assignments with the [assignment operator `=`](../abap-processing-internal-data/abenequals_operator.md) or [method calls](../abap-calling-and-exiting-program-units/abapcall_method_static_short.md) do not contain a keyword and do not necessarily contain another ABAP word. ABAP words are not reserved names as they are known in other programming languages. Although the use of an ABAP word for [user-defined identifiers](abennaming_conventions.md) is not forbidden, it should be avoided if possible. Even if this rule is followed, such a situation can occur if new language elements are introduced. Therefore, suitable naming conventions should be observed for user-defined identifiers to avoid conflicts with language elements.

- [Operands at Operand Positions](abenoperand_positions.md)

- [Operators](../abap-operands/abenoperators.md)

Specific ABAP words, operands, and operators can be combined to

- [expressions](../abap-operands/abenexpressions.md),

which can be specified at certain operand positions.

In [restricted ABAP language versions](../../abap-glossary/abenrestricted_version_glosry.md) not all language elements can be used. The topic Language Elements in ABAP Versions provides an overview of the ABAP language elements that are allowed in restricted language versions compared to [Standard ABAP](../../abap-glossary/abenstandard_abap_glosry.md).

A special syntax allows a set of statements to be written as

- [chained statements](abenchained_statements.md).

The tokens of a statement must be separated by at least one blank or a line break. Otherwise, blanks and line breaks between tokens are not significant. An ABAP statement is not limited to a line of the source code.

There is no case-sensitivity and in addition to ABAP words, operands, and operators, the following special characters can be used:

- If multiple similar expressions are combined into one expression with operators, the priority of the individual operations can be determined using parentheses (`()`).

- When calling functions and methods, parentheses (`()`) are used.

- Lists of operands are expressed by parentheses (`()`) and commas (`,`) in specific positions.

- When forming a [chained statement](../../abap-glossary/abenchained_statement_glosry.md), a colon (`:`) and commas (`,`) can be used.

There are single special characters such as parentheses for determining the priority in expressions that must be separated from other tokens by a blank character. Other special characters do not need to be separated by a blank, for example, the closing period.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

ABAP statement with the keyword `DELETE`, the addition `WHERE`, the operators `=`, `<`, `>`, `AND`, `OR`, the operands `itab`, `col1`, `op1`, `col2`, `op2`, `col3`, `op3`, and parentheses.

``` abap
DELETE itab 
  WHERE ( col1 = op1 AND ( col2 > op2 OR col3 < op3 ) ).
```
