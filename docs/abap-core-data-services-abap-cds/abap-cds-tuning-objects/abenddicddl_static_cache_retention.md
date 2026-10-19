---
title: "CDS DDL - DEFINE STATIC CACHE, RETENTION"
source_file: abenddicddl_static_cache_retention.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Tuning Objects > ABAP CDS - Static Caches > CDS DDL - DEFINE STATIC CACHE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE STATIC CACHE, RETENTION

## Syntax

``` abap
... 
[RETENTION retention_in_minutes] 
...  
```

## Description

The cache is kept stable for a retention time, defined in minutes by `RETENTION`. After this time, the cache is invalidated.
