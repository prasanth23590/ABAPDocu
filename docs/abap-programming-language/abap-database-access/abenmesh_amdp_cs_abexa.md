---
title: "AMDP - Filling a Mesh with SQLScript (Client-safe)"
source_file: abenmesh_amdp_cs_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Examples > AMDP - Examples (Client-safe)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - Filling a Mesh with SQLScript (Client-safe)

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how a mesh is filled with a database procedure. The AMDP method accesses [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) and the client is implicitly selected using the HANA session variable `CDS_CLIENT`. It is [client-safe](../../abap-glossary/abenclient_safe_glosry.md) by using the AMDP option [`CDS SESSION CLIENT DEPENDENT`](abapmethods_amdp_options_client.md).

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
CLASS cl_demo_amdp_filling_mesh_cs DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
        REDEFINITION . 
 
  PRIVATE SECTION. 
    TYPES: 
      BEGIN OF output_line, 
        position TYPE string, 
        product  TYPE string, 
      END OF output_line, 
      output TYPE STANDARD TABLE OF output_line WITH EMPTY KEY. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_amdp_filling_mesh_cs IMPLEMENTATION. 
  METHOD main. 
    DATA order_ids TYPE RANGE OF demo_cds_epm_salesorder-salesorder. 
    DATA(rows) = 1. 
    cl_demo_input=>new( )->request( EXPORTING text = `Orders` 
                                    CHANGING field = rows ). 
    SELECT 'I' AS sign, 'EQ' AS option, SalesOrder AS low 
           FROM demo_cds_epm_salesorder 
           ORDER BY low 
           INTO CORRESPONDING FIELDS OF TABLE @order_ids 
           UP TO @rows ROWS.                            "#EC CI_NOWHERE 
 
    TRY. 
        FINAL(order) = NEW cl_demo_amdp_mesh_cs( )->select( order_ids ). 
      CATCH cx_amdp_execution_error cx_amdp_version_error 
            cx_amdp_creation_error INTO FINAL(amdp_error). 
        out->write( amdp_error->get_text( ) ). 
        RETURN. 
    ENDTRY. 
 
    TRY. 
        LOOP AT order-orders ASSIGNING FIELD-SYMBOL(<order>). 
          out->begin_section( |Order #{ <order>-salesorder }| ). 
          ASSIGN order-orders\_buyers[ <order> ] 
            TO FIELD-SYMBOL(<buyer>). 
          IF sy-subrc <> 0. 
            out->write( 'Mismatch in data' ). 
            RETURN. 
          ENDIF. 
          out->begin_section( 
            |Buyer: { <buyer>-companyname } | && 
            |in { order-bupas\_addresses[ <buyer> ]-cityname } | ). 
          out->write( 
            name  = 'Sales Order Items' 
            data = VALUE output( 
              FOR <item> IN order-orders\_items[ <order> ] 
              ( position = <item>-salesorderitem 
                product = order-items\_products[ <item> ]-product 
              ) ) ). 
          out->end_section( )->end_section( ). 
        ENDLOOP. 
      CATCH cx_sy_itab_line_not_found. 
        out->write( 'Inconsistent data?' ). 
    ENDTRY. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The AMDP class `CL_DEMO_AMDP_MESH_CS` has a private AMDP method `SELECT_HDB` called by the public method `SELECT`.

The method fills the nodes of a [mesh](../abap-processing-internal-data/abenabap_meshes.md) for sales orders whose type is declared in the AMDP class. The number of sales orders is restricted using a ranges table. Subqueries are used that access local data.

### SQLScript Implementation of the AMDP Method

``` abap
METHOD select_hdb BY DATABASE PROCEDURE 
                  FOR HDB LANGUAGE SQLSCRIPT 
                  OPTIONS READ-ONLY 
                  USING demo_cds_epm_salesorder 
                        demo_cds_epm_salesorderitem 
                        demo_cds_epm_product 
                        demo_cds_epm_businesspartner 
                        demo_cds_epm_address. 
  orders = select * from DEMO_CDS_EPM_SALESORDER 
     where SalesOrder in ( 
      select low from :order_ids ); 
 
  bupas = select * from DEMO_CDS_EPM_BUSINESSPARTNER 
    where BusinessPartnerUUID in ( 
      select DISTINCT CustomerUUID from :orders ); 
 
  adresses = select * from DEMO_CDS_EPM_ADDRESS 
    where AddressUUID in ( 
      select AddressUUID from :bupas ); 
 
  items = select * from DEMO_CDS_EPM_SALESORDERitem 
    where SalesOrderUUID in ( select SalesOrderUUID from :orders ); 
 
  products = select * from DEMO_CDS_EPM_PRODUCT as product 
    where ProductUUID in ( 
      select distinct ProductUUID from :items ); 
ENDMETHOD.
```

## Hint

This is a syntax example for AMDP. The same function can be achieved with the same efficiency in ABAP SQL. AMDP is not needed in simple cases like this.
