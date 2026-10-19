---
title: "CDS DDL - ANNOTATE ENTITY, VIEW"
source_file: abencds_f1_annotate_view.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - Specifying Annotations > ABAP CDS - Metadata Extensions > ABAP CDS - DDL for Metadata Extensions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - ANNOTATE ENTITY, VIEW

## Syntax Forms

**ANNOTATE ENTITY**

``` abap
1. @Metadata.layer: #CORE|#LOCALIZATION|#INDUSTRY|#PARTNER|#CUSTOMER 
   [@entity_annot1] 
   [@entity_annot2] 
   ... 
   ANNOTATE ENTITY cds_entity WITH 
     [parameter_list] 
     { [element_list] }[;]
```

**ANNOTATE VIEW**

``` abap
2. @Metadata.layer: #CORE|#LOCALIZATION|#INDUSTRY|#PARTNER|#CUSTOMER 
   [@entity_annot1] 
   [@entity_annot2] 
   ... 
   [@view_entity_annot1 | @proj_view_annot1 | @_view_annot1] 
   [@view_entity_annot2 | @proj_view_annot2 | @_view_annot2] 
   ... 
   ANNOTATE VIEW cds_view WITH 
     [parameter_list] 
     { [element_list] }[;]
```

[`@Metadata.layer: #CORE|#LOCALIZATION|#INDUSTRY|#PARTNER|#CUSTOMER`](abencds_f1_metadata_ext_annos.md) · [`@entity_annot1`](../abap-cds-data-definitions/abencds_f1_entity_annotations.md) · [`@entity_annot2`](../abap-cds-data-definitions/abencds_f1_entity_annotations.md) · [`parameter_list`](abencds_f1_annotate_view_para_list.md) · [`element_list`](abencds_f1_annotate_view_sele_list.md) · [`@Metadata.layer: #CORE|#LOCALIZATION|#INDUSTRY|#PARTNER|#CUSTOMER`](abencds_f1_metadata_ext_annos.md) · [`@entity_annot1`](../abap-cds-data-definitions/abencds_f1_entity_annotations.md) · [`@entity_annot2`](../abap-cds-data-definitions/abencds_f1_entity_annotations.md) · [`@view_entity_annot1`](../abap-cds-data-definitions/abencds_view_entity_anno.md) · [`@proj_view_annot1`](../abap-cds-data-definitions/abencds_proj_view_annotations.md) · [`@_view_annot1`](../abap-cds-obsolete-language-elements/abencds_view_anno_v1.md) · [`@view_entity_annot2`](../abap-cds-data-definitions/abencds_view_entity_anno.md) · [`@proj_view_annot2`](../abap-cds-data-definitions/abencds_proj_view_annotations.md) · [`@_view_annot2`](../abap-cds-obsolete-language-elements/abencds_view_anno_v1.md) · [`parameter_list`](abencds_f1_annotate_view_para_list.md) · [`element_list`](abencds_f1_annotate_view_sele_list.md)

## Description

Defines a [CDS metadata extension](../../abap-glossary/abencds_metadata_extension_glosry.md) (MDE for short) in dedicated [`DDLX` source code](../../abap-glossary/abenddlx_source_code_glosry.md).

- `ANNOTATE ENTITY`

  Defines an MDE for any [CDS entity](../../abap-glossary/abencds_entity_glosry.md) except [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md).

- `ANNOTATE VIEW`

  Defines an MDE specifically for a [CDS view](../../abap-glossary/abencds_view_glosry.md).

The CDS metadata extension adds metadata to a CDS entity as [CDS annotations](../../abap-glossary/abencds_annotation_glosry.md). The entity in question must exist, be specified using the name of its [CDS entity](../../abap-glossary/abencds_entity_glosry.md) `cds_entity` or `cds_view`, and contain the annotation `Metadata.allowExtensions` with the default value `true` in its source code. A CDS entity can have more than one CDS metadata extension. `ANNOTATE ENTITY` can be used for all CDS entities including CDS views. `ANNOTATE VIEW` can be used for CDS views only.

The annotation [`@Metadata.layer`](abencds_f1_metadata_ext_annos.md) must be specified with one of the enumeration symbols shown in the example in front of the statement `ANNOTATE` to define the layer of the metadata extension. In the [analysis of metadata extensions](abencds_meta_data_extension_eval.md), the layer determines the priority of the metadata if there are multiple metadata extensions for the same CDS entity. The enumeration symbols are listed with the lowest priority ones on the left and the highest priority on the right. `#CORE` therefore has the lowest, and `#CUSTOMER` the highest priority. A syntax check warning is issued for annotations specified more than once, and the system uses the annotation of the first metadata extension found.

The annotations added to the extended entity are defined as follows. A metadata extension must contain at least one of these.

- Annotations in front of the statement `ANNOTATE`

  - Only entity annotations `@entity_annot` can be specified in front of the statement `ANNOTATE ENTITY`. Valid [SAP annotations](abencds_annotations_sap.md) must be in the [scope](abencds_annotations_scopes.md) of the [entity annotations](../abap-cds-data-definitions/abencds_f1_entity_annotations.md). They are added to the entity annotations of the extended entity.

  - Entity annotations and view annotations `@view_annot` can be specified in front of the statement `ANNOTATE VIEW`. Valid [SAP annotations](abencds_annotations_sap.md) must be in the [scope](abencds_annotations_scopes.md) of the [view annotations](../abap-cds-data-definitions/abencds_view_entity_anno.md). They are added to the view annotations of the extended view.

- [`parameter_list`](abencds_f1_annotate_view_para_list.md) is used to specify annotations for the parameters of the extended entity.

- [`element_list`](abencds_f1_annotate_view_sele_list.md) is used specify annotations for the elements of `SELECT` list of the extended entity.

In metadata extensions, only those annotations can be specified for which this is allowed in their [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) using the annotation `@MetadataExtension.usageAllowed:true`. In the CDS metadata extension, an annotation can be used in the same scope defined using `@Scope` as in a data definition. All other annotations produce syntax errors.

These annotations of a metadata extension are respected in the evaluation of annotations with the methods of the class `CL_DD_DDL_ANNOTATION_SERVICE` except for `GET_DIRECT_ANNOS_`, in accordance with the layers defined by the annotation `@Metadata.layer`. Here the annotations of a metadata extension always have a higher priority than the annotations specified in the source code of the CDS entity. These are only respected if they are not overridden by a corresponding annotation of a metadata extension. For the exact description of the evaluation, see section [evaluation of metadata extensions](abencds_meta_data_extension_eval.md).

## Hints

- Unlike the specification of annotations in the source code of the extended CDS entity, it is not possible to have any arbitrary annotations in metadata extensions; it is only possible to have [SAP annotations](abencds_annotations_sap.md). The syntax check for a metadata extension checks the validity of its specification with respect to the [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md):

  - the name of an annotation

  - the validity of the [annotation values](../../abap-glossary/abenannotation_value_glosry.md), the type, and (for enumerations) the enumeration symbol

  - the [scope](abencds_annotations_scopes.md)

  - whether any [annotation arrays](../../abap-glossary/abenannotation_array_glosry.md) are specified correctly (they must only be specified using square brackets). The format `@annot: value` is not possible. `@annot: [value]` must be used instead. The array can contain only similar elements (in accordance with its definition).

- The annotations (of a CDS entity) specified in metadata extensions does not have any effect on the activation or the behavior at runtime. They are only respected by the class `CL_DD_DDL_ANNOTATION_SERVICE`.

- The program `ABAP_DOCU_MDE_ANNOS` shows all annotations that can be specified in metadata extensions.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following metadata extension named `DEMO_CDS_METADATA_EXTENSION` adds annotations with original language *German* to the CDS view entity `DEMO_CDS_PARAMETERS` from the executable example for [CDS view entities with parameters](../../abap-programming-language/abap-database-access/abenselect_cds_para_abexa.md). The class `CL_DEMO_CDS_META_DATA_EXT` reads the annotations of the view with the methods of the classes `CL_DD_DDL_ANNOTATION_SERVICE` and `CL_DD_DDL_ANALYZE`. The method `GET_ANNOS` of the class `CL_DD_DDL_ANNOTATION_SERVICE` covers both the annotations specified in the metadata extension and the translations into the current text environment language. The method `GET_ANNOTATIONS` of the class `CL_DD_DDL_ANALYZE` only evaluates the specifications in the view `DEMO_CDS_PARAMETERS`.

``` abap
@Metadata.layer:#INDUSTRY
             
@EndUserText.label: 'Demo for View with Parameters'

annotate view demo_cds_parameters with
  parameters
    @EndUserText.label: 'Lower limit for distance'
    p_distance_l,
    @EndUserText.label: 'Upper limit for distance'
    p_distance_u,
    @EndUserText.label: 'Unit of distance'
    p_unit
{
  @EndUserText.label: 'Airline carrier'
  carrid;
  @EndUserText.label: 'Flight connection'
  connid;
  @EndUserText.label: 'Departure from city'
  cityfrom;
  @EndUserText.label: 'Arrival in city'
  cityto;
  @EndUserText.label: 'Flight distance'
  distance;
  @EndUserText.label: 'Unit of flight distance'
  distid;
};
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following metadata extension `DEMO_CDS_MDE_FOR_ABSTR_ENT` adds entity annotations and element annotations to the [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md) `DEMO_CDS_ABSTRACT_ENTITY_ELEM` from the example for its [element annotations](../abap-cds-data-definitions/abencds_f1_absent_list_annotation.md).

``` abap
@Metadata.layer: #CORE
@EndUserText.label : 'Label from MDE'
annotate entity demo_cds_abstract_entity_elem with
  {
    @EndUserText.quickInfo: 'Quickinfo from MDE'
    col2;
  }
```
