---
title: "EXACT, Lossless Conversion of Enumerated Types"
source_file: abenexact_constructor_enum.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Lossless Assignments > EXACT, Lossless Operator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# EXACT, Lossless Conversion of Enumerated Types

If the constructor expression [`CONV`](abenconstructor_expression_conv.md) is applied to [enumerated types](../../abap-glossary/abenenum_type_glosry.md), the same [rules](abenconv_constructor_enum.md) apply as to the conversion operator [`CONV`](abenconstructor_expression_conv.md):

- An [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) can be converted to the [base type](../../abap-glossary/abenbase_type_glosry.md) of its enumerated type, as with `CONV`.

  `... EXACT base_type( enum_dobj ) ...`

- A data object that can be converted to the [base type](../../abap-glossary/abenbase_type_glosry.md) of an [enumerated type](../../abap-glossary/abenenum_type_glosry.md) can be converted to the enumerated type, as with `CONV`.

  `... EXACT enum_type( dobj ) ...`

The conditions of losslessness also apply:

- If a data object that can be converted to the base type is converted to the enumerated type, this happens in accordance with the [rules](abapmove_exact.md) of [lossless assignment](../../abap-glossary/abenlossless_assignment_glosry.md).

- If an [arithmetic expression](abapcompute_arith.md) is used as the operand of a conversion to the enumerated type, the result must be obtained in accordance with the [rules](abenlossless_calculation.md) of [lossless calculation](../../abap-glossary/abenlossless_calculation_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

If the conversion operator is used, the operand is converted to the base type `c` with length 4, cutting off any surplus places. If the lossless operator is used, this results in an exception.

``` abap
TYPES: 
  char8 TYPE c LENGTH 4, 
  BEGIN OF ENUM text BASE TYPE char8, 
    first  VALUE IS INITIAL, 
    second VALUE 'Seco', 
    third  VALUE 'Thrd', 
  END OF ENUM text. 
 
FINAL(result1) = CONV text( `Seco` && `nd` ). 
 
TRY. 
    FINAL(result2) = EXACT text( `Seco` && `nd` ). 
  CATCH cx_sy_conversion_data_loss. 
    cl_demo_output=>display( `Oops!` ). 
ENDTRY. 
```

If an arithmetic expression is used in the conversion operator, the result is converted to the base type `i`, cutting off the decimal places. If the lossless operator is used, this results in an exception.

``` abap
TYPES: 
  BEGIN OF ENUM number, 
    n0, n1, n2, 
  END OF ENUM number. 
 
FINAL(result1) = CONV number( + '1.2' ). 
 
TRY. 
    FINAL(result2) = EXACT number( + '1.2' ). 
  CATCH cx_sy_conversion_rounding. 
    cl_demo_output=>display( `Oops!` ). 
ENDTRY.
```
