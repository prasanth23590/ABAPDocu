---
title: "AMDP - Graph Processing (Client-safe)"
source_file: abenamdp_graph_cs_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Examples > AMDP - Examples (Client-safe)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - Graph Processing (Client-safe)

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [graph](../../abap-glossary/abengraph_glosry.md) processing using a [graph workspace](../../abap-glossary/abengraph_workspace_glosry.md) and a [graph procedure](../../abap-glossary/abengraph_procedure_glosry.md). The AMDP methods both use the addition `CDS SESSION CLIENT DEPENDENT` and are [client-safe](../../abap-glossary/abenclient_safe_glosry.md).

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
CLASS cl_demo_amdp_graph_proc_cs DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
        REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_amdp_graph_proc_cs IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( `Demo: Graph Processing` 
    )->write_doc( '<b>FRANKFURT -> ROME</b>' ). 
    TRY. 
        cl_demo_amdp_graph_cs=>get_shortest_path( 
          EXPORTING im_city_from = 'FRANKFURT' 
                    im_city_to   = 'ROME' 
          IMPORTING ex_weight    = DATA(lv_weight) 
                    ex_route     = DATA(lt_route) ). 
 
        out->write( lv_weight 
        )->write( lt_route ). 
 
      CATCH BEFORE UNWIND cx_amdp_execution_failed INTO DATA(lr_exc). 
        out->write_doc( |Exception raised!| 
        )->write_doc( lr_exc->sql_message ). 
    ENDTRY. 
 
    out->line( 
    )->write_doc( '<b>ROME -> MADRID</b>' ). 
    TRY. 
        cl_demo_amdp_graph_cs=>get_shortest_path( 
          EXPORTING im_city_from = 'ROME' 
                    im_city_to   = 'MADRID' 
          IMPORTING ex_weight    = lv_weight 
                    ex_route     = lt_route ). 
 
        out->write( lv_weight 
        )->write( lt_route ). 
 
      CATCH BEFORE UNWIND cx_amdp_execution_failed INTO lr_exc. 
        out->write_doc( |Exception raised!| 
        )->write_doc( lr_exc->sql_message ). 
    ENDTRY. 
 
    out->line( )->write_doc( '<b>MADRID -> ISTANBUL</b>' ). 
    TRY. 
        cl_demo_amdp_graph_cs=>get_shortest_path( 
          EXPORTING im_city_from = 'MADRID' 
                    im_city_to   = 'ISTANBUL' 
          IMPORTING ex_weight    = lv_weight 
                    ex_route     = lt_route ). 
 
        out->write( lv_weight 
        )->write( lt_route ). 
      CATCH BEFORE UNWIND cx_amdp_execution_failed INTO lr_exc. 
        out->write_doc( |Exception raised!| 
        )->write_doc( lr_exc->sql_message ). 
    ENDTRY. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example accesses a [graph procedure](../../abap-glossary/abengraph_procedure_glosry.md) that is declared and implemented in the [AMDP class](../../abap-glossary/abenamdp_class_glosry.md) `CL_DEMO_AMDP_GRAPH_CS`.

The method `GET_SHORTEST_PATH` is a [graph procedure](../../abap-glossary/abengraph_procedure_glosry.md) that refers to the [graph workspace](../../abap-glossary/abengraph_workspace_glosry.md) `CL_DEMO_AMDP_GRAPH_CS=>GRAPH_WORKSPACE` operating on a [graph](../../abap-glossary/abengraph_glosry.md) model which is a flight data model. The graph workspace includes the declaration of the [vertex table](../../abap-glossary/abenvertex_table_glosry.md) and the [edge table](../../abap-glossary/abenedge_table_glosry.md).

``` abap
METHOD graph_workspace BY DATABASE GRAPH WORKSPACE FOR HDB 
  LANGUAGE SQL 
  USING demo_cds_spfli4graph 
        demo_cds_sgeocity4graph. 
 
  edge table demo_cds_spfli4graph 
    source column cityfrom 
    target column cityto 
    key    column connid 
  vertex table demo_cds_sgeocity4graph 
    key    column city 
ENDMETHOD.
```

The graph procedure is a read-only procedure that is written in [GraphScript](../../abap-glossary/abengraphscript_glosry.md). Its purpose is to return the shortest flight connection between two cities (representing two [vertices](../../abap-glossary/abenvertex_glosry.md)). The parameter `ex_weight` returns the overall flight time, and the parameter `ex_route` returns the a table showing some details of the round trip.

``` abap
METHOD get_shortest_path BY DATABASE PROCEDURE FOR HDB 
  LANGUAGE GRAPH 
  OPTIONS READ-ONLY 
  USING cl_demo_amdp_graph_cs=>graph_workspace. 
 
  Graph g = Graph ("CL_DEMO_AMDP_GRAPH_CS=>GRAPH_WORKSPACE"); 
 
  Vertex v_from = Vertex (:g, :im_city_from); 
  Vertex v_to   = Vertex (:g, :im_city_to); 
 
 
  WeightedPath<BigInt> p_path = Shortest_Path (:g, :v_from, :v_to 
    ,(Edge flight) => 
     BigInt 
     { 
       return BigInt( :flight.fltime ); 
     }  --optional weight 
  ); 
 
  --Multiset<Vertex> neighborhood = Neighbors (:g, :v_from, 1, -1); 
 
  ex_weight = Weight (:p_path); 
  ex_route  = select :part.connid, :part.cityfrom, :part.cityto, :part.fltime 
              foreach part in Edges( :p_path ); 
 
ENDMETHOD.
```

The example shows that the first method call is fine. The second method call does not show any data because the target city is not contained in the graph model. The third method call shows the message that is raised. In this case, neither of the two cities is contained in the graph model
