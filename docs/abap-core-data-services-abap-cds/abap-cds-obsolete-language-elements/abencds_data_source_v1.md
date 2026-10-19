---
title: "CDS DDL - DDIC-Based View, SELECT, data_source"
source_file: abencds_data_source_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, SELECT, data_source

## Syntax

``` abap
... entity[parameters]|path_expr [[AS] alias] [join] ...  
```

[`parameters`](abencds_select_parameters_v1.md) · [`path_expr`](abencds_path_expression_v1.md) · [`join`](abencds_joined_data_source_v1.md)

## Description

Defines a data source of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). A data source can be a DDIC database table defined in ABAP Dictionary a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md), a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md), or a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md).

- The data source is specified either directly using its name `entity` or using a path expression [`path_expr`](abencds_path_expression_v1.md) in which [CDS associations](../../abap-glossary/abencds_association_glosry.md) are evaluated. [CDS transient entities](../../abap-glossary/abencds_non_sql_entity_glosry.md) are not possible as association target of the path expression.

- If the data source is a CDS entity with a [list of input parameters](abencds_parameter_list_v1.md), actual parameters must be passed to these using [`parameters`](abencds_select_parameters_v1.md).

- An alternative name `alias` for a directly specified data source can be defined after `AS`. It is also possible to define an alias name without the keyword `AS` (see example below). If a path expression is used, an alternative name **must** be defined. The name must comply with the naming rules for [names](../abap-cds-syntax/abencds_general_syntax_rules.md).

- The syntax [`JOIN`](abencds_joined_data_source_v1.md) can be used to combine multiple data sources as [joins](../../abap-glossary/abenjoin_glosry.md).

## Hint

For an overview of all possible data sources of all available CDS entities, see [Data Source Matrix](../abap-cds-data-definitions/abencds_data_source_matrix.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Defines the CDS view `demo_business_partner_1` for the DDIC database table `snwd_bpa`, for which an alternative name `partner` is specified. This name is used in the [`SELECT` list](abencds_select_list_v1.md).

``` abap
@AbapCatalog.sqlViewName: 'DEMO_BPA_1'
define view DEMO_BUSINESS_PARTNER_1 as
  select from snwd_bpa as partner
         { key partner.bp_id,
           partner.company_name,
           partner.bp_role }
```

`as` can also be omitted in front of the alternative name `partner`. The following example demonstrates another valid spelling that is potentially confusing:

``` abap
@AbapCatalog.sqlViewName: 'DEMO_BPA_2'
define view DEMO_BUSINESS_PARTNER_2 as
  select from snwd_bpa
           partner{ key partner.bp_id,
                    partner.company_name,
                    partner.bp_role }
```
