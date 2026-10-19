---
title: "AMDP - Graph Processing"
source_file: abenamdp_hdb_graph.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Methods > METHOD, BY DATABASE PROCEDURE, FUNCTION, GRAPH WORKSPACE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - Graph Processing

[AMDP](../../abap-glossary/abenamdp_glosry.md) supports two [SAP HANA](../../abap-glossary/abensap_hana_glosry.md) artifacts for processing [graphs](../../abap-glossary/abengraph_glosry.md):

- [Graph workspaces](../../abap-glossary/abengraph_workspace_glosry.md)

- [Graph procedures](../../abap-glossary/abengraph_procedure_glosry.md)

Graph workspaces can be consumed by [graph procedures](../../abap-glossary/abengraph_procedure_glosry.md) using [GraphScript](../../abap-glossary/abengraphscript_glosry.md) which is the implementation language of an [AMDP method](abenamdp_methods.md) that specifies the addition [`FOR HDB LANGUAGE GRAPH`](abapmethod_by_db_proc.md) in the `METHOD` statement. In contrast to [AMDP procedures](../../abap-glossary/abenamdp_procedure_glosry.md) and [AMDP functions](../../abap-glossary/abenamdp_function_glosry.md), methods in this context operate on non-procedural database objects ([DDL objects](../../abap-glossary/abenddl_object_glosry.md)).

## More Information

[SAP HANA Graph Reference](https://help.sap.com/docs/SAP_HANA_PLATFORM/f381aa9c4b99457fb3c6b53a2fd29c02/f7093581a9284c59a85122a7955749f4)

## Graph Workspace

Graph workspaces are created in [AMDP methods](../../abap-glossary/abenamdp_method_glosry.md) that declare a [vertex table](../../abap-glossary/abenvertex_table_glosry.md) and an [edge table](../../abap-glossary/abenedge_table_glosry.md) as sources for a [graph](../../abap-glossary/abengraph_glosry.md) model.

The declaration consists of the key column of a vertex table ([vertex key](../../abap-glossary/abenvertex_key_glosry.md)) and the key column of an edge table ([edge key](../../abap-glossary/abenedge_key_glosry.md)), as well as a source and a target column of an edge table. Currently, graph workspaces are restricted to one key column, and one source and target column.

**Note:** Graph workspaces cannot be mocked during a syntax check. There is no separate signature available. Instead, the complete [database object](../../abap-glossary/abendb_object_glosry.md) must be created. It might be defined in a different [AMDP class](../../abap-glossary/abenamdp_class_glosry.md) and use other [AMDP](../../abap-glossary/abenamdp_glosry.md) objects. Hence, a special handling is needed, and implementation details from other classes must be used (transitive syntax check).

**Definition and implementation of a graph workspace**

The following code snippets are taken from the example [AMDP - Graph Processing](abenamdp_graph_cs_abexa.md).

Definition:

The method definition must include the addition [`FOR DDL OBJECT`](abapclass-methods_for_ddl_object.md).

``` abap
`CLASS-METHODS graph_workspace FOR DDL OBJECT 
        OPTIONS CDS SESSION CLIENT DEPENDENT.`
```

Implementation:

The `METHOD` statement includes the addition `BY DATABASE GRAPH WORKSPACE`. Currently, only [CDS views](../../abap-glossary/abencds_view_glosry.md) are allowed after the addition `USING`. The declaration of the vertex table and edge table is included automatically. The declaration consists of the key column of a vertex table ([vertex key](../../abap-glossary/abenvertex_key_glosry.md)) and the key column of an edge table ([edge key](../../abap-glossary/abenedge_key_glosry.md)), as well as a source and a target column of an edge table. Currently, graph workspaces are restricted to one key column, and one source and destination column.

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

## Graph Procedure

[Graph procedures](../../abap-glossary/abengraph_procedure_glosry.md) are methods that refer to [graph workspaces](../../abap-glossary/abengraph_workspace_glosry.md) and operate on [graph](../../abap-glossary/abengraph_glosry.md) models. Graph procedures may have scalar input parameters and scalar or tabular output parameters. Inconsistencies in the underlying vertex and edge tables may result in runtime errors (`CX_AMDP_EXECUTION_FAILED`), for example, if the edge source or target do not exist in the vertex table.

**Definition and implementation of a graph procedure**

The following code snippets are taken from the example [AMDP - Graph Processing](abenamdp_graph_cs_abexa.md).

Definition:

The example shows scalar-only importing parameters. The exporting parameters are both scalar and tabular.

``` abap
`CLASS-METHODS get_shortest_path 
      AMDP OPTIONS CDS SESSION CLIENT DEPENDENT 
      IMPORTING VALUE(im_city_from) TYPE demo_cds_spfli4graph-cityfrom 
                VALUE(im_city_to)   TYPE demo_cds_spfli4graph-cityto 
      EXPORTING VALUE(ex_weight)    TYPE int8 
                VALUE(ex_route)     TYPE tt_conn 
      RAISING   cx_amdp_execution_failed.`
```

Implementation:

The `METHOD` statement includes the addition `FOR HDB LANGUAGE GRAPH` to denote that the implementation contains [GraphScript](../../abap-glossary/abengraphscript_glosry.md) code. The `READ-ONLY` addition is mandatory. The `USING` addition must be followed by a graph workspace.

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

### Executable Example

The example [AMDP - Graph Processing](abenamdp_graph_cs_abexa.md) demonstrates graph processing using a graph workspace and a graph procedure.
