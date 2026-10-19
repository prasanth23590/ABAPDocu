---
title: "Client-Dependent CDS Table Function (Client-safe)"
source_file: abencds_func_client_dep_cs_abexa.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Table Functions > ABAP CDS - Client Handling in CDS Table Functions > ABAP CDS - CDS Table Function Client Handling Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Client-Dependent CDS Table Function (Client-safe)

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates client-dependent CDS table functions that are [client-safe](../../abap-glossary/abenclient_safe_glosry.md) and suited for [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md).

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_cds_functions_clnt_cs DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
      REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cds_functions_clnt_cs IMPLEMENTATION. 
  METHOD main. 
    DATA carrid TYPE s_carr_id VALUE 'LH'. 
    cl_demo_input=>new( )->request( CHANGING field = carrid ). 
    carrid = to_upper( carrid ). 
 
    SELECT * 
           FROM demo_cds_get_scarr_spfli_cs( carrid = @carrid ) 
           INTO TABLE @DATA(result_cds) 
           ##db_feature_mode[amdp_table_function]. 
 
    SELECT * 
           FROM demo_cds_get_scarr_spfli_dd_cs( carrid = @carrid ) 
           INTO TABLE @DATA(result_ddic) 
           ##db_feature_mode[amdp_table_function]. 
 
    ASSERT result_cds = result_ddic. 
 
    out->write( result_cds ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example class accesses the [client-dependent](abencds_func_client_handling.md) [CDS table function](../../abap-glossary/abencds_table_function_glosry.md) `DEMO_CDS_GET_SCARR_SPFLI_CS` that is [client-safe](../../abap-glossary/abenclient_safe_glosry.md). Client safety is enforced by the annotation [`ClientHandling.clientSafe`](../abap-cds-annotations/abencds_1549616294_anno.md) and the annotation [`ClientHandling.algorithm`](../abap-cds-annotations/abencds_1114072352_anno.md) must be used with the value `#SESSION_VARIABLE`. There is no input parameter of dictionary type `CLNT`. The implementing AMDP class `CL_DEMO_AMDP_FUNCTIONS_CS` has language version [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md) and is also client-safe.

``` abap
@AccessControl.authorizationCheck: #NOT_ALLOWED
@ClientHandling.type: #CLIENT_DEPENDENT
@ClientHandling.algorithm: #SESSION_VARIABLE
@ClientHandling.clientSafe: true
define table function DEMO_CDS_GET_SCARR_SPFLI_CS
  with parameters
    carrid :s_carr_id
returns
{
  client   :s_mandt;
  carrname :s_carrname;
  connid   :s_conn_id;
  cityfrom :s_from_cit;
  cityto   :s_to_city;
}
implemented by method
  CL_DEMO_AMDP_FUNCTIONS_CS=>GET_SCARR_SPFLI_FOR_CDS;
```

Another CDS table function `DEMO_CDS_GET_SCARR_SPFLI_DD_CS` does exactly the same, but is implemented by another method of the same AMDP class that accesses DDIC database tables instead of CDS view entities in a client safe way.
