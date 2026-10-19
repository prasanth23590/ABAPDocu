---
title: "CDS DCL - DEFINE ROLE, projection_rule"
source_file: abencds_dcl_role_proj_rule.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ROLE > CDS DCL - DEFINE ROLE, access_rules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ROLE, projection_rule

## Syntax

``` abap
GRANT SELECT ON cds_entity_projection 
  AS PROJECTION ON cds_entity_base 
    FALLBACK ASSOCIATION fallback_association;  
```

## Description

Creates an access rule for the [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md) `cds_entity_projection` which is a projection on the base view `cds_entity_base`. `cds_entity_projection` must be a [CDS transactional query](../../abap-glossary/abencds_transactional_pv_glosry.md), i.e. a projection view with the provider contract `TRANSACTIONAL_QUERY`.

At runtime, the [access conditions](../../abap-glossary/abenaccess_condition_glosry.md) of the base view are applied to the projection view if all of the following conditions are met:

- All CDS elements used in the access conditions of the base view are present in the projection view (aliasing using the keyword `AS` is supported).

- The access conditions of the base view do not use any parameters (`$parameters`...).

- If the access conditions of the base view use [path expressions](../../abap-glossary/abenpath_expression_glosry.md) and an [association target](../../abap-glossary/abenassociation_target_glosry.md) is redirected to another projection view using the keyword [`REDIRECTED TO`](../abap-cds-data-definitions/abencds_pv_assoc_redirected.md), using path filters is not allowed.

If it is not possible to apply the access conditions of the base view directly to the projection view, all access conditions are rewritten at runtime to point to the association `fallback_association`. This association must exist in the projection view and point to the base view.

## Hints

- The fallback association `fallback_association` should be a to-one association to the base view, using the key elements.

- The syntax check of the projection rule issues a syntax warning if it detects that the access conditions of the base view could potentially trigger the use of the fallback association at runtime. This check is user-independent and realizes a worst case estimation. Depending on the actual authorizations of a user performing the access controlled action, it is still possible that the fallback association is not used at runtime.
