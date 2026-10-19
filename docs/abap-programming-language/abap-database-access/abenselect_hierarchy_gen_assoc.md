---
title: "SELECT, FROM HIERARCHY, CHILD TO PARENT ASSOCIATION"
source_file: abenselect_hierarchy_gen_assoc.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data > SELECT, FROM hierarchy > SELECT, FROM HIERARCHY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, FROM HIERARCHY, CHILD TO PARENT ASSOCIATION

## Syntax

``` abap
... HIERARCHY( SOURCE hierarchy_source [WITH PRIVILEGED ACCESS] 
               CHILD TO PARENT ASSOCIATION _hierarchy_assoc 
              [PERIOD FROM field1 TO field2 VALID FROM from TO to] 
               START WHERE sql_cond 
              [SIBLINGS ORDER BY field1 [ASCENDING|DESCENDING][, 
                                 field2 [ASCENDING|DESCENDING], ...]] 
              [DEPTH depth] 
              [MULTIPLE PARENTS {NOT ALLOWED}{LEAVES ONLY}|ALLOWED] 
              [ORPHANS IGNORE|ERROR|ROOT] 
              [CYCLES ERROR|BREAKUP] 
              [LOAD BULK|INCREMENTAL|load_option] 
              [GENERATE SPANTREE] 
              [CACHE ON|OFF|FORCE] ) ...  
```

[`sql_cond`](abenabap_sql_expr_logexp.md)

### Addition

[1. `... SOURCE hierarchy_source [WITH PRIVILEGED ACCESS]`](abenselect_hierarchy_gen_assoc.md#addition-1)

[2. `... CHILD TO PARENT ASSOCIATION _hierarchy_assoc`](abenselect_hierarchy_gen_assoc.md#addition-2)

[3. `... PERIOD FROM field1 TO field2 VALID FROM from TO to`](abenselect_hierarchy_gen_assoc.md#addition-3)

[4. `... START WHERE sql_cond`](abenselect_hierarchy_gen_assoc.md#addition-4)

[5. `... SIBLINGS ORDER BY field1 [ASCENDING|DESCENDING], ...`](abenselect_hierarchy_gen_assoc.md#addition-5)

[6. `... DEPTH depth`](abenselect_hierarchy_gen_assoc.md#addition-6)

[7. `... MULTIPLE PARENTS {NOT ALLOWED}|{LEAVES ONLY}|ALLOWED`](abenselect_hierarchy_gen_assoc.md#addition-7)

[8. `... ORPHANS IGNORE|ERROR|ROOT`](abenselect_hierarchy_gen_assoc.md#addition-8)

[9. `... CYCLES ERROR|BREAKUP`](abenselect_hierarchy_gen_assoc.md#addition-9)

[10. `... LOAD BULK|INCREMENTAL|load_option`](abenselect_hierarchy_gen_assoc.md#addition-10)

[11. `... GENERATE SPANTREE`](abenselect_hierarchy_gen_assoc.md#addition-11)

[12. `... CACHE ON|OFF|FORCE`](abenselect_hierarchy_gen_assoc.md#addition-12)

## Overview

### Description

In this variant of the hierarchy generator `HIERARCHY`, a [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md) is generated that is defined by parent-child-relations between different columns of a so called hierarchy source that must expose a hierarchy annotation. The following needs to be specified:

- The [hierarchy source](../../abap-glossary/abenhierarchy_source_glosry.md) `hierarchy_source` of the SQL hierarchy must be specified after `SOURCE`.

- After `CHILD TO PARENT ASSOCIATION`, a [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md) `_hierarchy_assoc` exposed by the source `hierarchy_source` must be specified. The [association source](../../abap-glossary/abenassociation_source_glosry.md) and [association target](../../abap-glossary/abenassociation_target_glosry.md) of this association must be the source `hierarchy_source`. The `ON` condition of the hierarchy association defines the [parent-child relationships](../../abap-glossary/abenpcr_glosry.md) between the [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md).

- `START WHERE` must be followed by a start condition that defines [root nodes](../../abap-glossary/abenroot_node_glosry.md) for the [root node set](../../abap-glossary/abenroot_node_set_glosry.md) of the SQL hierarchy. The SQL hierarchy consists of the root nodes of the root node set and their [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md).

All other additions are optional and define further properties of the SQL hierarchy.

The columns of the SQL hierarchy are composed of the elements of the source specified after `SOURCE` and additional [hierarchy columns](abenddddl_hierarchy.md).

The hierarchy generator `HIERARCHY` exposes all associations of the source `hierarchy_source` specified after `SOURCE` implicitly and leaves its [association target](../../abap-glossary/abenassociation_target_glosry.md) unchanged.

### Hints

- The order of the additions is fixed. They must be specified as shown here.

- Rows of the result set of the source specified after `SOURCE` can occur more than once in the result set of the hierarchy generator, if selected by appropriate parent-child relationships.

- This variant of the hierarchy generator `HIERARCHY` in ABAP SQL works in the same way as the statement [`DEFINE HIERARCHY`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_define_hierarchy.md) in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md). Accessing the hierarchy generator `HIERARCHY` as the data source of a query is the same as accessing a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md) defined accordingly.

- Since hierarchies generated from the `START WHERE` condition are buffered on the database, it is advisable to use fixed values for the root nodes of large hierarchies of data that do not change often. To evaluate subnodes of such hierarchies, the [hierarchy navigators](../../abap-glossary/abenhierarchy_navigator_glosry.md) of ABAP SQL can then be used.

- An association exposed implicitly by the hierarchy generator `HIERARCHY` can be used in [path expressions](abenabap_sql_path.md) or in further hierarchy generators.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specifies the hierarchy generator `HIERARCHY` as the data source of a `SELECT` statement in class `CL_DEMO_HIERARCHY_TREE`. The source of the hierarchy generator is a CDS view that uses the [global temporary table](../../abap-glossary/abenglobal_temporary_table_glosry.md) `DEMO_SIMPLE_TREE` as a data source and whose CDS association `_tree` defines the parent-child relationship. The hierarchy generator selects the row with the value of `start_id` in the column `ID` as the [root node](../../abap-glossary/abenroot_node_glosry.md) and, starting from this node, inserts all [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md) in the result set that meet the `ON` condition of the hierarchy association. The result set contains all columns of the view `DEMO_CDS_SIMPLE_TREE_SOURCE`, plus all potential [hierarchy columns](abenddddl_hierarchy.md). Executing `CL_DEMO_HIERARCHY_TREE` demonstrates the result of the `SELECT` statement.

``` abap
FINAL(start_id) = 1. 
 
SELECT FROM HIERARCHY( SOURCE demo_cds_simple_tree_source 
                       CHILD TO PARENT ASSOCIATION _tree 
                       START WHERE id = @start_id 
                       SIBLINGS ORDER BY parent 
                       MULTIPLE PARENTS NOT ALLOWED ) 
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
       INTO TABLE @FINAL(asql_result).
```

## Addition 1

`... SOURCE hierarchy_source [WITH PRIVILEGED ACCESS]`

### Description

The addition `SOURCE` specifies `hierarchy_source` as the [hierarchy source](../../abap-glossary/abenhierarchy_source_glosry.md) of the hierarchy generator. This source must expose the [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md) `_hierarchy_assoc` specified after `CHILD TO PARENT ASSOCIATION`. The following are potential sources `hierarchy_source`:

- A CDS view `cds_view`

  `cds_view` can be specified as a [CDS view](../../abap-glossary/abencds_view_glosry.md) that exposes the hierarchy association `_hierarchy_assoc` in its `SELECT` list.

- A common table expression `+cte`

  `+cte` can be specified as a preceding [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md) in a [`WITH`](abapwith.md) statement that exposes the hierarchy association `_hierarchy_assoc` using the addition [`WITH ASSOCIATIONS`](abapwith_associations.md). The self-association prerequisite can be met as follows:

  - The addition [`REDIRECTED`](abapwith_associations_using.md) is used to replace the [association target](../../abap-glossary/abenassociation_target_glosry.md) of an association of a data source of the common table expression with the common table expression itself.

  - [`JOIN cardinality`](abapwith_associations_defining.md) is used to define a CTE association as a self-association for the common table expression.

- A nested SQL hierarchy `hierarchy`

  The hierarchy generator `HIERARCHY` can use other SQL hierarchies [`hierarchy`](abenselect_hierarchy.md) as a source. The following applies here:

  - A CDS hierarchy [`cds_hierarchy`](abenselect_cds_hierarchy.md) must expose the hierarchy association `_hierarchy_assoc` in its element list. To meet the self-association prerequisite, the association must be an additional association between the source of the CDS hierarchy and the CDS hierarchy.

  - The hierarchy generator `HIERARCHY` exposes all associations of its source implicitly.

  - A [CTE hierarchy](../../abap-glossary/abencte_hierarchy_glosry.md) must use [`WITH ASSOCIATIONS`](abapwith_associations.md) to expose the hierarchy association `_hierarchy_assoc`. Furthermore, the addition `REDIRECTED` must be used to replace the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the association in such a way that the self-association prerequisite is met.

    The hierarchy generator uses the result of an SQL hierarchy specified after `SOURCE` as a source, whereby its additional [hierarchy columns](abenddddl_hierarchy.md) are ignored. An outer hierarchy generator always adds its own hierarchy columns directly to the columns of the SQL hierarchy specified after `SOURCE`. Any hierarchy columns listed explicitly in the element list of a CDS hierarchy that is specified as a source, on the other hand, are part of this hierarchy's result set and are respected accordingly.

If a [CDS role](../../abap-glossary/abencds_role_glosry.md) is assigned to a CDS view specified as a source, the source is implicitly subject to [CDS access control](../../abap-glossary/abencds_access_control_glosry.md) and only nodes that meet the [access conditions](../../abap-glossary/abenaccess_condition_glosry.md) of the CDS role are transferred to the SQL hierarchy. When specifying the optional addition `WITH PRIVILEGED ACCESS`, the access control is deactivated, and the access conditions are not evaluated.

### Hint

SQL hierarchies should only be nested in exceptional cases.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Uses a CDS view and two common table expressions as the source of the hierarchy generator `HIERARCHY` in the class `CL_DEMO_HIERARCHY_GENERATOR`.

- The first common table expression accesses the same CDS view and uses a path expression to [expose](abapwith_associations_using.md) the same hierarchy association. This expression must use [`REDIRECTED TO`](abapwith_associations.md) to redirect the hierarchy association to itself and hence meet the self-association requirement.

- The second common table expression accesses the DDIC database table `DEMO_SIMPLE_TREE` in the same way as the CDS view and [defines](abapwith_associations_defining.md) a separate [CTE association](../../abap-glossary/abencte_association_glosry.md) as a self-association that is then used as a hierarchy association.

All main queries have the same result.

``` abap
FINAL(start_id) = 1. 
 
"CDS view as source of hierarchy generator 
 
SELECT FROM HIERARCHY( SOURCE demo_cds_simple_tree_source 
                       CHILD TO PARENT ASSOCIATION _tree 
                       START WHERE id = @start_id 
                       SIBLINGS ORDER BY parent 
                       MULTIPLE PARENTS NOT ALLOWED ) 
       FIELDS name 
       INTO TABLE @FINAL(cds_result). 
 
"CTE with association exposed as path as source of hierarchy generator 
 
WITH +tree AS ( 
        SELECT FROM demo_cds_simple_tree_source AS tree 
               FIELDS * ) 
        WITH ASSOCIATIONS ( \_tree 
                            REDIRECTED TO +tree 
                            VIA tree ) 
  SELECT FROM HIERARCHY( 
                SOURCE +tree 
                CHILD TO PARENT ASSOCIATION _tree 
                START WHERE id = @start_id ) 
         FIELDS name 
         INTO TABLE @FINAL(cte_path_result). 
ASSERT cte_path_result = cds_result. 
 
"CTE with association defined as join as source of hierarchy generator 
 
WITH +simple_tree_source AS ( 
        SELECT FROM demo_simple_tree 
               FIELDS id, 
                      parent_id as parent, 
                      name ) 
        WITH ASSOCIATIONS ( JOIN MANY TO ONE +simple_tree_source 
                              as _tree 
                              ON +simple_tree_source~parent = _tree~id ) 
  SELECT FROM HIERARCHY( 
                SOURCE +simple_tree_source 
                CHILD TO PARENT ASSOCIATION _tree 
                START WHERE id = @start_id ) 
         FIELDS name 
         INTO TABLE @FINAL(cte_join_result). 
ASSERT cte_join_result = cds_result.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Nesting of SQL hierarchies in the hierarchy generator `HIERARCHY` in the class `CL_DEMO_HIERARCHY_NESTED`. When executed, `CL_DEMO_HIERARCHY_NESTED` demonstrates the result of the `SELECT` statements. Three tree-like SQL hierarchies that start at the row with the value 1 in the column `ID` are restricted to a depth of 2. From these hierarchies, further SQL hierarchies are selected that start at the row with the value 5 in the column `ID`. The three inner SQL hierarchies are specified as a CDS hierarchy, the hierarchy generator `HIERARCHY`, and as a [CTE hierarchy](../../abap-glossary/abencte_hierarchy_glosry.md). In the case of the CDS hierarchy and the CTE hierarchy, the hierarchy association must be verified as a self-association explicitly. The three inner SQL hierarchies have the same result sets, which means that the results of the three `SELECT` statements are also the same.

``` abap
"CDS hierarchy as source of hierarchy generator 
 
SELECT FROM HIERARCHY( 
              SOURCE demo_cds_simple_tree_redir( p_id = 1, 
                                                 p_depth = 2 ) 
              CHILD TO PARENT ASSOCIATION _redir 
              START WHERE id = 5 ) 
       FIELDS id, 
              parent, 
              hierarchy_rank, 
              hierarchy_level 
       INTO TABLE @FINAL(hierarchy_cds_hierarchy). 
 
"Hierarchy generator as source of hierarchy generator 
 
SELECT FROM HIERARCHY( 
              SOURCE HIERARCHY( 
                       SOURCE demo_cds_simple_tree_source 
                       CHILD TO PARENT ASSOCIATION _tree 
                       START WHERE id = 1 
                       DEPTH 2 ) 
              CHILD TO PARENT ASSOCIATION _tree 
              START WHERE id = 5  ) 
       FIELDS id, 
              parent, 
              hierarchy_rank, 
              hierarchy_level 
       INTO TABLE @FINAL(hierarchy_hierarchy). 
ASSERT hierarchy_hierarchy = hierarchy_cds_hierarchy. 
 
"CTE hierarchy as source of hierarchy generator 
 
WITH +hierarchy AS ( 
        SELECT FROM HIERARCHY( 
                      SOURCE demo_cds_simple_tree_source 
                      CHILD TO PARENT ASSOCIATION _tree 
                      START WHERE id = 1 
                      DEPTH 2 ) AS hierarchy 
               FIELDS id, 
                      parent ) 
        WITH HIERARCHY hierarchy 
        WITH ASSOCIATIONS ( \_tree 
                            REDIRECTED TO +hierarchy 
                            VIA hierarchy ) 
  SELECT FROM HIERARCHY( 
                SOURCE +hierarchy 
                CHILD TO PARENT ASSOCIATION _tree 
                START WHERE id = 5 
                ) 
         FIELDS id, 
                parent_id, 
                hierarchy_rank, 
                hierarchy_level 
         INTO TABLE @FINAL(hierarchy_cte_hierarchy). 
ASSERT hierarchy_cte_hierarchy = hierarchy_cds_hierarchy.
```

## Addition 2

`... CHILD TO PARENT ASSOCIATION _hierarchy_assoc`

### Description

The addition `CHILD TO PARENT ASSOCIATION` specifies the [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md), whose `ON` condition of the hierarchy generator selects the [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md) of the [root node set](../../abap-glossary/abenroot_node_set_glosry.md). The hierarchy association must be exposed by the source `hierarchy_source` specified after `SOURCE`.

The hierarchy association defines the parent-child relationship between the [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md). The following conditions apply here:

- The association must be a [self-association](../../abap-glossary/abenself_association_glosry.md).

- Only equality comparisons with the operator `=` and combined using `AND` can occur in the `ON` condition of the association.

- In each comparison in the `ON` condition, one field of the [association source](../../abap-glossary/abenassociation_source_glosry.md) must be compared with a field, which is prefixed with `_hierarchy_assoc`, of the [association target](../../abap-glossary/abenassociation_target_glosry.md).

- The [association source](../../abap-glossary/abenassociation_source_glosry.md) of the association cannot contain any fields that have the same name as a [hierarchy column](abenddddl_hierarchy.md). An alternative element name must be defined for these fields.

Each row of the result set of the source `hierarchy_source` that meets the `ON` condition for an existing hierarchy node is included recursively in the SQL hierarchy as its [child node](../../abap-glossary/abenchild_node_glosry.md), if possible.

### Hint

The optional additions define further conditions specifying whether a row can be included as a hierarchy node or not.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity exposes its CDS association `_tree`. This CDS association meets all requirements of a hierarchy association and can be used as such.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_SIMPLE_TREE_SOURCE
  as select from demo_simple_tree
  association to exact one DEMO_CDS_SIMPLE_TREE_SOURCE as _tree 
    on $projection.parent = _tree.id
{
      _tree,
  key id,
      parent_id as parent,
      name
}
```

## Addition 3

`... PERIOD FROM field1 TO field2 VALID FROM from TO to`

### Description

Defines an SQL hierarchy as a [temporal SQL hierarchy](../../abap-glossary/abentemporal_hierarchy_glosry.md) in which the hierarchy nodes are limited by an adjustment of time intervals.

- With `field1` and `field2`, the fields of the source `hierarchy_source` are specified, which define the lower and upper limits of a [period](../../abap-glossary/abenperiod_glosry.md) in the hierarchy details. `field1` and `field2` must be different fields of the same data type. This can be:

  - The built-in type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) of the ABAP Dictionary.

  - A data type that is defined by one of the [DDIC data elements](../../abap-glossary/abendata_element_glosry.md) `TIMESTAMP` or `TIMESTAMPL`.

- `from` and `to` define the lower and upper limit of a time interval that acts as a condition for the periods of the [root node set](../../abap-glossary/abenroot_node_set_glosry.md). For `from` and `to`, [host variables](abenabap_sql_host_variables.md), [host expressions](abenabap_sql_host_expressions.md), and [type-compliant literals](abenabap_sql_literals.md) can be specified, whose ABAP data type matches the dictionary data type of `field1` and `field2` exactly.

A temporal SQL hierarchy is created as follows:

- Only [root nodes](../../abap-glossary/abenroot_node_glosry.md) of the [root node set](../../abap-glossary/abenroot_node_set_glosry.md) in which the period defined using `field1` and `field2` has a non empty intersection with the time interval defined by `from` and `to` are respected. This intersection forms the [validity interval](../../abap-glossary/abenvalidity_interval_glosry.md) of the root node.

- Only [child nodes](../../abap-glossary/abenchild_node_glosry.md) in which the period defined by `field1` and `field2` has a non empty intersection with the validity interval of the [parent node](../../abap-glossary/abenparent_node_glosry.md) are generated. This intersection forms the [validity interval](../../abap-glossary/abenvalidity_interval_glosry.md) of the child node.

For temporal SQL hierarchies, there are additional [hierarchy columns](abenddddl_hierarchy.md) `VALID_FROM` and `VALID_UNTIL` that contain the interval limits of the [validity interval](../../abap-glossary/abenvalidity_interval_glosry.md) of each hierarchy node.

The addition `PERIOD` must not be used with `GENERATE SPANTREE`.

### Hints

- The validity interval of a descendant node is always a subset of a validity interval of all ancestor nodes. Validity intervals can only remain the same or become narrower from hierarchy level to hierarchy level, they never widen.

- For a descendant node to belong to a temporal SQL hierarchy, it is not sufficient for its period to overlap with the time interval defined by `from` and `to`. Only the validity interval of the parent node is decisive. A path of a regular SQL hierarchy is truncated in a temporal SQL hierarchy at the position in which there is no intersection between the period and the preceding validity interval.

- The [association source](../../abap-glossary/abenassociation_source_glosry.md) of the current [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md) must not have any fields called `VALID_FROM` or `VALID_UNTIL`. An alternative element name must be defined for these fields.

- The value of `to` can also be less than the value of `from`. However, a validity interval is formed where necessary. In contrast, if the value of the lower interval limit of the period is greater than the value of the upper interval limit, the validity interval is empty.

- Additions such as `MULTIPLE PARENTS` or `CYCLES` affect the temporal SQL hierarchy. Nodes that would raise an exception in a regular SQL hierarchy can be hidden in a temporal SQL hierarchy.

- On an [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md), the hierarchy generator function [`HIERARCHY_TEMPORAL`](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/2969da89b87f4abd85fd0b5f9f5bc395) is used to create a temporal SQL hierarchy.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creates two [temporal SQL hierarchies](../../abap-glossary/abentemporal_hierarchy_glosry.md) in the class `CL_DEMO_HIERARCHY_TEMPORAL`, where in one date fields and in the other time stamp fields are used as [periods](../../abap-glossary/abenperiod_glosry.md).

``` abap
SELECT FROM HIERARCHY( 
  SOURCE demo_cds_parent_child_src_prd 
  CHILD TO PARENT ASSOCIATION _relat 
  PERIOD FROM date_from TO date_to 
   VALID FROM @( CONV d( cl_demo_date_time=>get_user_date( ) - 1 ) ) 
           TO @( CONV d( cl_demo_date_time=>get_user_date( ) + 1 ) ) 
  START WHERE id = 'A' 
  SIBLINGS ORDER BY id ) 
       FIELDS id, 
              parent, 
              valid_from, 
              valid_until 
       INTO TABLE @FINAL(asql_date_period) ##TYPE. 
 
GET TIME STAMP FIELD FINAL(ts). 
SELECT FROM HIERARCHY( 
  SOURCE demo_cds_parent_child_src_prd 
  CHILD TO PARENT ASSOCIATION _relat 
  PERIOD FROM ts_from TO ts_to 
   VALID FROM @( CONV timestamp( 
                   cl_abap_tstmp=>subtractsecs( 
                     tstmp = ts 
                     secs  = 86400 ) ) ) 
           TO @( CONV timestamp( 
                   cl_abap_tstmp=>add( 
                     tstmp = ts 
                     secs  = 86400 ) ) ) 
  START WHERE id = 'A' 
  SIBLINGS ORDER BY id ) 
       FIELDS id, 
              parent, 
              valid_from, 
              valid_until 
       INTO TABLE @FINAL(asql_ts_period) ##TYPE.
```

When executed, this class demonstrates how the `PERIOD` addition works. The date and time stamp fields of the DDIC database table `DEMO_PARCHLD_PRD`, which are accessed in the source of the hierarchy generator `DEMO_CDS_PARENT_CHILD_SRC_PRD`, are filled with data for this purpose. A regular SQL hierarchy without the addition `PERIOD` and the two temporal SQL hierarchies are shown. The [validity intervals](../../abap-glossary/abenvalidity_interval_glosry.md) are also output for these.

- The temporal SQL hierarchy based on date fields contains only the nodes with the values *A*, `B`, and `C` in the column `ID`. The period of the node with the value *D* does not overlap with the validity interval of the parent node with the value *B*. This means that the child node with the value *E* is truncated, regardless of its period. All other nodes `F` to *I* haven empty periods and are not relevant anyway.

- The temporal SQL hierarchy based on time stamps contains all nodes with periods `TS_FROM` to `TS_TO` that are not empty. The example illustrates how the validity intervals with the hierarchy levels can become narrower. In the last row, the validity interval corresponds to the previous one, even though the period is wider.

## Addition 4

`... START WHERE sql_cond.`

### Description

The addition `START WHERE` specifies the start condition for the hierarchy generator. After `START WHERE`, a logical expression [`sql_cond`](abenabap_sql_expr_logexp.md) must be specified that selects rows from the source `hierarchy_source`. The selected rows are inserted into the SQL hierarchy as a [root node set](../../abap-glossary/abenroot_node_set_glosry.md). For each [root node](../../abap-glossary/abenroot_node_glosry.md) in the root node set, the [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md) are selected that meet the `ON` condition of the hierarchy association and, if possible, inserted into the SQL hierarchy.

### Hint

The start condition should select a meaningful set of root nodes. If no rows in the result set of the source `hierarchy_source` meet the condition, the SQL hierarchy is empty. If all rows meet the condition, the descendant nodes of every row are selected and inserted.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specifies an interval condition for the start condition of the hierarchy generator `HIERARCHY` in the class `CL_DEMO_HIERARCHY_START_WHERE`. All rows in the CDS view specified as the source that meet the condition are inserted in the SQL hierarchy as root nodes and all their descendant nodes are selected. When executed, this class allows different limits to be entered and displays the result.

``` abap
FINAL(from) = 'A '. 
FINAL(to) =   'B '. 
 
SELECT FROM HIERARCHY( SOURCE demo_cds_parent_child_source 
                       CHILD TO PARENT ASSOCIATION _relat 
                       START WHERE id BETWEEN @from AND @to 
                       SIBLINGS ORDER BY parent 
                       MULTIPLE PARENTS ALLOWED 
                       CYCLES BREAKUP ) 
       FIELDS id, 
              parent 
       INTO TABLE @FINAL(asql_result).
```

## Addition 5

`... SIBLINGS ORDER BY field1 [ASCENDING|DESCENDING], ...`

### Description

The addition `SIBLINGS ORDER BY` sorts [sibling nodes](../../abap-glossary/abensibling_node_glosry.md) in the SQL hierarchy generated by the hierarchy generator. If this addition is not used, the order of the sibling nodes is undefined.

Fields `field1`, `field2`, ... of the source `hierarchy_source` can be specified in a comma-separated list after the addition `hierarchy_source` to specify the order of the sibling nodes.

The addition `ASCENDING` or `DESCENDING` can be specified for each field to specify an ascending or descending order, whereby ascending is the default.

The fields specified after `ORDER BY` cannot be of the [type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) `LCHR`, `LRAW`, `STRING`, `RAWSTRING`, or `GEOM_EWKB`.

### Hints

- If additionally a general [`ORDER BY`](abaporderby_clause.md) clause is specified in current query, it affects the SQL hierarchy that is sorted by `SIBLINGS ORDER BY`.

- The additional [hierarchy columns](abenddddl_hierarchy.md) cannot be specified after `SIBLINGS ORDER BY`. They can, however, be specified in the general [`ORDER BY`](abaporderby_clause.md) clause of the current query.

- The fields of the source `hierarchy source` must be specified by their name. It is not possible to specify a position as in the [`ORDER BY`](abaporderby_clause.md) clause.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Ascending and descending sort of [sibling nodes](../../abap-glossary/abensibling_node_glosry.md) in the class `CL_DEMO_HRRCHY_SIBLINGS_ORDER`. When executed, this program demonstrates how these additions work.

``` abap
SELECT FROM HIERARCHY( SOURCE demo_cds_simple_tree_source 
                       CHILD TO PARENT ASSOCIATION _tree 
                       START WHERE id = 1 
                       SIBLINGS ORDER BY id ASCENDING ) 
       FIELDS id, 
              parent, 
              hierarchy_parent_rank 
       INTO TABLE @FINAL(result_asc). 
 
SELECT FROM HIERARCHY( SOURCE demo_cds_simple_tree_source 
                       CHILD TO PARENT ASSOCIATION _tree 
                       START WHERE id = 1 
                       SIBLINGS ORDER BY id DESCENDING ) 
       FIELDS id, 
              parent, 
              hierarchy_parent_rank 
       INTO TABLE @FINAL(result_desc).
```

## Addition 6

`... DEPTH depth`

### Description

The addition `depth` can be used to limit the number of [hierarchy levels](../../abap-glossary/abenhierarchy_level_glosry.md) used to create [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md). `depth` expects a [host variable](abenabap_sql_host_variables.md), a [host expression](abenabap_sql_host_expressions.md), or a [literal](abenabap_sql_literals.md) of type `i`. Only the types `b`, `s`, or `i` can be specified for `depth`.

The value in `depth` has the following meaning:

- For `depth` values greater than 0, as many hierarchy edges as specified in `depth` are traced, starting from a [root node](../../abap-glossary/abenroot_node_glosry.md).

- If the value of `depth` is 0, only the [root nodes](../../abap-glossary/abenroot_node_glosry.md) are inserted into the SQL hierarchy.

- If `depth` is less than 0, no [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md) are created and `sy-subrc` is set to 4.

The addition `DEPTH` can be used only if the addition `ORPHANS` is not specified or is specified as `ORPHANS IGNORE`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Limits the number of [hierarchy levels](../../abap-glossary/abenhierarchy_level_glosry.md) in the class `CL_DEMO_HIERARCHY_DEPTH`. When executed, this program demonstrates how this addition works. It also shows the [hierarchy level](../../abap-glossary/abenhierarchy_level_glosry.md) from the hierarchy column `HIERARCHY_LEVEL`.

``` abap
SELECT FROM HIERARCHY( SOURCE demo_cds_simple_tree_source 
                       CHILD TO PARENT ASSOCIATION _tree 
                       START WHERE id = 1 
                       DEPTH 1 ) 
       FIELDS name, 
              hierarchy_level 
       INTO TABLE @FINAL(result_1).
```

## Addition 7

`... MULTIPLE PARENTS {NOT ALLOWED}|{LEAVES ONLY}|ALLOWED`

### Description

The addition `MULTIPLE PARENTS` can be used to define whether the hierarchy generator is allowed to generate [child nodes](../../abap-glossary/abenchild_node_glosry.md) with multiple [parent nodes](../../abap-glossary/abenparent_node_glosry.md):

- `NOT ALLOWED`

  This is the default setting. A child node can have exactly on parent node only).

- `LEAVES ONLY`

  Only [leaf nodes](../../abap-glossary/abenleaf_node_glosry.md) can have multiple parent nodes.

- `ALLOWED`

  All hierarchy nodes can have multiple parent nodes.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of an SQL hierarchy in the class `CL_DEMO_HIERARCHY_MULTI_PRNTS`. Only leaf nodes can have multiple parents here.

``` abap
SELECT FROM HIERARCHY( SOURCE demo_cds_parent_child_source 
                       CHILD TO PARENT ASSOCIATION _relat 
                       START WHERE id = 'A' 
                       MULTIPLE PARENTS LEAVES ONLY ) 
       FIELDS id, 
              parent, 
              hierarchy_level 
       INTO TABLE @FINAL(leaves_only).
```

When executed, this program demonstrates how the `MULTIPLE PARENTS` addition works.

- The first `SELECT` statement does not specify the addition and `NOT ALLOWED` is applied implicitly. The hierarchy node with the ID `D` has three parent nodes and hence an exception is raised.

- The next `SELECT` statement specifies the addition `MULTIPLE PARENTS LEAVES ONLY`. The hierarchy node with the ID `D` is a leaf node, which means the function can be accessed.

- A child node for the row with the ID `D` is inserted in front of the next `SELECT` statement in the DDIC database table `DEMO_PARENT_CHLD`. If used, the addition `MULTIPLE PARENTS LEAVES ONLY` now also raises an exception.

- The next `SELECT` statement specifies the addition `MULTIPLE PARENTS ALLOWED` and it is possible to access the table again.

## Addition 8

`... ORPHANS IGNORE|ERROR|ROOT`

### Description

The addition `ORPHANS` defines how [orphan nodes](../../abap-glossary/abenorphan_node_glosry.md) are handled. The following categories of orphan nodes exist:

- Hierarchy nodes that could have parent nodes according to the parent-child relationship, but the parent nodes are not in the SQL hierarchy (true orphans).

- Hierarchy nodes that cannot be reached from the root node set using hierarchy edges.

- Hierarchy nodes that are part of a [node cycle](../../abap-glossary/abennode_cycle_glosry.md) and cannot be reached from the root node set using hierarchy nodes (island orphans).

The additions work as follows:

- `IGNORE`

  This is the default setting. Any orphan nodes are not inserted in the SQL hierarchy.

- `ERROR`

  Any orphan nodes detected raise an exception.

- `ROOT`

  Orphan nodes are inserted into the SQL hierarchy as follows:

  - True orphans are included in the root node set as root nodes and flagged as orphan nodes in the [hierarchy column](abenddddl_hierarchy.md) `HIERARCHY_IS_ORPHAN`.

  - [Descendant nodes](../../abap-glossary/abendescendant_node_glosry.md) of true orphans are handled like those of parent nodes from the root node set, but are also flagged as orphan nodes in the [hierarchy column](abenddddl_hierarchy.md) `HIERARCHY_IS_ORPHAN`.

  - For the hierarchy nodes of island orphans, a parent node in the root node set is generated for the child node where the cycle occurs. In the generated root node, all columns of the source `hierarchy_source` contain the null value. In the [hierarchy columns](abenddddl_hierarchy.md), the additional root node is flagged as an orphan node and `PARENT_ID` also contains the null value.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Handles orphan nodes in the class `CL_DEMO_HIERARCHY_ORPHANS`.

``` abap
SELECT FROM HIERARCHY( SOURCE demo_cds_parent_child_source 
                       CHILD TO PARENT ASSOCIATION _relat 
                       START WHERE id = 'A' 
                       MULTIPLE PARENTS ALLOWED 
                       ORPHANS ROOT 
                       CYCLES BREAKUP ) 
       FIELDS CASE WHEN id IS NULL THEN '__' 
                   ELSE id 
                   END AS id, 
              CASE WHEN parent IS NULL THEN '__' 
                   ELSE parent 
                   END AS parent, 
              hierarchy_is_orphan, 
              hierarchy_is_cycle, 
              hierarchy_rank, 
              hierarchy_parent_rank, 
              hierarchy_level 
       INTO TABLE @FINAL(root).
```

When executed, this program demonstrates how the `ORPHANS` addition works.

- The first `SELECT` statement specifies the addition `ORPHANS IGNORE`. All orphan nodes are ignored and only the root node set consisting of a single root node is read and inserted in the SQL hierarchy.

- The next `SELECT` statement specifies the addition `ORPHANS ERROR`. The SQL hierarchy would contain orphan nodes and hence an exception is raised.

- The next `SELECT` statement specifies the addition `ORPHANS ROOT` and all orphan nodes are inserted in the SQL hierarchy:

  - The hierarchy node with the value *B* in the column `ID` is a true orphan node. It contains a blank in the column `PARENT_ID` but there is no root node with a blank in the column `ID`. The addition `ROOT` includes the hierarchy node itself in the root node set (the hierarchy column `HIERARCHY_PARENT_RANK` has the value 0) and the row is flagged as an orphan node in the hierarchy column `HIERARCHY_IS_ORPHAN`.

  - The hierarchy node with the value *C* in the column `ID` contains the value *B* in the column `PARENT_ID`. The parent node is an orphan node included in the root node set, which means that this hierarchy node is also flagged as an orphan node.

  - The hierarchy node with the value *X* in the column `ID` also contains the value *X* in the column `PARENT_ID`. The hierarchy node therefore starts a node cycle where this node is itself the parent node. It is not part of the root node set, however, which means it is an island orphan. A parent node is inserted into the root node set in which the columns of the CDS view `DEMO_CDS_PARENT_CHILD_SOURCE` and the hierarchy column `PARENT_ID`, contain null values.

  - The hierarchy nodes with the values `U`, `V`, and *W* in the column `ID` also comprise an island orphan. None of the hierarchy nodes in this node cycle is a root node. Again, a parent node is inserted in the root node set in which the columns of the CDS view and the hierarchy column `PARENT_ID`, contain null values.

## Addition 9

`... CYCLES ERROR|BREAKUP`

### Description

The addition `CYCLES` defines how [node cycles](../../abap-glossary/abennode_cycle_glosry.md) are defined. The additions work as follows:

- `ERROR`

  This is the default setting. An exception is raised when a node cycle is detected.

- `BREAKUP`

  The tracing of [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md) is terminated at the child node where the node cycle occurs and the [hierarchy column](abenddddl_hierarchy.md) `HIERARCHY_IS_CYCLE` is set to the value 1.

If the addition `BREAKUP` is specified, `MULTIPLE PARENTS ALLOWED` must also be specified.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Handling of node cycles in the class `CL_DEMO_HIERARCHY_CYCLES`.

``` abap
SELECT FROM HIERARCHY( SOURCE demo_cds_parent_child_source 
                       CHILD TO PARENT ASSOCIATION _relat 
                       START WHERE id = 'A' OR 
                                   id = 'X' OR 
                                   id = 'Y' OR 
                                   id = 'Z' 
                       MULTIPLE PARENTS ALLOWED 
                       CYCLES BREAKUP ) 
       FIELDS id, 
              parent, 
              hierarchy_is_cycle, 
              hierarchy_level 
       INTO TABLE @FINAL(breakup).
```

When executed, this program demonstrates how the `CYCLES` addition works.

- The first `SELECT` statement specifies the addition `CYCLES BREAKUP`. Here, the root node set consists of four root nodes of the CDS view `DEMO_CDS_PARENT_CHILD_SOURCE` and the following node cycles are detected:

  - The child node with the value *A* in the column `ID` is also its parent node. The hierarchy column `HIERARCHY_IS_CYCLE` contains the value 1 and no more descendant nodes are created.

  - Starting from the hierarchy node with the value *X* in the column `ID`, child nodes are created with the values `Y` and `Z` and again *X*. The cycle is detected at the final child node, `HIERARCHY_IS_CYCLE` contains the value 1, and no more descendant nodes are created. The same applies to the descendant nodes starting from the root nodes with the values `Y` and `Z`.

- The second `SELECT` statement specifies the addition `CYCLES ERROR` and raises an exception.

## Addition 10

`... LOAD BULK|INCREMENTAL|load_option`

### Description

The addition `LOAD` specifies the load policy for the generated hierarchy. It can be used for performance optimization.

The addition works as follows:

- `BULK`

  This is the default setting. The entire source table of the hierarchy is loaded.

- `INCREMENTAL`

  Only the rows of the source table that can be reached from the start nodes ([root node set](../../abap-glossary/abenroot_node_set_glosry.md)) are loaded.

- `load_option`

  `load_option` is an [enumerated object](../../abap-glossary/abenenumerated_object_glosry.md) with the [enumerated type](../../abap-glossary/abenenumerated_type_glosry.md) `LOAD_OPTION` from the class `SQL_HIERARCHY` and the following [enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md) can be passed:

  - `SQL_HIERARCHY=>C_LOAD_OPTION-BULK`: equivalent to `LOAD BULK`.

  - `SQL_HIERARCHY=>C_LOAD_OPTION-INCREMENTAL`: equivalent to `LOAD INCREMENTAL`.

### Hints

- The performance optimization with `LOAD INCREMENTAL` depends on the data source. If the source table is very large and the hierarchy generator reads relatively few rows, there is a positive effect. If, on the other hand, the source table has only few rows and they are all part of the hierarchy, `LOAD INCREMENTAL` might even take longer than `LOAD BULK`.

- `LOAD INCREMENTAL` should not be used with [global temporary tables](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_gtt.md) as data source, because it does not have any positive effect then (if anything, it slows down the performance).

### Executable Example

The executable example demonstrates how the addition `LOAD INCREMENTAL` can speed up the generation of a hierarchy.

[`BULK` vs `INCREMENTAL`](abenselect_hierarchy_abexa.md)

## Addition 11

`... GENERATE SPANTREE`

### Description

If the addition `GENERATE SPANTREE` is specified, the hierarchy generator inserts only child nodes without multiple parent nodes, starting from every root node. If, due to its parent-child relationships, a child node were to have multiple parent nodes after its root node, exactly one of the possible paths from the root node to this child node is selected and the child node is created for this path only.

- If the paths have different lengths, the shortest is selected.

- If the paths all have the same length, the first path found is selected.

If the addition `GENERATE SPANTREE` is specified, the following additions must be specified at the same time:

- `MULTIPLE PARENTS ALLOWED`

- `ORPHANS IGNORE` or `ORPHANS` not specified

- `CYCLES BREAKUP`

### Hints

- If the parent-child relationships for the current data produce only tree-like SQL hierarchies, the addition `GENERATE SPANTREE` is ignored.

- Selecting one of multiple paths to a child node does not mean that all others are completely discarded. In this case, only the edges leading to the child node are missing.

- The addition `GENERATE SPANTREE` can be used to detect whether at least one path leads from a root node to a child node without the result set needing to contain all paths.

- The addition `GENERATE SPANTREE` is used in an [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) to access the hierarchy generator function [`HIERARCHY_SPANTREE`](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/2969da89b87f4abd85fd0b5f9f5bc395) there.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of `GENERATE SPANTREE` in the class `CL_DEMO_HIERARCHY_SPANTREE`.

``` abap
SELECT FROM HIERARCHY( SOURCE demo_cds_parent_child_source 
                       CHILD TO PARENT ASSOCIATION _relat 
                       START WHERE id = 'A' OR 
                                   id = 'K' OR 
                                   id = 'X' OR 
                                   id = 'Y' 
                       MULTIPLE PARENTS ALLOWED 
                       CYCLES BREAKUP 
                       GENERATE SPANTREE ) 
       FIELDS id, 
              parent 
       INTO TABLE @FINAL(spantree).
```

When executed, this program demonstrates how the `GENERATE SPANTREE` addition works.

- The first `SELECT` statement does not specify the addition `GENERATE SPANTREE`. The SQL hierarchy contains all possible paths from root nodes to child nodes.

- The second `SELECT` statement specifies the addition `GENERATE SPANTREE`. Starting from each root node, the result set only contains one path to the potential child nodes:

  - From the root node with the value *A* in `ID`, two paths lead to `D`. Only the shorter path directly from *A* to `D` is created. The connection between `C` and `D` in the longer path is not created.

  - From the root node with the value *A* in `ID`, two paths lead to `N`. Only one of the two paths from `L` to `N` or `M` to `N` is created.

  - The child node with the value *Z* in `ID` has two parent nodes *X* and `Y`. Since both are root nodes, both paths are created.

## Addition 12

`... CACHE ON|OFF|FORCE`

### Description

The optional addition `CACHE` defines the caching policy for the generated hierarchy result. It can be used for performance optimization. The addition works as follows:

- `ON`

  The generated hierarchy is cached by the HANA database if the system assesses the source to be reliably deterministic. This is the default behavior.

- `OFF`

  The generated hierarchy is not cached by the HANA database.

- `FORCE`

  The generated hierarchy is cached by the HANA database even if the source cannot be assessed to be reliably deterministic.
