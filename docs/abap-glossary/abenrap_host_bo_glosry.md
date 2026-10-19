---
title: "RAP host BO"
source_file: abenrap_host_bo_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP host BO

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

A [RAP BO](abenrap_bo_glosry.md) in a [cross-BO scenario](abencds_cross_bo_assoc_glosry.md) that has an [association](abenassociation_glosry.md) to a dependent [BO](abenrap_bo_glosry.md). An [association](abenassociation_glosry.md) to a dependent [BO](abenrap_bo_glosry.md) establishes a [composition-like relationship](abencds_composition_glosry.md) where the [host BO](abenrap_bo_glosry.md) takes over [locking](abenlock_glosry.md), [permission handling](abenauthorization_glosry.md) and [deletion](abenrap_delete_operation_glosry.md) for its dependent [BO](abenrap_bo_glosry.md). A [host BO](abenrap_bo_glosry.md) uses the [syntax](abensyntax_check_glosry.md) `to dependent` on the [association](abenassociation_glosry.md) to the dependent [BO](abenrap_bo_glosry.md).
