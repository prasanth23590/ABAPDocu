---
title: "ABAP SQL - SQL Path Expressions sql_path"
source_file: abenabap_sql_path.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - SQL Path Expressions sql_path

## Syntax

``` abap
... [source~]\_assoc1[sql_para][attributes] 
            [\_assoc2[sql_para][attributes]] 
            [\...] ...  
```

[`sql_para`](abenabap_sql_parameters.md) · [`attributes`](abenabap_sql_path_filter.md) · [`sql_para`](abenabap_sql_parameters.md) · [`attributes`](abenabap_sql_path_filter.md)

## Description

Specifies an [SQL path expression](../../abap-glossary/abensql_path_expression_glosry.md). ABAP SQL statements can contain path expressions in certain operand positions whose root element must be a [CDS association](../../abap-glossary/abencds_association_glosry.md) or [CTE association](../../abap-glossary/abencte_association_glosry.md) exposed as follows:

- In the same `SELECT` statement of a [query](../../abap-glossary/abenasql_query_glosry.md), the name of the [CDS entity](../../abap-glossary/abencds_entity_glosry.md) is used to access one of the following [data sources](abapselect_data_source.md):

  - A [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) that [exposes](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_select_list_association_v2.md) the CDS association in its [`SELECT` list](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_select_list_v2.md).

  - A [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) that [exposes](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_select_list_association_v1.md) the CDS association in its [`SELECT` list](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_select_list_v1.md).

  - A [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md) that [exposes](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_hiera_element.md) the CDS association in its [element list](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_hiera_element_list.md).

- In a [`WITH`](abapwith.md) statement, the association with the addition [`WITH ASSOCIATIONS`](abapwith_associations.md) is exposed by a preceding [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md). This can be one of the following:

  - [CDS association](../../abap-glossary/abencds_association_glosry.md) or [CTE association](../../abap-glossary/abencte_association_glosry.md) [exposed](abapwith_associations_using.md) using a path expression.

  - [CTE association](../../abap-glossary/abencte_association_glosry.md) [defined and exposed](abapwith_associations_defining.md) for the common table expression.

In a path expression, the names of associations `_assoc1`, `_assoc2`, ... are separated by backslashes (`\`). Associations specified after the root element must be exposed in the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the directly prefixed association in the path expression. No CDS associations can occur that are defined in a [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md) or whose association targets are a [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md).

When a `SELECT` statement with path expressions is compiled, the joins represented by them are implicitly inserted in the [`FROM`](abapfrom_clause.md) clause of the statement and the resulting additional data sources are implicitly evaluated at the usage locations of the path expressions. The join conditions of the associations and the other conditions of the CDS entities or common table expressions involved are respected. Path expressions can be used:

- In the [column specifications](abenabap_sql_columns.md) of `SELECT` statements of [queries](../../abap-glossary/abenasql_query_glosry.md).

  The path expression represents a left outer join (`LEFT OUTER JOIN`) by default.

- As a [data source](abapselect_data_source.md) of the [`FROM` clause](abapfrom_clause.md) in [queries](../../abap-glossary/abenasql_query_glosry.md).

  The path expression represents an inner join (`INNER JOIN`) by default.

- To [expose](abapwith_associations_using.md) an association of a [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md) in the [`WITH`](abapwith.md) statement.

When specifying columns and when exposing an association, an optional `source` unit can be specified in front of the path expression, separated by a [column selector](../../abap-glossary/abentable_comp_selector_glosry.md) `~`. The first association of this unit is exposed. This is either a CDS view, a CDS hierarchy, or a common table expression. However, when used as a data source, the path expression follows the exposed unit directly anyway.

An association has the [cardinality](../../abap-glossary/abencardinality_glosry.md) defined implicitly or explicitly in the CDS entity or common table expression by default. Syntax warnings or syntax errors occur when the cardinality does not match the way the path expression is used in the `SELECT` statement. If the association has the cardinality *to one*, the addition [`MANY TO ONE`](abapselect_join.md) is added implicitly in the case of a `LEFT OUTER JOIN` on databases where this is supported. The consequences of this behavior should be noted. The following can be specified after an association:

- Actual parameters can be passed to input parameters of the data source of a CDS association by using [`sql_para`](abenabap_sql_parameters.md).

- The following attributes can be specified for the section of the path expression using [`attributes`](abenabap_sql_path_filter.md):

  - Cardinality of the association

  - Category of the join expression

  - Filter conditions

A path expression can be split across multiple lines of source code at the following places:

- In front of a backslash (`\`), but not in the [`SELECT`](abapselect_list.md) list

- In blanks in parentheses of parameter passing

- In blanks in square brackets for attributes

Certain [restrictions](abenabap_sql_path_restrictions.md) apply to the associations of path expressions in ABAP SQL.

## Hints

- When the associations of the path expressions are defined as joins, an attempt is made to map them to as few join expressions as possible. Associations with identical [parameter passing](abenabap_sql_parameters.md) and semantically identical [attributes](abenabap_sql_path_filter.md) generally produce only one join expression.

- If the [column specifications](abenabap_sql_columns.md) of different [clauses](abenselect_clauses.md) are checked for matches in a `SELECT` statement, any parameters specified and attributes are also checked. Here, the same host variables must also be used in the same operand positions.

- No path expressions can be created using CDS associations that are [exposed](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_absent_association.md) in the element list of [CDS abstract entities](../../abap-glossary/abencds_abstract_entity_glosry.md).

- When a path expression of a `TO EXACT ONE` association is used with [attributes](abenabap_sql_path_filter.md), then the join is rewritten to a `TO ONE` join on the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) to avoid potential cardinality conflicts. This can be mitigated by explicitly specifying the cardinality `TO EXACT ONE` as attribute of the path expression.

- When the target entities of a path expression of a `TO EXACT ONE` association or of a `TO EXACT ONE` join have [CDS access controls](../../abap-glossary/abencds_access_control_glosry.md) assigned, then the join is rewritten to a `TO ONE` join on the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) to avoid potential cardinality conflicts.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Simple path specified for the CDS association `_spfli_scarr` from the following CDS view entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_ASSOCIATION_VE
  as select from spfli
  association [1..1] to scarr as _spfli_scarr
    on $projection.id = _spfli_scarr.carrid
{
      _spfli_scarr,
  key spfli.carrid                 as id,
  key _spfli_scarr[inner].carrname as carrier,
  key spfli.connid                 as flight,
      spfli.cityfrom               as departure,
      spfli.cityto                 as destination
}
```

The class `CL_DEMO_CDS_ASSOCIATION` uses the following `SELECT` statement with the simple path `\_spfli_scarr` for the view and compares it with accesses to the data that work in the same way.

``` abap
SELECT id, 
       \_spfli_scarr[ INNER MANY TO ONE ]-carrname AS carrier, 
       flight, 
       departure, 
       destination 
       FROM demo_cds_association_ve 
       INTO TABLE @FINAL(result).
```

A `SELECT` statement that accesses the entire `SELECT` list of the view and a `SELECT` statement that accesses a view with a join of the same type produce the same result.

## Executable Examples

- [Path Expressions, Use in the `SELECT` List](abenpath_expr_in_colspec_abexa.md)

- [Path Expressions, Use in the `FROM` Clause](abenpath_expr_in_from_clause_abexa.md)
