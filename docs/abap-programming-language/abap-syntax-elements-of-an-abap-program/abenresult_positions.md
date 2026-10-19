---
title: "Result Positions"
source_file: abenresult_positions.html
section: "ABAP Programming Language > ABAP - Syntax Elements of an ABAP Program > ABAP Statements > Operand Positions > Expression Positions for Expressions > Write Positions for Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Result Positions

Result positions are [write positions](../../abap-glossary/abenwrite_position_glosry.md) in which [writable expressions](../../abap-glossary/abenwritable_expression_glosry.md) can be specified. Writes are performed on the result of the expression. Result positions include the following:

- Actual parameter in [method calls](../abap-calling-and-exiting-program-units/abenmethod_calls.md) for [output parameters](../abap-calling-and-exiting-program-units/abapcall_method_parameters.md), [input/output parameters](../abap-calling-and-exiting-program-units/abapcall_method_parameters.md), and [return values](../abap-calling-and-exiting-program-units/abapcall_method_parameters.md)

- Left side of an assignment with the [assignment operator `=`](../abap-processing-internal-data/abenequals_operator.md)

- Memory area `mem_area` of the statement [`ASSIGN mem_area TO`](../abap-processing-internal-data/abapassign_mem_area_writable_exp.md)

- Structure `struc` of the statement [`ASSIGN COMPONENT comp OF STRUCTURE struc`](../abap-processing-internal-data/abapassign_dynamic_components.md)

- Right side in the declaration of a local field symbol in a [`LET` expression](../abap-declarations/abaplet.md)

- Operand `dobj` of the statement [`CLEAR`](../abap-processing-internal-data/abapclear.md)

- Operand `byte_string` of the statement [`SET BIT`](../abap-processing-internal-data/abapset_bit.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Uses a table expression `itab[ sy-index ]` on the left side of a [calculation assignment](../../abap-glossary/abencalculation_assignment_glosry.md).

``` abap
DATA itab TYPE TABLE OF i. 
 
itab = VALUE #( ( 1 ) ( 2 ) ( 3 ) ). 
 
DO 3 TIMES. 
  itab[ sy-index ] *= 10. 
ENDDO.
```
