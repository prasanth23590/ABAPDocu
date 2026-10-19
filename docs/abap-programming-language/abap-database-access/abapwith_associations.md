---
title: "WITH, ASSOCIATIONS"
source_file: abapwith_associations.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > WITH"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# WITH, ASSOCIATIONS

## Syntax

``` abap
... WITH ASSOCIATIONS ( path 
                       |join[, 
                        ...] ) 
                     |(assoc_syntax)  
```

[`path`](abapwith_associations_using.md) · [`join`](abapwith_associations_defining.md)

## Description

The addition `WITH ASSOCIATIONS` for the definition of a common table expression exposes associations of this table expression for use in the subsequent queries of a [`WITH`](abapwith.md) statement. The following can be specified:

- Existing [CDS associations](../../abap-glossary/abencds_association_glosry.md) or [CTE associations](../../abap-glossary/abencte_association_glosry.md) of the common table expression using [SQL path expressions](../../abap-glossary/abensql_path_expression_glosry.md) [`path`](abapwith_associations_using.md).

- Definitions of new [CTE associations](../../abap-glossary/abencte_association_glosry.md) of the common table expression using [`join`](abapwith_associations_defining.md).

The parentheses must contain at least one association and multiple associations can be specified as a comma-separated list. Both existing and new associations can be specified together and in any order.

- In subsequent queries of the current `WITH` statement, the exposed associations can be used as root elements of the path expressions in question.

  - In the [specified columns](abenabap_sql_columns.md) of `SELECT` statements of the subsequent queries.

  - As a [data source](abapselect_data_source.md) of the [`FROM` clause](abapfrom_clause.md) of the subsequent queries.

- Exposed [self-associations](../../abap-glossary/abenself_association_glosry.md) can be specified in the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](abenselect_hierarchy_generator.md) as a [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md).

- An exposed association can be exposed again by a subsequent common table expression of the current `WITH` statement using the addition `WITH ASSOCIATIONS`, as long as this addition uses the exposing table expression as a data source. Different [attributes](abenabap_sql_path_filter.md) can be specified here.

Instead of specifying associations statically in parentheses, a parenthesized data object `assoc_syntax` can be specified. When the statement is executed, the data object must contain the syntax shown for the static specification. In this case, the common table expression can be used only in other dynamic tokens of the `WITH` statement. The data object `assoc_syntax` can be a character-like data object or a [standard table](../../abap-glossary/abenstandard_table_glosry.md) with a character-like row type. The syntax in `assoc_syntax`, as in the static syntax, is not case-sensitive. When an internal table is specified, the syntax can be distributed across multiple rows. Invalid syntax raises a catchable exception from the class `CX_SY_DYNAMIC_OSQL_ERROR`.

If an association is exposed more than once under different alias names, it is handled as a separate association when used in a path expression. A separate instance of a join expression is created for each association used and each expression uses the result set of the exposing common table expression as its left side.

The addition `WITH ASSOCIATIONS` cannot be used if the subquery of the common table expression contains the [set operator](../../abap-glossary/abencds_set_operators_glosry.md) [`UNION`](abapunion.md), [`INTERSECT`](abapunion.md), or [`EXCEPT`](abapunion.md). Furthermore, it is not possible to use the addition `USING` in the current CTE, nor in CTEs where the addition `REDIRECTED TO` is applied, nor in queries that use the association in a path expression and that transform it to a join expression.

## Hints

- When an association of the data source of a common table expression is exposed using `WITH ASSOCIATION`, this is the same as [exposing](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_select_list_association_v2.md) an association of the data source of a CDS view entity in its `SELECT` list.

- It should be noted that the exposing common table expression itself is the [association source](../../abap-glossary/abenassociation_source_glosry.md) of the exposed association and not the data source of the expression. The exposing common table expression replaces the original [association source](../../abap-glossary/abenassociation_source_glosry.md) of the association. The left side of a join expression created for the exposed association is the result set of the subquery of the common table expression.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example class `CL_DEMO_WITH_ASSOCIATIONS` demonstrates how CDS associations are exposed by common table expressions. It works in the same way as the [executable example](abenpath_expr_in_from_clause_abexa.md) for using path expressions in the `FROM` clause. The main query uses the alias name `_spfli_scarr` to access the [association target](../../abap-glossary/abenassociation_target_glosry.md) `SCARR` of the final CDS association `_scarr` of the path expression `\_spfli[ fltime > @fltime ]\_scarr` exposed for the common table expression `+cte`. The `SELECT` list of the common table expression must specify the component `\_spfli-carrid` with the same filter condition `fltime > @fltime` as in the exposed association so that the associated join can be created.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: 
  tz     TYPE s_tzone    VALUE 'UTC+1', 
  currc  TYPE s_currcode VALUE 'EUR', 
  fltime TYPE s_fltime   VALUE 0. 
 
cl_demo_input=>new( 
  )->add_field( CHANGING field = tz 
  )->add_field( CHANGING field = currc 
  )->add_field( CHANGING field = fltime )->request( ). 
 
WITH 
  +cte AS ( SELECT \_spfli[ MANY TO MANY 
                            WHERE fltime > @fltime ]-carrid 
                   FROM demo_cds_assoc_sairport_tz( 
                     tz = @( to_upper( tz ) ) ) ) 
       WITH ASSOCIATIONS ( \_spfli[ MANY TO MANY 
                                    WHERE fltime > @fltime ] 
                           \_scarr AS _spfli_scarr ) 
  SELECT DISTINCT carrname 
         FROM +cte\_spfli_scarr[ 
                currcode = @( CONV s_currcode( to_upper( currc ) ) ) ] 
                  AS scarr 
         ORDER BY carrname 
         INTO TABLE @FINAL(result). 
 
out->write( result ). 
 
out->display( ).
```
