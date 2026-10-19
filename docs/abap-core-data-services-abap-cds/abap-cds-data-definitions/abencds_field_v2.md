---
title: "CDS DDL - CDS View Entity, field"
source_file: abencds_field_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, Elementary CDS Operands"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, field

## Syntax

``` abap
... [entity.]field|[alias.]field ...  
```

## Description

Defines a [CDS source field](../../abap-glossary/abencds_field_glosry.md) in an operand position of a CDS entity. A CDS source field is a field of a [data source](abencds_data_source_v2.md) `entity` of the current [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md). `field` expects the actual name of the element. Any alternative element names defined using [`AS`](abencds_select_list_entry_v2.md) cannot be used, with the exception of the `ON` condition of a [CDS association](../../abap-glossary/abencds_association_glosry.md).

If the view entity makes use of multiple [data sources](abencds_data_source_v2.md) by using join expressions, then all fields must be prefixed with the name of their data source separated by a period (.). The prefix is required in all cases, even if the field names are unique.

For fields that are included via associations, special rules apply. See topic [CDS DDL - CDS View Entity, `path_expr`](abencds_path_expression_v2.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The CDS view entity `DEMO_CDS_SCARR_SPFLI_2` defines a join and therefore, all fields from the `SELECT` list must be prefixed by the name of their data source.

The second CDS view entity shown below, `DEMO_CDS_FIELDS_ASSOC_VE`, defines an association and all fields of the association target that are used in the `SELECT` list must by prefixed by the name of the data source.

``` abap
@AccessControl.authorizationCheck: #NOT_ALLOWED
define view entity DEMO_CDS_SCARR_SPFLI_2
  as select from spfli
      join scarr
        on scarr.carrid = spfli.carrid
    {
      key spfli.carrid   as id,
      key scarr.carrname as carrier,
      key spfli.connid   as flight,
          spfli.cityfrom as departure,
          spfli.cityto   as destination
    }

```abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_FIELDS_ASSOC_VE
  as select from spfli
    association to scarr as _scarr
      on spfli.carrid = _scarr.carrid
    {
      key carrid,
      key connid,
          airpfrom,
          airpto,
          _scarr.carrname,
          _scarr.url
    }
```
