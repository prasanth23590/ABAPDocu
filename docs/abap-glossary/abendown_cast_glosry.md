---
title: "downcast"
source_file: abendown_cast_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# downcast

[ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

Also called narrowing cast. [Assignment](abenassignment_glosry.md) between [reference variables](abenreference_variable_glosry.md) in which the [static type](abenstatic_type_glosry.md) of the target variable is more specific than the static type of the source variable and the assignability is not checked until runtime. A downcast must always be performed explicitly. This is done using assignments with the [casting operator](abencasting_operator_glosry.md) ([`?=`](../abap-programming-language/abap-processing-internal-data/abapmove_cast.md)) and [constructor expressions](abenconstructor_expression_glosry.md) with the casting operator [`CAST`](../abap-programming-language/abap-processing-internal-data/abenconstructor_expression_cast.md). Downcasts are also still possible using the `INTO` addition of the statement [`WHEN TYPE`](../abap-programming-language/abap-program-flow-logic/abapwhen_type.md) of a case distinction using [`CASE TYPE OF`](../abap-programming-language/abap-program-flow-logic/abapcase_type.md). See also [upcast](abenup_cast_glosry.md).

[***-\>* More about**](../abap-programming-language/abap-processing-internal-data/abenconversion_references.md)
