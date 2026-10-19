---
title: "CDS DDL - DDIC-Based View, SELECT, select_list"
source_file: abencds_select_list_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, SELECT, select_list

## Syntax

``` abap
... element1, element2, ... 
  | * ...  
```

[`element1`](abencds_select_list_entry_v1.md) · [`element2`](abencds_select_list_entry_v1.md)

## Description

Defines an element of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). The elements can be specified as follows:

- In a comma-separated list, elements can be defined by specifying [`element1`](abencds_select_list_entry_v1.md), [`element2`](abencds_select_list_entry_v1.md) ...

- `*` can be used to define all fields of the data source of the CDS view as elements and expose all CDS associations, to-child and to-parent associations of the current view. If another CDS view is used as a data source, the CDS associations, to-child and to-parent associations exposed in its `SELECT` list are not exposed by the current CDS view. The asterisk `*` cannot be specified if the current CDS view contains [joins](abencds_joined_data_source_v1.md) or [union sets](abencds_union_v1.md) when the [data source](abencds_data_source_v1.md) is specified.

The names of the elements of a CDS view must be unique. These are either

- The names of the elements taken from the data sources

- Alternative element names specified using [`AS`](abencds_select_list_entry_v1.md)

- The names specified in a [name list](abencds_name_list_v1.md)

These names are also the names of the view fields of the [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md) and the corresponding rules that must be kept.

## Hint

The maximum number of elements and the limit on the total of field lengths is determined by the corresponding [limits](abencds_v1_views.md) for the associated [CDS-managed DDIC view](../../abap-glossary/abencds_mngdddic_view_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view `demo_sales_order_old2` is a view of the DDIC database table `snwd_so`. Three elements (`so_id`, `currency_code`, and `gross_amount`) are defined for this view.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_SO_VW2'
define view DEMO_SALES_ORDER_OLD2
  as select from snwd_so
{
  key   so_id,
        @Semantics.currencyCode
        currency_code,
        @Semantics.amount.currencyCode: 'currency_code'
        gross_amount
}
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view `demo_sales_order_old3` is a view of all the fields of the DDIC database table `snwd_so`. Accessing the CDS view has the same effect as when the database itself is accessed.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_SO_VW3'
define view DEMO_SALES_ORDER_OLD3 as
  select from snwd_so
         { * }
```
