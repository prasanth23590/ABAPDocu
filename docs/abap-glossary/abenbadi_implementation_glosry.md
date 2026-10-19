---
title: "BAdI implementation"
source_file: abenbadi_implementation_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# BAdI implementation

[ABAP](../abap-programming-language/abap-overview/abentechno_glossary.md)

## Definition

Implementation of a [BAdI](abenbadi_glosry.md). Multiple BAdI implementations can be assigned to a single BAdI. A BAdI implementation consists of a [BAdI implementation class](abenbadi_implement_class_glosry.md) and a filter condition that can be used to select the BAdI implementation in the [`GET BADI`](../abap-programming-language/abap-enhancements/abapget_badi.md) statement in the [BAdI object](abenbadi_method_glosry.md). A BAdI implementation can be in the state *active* or *inactive*, which overrides both the [Switch Framework](abenswitch_framework_glosry.md) setting and the filter condition.
