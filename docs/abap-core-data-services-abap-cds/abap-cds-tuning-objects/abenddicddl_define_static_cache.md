---
title: "CDS DDL - DEFINE STATIC CACHE"
source_file: abenddicddl_define_static_cache.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Tuning Objects > ABAP CDS - Static Caches"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE STATIC CACHE

## Syntax

``` abap
DEFINE STATIC CACHE cache_name 
  ON view_entity_name 
{ element_list } 
[RETENTION retention_in_minutes] 
[SEGREGATE CACHE DATA BY filter_cond] 
[CREATION CONFIGURABLE DEFAULT {ON|OFF}];  
```

[`[RETENTION retention_in_minutes]`](abenddicddl_static_cache_retention.md) · [`[SEGREGATE CACHE DATA BY filter_cond]`](abenddicddl_static_cache_segregate.md) · [`[CREATION CONFIGURABLE DEFAULT {ON|OFF}];`](abenddicddl_static_cache_config.md)

## Description

[Dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md) statement used to define a [static cache](../../abap-glossary/abenstatic_view_cache_glosry.md) for a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). The naming rules for CDS objects apply to static caches as well. A static cache is defined on a view entity `view_entity_name`, after which the element list that is to be included in the cache must be defined. Not all elements of the select list of the view entity need to be included in the cache.

The cache is kept stable for a retention time, defined in minutes by `RETENTION`, after which it is invalidated.

Filtering cached data can be done with the optional statement ` SEGREGATE CACHE DATA BY`.

Caches can be toggled on and off with the transaction `S_DBCACHE_CONFIG`. The default state of the cache can be controlled using the statement `CREATION CONFIGURABLE DEFULT`, or otherwise the corresponding Fiori app *Manage Cache Configuration*. If the statement is not included in the static cache source code, the cache will always be active on the HANA database. If the statement is used, the cache will be able to be toggled.

## Hint

There are some limitations to static caches:

- The element list of static caches must not be empty

- View entities with parameters cannot be cached

- `AVG` cannot be used
