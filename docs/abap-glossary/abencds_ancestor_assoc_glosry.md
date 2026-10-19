---
title: "ancestor association"
source_file: abencds_ancestor_assoc_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ancestor association

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

An [intra-BO association](abencds_intra_bo_assoc_glosry.md) whose [association target](abenassociation_target_glosry.md) is a [RAP BO entity](abenrap_bo_entity_glosry.md) between the current node and the [RAP BO root entity](abenrap_bo_root_entity_glosry.md). The association target must be higher in the hierarchical structure of the RAP composition tree, so it cannot be a sibling node or the [CDS parent entity](abenparent_entity_glosry.md) of the current node. An ancestor association is defined using the keyword [`ancestor`](../abap-rap-business-objects/rap-behavior-definitions/abenbdl_ancestor_ext.md). The purpose of ancestor associations is to make it possible to implicitly derive the path to a RAP BO's [authorization master entity](abenrap_auth_ma_ent_glosry.md), [lock master entity](abenrap_lock_ma_ent_glosry.md), and [ETag master entity](abenrap_etag_ma_ent_glosry.md), so the respective entities need not be defined explicitly.

[***-\>* More about**](../abap-rap-business-objects/rap-behavior-definitions/abenbdl_ancestor_ext.md)
