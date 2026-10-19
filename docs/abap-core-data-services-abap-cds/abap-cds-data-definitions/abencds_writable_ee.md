---
title: "CDS DDL - DEFINE EXTERNAL ENTITY, WRITABLE"
source_file: abencds_writable_ee.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - External Entities > CDS DDL - DEFINE EXTERNAL ENTITY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE EXTERNAL ENTITY, WRITABLE

## Syntax

``` abap
... WRITABLE ...  
```

## Description

The addition `WRITABLE` defines a [CDS external entity](../../abap-glossary/abencds_external_entity_glosry.md) as [writable](../../abap-glossary/abenwritable_ee_glosry.md). Writable external entities allow modifying data on external database systems using ABAP SQL [`INSERT`](../../abap-programming-language/abap-database-access/abapinsert_dbtab.md), [`UPDATE`](../../abap-programming-language/abap-database-access/abapupdate.md), [`MODIFY`](../../abap-programming-language/abap-database-access/abapmodify_dbtab.md), and [`DELETE`](../../abap-programming-language/abap-database-access/abapdelete_dbtab.md) operations. Only [dynamic external entities](../../abap-glossary/abencds_dynamic_ee_glosry.md) can be writable.

As a prerequisite, the CDS external entity must have exactly the same [primary key](../../abap-glossary/abenprimary_key_glosry.md) as the remote object.

The database connection is managed using an [ABAP SQL connection object](../../abap-glossary/abenabap_sql_conn_obj_glosry.md) that is created using the method `WRITE_ENABLED_4_LOGICAL_SCHEMA` of the system class `CL_ABAP_SQL_CONNECTION_BUILDER`. This connection object enables write access for exactly one logical external schema and the external entities linked with the respective logical external schema. The following rules apply to the connection object:

- It represents a [service connection](../../abap-glossary/abenservice_connection_glosry.md) to an external database system.

- When instantiating the connection object, a name for the service connection must be defined. This name must start with *R/3\**.

- A connection object can be write-enabled for exactly one [logical external schema](../../abap-glossary/abencds_logical_schema_glosry.md). When instantiating the connection object, the name of the logical external schema that is to be write enabled must be specified.

For further details on ABAP SQL connection objects, see the topic [`IF_ABAP_SQL_CONNECTION`, ABAP SQL Connection Object](../../abap-programming-language/abap-database-access/abenif_abap_sql_connection.md).

For write access, a connection object that is write-enabled for a specific logical external schema must be specified using the addition [`CONNECTION`](../../abap-programming-language/abap-database-access/abapiumd_conn.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following external entity is defined as writable. It represents the remote database object `WRITABLE_2502`.

``` abap
@EndUserText.label: 'Demo CDS external entity'
define writable external entity DEMO_CDS_EXTERNAL_ENTITY_WRITE 
  external name "WRITABLE_2502"
{
    key SYSID       : abap.char(3) external name "K_SYSID";
    key K_USERNAME  : abap.char(12)       ;
    key K_VERI_ID   : abap.char(5)        ;
    key K_CHAR      : abap.char(10)       ;
        F_CLNT      : abap.char(3)       ;
        F_CUKY      : abap.cuky(5)        ;
        @Semantics.amount.currencyCode : 'F_CUKY' 
        F_CURR      : abap.curr(10,2)     ;
        F_DATS      : abap.dats           ;
        F_DEC       : abap.dec(10,2)      ;
        F_FLTP      : abap.fltp           ;
        F_INT1      : abap.int1           ;
        F_INT2      : abap.int2           ;
        F_INT4      : abap.int4           ;
        F_LANG      : abap.lang           ;
        F_NUMC      : abap.numc(10)       ;
        F_RAW       : abap.raw(10)        ;
        F_UNIT      : abap.unit(2)        ;
        @Semantics.quantity.unitOfMeasure : 'F_UNIT' 
        F_QUAN      : abap.quan(2,0)      ;
        F_TIMS      : abap.tims           ;
        F_RAWSTRING : abap.rawstring      ;
        F_SSTRING   : abap.sstring(16)    ;
        F_STRING    : abap.string         ;
        F_UTCL      : abap.utclong        ;
        F_DATN      : abap.datn           ;
        F_TIMN      : abap.timn           ;
        F_D16N      : abap.decfloat16     ;
        F_D34N      : abap.decfloat34     ;
        F_INT8      : abap.int8           ;
}
with federated data
provided at runtime
```

The logical external schema `DEMO_CDS_LES_WRITE_ACCESS` specifies the connection details to connect to an external system.

The ABAP SQL connection object that enables write access is generated as follows. The name of the [service connection](../../abap-glossary/abenservice_connection_glosry.md) is *R/3\*service* and the connection object write enables the logical external schema `DEMO_CDS_LES_WRITE_ACCESS`.

``` abap
FINAL(lo_con) = 
   cl_abap_sql_connection_builder=>write_enabled_4_logical_schema( 
      i_connection_name     = 'R/3*service' 
      i_logical_schema_name = 'DEMO_CDS_LES_WRITE_ACCESS' )->create( ).
```

To perform write operations on the remote object, a logical external schema must be specified using a [`PROVIDED BY`](../../abap-programming-language/abap-database-access/abapselect_data_source.md) clause. The ABAP SQL connection object for the same logical external schema must be specified after [`CONNECTION`](../../abap-programming-language/abap-database-access/abapiumd_conn.md). The changes are committed using a database commit for the specified database connection using [`COMMIT CONNECTION @con_ref`](../../abap-programming-language/abap-database-access/abapcommit_rollback_connection.md).

The following code snippet demonstrates how to manipulate data of the remote object using ABAP SQL.

``` abap
DATA(sys_date) = cl_demo_date_time=>get_system_date( ). 
DATA(sys_time) = cl_demo_date_time=>get_system_time( ). 
 
  "ABAP SQL Connection Object 
  "for the logical external schema DEMO_CDS_LES_WRITE_ACCESS 
 
FINAL(lo_con) = 
  cl_abap_sql_connection_builder=>write_enabled_4_logical_schema( 
  i_connection_name     = 'R/3*service' 
  i_logical_schema_name = 'DEMO_CDS_LES_WRITE_ACCESS' )->create( ). 
 
FINAL(ls_written) = VALUE demo_cds_external_entity_write( 
                      sysid      = sy-sysid 
                      k_username = sy-uname 
                      k_char     = 'DEMO' 
                      f_datn     = sys_date 
                      f_timn     = sys_time 
                      f_raw      = 'ABCDE0' ). 
 
 TRY. 
 
"Delete from remote source 
DELETE FROM demo_cds_external_entity_write 
  PROVIDED BY demo_cds_les_write_access 
  CONNECTION @lo_con. 
COMMIT CONNECTION @lo_con. 
 
"Insert a data record into remote source 
INSERT demo_cds_external_entity_write 
  PROVIDED BY demo_cds_les_write_access 
  CONNECTION @lo_con 
  FROM @ls_written. 
COMMIT CONNECTION @lo_con. 
 
"Update a data record 
UPDATE demo_cds_external_entity_write 
  PROVIDED BY demo_cds_les_write_access 
  CONNECTION @lo_con 
  SET k_username = 'UPDATE' 
  WHERE k_char = 'DEMO'. 
COMMIT CONNECTION @lo_con. 
 
"Inserting a data record using modify 
MODIFY demo_cds_external_entity_write 
  PROVIDED BY demo_cds_les_write_access 
  CONNECTION @lo_con 
  FROM @( VALUE #( sysid      = sy-sysid 
                   k_username = 'BLUB' 
                   k_char     = 'MODIFY' 
                   f_datn     = sys_date 
                   f_timn     = sys_time 
                   f_raw      = 'ABCDE0' ) ). 
COMMIT CONNECTION @lo_con. 
CATCH cx_dd_ee_asql_runtime INTO DATA(lx_dd_asql). 
ENDTRY.
```

**Note:** For the query to work, the CDS logical external schema must have a configuration for the current client in your local system. Otherwise, a runtime error occurs.

## More Information

- [Writable External Entities](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/51854921f45148f8bb4157fe8e16af48?version=sap_cross_product_abap) - ABAP Data Models guide (SAP Help Portal)
