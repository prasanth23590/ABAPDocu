---
title: "REDUCE, Type Inference for Actual Parameter"
source_file: abenreduce_constructor_inference.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Iteration Expressions > REDUCE, Reduction Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# REDUCE, Type Inference for Actual Parameter

If a constructor expression

[`REDUCE`](abenconstructor_expression_reduce.md) \#( ... INIT ... FOR ... )

is passed to generically typed formal parameters as an actual parameter using the character `#` as a symbol for the operand type, the following type inference is performed for the character `#`:

- If the data type of the first declaration after `INIT` matches the generic type of the formal parameter, this data type is used.

- If the data type of the first declaration after `INIT` does not match the generic type of the formal parameter, the type is derived from the generic type as follows:

  - `string` for `csequence` and `clike`

  - `xstring` for `xsequence`

  - `decfloat34` for `numeric` and `decfloat`

  - `p` with the length 8 and no decimal places if `p` is generic

  - The [standard key](../../abap-glossary/abenstandard_key_glosry.md) for a standard table type with generic primary table key

    Generic data types other than table types that are explicitly generic with respect to their secondary table keys cannot be made more concrete and produce a syntax error. More specifically, this applies to the types `c`, `n`, and `x` with generic lengths.

## Hints

- The data type of the first declaration after `INIT` is always identified statically.

- The rules for derivations of the type where `#` is specified for actual parameters that are passed to generically typed formal parameters can prevent syntax errors in programs that call a procedure and in which the complete typing of a formal parameter is subsequently generalized by converting to a generic type.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The operator `REDUCE` generates a result of type `string` here. The generic parameter `p` has this type during the execution of the method, which is shown by the value *g* in the attribute `type_kind`. The method call leads to a corresponding syntax warning that is suppressed by a pragma.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS meth IMPORTING p TYPE csequence. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD meth. 
    FINAL(t) = cl_abap_typedescr=>describe_by_data( p )->type_kind. 
    cl_demo_output=>display( |{ p } of type { t }| ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    demo=>meth( REDUCE #( INIT s = 0 
                           FOR  i = 1 UNTIL i > 10 
                           NEXT s += i ) ) ##type. 
  ENDMETHOD. 
ENDCLASS.
```

## Executable Example

[Reduce Operator, Type Inference](abenreduce_type_inference_abexa.md)
