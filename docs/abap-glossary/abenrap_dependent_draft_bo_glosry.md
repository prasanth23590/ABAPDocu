---
title: "RAP dependent draft BO"
source_file: abenrap_dependent_draft_bo_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP dependent draft BO

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

A [draft-enabled RAP business object](abendraft_rap_bo_glosry.md) in a [cross-BO association](abencds_cross_bo_assoc_glosry.md) scenario whose [draft management](abenrap_draft_handling_glosry.md) is delegated to the associated principal draft BO. That means that its [instances](abeninstance_glosry.md) can only be set to draft if the associated instances of the principal draft BO are set to draft. A dependent draft BO has the header syntax `use draft as dependent` in the [projection view](abencds_projection_view_glosry.md) BDEF.

[***-\>* More about**](../abap-rap-business-objects/rap-behavior-definitions/abenbdl_use_projection.md)
