---
title: "CDS DDL - DEFINE ABSTRACT ENTITY"
source_file: abencds_f1_define_abstract_entity.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Abstract Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE ABSTRACT ENTITY

## Syntax

``` abap
[@entity_annot1] 
[@entity_annot2] 
... 
[DEFINE] [ROOT] ABSTRACT ENTITY abstract_entity 
         [parameter_list] 
          element_list[;]  
```

[`@entity_annot1`](abencds_f1_entity_annotations.md) · [`@entity_annot2`](abencds_f1_entity_annotations.md) · [`parameter_list`](abencds_f1_entity_parameter_list.md) · [`element_list`](abencds_f1_absent_element_list.md)

## Description

Defines an [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md) `abstract_entity` in [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md). When a CDS abstract entity is activated, its metadata is created but no other object instances are created on the database or in AS ABAP. The name `abstract_entity` must comply with the naming conventions for [dictionary types](../../abap-dictionary-ddic/ddic-data-types/abenddic_data_types.md) and can have a maximum of 30 characters.

- [`@entity_annot`](abencds_f1_entity_annotations.md) can be used to specify optional [annotations](../../abap-glossary/abencds_annotation_glosry.md) for the CDS abstract entity.

- [`parameter_list`](abencds_f1_entity_parameter_list.md) is used to declare a list of optional input parameters for the CDS abstract entity.

- [`element_list`](abencds_f1_absent_element_list.md) is used to declare elements, CDS associations, CDS to-child associations, and CDS-to-parent associations of the CDS abstract entity.

A CDS abstract entity can be used as a global structured type in ABAP programs. The entity is located in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP. The elements of the CDS abstract entity define the components of the global structured type that can be referenced in ABAP programs using `TYPE`. As is the case for any CDS entity, the annotations of a CDS abstract entity can be evaluated.

In ABAP CDS, the keyword `ROOT` is used to define the CDS abstract entity `abstract_entity` as a [root entity](../../abap-glossary/abenroot_entity_glosry.md) of the hierarchy of a [business object](../../abap-glossary/abenbusiness_object_glosry.md). The following applies to the root entity:

- There is exactly one root entity in the structure of a business object.

- A root entity can have [child entities](../../abap-glossary/abenchild_entity_glosry.md) defined by means of [to-child associations](../../abap-glossary/abento_child_association_glosry.md) using the keyword [`COMPOSITION`](abencds_absent_composition.md), but this is not mandatory. A root entity can also be a [leaf entity](../../abap-glossary/abenleaf_entity_glosry.md).

- A root entity does not have a [parent entity](../../abap-glossary/abenparent_entity_glosry.md). [To-parent](abencds_absent_to_parent_assoc.md) associations are not allowed in root entities.

## Hints

- A CDS abstract entity cannot be used as a data source in other CDS entities or in ABAP SQL.

- The [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md) of a CDS abstract entity must have the same name as this entity.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following DDL source code shows a CDS abstract entity:

``` abap
@EndUserText.label: 'Abstract CDS Entity'
@Metadata.allowExtensions: false
define abstract entity demo_cds_abstract_entity
  {
    key col1 : abap.char(3);
        col2 : abap.int4;
        col3 : abap.string;
        col4 : DEMO_BT_CHAR_TEXT;
  }
```

The class `CL_DEMO_CDS_ABSTRACT_ENTITY` demonstrates the following:

- The structure of the CDS abstract entity can be evaluated using [RTTI](../../abap-glossary/abenrun_time_type_identific_glosry.md) methods.

- The annotations of the CDS abstract entity can be evaluated using the class `CL_DD_DDL_ANNOTATION_SERVICE`.

- The structure of the CDS abstract entity can be used as a data type in the ABAP program.
