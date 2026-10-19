---
title: "Time-Stamp-Like Expression Positions"
source_file: abentimestamp_expr_positions.html
section: "ABAP Programming Language > ABAP - Syntax Elements of an ABAP Program > ABAP Statements > Operand Positions > Expression Positions for Expressions > Read Positions for Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Time-Stamp-Like Expression Positions

Time-stamp-like expression positions are [read positions](../../abap-glossary/abenread_position_glosry.md) where [time stamp fields](../../abap-glossary/abentimestamp_field_glosry.md) and [constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md), [table expressions](../../abap-glossary/abentable_expression_glosry.md), and [built-in functions](../../abap-glossary/abenbuiltin_function_glosry.md) can be specified, or [functional method calls](../../abap-glossary/abenfunctional_method_call_glosry.md) and [method chainings](../../abap-glossary/abenmethod_chaining_glosry.md) whose return value has a [time stamp type](../../abap-glossary/abentimestamp_type_glosry.md). The following time-stamp-like expression positions exist:

- Time-stamp-like arguments in time stamp functions

  - Operand `time_stamp` of the function

    [`utclong_add( val = time_stamp ... )`](../abap-processing-internal-data/abenutclong_add.md)

  - Operands `time_stamp2` and `time_stamp1` of the function

    [`utclong_diff( high = time_stamp2 low = time_stamp1 )`](../abap-processing-internal-data/abenutclong_diff.md)

- Functional operand positions in statements for time stamps

  - Operand `time_stamp` of the statement

    [`CONVERT UTCLONG time_stamp TIME ZONE tz INTO ...`](../abap-processing-internal-data/abapconvert_utclong.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specification of a functional method call and a time stamp function as arguments of the time stamp function `utclong_diff`.

``` abap
DATA ts TYPE timestampl. 
GET TIME STAMP FIELD ts. 
 
cl_demo_output=>display( 
  utclong_diff( 
    low =  cl_abap_tstmp=>tstmp2utclong( timestamp =  ts ) 
    high = utclong_add( val = utclong_current( ) 
                        hours = 1 ) ) ).
```
