---
title: "ObjectModel.association.toHierarchy"
source_file: abencds_556934736-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > ObjectModel"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ObjectModel.association.toHierarchy

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `ObjectModel.association.toHierarchy`                              |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `Boolean`                                                          |
| **Enums**   | `-`                                                                |
| **Default** | `true`                                                             |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_SAP_CLOUD_PLATFORM`                                  |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## ObjectModel

### Short Description

ObjectModel annotations provide definitions of text-related aspects of the CDS-based data model.

## association

No KTD found

## toHierarchy

### Short Description

As one element of a CDS Entity assigned multiple different hierarchy definitions, the hierarchies must not be annotated at the element directly to support extension scenarios. Therefore, the annotation (`@ObjectModel.association.toHierarchy`) is needed that can annotate exposed associations as hierarchies. Afterwards, one of these hierarchies can be chosen with the annotation (`@Consumption.filter.hierarchyAssociation`) for the corresponding element on a higher layer in the data model. This could be done on SAP side in the corresponding entity or from a customer in a customer extend.

### Use Case: Support of custom hierarchies in Analytics scenarios

- `@ObjectModel.association.toHierarchy`: true \| `@ObjectModel.association.toHierarchy` : annotates that the corresponding exposed association is a hierarchy and can therefore be used at a later point in a higher layer of the data model for the corresponding representative key.

- `@ObjectModel.association.toHierarchy`: false : annotates that the corresponding exposed association cannot be used as a hierarchy at a later point for the corresponding representative key.
