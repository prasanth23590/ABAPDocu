---
title: "ABAP CDS - Restrictions in DDL in Cloud Development"
source_file: abencds_ddl_v5.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Restrictions in DDL in Cloud Development

In [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md), the following restrictions apply to CDS entities defined by customers and partners in [SAP BTP ABAP environment](../../abap-glossary/abensap_btp_abap_env_glosry.md) and [SAP S/4HANA Cloud ABAP environment](../../abap-glossary/abens4_hana_cloud_abap_env_glosry.md):

- In the definition of CDS entities, only repository objects released by SAP, or repository objects in the same software component, can be used.

- Only released [CDS annotations](../../abap-glossary/abencds_annotation_glosry.md) can be used. Array elements of [annotation arrays](../../abap-glossary/abenannotation_array_glosry.md) can be specified in square brackets only.

## Hints

- See [Released APIs](../../abap-apis/released-apis/abenreleased_apis.md) for a list of repository objects that are released as APIs in the current system.

- In the column `API`, the program `ABAP_DOCU_CDS_ANNOS_OVERVIEW` indicates whether an SAP annotation is released for [SAP BTP](../../abap-glossary/abensap_btp_glosry.md) and other cloud environments.
