---
title: "DATA, Inline Declaration for Variables"
source_file: abendata_inline.html
section: "ABAP Programming Language > ABAP - Declarations > Inline Declarations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DATA, Inline Declaration for Variables

## Syntax

``` abap
... DATA(var) ...  
```

## Description

A declaration expression with the declaration operator `DATA` declares a [variable](../../abap-glossary/abenvariable_glosry.md) `var` that is used as an operand in the current [write position](../../abap-glossary/abenwrite_position_glosry.md). The declared variable is visible statically in the program as of `DATA(var)` and is valid in the current [context](../../abap-glossary/abenobj_context_glosry.md). The declaration is made when the program is compiled, regardless of whether the statement is actually executed.

The declaration operator `DATA` can be specified in any designated [declaration position](../abap-syntax-elements-of-an-abap-program/abendeclaration_positions.md). The date type of the variable is determined by the [operand type](../../abap-glossary/abenoperand_type_glosry.md). It must be possible to derive this type completely statically.

A variable `var` declared inline cannot be used in a read position of the same statement.

If a data object called `data` already exists in the current context, `DATA(var)` is interpreted as a [substring access](../abap-operands/abenoffset_length.md) and not as an inline declaration. A syntax warning indicates this. `DATA(var)` only works as an inline declaration if there is no data object called `data` yet.

## Hints

- A valid statement with an inline declaration of a variable can generally be interpreted as a short form for a declaration statement used as a direct prefix.

  `DATA var TYPE ...`

  `... var ...` Deviations from this rule occur only if an identically named data object of a more global context is used in the same statement. This is still valid in the statement and is only hidden after the statement.

- Just like the statement `DATA`, an inline declaration does not open a local context for the current statement block. An inline declaration for a variable can only be made once within a context and the variable must not have been declared there using `DATA`.

- An inline declaration can never occur on the right-hand side of an assignment or within an expression.

- The operand position and the types of other operands can be included in the static derivation of the operand type. If the type of a different operand cannot be identified statically, for example because it is specified as a generically typed field symbol, either a suitable [standard type](../../abap-glossary/abenstandard_type_glosry.md) is used or no inline declaration is possible.

- If the operand type is defined by reference to a data type of the ABAP Dictionary, it is inherited with its semantic properties, such as field help, input help, or conversion exits.

- If multiple equally valid operand types are possible in a [declaration position](../abap-syntax-elements-of-an-abap-program/abendeclaration_positions.md), the recommended preferred data type is generally used.

- If no other write accesses to the variable `var` should take place in the current context, it is preferable to use the declaration operator [`FINAL`](abenfinal_inline.md) to declare an immutable variable instead of `DATA`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Inline declaration of an internal table as the target field of an assignment and inline declaration of an appropriate work area in a `LOOP`. Since there are other write accesses to the variables, inline declarations with [`FINAL`](abenfinal_inline.md) are not possible here.

``` abap
TYPES t_itab TYPE TABLE OF i 
             WITH NON-UNIQUE KEY table_line. 
 
DATA(itab) = VALUE t_itab( ( 1 ) ( 2 ) ( 3 ) ). 
... 
APPEND 4 TO itab. 
... 
LOOP AT itab INTO DATA(wa). 
  ... 
  wa = 0. 
  ... 
ENDLOOP.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

If a data object called `data` does not exist in the current context, the first statement is an inline declaration and the second statement executes a substring access.

``` abap
DATA(data) = '1'. 
DATA(data) = '2'.
```
