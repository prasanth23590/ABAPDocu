---
title: "conflict switch"
source_file: abenconflict_switch_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# conflict switch

[ABAP](../abap-programming-language/abap-overview/abentechno_glossary.md)

## Definition

A special [switch](abenswitch_glosry.md) for [conflict resolution](abenconflict_resolution_glosry.md). Multiple regular switches are assigned to a conflict switch. The switch status of a conflict switch is determined by the switch status of the assigned switches: *on* if all assigned switches are *on*, *off* if at least one assigned switch is *off*, and *standby* in all remaining cases. For every combination of [enhancement implementation](abenenhancement_impl_glosry.md) to which the regular switches of the conflict switch are assigned, a [conflict resolving enhancement implementation](abenconflict_resol_impl_glosry.md) must be created to which the conflict switch is assigned.
