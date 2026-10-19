---
title: "DO"
source_file: abapdo.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Control Structures > Loops"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DO

## Syntax

``` abap
DO [n TIMES]. 
  [statement_block] 
ENDDO.  
```

### Addition

[`... n TIMES`](abapdo.md#addition)

## Overview

### Description

Unconditional loop. The statements `DO` and `ENDDO` define a control structure, which can contain a complete [statement block](../../abap-glossary/abenstatement_block_glosry.md) `statement_block`.

Without the addition [`n TIMES`](abapdo.md), the statement block is repeated until it is exited using one of the following statements:

- [`EXIT`](../abap-calling-and-exiting-program-units/abapexit_loop.md) that exits a complete loop and resumes the program behind the closing statement of the loop.

- A statement for [exiting the current processing block](../abap-calling-and-exiting-program-units/abenleave_processing_blocks.md)

In order to exit the current loop pass and to continue with the next loop pass, the statements [`CONTINUE`](../abap-calling-and-exiting-program-units/abapcontinue.md) and [`CHECK`](../abap-calling-and-exiting-program-units/abapcheck_processing_blocks.md) can be used.

Within the statement block, the system field `sy-index` contains the number of previous loop passes, including the current pass. In nested loops, `sy-index` always refers to the current loop.

### Hints

- If `DO` loops are used to construct values or fill internal tables, they can usually be expressed more elegantly using conditional iterations with [`FOR`](abenfor_conditional.md) in constructor expressions.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Exit a `DO` loop based on a condition.

``` abap
DATA(str) = `xxx`. 
DO. 
  str = str && str. 
  IF strlen( str ) > 10000. 
    EXIT. 
  ENDIF. 
ENDDO.
```

## Addition

`... n TIMES`

### Description

The addition `n TIMES` limits the number of loop passes in a `DO` loop. `n` is a [numeric expression position](../../abap-glossary/abennumerical_expr_position_glosry.md) of operand type `i`.

The numeric value of `n` when entering the loop determines the maximum number of times the statement block is executed. The control structure ignores changes to the value `n` within the loop. If `n` contains a value less than or equal to 0, the statement block is not executed.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Calculation and display of the first ten square numbers in a `DO` loop.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA square TYPE i. 
 
DO 10 TIMES. 
  square = ipow( base = sy-index exp = 2 ). 
  out->write( |{ sy-index } { square }| ). 
ENDDO. 
 
out->display( ).
```
