---
title: "WITH, ASSOCIATIONS, JOIN"
source_file: abapwith_associations_defining.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > WITH > WITH, ASSOCIATIONS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# WITH, ASSOCIATIONS, JOIN

## Syntax

``` abap
... JOIN cardinality target AS _assoc 
      ON sql_cond ...  
```

[`sql_cond`](abenabap_sql_expr_logexp.md)

### Addition

[`... cardinality`](abapwith_associations_defining.md#addition)

## Overview

### Description

Specifying `JOIN` initiates the definition and exposure of a [CTE association](../../abap-glossary/abencte_association_glosry.md) with the name `_assoc` in the addition [`WITH ASSOCIATIONS`](abapwith_associations.md) when a common table expression is defined in a [`WITH`](abapwith.md) statement.

A CTE association joins the current common table expression `+cte` as an [association source](../../abap-glossary/abenassociation_source_glosry.md) with the [association target](../../abap-glossary/abenassociation_target_glosry.md) `target` specified in the definition of the CTE association using an `ON` condition [`sql_cond`](abenabap_sql_expr_logexp.md). All [data sources](abapselect_data_source.md) visible and usable in this position can be specified for `target`.

`AS` must be used to specify a name `_assoc` for the CTE association under which it can be addressed in the subsequent queries of the current `WITH` statement. The name can contain letters, digits, the minus sign (`-`), and the underscore (`_`) in any order.

By specifying its name, a CTE association of a common table expression can be used in the subsequent queries of the same `WITH` statement in all operand positions for associations. These are elements of [path expressions](abenabap_sql_path.md) or the specification of [hierarchy associations](../../abap-glossary/abenhierarchy_association_glosry.md).

When a CTE association is used in a path expression, it is transformed to a join expression. The [association source](../../abap-glossary/abenassociation_source_glosry.md) represents the left side and the [association target](../../abap-glossary/abenassociation_target_glosry.md) represents the right side. The `ON` condition of the CTE association is added to the `ON` condition of the join. The category of the join is determined by where the path expression is used:

- After [`FROM`](abapfrom_clause.md), it is an inner join (`INNER JOIN`)

- As a [column specification](abenabap_sql_columns.md), it is a left outer join (`LEFT OUTER JOIN`)

The following applies when the `ON` condition [`sql_cond`](abenabap_sql_expr_logexp.md) is specified:

- Any fields in the [association target](../../abap-glossary/abenassociation_target_glosry.md) can be prefixed with the name of the CTE association `_assoc.`. Any fields in the [association source](../../abap-glossary/abenassociation_source_glosry.md) can be prefixed with the name of the common table expression `+cte`. The prefix is separated using the [column selector](../../abap-glossary/abentable_comp_selector_glosry.md) `~`. These specifications are mandatory only if the names of the fields occur in both data sources.

- Any fields of the [association source](../../abap-glossary/abenassociation_source_glosry.md) specified in the `ON` condition must be listed in the [`SELECT` list](abapselect_list.md) of the common table expression so that a join expression can be built from the CTE association when used in a path expression. The names defined in the common table expression must be used here. These are either the alias names defined using `AS` or the names defined in an optional name list.

### Hints

- A CTE association cannot be used in the same common table expression for which it is defined.

- More specifically, [internal tables](abapselect_itab.md) or previously defined common table expressions of the same `WITH` statement and the current common table expression itself can also be specified as [association targets](../../abap-glossary/abenassociation_target_glosry.md). The latter is a [self-association](../../abap-glossary/abenself_association_glosry.md).

- It is advisable to use an underscore `_` as the first character of the CTE association name.

- The character `+` cannot be used as the first character of a CTE association name, which means there can be no naming conflicts in the `ON` condition.

- A common table expression that defines and exposes a self-association can be used as the source of the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](abenselect_hierarchy_generator.md). More specifically, this makes it possible to also use internal tables as the source of hierarchies.

## Addition

`... cardinality`

### Description

It is mandatory to specify a [cardinality](../../abap-glossary/abencardinality_glosry.md) `cardinality`. A cardinality for both the source and the target, or only for the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the CTE association is possible. The following options are available:

- `ONE TO ONE`

- `ONE TO MANY`

- `ONE TO EXACT ONE`

- `EXACT ONE TO ONE`

- `EXACT ONE TO MANY`

- `EXACT ONE TO EXACT ONE`

- `MANY TO ONE`

- `MANY TO MANY`

- `MANY TO EXACT ONE`

- `TO ONE`

- `TO MANY`

This cardinality is used by some database systems for performance optimizations. This works in the same way as for cardinality specifications in [join expressions](abapselect_join.md). This means that an optimization is attempted, and the result can be undefined if the result set does not match the cardinality.

### Hint

To avoid undefined and platform-dependent behavior, the cardinality should always be defined to match the data to be read.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following `WITH` statement from the class `CL_DEMO_WITH_ASSOCIATIONS_JOIN` demonstrates the way [CTE associations](../../abap-glossary/abencte_association_glosry.md) are defined and used. The example works in exactly the same way as the [executable example](abenpath_expr_in_from_clause_abexa.md) for path expressions in the `FROM` clause. The CDS views and CDS associations used here are replaced one by one by common table expressions and CTE associations. When executing `CL_DEMO_WITH_ASSOCIATIONS_JOIN`, the class displays the result and compares the behavior of CTE associations and CDS associations when accessed.

``` abap
DATA: 
  tz     TYPE s_tzone    VALUE 'UTC+1', 
  currc  TYPE s_currcode VALUE 'EUR', 
  fltime TYPE s_fltime   VALUE 0. 
 
WITH 
  +spfli_scarr AS 
     ( SELECT FROM spfli 
              FIELDS carrid, 
                     airpfrom, 
                     fltime ) 
        WITH ASSOCIATIONS ( JOIN MANY TO ONE scarr AS _scarr 
          ON +spfli_scarr~carrid = _scarr~carrid ), 
   +sairport_tz AS 
     ( SELECT FROM sairport 
              FIELDS id 
              WHERE time_zone = @tz ) 
        WITH ASSOCIATIONS ( JOIN MANY TO ONE +spfli_scarr AS _spfli 
          ON +sairport_tz~id = _spfli~airpfrom ) 
   SELECT DISTINCT carrname 
          FROM +sairport_tz 
               \_spfli[ fltime > @fltime ] 
               \_scarr[ currcode = @( CONV s_currcode( 
                                             to_upper( currc ) ) ) ] 
               AS scarr 
          ORDER BY carrname 
          INTO TABLE @FINAL(result_cte_assoc).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following `WITH` statement from the class `CL_DEMO_WITH_ASSCTNS_HIERA` demonstrates the way a common table expression `+parent_child_source` and its CTE association `_relat` are used as the data source and [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md) of the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](abenselect_hierarchy_generator.md). The CTE association `_relat` is a [self-association](../../abap-glossary/abenself_association_glosry.md). When executing `CL_DEMO_WITH_ASSCTNS_HIERA`, the class displays the result and compares it with the result when a similar CDS view and CDS association are used in the hierarchy generator.

``` abap
FINAL(start_id) = CONV demo_parent_chld-id( 'A' ). 
 
WITH 
  +parent_child_source AS 
     ( SELECT FROM demo_parent_chld 
              FIELDS id, 
                     parent_id AS parent ) 
       WITH ASSOCIATIONS ( JOIN MANY TO MANY +parent_child_source 
                             AS _relat 
         ON +parent_child_source~parent = _relat~id ) 
   SELECT FROM HIERARCHY( SOURCE +parent_child_source 
                          CHILD TO PARENT ASSOCIATION _relat 
                          START WHERE id = @start_id 
                          SIBLINGS ORDER BY id 
                          MULTIPLE PARENTS ALLOWED ) 
         FIELDS id, 
                parent, 
                hierarchy_rank, 
                hierarchy_tree_size, 
                hierarchy_parent_rank, 
                hierarchy_level, 
                hierarchy_is_cycle, 
                hierarchy_is_orphan, 
                node_id, 
                parent_id 
         INTO TABLE @FINAL(cte_result).
```
