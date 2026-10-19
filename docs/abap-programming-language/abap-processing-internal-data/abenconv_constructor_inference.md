---
title: "CONV, Type Inference for Actual Parameters"
source_file: abenconv_constructor_inference.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > CONV, Conversion Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CONV, Type Inference for Actual Parameters

If a constructor expression

[`CONV`](abenconstructor_expression_conv.md) \#( \[[`let_exp`](../abap-declarations/abaplet.md)\] dobj )

is passed to generically typed formal parameters as an actual parameter using the character `#` as a symbol for the operand type, the following type inference is performed for the character `#`:

- If the data type of the operand `dobj` is known and matches the generic type of the formal parameter, no conversion is performed, and the type of the operand is used instead.

- If the data type of the operand `dobj` is known and is elementary, types are derived from it as follows for formal parameter types with generic lengths as follows:

  - Generic type `c`

    `c` with the length of the operand in operands of the types `n`, `d`, and `t`; `c` of the predefined output length of the operand for all other operand types except strings; no type is derived for operands of the types `string` and `xtring`

  - Generic type `n`

    `n` with the length of the operand for operands of the types `n`, `d`, and `t` and `n` with the length of a [conversion](abenconversion_elementary.md) of the operand to `n` for all other operand types except numeric types with decimal places and strings; no type is derived for operands of the types `decfloat16`, `decfloat34`, `f`, and `p` with decimal places plus `string` and `xtring`

  - Generic type `x`

    `x` with the rounded half length of the operand for operands of the type `c`; `x` with the length 4 for all other operand types except strings; no type is derived for operands of the types `string` and `xtring`

  - Generic type `p`

    `p` without decimal places with the length 16 for operands of the types `decfloat16`, `decfloat34`, `f`, `string`, or `c` and `n` with lengths greater than 15; `p` without decimal places with the length 8 for all other operand types

- In other cases, the type is derived from the generic type of the formal parameter as follows:

  - `csequence` and `clike` produce `string`

  - `xsequence` produces `xstring`

  - `numeric` and `decfloat` produce `decfloat34`

  - `p` produces `p` with the length 8 and no decimal places

  - Standard table type with generic primary table key produces a standard table with a [standard key](../../abap-glossary/abenstandard_key_glosry.md)

Other combinations of generic formal parameter types and operands cannot be made more concrete in any meaningful way and produce a syntax error with the exception of table types that are explicitly generic with respect to their secondary table keys.

Syntax warnings that can be hidden using pragmas also indicate any redundant conversions resulting from the rules above.

## Hint

The rules for derivations of the type where `#` is specified for actual parameters that are passed to generically typed formal parameters can prevent syntax errors in programs that call a procedure and in which the complete typing of a formal parameter is subsequently generalized by converting to a generic type.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The operator `CONV` generates a result of type `decfloat34` in this case. The generic parameter `p` has this type during the execution of the method, which is shown by the value *e* returned by `DESCRIBE FIELD`. The method call produces a corresponding syntax warning.

``` abap
CLASS demo1 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main IMPORTING p TYPE numeric. 
ENDCLASS. 
 
CLASS demo1 IMPLEMENTATION. 
  METHOD main. 
    FINAL(t)  = CAST cl_abap_datadescr( 
      cl_abap_typedescr=>describe_by_data( 
        p ) )->type_kind. 
    cl_demo_output=>display( |{ p } of type { t }| ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS demo2 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS demo2 IMPLEMENTATION. 
  METHOD main. 
    FIELD-SYMBOLS <fs> TYPE any. 
    ASSIGN 100 TO <fs>. 
    demo1=>main( CONV #( <fs> ) ) ##TYPE. 
  ENDMETHOD. 
ENDCLASS.
```

## Executable Example

[Conversion Operator, Type Inference](abenconv_type_inference_abexa.md)
