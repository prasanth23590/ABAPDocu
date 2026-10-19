---
title: "ABAP CDS - DCL Restrictions for Transactional CDS Projection Views"
source_file: abencds_f1_dcl_projection_views.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - DCL Restrictions for Transactional CDS Projection Views

[CDS transactional queries](../../abap-glossary/abencds_transactional_pv_glosry.md) and [CDS transactional interfaces](../../abap-glossary/abencds_trans_interface_glosry.md) (`DEFINE ROOT VIEW ENTITY ... AS PROJECTION ON ...`) are designed to apply CDS access control from the underlying CDS entity `1:1`.

For this purpose, CDS access control provides a special rule type [`projection_rule`](abencds_dcl_role_proj_rule.md).

Prior to the introduction of projection rules, access rules for transactional projection views were regular access rules, which had to comply with the following restrictions:

- The use of [`REDEFINITION`](abencds_dcl_role_cond_rule.md) is not allowed.

- Only the condition [`INHERITING CONDITIONS FROM ENTITY`](abencds_f1_cond_inherit.md) can be used.

- The only exception is to create an access control with a full access rule.

- The inheriting entity in `INHERITING CONDITIONS FROM ENTITY` must match the source entity of the CDS projection view.

- The only allowed [replacement step](abencds_f1_cond_inherit_rpl_step.md) is [`ELEMENT WITH`](abencds_f1_cond_inherit_rpl_step.md) in one of the following flavors:

  - Replacing a plain entity field with a plain entity field.

  - Renaming of an association.

  - Replacing a path expression that ends with a field with a plain entity field.
