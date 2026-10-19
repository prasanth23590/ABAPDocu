---
title: "RAP - CDS-Based Authorization"
source_file: abenbdl_cds_based_auth.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorCharacteristics > RAP - Authorization"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - CDS-Based Authorization

## Description

Read access to RAP business objects can be limited using the data control language of ABAP CDS ([CDS DCL](../../abap-glossary/abencds_dcl_glosry.md)) in the CDS data model that a RAP BO is based on.

The following annotations are available in CDS data definitions to define access control settings:

- [`AccessControl.authorizationCheck`](../../abap-core-data-services-abap-cds/abap-cds-annotations/abencds_1180334353_anno.md)

The following rules apply to the CDS entities belonging to a RAP behavior definition regarding the CDS-based access control. The rules are checked per authorization master group, this means, for a [RAP authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md) and all its [authorization dependent entities](../../abap-glossary/abenrap_auth_dep_ent_glosry.md). Authorizations are considered as hierarchical, meaning that the authorization checks may get at most stricter.

- [`AccessControl.authorizationCheck`](../../abap-core-data-services-abap-cds/abap-cds-annotations/abencds_1180334353_anno.md)

  - The value `#CHECK` should not be used at all. Use `#MANDATORY` instead.

  - All children of an entity with value `#NOT_REQUIRED` must be either `#NOT_REQUIRED` or `#MANDATORY`.

  - All children of an entity with value `#NOT_ALLOWED` must be one of `#NOT_ALLOWED`, `#NOT_REQUIRED`, or `#MANDATORY`.

  - All children of `#PRIVILEGED_ONLY` must be `#PRIVILEGED_ONLY` too.

  - All children of `#PRIVILEGED_ONLY` must be related by one of the [CDS compositions](../../abap-glossary/abencds_composition_glosry.md) specified as values of this annotation.
