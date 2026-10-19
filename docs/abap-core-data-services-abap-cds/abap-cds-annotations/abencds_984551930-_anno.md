---
title: "MappingRole"
source_file: abencds_984551930-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > MappingRole"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MappingRole

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `MappingRole`                                                 |
| **Scope**   | `#ROLE`                                                       |
| **Type**    | `Boolean`                                                     |
| **Enums**   | `-`                                                           |
| **Default** | `true`                                                        |
| **Text**    | `-`                                                           |
| **MDE**     | `-`                                                           |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM` |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## MappingRole

Defines the assignment of a CDS role to users in a role definition of CDS DCL.

## Annotation Values

true: The role is assigned to all users regardless of the client. The access rules are defined by access conditions, which are usually user-specific.

false: This value cannot be used.

If the annotation is not specified, the value false would be used.

## Note

The CDS access control must be assigned to the users of the system. Currently, the only possibiltiy is to assign it to all users. Thats why 'false' is not supported and it is mandatory to specify @MappingRole: true in front of DEFINE ROLE. Otherwise, a syntax error occurs.
