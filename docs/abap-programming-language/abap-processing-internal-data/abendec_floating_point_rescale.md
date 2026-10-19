---
title: "num_func - rescale"
source_file: abendec_floating_point_rescale.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Numeric Functions (num_func) > num_func - round, rescale"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# num_func - rescale

## Syntax

``` abap
... rescale( val = arg {dec = n}|{prec = n} [mode = m] ) ...  
```

## Description

The rescaling function `rescale` can be implemented in [operand positions](../abap-operands/abenoperands_expressions.md) using the above syntax. This function changes the [scaling](../../abap-glossary/abenscale_glosry.md) of a decimal floating point number specified as an argument for the parameter `val`. A data object specified for `arg` is converted to the data type `decfloat34` before the function is executed, if necessary.

Either the parameter `dec` or the parameter `prec` must be given a value, where either the [scaling](../../abap-glossary/abenscale_glosry.md) or the [precision](../../abap-glossary/abenprecision_glosry.md) is set:

- If the parameter `dec` is given a value, the input value is returned using the [scaling](../../abap-glossary/abenscale_glosry.md) specified in `n`. `n` expects data objects of the type `i`, whose value must not be less than -6144. If the scaling would produce more than 34 places in the mantissa of the return value, a catchable exception is raised.

- If the parameter `prec` is given a value, the value entered is returned with the [precision](../../abap-glossary/abenprecision_glosry.md) specified in `n` and appropriate [scaling](../../abap-glossary/abenscale_glosry.md). `n` expects data objects of the type `i`, whose value must be greater than 0 and less than 34.

A rescaling can both reduce and increase [scaling](../../abap-glossary/abenscale_glosry.md) and [precision](../../abap-glossary/abenprecision_glosry.md). An increase adds zeros on the right.

The input value is rounded if required. The optional parameter `mode` can be used to specify the rounding rule, as described under the function `round`. The default is commercial rounding.
