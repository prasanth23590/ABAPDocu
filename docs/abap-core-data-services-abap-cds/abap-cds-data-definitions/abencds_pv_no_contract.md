---
title: "CDS DDL - CDS Projection View, No Contract"
source_file: abencds_pv_no_contract.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS Projection View, No Contract

It is possible, but not recommended, to define a [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md) without a [provider contract](abencds_pv_provider_contract.md). The default provider contract, if no provider contract is set explicitly, is [`TRANSACTIONAL_QUERY`](abencds_pv_provider_contract.md). The same features are available as for [transactional queries](../../abap-glossary/abencds_transactional_pv_glosry.md) and a projection view without provider contract can be used in the same scenarios. However, there are some minor differences in the syntax checks applied:

- In a transactional projection view with provider contract `TRANSACTIONAL_QUERY`, path fields [`path_expr`](abencds_proj_view_path_expr.md).element can be used in an [association `ON` condition](abencds_proj_view_association.md) via `$projection`. In a projection view without provider contract, this is not allowed.

  Example:

  Field in the projection list:

  `_assoc.fieldName`

  This path field can be used in an association `ON` condition in a transactional query, but not in a projection view without provider contract:

  `... on $projection.fieldName = 'A' ...`

## Hint

Specifying a provider contract is strongly recommended, but not enforced, in most cases. However, there is one exception: if the projected entity is a [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md), then the provider contract `TRANSACTIONAL_QUERY` is mandatory. When no provider contract is specified, a syntax check error occurs.
