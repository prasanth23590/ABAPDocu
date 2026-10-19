---
title: "conflict resolving enhancement implementation"
source_file: abenconflict_resol_impl_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# conflict resolving enhancement implementation

[ABAP](../abap-programming-language/abap-overview/abentechno_glossary.md)

## Definition

An [enhancement implementation](abenenhancement_impl_glosry.md) to which a [conflict switch](abenconflict_switch_glosry.md) is assigned instead of a regular [switch](abenswitch_glosry.md). A conflict resolving enhancement implementation is used for [conflict resolution](abenconflict_resolution_glosry.md). It must mirror the common semantics of all regular enhancement implementations that can potentially be switched on at the same time and which then show conflicts. These enhancement implementations can be determined by assigning switches to the conflict switch. During conflict resolution, a conflict resolving enhancement implementation has priority over regular enhancements. In the event of multiple conflict resolving enhancement implementations exist, the one that resolves the most conflicts takes priority.
