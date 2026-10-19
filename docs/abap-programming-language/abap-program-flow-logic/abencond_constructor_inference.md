---
title: "COND, SWITCH, Type Inference for Actual Parameters"
source_file: abencond_constructor_inference.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Conditional Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# COND, SWITCH, Type Inference for Actual Parameters

If the following constructor expression is passed to generically typed formal parameters as an actual parameter using the character `#` as a symbol for the operand type, the following type inference is performed for the character `#`:

[`COND`](abenconditional_expression_cond.md)\|[`SWITCH`](abenconditional_expression_switch.md) \#( ... THEN ... )

is passed to generically typed formal parameters as an actual parameter using the character `#` as a symbol for the operand type, the following type inference is performed for the character `#`:

- If the data type of the operand after the first `THEN` is known statically and matches the generic type of the formal parameter, this data type is used.

- If the data type of the operand after the first `THEN` is known statically and does not match the generic type of the formal parameter or if it is not known statically, the type is derived from the generic type as follows:

  - `string` for `csequence` and `clike`

  - `xstring` for `xsequence`

  - `decfloat34` for `numeric` and `decfloat`

  - `p` with the length 8 and no decimal places if `p` is generic

  - The [standard key](../../abap-glossary/abenstandard_key_glosry.md) for a standard table type with generic primary table key

    Generic data types other than table types that are explicitly generic with respect to their secondary table keys cannot be made more concrete and produce a syntax error. More specifically, this applies to the types `c`, `n`, and `x` with generic lengths.

## Hint

The rules for derivations of the type where `#` is specified for actual parameters that are passed to generically typed formal parameters can prevent syntax errors in programs that call a procedure and in which the complete typing of a formal parameter is subsequently generalized by converting to a generic type.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The operator `COND` generates a result of type `string` in this case. The generic parameter `p` has this type during the execution of the method, which is displayed by the value *g* returned by `DESCRIBE FIELD`. The method call leads to a corresponding syntax warning.

``` abap
CLASS demo1 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main IMPORTING p TYPE csequence. 
ENDCLASS. 
 
CLASS demo1 IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    FINAL(t) = CAST cl_abap_datadescr( 
      cl_abap_typedescr=>describe_by_data( p ) )->type_kind. 
    out->write( |{ p } of type { t }| ). 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS demo2 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS demo2 IMPLEMENTATION. 
  METHOD main. 
    FIELD-SYMBOLS: 
      <fs1> TYPE any, 
      <fs2> TYPE any. 
    ASSIGN 'AM' TO <fs1>. 
    ASSIGN 'PM' TO <fs2>. 
 
    demo1=>main( COND #( 
      WHEN cl_demo_date_time=>get_user_time( ) < '120000' THEN <fs1> 
      ELSE <fs2> ) ) ##TYPE. 
  ENDMETHOD. 
ENDCLASS.
```

## Executable Example

[Conditional Operator, Type Inference](abencond_type_inference_abexa.md)
