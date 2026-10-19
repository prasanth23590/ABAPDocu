---
title: "RETURN"
source_file: abapreturn.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Exiting Program Units > Exiting Processing Blocks"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RETURN

## Syntax

``` abap
RETURN [expr].  
```

### Addition

[`... [expr]`](abapreturn.md#addition)

## Overview

### Description

This statement immediately terminates the current processing block. It can appear at any point in a [processing block](../../abap-glossary/abenprocessing_block_glosry.md) and terminates this block regardless of the statement block or control structure in which the statement appears.

After the processing block has been exited, the runtime framework behaves as when the [processing block is exited in a regular way](abenend_processing_blocks.md). In particular, the output parameters of procedures are passed on to the bound actual parameters.

### Hints

- The statement `RETURN` is generally intended for early but proper returns from processing blocks.

- Especially in [functional methods](../../abap-glossary/abenfunctional_method_glosry.md), the actual value of the [return value](../../abap-glossary/abenreturn_value_glosry.md) is passed to the caller.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Exit of the method `show_list` using `RETURN` if one of the formal parameters required (`structure` or `data_tab`) is initial.

``` abap
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    TYPES table_type TYPE STANDARD TABLE OF i. 
    METHODS show_list 
      IMPORTING structure TYPE c 
      CHANGING  data_tab  TYPE ANY TABLE. 
ENDCLASS. 
 
CLASS cls IMPLEMENTATION. 
  METHOD show_list. 
    DATA alv_list TYPE REF TO cl_gui_alv_grid. 
    IF structure IS INITIAL OR 
       data_tab  IS INITIAL. 
      RETURN. 
    ENDIF. 
    CREATE OBJECT alv_list 
      EXPORTING 
        i_parent = cl_gui_container=>screen0. 
    alv_list->set_table_for_first_display( 
      EXPORTING i_structure_name = structure 
      CHANGING  it_outtab        = data_tab ). 
  ENDMETHOD. 
ENDCLASS.
```

## Addition

`... [expr]`

### Description

In [functional methods](../../abap-glossary/abenfunctional_method_glosry.md), that is methods with one [return value](../../abap-glossary/abenreturn_value_glosry.md) `r`, a data object or an expression `expr` can be placed behind `RETURN` where `expr` is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md). The statement

`RETURN expr.`

acts as a short form of the statements:

``` abap
r = expr. 
RETURN.
```

That means:

- The result of the expression `expr` is passed as the return value `r` of the method to the caller.

- The result of the expression `expr` must be [convertible](../../abap-glossary/abenconvertible_glosry.md) to the return value `r` of the method.

- For `expr`, a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) with the specification `#` for the type can be used. Then the type is inferred from the return value `r`.

### Hints

- It is possible to write

  `RETURN r.` where `r` is the return value. In this case, the assignment `r = r` is skipped internally.

- If `RETURN` is the last statement in front of `ENDMETHOD`, it is skipped internally and `RETURN expr` works in the same way as `r = expr`.

- In any other context than a functional method, the `RETURN` statement has no addition.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A [conditional iteration](../abap-program-flow-logic/abenfor_conditional.md) with `FOR` is used behind `RETURN` to fill a tabular return value. In case of an error (overflow), the exception is caught and an empty table is constructed behind `RETURN`.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    TYPES: 
      BEGIN OF line, 
        num    TYPE i, 
        square TYPE i, 
      END OF line, 
      squares TYPE SORTED TABLE OF line WITH UNIQUE KEY num. 
    CLASS-METHODS main 
      IMPORTING limit    TYPE i 
      RETURNING VALUE(r) TYPE squares. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD main. 
    TRY. 
        RETURN VALUE #( FOR i = 1 UNTIL i > limit 
                ( num = i square = ipow( base = i exp = 2 ) ) ). 
      CATCH cx_sy_arithmetic_error. 
        RETURN VALUE #( ). 
    ENDTRY. 
  ENDMETHOD. 
ENDCLASS.
```
