---
title: "Character-Like Expression Positions"
source_file: abenstring_expression_positions.html
section: "ABAP Programming Language > ABAP - Syntax Elements of an ABAP Program > ABAP Statements > Operand Positions > Expression Positions for Expressions > Read Positions for Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Character-Like Expression Positions

Character-like expression positions are [read positions](../../abap-glossary/abenread_position_glosry.md) where [character-like data objects](../../abap-glossary/abencharlike_data_object_glosry.md), [constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md), [string expressions](../../abap-glossary/abenstring_expression_glosry.md), [table expressions](../../abap-glossary/abentable_expression_glosry.md), and [built-in functions](../../abap-glossary/abenbuiltin_function_glosry.md) can be specified, as well as [functional method calls](../../abap-glossary/abenfunctional_method_call_glosry.md) and [method chainings](../../abap-glossary/abenmethod_chaining_glosry.md) whose return value has a [character-like data type](../../abap-glossary/abencharlike_data_type_glosry.md). The following character-like expression positions exist:

- Operand positions in [string expressions](../abap-processing-internal-data/abapcompute_string.md)

- Character-like arguments in [processing functions](../abap-processing-internal-data/abenprocess_functions.md)

- Character-like arguments in [description functions](../abap-processing-internal-data/abendescriptive_functions.md)

- Operand `comp` of the statement

  [`ASSIGN COMPONENT comp OF STRUCTURE`](../abap-processing-internal-data/abapassign_dynamic_components.md)

- Regular expression `regex` in the statements

  [`FIND ... PCRE|REGEX regex ... IN ...`](../abap-processing-internal-data/abapfind_pattern.md)

  [`REPLACE ... PCRE|REGEX regex ... IN ...`](../abap-processing-internal-data/abapreplace_pattern.md)

- Search pattern `substring` in the statements

  [`FIND ... SUBSTRING substring ... IN ...`](../abap-processing-internal-data/abapfind_pattern.md)

  [`REPLACE ... SUBSTRING substring ... IN ...`](../abap-processing-internal-data/abapreplace_pattern.md)

- Operand `dobj` in the statement

  [`FIND ... IN dobj ...`](../abap-processing-internal-data/abapfind.md)

- Operand `new` in the statement

  [`REPLACE ... WITH new ...`](../abap-processing-internal-data/abapreplace.md)

  [`REPLACE ... IN TABLE ... WITH new ...`](../abap-processing-internal-data/abapreplace_itab.md)

- Operand `substring` in the statement

  [`SHIFT ... UP TO substring`](../abap-processing-internal-data/abapshift_places.md)

- Operand `mask` in the statement

  [`SHIFT ... DELETING ... mask`](../abap-processing-internal-data/abapshift_deleting.md)

- Operands `dobj` and `sep` in the statement

  [`SPLIT dobj AT sep INTO ...`](../abap-processing-internal-data/abapsplit.md)

- Operand `text` in the statement

  [`CONVERT text INTO SORTABLE CODE ...`](../abap-processing-internal-data/abapconvert_text.md)

- Operands `text2` and `text2` in the statement

  [`OVERLAY ... WITH text2 USING mask`](../abap-processing-internal-data/abapoverlay.md)

- Operand `mask` in the statement

  [`TRANSLATE ... USING mask`](../abap-processing-internal-data/abaptranslate.md)

- Operand `sub` in the statement

  [`ASSERT ... SUBKEY sub ...`](../abap-program-maintenance/abapassert.md) `LOG-POINT ... SUBKEY sub ...`

- Operands `text` and `dobj1` to `dobj4` in the statements

  `MESSAGE text ...`

  MESSAGE ... [`WITH dobj1 ... dobj4`](../abap-text-repositories/abapmessage.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of a string expression `` `(` && sub && `)+` `` to form a regular expression in the statement [`FIND`](../abap-processing-internal-data/abapfind.md) to make it possible to find groups of a substring `sub`.

``` abap
DATA: text TYPE string, 
      sub  TYPE string. 
 
FIND PCRE `(` && sub && `)+` IN text.
```
