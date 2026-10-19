---
title: "CDS DDL - DDIC-Based View, name_list"
source_file: abencds_name_list_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, name_list

## Syntax

``` abap
... ( name1, name2, ... ) ...  
```

## Description

Defines the element names of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) in a name list. The specified names `name1`, `name2`, ... are assigned to the elements defined explicitly in the [`SELECT` list](abencds_select_list_v1.md) of the [`SELECT` statement](abencds_select_statement_v1.md) in the order given. The names work like the alternative names defined in the `SELECT` list using [`AS`](abencds_select_list_entry_v1.md) and overwrite these names. If a name list is specified, it must contain a name for each element of the view.

The view field is created under the element name in the [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md). Accordingly, an element name must comply with the rules for names of view fields of DDIC database views, as well as the general naming rules for [names](../abap-cds-syntax/abencds_general_syntax_rules.md): This means that it must also meet the following requirements:

- The naming conventions for [component names](../../abap-dictionary-ddic/ddic-data-types/abenddic_structures_tech.md) of [DDIC structures](../../abap-dictionary-ddic/ddic-data-types/abenddic_structures.md) in ABAP Dictionary

- It cannot be a reserved component name. The reserved names that cannot be used are specified in the database table `TRESE`.

A name list can be specified only if the [elements](abencds_select_list_entry_v1.md) in the [`SELECT` list](abencds_select_list_v1.md) are specified explicitly. No name lists can be used if the `SELECT` list is specified as [`*`](abencds_select_list_v1.md) or if the element list contains the entry [`$EXTENSION.*`](abencds_select_list_entry_v1.md).

## Hints

- An explicit name list can be used, for example, to define the element names of a CDS view that defines a union set of multiple `SELECT` statements using [`UNION`](abencds_union_v1.md).

- A CDS view with an explicit name list cannot be expanded using [`EXTEND VIEW`](../abap-cds-data-definitions/abencds_extend_view.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Defines the names of the four elements of the CDS view `business_partner` as `id`, `role`, `company_name`, and `phone_number`.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_BPA_VW_OLD'
define view DEMO_BUSINESS_PARTNER_OLD
  (id, role, company_name, phone_number) as
  select from snwd_bpa
         { key snwd_bpa.bp_id,
               snwd_bpa.bp_role,
               snwd_bpa.company_name,
               snwd_bpa.phone_number }
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Defines the names of the three elements of the CDS view `demo_employee_sales_figures` as `financial_year`, `employee_id`, and `gross_amount`.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_SALES_FIG_VW' 
demo_view employee_sales_figures 
  (financial_year, employee_id, gross_amount) as 
   select from sales_2011_tab 
          { key '2011' as year, 
            key id, 
            amount } 
   union 
     select from sales_2012_tab 
            { '2012' as year, 
              employee_number, 
              gross_amount }
```
