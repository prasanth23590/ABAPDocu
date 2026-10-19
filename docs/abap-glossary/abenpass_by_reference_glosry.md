---
title: "pass by reference"
source_file: abenpass_by_reference_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# pass by reference

[ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

A method of passing data from [actual parameters](abenactual_parameter_glosry.md) to [formal parameters](abenformal_parameter_glosry.md) when a [procedure](abenprocedure_glosry.md) is called, which is defined in the [parameter interface](abenparameter_interface_glosry.md) of the procedure. Pass by reference does not create a local [data object](abendata_object_glosry.md) for the actual parameter. Instead a reference to the actual parameter is passed to the procedure and it works with the actual parameter itself. [Input parameters](abeninput_parameter_glosry.md) passed by reference must not be modified in the procedure. See also [pass by value](abenpass_by_value_glosry.md).

[***-\>* More about**](../abap-programming-language/abap-program-structure/abenformal_parameters_oview.md)
