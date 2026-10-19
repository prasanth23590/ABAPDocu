---
title: "ABAP SQL, Parameter Passing to a CDS View Entity"
source_file: abenselect_cds_para_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Parameter Passing sql_para"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL, Parameter Passing to a CDS View Entity

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a read performed on a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) using parameter passing.

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
CLASS cl_demo_cds_param_view_entity DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cds_param_view_entity IMPLEMENTATION. 
  METHOD main. 
    DATA: 
      from_distance TYPE s_distance VALUE 2000, 
      to_distance   TYPE s_distance VALUE 6000, 
      unit          TYPE s_distid   VALUE 'MI'. 
    cl_demo_input=>new( 
      )->add_field( CHANGING field = from_distance 
      )->add_field( CHANGING field = to_distance 
      )->add_field( CHANGING field = unit 
      )->request( ). 
 
    SELECT * 
           FROM demo_cds_param_view_entity( 
             p_distance_l = @from_distance, 
             p_distance_u = @to_distance, 
             p_unit       = @unit ) 
           ORDER BY carrid, connid 
           INTO TABLE @FINAL(result). 
    out->write( result ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

[`SELECT`](abapselect.md) is used to access a CDS view entity with parameters as a [data source](abapselect_data_source.md). Actual parameters are assigned to the input parameters of the view. The values of these actual parameters are defined via user input.

The view `demo_cds_param_view_entity` used has the following CDS source code with a [list of input parameters](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_parameter_list_v2.md):

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'View Entity with Input Parameters'
define view entity Demo_Cds_Param_View_Entity 
   with parameters
    p_distance_l :s_distance,
    p_distance_u :s_distance,
    p_unit       :s_distid
  as select from
    spfli
    {
      key carrid,
      key connid,
          cityfrom,
          cityto,
          distance,
          distid          
    }
    where
          distid   =       $parameters.p_unit
      and distance between $parameters.p_distance_l 
                       and $parameters.p_distance_u;        
```

Those rows are read from the DDIC database table `SPFLI` for which the distance in the transferred unit lies between the two passed values.
