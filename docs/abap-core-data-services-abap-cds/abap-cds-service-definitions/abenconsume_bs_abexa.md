---
title: "ABAP CDS - Consuming Business Services with Demo Class"
source_file: abenconsume_bs_abexa.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Service Definitions > ABAP CDS - Consuming Business Services"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Consuming Business Services with Demo Class

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how the OData data of business services can be consumed in ABAP with a demonstration class.

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
CLASS cl_demo_consume_bs_simple DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_consume_bs_simple IMPLEMENTATION. 
  METHOD main. 
    DATA(service_binding) = `demo_sb_scarr_spfli`. 
    DATA(entity)          = `demo_cds_scarr_spfli`. 
    DATA(limit)           =  50. 
    cl_demo_input=>new( 
       )->add_field( CHANGING field = service_binding 
       )->add_field( CHANGING field = entity 
       )->add_field( CHANGING field = limit 
       )->request( ). 
    IF limit < 1 OR limit > 1000. 
      out->write( 'Enter a number between 1 and 1000' ). 
      RETURN. 
    ENDIF. 
 
    TRY. 
        cl_demo_bs_consumption=>new( service_binding )->odata_to_itab( 
          EXPORTING 
            entity          = entity 
            limit           = limit 
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

Business services are designed mainly for accessing AS ABAP from outside, however for demonstration purposes here, an ICF client implemented in ABAP is used to read the ICF nodes of business services. The ICF client is implemented in the class `CL_DEMO_BS_CONSUMPTION` that offers some methods for examining the OData data of [service bindings](../../abap-glossary/abenservice_binding_glosry.md) whose names are passed by parameter:

- Several methods are available for reading URLs for use in browsers.

- One method reads the non-handled OData data in XML or JSON format.

- One method extracts important metadata to internal tables.

- One method extracts the actual data to internal tables.

The class `CL_DEMO_CONSUME_BS_SIMPLE` shown above uses the class to extract the data of individual CDS entities exposed in service definitions to internal tables and display it. The class `CL_DEMO_BS_SIMPLE_URL` displays a URL that can be copied and pasted to a web browser in order to display the OData data in XML or JSON format.

Further example classes are:

- `CL_DEMO_BS_URLS` gets the URLs of service bindings.

- `CL_DEMO_BS_ODATA` gets the unhandled OData data of service bindings.

- `CL_DEMO_BS_META_DATA` gets important metadata as the content of internal tables.

- `CL_DEMO_CONSUME_BS_WITH_PARAMS` demonstrates parameter passing to exposed CDS entities with input parameters.

- `CL_DEMO_CONSUME_BS_WITH_ASSOCS` demonstrates how paths are specified for exposed CDS entities joined using associations.

The defaults for the input parameters of the class access service definitions and service bindings that were created for these demonstrations. These service bindings use the OData protocol (version 2) for [Web APIs](../../abap-glossary/abenweb_api_glosry.md).
