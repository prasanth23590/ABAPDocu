---
title: "AbapCatalog.compiler.compareFilter"
source_file: abencds_1687178802-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.compiler.compareFilter

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `AbapCatalog.compiler.compareFilter`                          |
| **Scope**   | `#VIEW`                                                       |
| **Type**    | `Boolean`                                                     |
| **Enums**   | `-`                                                           |
| **Default** | `true`                                                        |
| **Text**    | `-`                                                           |
| **MDE**     | `-`                                                           |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM` |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AbapCatalog

Technical settings of a CDS entity.

## compiler

Influences the compilation of a CDS object.

## compareFilter

Defines the evaluation of filter conditions in path expressions of a CDS view.

## Annotation Values

true: The filter conditions of CDS associations occurring more than once in path expressions are compared and, if they match, the associated join expression is created only once.

false: For each CDS association with a filter condition, a separate join expression is created and evaluated.

If the annotation is not specified, the value false is used.

## Further Information

It is advisable to use the annotation `AbapCatalog.compiler.compareFilter` with the value `true`. ADT suggests this when a new CDS view is created.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Example for the annotation `AbapCatalog.compiler.compareFilter`.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_COMP_FILTER'

// false = 2 joins; true = 1 join
@AbapCatalog.compiler.compareFilter: true
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view, compare filter annotation'
define view DEMO_CDS_COMPARE_FILTER_V1
  as select from sflight as main
  association to scarr as _assoc1 
    on main.carrid = _assoc1.carrid
{
  key carrid,
  key connid,
  key fldate,
      _assoc1 [ carrid = 'LH'].url,
      _assoc1 [ carrid = 'LH']. carrname
}
```

The following image shows the SQL statement that is generated on the database when the annotation ` AbapCatalog.compiler.compareFilter` is set to `true`. Only one join expression is generated: ![figure](images_abdoc_true.png)

The following image shows the SQL statement that is generated on the database when the annotation `AbapCatalog.compiler.compareFilter` is set to `false`. Two join expressions are generated: ![figure](images_abdoc_false.png)
