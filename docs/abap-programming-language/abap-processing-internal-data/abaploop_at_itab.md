---
title: "LOOP AT itab, Basic Form"
source_file: abaploop_at_itab.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# LOOP AT itab, Basic Form

## Syntax

``` abap
LOOP AT itab result [cond].   
  ...   
ENDLOOP.  
```

[`result`](abaploop_at_itab_result.md) · [`cond`](abaploop_at_itab_cond.md) · [`ENDLOOP. `](abapendloop.md)

## Description

This variant of the statement [`LOOP AT itab`](abaploop_at_itab_variants.md) sequentially reads lines of the internal table `itab` and executes the statement block between `LOOP` and `ENDLOOP` once for each line. Either all lines are read or a subset specified by one or more conditions [`cond`](abaploop_at_itab_cond.md).

- The output behavior [`result`](abaploop_at_itab_result.md) determines how and to where the line content is read.

- The conditions [`cond`](abaploop_at_itab_cond.md) can consist of the following optional additions:

  - The table key with which the loop is executed can be determined with an addition [`USING KEY`](abaploop_at_itab_cond.md). The table key affects the order in which the lines are processed.

  - Using the additions [`FROM`](abaploop_at_itab_cond.md) and [`TO`](abaploop_at_itab_cond.md) for index tables and [`WHERE`](abaploop_at_itab_cond.md) for all table categories, the loop processing can be restricted to a subset of lines.

  - An addition [`STEP`](abaploop_at_itab_cond.md) allows a step size and the direction of the loop processing to be defined.

The order in which the lines are read can depend on:

- The [table category](../../abap-glossary/abentable_category_glosry.md)

- The addition [`USING KEY`](abaploop_at_itab_cond.md)

- The addition [`STEP`](abaploop_at_itab_cond.md)

If none of the additions is specified, the standard order depends on the table category as follows:

- **Standard tables and sorted tables**

  The lines are read by ascending line numbers in the [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md). In each loop pass, the system field `sy-tabix` contains the line number of the current line in the primary table index.

- **Hashed tables**

  The lines are processed in the order in which they were inserted into the table, and after a sort using the statement `SORT` in the sort order. In each loop pass, the system field `sy-tabix` contains the value 0.

The loop is executed until all the table lines of the table or the subset as specified in the [`cond`](abaploop_at_itab_cond.md) condition have been read or until it is exited with a [statement](../abap-calling-and-exiting-program-units/abenleave_program_units.md). If no corresponding lines are found or if the internal table is empty, the loop is not executed at all.

If the internal table is specified as the return value or result of a [functional method](../../abap-glossary/abenfunctional_method_glosry.md), a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md), or a [table expression](../../abap-glossary/abentable_expression_glosry.md), the value is persisted for the duration of the loop. Afterwards, the internal table can no longer be accessed.

**Caution**

[Special rules apply](abenitab_loop_change.md) when changing the internal table within a loop. In particular you should never perform write accesses on a complete table body.

## System Fields

This variant of the statement `LOOP AT` sets the value of the system field `sy-tabix`:

- In each loop pass for [index tables](../../abap-glossary/abenindex_table_glosry.md) and when using a [sorted key](../../abap-glossary/abensorted_key_glosry.md) on the line number of the current table line in the associated table index.

- In [hashed tables](../../abap-glossary/abenhashed_table_glosry.md) and when using a [hash key](../../abap-glossary/abenhash_key_glosry.md) on the value 0.

The loop entry `LOOP AT` does not modify `sy-subrc`. After exiting the loop, behind `ENDLOOP`, `sy-tabix` is set to the value that it had before entering the loop and `sy-subrc` is set as follows:

| **`sy-subrc`** | **Meaning**                          |
|----------------|--------------------------------------|
| 0              | At least one loop pass was executed. |
| 4              | No loop pass was executed.           |

## Hints

- If the internal table `itab` is specified using a [reference variable](../../abap-glossary/abenreference_variable_glosry.md), the loop is executed completely using the table referenced at entry. Any changes to the reference variable do not have an effect on the loop. The associated object cannot be deleted by the [Garbage Collector](../../abap-glossary/abengarbage_collector_glosry.md) until the loop has been completed. The same thing applies if the table is represented by a field symbol. After the implementation of the field symbol in the loop, iteration still takes place using the table linked to the field symbol when `LOOP` is entered.

- There is no implicit selection of a suitable key or index. The used table key or table index is always specified uniquely. A syntax check warning occurs if there is a suitable [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) available but not used. This warning should be removed by using the key. However, in exceptional cases, it can also be bypassed using a [pragma](../../abap-glossary/abenpragma_glosry.md).

- It is generally better to read multiple lines in a `LOOP` than making multiple individual line reads using the statement [`READ TABLE`](abapread_table.md) or [table expressions](abentable_expressions.md).

- For compatibility reasons, when a table body is replaced in the loop, a runtime error only occurs when a directly specified table is read without a specified secondary key and when a work area `wa` is specified for the output behavior [`result`](abaploop_at_itab_result.md).

- Using a special variant [`LOOP AT mesh_path`](abenmesh_loop.md), a loop can be executed across the last node of a [mesh path](../../abap-glossary/abenmesh_path_glosry.md).

- Another form of [table iterations](../../abap-glossary/abentable_iteration_glosry.md) is possible using [iteration expressions](../../abap-glossary/abeniteration_expression_glosry.md) and [`FOR`](abenfor_itab.md) in certain constructor expressions.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Loop across an internal table constructed using the [value operator](../../abap-glossary/abenvalue_operator_glosry.md) [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md), where each line is assigned to a field symbol declared inline using [`FIELD-SYMBOL`](../abap-declarations/abenfield-symbol_inline.md).

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES t_itab TYPE TABLE OF i WITH EMPTY KEY. 
 
LOOP AT VALUE t_itab( ( 1 ) ( 2 ) ( 3 ) ) ASSIGNING FIELD-SYMBOL(<fs>). 
  out->write( |{ <fs> }| ). 
ENDLOOP. 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Nested `LOOP` loops without explicit key declaration. The content of the current line for the outer loop is evaluated in the `WHERE` condition for the inner loop.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA name TYPE scarr-carrname VALUE '*'. 
cl_demo_input=>request( CHANGING field = name ). 
 
DATA: scarr_tab TYPE SORTED TABLE OF scarr 
                WITH UNIQUE KEY carrname, 
      spfli_tab TYPE SORTED TABLE OF spfli 
                WITH NON-UNIQUE KEY carrid. 
 
SELECT * 
       FROM scarr 
       INTO TABLE @scarr_tab. 
 
SELECT * 
       FROM spfli 
       INTO TABLE @spfli_tab. 
 
LOOP AT scarr_tab ASSIGNING FIELD-SYMBOL(<scarr_line>) 
                  WHERE carrname CP name. 
  LOOP AT spfli_tab INTO FINAL(spfli_line) 
                    WHERE carrid = <scarr_line>-carrid. 
    out->write_data( spfli_line ). 
  ENDLOOP. 
ENDLOOP. 
 
out->display( ).
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_ITAB_DYN_LOOP`

- *Cause:* Error in a dynamic `WHERE` condition

  *Runtime error:* `DYN_WHERE_PARSE_ERROR`
