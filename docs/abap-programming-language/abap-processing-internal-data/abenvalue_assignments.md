---
title: "Assignments"
source_file: abenvalue_assignments.html
section: "ABAP Programming Language > ABAP - Processing Internal Data"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Assignments

An assignment passes the content of a source to a target data object. The source can be one of the following:

- [Data objects](../../abap-glossary/abendata_object_glosry.md)

- Return values or results of [functional methods](../../abap-glossary/abenfunctional_method_glosry.md), [built-in functions](../../abap-glossary/abenbuiltin_function_glosry.md) and [constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md), or [table expressions](../../abap-glossary/abentable_expression_glosry.md)

- Results of [calculation expressions](../../abap-glossary/abencalculation_expression_glosry.md)

The following sections describe the rules, operators, and keywords where the assignment of source values to target data objects is of significance.

- [Assignment and conversion rules](abenconversion_rules.md)

- [`=` - assignment operator](abenequals_operator.md)

- [`CONV` - conversion operator](abenconstructor_expression_conv.md)

- [Assigning structure components](abencorresponding.md)

- [Assigning references](abenreference_assignments.md)

- [Lossless assignments](abenlossless_move.md)

- [Special assignments](abenabap_data_move.md)

- [Initializations](abeninitializations.md)

Assignments also occur, however, in the [operand positions](../../abap-glossary/abenoperand_position_glosry.md) of many other statements in which the [assignment rules](abenconversion_rules.md) also apply.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Typical assignment with the assignment operator (`=`) during which a conversion takes place. In the assignment to a data object `num` of type `i`, the current user date is converted to the number of days since 01.01.0001.

``` abap
DATA num TYPE i. 
 
num = cl_demo_date_time=>get_user_date( ). 
 
cl_demo_output=>display( 
            |{ cl_demo_date_time=>get_user_date( ) }->{ num }| 
                          ).
```
