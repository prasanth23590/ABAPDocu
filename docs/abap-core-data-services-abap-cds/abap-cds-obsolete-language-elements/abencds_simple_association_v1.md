---
title: "CDS DDL - DDIC-Based View, ASSOCIATION"
source_file: abencds_simple_association_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, Associations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, ASSOCIATION

## Syntax

``` abap
... ASSOCIATION [ [min..max] ] TO target [AS _assoc] ON cds_cond 
                [ WITH DEFAULT FILTER cds_cond ] ...  
```

[`cds_cond`](abencds_conditional_expression_v1.md) · [`cds_cond`](abencds_conditional_expression_v1.md)

### Addition

[1. `... [min..max]`](abencds_simple_association_v1.md#addition-1)

[2. `... AS _assoc`](abencds_simple_association_v1.md#addition-2)

[3. `... WITH DEFAULT FILTER cds_cond`](abencds_simple_association_v1.md#addition-3)

## Overview

### Description

Defines a [CDS association](../../abap-glossary/abencds_association_glosry.md) with the name `_assoc` in a [`SELECT` statement](abencds_select_statement_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). A CDS association associates the current CDS view as [association source](../../abap-glossary/abenassociation_source_glosry.md) with the [association target](../../abap-glossary/abenassociation_target_glosry.md) `target` using an `ON` condition [`cds_cond`](abencds_conditional_expression_v1.md). The association target can be a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md), a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md), another CDS custom entity, a [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md), a [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md), or a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). If `target` is a [CDS transient entity](../../abap-glossary/abencds_non_sql_entity_glosry.md), the way the CDS association can be used is restricted.

A CDS association of a [`SELECT` statement](abencds_select_statement_v1.md) in a CDS view can be accessed as follows:

- By specifying its name in a [path expression](abencds_path_expression_v1.md) in the same statement and in all places where this is documented. A CDS association whose [association target](../../abap-glossary/abenassociation_target_glosry.md) is a [CDS transient entity](../../abap-glossary/abencds_non_sql_entity_glosry.md) can only be [exposed](abencds_select_list_association_v1.md) in the [`SELECT` list](abencds_select_list_v1.md).

- If a CDS association whose [association target](../../abap-glossary/abenassociation_target_glosry.md) is not a CDS abstract entity or a CDS custom entity is exposed using a [path expression](abencds_path_expression_v1.md) in the [`SELECT` list](abencds_select_list_v1.md) of the current `SELECT` statement, the following can use it in their path expressions:

  - Other [CDS views](abencds_path_expression_v1.md)

  - [ABAP SQL statements](../../abap-programming-language/abap-database-access/abenabap_sql_path.md)

- Exposed [self associations](../../abap-glossary/abenself_association_glosry.md) can be specified as [hierarchy associations](../../abap-glossary/abenhierarchy_association_glosry.md) in [CDS hierarchies](../../abap-glossary/abencds_hierarchy_glosry.md) or in the ABAP SQL [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](../../abap-programming-language/abap-database-access/abenselect_hierarchy_generator.md).

When a CDS view is activated that uses a path expression to access a CDS association or an element, or when a path expression is used for access in ABAP SQL, every CDS association of the path expression is transformed to a [join expression](../../abap-glossary/abenjoin_expression_glosry.md). Here, the [association source](../../abap-glossary/abenassociation_source_glosry.md) represents the left side and the [association target](../../abap-glossary/abenassociation_target_glosry.md) represents the right side. The `ON` condition of the association is added to the `ON` condition of the join. By default, the [join type](../../abap-glossary/abenjoin_type_glosry.md) is determined by where the [path expression](abencds_path_expression_v1.md) is used:

- After [`FROM`](abencds_select_statement_v1.md), it is an [inner join](../../abap-glossary/abeninner_join_glosry.md) inner join (`INNER JOIN`)

- In all other locations, it is a [left outer join](../../abap-glossary/abenleft_outer_join_glosry.md) (`LEFT OUTER JOIN`)

This setting can be overwritten by specifying the [join type](abencds_path_expr_jointype_v1.md) when using the CDS association in a path expression. A path expression in a [`SELECT` list](abencds_select_list_v1.md) that [exposes](abencds_select_list_association_v1.md) its closing CDS association is not defined as a join. A self association whose [association target](../../abap-glossary/abenassociation_target_glosry.md) is the same as the [association source](../../abap-glossary/abenassociation_source_glosry.md) cannot be created as a join in the CDS view where it is defined.

When specifying the `ON` condition, for the operands, [general](abencds_cond_expr_operands_v1.md) and the following [special rules](abencds_cond_expr_on_assoc_v1.md) apply:

- The fields of the [association target](../../abap-glossary/abenassociation_target_glosry.md) must be prefixed in the `ON` condition by the name of the CDS association (prefix `_assoc.` separated by a period).

- If the CDS association in the [`SELECT` list](abencds_select_list_v1.md) of the current `SELECT` statement is exposed, the fields of the [association source](../../abap-glossary/abenassociation_source_glosry.md) specified in the `ON` condition must also be listed in the [`SELECT` list](abencds_select_list_v1.md). This ensures that a join expression can be built from the CDS association (when used in a path expression).

- To make a reference to an element of the [`SELECT` list](abencds_select_list_v1.md) in the `ON` condition, the field name can be prefixed with `$projection` instead of the [association source](../../abap-glossary/abenassociation_source_glosry.md). In this case, an alternative element name defined using [`AS`](abencds_select_list_entry_v1.md) can be specified instead of the field name. If a path expression of the `SELECT` list is used when the prefix `$projection` is used in the `ON` condition, the current CDS association cannot itself be used in the `SELECT` list, to avoid invalid join expressions.

### Hints

- CDS associations not listed in the `SELECT` list can only be used in path expressions of the current `SELECT` statement.

- When a CDS view is activated, a join defined by a CDS association is built for every use in a path expression and not for the definition of the CDS association. No joins are constructed for CDS associations that are not used in their CDS views.

- If a CDS association is used in a path expression of the `SELECT` list of the current `SELECT` statement, a join is defined for the current view. Here, the `ON` conditions of the CDS association are applied to the join directly. No path expressions are allowed in the `ON` condition of a join, which means that no reference can be made to a path expression of the `SELECT` list when using the prefix `$projection` in the `ON` condition of a CDS association, if CDS the association is also used here.

- CDS associations and [join expressions](abencds_joined_data_source_v1.md) can be used in a `SELECT` statement of a CDS view. When the join expressions defined by the CDS associations are used in path expressions, all joins are joined.

- Special rules apply to CDS associations in `SELECT` statements joined with [`UNION`](abencds_union_v1.md).

- [Cyclical dependencies](../abap-cds-data-definitions/abencds_cycle_problems.md) should be avoided when using CDS associations to prevent problems occurring in mass activations of CDS entities.

- CDS associations whose [association target](../../abap-glossary/abenassociation_target_glosry.md) is a [CDS transient entity](../../abap-glossary/abencds_non_sql_entity_glosry.md) cannot be used anywhere where they could produce instances of join expressions.

## Addition 1

`... [min..max]`

### Description

Defines the [cardinality](../../abap-glossary/abencardinality_glosry.md) of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of a CDS view, which is defined with a CDS association `ASSOCIATION`. The square brackets `[ ]` are part of the syntax. For `min` and `max`, positive integers (including 0) and asterisks (`*`) can be specified:

- `max` cannot be 0.

- An asterisk `*` for `max` means any number of rows.

- `min` can be omitted (set to 0 if omitted).

- `min` cannot be `*`.

- When a CDS association is used in a [`WHERE` condition](abencds_where_clause_v1.md), 1 must be specified for `max`.

If the cardinality is not defined explicitly, the cardinality to-one is used implicitly (`[min..1]`).

A cardinality is specified to document the semantics of the data model and, in some database systems, for optimizations. In these database systems, left outer joins (`LEFT OUTER JOIN`) produced by [path expressions](abencds_path_expression_v1.md) are given the addition `TO ONE` if an explicit or implicit *to 1* cardinality is used and the addition `TO MANY` if any other cardinality is used. These additions work in the same way as when they are specified explicitly in [`LEFT OUTER JOIN`](abencds_joined_data_source_v1.md). This means that an optimization is attempted and the result can be undefined if the result set does not match the cardinality.

### Hints

- To avoid undefined and platform-dependent behavior, the cardinality should always be defined to match the data in question.

  **Note:** The cardinality is mainly descriptive, not prescriptive. It does not force a matching result set.

- The specified cardinality is evaluated by the syntax check for paths specified in the CDS DDL of CDS or in ABAP SQL. A non-matching cardinality usually produces a syntax check warning.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specifies the cardinality of a CDS association incorrectly. The following CDS view joins the DDIC database tables `SCARR` and `SPFLI` in a CDS association `_spfli` without specifying the cardinality explicitly. The implicitly set cardinality is *to 1*. If the CDS association is used in a path specified in the `SELECT` list, this is implemented in some database systems (for example the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md)) as a left outer join using the implicit addition `TO ONE`. The actual cardinality of the data is, however, `TO MANY`.

``` abap
@AbapCatalog.sqlViewName: 'DEMOCDSWRGC'
define view demo_cds_wrong_cardinality
  as select from scarr
  association to spfli as _spfli on _spfli.carrid = scarr.carrid
{
  key scarr.carrid   as carrid,
      scarr.carrname as carrname,
      _spfli.connid  as connid
}
```

The class `CL_DEMO_CDS_WRONG_CARDINALITY` uses different `SELECT` statements to access the view. On optimizing database systems, such as the SAP HANA database, the two reads return a different number of rows, potentially an unexpected result.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specifies the cardinality of a CDS association correctly. The following CDS view joins the DDIC database tables `SCARR` and `SPFLI` in a CDS association `_spfli` while specifying the cardinality explicitly. If the CDS association is used in a path specified in the `SELECT` list, this is implemented in some database systems (for example the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md)) as a left outer join using the implicit addition `TO MANY`, which matches the actual cardinality of the data.

``` abap
@AbapCatalog.sqlViewName: 'DEMOCDSEXPC'
define view demo_cds_explicit_cardinality
  as select from
    scarr
    association [1..*] to spfli as _spfli on
      _spfli.carrid = scarr.carrid
    {
      scarr.carrid   as carrid,
      scarr.carrname as carrname,
      _spfli.connid  as connid
    }
```

The class `CL_DEMO_CDS_EXPLICIT_CRDNLTY` uses different `SELECT` statements to access the view. The two reads return the same number of rows on all database systems.

## Addition 2

`... AS _assoc`

### Description

Defines the name `_assoc` of a CDS association of a CDS view defined using `ASSOCIATION`. If no name is defined explicitly using `AS`, `_assoc` is set implicitly to the name of the [association target](../../abap-glossary/abenassociation_target_glosry.md). The name `_assoc` must comply with the naming rules for [names](../abap-cds-syntax/abencds_general_syntax_rules.md).

### Hint

It is advisable to use an underscore `_` as the first character of the CTE CDS association name.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Example of a simple CDS association. The following CDS view provides the same result as the CDS view `DEMO_CDS_SCARR_SPFLI` in the [joins](abencds_joined_data_source_v1.md) example, as shown in the class `CL_DEMO_CDS_ASSOCIATION` using an assertion. Furthermore, the CDS association `spfli_scarr` is [exposed](abencds_select_list_association_v1.md) to be used from outside in the [`SELECT` list](abencds_select_list_v1.md) by specifying a [path](abencds_path_expression_v1.md) that contains only the name of a CDS association. The class `CL_DEMO_CDS_ASSOCIATION` also shows how the CDS association can be accessed by [specifying a path](../../abap-programming-language/abap-database-access/abenabap_sql_path.md) in ABAP SQL.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_ASSOC'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view demo_cds_association(
    _spfli_scarr,
    id,
    carrier,
    flight,
    departure,
    destination
  )
  as select from
    spfli
    association [1..1] to scarr as _spfli_scarr on
      $projection.carrid = _spfli_scarr.carrid
    {
          _spfli_scarr,
      key spfli.carrid,
      key _spfli_scarr[inner].carrname,
      key spfli.connid,
          spfli.cityfrom,
          spfli.cityto
    }
```

## Addition 3

`... WITH DEFAULT FILTER cds_cond`

### Description

Defines a standard filter condition for a [path expression](abencds_path_expression_v1.md).

- If no [filter condition](abencds_path_expression_filter_v1.md) is specified when the CDS association is used in an path expression, the condition [`cds_cond`](abencds_conditional_expression_v1.md) specified using `DEFAULT FILTER` is used as the filter condition and applied in an extended condition for the join. The same [rules](abencds_cond_expr_filter_v1.md) apply to the default filter condition as to a filter condition specified as an attribute.

- If a [filter condition](abencds_path_expression_filter_v1.md) is specified when the CDS association is used in a path expression, this condition is used instead of the default filter condition.

### Hint

When the syntax check evaluates a cardinality specified using `[min..max]`, the default filter condition is respected alongside the `ON` condition.
