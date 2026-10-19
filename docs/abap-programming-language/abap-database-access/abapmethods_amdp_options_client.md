---
title: "[CLASS-]METHODS, AMDP OPTIONS client_handling"
source_file: abapmethods_amdp_options_client.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Methods > [CLASS-]METHODS, AMDP OPTIONS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# \[CLASS-\]METHODS, AMDP OPTIONS client_handling

## Syntax Forms

**Client-Safe Variants**

``` abap
 ... AMDP OPTIONS {CDS SESSION CLIENT DEPENDENT} 
               | {CLIENT INDEPENDENT} ...
```

### Variant

[1. `... CDS SESSION CLIENT DEPENDENT`](abapmethods_amdp_options_client.md#variant-1)

[2. `... CLIENT INDEPENDENT`](abapmethods_amdp_options_client.md#variant-2)

## Overview

### Description

These variants of the addition [`AMDP OPTIONS`](abapmethods_amdp_options.md) define the [client handling](abenamdp_client_handling.md) of an [AMDP method](../../abap-glossary/abenamdp_method_glosry.md). The variants

- `CDS SESSION CLIENT DEPENDENT`

- `CLIENT INDEPENDENT`

restrict the [`USING`](abapmethod_by_db_proc.md) list and involve also checks of the SQLScript source code. They are necessary for the [client safety](abenamdp_client_safety.md) of the AMDP method. One of the variants must be used in [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md).

For a detailed overview, how the `USING` list depends on the client handling, refer to [Client Handling/`USING` Matrices](abenamdp_call_matrices.md).

### Hint

An AMDP method that accesses a CDS entity whose client handling is governed implicitly or explicitly by the HANA session variable `CDS_CLIENT`, must be declared with one of the options `CDS SESSION CLIENT`. Otherwise, a syntax error occurs.

## Variant 1

`... CDS SESSION CLIENT DEPENDENT`

### Description

The option `CDS SESSION CLIENT DEPENDENT` declares the AMDP method implementation explicitly to be [client-dependent](../../abap-glossary/abenclient_dependent_glosry.md) and the client handling of the AMDP method is as follows:

- The ABAP-specific [session variable](../../abap-glossary/abensession_variable_glosry.md) `CDS_CLIENT` of the HANA database is set to its default value when the AMDP method is called from ABAP. That is the [client](../../abap-glossary/abenclient_glosry.md) of the current [logon](../../abap-glossary/abenlogon_glosry.md) to the [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) (nominal value of the ABAP system field [`sy-mandt`](../abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md)).

- The method implementation is made [client-safe](../../abap-glossary/abenclient_safe_glosry.md). Only the following client-safe objects can be accessed and specified after the addition [`USING`](abapmethod_by_db_proc.md):

  - [Client-dependent CDS view entities](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_v2_view_client_handling.md) filtered by the HANA session variable `CDS_CLIENT` (CDS [session variable](../../abap-glossary/abensession_variable_glosry.md) [`$session.client`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_session_var_builtin_v2.md)).

  - [Client-dependent CDS table functions](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_handling.md) that are [client-safe](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_safety.md).

  - Client-dependent [DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md). When accessed by AMDP methods with the addition `CDS SESSION CLIENT DEPENDENT`, an implicitly generated database view is accessed that wraps the database table and selects data for the client contained in the HANA session variable `CDS_CLIENT` only. Only read accesses are allowed.

  - Client-independent CDS objects and DDIC database tables

  - Other client-dependent or client-independent AMDP methods with the AMDP option `CDS SESSION CLIENT DEPENDENT` or `CLIENT INDEPENDENT`

- The SQLScript method implementation is checked as described under [AMDP - Client Safety](abenamdp_client_safety.md).

### Hints

- It makes no sense, to pass an explicit parameter for the client to a method with the option `CDS SESSION CLIENT DEPENDENT` and use it in a `WHERE` condition for a client column. Since the results of the allowed data sources are implicitly restricted to the current client, the result would be empty for all clients other than the current client.

- When accessing a client-dependent DDIC database table from an AMDP method where `CDS SESSION CLIENT DEPENDENT` is used, the data source implicitly becomes client-safe.

- Together with `CDS SESSION CLIENT DEPENDENT`, there can be no input parameter with the name `dependent`.

- The HANA session variable `CDS_CLIENT` can be addressed in the CDS DDL of [ABAP CDS](../../abap-glossary/abencds_ddl_glosry.md) under the name [`$session.client`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_session_variable_v2.md).

### Executable Example

Refer to [AMDP - Implementation of SQLScript Procedures (Client-safe)](abenamdp_cs_abexa.md) for the only way of handling client-dependent data that is client-safe.

## Variant 2

`... CLIENT INDEPENDENT`

### Description

The option `CLIENT INDEPENDENT` defines the method implementation to be [client-independent](../../abap-glossary/abenclient_independent_glosry.md). Only client-independent [CDS entities](../../abap-glossary/abencds_entity_glosry.md) and [DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md) can be accessed and specified after the addition [`USING`](abapmethod_by_db_proc.md). The SQLScript method implementation is checked as described under [AMDP - Client Safety](abenamdp_client_safety.md). A client-independent method implementation is automatically [client-safe](../../abap-glossary/abenclient_safe_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The AMDP methods `GET_DOKIL_CDS` and `GET_DOKIL_DDIC` of AMDP class `CL_DEMO_AMDP_TABFNC_CLNTINDPCS` have the AMDP option `CLIENT INDEPENDENT` and access a client-independent CDS view entity as well as a client-independent DDIC database table.

``` abap
METHOD get_dokil_cds 
       BY DATABASE PROCEDURE FOR HDB 
       LANGUAGE SQLSCRIPT 
       OPTIONS READ-ONLY 
       USING demo_cds_dokil. 
 
  docu_objects = 
      select * 
             from demo_cds_dokil 
               where  id = :id and 
                       object like :object and 
                       langu = 'E' 
               order by object; 
 
ENDMETHOD.
```

``` abap
METHOD get_dokil_ddic 
       BY DATABASE PROCEDURE FOR HDB 
       LANGUAGE SQLSCRIPT 
       OPTIONS READ-ONLY 
       USING dokil. 
 
  docu_objects = 
      select id, object, langu, typ, version, masterlang 
             from dokil 
               where  id = :id and 
                       object like :object and 
                       langu = 'E' 
               order by object; 
 
ENDMETHOD.
```

The following code snippet calls the AMDP methods. Both results are the same.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA id TYPE     dokil-id     VALUE 'SD'. 
DATA object TYPE dokil-object VALUE 'ABENABAP*'. 
cl_demo_input=>new( 
  )->add_field( CHANGING field  = id 
  )->add_field( CHANGING field = object 
  )->request( ). 
 
REPLACE ALL OCCURRENCES OF '*' IN object WITH '%'. 
 
cl_demo_amdp_tabfnc_clntindpcs=>get_dokil_cds( 
  EXPORTING 
    id           = id 
    object       = object 
  IMPORTING 
    docu_objects =  FINAL(objects_cds) ). 
 
 
cl_demo_amdp_tabfnc_clntindpcs=>get_dokil_ddic( 
  EXPORTING 
    id           = id 
    object       = object 
  IMPORTING 
    docu_objects =  FINAL(objects_ddic) ). 
 
ASSERT objects_cds = objects_ddic. 
 
out->write( objects_cds ). 
 
out->display( ).
```
