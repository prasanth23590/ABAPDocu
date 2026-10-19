---
title: "scaling"
source_file: abenscale_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# scaling

[ABAP Language](../abap-programming-language/abenabala_glossary.md) [General](abenabap_glossary.md)

## Definition

Property of a [decimal floating point number](abendecfloat_glosry.md). A decimal floating point number can be viewed as an integer number of a given length that is scaled by dividing through a power of 10. This defines the number of [decimal places](abendecimal_place_glosry.md). In this sense, the negative exponent of a decimal floating point number is called scaling, which is applied to the mantissa. If the scaling is positive, it is equivalent to the number of decimal places. Decimal floating point numbers with the same value can have different scaling. Operations on decimal floating point numbers usually retain the scaling and therefore the number of decimal places. A [built-in function](abenbuiltin_function_glosry.md) for changing the scaling is [`rescale`](../abap-programming-language/abap-processing-internal-data/abendec_floating_point_functions.md). See also [precision](abenprecision_glosry.md).
