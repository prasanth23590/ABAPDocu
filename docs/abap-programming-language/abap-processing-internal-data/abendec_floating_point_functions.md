---
title: "num_func - round, rescale"
source_file: abendec_floating_point_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Numeric Functions (num_func)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# num_func - round, rescale

## Syntax

``` abap
... round|rescale( val = arg ...  ) ...  
```

## Description

The [built-in](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) rounding functions expect a [decimal floating point number](../../abap-glossary/abendecfloat_glosry.md) as a main argument `val` and additional arguments that describe how this floating point number is handled. The type of the return value of a rounding function is always `decfloat34`. Within an arithmetic expression, the argument for the decimal floating point number can either be an arithmetic expression or a function. The other arguments must always be specified as numeric data objects.

- [Rounding Function](abendec_floating_point_round.md)

- [Rescaling Function](abendec_floating_point_rescale.md)

## Hint

The class `CL_ABAP_MATH` includes the method `NORMALIZE` for normalizing a decimal floating point object. The mantissa does not have any closing zeros in a normalized floating point number.
