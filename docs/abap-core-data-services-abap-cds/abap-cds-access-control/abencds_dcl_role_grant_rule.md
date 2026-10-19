---
title: "CDS DCL - DEFINE ROLE, grant_rule"
source_file: abencds_dcl_role_grant_rule.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ROLE > CDS DCL - DEFINE ROLE, access_rules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ROLE, grant_rule

## Syntax

``` abap
GRANT SELECT ON cds_entity [REDEFINITION];  
```

## Description

Full access rule in the statement [`DEFINE ROLE`](abencds_f1_define_role.md) in [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md). A full access rule `GRANT SELECT ON` without the addition `WHERE` provides access to a CDS entity `cds_entity` without conditions. If `cds_entity` is specified, the same applies as for a [conditional access rule](abencds_dcl_role_cond_rule.md).

The addition `REDEFINITION` prevents further `REDEFINITION` rules from being created for the same CDS entity and letting their activation fail.

## Hints

- For a [CDS entity](../../abap-glossary/abencds_entity_glosry.md), a full access rule has the same effect as when there is no role for the CDS entity or when CDS access control is forbidden for this CDS entity by using the annotation `@AccessControl.authorizationCheck:#NOT_ALLOWED` or by using [`[WITH] PRIVILEGED ACCESS`](../../abap-programming-language/abap-database-access/abapselect_data_source.md) in ABAP SQL when the entity is accessed.

- SAP does not deliver any CDS roles with full access rules. Partners and customers can use full access rules to override roles supplied by SAP.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS role specifies that all users can access the CDS view entity `DEMO_CDS_AUTH_FULLACCESS` without access conditions:

``` abap
CDS or DDIC source code was not found
```
