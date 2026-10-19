---
title: "ABAP SQL - col"
source_file: abenabap_sql_columns.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Operands sql_elem"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - col

## Syntax

``` abap
... [data_source|tabalias~]colname 
  | [data_source|tabalias~]sql_path-element ...  
```

[`sql_path`](abenabap_sql_path.md)

### Variant

[1. `... colname`](abenabap_sql_columns.md#variant-1)

[2. `... sql_path-element`](abenabap_sql_columns.md#variant-2)

### Addition

[`... data_source|tabalias~`](abenabap_sql_columns.md#addition)

## Overview

### Description

Specifies a column of a [data source](abapselect_data_source.md) of a [query](../../abap-glossary/abenasql_query_glosry.md) or the target of a [write](abenabap_sql_writing.md) in an ABAP SQL statement.

Columns can be specified as [elementary SQL expressions](abensql_elem.md) in all operand positions in which [SQL expressions](abapsql_expr.md) are possible. However, they can also occur in specific operand positions in which no SQL expressions are possible.

## Variant 1

`... colname`

### Description

Specifies a column of a [data source](abapselect_data_source.md) of a [query](../../abap-glossary/abenasql_query_glosry.md) or of the target of a [write](abenabap_sql_writing.md) directly using its name `colname` (as defined as a component of the associated DDIC structure).

### Hint

For a column specification, the actual names of the components must be used for a DDIC database table that contains an [include structure](../../abap-dictionary-ddic/ddic-data-types/abenddic_include_structure.md), and not the names of any groups defined in the ABAP Dictionary.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Direct column specification `carrid`, `carrname`, and `url` in the clauses of a [`SELECT`](abapselect.md) statement.

``` abap
SELECT FROM   scarr 
       FIELDS carrid, carrname 
       WHERE  url = ' ' 
       INTO   TABLE @FINAL(itab).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A [`SELECT`](abapselect.md) statement accesses the CDS view entity `demo_cds_enum_type_usage_1` that defines one enumerated element `friday`. This CDS enumerated element is used as column in the `SELECT` list, as operand in the `WHERE` clause, and as operand in the `ORDER BY` clause.

``` abap
SELECT friday AS EnumElement 
       FROM demo_cds_enum_type_usage_1 
       WHERE friday = @demo_cds_enum_weekday-fri 
       ORDER BY friday 
       INTO TABLE @FINAL(itab).
```

## Variant 2

`... sql_path-element`

### Description

Specifies an element of a data source of a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) after a path expression [`sql_path`](abenabap_sql_path.md). This can be specified in `SELECT` statements where path expressions can be used in all places where a column can be specified, unless otherwise indicated.

The element `element` closes the path expression constructed from [CDS associations](../../abap-glossary/abencds_association_glosry.md) or [CTE associations](../../abap-glossary/abencte_association_glosry.md), for which the structure component selector `-` is used. This element must be an element of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the final association in the path.

### Hints

- [Path expressions](abenabap_sql_path.md) can be used in the following `SELECT` statements:

  - Statements that use the [CDS entity](../../abap-glossary/abencds_entity_glosry.md) to access a [CDS view](../../abap-glossary/abencds_view_glosry.md) in which the used associations are exposed for use from outside.

  - Statements in a [`WITH`](abapwith.md) statement that follow [common table expressions](../../abap-glossary/abencommon_table_expression_glosry.md) that themselves expose associations using the addition [`WITH ASSOCIATIONS`](abapwith_associations.md).

- If an element is specified after the path expression, this represents a column specified of the join created implicitly for the path expression. Left outer joins (`LEFT OUTER JOIN`) are created for path expressions in specified columns.

- [`source~`](abenabap_sql_path.md) can be used to prefix the path expression with the unit from which its first association is exposed.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A [`SELECT`](abapselect.md) statement accesses the [CDS view](../../abap-glossary/abencds_view_glosry.md) `demo_cds_assoc_scarr` that exposes a CDS association `_spfli`. As its [association target](../../abap-glossary/abenassociation_target_glosry.md), this CDS association uses a view that exposes the CDS associations `_sflight` and `_sairport`. The columns specified in the `SELECT` statement include any path expressions created by these CDS associations. See also the associated [executable example](abenpath_expr_in_colspec_abexa.md).

``` abap
SELECT carrname, 
        \_spfli[ MANY TO MANY ]-connid AS connid, 
        \_spfli[ MANY TO MANY ]\_sairport-name AS name 
        FROM demo_cds_assoc_scarr 
        WHERE carrid = '...' and 
              \_spfli[ MANY TO MANY ]\_sflight[ 
                       MANY TO MANY ]-fldate > '20190515' 
        INTO TABLE @FINAL(itab).
```

## Addition

`... data_source|tabalias~`

### Description

The [column selector](../../abap-glossary/abentable_comp_selector_glosry.md) `~` can be used to prefix every specified column directly with the name of the associated data source of a query or of the target of a write (as `data_source` or as an alias name `tabalias`).

The data source must be specified in the following cases:

- If multiple [data sources](abapselect_data_source.md) in an ABAP SQL statement are edited and the column name is not unique.

- On the right-hand side of the [relational expressions](abenabap_sql_stmt_logexp.md) of SQL conditions [`sql_cond`](abenasql_cond.md) for statements.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of the name `scarr` of a data source and the alias name `connections` of a different data source in front of the column selector `~` of specified columns.

``` abap
SELECT FROM scarr 
         INNER JOIN spfli AS connections 
           ON scarr~carrid = connections~carrid 
       FIELDS scarr~carrname, connections~connid 
       WHERE  connections~cityfrom = '...' 
       INTO TABLE @FINAL(itab).
```
