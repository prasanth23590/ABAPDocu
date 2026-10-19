---
title: "CDS DDL - DEFINE CUSTOM ENTITY, Implementing a Custom Query"
source_file: abencds_custom_query_abexa.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Custom Entities > CDS DDL - DEFINE CUSTOM ENTITY > CDS DDL - DEFINE CUSTOM ENTITY, ABAP Class"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE CUSTOM ENTITY, Implementing a Custom Query

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how an ABAP method can be used for data provisioning in a CDS custom entity.

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
CLASS cl_demo_consume_bs_cstm_query DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_consume_bs_cstm_query IMPLEMENTATION. 
  METHOD main. 
    FINAL(service_binding) = `DEMO_SB_CUSTOM_QUERY`. 
    FINAL(entity)          = `DEMO_CDS_CUSTOM_ENTITY`. 
 
    DATA(p_number) = `10`. 
    cl_demo_input=>new( 
       )->add_field( CHANGING field = p_number 
       )->request( ). 
    IF p_number CN '0123456789' OR p_number < 1 OR p_number > 100. 
      out->write( 'Enter a number between 1 and 100' ). 
      RETURN. 
    ENDIF. 
 
    TRY. 
        cl_demo_bs_consumption=>new( service_binding )->odata_to_itab( 
          EXPORTING 
            parameters      = VALUE #( ( p_number ) ) 
          IMPORTING 
            itab            = FINAL(itab) ). 
      CATCH cx_demo_bs_consumption INTO FINAL(exc). 
        out->write_text( exc->get_text( ) ). 
        RETURN. 
    ENDTRY. 
 
    out->write( itab->* ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The CDS custom entity `DEMO_CDS_CUSTOM_ENTITY` is bound to the ABAP class `CL_DEMO_CUSTOM_ENTITY_QUERY`. This class implements the interface `IF_RAP_QUERY_PROVIDER` and generates an internal table with newly created UUID values. The number of UUID values can be passed as parameter.

The example accesses the CDS custom entity `DEMO_CDS_CUSTOM_ENTITY` and fills it with data using the [service binding](../../abap-glossary/abenservice_binding_glosry.md) `DEMO_SB_CUSTOM_QUERY`, which binds the service definition `DEMO_SD_CUSTOM_ENTITY` to an OData node in ICF. This is done using the demonstration class `CL_DEMO_BS_CONSUMPTION`, which accesses the OData service of the service binding by using an ICF client.

Class `CL_DEMO_BS_CUSTOM_QUERY_URL` displays a URL that can be copied and pasted to a web browser in order to display the OData data in XML or JSON format.

It should be noted that no data is queried from the database in this example and that the data is generated from ABAP only.
