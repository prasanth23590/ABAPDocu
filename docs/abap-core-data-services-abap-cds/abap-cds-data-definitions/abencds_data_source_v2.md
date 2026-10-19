---
title: "CDS DDL - CDS View Entity, SELECT, data_source"
source_file: abencds_data_source_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, SELECT, data_source

## Syntax

``` abap
... entity[parameters]|path_expr [AS alias] [join] ...  
```

[`parameters`](abencds_select_parameters_v2.md) · [`path_expr`](abencds_path_expression_v2.md) · [`join`](abencds_joined_data_source_v2.md)

## Description

Defines a data source of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). A data source can be a [DDIC database table](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables.md), a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md), a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md), or a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md).

- The data source is specified either directly using its name `entity` or using a path expression [`path_expr`](abencds_path_expression_v2.md) in which [CDS associations](../../abap-glossary/abencds_association_glosry.md) are evaluated. [CDS transient entities](../../abap-glossary/abencds_non_sql_entity_glosry.md) are not possible as association target of the path expression.

- If the data source is a CDS entity with a [list of input parameters](abencds_parameter_list_v2.md), actual parameters must be passed to these using [`parameters`](abencds_select_parameters_v2.md).

- An [alias name](../../abap-glossary/abenalias_glosry.md) `alias` for a directly specified data source can be defined after `AS`. The name must comply with the naming rules for [names](../abap-cds-syntax/abencds_general_syntax_rules.md).

- The syntax [`JOIN`](abencds_joined_data_source_v2.md) can be used to combine multiple data sources as [joins](../../abap-glossary/abenjoin_glosry.md).

## Hints

- If the data source after `FROM` is specified as a path expression and if, additionally, the view defines an association, then there is a conflict because in the `ON` condition of an association, it is not possible to specify a path expression. To prevent this conflict, the following options are available:

  - Use the `$projection` syntax in the `ON` condition

  - Assign an alias name to the data source

  - Resolve the path expression and use the association target as prefix in the `ON` condition.

- For an overview of all possible data sources of all available CDS entities, see [Data Source Matrix](abencds_data_source_matrix.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Defines the CDS view entity `DEMO_CDS_DATA_SOURCE` with two data sources:

- The first data source `demo_cds_param_view_entity` requires values for three input parameters. It is assigned the alias name `source1`. To use this data source in the `SELECT` list, the alias name `source1` must be used as prefix.

- The second data source `scarr` is defined using an inner join. It is assigned the alias name `_source2`. To use this data source in the `SELECT` list, the alias name `_source2` must be used as prefix.

``` abap
@EndUserText.label: 'CDS view entity data source example'
define view entity DEMO_CDS_DATA_SOURCE
  as select from Demo_Cds_Param_View_Entity
                 ( p_distance_l:12, p_distance_u:23, p_unit:'kms' ) 
                                           as source1
    inner join   scarr                     as _source2
      on source1.carrid = _source2.carrid
  {       
    key source1.carrid,
    key source1.connid,
        source1.cityfrom,
        source1.cityto,
        source1.distance,
        source1.distid,
        //scarr
        _source2.carrname,
        _source2.currcode,
        _source2.url
  }
```
