---
title: "CDS prebound parameter"
source_file: abencds_prebound_parameter_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS prebound parameter

[CDS](../abap-core-data-services-abap-cds/abencds_glossary.md)

## Definition

In [ABAP CDS](abenabap_cds_glosry.md), a prebound parameter overwrites a parameter binding in a CDS association. Overwriting parameter bindings is usually forbidden, but it can be allowed to be defined using the keyword `default` in the CDS association definition. This definition can both be the initial definition within an entity or the exposure of an association in the projection list.

Prebound parameters are relevant in cases where the parameter binding can already be specified when the association is defined. As a result, the prebound parameter does not need to be specified every time when the association is used to read elements.
