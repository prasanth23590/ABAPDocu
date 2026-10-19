---
title: "ABAP CDS - DCL Restrictions for CDS Hierarchies"
source_file: abencds_f1_dcl_hierarchies.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - DCL Restrictions for CDS Hierarchies

[CDS hierarchies](../../abap-glossary/abencds_hierarchy_glosry.md) can be protected with access control. However, it must be ensured that individual rows are not filtered out if they are part of a logical block in the hierarchy construction. Otherwise, the hierarchies constructed by the database could be destroyed and hierarchy operators produce undefined results.

For this reason, the use of [access conditions](../../abap-glossary/abenaccess_condition_glosry.md) with arbitrary entity elements is not allowed.

However, if the CDS hierarchy declares a directory ([`DEFINE HIERARCHY ... DIRECTORY ... FILTER BY`](../abap-cds-data-definitions/abencds_f1_define_hierarchy.md)), then elements of this association can be used.

In addition, access conditions that do not result in database selections can be used:

- PFCG conditions without fields `( ( ) = ASPECT PFCG_AUTH( ... ) )`

- Conditions with exclusive use of [left side host expressions](abencds_dcl_cond_left_side.md). This allows protection of a CDS hierarchy using the hierarchy directory specified by a parameter.

- The special conditions `TRUE`, `FALSE`, and `VOID`. These should not, however, be used directly in CDS access controls.

## Hints

- When conditions on the directory association are involved, they are applied to the constructed hierarchy object. Therefore, the time for its creation will be consumed even if the user does not have the authorization to retrieve the result.

- The requirement to specify a `FILTER BY` addition in the `CDS` hierarchy definition still exists and by design already provides an all-or-nothing behavior regarding the hierarchy directory. Due to the properties from above, access control can act as an additional reason for *nothing*.
