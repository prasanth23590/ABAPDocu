---
title: "CASE"
source_file: abapcase.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Control Structures > Branches"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CASE

## Syntax

``` abap
CASE operand.   
  [WHEN operand1 [OR operand2 [OR operand3 [...]]].   
    [statement_block1]]   
  ...   
  [WHEN OTHERS.   
    [statement_blockn]]   
ENDCASE.  
```

## Description

Simple case distinction. These statements define a control structure that can contain multiple statement blocks `statement_block1`, ..., `statement_blockn`, of which a maximum of one is executed depending on the value of the operand `operand`.

Starting with the first `WHEN` statement, the system checks from top to bottom whether the content of the operand in `operand` matches the content of one of the operands `operand1`, `operand2`, .... The statement block is executed after the first match. If no matches are found, the statement block is executed after the statement `WHEN OTHERS`.

- The operand `operand` after `CASE` is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md).

- The operands `operand1`, `operand2`, ... after `WHEN` are extended functional operand positions in which, however, [table expressions](../../abap-glossary/abentable_expression_glosry.md) cannot be specified. This property of operand positions is obsolete and should no longer be used.

If the end of the executed statement block is reached or no statement block is executed, processing continues after `ENDCASE`.

The content is compared as illustrated in the following logical expression:

``` abap
`operand = operand1 [OR operand = operand2 
                   [OR operand = operand3 [...]]]`
```

The [comparison rules](abenlogexp_rules_operands.md) for comparisons between any operands apply to this comparison, depending on the data types of the operands involved.

## Hints

- For `operand`, the current value is used in every comparison. This may differ from the starting value if `operand` is a variable that is changed in a [functional method](../../abap-glossary/abenfunctional_method_glosry.md) specified after a `WHEN` statement.

- A `CASE` control structure is somewhat faster than a semantically equivalent `IF` control structure.

- Functional methods and certain built-in functions can be specified after `WHEN`, however this should be avoided. Constant values, for example, should be specified in the operand positions after `WHEN`.

- A special control structure introduced using [`CASE TYPE OF`](abapcase_type.md) makes it possible for the type of object reference variables to be checked.

- The [conditional operator](../../abap-glossary/abenconditional_operator_glosry.md) [`SWITCH`](abenconditional_expression_switch.md) can also be used to make case distinctions in operand positions.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Branching of the program flow depending on the time of the day.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA time_of_day TYPE string. 
 
cl_demo_input=>add_field( CHANGING field = time_of_day ). 
cl_demo_input=>request( ). 
 
CASE time_of_day. 
  WHEN `morning`. 
    out->write( `Good morning!` ). 
  WHEN `night`. 
    out->write( `Good night!` ). 
  WHEN OTHERS. 
    out->write( `Hello.` ). 
ENDCASE. 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates that the calculation type of an arithmetic expression after `CASE` is determined only by its operands. The calculation type after the first `CASE` statement is `i` and the result of the calculation is 0. The comparison with the value 0 after `WHEN` is true regardless of its data type. The calculation type of the comparison after `IF` is `decfloat34`, however, and the result is false. To force a specific calculation type after `CASE`, an additional operand can be added as shown in the second `CASE` statement. This operand does not contribute to the calculation.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: 
  inum1 TYPE i VALUE 1, 
  inum2 TYPE i VALUE 3, 
  decf  TYPE decfloat34 VALUE 0. 
 
CASE  inum1 / inum2. 
  WHEN decf. 
    out->write_text( 'In CASE equal' ). 
ENDCASE. 
 
IF decf <> inum1 / inum2. 
  out->write_text( 'In IF not equal' ). 
ENDIF. 
 
CASE CONV decfloat34( inum1 / inum2 ). 
  WHEN decf. 
    out->write_text( 'In CASE equal' ). 
  WHEN OTHERS. 
    out->write_text( 'In CASE not equal' ). 
ENDCASE. 
 
out->display( ).
```
