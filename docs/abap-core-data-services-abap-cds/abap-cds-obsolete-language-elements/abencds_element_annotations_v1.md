---
title: "CDS DDL - DDIC-Based View, SELECT, element_annot"
source_file: abencds_element_annotations_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, select_list > CDS DDL - DDIC-Based View, SELECT, element"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, SELECT, element_annot

## Syntax

``` abap
... @annotation ...   
... @<annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) · [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) in the definition of an [element](abencds_select_list_entry_v1.md) of a [`SELECT` list](abencds_select_list_v1.md) in a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) as element annotation. Element annotations can be specified before and after the element.

- In front of the element, the character `@` must be placed before the name `annotation` of the annotation.

- Following the element, the characters `@<` must be placed before the name `annotation` of the annotation.

The elements of [CDS entities](../../abap-glossary/abencds_entity_glosry.md) can be annotated with the element annotations listed in topic [`element_annot`](../abap-cds-data-definitions/abencds_f1_element_annotation.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the CDS view `demo_corporation_sales_order`, a short text and a tooltip are assigned to the element `role`. The element `currency_code` is flagged as a currency key and is assigned as a currency key to the element `gross_amount`.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_CORP_SO_VW'
define view demo_corporation_sales_order as
  select from snwd_bpa as business_partner
           inner join snwd_so as sales_order
             on business_partner.node_key = sales_order.buyer_guid
         { key sales_order.so_id as sales_order_id,
               business_partner.bp_id as corporation_id,
               business_partner.company_name,
              @EndUserText.label: 'Corporation Role'
              @EndUserText.quickInfo: 'Customer or supplier'
                 business_partner.bp_role as role,
              @Semantics.currencyCode
                 sales_order.currency_code,
              @Semantics.amount.currencyCode: 'currency_code'
                 sales_order.gross_amount }
         where business_partner.legal_form = 'Inc.'; //Corporations only
```
