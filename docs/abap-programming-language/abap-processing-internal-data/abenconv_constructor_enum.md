---
title: "CONV, Conversion of Enumerated Types"
source_file: abenconv_constructor_enum.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > CONV, Conversion Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CONV, Conversion of Enumerated Types

If the constructor expression [`CONV`](abenconstructor_expression_conv.md) is used on [enumerated types](../../abap-glossary/abenenum_type_glosry.md), the following rules apply:

- If the operand `dobj` is an [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) `enum_dobj` and `type` corresponds exactly to the [base type](../../abap-glossary/abenbase_type_glosry.md) `base_type` of the enumerated type, the result is the actual [enumerated value](../../abap-glossary/abenenumerated_value_glosry.md) of the operand.

  `... CONV base_type( enum_dobj ) ...`

- If `type` is an enumerated type `enum_type`, the following can be specified for the operand `dobj`:

  - A data object of the same elementary type as the [base type](../../abap-glossary/abenbase_type_glosry.md) of the enumerated type, with any length and number of decimal places

  - An expression allowed at this position whose result can be converted to the [base type](../../abap-glossary/abenbase_type_glosry.md) of the enumerated type

    If the operand represents a valid [enumerated value](../../abap-glossary/abenenumerated_value_glosry.md), the result is a temporary [enumerated variable](../../abap-glossary/abenenumerated_variable_glosry.md) with this value. If the value is not valid, an exception `CX_SY_CONVERSION_NO_ENUM_VALUE` occurs. `... CONV enum_type( dobj ) ...`

In all other cases, the normal [conversion rules](abenconversion_enumerated.md) apply to `CONV`, where enumerated types can only be converted to the character-like types `c` and `string` and no types can be converted to enumerated types.

**Short form:**

If the enumerated type of an enumerated object `enum_dobj` has the same base type `base_type` as any other enumerated type `enum_type` and the enumerated value in the enumerated variable is also defined in `enum_type`, it is possible, according to the above rules, to nest constructor expressions `CONV` as follows:

`CONV enum_type( CONV base_type( enum_dobj ) )`

The following short form can also be used for the nesting:

`CONV enum_type( enum_dobj )`

The result is the enumerated value from `enum_dobj` with the data type `enum_type`.

## Hints

- Using `CONV` for enumerated types deviates from the rule that `CONV` always behaves according to the regular conversion rules in assignments.

- If the operand is an enumerated type with a character-like [base type](../../abap-glossary/abenbase_type_glosry.md), and this base type is specified as `type`, the special rule above applies instead of the general conversion rule. That is, the enumerated value is returned, not the name.

- Corresponding [rules](abenexact_constructor_enum.md) apply to the lossless operator [`EXACT`](abenconstructor_expression_exact.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first three assignments to the fields `text1`, `text2`, and `text3` follow the regular [conversion rules](abenconversion_enumerated.md) for enumerated type to character-like. The result in each case is the name `BLUE`.

A direct assignment of the enumerated constant `blue` to a field `value1` of type `i` is not possible. The conversion operator `CONV` returns the actual enumerated value *1* for the base type `i`.

It is also not possible to assign the value 1 of type `i` to an enumerated variable `color1` with enumerated type `color`. However, the conversion operator `CONV` returns an enumerated value for the type `color` if the operand has the base type `i` and a allowed value.

``` abap
TYPES: 
  BEGIN OF ENUM color, 
    red, blue, green, 
  END OF ENUM color. 
 
DATA: text1 TYPE string, 
      text2 TYPE string. 
 
text1 = blue. 
text2 = CONV #( blue ). 
FINAL(text3) = CONV string( blue ). 
 
ASSERT text1 = text2. 
ASSERT text1 = text3. 
 
DATA: value1 TYPE i, 
      value2 TYPE i. 
 
"value1 = blue. 
value2 = CONV #( blue ). 
FINAL(value3) = CONV i( blue ). 
 
ASSERT value2 = value3. 
 
DATA: color1 TYPE color, 
      color2 TYPE color. 
 
"color1 = 1. 
color2 = CONV #( 1 ). 
FINAL(color3) = CONV color( 1 ). 
 
ASSERT color2 = color3. 
 
cl_demo_output=>display( |Name:  { color3 
                       }\nValue: { value3 }| ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The short form

CONV animal( peach )

of the conversion operator `CONV` acts like

CONV animal( CONV i( peach ) )

It creates the value 2 from the enumerated constant `peach` of the enumerated type `fruit`, which can be assigned to the enumerated variable `animal` with enumerated type `animal`. The output shows the associated name `DOG`.

``` abap
TYPES: 
  BEGIN OF ENUM fruit, 
    apple, peach, orange, 
  END OF ENUM fruit. 
 
TYPES: 
  BEGIN OF ENUM animal, 
    cat, dog, cow, 
  END OF ENUM animal. 
 
cl_demo_output=>display( CONV animal( peach ) ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example shows the difference between the regular [conversion rules](abenconversion_enumerated.md) and using the conversion operator `CONV` for a character-like base type:

- In assignments to `result1`, the regular conversion rules apply and the name `SECOND` is assigned.

- In assignments to `result2`, the special rule for `CONV` with the specification of the base type applies and the enumerated value *aaaaaaaa* is assigned.

``` abap
TYPES: 
  char8 TYPE c LENGTH 8, 
  BEGIN OF ENUM text BASE TYPE char8, 
    first  VALUE IS INITIAL, 
    second VALUE 'aaaaaaaa', 
    third  VALUE 'bbbbbbbb', 
  END OF ENUM text. 
 
DATA: result1 TYPE char8, 
      result2 TYPE char8. 
 
result1 = second. 
result2 = CONV #( second ). 
 
cl_demo_output=>display( 
  |result1: { result1 }\nresult2: { result2 }| ).
```

## Executable Example

[Conversion Operator, Enumerated Types](abenconv_enum_abexa.md)
