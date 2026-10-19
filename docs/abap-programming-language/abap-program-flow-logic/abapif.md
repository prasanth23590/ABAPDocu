---
title: "IF"
source_file: abapif.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Control Structures > Branches"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# IF

## Syntax

``` abap
IF log_exp1.   
  [statement_block1]   
[ELSEIF log_exp2.   
  [statement_block2]]   
...   
[ELSE.   
  [statement_blockn]]   
ENDIF.  
```

[`log_exp1`](abenlogexp.md) · [`log_exp2`](abenlogexp.md)

## Description

These statements define a control structure that can contain multiple statement blocks `statement_block` of which a maximum of one is executed, depending on the logical expressions [`log_exp`](abenlogexp.md).

After `IF` and `ELSEIF` any logical expressions [`log_exp`](abenlogexp.md) can be listed, while the expressions `statement_block` stand for any statement blocks.

The logical expressions, beginning with the `IF` statement, are checked from top to bottom and the statement block after the first real logical expression is executed. If none of the logical expressions are true, the statement block after the `ELSE` statement is executed.

If the end of the executed statement block is reached or if no statement block is to be executed, the processing is continued after `ENDIF`.

## Hint

The [conditional operator](../../abap-glossary/abenconditional_operator_glosry.md) [`COND`](abenconditional_expression_cond.md) can also be used to implement branches in operand positions that are based on logical expressions.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Transformation of a time to the 12-hour format (see also [Country-Specific Formats](../abap-language-environment/abencountry_formats.md)).

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(time) = cl_demo_date_time=>get_user_time( ). 
 
IF time < '120000'. 
  out->write( 
    |{ time TIME = ISO } AM| ). 
ELSEIF time > '120000' AND 
       time < '240000'. 
  out->write( 
    |{ CONV t( time - 12 * 3600 ) TIME = ISO } PM| ). 
ELSE. 
  out->write( 
    |High Noon| ). 
ENDIF. 
 
out->display( ).
```

See also the example for [`COND`](abenconditional_expression_cond.md).
