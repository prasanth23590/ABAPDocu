---
title: "DDIC - Dictionary DDL for Defining Dynamic Caches"
source_file: abenddic_define_dynamic_cache.html
section: "ABAP Dictionary (DDIC) > DDIC - Tuning Objects > DDIC - Dynamic Caches"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Dictionary DDL for Defining Dynamic Caches

An ABAP Dictionary [dynamic cache](../../abap-glossary/abendynamic_cache_glosry.md) is defined as a source-code-based cache in the [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md) [Dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md). A dynamic cache is defined in a separate piece of `DTDC` source code and is saved and transported with this code. A piece of `DTDC` source code for dynamic caches can define exactly one dynamic cache:

- [`DEFINE DYNAMIC CACHE`](abenddicddl_define_dynamic_cache.md)

No name table and no [DDIC runtime object](../../abap-glossary/abenddic_runtime_object_glosry.md) are generated for a dynamic cache. Therefore, a dynamic cache cannot be accessed or read with ABAP.
