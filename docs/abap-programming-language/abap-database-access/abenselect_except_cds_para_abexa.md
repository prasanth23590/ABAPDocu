---
title: "SELECT, Difference of CDS View Entity with Input Parameters"
source_file: abenselect_except_cds_para_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > UNION, INTERSECT, EXCEPT > EXCEPT, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, Difference of CDS View Entity with Input Parameters

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a difference of a CDS view with input parameters.

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
CLASS cl_demo_cds_parameters_except DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cds_parameters_except IMPLEMENTATION. 
  METHOD main. 
    DATA: 
      from_distance TYPE s_distance VALUE 0000, 
      to_distance   TYPE s_distance VALUE 1000. 
    cl_demo_input=>new( 
      )->add_field( CHANGING field = from_distance 
      )->add_field( CHANGING field = to_distance 
      )->request( ). 
 
    WITH 
      +union AS ( 
        SELECT carrid, connid, cityfrom, cityto, distance, distid 
               FROM demo_cds_parameters( p_distance_l = @from_distance, 
                                         p_distance_u = @to_distance, 
                                         p_unit       = 'MI' ) 
        UNION 
        SELECT carrid, connid, cityfrom, cityto, distance, distid 
               FROM demo_cds_parameters( p_distance_l = @from_distance, 
                                         p_distance_u = @to_distance, 
                                         p_unit       = 'KM' ) ) 
 
    SELECT carrid, connid, cityfrom, cityto, distance, distid 
           FROM +union 
    EXCEPT 
    SELECT carrid, connid, cityfrom, cityto, distance, distid 
           FROM demo_cds_parameters( p_distance_l = @from_distance, 
                                     p_distance_u = @to_distance, 
                                     p_unit       = 'KM' ) 
    ORDER BY distid, carrid, connid 
    INTO TABLE @FINAL(result). 
 
    out->write( result ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example uses a [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md) and two `SELECT` statements joined using [`EXCEPT`](abapunion.md) to access the following CDS view entity.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@Metadata.allowExtensions
@EndUserText.label: 'Demo f&#x00FC;r Parameter-View'
define view entity demo_cds_parameters
  with parameters
    p_distance_l :s_distance,
    p_distance_u :s_distance,
    p_unit       :s_distid
  as select from spfli
{
  key carrid,
  key connid,
      cityfrom,
      cityto,
      distance,
      distid
}
where
      distid   = $parameters.p_unit
  and distance between $parameters.p_distance_l and $parameters.p_distance_u;
```

This fills the input parameter `p_unit` with different values.
