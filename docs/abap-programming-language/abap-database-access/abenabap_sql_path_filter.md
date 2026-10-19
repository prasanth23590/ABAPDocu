---
title: "ABAP SQL - Path Expressions, attributes"
source_file: abenabap_sql_path_filter.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Path Expressions sql_path"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Path Expressions, attributes

## Syntax

``` abap
... [ [[cardinality] [INNER|{LEFT|RIGHT OUTER}]] [[WHERE] sql_cond] ] 
  | [ [[INNER|{LEFT|RIGHT OUTER}] [cardinality]] [[WHERE] sql_cond] ]...  
```

[`sql_cond`](abenabap_sql_expr_logexp.md) · [`sql_cond`](abenabap_sql_expr_logexp.md)

### Addition

[1. `... cardinality`](abenabap_sql_path_filter.md#addition-1)

[2. `... INNER|{LEFT|RIGHT OUTER}`](abenabap_sql_path_filter.md#addition-2)

[3. `... [WHERE] sql_cond`](abenabap_sql_path_filter.md#addition-3)

## Overview

### Description

Attributes for a section of a path expression can be specified in square brackets for every [CDS association](../../abap-glossary/abencds_association_glosry.md) or [CTE association](../../abap-glossary/abencte_association_glosry.md) [`_assoc`](../../abap-glossary/abencds_association_glosry.md) of the [path expression](abenabap_sql_path.md) specified in a [data source](abapselect_data_source.md) of a [`FROM` clause](abapfrom_clause.md) or a [column specification](abenabap_sql_columns.md). The following can be done using these attributes:

- The [cardinality](../../abap-glossary/abencardinality_glosry.md) `cardinality` of the section can be declared.

- The type of the join expression can be specified.

- A filter condition `sql_cond` can be specified.

## Addition 1

`... cardinality`

### Description

The [cardinality](../../abap-glossary/abencardinality_glosry.md) `cardinality` of the current association `_assoc` is declared.

The cardinality can either be specified in syntax written in words or in numeric syntax in parentheses. The syntax written in words can specify a [source](../../abap-glossary/abensource_cardinality_glosry.md) and a [target cardinality](../../abap-glossary/abentarget_cardinality_glosry.md), while the numeric syntax only specifies a target cardinality. The syntax written in words is recommended.

- Cardinality syntax written in words:

  - `ONE TO ONE`

  - `ONE TO MANY`

  - `ONE TO EXACT ONE`

  - `EXACT ONE TO ONE`

  - `EXACT ONE TO MANY`

  - `EXACT ONE TO EXACT ONE`

  - `MANY TO ONE`

  - `MANY TO MANY`

  - `MANY TO EXACT ONE`

    If specified, the join type must precede the cardinality specification. For example: `\_assoc[ INNER MANY TO ONE ]-field AS alias`.

- Numeric cardinality syntax:

  - The target cardinality can be specified by the numbers `1` or `2` or by specifying the character `*` in parentheses `( )`.

    If specified, the join type must be placed after the cardinality specification. For example: `\_assoc[ (1) INNER ]-field AS alias`. If the cardinality is specified as `(1)`, a `LEFT OUTER JOIN` is defined implicitly using the addition [`MANY TO ONE`](abapselect_join.md) on database systems that support this, and the consequences of this should be noted.

Specifying the cardinality overwrites the original definition of the cardinality [`cardinality`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_cardinality_v2.md) or [`TO ONE|MANY`](abapwith_associations_defining.md) of the current association with the new cardinality.

- The cardinality can be specified to prevent syntax warnings or syntax errors in cases where the cardinality of the association does not match the way it is used in a path expression of a `SELECT` statement or affects the way it is used.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Paths specified with an explicitly specified cardinality of CDS associations in the `SELECT` list. If supported by the database, only the left outer join between the DDIC database tables `SPFLI` and `SAIRPORT` is defined using the addition `MANY TO ONE`.

``` abap
SELECT scarr~carrname, 
       \_spfli[ MANY TO MANY ]-connid       AS connid, 
       \_spfli[ MANY TO MANY ]\_sflight[ MANY TO MANY ]-fldate 
                                            AS fldate, 
       \_spfli[ MANY TO MANY ]\_sairport[ 
                MANY TO ONE ]-name          AS name 
       FROM demo_cds_assoc_scarr            AS scarr 
       WHERE scarr~carrid = '...' 
       ORDER BY carrname, connid, fldate 
       INTO TABLE @FINAL(result).
```

## Addition 2

`... INNER|{LEFT|RIGHT OUTER}`

### Description

This addition defines the [join type](../../abap-glossary/abenjoin_type_glosry.md) into which the current association `_assoc` is transformed:

- `INNER` specifies an [inner join](../../abap-glossary/abeninner_join_glosry.md).

- `LEFT|RIGHT OUTER` specifies a [left outer join](../../abap-glossary/abenleft_outer_join_glosry.md) or a [right outer join](../../abap-glossary/abenright_outer_join_glosry.md).

The join type can only be specified together with the cardinality.

If the join type is not specified explicitly, the type depends on the place where the path expression is used:

- When [columns are specified](abenabap_sql_columns.md) in `SELECT` statements, a `LEFT OUTER JOIN` is used.

- An `INNER JOIN` is used as a [data source](abapselect_data_source.md) of the [`FROM` clause](abapfrom_clause.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Path specifications with an explicitly specified cardinality and a switch of the left outer joins to inner joins in the columns specified in the `SELECT` list.

``` abap
SELECT scarr~carrname, 
       \_spfli[ INNER MANY TO ONE ]-connid AS connid, 
       \_spfli[ INNER MANY TO ONE ]\_sflight[ INNER MANY TO ONE 
         ]-fldate 
                                           AS fldate, 
       \_spfli[ INNER MANY TO ONE ]\_sairport[ INNER MANY TO ONE 
         ]-name 
                                           AS name 
       FROM demo_cds_assoc_scarr           AS scarr 
       WHERE scarr~carrid = 'LH' 
       ORDER BY carrname, connid, fldate 
       INTO TABLE @FINAL(result).
```

## Addition 3

`... [WHERE] sql_cond`

### Description

Specifies a [filter condition](../../abap-glossary/abenfilter_condition_glosry.md) [`sql_cond`](abenabap_sql_expr_logexp.md) for the current association `_assoc`. The addition `WHERE` is optional in cases where the filter condition is the only item specified in the square brackets. The addition must be specified if one of the other additions is used first.

When the association is resolved in a join, the filter condition is converted to an extended condition for the join. If no filter condition is specified in the path expression, the default filter condition defined using [`WITH DEFAULT FILTER`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_association_v2.md) is used in the case of a CDS association.

Columns specified in the filter condition `sql_cond` always refer to the target [`target`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_association_v2.md) or [`target`](abapwith_associations_defining.md) of the association for which the condition is specified. An explicit name must not and cannot be specified with the [column selector](../../abap-glossary/abentable_comp_selector_glosry.md) `~` in front of a column specification.

### Hints

- The [relational expressions](abenabap_sql_expr_logexp.md) that can be used in a filter condition are a subset of the [relational expressions for statements](abenabap_sql_stmt_logexp.md), but also allow [SQL expressions](abapsql_expr.md) as operands on the right side.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specification of filter conditions in a path expression.

``` abap
SELECT carrid, connid, fldate, price 
       FROM demo_cds_assoc_scarr 
            \_spfli[   airpfrom = 'FRA' ] 
            \_sflight[ currency  = 'EUR' AND 
                       price  BETWEEN 500 AND 1500 ] 
            AS flights 
       ORDER BY carrid, connid, fldate, price 
       INTO TABLE @FINAL(result).
```
