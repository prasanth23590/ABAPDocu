---
title: "pass by value"
source_file: abenpass_by_value_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# pass by value

[ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

Method of passing data from [actual parameters](abenactual_parameter_glosry.md) to [formal parameters](abenformal_parameter_glosry.md) when a [procedure](abenprocedure_glosry.md) is called, which is defined in the [parameter interface](abenparameter_interface_glosry.md) of the procedure. Pass by value creates a local [data object](abendata_object_glosry.md) as a copy of the actual parameter. [Output parameters](abenoutput_parameter_glosry.md) and [return values](abenreturn_value_glosry.md) are initialized when the procedure is called. [Input parameters](abeninput_parameter_glosry.md) and [input/output parameters](abeninput_output_parameter_glosry.md) are passed the value of the actual parameter when the procedure is called. Modified formal parameters are only passed to the actual parameter if the procedure has been processed without errors, that is, when the last statement is reached or when it is exited via [`RETURN`](../abap-programming-language/abap-calling-and-exiting-program-units/abapreturn.md) (or [`EXIT`](../abap-programming-language/abap-calling-and-exiting-program-units/abapexit_processing_blocks.md) or [`CHECK`](../abap-programming-language/abap-calling-and-exiting-program-units/abapcheck_processing_blocks.md)). See also [pass by reference](abenpass_by_reference_glosry.md).

[***-\>* More about**](../abap-programming-language/abap-program-structure/abenformal_parameters_oview.md)
