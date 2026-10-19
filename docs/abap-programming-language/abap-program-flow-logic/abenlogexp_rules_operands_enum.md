---
title: "rel_exp - Comparing Enumerated Types"
source_file: abenlogexp_rules_operands_enum.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Rules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparing Enumerated Types

An operand with an [enumerated type](../../abap-glossary/abenenum_type_glosry.md) can only be compared with [enumerated objects](../../abap-glossary/abenenumerated_object_glosry.md) of the same enumerated type. There is no implicit conversion. The values of the operands are compared according to the [rules](abenlogexp_rules_operands.md) that apply to the elementary [base type](../../abap-glossary/abenbase_type_glosry.md) of the enumerated type.

## Hint

An operand of an enumerated type cannot be compared directly with a character-like operand of type `c` or `string`, even though there is a [conversion rule](../abap-processing-internal-data/abenconversion_enumerated.md) for this case. In this case, helper variables or the conversion operator [`CONV`](../abap-processing-internal-data/abenconstructor_expression_conv.md) can be used to perform an explicit conversion.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the first two comparisons, [enumerated objects](../../abap-glossary/abenenumerated_object_glosry.md) of the enumerated type `number` are compared with each other. The third comparison shows how an operand with an enumerated type can be converted to be compared like a character.

``` abap
TYPES: 
  BEGIN OF ENUM number, 
    n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, 
  END OF ENUM number. 
 
DATA: num2 TYPE number VALUE n2, 
      num5 TYPE number VALUE n5. 
 
IF num2 < num5. 
  cl_demo_output=>write( |num2 < num5| ). 
ENDIF. 
 
IF num2 > n0. 
  cl_demo_output=>write( |num2 > n0| ). 
ENDIF. 
 
IF CONV string( n7 ) = `N7`. 
  cl_demo_output=>write( |CONV string( n7 ) = `N7`| ). 
ENDIF. 
 
cl_demo_output=>display( ).
```
