---
title: "CDS DDL - CDS View Entity, ASSOCIATION"
source_file: abencds_simple_association_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - CDS View Entity, SELECT, Associations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, ASSOCIATION

## Syntax

``` abap
... ASSOCIATION [cardinality] [TO] target [AS _assoc] ON cds_cond 
                [WITH DEFAULT FILTER cds_cond] ...  
```

[`cardinality`](abencds_cardinality_v2.md) · [`cds_cond`](abencds_conditional_expression_v2.md) · [`cds_cond`](abencds_conditional_expression_v2.md)

### Addition

[1. `... cardinality`](abencds_simple_association_v2.md#addition-1)

[2. `... AS _assoc`](abencds_simple_association_v2.md#addition-2)

[3. `... ON cds_cond`](abencds_simple_association_v2.md#addition-3)

[4. `... WITH DEFAULT FILTER cds_cond`](abencds_simple_association_v2.md#addition-4)

## Overview

### Description

Defines a [CDS association](../../abap-glossary/abencds_association_glosry.md) with the name `_assoc` in a [`SELECT` statement](abencds_select_statement_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). A CDS association associates the current CDS view entity as [association source](../../abap-glossary/abenassociation_source_glosry.md) with the [association target](../../abap-glossary/abenassociation_target_glosry.md) `target` using an `ON` condition [`cds_cond`](abencds_conditional_expression_v2.md). The association target `target` can be a [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md), another [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), a [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md), a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), a [table function](../../abap-glossary/abentable_function_glosry.md), a [hierarchy](../../abap-glossary/abenhierarchy_glosry.md), an [abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md), or a [custom entity](../../abap-glossary/abencds_custom_entity_glosry.md). If `target` is a [CDS transient entity](../../abap-glossary/abencds_non_sql_entity_glosry.md), the way the CDS association can be used is restricted.

Usage of associations in the `SELECT` list: All use cases of a CDS association are described in topic [CDS DDL - CDS associations and joins](abencds_assoc_join_v2.md).

Associations and joins: in some cases, a CDS association is internally transformed into a join. All use cases of CDS associations and information about the joins created on the database are described in topic [CDS DDL - CDS associations and joins](abencds_assoc_join_v2.md).

The automatically generated join type can be changed by specifying a different join type in the attributes of a path expression, see topic [CDS DDL - CDS View Entity, `path_expr`, `join_type`](abencds_path_expr_jointype_v2.md).

**Limitations**

- CDS associations whose [association target](../../abap-glossary/abenassociation_target_glosry.md) is a [CDS transient entity](../../abap-glossary/abencds_non_sql_entity_glosry.md) cannot be used anywhere where they could produce instances of join expressions.

- CDS associations whose association target is a CDS projection view cannot be used in [path expressions](abencds_path_expression_v2.md). It is also not possible to add a field from the association target to the element list.

### Hints

- CDS associations and [join expressions](abencds_joined_data_source_v2.md) can both be used in a `SELECT` statement of a CDS view entity. A path expression can even consist of a mix of joins and associations. When accessed, the associations and joins are merged.

- Special rules apply to CDS associations in `SELECT` statements with [`set operators`](abencds_set_operators.md).

- [Cyclical dependencies](abencds_cycle_problems.md) should be avoided when using CDS associations to prevent problems occurring in mass activations of CDS entities.

- Exposed [self associations](../../abap-glossary/abenself_association_glosry.md) can be specified as [hierarchy associations](../../abap-glossary/abenhierarchy_association_glosry.md) in [CDS hierarchies](../../abap-glossary/abencds_hierarchy_glosry.md) or in the ABAP SQL [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](../../abap-programming-language/abap-database-access/abenselect_hierarchy_generator.md).

- A self association whose association target is the same as the association source cannot be created as a join in the CDS view entity where it is defined. So it is not allowed to use a self association in a position where a join is generated.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The CDS view entity `DEMO_SALES_CDS_INV_HEADER` shown below returns information about sales invoices and works with the DDIC database tables `DEMO_SO_INV_HE`, `DEMO_SALES_ORDER`, `DEMO_SALES_BUPA`, and `DEMO_SALES_SO_I`.

Two CDS associations are defined:

- `_buyer` stands for a join between the current view and the [association target](../../abap-glossary/abenassociation_target_glosry.md) `DEMO_SALES_BUPA`.

- `_invoice_items` stands for a join between the current view and the [association target](../../abap-glossary/abenassociation_target_glosry.md) `DEMO_SALES_SO_I`.

The [association source](../../abap-glossary/abenassociation_source_glosry.md) fields used in the `ON` conditions, `buyer_id` and `so_key`, are part of the `SELECT` list.

- The CDS association `_buyer` is not exposed in the `SELECT` list and can only be used in path expressions of the current `SELECT` statement. This association can be specified in the `WHERE` condition due to the cardinality to-one.

- The CDS association `_invoice_items` is not accessed in path expressions of the current `SELECT` statement. However, this association is exposed in the `SELECT` list, which means it can be used in path expressions of other CDS views. This association cannot be specified in a `WHERE` condition due to the cardinality to-many.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity demo_sales_cds_inv_header
  as select from demo_so_inv_he
    inner join   demo_sales_order as _inner
      on demo_so_inv_he.so_key = _inner.so_key
  association of many to one demo_sales_bupa as _buyer
    on demo_so_inv_he.buyer_id = _buyer.id
  association of one to one demo_sales_so_i as _invoice_items
    on $projection.so_key = _invoice_items.so_item_key
  {
        //_buyer
    key _buyer.id,
        _buyer.birth_name,
        _buyer.family_name,
        //_inner
        _inner.lifecycle_status,
        //demo_so_inv_he
        demo_so_inv_he.so_key,
        demo_so_inv_he.gross_amount,
        demo_so_inv_he.net_amount,
        demo_so_inv_he.tax_amount,
        demo_so_inv_he.currency_code,
        //_invoice_items
        _invoice_items
  }
  where _buyer.title = 'Mr.'
```

The CDS view entity can be accessed in an ABAP program with a simple ABAP SQL `SELECT` statement.

``` abap
SELECT id, birth_name, family_name 
       FROM demo_sales_cds_inv_header 
       INTO TABLE @DATA(itab).
```

The complexity of the actual query is wrapped transparently in the CDS view entity for the application programmer. When the view is accessed, the join (defined by the CDS association `_invoice_items`) between `DEMO_SO_INV_HE` and `DEMO_SALES_SO_I` is not built, because there are no path expressions that need to access the join.

The CDS view entity `DEMO_SALES_CDS_INV_HEADER` shown above is used as the data source in the definition of the CDS view entity `DEMO_SALES_CDS_SO_ITEM`. This data source is used to access the [exposed](abencds_select_list_association_v2.md) CDS association `_invoice_items`. The elements of the CDS association are accessed in this view. There is no visual indication that it is the result of a join. This join between `DEMO_SALES_CDS_INV_HEADER` and `DEMO_SALES_SO_I` is created when the CDS view entity `DEMO_SALES_CDS_SO_ITEM` is activated. The other CDS association `_buyer` of the CDS view entity `DEMO_SALES_CDS_INV_HEADER` cannot be accessed.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_SALES_CDS_SO_ITEM
  as select from
    demo_sales_cds_inv_header
    {
      key id,
          birth_name,
          family_name,
          lifecycle_status,
          so_key,
          net_amount,
          tax_amount,
          currency_code,
          /* Associations */
          _invoice_items.material,
          _invoice_items.posnr
    }
```

## Addition 1

`... cardinality`

### Description

A [cardinality](../../abap-glossary/abencardinality_glosry.md) to express the relation between the rows of the data sources can optionally be specified. The following options are available:

- The cardinality can be specified in words, for example:

  `association of many to many AssocTarget as Name on CdsCond` Note that the syntax addition `TO` is left out in this case. This is the recommended option.

- The cardinality of the association target can be specified in numbers in square brackets, for example:

  `association[0..1] to AssocTarget as Name on CdsCond` Note that the association target is specified after `TO` in this case.

- No cardinality can be specified, as in the following example:

  `association to AssocTarget as Name on CdsCond` Note that the association target is specified after `TO` in this case. If the cardinality is not defined explicitly, the cardinality many-to-one is used implicitly.

For further details, see topic [CDS DDL - CDS View Entity, `cardinality`](abencds_cardinality_v2.md).

## Addition 2

`... AS _assoc`

### Description

Defines the name `_assoc` of a CDS association. If no name is defined explicitly using `AS`, `_assoc` is set implicitly to the name of the [association target](../../abap-glossary/abenassociation_target_glosry.md). The name `_assoc` must comply with the naming rules for [names](../abap-cds-syntax/abencds_general_syntax_rules.md).

### Hint

It is recommended that an underscore `_` is used as the first character of the CDS association name.

## Addition 3

`... ON cds_cond`

### Description

When specifying the `ON` condition, the following rules apply:

- Fields of the [association source](../../abap-glossary/abenassociation_source_glosry.md) must be prefixed by the name of the data source. If an alias name was assigned, then the alias name must be used as prefix.

- The fields of the [association target](../../abap-glossary/abenassociation_target_glosry.md) must be prefixed by the name of the CDS association (prefix `_assoc.` separated by a period).

- Fields that are listed in the `SELECT` list of the current view entity must be prefixed with `$projection`.

- If the prefix `$projection` refers to a path expression, a literal, or an [expression](abencds_expressions_v2.md) of the `SELECT` list, then the current CDS association cannot be exposed in the `SELECT` list to avoid invalid join expressions.

- If the CDS association is exposed in the [`SELECT` list](abencds_select_list_v2.md) of the current `SELECT` statement, the fields of the [association source](../../abap-glossary/abenassociation_source_glosry.md) specified in the `ON` condition must also be listed in the [`SELECT` list](abencds_select_list_v2.md). This ensures that a join expression can be built from the CDS association (when used in a path expression).

The following rules apply to the operands and syntax of the `ON` condition:

- All relational operators are allowed. That means all comparison operators are allowed as well as `BETWEEN`, `LIKE`, `IS [NOT] NULL`, and `IS [NOT] INITIAL`.

- The Boolean operators `NOT`, `AND`, and `OR` are allowed.

- `lhs` can be a [field](abencds_field_v2.md) of one of the two data sources [`data_source`](abencds_data_source_v2.md) of the CDS association. If a comparison operator is used as operator, then `lhs` can also be a [CDS literal](../../abap-glossary/abencds_literal_glosry.md).

- `rhs` can be a [field](abencds_field_v2.md) of both data sources [`data_source`](abencds_data_source_v2.md) of the CDS association, a [CDS literal](../../abap-glossary/abencds_literal_glosry.md), a [parameter](abencds_parameter_v2.md), or a [session variable](abencds_session_variable_v2.md). **Exception:** if the operator `LIKE` is used, then `rhs` must be a character literal.

- Path expressions are not allowed.

- CDS DDL expressions are not allowed.

Special rules apply when the operands of the `ON` condition are [CDS enumerated elements](../../abap-glossary/abencds_enum_element_glosry.md). These rules are described in the topic [CDS DDL - Using CDS Enumerated Types](abencds_use_enum_type.md).

**Note:**

If the association target is a [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md), stricter rules apply:

- Only the equal operator `=` is allowed.

- Only the Boolean operator `AND` is allowed.

- Only [CDS source fields](../../abap-glossary/abencds_field_glosry.md) are allowed as operands.

## Addition 4

`... WITH DEFAULT FILTER cds_cond`

### Description

Defines a standard filter condition for a [path expression](abencds_path_expression_v2.md).

- If no [filter condition](abencds_path_expression_filter_v2.md) is specified when the CDS association is used in a path expression, the condition [`cds_cond`](abencds_conditional_expression_v2.md) specified using `DEFAULT FILTER` is used as the filter condition and applied in an extended condition for the join. The same [rules](abencds_path_expression_filter_v2.md) apply to the default filter condition as to a filter condition specified as an attribute.

- If a [filter condition](abencds_path_expression_filter_v2.md) is specified when the CDS association is used in a path expression, this condition is used instead of the default filter condition.

### Hint

When the syntax check evaluates a cardinality specified using `[min..max]`, the default filter condition is respected alongside the `ON` condition.
