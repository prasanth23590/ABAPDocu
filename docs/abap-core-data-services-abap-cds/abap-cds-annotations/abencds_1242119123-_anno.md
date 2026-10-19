---
title: "AbapCatalog.buffering.status"
source_file: abencds_1242119123-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.buffering.status

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `AbapCatalog.buffering.status`                                |
| **Scope**   | `#VIEW`                                                       |
| **Type**    | `String(20)`                                                  |
| **Enums**   | `#ACTIVE, #NOT_ALLOWED, #SWITCHED_OFF`                        |
| **Default** | `#SWITCHED_OFF`                                               |
| **Text**    | `-`                                                           |
| **MDE**     | `-`                                                           |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM` |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AbapCatalog

Technical settings of a CDS entity.

## buffering

Defines table buffering for a CDS DDIC-based view.

## status

Activates and deactivates table buffering for the CDS DDIC-based view.

If the annotation is not specified, the value \#SWITCHED_OFF is used.

## Enums

## \#NOT_ALLOWED

Table buffering not allowed.

## \#ACTIVE

Table buffering active.

## \#SWITCHED_OFF

Table buffering allowed but not active.

## Further Information

More information:

- [Table Buffering of CDS DDIC-Based Views](../abap-cds-obsolete-language-elements/abencds_v1_buffering.md)

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Activates [table buffering](../../abap-glossary/abentable_buffering_glosry.md) with single record buffering for the CDS view `business_partner`.

``` abap
@AbapCatalog.sqlViewName:      'BPA_VW' 
@AbapCatalog.buffering.status: #ACTIVE 
@AbapCatalog.buffering.type:   #SINGLE 
define view business_partner as 
  select from snwd_bpa 
         { key snwd_bpa.bp_id as id, 
               snwd_bpa.bp_role as role, 
               snwd_bpa.company_name, 
               snwd_bpa.phone_number }
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

For the CDS view `business_partner`, activates [table buffering](../../abap-glossary/abentable_buffering_glosry.md) for a generic area and a key element.

``` abap
@AbapCatalog.sqlViewName:                 'BPA_VW' 
@AbapCatalog.buffering.status:            #ACTIVE 
@AbapCatalog.buffering.type:              #GENERIC 
@AbapCatalog.buffering.numberOfKeyFields: 1 
define view business_partner as 
  select from snwd_bpa 
        { key snwd_bpa.bp_id as id, 
              snwd_bpa.bp_role as role, 
              snwd_bpa.company_name, 
              snwd_bpa.phone_number }
```
