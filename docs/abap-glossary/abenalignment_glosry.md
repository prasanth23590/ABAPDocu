---
title: "alignment"
source_file: abenalignment_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# alignment

[General](abenabap_glossary.md)

## Definition

Most [data types](abendata_type_glosry.md) are subject to specific alignment requirements depending on the current platform. In memory, [fields](abenfield_glosry.md) of this [type](abentype_glosry.md) must start at addresses that are divisible by 2, 4, 8, or 16. In a [structure](abenstructure_glosry.md) or [substructure](abensubstructure_glosry.md), the [structure component](abenstructure_component_glosry.md) with the highest alignment requirement determines the alignment of the entire structure, where [alignment gaps](abenalignment_gap_glosry.md) are created before or after components with alignment requirements.

[***-\>* More about**](../abap-programming-language/abap-data-types-and-data-objects/abenalignment.md)
