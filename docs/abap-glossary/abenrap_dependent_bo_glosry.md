---
title: "RAP dependent BO"
source_file: abenrap_dependent_bo_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP dependent BO

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

A [RAP BO](abenrap_bo_glosry.md) in a [cross-BO scenario](abencds_cross_bo_assoc_glosry.md) that delegates [locking](abenrap_locking_glosry.md), [permission handling](abenauthorization_glosry.md) and [deletion](abenrap_delete_operation_glosry.md) to its [host BO](abenhost_computer_glosry.md). If associated to a [host BO](abenhost_computer_glosry.md), it establishes a [composition-like relationship](abencds_composition_glosry.md) to the host. A [dependent object](abenrap_bo_entity_glosry.md) uses the syntax `dependent` in the header of the [BDEF](abencds_bdef_header_glosry.md).
