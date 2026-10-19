---
title: "BAdI reference variable"
source_file: abenbadi_reference_variable_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# BAdI reference variable

[ABAP](../abap-programming-language/abap-overview/abentechno_glossary.md)

## Definition

Special [object reference variable](abenobject_refer_variable_glosry.md) that is declared with reference to a [BAdI](abenbadi_glosry.md) and is used to access the associated [BAdI object](abenbadi_object_glosry.md). BAdI reference variables are supplied with a [BAdI reference](abenbadi_reference_glosry.md) using [`GET BADI`](../abap-programming-language/abap-enhancements/abapget_badi.md) and are only used in [`CALL BADI`](../abap-programming-language/abap-enhancements/abapcall_badi.md) to call [BAdI methods](abenbadi_method_glosry.md). Technically, BAdI reference variables are [class reference variables](abenclass_reference_variabl_glosry.md) of the [static type](abenstatic_type_glosry.md) of a concrete [BAdI](abenbadi_class_glosry.md) class, or of its abstract superclass `CL_BADI_BASE`.
