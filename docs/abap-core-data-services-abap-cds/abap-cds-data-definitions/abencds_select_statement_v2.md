---
title: "CDS DDL - CDS View Entity, SELECT"
source_file: abencds_select_statement_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, SELECT

## Syntax

``` abap
 SELECT [DISTINCT] FROM data_source 
       [association1 association2 ...] 
       [aspect binding] 
           {select_list} 
       [clauses]  
```

[`data_source`](abencds_data_source_v2.md) · [`association1`](abencds_simple_association_v2.md) · [`association2`](abencds_simple_association_v2.md) · [`aspect binding`](abencds_bind_aspect.md) · [`select_list`](abencds_select_list_v2.md) · [`clauses`](abencds_select_clauses_v2.md)

## Description

In a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), as part of the statement `DEFINE VIEW ENTITY`, a `SELECT` statement defines a query performed on the data sources specified in [`data_source`](abencds_data_source_v2.md). Possible data sources are [DDIC database tables](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables.md), [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md), [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md), [CDS hierarchies](../../abap-glossary/abencds_hierarchy_glosry.md), or [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md).

- `DISTINCT` removes duplicates from the result set. If `DISTINCT` is specified, the elements cannot have the [type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) `LCHR`, `LRAW`, `STRING`, `RAWSTRING`, or `GEOM_EWKB`.

  **Note:** For determining duplicate rows, **all** columns are considered and not just key fields.

- [`association1`](abencds_simple_association_v2.md), [`association2`](abencds_simple_association_v2.md), ... define CDS associations for the current `SELECT` statement. These CDS associations can be accessed in [`data_source`](abencds_data_source_v2.md) and in [`select_list`](abencds_select_list_v2.md) using [path expressions](abencds_path_expression_v2.md).

- [`aspect binding`](abencds_bind_aspect.md): Optionally, one or more CDS aspects can be bound to the view entity.

- The [`select_list`](abencds_select_list_v2.md) defines the components read in a list.

- The optional addition [`clauses`](abencds_select_clauses_v2.md) are `SELECT` clauses that enable conditions, groupings, or set operators.

## Hints

- The syntax `SELECT *` to select all elements from the data source is **not** supported in CDS view entities. This syntax can be used in ABAP SQL and in [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), but **not** in CDS view entities.

- For an overview of all possible data sources of all available CDS entities, see [Data Source Matrix](abencds_data_source_matrix.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The CDS view entity `DEMO_CDS_BUPA_NAME` shown below is based on the existing [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) `DEMO_SALES_CDS_BUPA`. In the `SELECT` list, the element `family_name` is defined, assigned the alias name `last_name`, and given the comment `Business partner last name`.

``` abap
@EndUserText.label: 'CDS view entity business partner name'
define view entity DEMO_CDS_BUPA_NAME
  as select from
    DEMO_SALES_CDS_BUPA
    {
      family_name as last_name // Business partner last name
    }
```

The CDS view entity `DEMO_CDS_BUPA_NAME` can be addressed in ABAP programs using ABAP SQL, for example:

SELECT \* FROM demo_cds_bupa_name INTO TABLE @itab ...

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity removes any duplicate values of the result set using `DISTINCT`.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, select distinct'

define view entity DEMO_CDS_DISTINCT
  as select distinct from demo_dbtab_child
{
  key key_field,
      char_field
}
where
  key_field = 1 // 3 entries, 2 duplicate
```

The class `CL_DEMO_CDS_DISTINCT` first fills the underlying database table and then accesses the view using [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md). One duplicate entry is removed from the result set.

The addition `DISTINCT` of `SELECT` is no longer needed in this case.
