---
title: "SELECT, FROM hierarchy_node_navigator"
source_file: abenselect_hierarchy_node_navis.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source > SELECT, FROM hierarchy_data > SELECT, FROM hierarchy_navigator"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, FROM hierarchy_node_navigator

## Syntax

``` abap
... {HIERARCHY_DESCENDANTS 
    |HIERARCHY_ANCESTORS 
    |HIERARCHY_SIBLINGS}( 
       SOURCE hierarchy 
       START WHERE sql_cond 
      [DISTANCE [FROM n1] [TO n2]] ) ...  
```

[`hierarchy`](abenselect_hierarchy.md) · [`sql_cond`](abenabap_sql_expr_logexp.md)

### Variant

[1. `HIERARCHY_DESCENDANTS( ... )`](abenselect_hierarchy_node_navis.md#variant-1)

[2. `HIERARCHY_ANCESTORS( ... )`](abenselect_hierarchy_node_navis.md#variant-2)

[3. `HIERARCHY_SIBLINGS( ... )`](abenselect_hierarchy_node_navis.md#variant-3)

### Addition

[`... DISTANCE [FROM n1] [TO n2]`](abenselect_hierarchy_node_navis.md#addition)

## Overview

### Description

Specifies a [hierarchy node navigator](../../abap-glossary/abenhierarchy_node_navi_glosry.md) as a data source [`data_source`](abapselect_data_source.md) in an ABAP SQL [query](../../abap-glossary/abenasql_query_glosry.md). It accesses and evaluates the [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) [`hierarchy`](abenselect_hierarchy.md) specified after `SOURCE`.

After `START WHERE`, a logical expression [`sql_cond`](abenabap_sql_expr_logexp.md) must be specified that contains conditions for [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md) of the SQL hierarchy after `SOURCE`. The columns of the hierarchy can also be used as operands here. Any hierarchy nodes that meet the conditions are the [start nodes](../../abap-glossary/abenstart_node_glosry.md) of the hierarchy navigators. They evaluate the SQL hierarchy [`hierarchy`](abenselect_hierarchy.md) specified after `SOURCE`, starting from all start nodes, and insert the selected hierarchy nodes into their result set.

In addition to the [hierarchy columns](abenddddl_hierarchy.md) of the SQL hierarchy specified after `SOURCE`, the result set of each of these hierarchy navigators contains two further hierarchy columns:

- `START_RANK` with the type `INT8`

- `START_ID` with the type `SSTRING` and length 1333

In each row of the result set, these columns contain the values of the [hierarchy columns](abenddddl_hierarchy.md) `HIERARCHY_RANK` and `NODE_ID` of the associated start nodes.

## Variant 1

`HIERARCHY_DESCENDANTS( ... )`

### Description

The hierarchy navigator `HIERARCHY_DESCENDANTS` selects all [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md) of the [start nodes](../../abap-glossary/abenstart_node_glosry.md) and the start nodes themselves, from the SQL hierarchy [`hierarchy`](abenselect_hierarchy.md) specified after `SOURCE`. In addition the [hierarchy columns](abenddddl_hierarchy.md) of the SQL hierarchy specified after `SOURCE`, plus `START_RANK` and `START_ID`, the result set contains a further hierarchy column, `HIERARCHY_DISTANCE`, with the type `INT4`, which contains the distance to the respective start node. This distance is the positive difference between the hierarchy levels `HIERARCHY_LEVEL` of the individual [child nodes](../../abap-glossary/abenchild_node_glosry.md) and the respective start nodes.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Call of the hierarchy navigator `HIERARCHY_DESCENDANTS` in the class `CL_DEMO_HIERARCHY_NAVIGATORS`, where the hierarchy generator `HIERARCHY` is specified as the source. When executed, `CL_DEMO_HIERARCHY_NAVIGATORS` demonstrates how this hierarchy navigator works. It also displays the value of the hierarchy column `HIERARCHY_DISTANCE`.

``` abap
FINAL(id) = 6. 
 
SELECT FROM HIERARCHY_DESCENDANTS( 
              SOURCE HIERARCHY( 
                       SOURCE demo_cds_simple_tree_source 
                       CHILD TO PARENT ASSOCIATION _tree 
                       START WHERE id = 1 
                       SIBLINGS ORDER BY id ASCENDING ) 
             START WHERE id = @id ) 
       FIELDS id, 
              parent_id, 
              hierarchy_rank, 
              hierarchy_level, 
              hierarchy_tree_size, 
              hierarchy_distance 
         INTO TABLE @FINAL(descendants).
```

## Variant 2

`HIERARCHY_ANCESTORS( ... )`

### Description

The hierarchy navigator `HIERARCHY_ANCESTORS` selects all [ancestor nodes](../../abap-glossary/abenancestor_node_glosry.md) of the [start nodes](../../abap-glossary/abenstart_node_glosry.md), as well as the start nodes themselves, from the SQL hierarchy specified after `SOURCE`. In addition to the [hierarchy columns](abenddddl_hierarchy.md) of the SQL hierarchy specified after `SOURCE`, plus `START_RANK` and `START_ID`, the result set contains a further hierarchy column, `HIERARCHY_DISTANCE`, with the type `INT4`, which contains the distance to the respective start node. This distance is the negative difference between the hierarchy levels `HIERARCHY_LEVEL` of the individual [parent nodes](../../abap-glossary/abenparent_node_glosry.md) and the respective start nodes.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Call of the hierarchy navigator `HIERARCHY_ANCESTORS` in the class `CL_DEMO_HIERARCHY_NAVIGATORS`, where the CDS hierarchy `DEMO_CDS_SIMPLE_TREE` is specified as a source. When executed, this class demonstrates how this hierarchy navigator works. It also displays the value of the additional hierarchy column `HIERARCHY_DISTANCE`.

``` abap
FINAL(id) = 6. 
 
SELECT FROM HIERARCHY_ANCESTORS( 
              SOURCE demo_cds_simple_tree( p_id = 1 ) 
              START WHERE id = @id ) 
       FIELDS id, 
              parent_id, 
              hierarchy_rank, 
              hierarchy_level, 
              hierarchy_tree_size, 
              hierarchy_distance 
       INTO TABLE @FINAL(ancestors).
```

## Variant 3

`HIERARCHY_SIBLINGS( ... )`

### Description

The hierarchy navigator `HIERARCHY_SIBLINGS` selects all [sibling nodes](../../abap-glossary/abensibling_node_glosry.md) of the [start nodes](../../abap-glossary/abenstart_node_glosry.md), as well as the start nodes themselves, from the SQL hierarchy specified after `SOURCE`. In addition to the [hierarchy columns](abenddddl_hierarchy.md) of the SQL hierarchy specified after `SOURCE`, plus `START_RANK` and `START_ID`, the result set contains a further hierarchy column, `HIERARCHY_SIBLING_DISTANCE`, with the type `INT4`, which contains the distance to the respective start node. This is the positive or negative difference between the numbers `HIERARCHY_RANK` of the sibling nodes and the respective start nodes.

### Hint

If the values in the additional column `HIERARCHY_SIBLING_DISTANCE` are accessed, the addition `SIBLINGS ORDER BY` should be used in the SQL hierarchy specified after `SOURCE`. Otherwise, the values remain undefined.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Call of the hierarchy navigator `HIERARCHY_SIBLINGS` in the class `CL_DEMO_HIERARCHY_NAVIGATORS`, where the [CTE hierarchy](../../abap-glossary/abencte_hierarchy_glosry.md) `+hierarchy` is specified a source. When executed, this class demonstrates how this hierarchy navigator works. It also displays the value of the additional hierarchy column `HIERARCHY_SIBLING_DISTANCE`.

``` abap
FINAL(id) = 6. 
 
WITH +hierarchy AS ( 
        SELECT FROM HIERARCHY( 
                      SOURCE demo_cds_simple_tree_source 
                      CHILD TO PARENT ASSOCIATION _tree 
                      START WHERE id = 1 
                      SIBLINGS ORDER BY id ASCENDING ) AS hierarchy 
               FIELDS id, 
                      parent ) WITH HIERARCHY hierarchy 
  SELECT FROM HIERARCHY_SIBLINGS( 
                SOURCE +hierarchy 
                START WHERE id = @id ) 
         FIELDS id, 
                parent_id, 
                hierarchy_rank, 
                hierarchy_level, 
                hierarchy_tree_size, 
                hierarchy_sibling_distance 
         INTO TABLE @FINAL(siblings).
```

## Addition

`... DISTANCE [FROM n1] [TO n2]`

### Description

In the case of the hierarchy navigators `HIERARCHY_DESCENDANTS` and `HIERARCHY_ANCESTORS`, the addition `DISTANCE` restricts the distance to the respective [start node](../../abap-glossary/abenstart_node_glosry.md). The addition `DISTANCE` cannot be specified for the hierarchy navigator `HIERARCHY_SIBLINGS`.

At least one of the additions `FROM` or `TO` must be specified in the order shown. `n1` and `n2` expect [host variables](abenabap_sql_host_variables.md), [host expressions](abenabap_sql_literals.md), or [literals](abenabap_sql_literals.md) with the type `i`. Only the types `b`, `s`, or `i` can be used. Only those hierarchy nodes are selected for which the value of the hierarchy column `HIERARCHY_DISTANCE` is between the values of `n1` and `n2`. If the value of `n1` is greater than `n2`, no hierarchy node is selected. If `TO`, is not specified, there is no upper limit. If `FROM`, is not specified, there is no lower limit.

### Hints

- The function of the addition `DISTANCE` can also be achieved using the comparison operator [`BETWEEN`](abenwhere_logexp_interval.md) for the hierarchy column `HIERARCHY_DISTANCE`. In this case, the selection is applied to the result set of the hierarchy navigator rather than being performed by the navigator itself.

- To get hierarchy nodes in the result set of `HIERARCHY_DESCENDANTS`, the interval boundaries must include positive values. To get hierarchy nodes in the result set of `HIERARCHY_ANCESTORS`, the interval boundaries must include negative values.

- To exclude the start nodes from the result set, the additions `FROM` and `TO` can be used as follows:

  - If `FROM 1` is specified without the addition `TO`, `HIERARCHY_DESCENDANTS` selects only [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md)

  - If `TO -1` is specified without the addition `FROM`, `HIERARCHY_ANCESTORS` selects only the [ancestor nodes](../../abap-glossary/abenancestor_node_glosry.md)

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Call of the hierarchy navigator `HIERARCHY_DESCENDANTS` in the class `CL_DEMO_HIERARCHY_DISTANCE` while specifying the addition `DISTANCE`. When executed, this class demonstrates how this addition works. If, for example, the value *2* is specified for `n1` and `3` is specified for `n2`, only the grandchildren nodes and great-grandchildren nodes of the start node are selected. If `-3` is specified for `n1` and `-2` is specified for `n2`, the result set of `HIERARCHY_DESCENDANTS` is empty. For these values, on the other hand, the result set of `HIERARCHY_ANCESTORS` contains the grandparents and great-grandparents of the start node.

``` abap
FINAL(id) = 1. 
FINAL(n1) = 2. 
FINAL(n2) = 3. 
 
SELECT FROM HIERARCHY_DESCENDANTS( 
              SOURCE HIERARCHY( 
                       SOURCE demo_cds_simple_tree_source 
                       CHILD TO PARENT ASSOCIATION _tree 
                       START WHERE id = 1 
                       SIBLINGS ORDER BY id ASCENDING ) 
            START WHERE id = @id 
            DISTANCE FROM @n1 TO @n2 ) 
       FIELDS id, 
              parent_id, 
              hierarchy_rank, 
              hierarchy_level, 
              hierarchy_tree_size, 
              hierarchy_distance 
       INTO TABLE @FINAL(descendants).
```
