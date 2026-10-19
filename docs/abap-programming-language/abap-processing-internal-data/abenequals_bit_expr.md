---
title: "=, Bit Expression"
source_file: abenequals_bit_expr.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > =, Assignment Operator > =, Assign Calculation Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# =, Bit Expression

## Syntax

``` abap
result = bit_exp.  
```

[`bit_exp`](abapcompute_bit.md)

## Description

If a [bit expression](../../abap-glossary/abenbit_expression_glosry.md) [`bit_exp`](abapcompute_bit.md) is specified on the right side of the [assignment operator `=`](abenequals_operator.md), a byte chain with the [calculation length](abenbitexp_length.md) is calculated and assigned to the left side `result` like a [source field with the type `xstring`](abenconversion_type_xstring.md).

The following can be specified for `result`:

- A [variable](../../abap-glossary/abenvariable_glosry.md) with the type `x` or `xstring`.

- A [variable](../../abap-glossary/abenvariable_glosry.md) with the type `c` or `string`.

- An inline declaration [`DATA(var)`](../abap-declarations/abendata_inline.md) or [`FINAL(var)`](../abap-declarations/abenfinal_inline.md). The data type of the declared variable `var` is `xstring`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Bit expressions as the right side of assignments. The expressions can also be used directly as input parameters of the output methods.

``` abap
DATA hex1 TYPE xstring VALUE '0123456789ABCDEF'. 
DATA hex2 TYPE xstring VALUE 'FEDCBA9876543210'. 
 
FINAL(result1)  = hex1 BIT-AND hex2. 
FINAL(result2)  = hex1 BIT-OR hex2. 
cl_demo_output=>write(   result1 ). 
cl_demo_output=>display( result2 ).
```
