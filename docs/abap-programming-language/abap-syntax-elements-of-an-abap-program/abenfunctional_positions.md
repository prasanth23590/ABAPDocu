---
title: "Functional Operand Positions"
source_file: abenfunctional_positions.html
section: "ABAP Programming Language > ABAP - Syntax Elements of an ABAP Program > ABAP Statements > Operand Positions > Expression Positions for Expressions > Read Positions for Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Functional Operand Positions

Functional operand positions are [read positions](../../abap-glossary/abenread_position_glosry.md) that expect appropriate [data objects](../../abap-glossary/abendata_object_glosry.md) and [functional method calls](../../abap-glossary/abenfunctional_method_call_glosry.md) or [method chainings](../../abap-glossary/abenmethod_chaining_glosry.md), as well as [constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md) and [table expressions](../../abap-glossary/abentable_expression_glosry.md) whose return value or result has a suitable data type. The following functional operand positions exist:

- Functional operand positions in ABAP Objects

  - Operand `oref` of the statement

    [`SET HANDLER ... FOR oref`](../abap-calling-and-exiting-program-units/abapset_handler_instance.md).

- Functional operand positions in relational expressions

  - Operand `ref` of the predicate expression

    [`... ref IS [NOT] BOUND ...`](../abap-program-flow-logic/abenlogexp_bound.md)

- Functional operand positions in assignments

  - Operand `struc1` of the statement

    [`MOVE-CORRESPONDING struc1 TO ...`](../abap-processing-internal-data/abapmove-corresponding.md)

  - Operand `val` of the statement

    [`CLEAR ... WITH val`](../abap-processing-internal-data/abapclear.md)

- Functional Operand Positions in String Processing and Byte String Processing

  - Character-like or byte-like arguments of the built-in functions

    [`dbmaxlen`](../abap-processing-internal-data/abenlength_functions.md), [`xstrlen`](../abap-processing-internal-data/abendescriptive_functions_binary.md)

  - Operand `itab` of the statement

    [`CONCATENATE LINES OF itab INTO ...`](../abap-processing-internal-data/abapconcatenate.md)

  - Operand `itab` of the statement

    [`FIND ... IN TABLE itab ...`](../abap-processing-internal-data/abapfind_itab.md)

- Functional operand positions in statements for internal tables

  - Internal table `itab` of the statement

    [`READ TABLE itab ...`](../abap-processing-internal-data/abapread_table.md)

  - Work area `wa` of the statement

    [`READ TABLE ... FROM wa ...`](../abap-processing-internal-data/abapread_table_key.md)

  - Internal table `itab` of the statement

    [`LOOP AT itab ...`](../abap-processing-internal-data/abaploop_at_itab.md)

  - Internal table `jtab` of the statement

    [`INSERT LINES OF jtab INTO ...`](../abap-processing-internal-data/abapinsert_itab_linespec.md)

  - Work area `wa` of the statement

    [`COLLECT wa INTO ...`](../abap-processing-internal-data/abapcollect.md)

  - Internal table `jtab` of the statement

    [`APPEND LINES OF jtab TO ...`](../abap-processing-internal-data/abapappend_linespec.md)

  - Work area `wa` of the statement

    [`DELETE TABLE ... FROM wa ...`](../abap-processing-internal-data/abapdelete_itab_key.md)

- Functional operand positions in statements for UTC time stamps

  - Operand `tz` of the statement

    [`CONVERT UTCLONG time_stamp TIME ZONE tz INTO...`](../abap-processing-internal-data/abapconvert_utclong.md)

  - Operands `dat`, `tim`, `dst`, and `tz` of the statement

    [`CONVERT DATE dat TIME tim DAYLIGHT SAVING TIME dst INTO UTCLONG ... TIME ZONE tz`](../abap-processing-internal-data/abapconvert_date_utclong.md)

  - Operands `time_stamp` and `tz` of the statement

    [`CONVERT TIME STAMP time_stamp TIME ZONE tz INTO ...`](../abap-processing-internal-data/abapconvert_time-stamp.md)

  - Operands `dat`, `tim`, `dst`, and `tz` of the statement

    [`CONVERT DATE dat TIME tim DAYLIGHT SAVING TIME dst INTO TIME STAMP ... TIME ZONE tz`](../abap-processing-internal-data/abapconvert_date_time-stamp.md)

- Functional operand positions in message processing

  - Operand `oref` of the statement

    MESSAGE [`oref`](../abap-text-repositories/abapmessage_msg.md) ...

  - Operands `dobj1` to `dobj4` of the statement

    MESSAGE ...[`WITH dobj1 ... dobj4`](../abap-text-repositories/abapmessage.md)

- Functional operand positions in statements for checkpoints

  - Operands `val1 val2` of the statement

    [`ASSERT ... FIELDS val1 val2 ...`](../abap-program-maintenance/abapassert.md)

  - Operands `val1 val2 ...` of the statement

    `LOG-POINT ... FIELDS val1 val2 ...`

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Calls a functional method `cl_abap_tstmp=>normalize` in a functional operand position.

``` abap
DATA ts TYPE timestamp. 
... 
CONVERT TIME STAMP cl_abap_tstmp=>normalize( ts ) TIME ZONE 'UTC' 
        INTO DATE FINAL(date) TIME FINAL(time).
```
