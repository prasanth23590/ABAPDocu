---
title: "CDS DDL - DEFINE CUSTOM ENTITY, association"
source_file: abencds_f1_custom_association.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Custom Entities > CDS DDL - DEFINE CUSTOM ENTITY > CDS DDL - DEFINE CUSTOM ENTITY, element_list > CDS DDL - DEFINE CUSTOM ENTITY, element"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE CUSTOM ENTITY, association

## Syntax

``` abap
... ASSOCIATION [cardinality] [TO] target ON cds_cond 
                [ WITH DEFAULT FILTER cds_cond ] ...  
```

[`cardinality`](abencds_cardinality_v2.md) · [`cds_cond`](../abap-cds-obsolete-language-elements/abencds_conditional_expression_v1.md)

### Addition

[1. `... cardinality`](abencds_f1_custom_association.md#addition-1)

[2. `... ON cds_cond`](abencds_f1_custom_association.md#addition-2)

[3. `... WITH DEFAULT FILTER cds_cond`](abencds_f1_custom_association.md#addition-3)

## Overview

### Description

Defines a [CDS association](../../abap-glossary/abencds_association_glosry.md) in the [element list](abencds_f1_custom_element_list.md) of a [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md). The CDS association uses an `ON` condition to associate the current CDS entity with the [association target](../../abap-glossary/abenassociation_target_glosry.md) `target.` The association target can be a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md), a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md), another CDS custom entity, a [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md), a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), a [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md), or a [DDIC database view](../../abap-glossary/abendatabase_view_glosry.md).

The syntax is similar to the syntax of the addition [`ASSOCIATION`](abencds_simple_association_v2.md) in the `SELECT` statement of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) with the following differences:

- The addition `AS _assoc` is not used. The CDS association is declared using the name `_assoc` in the [element list](abencds_f1_custom_element.md) of the CDS custom entity, after which the addition `ASSOCIATION` is specified in the element list.

- There are further restrictions regarding the syntax of the `ON` condition (see below).

A CDS association defined using the addition `ASSOCIATION` in the element list of a CDS custom entity is always exposed. It cannot, however, be used in any [SQL path expressions](../../abap-glossary/abensql_path_expression_glosry.md), either in ABAP CDS or in ABAP SQL.

### Hints

- A CDS association of a CDS custom entity cannot be used anywhere where it could produce instances of join expressions.

- For an overview of all possible association targets of all CDS entities that can define associations, see [Data Source Matrix](abencds_data_source_matrix.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following DDL source code shows a CDS custom entity that exposes a CDS association with another CDS custom entity:

``` abap
@EndUserText.label: 'CDS custom entity, association'
define custom entity DEMO_CDS_CUSTOM_SO
  {
    key id               : abap.char(20);
        seller_id        : abap.char(20);
        buyer_id         : abap.char(20);
        act_indicator    : abap.char( 1 );
        type_code        : abap.char( 5 );
        _type_code_texts : association of many to many
          DEMO_SALES_SO_CUSTOM_ANALYTICS
          on _type_code_texts.TypeCode = DEMO_CDS_CUSTOM_SO.type_code;
  }
```

## Addition 1

`... cardinality`

### Description

The same rules apply as described in topic [CDS DDL - CDS View Entity, `cardinality`](abencds_cardinality_v2.md).

## Addition 2

`... ON cds_cond`

### Description

When specifying the `ON` condition, the following rules apply:

- Fields of the [association source](../../abap-glossary/abenassociation_source_glosry.md) must be prefixed by the name of the data source.

- The fields of the [association target](../../abap-glossary/abenassociation_target_glosry.md) must be prefixed by the name of the CDS association (prefix `_assoc.` separated by a period).

- Fields that are listed in the `SELECT` list of the current view entity must be prefixed with `$projection`.

The following rules apply to the operands and syntax of the `ON` condition:

- As relational operator, only the equal operator (=) is allowed.

- The Boolean operator `AND` is allowed. `OR` and `NOT` are not allowed.

- `lhs` must be a [field](abencds_field_v2.md) of one of the two data sources [`data_source`](abencds_data_source_v2.md) of the CDS association.

- `rhs` must be a [field](abencds_field_v2.md) of both data sources [`data_source`](abencds_data_source_v2.md) of the CDS association.

- [CDS enumerated elements](../../abap-glossary/abencds_enum_element_glosry.md) are not allowed as operands in the `ON` condition.

## Addition 3

`... WITH DEFAULT FILTER cds_cond`

### Description

The same rules apply as described in topic [CDS DDL - CDS View Entity, `ASSOCIATION`](abencds_simple_association_v2.md).
