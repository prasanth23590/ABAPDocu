---
title: "ABAP CDS - DDIC-Based Entities (Obsolete)"
source_file: abencds_ddic_entity.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - DDIC-Based Entities (Obsolete)

It is still possible, but not recommended, to create DDIC-based entities. SAP recommends creating CDS view entities instead of CDS DDIC-based views.

A [CDS DDIC-based entity](../../abap-glossary/abencds_ddic_based_entity_glosry.md) is a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) for which a [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md) is created in the ABAP Dictionary alongside the CDS entity upon activation. Therefore, [DDIC-based entities](../../abap-glossary/abencds_ddic_based_entity_glosry.md) are not exclusively CDS entities, but also DDIC artefacts (see image below). There is only one kind of DDIC-based entity available, namely [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). ![figure](images_abdoc_ddic_view_2.png)

A [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) is defined using the statement [`DEFINE VIEW`](abencds_define_view_v1.md). This kind of [CDS view](../../abap-glossary/abencds_view_glosry.md) was first released with release 7.40, SP05 and it was for many years the only available kind of CDS view.

Since release 7.80, [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) are available. They are defined using the statement `DEFINE VIEW ENTITY`. They have evolved from [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), serve the same purpose and have the same structure as their predecessor. But they offer several advantages over the *classic* [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md):

- No additional DDIC view is created upon activation

- Improved performance during view activation

- Optimization and simplification of syntax

- Stricter syntax checks indicate problematic situations more explicitly (for example, annotation checks)

A complete and exhaustive list of new features, improvements, and differences is provided in the following blog series: [CDS view entities are feature complete. Overview of new features, improvements, and differences](https://blogs.sap.com/2022/05/06/cds-view-entities-are-feature-complete.-overview-of-new-features-improvements-and-differences/).

For these reasons, it is recommended that [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) are created instead of [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) when a new CDS view is required. [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) are still supported to ensure downward compatibility. ![figure](images_abdoc_v1_v2.png)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

- The CDS view `DEMO_CDS_SCARR_SPFLI` shown below is a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md).

- The second view shown below, `DEMO_CDS_SCARR_SPFLI_2`, is a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) and it uses the new syntax `DEFINE VIEW ENTITY`.

- The syntax differs slightly: the second view does not have the annotation `@AbapCatalog.sqlViewName`, because it does not have any DDIC view (the SQL view of the database is derived directly from the definition). Moreover, name lists are not supported and the element names are specified with the keyword `AS` instead.

- The class `CL_DEMO_CDS_DDIC_VS_VIEW_ENTTY` uses `SELECT` to access both views. The result is exactly the same.

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

```abap
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
```
