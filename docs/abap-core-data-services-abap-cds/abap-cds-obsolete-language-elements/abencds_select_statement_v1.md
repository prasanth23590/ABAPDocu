---
title: "CDS DDL - DDIC-Based View, SELECT"
source_file: abencds_select_statement_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, SELECT

## Syntax

``` abap
 SELECT [DISTINCT] { select_list 
                    FROM data_source 
                    [association1 association2 ...] } 
                | { FROM data_source 
                    [association1 association2 ...] 
                    {select_list} } 
                  [clauses]  
```

[`select_list`](abencds_select_list_v1.md) · [`data_source`](abencds_data_source_v1.md) · [`association1`](abencds_simple_association_v1.md) · [`association2`](abencds_simple_association_v1.md) · [`data_source`](abencds_data_source_v1.md) · [`association1`](abencds_simple_association_v1.md) · [`association2`](abencds_simple_association_v1.md) · [`select_list`](abencds_select_list_v1.md) · [`clauses`](abencds_select_clauses_v1.md)

## Description

The `SELECT` statement defines a query performed on the data sources specified in [`data_source`](abencds_data_source_v1.md) for a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), as part of the statement [`DEFINE VIEW`](abencds_define_view_v1.md). Possible data sources are [DDIC database tables](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables.md), [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md), [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md), [CDS hierarchies](../../abap-glossary/abencds_hierarchy_glosry.md), or [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md).

- [`select_list`](abencds_select_list_v1.md) defines the components read in a list.

- [`association1`](abencds_simple_association_v1.md), [`association2`](abencds_simple_association_v1.md), ... define CDS associations for the current `SELECT` statement. These CDS associations can be accessed in [`data_source`](abencds_data_source_v1.md) and in [`select_list`](abencds_select_list_v1.md) using [path expressions](abencds_path_expression_v1.md).

- `DISTINCT` removes duplicates from the results list. If `DISTINCT` is specified, the elements cannot have the [type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) `LCHR`, `LRAW`, `STRING`, `RAWSTRING`, or `GEOM_EWKB`.

  **Note:** For determining duplicate rows, **all** columns are considered and not just key fields.

Both variants of the code are equivalent. Curly brackets `{ }` must be used in the second variant before and after the `select_list`.

The optional addition [`clauses`](abencds_select_clauses_v1.md) are `SELECT` clauses that enable conditions, groupings, and unions.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The CDS view `demo_cds_scarr_spfli` defined here is a view that joins two database tables `SCARR` and `SPFLI`.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CDS_JOIN'
@AccessControl.authorizationCheck: #NOT_ALLOWED
define view demo_cds_scarr_spfli(
    id,
    carrier,
    flight,
    departure,
    destination
  )
  as select from spfli
    join         scarr on scarr.carrid = spfli.carrid
{
  key spfli.carrid,
  key scarr.carrname,
  key spfli.connid,
      spfli.cityfrom,
      spfli.cityto
}
```

The CDS view can be addressed in ABAP programs using ABAP SQL, for example:

SELECT \* FROM demo_cds_scarr_spfli INTO TABLE @itab ...
