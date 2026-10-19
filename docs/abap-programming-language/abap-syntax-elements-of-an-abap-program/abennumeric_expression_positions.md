---
title: "Numeric Expression Positions"
source_file: abennumeric_expression_positions.html
section: "ABAP Programming Language > ABAP - Syntax Elements of an ABAP Program > ABAP Statements > Operand Positions > Expression Positions for Expressions > Read Positions for Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Numeric Expression Positions

Numeric expression positions are [read positions](../../abap-glossary/abenread_position_glosry.md) where [numeric data objects](../../abap-glossary/abennumeric_data_object_glosry.md), [constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md), [arithmetic expressions](../../abap-glossary/abenarithmetic_expression_glosry.md), [table expressions](../../abap-glossary/abentable_expression_glosry.md), and [built-in functions](../../abap-glossary/abenbuiltin_function_glosry.md), or [functional method calls](../../abap-glossary/abenfunctional_method_call_glosry.md) and [method chainings](../../abap-glossary/abenmethod_chaining_glosry.md) whose return value has a [numeric data type](../../abap-glossary/abennumeric_data_type_glosry.md), can be specified. The following numeric expression positions exist:

- Arguments of functions

  - Numeric arguments of [string functions](../abap-processing-internal-data/abenstring_functions.md)

  - Numeric arguments of [extremum functions](../abap-processing-internal-data/abennmax_nmin_functions.md)

- Counters and positions:

  - Operand `comp` of the statement

    [`ASSIGN COMPONENT comp OF STRUCTURE`](../abap-processing-internal-data/abapassign_dynamic_components.md)

  - Operand `n` of the statement

    [`DO n TIMES`](../abap-program-flow-logic/abapdo.md)

  - Operand `sec` of the statement

    [`WAIT UP TO sec SECONDS`](../abap-program-flow-logic/abapwait_up_to.md)

  - Operand `num` of the statement

    [`SHIFT ... BY num PLACES`](../abap-processing-internal-data/abapshift_places.md)

  - Operands `bitpos` and `val` of the statement

    [`SET BIT bitpos ... TO val`](../abap-processing-internal-data/abapset_bit.md).

  - Operand `bitpos` of the statement

    [`GET BIT bitpos ...`](../abap-processing-internal-data/abapget_bit.md).

- Positions specifications in the statements `FIND` and `REPLACE`:

  - Operands `off` and `len` of the statements

    [`FIND ... IN SECTION ... OF`](../abap-processing-internal-data/abapfind_section_of.md)

    [`REPLACE ... IN SECTION ... OF`](../abap-processing-internal-data/abapfind_section_of.md)

  - Operands `lin1`, `off1`, `lin2`, and `off2` of the statements

    [`FIND ... IN TABLE ... FROM lin1 OFFSET off1 TO lin2 OFFSET off2 ...`](../abap-processing-internal-data/abapfind_table_range.md)

    [`REPLACE ... IN TABLE ... FROM lin1 OFFSET off1 TO lin2 OFFSET off2 ...`](../abap-processing-internal-data/abapreplace_table_range.md)

  - Operands `off` and `len` of the statement

    [`REPLACE SECTION OFFSET off LENGTH len OF ...`](../abap-processing-internal-data/abapreplace_in_position.md)

- Specification of the line number `idx` with respect to a table index when accessing internal tables in the following:

  - [`READ TABLE itab INDEX idx ...`](../abap-processing-internal-data/abapread_table_index.md)

  - [`LOOP AT itab ...FROM idx1 TO idx2 STEP n ...`](../abap-processing-internal-data/abaploop_at_itab_cond.md)

  - [`INSERT itab ... INDEX idx ...`](../abap-processing-internal-data/abapinsert_itab_position.md)

  - [`INSERT LINES OF jtab FROM idx1 TO idx2 STEP n ...`](../abap-processing-internal-data/abapinsert_itab_linespec.md)

  - [`APPEND LINES OF jtab FROM idx1 TO idx2 STEP n ...`](../abap-processing-internal-data/abapappend_linespec.md)

  - [`MODIFY itab INDEX idx ...`](../abap-processing-internal-data/abapmodify_itab_index.md)

  - [`DELETE itab INDEX idx ...`](../abap-processing-internal-data/abapdelete_itab_line.md)

  - [`DELETE itab FROM idx1 TO idx2 STEP n ...`](../abap-processing-internal-data/abapdelete_itab_lines.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specifies a built-in function `lines( itab )` for specifying the loop passes of a [`DO`](../abap-program-flow-logic/abapdo.md) loop.

``` abap
DATA itab TYPE TABLE OF i WITH EMPTY KEY. 
 
... 
 
DO lines( itab ) TIMES. 
  ... 
ENDDO.
```
