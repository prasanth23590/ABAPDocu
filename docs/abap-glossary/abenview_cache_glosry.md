---
title: "view cache"
source_file: abenview_cache_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# view cache

[General](abenabap_glossary.md)

## Definition

A cache on the [SAP HANA database](abenhana_database_glosry.md) that serves performance optimization. On the SAP HANA database, there are two types of view caches:

- [Static cache](abenstatic_view_cache_glosry.md):

  - A cache that is kept stable for a predefined retention time.

  - Called [*result cache*](https://help.sap.com/docs/SAP_HANA_PLATFORM/bed8c14f9f024763b0777aa72b5436f6/8ea43b3ff2e541e398e27d7e5caefab7) on the SAP HANA database.

- [Dynamic cache](abendynamic_cache_glosry.md)

  - A cache that guarantees real-time data.

  - Called [*dynamic result cache*](https://help.sap.com/docs/SAP_HANA_PLATFORM/bed8c14f9f024763b0777aa72b5436f6/bc12a173118548e9be8b69f1d62dfae1) on the SAP HANA database.

  - Integrated into [ABAP Dictionary](abenabap_dictionary_glosry.md). Defined using the statement [`DEFINE DYNAMIC CACHE`](../abap-dictionary-ddic/ddic-tuning-objects/abenddicddl_define_dynamic_cache.md) in [DDIC DDL](abenddic_dcl_glosry.md).

## More Information

ABAP Data Models guide, section about [Static Caches](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/b8202709b9d14d1db78c188a86e5e8a8?version=sap_cross_product_abap).
