---
title: "CDS DDL - CDS Table Entity, ASSOCIATION"
source_file: abencds_table_entity_assoc.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Table Entities > CDS DDL - DEFINE TABLE ENTITY > CDS DDL - CDS Table Entity, element_list > CDS DDL - CDS Table Entity, element"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS Table Entity, ASSOCIATION

## Syntax

``` abap
... ASSOCIATION [cardinality] TO target ON cds_cond 
                [ WITH DEFAULT FILTER cds_cond ] ...  
```

[`cardinality`](abencds_cardinality_v2.md) · [`cds_cond`](../abap-cds-obsolete-language-elements/abencds_conditional_expression_v1.md)

### Addition

[1. `... cardinality`](abencds_table_entity_assoc.md#addition-1)

[2. `... ON cds_cond`](abencds_table_entity_assoc.md#addition-2)

[3. `... WITH DEFAULT FILTER cds_cond`](abencds_table_entity_assoc.md#addition-3)

## Overview

### Description

Defines a [CDS association](../../abap-glossary/abencds_association_glosry.md) in the [element list](abencds_table_entity_element_list.md) of a [CDS table entity](../../abap-glossary/abencds_table_entity_glosry.md). The CDS association uses an `ON` condition to associate the current CDS entity with the [association target](../../abap-glossary/abenassociation_target_glosry.md) `target.` The association target can be other CDS entities.

The syntax is similar to the syntax of the addition [`ASSOCIATION`](abencds_simple_association_v2.md) in the `SELECT` statement of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) with the following differences:

- The addition `AS _assoc` is not used. The CDS association is declared using the name `_assoc` in the [element list](abencds_table_entity_element_list.md) of the table entity, after which the addition `ASSOCIATION` is specified in the element list.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Example of a simple CDS association in a table entity. The association `_assoc` associates the table entity `DEMO_CDS_TE_ASSOC` with the table entity `DEMO_CDS_TABLE_ENTITY`.

``` abap
@ClientHandling.type: #CLIENT_DEPENDENT
@AbapCatalog.deliveryClass: #APPLICATION_DATA
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS table entity, association'
define table entity DEMO_CDS_TE_ASSOC
{
  key col1   : abap.int8;
      col2   : abap.int4;
      col3   : abap.char(3);
      _assoc : association of one to one demo_cds_table_entity 
        on _assoc.key_field = DEMO_CDS_TE_ASSOC.col1;

}
```

The class `CL_DEMO_CDS_ASSOCIATION_TE` demonstrates how to access fields from an association target in a CDS table entity.

Here's a code snippet:

``` abap
SELECT col1, col2, \_assoc-key_field, \_assoc-char_field_null 
  FROM demo_cds_te_assoc 
  INTO TABLE @FINAL(result) ##NO_NULL_VALUES.
```

## Addition 1

`... cardinality`

### Description

The same rules apply as described in topic [CDS DDL - CDS View Entity, `cardinality`](abencds_cardinality_v2.md) with one further restriction: the cardinality must be written in words. The numeric notation is not available in table entities.

## Addition 2

`... ON cds_cond`

### Description

When specifying the `ON` condition, the following rules apply:

- Fields of the [association source](../../abap-glossary/abenassociation_source_glosry.md) must be prefixed by the name of the data source or by `$projection.`.

- The fields of the [association target](../../abap-glossary/abenassociation_target_glosry.md) must be prefixed by the name of the CDS association (prefix `_assoc.` separated by a period).

The following rules apply to the operands and syntax of the `ON` condition:

- All relational operators are allowed. This means that comparison operators are allowed as well as `BETWEEN`, `LIKE`, `IS NULL`, `IS INITIAL`.

- The Boolean operators `NOT`, `AND` and `OR` are allowed.

- `lhs` can be a [field](abencds_field_v2.md) of one of the two data sources [`data_source`](abencds_data_source_v2.md) of the CDS association. If a comparison operator is used as operator, then `lhs` can also be a [CDS literal](../../abap-glossary/abencds_literal_glosry.md).

- `rhs` can be a [field](abencds_field_v2.md) of both data sources [`data_source`](abencds_data_source_v2.md) of the CDS association, a literal, or a [session variable](abencds_session_variable_v2.md). **Exception:** if the operator `LIKE` is used, then `rhs` must be a character literal.

Special rules apply when the operands of the `ON` condition are [CDS enumerated elements](../../abap-glossary/abencds_enum_element_glosry.md). These rules are described in the topic [CDS DDL - Using CDS Enumerated Types](abencds_use_enum_type.md).

**Note:**

If the association target is a [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md), stricter rules apply:

- Only the equal operator `=` is allowed.

- Only the Boolean operator `AND` is allowed.

- Only [CDS source fields](../../abap-glossary/abencds_field_glosry.md) are allowed as operands.

## Addition 3

`... WITH DEFAULT FILTER cds_cond`

### Description

The same rules apply as described in topic [CDS DDL - CDS View Entity, `ASSOCIATION`](abencds_simple_association_v2.md).
