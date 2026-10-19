---
title: "WAIT UP TO"
source_file: abapwait_up_to.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Program Interruption"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# WAIT UP TO

## Syntax

``` abap
WAIT UP TO sec SECONDS.  
```

## Description

This statement interrupts the execution of the program by the number of seconds specified in `sec`. `sec` is a [numeric expression position](../../abap-glossary/abennumerical_expr_position_glosry.md) of the operand type `f` to which positive numbers can be passed, including 0. The unit of the number specified in `sec` is seconds and the time resolution is one millisecond. After the specified time has passed, the program execution continues with the statement following `WAIT`. When used, this statement always changes the [work process](../../abap-glossary/abenwork_process_glosry.md).

## System Fields

This statement always sets `sy-subrc` to 0.

## Hints

- Each time this variant of the statement `WAIT` is used, a [database commit](../../abap-glossary/abendatabase_commit_glosry.md) is triggered. For this reason, `WAIT` must not be used between [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statements that open or close a [database cursor](../../abap-glossary/abendatabase_cursor_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The output of the following example should correspond to approximately one million microseconds.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(timer)  = cl_abap_runtime=>create_hr_timer( ). 
 
FINAL(t1) = timer->get_runtime( ). 
 
WAIT UP TO 1 SECONDS. 
 
FINAL(t2) = timer->get_runtime( ). 
 
out->write( |{ t2 - t1  STYLE = SCIENTIFIC }| ). 
 
out->display( ).
```
