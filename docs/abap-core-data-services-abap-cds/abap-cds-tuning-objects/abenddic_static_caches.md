---
title: "ABAP CDS - Static Caches"
source_file: abenddic_static_caches.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Tuning Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Static Caches

A [static cache](../../abap-glossary/abenstatic_view_cache_glosry.md) is an ABAP CDS object that defines cache settings for cached data on the SAP HANA database. It serves as an interface between AS ABAP and [static result caches](https://help.sap.com/docs/SAP_HANA_PLATFORM/bed8c14f9f024763b0777aa72b5436f6/bc12a173118548e9be8b69f1d62dfae1) in SAP HANA. Static caches can be defined for CDS view entities. It caches a part of the CDS view entity's data in order to avoid repeated aggregation. This can improve performance.

Static caches are defined using the syntax [`DEFINE STATIC CACHE`](abenddicddl_define_static_cache.md) and can only be defined for view entities without parameters and without certain functions like `AVG`. The cached data is retained for a specified amount of time.

## Accessing Static Caches Using ABAP SQL

When querying cached data, whether or not the cache is accessed depends on whether or not [database hints](../../abap-programming-language/abap-database-access/abenabap_sql_db_hints.md) are provided. If no database hints are provided, the cache cannot be accessed.

### Hints

- SAP HANA offers static and dynamic [view caches](../../abap-glossary/abenview_cache_glosry.md). The counterpart to static caches are called [static result caches](https://help.sap.com/docs/SAP_HANA_PLATFORM/bed8c14f9f024763b0777aa72b5436f6/bc12a173118548e9be8b69f1d62dfae1) on SAP HANA.

- Some settings for static caches can be controlled using the `@Consumption.cacheSettings` annotation in the cached view.

## More Information

[Static Caches](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/b8202709b9d14d1db78c188a86e5e8a8?version=sap_cross_product_abap)
