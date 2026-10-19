---
title: "BAdI method"
source_file: abenbadi_method_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# BAdI method

[ABAP](../abap-programming-language/abap-overview/abentechno_glossary.md)

## Definition

[Method](abenmethod_glosry.md) of a [BAdI interface](abenbadi_interface_glosry.md). A BAdI method is implemented in [BAdI implementations](abenbadi_implementation_glosry.md) and then called exclusively via the associated BAdI object using [`CALL BADI`](../abap-programming-language/abap-enhancements/abapcall_badi.md). If the BAdI interface is part of the definition of a [BAdI](abenbadi_glosry.md) that is defined for multiple use, the [parameter interface](abenparameter_interface_glosry.md) of a BAdI method can only contain [input parameters](abeninput_parameter_glosry.md) and [input/output parameters](abeninput_output_parameter_glosry.md). If all BAdIs are defined for single use, the interface can also have [output parameters](abenoutput_parameter_glosry.md) or a [return value](abenreturn_value_glosry.md). BAdI methods can define or propagate [exceptions](abenexception_glosry.md), and their implementation can be made [optional](../abap-programming-language/abap-declarations/abapmethods_default.md).
