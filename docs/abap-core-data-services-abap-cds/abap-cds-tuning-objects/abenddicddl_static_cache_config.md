---
title: "CDS DDL - DEFINE STATIC CACHE, CREATION CONFIGURABLE DEFAULT"
source_file: abenddicddl_static_cache_config.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Tuning Objects > ABAP CDS - Static Caches > CDS DDL - DEFINE STATIC CACHE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE STATIC CACHE, CREATION CONFIGURABLE DEFAULT

## Syntax

``` abap
... 
[CREATION CONFIGURABLE DEFAULT {ON|OFF}]; 
...  
```

## Description

Caches can be toggled on and off with the transaction `S_DBCACHE_CONFIG`. The default state of the cache can be controlled using the statement `CREATION CONFIGURABLE DEFULT`, or otherwise the corresponding Fiori app *Manage Cache Configuration*. If the statement is not included in the static cache source code, the cache will always be active on the HANA database. If the statement is used, the cache will be able to be toggled.
