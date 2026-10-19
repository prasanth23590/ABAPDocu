---
title: "conflict resolution"
source_file: abenconflict_resolution_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# conflict resolution

[ABAP](../abap-programming-language/abap-overview/abentechno_glossary.md)

## Definition

Term in [Switch Framework](abenswitch_framework_glosry.md). A conflict occurs if multiple [enhancement implementation elements](abenenhancement_impl_elem_glosry.md) exist for a single [enhancement option](abenenhancement_point_glosry.md) for which only one enhancement can be carried out, and when more than one of these enhancement implementation elements are switched on at the same time. Currently, a conflict can occur with the statements `ENHANCEMENT-SECTION` and [`GET BADI`](../abap-programming-language/abap-enhancements/abapget_badi.md). To resolve the conflict, the [conflict resolving enhancement implementation](abenconflict_resol_impl_glosry.md) with the highest priority is searched among the [enhancement implementations](abenenhancement_impl_glosry.md) and its enhancement implementation element is then used.
