---
title: "Numeric Literals"
source_file: abenuntyped_number_literals.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects > Literals"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Numeric Literals

## Syntax

``` abap
... [+|-]n[n[n[...]]] ...  
```

## Description

A numeric literal consists of a continuous sequence of up to 31 digits `n` (`0` to `9`), which can be directly preceded by a plus (`+`) or minus (`-`) sign.

- Numeric literals between -2147483648 and 2147483647 are [integer literals](../../abap-glossary/abeninteger_literal_glosry.md) and have the built-in ABAP type [`i`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md).

- Numeric literals outside of this interval are [packed number literals](../../abap-glossary/abenpacked_number_literal_glosry.md) and have the built-in ABAP type [`p`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md), with a length of 8 bytes if they are not longer than 15 digits and with a length of 16 bytes if they have between 16 and 31 digits.

## Hints

- There are no numeric literals of type [`int8`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md). The [conversion operator](../../abap-glossary/abenconversion_operator_glosry.md) [`CONV`](../abap-processing-internal-data/abenconstructor_expression_conv.md) can be used to convert a numeric literal to the type `int8`.

- [Packed number literals](../../abap-glossary/abenpacked_number_literal_glosry.md) have a different internal representation from [integer literals](../../abap-glossary/abeninteger_literal_glosry.md). They cannot be [cast](../../abap-glossary/abencast_casting_glosry.md) directly on field symbols with the data type integer.

- In numeric literals, no decimal separators or [scientific notation](../../abap-glossary/abenscientific_notation_glosry.md) with mantissa and exponent are possible.

- Numbers that cannot be represented as numeric literals can only be specified in character literals. If they are used in operand positions in which a numeric value is expected, they are converted into these. The [conversion operator](../../abap-glossary/abenconversion_operator_glosry.md) [`CONV`](../abap-processing-internal-data/abenconstructor_expression_conv.md) is recommended for targeted conversions.

- Numeric literals that span multiple lines are not allowed. Furthermore, the [literal operator](abenliteral_operator.md) `&` cannot be used to create a composite literal from multiple numeric literals.

- A numeric literal `+|-literal` directly prefixed with a plus or minus sign must not be confused with a [simple arithmetic expression](../abap-processing-internal-data/abapcompute_arith.md) `+|- literal` for which there is a space between the operator `+|-` and an unsigned literal. Unlike the numeric literal, the expression is not evaluated until runtime. Therefore, in such cases, the numeric literal should always be used for performance reasons.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first literal is of the type `i`. The following literals are of the type `p` with lengths 8 and 16.

``` abap
DATA: t TYPE c LENGTH 1, 
      l TYPE i. 
 
DATA(datadescr) = CAST cl_abap_datadescr( 
    cl_abap_typedescr=>describe_by_data( 
     123456 ) ). 
 
cl_demo_output=>write( datadescr->type_kind ). 
 
datadescr = CAST cl_abap_datadescr( 
    cl_abap_typedescr=>describe_by_data( 123456790123 ) ). 
cl_demo_output=>write( |{ datadescr->type_kind } { 
                          datadescr->length  }| ). 
 
datadescr = CAST cl_abap_datadescr( 
    cl_abap_typedescr=>describe_by_data( 12345679012345678 ) ). 
cl_demo_output=>write( |{ datadescr->type_kind } { 
                          datadescr->length  }| ). 
 
cl_demo_output=>display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Targeted conversion of a character literal into type `int8`.

``` abap
FINAL(num) = CONV int8( '123456790123' ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example shows that a casting of a [packed number literal](../../abap-glossary/abenpacked_number_literal_glosry.md) to the type `int8` has a different result than when using a field of the type `int8`, due to the different internal representation. If the field symbol `<fs2>` were typed with the [time stamp type](../../abap-glossary/abentimestamp_type_glosry.md) [`utclong`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_date_time.md), an exception would even be raised for the use in the [embedded expression](../../abap-glossary/abenembedded_expression_glosry.md) of the output.

``` abap
FIELD-SYMBOLS <fs1> TYPE int8. 
FIELD-SYMBOLS <fs2> TYPE int8. 
DATA num TYPE int8. 
 
num = 3155380704000000000. 
ASSIGN num                 TO <fs1> CASTING. 
ASSIGN 3155380704000000000 TO <fs2> CASTING. 
 
cl_demo_output=>display( |{ <fs1> } \n| && 
                         |{ <fs2> }| ).
```
