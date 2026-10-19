---
title: "Literal Operator"
source_file: abenliteral_operator.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects > Literals"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Literal Operator

## Syntax

``` abap
... { '...' & '...' [& '...' [...] ] }   
  | { `...` & `...` [& `...` [...] ] } ...  
```

## Description

The literal operator `&` can be used to combine two [character literals](abenuntyped_character_literals.md) of the same type into a single character literal. The two categories of literals cannot be mixed. As a result, the definition of one literal can span multiple program lines. The content of the resulting literal must match its type and its length must not exceed the associated maximum length.

The literal operator can normally be specified to combine literals in all [read positions](../../abap-glossary/abenread_position_glosry.md). Exceptions to this are literals [specified dynamically in parentheses](../abap-operands/abenoperands_specifying.md), literals in parenthesized lists separated by commas (here the only relevant operand position is [`WHERE IN`](../abap-database-access/abenwhere_logexp_operand_in.md)).

## Hints

- The literal operator cannot be used for [numeric literals](abenuntyped_character_literals.md).

- Apart from character literals, the literal operator can also be used to combine [string templates](../../abap-glossary/abenstring_template_glosry.md).

- Any trailing blanks in text field literals are respected by the literal operator.

- When used for literals, the literal operator `&` must not be confused with the [concatenation operator `&&`](../abap-processing-internal-data/abenstring_operators.md) that can be used in [string expressions](../../abap-glossary/abenstring_expression_glosry.md) to concatenate character-like operators. While literals are combined using the literal operator once when a program is compiled, the concatenation operator executes a real operation at runtime and concatenates any number of character-like operands. The trailing blanks of operands with fixed lengths, particularly text field literals, are ignored.

- Character literals combined using the literal operator `&` are subject to the upper limit of 255 characters. Longer character strings can only be concatenated at runtime, for example using the [concatenation operator `&&`](../abap-processing-internal-data/abenstring_operators.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Construction of an HTML string from literals.

``` abap
DATA html TYPE string. 
 
html = 
  `<html>`   & 
  `<body>`   & 
  `Text`     & 
  `</body>`  & 
  `</html>`. 
 
cl_abap_browser=>show_html( html_string = html ).
```
