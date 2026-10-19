---
title: "System Class CL_ABAP_MATH"
source_file: abenfloating_point_class.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > System Classes for Numbers"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# System Class CL_ABAP_MATH

- [Constants for Minimum and Maximum Values](abenfloating_point_class.md#constants-for-minimum-and-maximum-values)

- [Common Mathematical Constants](abenfloating_point_class.md#common-mathematical-constants)

- [Operations with Floating Point Numbers](abenfloating_point_class.md#operations-with-floating-point-numbers)

  - [Rounding Binary Floating Point Numbers](abenfloating_point_class.md#rounding-binary-floating-point-numbers)

  - [Operations with Decimal Floating Point Numbers](abenfloating_point_class.md#operations-with-decimal-floating-point-numbers)

## Constants for Minimum and Maximum Values

The class `CL_ABAP_MATH` contains constants with the limits of the value ranges [built-in numeric types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Display of the minimum and maximum values of numeric types.

``` abap
cl_demo_output=>display( 
  |i:          { cl_abap_math=>min_int4 WIDTH = 20 
          } to { cl_abap_math=>max_int4 WIDTH = 20 } \n| && 
  |int8:       { cl_abap_math=>min_int8 WIDTH = 20 
          } to { cl_abap_math=>max_int8 WIDTH = 20 } \n| && 
  |decfloat16: { cl_abap_math=>min_decfloat16 STYLE = SCIENTIFIC 
                                              WIDTH = 20 
          } to { cl_abap_math=>max_decfloat16 STYLE = SCIENTIFIC 
                                              WIDTH = 20 } \n| && 
  |decfloat34: { cl_abap_math=>min_decfloat34 STYLE = SCIENTIFIC 
                                              WIDTH = 20 
          } to { cl_abap_math=>max_decfloat34 STYLE = SCIENTIFIC 
                                              WIDTH = 20 } \n| ).
```

## Common Mathematical Constants

The class `CL_ABAP_MATH` contains common mathematical constants, including pi, Euler's constant e, square roots of numbers such as 2 or 3, or logarithms of some constants.

## Operations with Floating Point Numbers

The class `CL_ABAP_MATH` contains methods for operations with floating point numbers.

### Rounding Binary Floating Point Numbers

The method `ROUND_F_TO_15_DECS` rounds a [binary floating point number](../../abap-glossary/abenbinfloat_glosry.md) to 15 places using commercial rounding.

### Hint

Commercial rounding to 15 digits can also be achieved using the built-in function [`round`](abendec_floating_point_functions.md), the result of which, however, has the `decfloat34` type.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example shows how rounding errors in the output formatting of binary floating point numbers can be prevented by two-step rounding using the method `ROUND_F_TO_15_DECS`. Instead of the method call, the function call `round( val = float dec = 15 )` can be used here.

``` abap
DATA float TYPE f VALUE '1.005'. 
 
cl_demo_output=>display( 
  |{ float DECIMALS = 2 }\n| && 
  |{ cl_abap_math=>round_f_to_15_decs( float ) DECIMALS = 2 }\n| ).
```

### Operations with Decimal Floating Point Numbers

- The method `GET_SCALE` returns the [scaling](../../abap-glossary/abenscale_glosry.md) of a [decimal floating point number](../../abap-glossary/abendecfloat_glosry.md).

- The method `GET_NUMBER_OF_DIGITS` returns the [precision](../../abap-glossary/abenprecision_glosry.md) of a [decimal floating point number](../../abap-glossary/abendecfloat_glosry.md).

- The method `NORMALIZE` returns a normalized floating point number. This means that the [scaling](../../abap-glossary/abenscale_glosry.md) and [precision](../../abap-glossary/abenprecision_glosry.md) of an input value are changed so that the mantissa has no trailing zeros.

- The method `GET_SCALE_NORMALIZED` returns the [scaling](../../abap-glossary/abenscale_glosry.md) of a normalized [decimal floating point number](../../abap-glossary/abendecfloat_glosry.md). If the input value has decimal places, the return value is the number of decimal places without trailing zeros.

- The method `GET_MAX_DB_VALUE` returns the maximum value of a number of the type `DF16_DEC` or `DF34_DEC` on the database.

- The method `GET_DB_LENGTH_DECS` returns the length and number of decimal places of a number of the type `DF16_DEC` or `DF34_DEC` on the database.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Display of the scaling and precision of a decimal floating point number.

``` abap
FINAL(decf) = CONV decfloat34( '1234.56789' ). 
 
cl_demo_output=>display( 
 |value = { decf 
 }\nscale = { cl_abap_math=>get_scale( decf ) 
 }\nprecision = { cl_abap_math=>get_number_of_digits( decf ) }| ).
```
