---
title: "ABAP SQL - Working with Hierarchies"
source_file: abenabap_sql_hiera_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Working with Hierarchies

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example summarizes the functions ABAP SQL offers together with ABAP CDS for working with [hierarchical data](../../abap-glossary/abenhierarchy_glosry.md) that is stored in database tables by using [parent-child relationships](../../abap-glossary/abenpcr_glosry.md) defined by [hierarchy associations](../../abap-glossary/abenhierarchy_association_glosry.md).

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
CLASS cl_demo_sql_hierarchies DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    TYPES: 
      BEGIN OF value, 
        id     TYPE i, 
        amount TYPE p LENGTH 16 DECIMALS 2, 
      END OF value. 
    DATA 
      value_tab TYPE SORTED TABLE OF value WITH UNIQUE KEY id. 
    DATA 
      rnd TYPE REF TO cl_abap_random_int. 
    METHODS: 
      fill_table, 
      get_root_id RETURNING VALUE(root_id) TYPE i. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_sql_hierarchies IMPLEMENTATION. 
  METHOD main. 
    fill_table( ). 
 
    FINAL(root_id) =  get_root_id( ) / 10 + 1. 
 
    out->begin_section( `SQL Hierarchies in ABAP SQL` 
      )->begin_section( `CDS Artefacts` 
      )->begin_section( `CDS Source` 
      )->write_doc( cl_demo_output_helper=>get_ddls_source_code_html( 
                      source = 'DEMO_CDS_SIMPLE_TREE_VIEW' ) 
      )->next_section( `CDS Hierarchy` 
      )->write_doc( cl_demo_output_helper=>get_ddls_source_code_html( 
                      source = 'DEMO_CDS_SIMPLE_TREE' ) 
      )->end_section( )->end_section( 
      )->begin_section( `Hierarchies as Data Source in the FROM clause` 
      )->begin_section( `Using a CDS Hierarchy` 
      )->begin_code( `cds` ). 
 
    SELECT FROM demo_cds_simple_tree( p_id = @root_id ) "hierarchy 
           FIELDS id, 
                  parent, 
                  name, 
                  hierarchy_rank, 
                  hierarchy_tree_size, 
                  hierarchy_parent_rank, 
                  hierarchy_level, 
                  hierarchy_is_cycle, 
                  hierarchy_is_orphan, 
                  node_id, 
                  parent_id 
           INTO TABLE @FINAL(cds_result). 
 
    out->end_code( `cds` 
       )->write( cds_result ). 
 
    IF lines( cds_result ) < 10 OR lines( cds_result ) > 20. 
      CLEAR value_tab. 
      me->main(  ). 
      RETURN. 
    ENDIF. 
 
    out->next_section( `Using the Hierarchy Generator` 
      )->begin_section( `Source CDS View` 
      )->begin_code( `asql_cds` ). 
 
    SELECT FROM HIERARCHY( SOURCE demo_cds_simple_tree_view 
                           CHILD TO PARENT ASSOCIATION _tree 
                           START WHERE id = @root_id 
                           SIBLINGS ORDER BY id 
                           MULTIPLE PARENTS NOT ALLOWED ) "hierarchy 
           FIELDS id, 
                  parent, 
                  name, 
                  hierarchy_rank, 
                  hierarchy_tree_size, 
                  hierarchy_parent_rank, 
                  hierarchy_level, 
                  hierarchy_is_cycle, 
                  hierarchy_is_orphan, 
                  node_id, 
                  parent_id 
           INTO TABLE @FINAL(asql_cds_result). 
 
    ASSERT asql_cds_result = cds_result. 
 
    out->end_code( `asql_cds` 
      )->next_section( `Source CTE` 
      )->begin_code( `asql_cte` ). 
 
    WITH 
      +cte_simple_tree_source AS 
         ( SELECT FROM demo_simple_tree 
                  FIELDS id, 
                         parent_id AS parent, 
                         name ) 
            WITH ASSOCIATIONS ( 
              JOIN MANY TO MANY +cte_simple_tree_source AS _tree 
                ON +cte_simple_tree_source~parent = _tree~id ) 
      SELECT FROM HIERARCHY( SOURCE +cte_simple_tree_source 
                             CHILD TO PARENT ASSOCIATION _tree 
                             START WHERE id = @root_id 
                             SIBLINGS ORDER BY id 
                             MULTIPLE PARENTS NOT ALLOWED ) "hierarchy 
             FIELDS id, 
                    parent, 
                    name, 
                    hierarchy_rank, 
                    hierarchy_tree_size, 
                    hierarchy_parent_rank, 
                    hierarchy_level, 
                    hierarchy_is_cycle, 
                    hierarchy_is_orphan, 
                    node_id, 
                    parent_id 
             INTO TABLE @FINAL(asql_cte_result). 
 
    ASSERT asql_cte_result = cds_result. 
 
    out->end_code( `asql_cte` 
      )->end_section( 
      )->next_section( `Using a CTE Hierarchy` 
      )->begin_section( `Source CDS Hierarchy` 
      )->begin_code( `cte_cds` ). 
 
    WITH 
      +tree AS 
        ( SELECT FROM demo_cds_simple_tree( p_id = @root_id ) 
                 FIELDS * ) 
          WITH HIERARCHY demo_cds_simple_tree 
      SELECT FROM  +tree "hierarchy 
             FIELDS id, 
                    parent, 
                    name, 
                    hierarchy_rank, 
                    hierarchy_tree_size, 
                    hierarchy_parent_rank, 
                    hierarchy_level, 
                    hierarchy_is_cycle, 
                    hierarchy_is_orphan, 
                    node_id, 
                    parent_id 
             INTO TABLE @FINAL(cte_cds_result). 
 
    ASSERT cte_cds_result  = cds_result. 
 
    out->end_code( `cte_cds` 
      )->next_section( `Source Hierarchy Generator` 
      )->begin_code( `cte_asql`  ). 
 
    WITH 
      +tree AS 
        ( SELECT FROM HIERARCHY( 
            SOURCE demo_cds_simple_tree_view 
            CHILD TO PARENT ASSOCIATION _tree 
            START WHERE id = @root_id 
            SIBLINGS ORDER BY id 
            MULTIPLE PARENTS NOT ALLOWED ) AS asql_hierarchy 
            FIELDS id, 
                   parent, 
                   name ) 
          WITH HIERARCHY asql_hierarchy 
      SELECT FROM +tree "hierarchy 
             FIELDS id, 
                    parent, 
                    name, 
                    hierarchy_rank, 
                    hierarchy_tree_size, 
                    hierarchy_parent_rank, 
                    hierarchy_level, 
                    hierarchy_is_cycle, 
                    hierarchy_is_orphan, 
                    node_id, 
                    parent_id 
             INTO TABLE @FINAL(cte_asql_result). 
 
    ASSERT cte_asql_result = cds_result. 
 
    out->end_code( `cte_asql` 
      )->next_section( `Source CTE` 
      )->begin_code( `cte_cte` ). 
 
    WITH 
      +cte_simple_tree_source AS 
        ( SELECT FROM demo_simple_tree 
                 FIELDS id, 
                        parent_id AS parent, 
                        name ) 
           WITH ASSOCIATIONS ( 
             JOIN MANY TO MANY +cte_simple_tree_source AS _tree 
               ON +cte_simple_tree_source~parent = _tree~id ), 
      +tree AS 
        ( SELECT FROM HIERARCHY( 
            SOURCE +cte_simple_tree_source 
            CHILD TO PARENT ASSOCIATION _tree 
            START WHERE id = @root_id 
            SIBLINGS ORDER BY id 
            MULTIPLE PARENTS NOT ALLOWED ) AS cte_hierarchy 
            FIELDS id, 
                   parent, 
                   name  ) 
            WITH HIERARCHY cte_hierarchy 
      SELECT FROM +tree "hierarchy 
             FIELDS id, 
                    parent, 
                    name, 
                    hierarchy_rank, 
                    hierarchy_tree_size, 
                    hierarchy_parent_rank, 
                    hierarchy_level, 
                    hierarchy_is_cycle, 
                    hierarchy_is_orphan, 
                    node_id, 
                    parent_id 
             INTO TABLE @FINAL(cte_cte_result). 
 
    ASSERT cte_cte_result = cds_result. 
 
    out->end_code( `cte_cte` 
      )->end_section( 
      )->end_section( 
      )->next_section( `Hierarchy Navigators` 
      )->begin_section( `HIERARCHY_DESCENDANTS` ). 
 
    "Get the ID of the second longest subtree 
    SELECT FROM demo_cds_simple_tree( p_id = @root_id ) AS h 
           FIELDS id 
           ORDER BY hierarchy_tree_size DESCENDING 
           INTO TABLE @FINAL(sub_ids) 
           UP TO 1 ROWS OFFSET 1. 
    FINAL(sub_id) = sub_ids[ 1 ]-id. 
 
    out->begin_code( `descendants` ). 
 
    SELECT FROM HIERARCHY_DESCENDANTS( 
                  SOURCE demo_cds_simple_tree( p_id = @root_id ) 
                  START WHERE id = @sub_id  ) 
      FIELDS id, 
             parent_id, 
             name, 
             hierarchy_distance 
      INTO TABLE @FINAL(descendants). 
 
    out->end_code( `descendants` 
      )->write( descendants 
      )->next_section( `HIERARCHY_ANCESTORS` ). 
 
    "Get the ID of the longest path 
    SELECT SINGLE FROM demo_cds_simple_tree( p_id = @root_id ) 
           FIELDS id 
           WHERE hierarchy_level = ( 
             SELECT FROM demo_cds_simple_tree( p_id = @root_id ) 
                    FIELDS MAX( hierarchy_level ) AS max_level ) 
           INTO (@FINAL(max_id)). 
 
    out->begin_code( `ancestors` ). 
 
    SELECT FROM HIERARCHY_ANCESTORS( 
                  SOURCE demo_cds_simple_tree( p_id = @root_id ) 
                  START WHERE id = @max_id ) 
      FIELDS id, 
              parent_id, 
              name, 
              hierarchy_distance 
      INTO TABLE @FINAL(ancestors). 
 
    out->end_code( `ancestors` 
      )->write( ancestors 
      )->next_section( `HIERARCHY_SIBLINGS` ). 
 
    "Get the ID of a node with the most siblings 
    SELECT FROM demo_cds_simple_tree( p_id = @root_id ) 
           FIELDS hierarchy_parent_rank AS rank, 
                  COUNT( hierarchy_parent_rank ) AS rank_count 
           GROUP BY hierarchy_parent_rank 
           ORDER BY rank_count DESCENDING 
           INTO TABLE @FINAL(rank_counts) 
           UP TO 1 ROWS. 
    FINAL(sibl_id) = 
      cds_result[ hierarchy_parent_rank = rank_counts[ 1 ]-rank ]-id. 
 
    out->begin_code( `siblings` ). 
 
    SELECT FROM HIERARCHY_SIBLINGS( 
                  SOURCE demo_cds_simple_tree( p_id = @root_id ) 
                  START WHERE id = @sibl_id ) 
      FIELDS id, 
              parent_id, 
              name, 
              hierarchy_sibling_distance 
      INTO TABLE @FINAL(siblings). 
 
    out->end_code( `siblings` 
      )->write( siblings 
      )->next_section( `HIERARCHY_DESCENDANTS_AGGREGATE` 
      )->begin_code( `descendants_aggregate` ). 
 
    SELECT FROM HIERARCHY_DESCENDANTS_AGGREGATE( 
                  SOURCE demo_cds_simple_tree( p_id = @sub_id  ) AS h 
                  JOIN @value_tab AS v 
                    ON  v~id = h~id 
                  MEASURES SUM( v~amount ) AS amount_sum 
                  WHERE hierarchy_rank > 1 
                  WITH SUBTOTAL 
                  WITH BALANCE ) 
      FIELDS id, 
             amount_sum, 
             hierarchy_rank, 
             hierarchy_aggregate_type 
      INTO TABLE @FINAL(descendants_aggregate). 
 
    out->end_code( `descendants_aggregate` 
      )->write( descendants_aggregate ). 
 
    SELECT FROM HIERARCHY_DESCENDANTS( 
                  SOURCE demo_cds_simple_tree( p_id = @sub_id  ) 
                  START WHERE id = @sub_id  ) AS h 
                  LEFT OUTER JOIN @value_tab AS v 
                     ON  v~id = h~id 
           FIELDS  h~id, 
                   h~parent_id, 
                   v~amount, 
                   hierarchy_rank 
    INTO TABLE @FINAL(join). 
    out->write( join ). 
 
    ASSERT 
      descendants_aggregate[ hierarchy_aggregate_type  = 1 ]-amount_sum 
        = REDUCE value-amount( 
            INIT s TYPE decfloat34 
            FOR <v> IN join WHERE ( hierarchy_rank > 1 ) 
             NEXT s += <v>-amount ). 
 
    ASSERT 
      descendants_aggregate[ hierarchy_aggregate_type  = 2 ]-amount_sum 
        = join[ hierarchy_rank = 1 ]-amount. 
 
    DELETE FROM demo_simple_tree. "GTT must be deleted 
  ENDMETHOD. 
  METHOD fill_table. 
    DATA tree_tab TYPE TABLE OF demo_simple_tree WITH EMPTY KEY. 
    tree_tab = VALUE #( 
        ( id = 1  parent_id = 0 name = '1'  ) 
        ( id = 2  parent_id = 0 name = '2'  ) 
        ( id = 3  parent_id = 0 name = '3'  ) 
        ( id = 4  parent_id = 0 name = '4'  ) 
        ( id = 5  parent_id = 0 name = '5'  ) 
        ( id = 6  parent_id = 0 name = '6'  ) 
        ( id = 7  parent_id = 0 name = '7'  ) 
        ( id = 8  parent_id = 0 name = '8'  ) 
        ( id = 9  parent_id = 0 name = '9'  ) 
        ( id = 10 parent_id = 0 name = '10' ) ). 
 
    DATA(id) = 10. 
    DO. 
      FINAL(parent_id) = rnd->get_next( ). 
      IF line_exists( tree_tab[ id = parent_id ] ). 
        id += 1. 
        tree_tab = VALUE #( BASE tree_tab ( 
          id        =  id 
          parent_id = parent_id 
          name      = tree_tab[ id = parent_id ]-name && `-` && id ) ). 
      ENDIF. 
      IF id > 1000. 
        EXIT. 
      ENDIF. 
    ENDDO. 
 
    DELETE FROM demo_simple_tree. 
    INSERT demo_simple_tree FROM TABLE @tree_tab. 
 
    DATA value_rnd TYPE REF TO cl_abap_random_int. 
    value_rnd = cl_abap_random_int=>create( 
          seed = CONV #( cl_demo_date_time=>get_system_time( ) ) 
          min  = 1 
          max  = 100 ). 
    LOOP AT tree_tab ASSIGNING FIELD-SYMBOL(<node>). 
      value_tab = VALUE #( BASE value_tab ( 
        id = <node>-id 
        amount = 
          value_rnd->get_next( ) / value_rnd->get_next( ) * 100 ) ). 
    ENDLOOP. 
 
  ENDMETHOD. 
  METHOD get_root_id. 
    DO. 
      root_id = rnd->get_next( ). 
      SELECT SINGLE 'X' 
             FROM demo_simple_tree 
             WHERE id = @root_id 
             INTO @FINAL(id_exists). 
      IF sy-subrc = 0. 
        EXIT. 
      ENDIF. 
    ENDDO. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    rnd = cl_abap_random_int=>create( 
      seed = CONV #( cl_demo_date_time=>get_system_time( ) ) 
      min  = 1 
      max  = 1000 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Hierarchical data in database tables means that lines of one or more database tables are connected by [parent-child relationships](../../abap-glossary/abenpcr_glosry.md). There are many use cases where hierarchical data plays a role and where accessing information about the hierarchical relationship is important. For example, a common task can be to find out the descendants or ancestors of a given hierarchy node or to aggregate values of subtrees.

## Overview

In former times you had to load the data from the database into internal tables and program it all by yourself (if you did not find an appropriate API). In between, [meshes](../../abap-glossary/abenmesh_glosry.md) offered some features for working with hierarchies, as shown in this [example](../abap-processing-internal-data/abenmesh_for_reflex_sngl_abexa.md), but have not found wide distribution.

Meanwhile, the standard AS ABAP database is a SAP HANA database that offers a lot of helpful features. Among other things, you will find a set of hierarchy functions there that allow you to deal with hierarchical data directly on the database and that you can look up in the [SAP HANA documentation](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/b4b0eec1968f41a099c828a4a6c8ca0f). Now you might expect that you must use [AMDP](abenamdp.md) in order to access these functions from your ABAP programs, but no need to do so! ABAP SQL and ABAP CDS support hierarchies directly by wrapping the HANA built-in functions without any loss of performance. You can stay in the comfortable ABAP world and nevertheless have access to most modern features. All you have to do, is to understand some concepts and learn some additional syntax and then you can start right away.

## SQL Hierarchies

With [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) we denote a special [hierarchical data source](abenselect_hierarchy_data.md) that you can use in the `FROM` clause of ABAP SQL queries. A SQL hierarchy is a tabular set of rows which form the hierarchy nodes of a hierarchy and which contains additionally [hierarchy columns](../../abap-glossary/abenhierarchy_column_glosry.md) that contain hierarchy attributes with hierarchy-specific information for each row. For creating a SQL hierarchy, you need the following:

- **Data Source**

  This can be any data source you can access normally in an ABAP SQL query, as most commonly a database table or a CDS view, but also a CTE (common table expression). The structure and content of the data source should be able to represent hierarchical data.

- **Parent-Child Relation**

  A parent-child relation must be defined between two or more columns of the data source. From the parent-child relation and the actual data of the data source, the SQL hierarchy consisting of parent nodes and child nodes can be created. The parent-child relation must be defined by a self-association which we call hierarchy association. This can be achieved with CDS associations or CTE associations. A data source exposing a hierarchy association can be used as a hierarchy source for creating a SQL hierarchy.

- **Hierarchy Creation**

  From a hierarchy source, that is a data source exposing a hierarchy association, a SQL hierarchy can be created. This can be done either by defining a CDS hierarchy outside an ABAP program or with the hierarchy generator of ABAP SQL directly in the `FROM` clause of an ABAP SQL query inside an ABAP program.

The following topics show you step-by-step how SQL hierarchies can be created and accessed.

## Creating SQL Hierarchies

### ABAP CDS Hierarchies

With [CDS hierarchies](../../abap-glossary/abenhierarchy_column_glosry.md), you outsource the hierarchy data source and the creation of the SQL hierarchy from your ABAP program to ABAP CDS. Here the hierarchy is a fully fledged CDS entity, it is reusable in different programs or in other CDS entities (views), and can be part of your data model including access control using CDS DCL. For a CDS hierarchy, the hierarchy source cannot be anything else but a CDS view that exposes a [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md). Here is a very simple example for that:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_SIMPLE_TREE_VIEW
  as select from demo_simple_tree
  association [1..1] to DEMO_CDS_SIMPLE_TREE_VIEW as _tree 
    on $projection.parent = _tree.id
{
      _tree,
  key id,
      parent_id as parent,
      name
}
```

This CDS view entity accesses the database table `DEMO_SIMPLE_TREE`, where the actual data is stored, and exposes a [self-association](../../abap-glossary/abenself_association_glosry.md) `_tree`. The `ON` condition of the association defines a parent-child relation between the elements `id` and `parent`. It simply means that a row of the result set where column `parent` has the same value as the column `id` of another row is a child of the latter row in the hierarchy that is constructed from that view. The CDS view exposes also another column `name` of the database table that represents the remaining data content. Note that you can define such CDS views for any available data source and that the `ON` condition can be more complex than shown in the simple example here.

Now we can use the above CDS view as the hierarchy source of a CDS hierarchy that can be defined as follows:

``` abap
define hierarchy DEMO_CDS_SIMPLE_TREE
  with parameters
    p_id : abap.int4
  as parent child hierarchy(
    source
      DEMO_CDS_SIMPLE_TREE_SOURCE
      child to parent association _tree
      start where
        id = :p_id
      siblings order by
        id ascending
    )
    {
      id,
      parent,
      name
    }
```

The CDS DDL statement [`DEFINE HIERARCHY`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_define_hierarchy.md) that can be used in the DDL source code editor of ADT defines a CDS hierarchy as a CDS entity that can be accessed in CDS views or ABAP SQL as a SQL hierarchy. The most important additions of the statement are:

- `SOURCE` for specifying the hierarchy source, here our `DEMO_CDS_SIMPLE_TREE_VIEW`.

- `CHILD TO PARENT ASSOCIATION` for specifying the hierarchy association, here `_tree`.

- `START WHERE` for defining the root nodes of the SQL hierarchy, here represented by an input parameter `p_id` that must be passed when accessing the CDS hierarchy.

- `SIBLINGS ORDER BY` to define also a sort order for sibling nodes besides the sort order that comes from the parent-child relationship anyhow.

- An element list `{ ... }` that defines the columns of the SQL hierarchy, here simply all elements of the hierarchy source.

For a full description and all other additions see [`DEFINE HIERARCHY`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_define_hierarchy.md).

When you access the CDS hierarchy, all lines are selected from the original data source, in our case the database table `DEMO_SIMPLE_TREE`, that fulfill the `START WHERE` condition. Those make up the root node set of the SQL hierarchy. In the simplest case we have exactly one root node, but more are possible. Then, for each root node, its descendants are retrieved. That means each line from the database table that fulfills the `ON`-condition of the hierarchy association is added to the SQL hierarchy. And for each descendant this is done again and again until all descendants are found. And that is basically all! Further additions to `DEFINE HIERARCHY` allow you to control the creation of the SQL hierarchy, for example, whether multiple parents are allowed or how orphans or cycles should be handled.

Besides the elements of the hierarchy, the element list can also contain the hierarchy attributes listed under [Hierarchy Attributes](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_hierarchy_attributes.md). Then the SQL hierarchy is enriched with columns containing information about the role, the current line plays as a hierarchy node, as, for example, the hierarchy rank or the hierarchy level. In our example, we did not add such elements, because ABAP SQL does that implicitly for you when accessing the CDS hierarchy!

The SQL hierarchy can be used in an ABAP SQL query by using the CDS hierarchy directly as a data source of the `FROM` clause:

``` abap
DATA root_id type demo_cds_simple_tree_view-id. 
 
... 
 
SELECT FROM demo_cds_simple_tree( p_id = @root_id ) 
       FIELDS id, 
              parent, 
              name, 
              hierarchy_rank, 
              hierarchy_tree_size, 
              hierarchy_parent_rank, 
              hierarchy_level, 
              hierarchy_is_cycle, 
              hierarchy_is_orphan, 
              node_id, 
              parent_id 
           INTO TABLE @FINAL(cds_result).
```

And although we did not define any hierarchy attributes in the element list of the CDS hierarchy, we can add all the hierarchy columns listed under [Hierarchy Columns](abenddddl_hierarchy.md) to the `SELECT` list of our ABAP SQL statement! This is always possible when a SQL hierarchy is accessed in ABAP SQL. We can pass any ID to the CDS hierarchy now and see what happens. If such a line is found in the database table, the respective hierarchical data will be retrieved and delivered. Execute class `CL_DEMO_SQL_HIERARCHIES` for filling the database table with randomly generated data and inspect the tabular result. As expected, all elements of the `SELECT` list appear as columns. Note that the content of column `NAME` could be anything. It is filled here with a string representation of the path from the root node to the current node for demonstration purposes only.

From the ABAP language point of view, CDS hierarchies are the most convenient way of using SQL hierarchies. Now let us turn to other ways, involving more ABAP, until we do not use any CDS more in the end.

### ABAP SQL Hierarchy Generator HIERARCHY

The ABAP SQL [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) is a ABAP SQL function named [`HIERARCHY`](abenselect_hierarchy_generator.md), that allows you to define a SQL hierarchy in the ABAP program itself. Let us look directly at an example:

``` abap
DATA root_id TYPE demo_cds_simple_tree_view-id. 
 
... 
 
SELECT FROM HIERARCHY( SOURCE demo_cds_simple_tree_view 
                       CHILD TO PARENT ASSOCIATION _tree 
                       START WHERE id = @root_id 
                       SIBLINGS ORDER BY id 
                       MULTIPLE PARENTS NOT ALLOWED ) "hierarchy 
       FIELDS id, 
              parent, 
              name, 
              hierarchy_rank, 
              hierarchy_tree_size, 
              hierarchy_parent_rank, 
              hierarchy_level, 
              hierarchy_is_cycle, 
              hierarchy_is_orphan, 
              node_id, 
              parent_id 
       INTO TABLE @FINAL(asql_cds_result).
```

`ASSERT asql_cds_result = cds_result.`

Looks familiar? Well, almost the same syntax used for defining the CDS hierarchy is used in the brackets `HIERARCHY( ... )` and it does exactly the same thing! The difference is the same as it is between ABAP SQL joins and joins in CDS views:

- If you code it in ABAP SQL, it is for usage in one program only.

- If you code it in ABAP CDS, it is for usage in many programs or whole data models.

And, as you can see, we dare to prove this with an `ASSERT` statement. Also note that we use the hierarchy columns again. They exist implicitly when an SQL hierarchy, here created by the hierarchy generator, is accessed.

The above hierarchy generator of ABAP SQL accesses the same hierarchy source as the CDS hierarchy, namely the CDS view `DEMO_CDS_SIMPLE_TREE_VIEW` that exposes the necessary hierarchy association `_tree`. In the following code snippet, we replace the CDS hierarchy source with a CTE:

``` abap
DATA root_id type demo_cds_simple_tree_view-id. 
 
... 
 
WITH 
  +cte_simple_tree_source AS 
     ( SELECT FROM demo_simple_tree 
              FIELDS id, 
                     parent_id AS parent, 
                     name ) 
        WITH ASSOCIATIONS ( 
          JOIN MANY TO MANY +cte_simple_tree_source AS _tree 
            ON +cte_simple_tree_source~parent = _tree~id ) 
  SELECT FROM HIERARCHY( SOURCE +cte_simple_tree_source 
                         CHILD TO PARENT ASSOCIATION _tree 
                         START WHERE id = @root_id 
                         SIBLINGS ORDER BY id 
                         MULTIPLE PARENTS NOT ALLOWED ) "hierarchy 
         FIELDS id, 
                parent, 
                name, 
                hierarchy_rank, 
                hierarchy_tree_size, 
                hierarchy_parent_rank, 
                hierarchy_level, 
                hierarchy_is_cycle, 
                hierarchy_is_orphan, 
                node_id, 
                parent_id 
         INTO TABLE @FINAL(asql_cte_result).
```

`ASSERT asql_cte_result = cds_result.`

Common table expressions (CTEs) are a very powerful tool for defining subqueries that can be used in subsequent queries of the same [`WITH`](abapwith.md) statement. They can be regarded as an internal ABAP SQL definition of data sources that fulfill the same functionality as program external data sources, especially CDS views. As you see above, the CTE `cte_simple_tree_source` does the same as the CDS view `DEMO_CDS_SIMPLE_TREE_VIEW`:

- It accesses the database table `DEMO_SIMPLE_TREE`.

- It exposes an association `_tree` by using the addition [`WITH ASSOCIATIONS`](abapwith_associations.md).

The main query of the `WITH` statement uses the hierarchy generator in the same way as the `SELECT` above, just with the CTE as a data source instead of the CDS view and the result is - of course - the same.

For a full description of the hierarchy generator and all other additions see [`SELECT, FROM HIERARCHY`](abenselect_hierarchy_generator.md).

We managed to create a SQL hierarchy with ABAP SQL means only. Last but not least we will use CTEs as hierarchies themselves. You might skip the following section and turn directly to the hierarchy navigators if you are not too interested in this syntactic gimmicks.

### ABAP CTE Hierarchies

A CTE that produces hierarchical data can declare itself as a SQL hierarchy of a freely defined name with the addition [`WITH HIERARCHY`](abapwith_hierarchy.md). That simply means that subsequent queries of the same `WITH` statement can use the CTE as a hierarchy with its implicit hierarchy columns or - more important - in hierarchy navigators.

The following code snippets show the three ways in which a CTE can produce hierarchical data:

``` abap
DATA root_id TYPE demo_cds_simple_tree_view-id. 
 
... 
 
WITH 
      +tree AS 
        ( SELECT FROM demo_cds_simple_tree( p_id = @root_id ) 
                 FIELDS * ) 
          WITH HIERARCHY demo_cds_simple_tree 
      SELECT FROM  +tree "hierarchy 
             FIELDS id, 
                    parent, 
                    name, 
                    hierarchy_rank, 
                    hierarchy_tree_size, 
                    hierarchy_parent_rank, 
                    hierarchy_level, 
                    hierarchy_is_cycle, 
                    hierarchy_is_orphan, 
                    node_id, 
                    parent_id 
             INTO TABLE @FINAL(cte_cds_result). 
 
... 
 
WITH 
      +tree AS 
        ( SELECT FROM HIERARCHY( 
            SOURCE demo_cds_simple_tree_view 
            CHILD TO PARENT ASSOCIATION _tree 
            START WHERE id = @root_id 
            SIBLINGS ORDER BY id 
            MULTIPLE PARENTS NOT ALLOWED ) AS asql_hierarchy 
            FIELDS id, 
                   parent, 
                   name ) 
          WITH HIERARCHY asql_hierarchy 
      SELECT FROM +tree "hierarchy 
             FIELDS id, 
                    parent, 
                    name, 
                    hierarchy_rank, 
                    hierarchy_tree_size, 
                    hierarchy_parent_rank, 
                    hierarchy_level, 
                    hierarchy_is_cycle, 
                    hierarchy_is_orphan, 
                    node_id, 
                    parent_id 
             INTO TABLE @FINAL(cte_asql_result). 
 
... 
 
WITH 
      +cte_simple_tree_source AS 
        ( SELECT FROM demo_simple_tree 
                 FIELDS id, 
                        parent_id AS parent, 
                        name ) 
           WITH ASSOCIATIONS ( 
             JOIN MANY TO MANY +cte_simple_tree_source AS _tree 
               ON +cte_simple_tree_source~parent = _tree~id ), 
      +tree AS 
        ( SELECT FROM HIERARCHY( 
            SOURCE +cte_simple_tree_source 
            CHILD TO PARENT ASSOCIATION _tree 
            START WHERE id = @root_id 
            SIBLINGS ORDER BY id 
            MULTIPLE PARENTS NOT ALLOWED ) AS cte_hierarchy 
            FIELDS id, 
                   parent, 
                   name  ) 
            WITH HIERARCHY cte_hierarchy 
      SELECT FROM +tree "hierarchy 
             FIELDS id, 
                    parent, 
                    name, 
                    hierarchy_rank, 
                    hierarchy_tree_size, 
                    hierarchy_parent_rank, 
                    hierarchy_level, 
                    hierarchy_is_cycle, 
                    hierarchy_is_orphan, 
                    node_id, 
                    parent_id 
             INTO TABLE @FINAL(cte_cte_result).
```abap
ASSERT cte_cds_result  = cds_result. 
ASSERT cte_asql_result = cds_result. 
ASSERT cte_cte_result  = cds_result.
```

A CTE that is exposed as a SQL hierarchy must access a SQL hierarchy itself and in the end these are always based on a CDS hierarchy or the ABAP SQL hierarchy generator as shown above. Again, the hierarchy source of the hierarchy generator can be a CDS view or a CTE exposing the hierarchy association. Executing `CL_DEMO_SQL_HIERARCHIES` shows that all assertions are fulfilled.

## Hierarchy Navigators

[Hierarchy navigators](../../abap-glossary/abenhierarchy_navigator_glosry.md) are an additional set of [hierarchy functions](../../abap-glossary/abenhierarchy_function_glosry.md) in ABAP SQL that allow you to work on existing SQL hierarchies instead of creating them. Hierarchy navigators can work on SQL hierarchies created as shown above, namely on CDS hierarchies, the hierarchy generator or a CTE hierarchy. They can be used as data sources in ABAP SQL queries. If you need a SQL hierarchy multiple times, from a performance point of view it is best to create it once with a given set of root nodes and then access it with hierarchy navigators. Furthermore, each hierarchy navigator can add further hierarchy columns to the result set that offer additional options for the evaluation.

In the following examples, we access our CDS hierarchy with hierarchy navigators. But you could also replace it with the hierarchy generator or a CTE hierarchy. Check the examples of the [documentation](abenselect_hierarchy_navigators.md), where this is also shown.

### Hierarchy Node Navigator HIERARCHY_DESCENDANTS

As the name says, [`HIERARCHY_DESCENDANTS`](abenselect_hierarchy_node_navis.md) fetches all descendants for any nodes from a SQL hierarchy. It adds `HIERARCHY_DISTANCE` as an additional hierarchy column to the result set. Let us look at an example. All examples are code snippets from `CL_DEMO_SQL_HIERARCHIES` again.

``` abap
DATA root_id TYPE demo_cds_simple_tree_view-id. 
 
DATA sub_id TYPE demo_cds_simple_tree_view-id. 
 
... 
 
SELECT FROM HIERARCHY_DESCENDANTS( 
              SOURCE demo_cds_simple_tree( p_id = @root_id ) 
              START WHERE id = @sub_id  ) 
  FIELDS id, 
         parent_id, 
         name, 
         hierarchy_distance 
  INTO TABLE @FINAL(descendants).
```

Our CDS hierarchy `DEMO_CDS_SIMPLE_TREE_VIEW` is used to create a SQL hierarchy with a start node passed to parameter `p_id` and for a node `sub_id` all descendants are fetched. Running the program shows the result including the additional column `HIERARCHY_DISTANCE` that contains the distance to the respective start node. A further parameter `DISTANCE` - not shown here - allows you to restrict the distance to the respective start node.

### Hierarchy Node Navigator HIERARCHY_ANCESTORS

Now the other way around: The ABAP SQL function [`HIERARCHY_ANCESTORS`](abenselect_hierarchy_node_navis.md) returns the ancestors of any given node of an existing hierarchy:

``` abap
DATA root_id TYPE demo_cds_simple_tree_view-id. 
 
DATA max_id TYPE demo_cds_simple_tree_view-id. 
 
... 
 
SELECT FROM HIERARCHY_ANCESTORS( 
              SOURCE demo_cds_simple_tree( p_id = @root_id ) 
              START WHERE id = @max_id ) 
  FIELDS id, 
          parent_id, 
          name, 
          hierarchy_distance 
  INTO TABLE @FINAL(ancestors).
```

Looking at the result when executing `CL_DEMO_SQL_HIERARCHIES`, you see that the value of column `HIERARCHY_DISTANCE` is negative now. Using aggregate functions or evaluating the internal result table, you can now easily extract further information like the number of ancestors and so on.

### Hierarchy Node Navigator HIERARCHY_SIBLINGS

Besides descendants and ancestors, hierarchy nodes also can have siblings, that is nodes that have the same parent node. You can find these by looking for all nodes with the same value in hierarchy column `HIERARCHY_PARENT_RANK`. But there is also [`HIERARCHY_SIBLINGS`](abenselect_hierarchy_node_navis.md) as a hierarchy function for that:

``` abap
DATA root_id TYPE demo_cds_simple_tree_view-id. 
 
DATA sibl_id TYPE demo_cds_simple_tree_view-id. 
 
... 
 
SELECT FROM HIERARCHY_SIBLINGS( 
              SOURCE demo_cds_simple_tree( p_id = @root_id ) 
              START WHERE id = @sibl_id ) 
  FIELDS id, 
          parent_id, 
          name, 
          hierarchy_sibling_distance 
  INTO TABLE @FINAL(siblings).
```

You see that this function adds another hierarchy column `HIERARCHY_SIBLING_DISTANCE` that contains the distance to the respective start node. Executing `CL_DEMO_SQL_HIERARCHIES`, where we start with a node that definitely has some siblings, shows the result.

### Hierarchy Aggregate Navigators

Finally let us turn to the [hierarchy aggregate navigators](../../abap-glossary/abenhierarchy_agg_navi_glosry.md) that allow you to apply some aggregate functions to descendants and ancestors of any node of a SQL hierarchy:

- [`HIERARCHY_DESCENDANTS_AGGREGATE`](abenselect_hierarchy_desc_agg.md)

- [`HIERARCHY_ANCESTORS_AGGREGATE`](abenselect_hierarchy_ancs_agg.md)

We will show an example for the descendants case and refer to the [documentation](abenselect_hierarchy_ancs_agg.md) for the ancestors.

Applying aggregate functions to columns normally means that you have some data there for which this makes sense. In our simplistic SQL hierarchy tree we do not have such meaningful data. On the other hand, this can also be a use case: You can have the administrative data for the parent-child relation in one database table and the real data in another one. And for that use case, the hierarchy aggregate navigator `HIERARCHY_DESCENDANTS_AGGREGATE` gives you the option of joining such data to your SQL hierarchy:

``` abap
TYPES: 
  BEGIN OF value, 
    id     TYPE i, 
    amount TYPE p LENGTH 16 DECIMALS 2, 
  END OF value. 
 
DATA value_tab TYPE SORTED TABLE OF value WITH UNIQUE KEY id. 
 
DATA root_id TYPE demo_cds_simple_tree_view-id. 
 
DATA sub_id TYPE demo_cds_simple_tree_view-id. 
 
... 
 
SELECT FROM HIERARCHY_DESCENDANTS_AGGREGATE( 
              SOURCE demo_cds_simple_tree( p_id = @sub_id  ) AS h 
              JOIN @value_tab AS v 
                ON  v~id = h~id 
              MEASURES SUM( v~amount ) AS amount_sum 
              WHERE hierarchy_rank > 1 
              WITH SUBTOTAL 
              WITH BALANCE ) 
  FIELDS id, 
         amount_sum, 
         hierarchy_rank, 
         hierarchy_aggregate_type 
  INTO TABLE @FINAL(descendants_aggregate).
```

In our example, we join an internal table `value_tab` of the same program to the SQL hierarchy. In a real life example you would join another database table, of course. On the other hand the example shows ABAP SQL's capability of using internal tables as data sources. You even can go so far to evaluate hierarchical data in internal tables with ABAP SQL by using an internal table as data source for a CTE hierarchy!

The example does the following:

- We use the hierarchy aggregate navigator `HIERARCHY_DESCENDANTS_AGGREGATE` as a data source of a `FROM` clause.

- Our CDS hierarchy `DEMO_CDS_SIMPLE_TREE_VIEW` joined with internal table `value_tab` is used as the data source.

- The ABAP SQL function returns a tabular result of nodes of the data source.

- The aggregate function `SUM` behind `MEASURES` sums up the values of the column amounts of the joined internal table for all descendants of each node returned by the ABAP SQL function.

- The `WHERE` condition restricts the result set by a freely programmable condition.

- The `WITH` additions add further rows to the result set that can be recognized by values in an additional hierarchy column `HIERARCHY_AGGREGATE_TYPE`:

  - `WITH SUBTOTAL`

    In the row where `HIERARCHY_AGGREGATE_TYPE` has value 1, column `AMOUNT_SUM` contains the sum of the values of all hierarchy nodes that meet the `WHERE` condition.

  - `WITH BALANCE`

    In the row where `HIERARCHY_AGGREGATE_TYPE` has value 2, column `AMOUNT_SUM` contains the sum of the values of all hierarchy nodes that do not meet the `WHERE` condition. For more `WITH` additions see the [documentation](abenselect_hierarchy_desc_agg.md).

Executing `CL_DEMO_SQL_HIERARCHIES` shows the result. It also shows the result of the joined data source, where you can check that the calculated values are correct.
