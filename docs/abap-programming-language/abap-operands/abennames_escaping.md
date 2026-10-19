---
title: "!, Escape Character for Operands"
source_file: abennames_escaping.html
section: "ABAP Programming Language > ABAP - Operands > Data Objects in Operand Positions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# !, Escape Character for Operands

## Syntax

``` abap
... !operand ...  
```

## Description

The character `!` can be written directly before a name `operand` of a single operand in order to distinguish it from an [ABAP word](../../abap-glossary/abenabap_word_glosry.md) with the same notation in a statement. The escape character `!` can be placed in front of a [chaining](abencomponent_chaining_selector.md), but it cannot be used in front of components that are addressed by a [component selector](../../abap-glossary/abencomponent_selector_glosry.md).

With the exception of the first word of a statement that is introduced by a keyword, each word of a statement that is preceded by the escape character is interpreted as an operand, and not as an ABAP word during program generation. The escape character itself is not part of a name and is ignored when the statement is executed.

## Hints

- The escape character `!` may be required on rare occasions in which the compiler cannot tell the difference between an operand and a [reserved word](../../abap-glossary/abenabap_word_glosry.md) of the same name. Otherwise, it can be used for the documentation of operands in the source code.

- The escape character `!` must not be used in front of [operators](../../abap-glossary/abenoperator_glosry.md). For example, `!=` cannot be specified instead of `=`.
