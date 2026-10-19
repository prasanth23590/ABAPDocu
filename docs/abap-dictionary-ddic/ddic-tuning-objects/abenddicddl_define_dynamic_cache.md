---
title: "DDIC DDL - DEFINE DYNAMIC CACHE"
source_file: abenddicddl_define_dynamic_cache.html
section: "ABAP Dictionary (DDIC) > DDIC - Tuning Objects > DDIC - Dynamic Caches > DDIC - Dictionary DDL for Defining Dynamic Caches"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC DDL - DEFINE DYNAMIC CACHE

## Syntax

``` abap
DEFINE DYNAMIC CACHE cache_name 
  ON dbtab 
{ projection_list } 
  [WHERE filter_cond] 
  [SEGREGATE CACHE DATA BY filter_cond] 
  [CREATION CONFIGURABLE DEFAULT {ON|OFF}];  
```

## Description

[Dictionary DDL](../../abap-glossary/abendictionary_ddl_glosry.md) statement used to define a [dynamic cache](../../abap-glossary/abendynamic_cache_glosry.md) for a [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md).

The name `cache_name` of a dynamic cache must comply with the [naming conventions for DDIC data types](../ddic-data-types/abenddic_types_names.md) and can have a maximum of 30 characters. The name is in the namespace of the [DDIC data types](../ddic-data-types/abenddic_data_types.md) and must match the name of the `DTDC` source code.

A dynamic cache can be defined for exactly one DDIC database table `dbtab`, which is specified after `ON`. Tables with [data aging](../../abap-glossary/abendata_aging_glosry.md) are not supported. Multiple dynamic caches can be defined for the same database table.

**Projection List**

The projection list projection_list of a dynamic cache consists of a restricted subquery which is applied to the DDIC database table to be tuned. It can consist of the following components:

- Fields of `dbtab` can optionally be specified.

  Client fields must not be specified. Client handling takes place implicitly.

- At least one aggregate function must be specified in the projection list. The following aggregate functions can be specified:

  - `SUM(arg)`

  - `AVG(arg)`

  - `MIN(arg)`

  - `MAX(arg)`

  - `COUNT(arg)`

  - `COUNT(*)`

- The argument `arg` of the aggregate function can be a field of `dbtab`, an untyped numeric or character literal, an arithmetic expression, or a case expression. The arithmetic expression can, in turn, have fields or literals as operands. The case expression can have fields, literals, or arithmetic expressions as operands.

**Clauses**

In a WHERE filter condition filter_cond, the cache result can be restricted as follows:

lhs = rhs \[{AND \| OR} lhs = rhs\]

- It is possible to join multiple expressions using `AND` and `OR`.

- `lhs` can be a field of `dbtab`.

- `rhs` can be a field of `dbtab` or an untyped numeric or character literal.

- The fields evaluated in the condition do not need to be defined as elements in the projection list.

Optionally, a further filter condition filter_cond can be added after SEGREGATE CACHE DATA BY to define which filtered results should be cached as follows:

lhs = rhs \[AND lhs = rhs\]

- It is possible to join multiple expressions using `AND`.

- `lhs` must be a field of `dbtab`.

- `rhs` can be a character or numeric literal or a numbered placeholder `$1`, `$2`, ...

- The fields evaluated in the condition must be defined as elements in the projection list.

**`CREATION CONFIGURABLE DEFAULT {ON|OFF}`**: Optional addition to activate or deactivate the dynamic cache.

- `ON`: the dynamic cache is created on SAP HANA as soon as the DDIC definition is activated.

- `OFF`: creation of the dynamic cache on SAP HANA is deferred to a later point in time.

If this clause is not used, the default is ON.

If the dynamic cache is deactivated, the consumer can later on decide when the cache should be used. This configuration can be done with transaction S_DBCACHE_CONFIG.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code shows an example for a dynamic cache for the database table `DEMO_DDIC_TYPES`.

``` abap
DEFINE DYNAMIC CACHE demo_ddic_dynamic_cache 
  ON demo_ddic_types 
    { 
     int4, 
     sum( int8 ) 
    } 
WHERE int1 = 4 
SEGREGATE CACHE DATA BY int4 = $1 
 CREATION CONFIGURABLE DEFAULT OFF;
```

This cache is generated as SQL view on the database. Client handling is added automatically. ![figure](images_dynamic_cache.png)
