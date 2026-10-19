---
title: "ABAP CDS - Restrictions in DCL in Cloud Development"
source_file: abencds_f1_dcl_syntax_v5.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Restrictions in DCL in Cloud Development

In [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md), the following restrictions apply to CDS roles and CDS access policies defined by customers and partners in [SAP BTP ABAP environment](../../abap-glossary/abensap_btp_abap_env_glosry.md) and [SAP S/4HANA Cloud ABAP environment](../../abap-glossary/abens4_hana_cloud_abap_env_glosry.md):

- An access control can use other development objects when these either belong to the same software component or are a [released API](../../abap-glossary/abenreleased_api_glosry.md) with the [C1 contract](../../abap-glossary/abenc1_contract_glosry.md). This affects the following usage types:

  - CDS entities as data source for data source in PFCG mappings and user-defined aspects.

  - CDS entities or database tables which act as association target in any used path expression.

  - CDS entities used as inheritance source for [access conditions](../../abap-glossary/abenaccess_condition_glosry.md) or as selector for role-based inheritance.

  - Authorization objects

- The following usage types cannot yet be released and are therefore limited to customer objects in the same software component:

  - Access roles used as inheritance source for role-based inheritance.

  - User-defined aspects and PFCG mappings.

  - SACF scenarios.

- The protected entity itself can only be in the same software component as the access control.

- In entity-based condition inheritance when inheriting from an entity not in the same software component, the following restrictions apply:

  - The usage of replacement step `ROOT WITH` is mandatory.

  - Replacement steps `PARAMETER WITH` and `PFCG FILTER` are allowed.

  - All other replacement steps cannot be used.

- In role-based condition inheritance, the flavor without selector `(GRANT SELECT ON ... INHERIT ...)` is not allowed.

## Hint

See [Released APIs](../../abap-apis/released-apis/abenreleased_apis.md) for a list of repository objects that are released as APIs in the current system.
