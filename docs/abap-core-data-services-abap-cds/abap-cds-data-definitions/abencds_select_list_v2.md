---
title: "CDS DDL - CDS View Entity, SELECT, select_list"
source_file: abencds_select_list_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, SELECT, select_list

## Syntax

``` abap
... element1, element2, ...  
```

[`element1`](abencds_select_list_entry_v2.md) · [`element2`](abencds_select_list_entry_v2.md)

## Description

Defines an element of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). The elements can be specified in a comma-separated list: [`element1`](abencds_select_list_entry_v2.md), [`element2`](abencds_select_list_entry_v2.md) ...

The names of the elements of a CDS view entity must be unique. These are either

- the names of the elements taken from the data sources, or

- alternative element names specified using [`AS`](abencds_select_list_entry_v2.md).

Defining a client field in the `SELECT` list is not allowed, since [client handling](abencds_v2_view_client_handling.md) takes place implicitly in CDS view entities.

## Hint

It is not possible to use an asterisk `*` to include all fields of the data source in the CDS view entity as elements and expose all CDS associations, to-child and to-parent associations of the current view. This syntax can be used in ABAP SQL and in [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), but not in [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity `DEMO_SALES_CDS_SO_VE_SIMPLE` is a view of the DDIC database table `demo_sales_order`. Three elements (`so_key`, `BuyerID`, and `currencySum`) are defined for this view.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_SALES_CDS_SO_VE_SIMPLE
  as select from demo_sales_order as SalesOrder
  {
    key so_key,
        buyer_id     as BuyerID,
        currency_sum as currencySum
  }
```
