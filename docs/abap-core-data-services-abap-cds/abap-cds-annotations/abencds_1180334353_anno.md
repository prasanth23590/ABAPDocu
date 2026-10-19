---
title: "AccessControl.authorizationCheck"
source_file: abencds_1180334353_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AccessControl"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AccessControl.authorizationCheck

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)                            |
|-------------|-------------------------------------------------------------------------------|
| **Syntax**  | `AccessControl.authorizationCheck`                                            |
| **Scope**   | `#EXTERNAL_ENTITY`, `#HIERARCHY`, `#TABLE_ENTITY`, `#TABLE_FUNCTION`, `#VIEW` |
| **Type**    | `String(20)`                                                                  |
| **Enums**   | `#CHECK, #MANDATORY, #NOT_ALLOWED, #NOT_REQUIRED, #PRIVILEGED_ONLY`           |
| **Default** | `#NOT_REQUIRED`                                                               |
| **Text**    | `-`                                                                           |
| **MDE**     | `-`                                                                           |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`                 |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AccessControl

Defines access control for a CDS object.

## authorizationCheck

Defines implicit access control when ABAP SQL is used to access the CDS object.

If the annotation is not specified, the value \#NOT_REQUIRED is used.

## Enums

## \#NOT_REQUIRED

Like \#CHECK, but there is no syntax check warning.

When no access control exists, all users have full access to the entity. When an access control exist, it is evaluated.

## \#NOT_ALLOWED

No access control shall exist. When an access control exists, it is ignored at runtime. Use this for technical entities where access control would be harmful. This value does not prevent the creation of access controls, however a warning will be emitted that the access control is not applied at runtime.

## \#MANDATORY

An access control must exist. When no access control has been created for the entity, a runtime error will occur when the entity is accessed in ABAP SQL. Use this for entities where access control is critical and accidental removal of the access control must not remain unnoticed.

## \#CHECK

If ABAP SQL is used to access the view, access control is performed implicitly if a CDS role is assigned to the view.

The runtime behavior is identical to \#NOT_REQUIRED, however there is a syntax warning in the CDS object when no access control exists yet.

## \#PRIVILEGED_ONLY

This special value is only evaluated by dedicated frameworks (SADL). For ABAP SQL, the actual behavior is like \#CHECK. Customers shall not use this value unless explicitly requested by documentation.

## Further Information

- The value `#NOT_REQUIRED` is recommended for CDS objects that do not require [access control](../../abap-glossary/abencds_access_control_glosry.md) in the beginning, but that might later on be enhanced with roles.

- [CDS access control](../../abap-glossary/abencds_access_control_glosry.md) does not work for client-independent access. For CDS objects that are subject to client-independent access, it is recommended that the annotation `AccessControl.authorizationCheck:#NOT_ALLOWED` is used.

- There are some restrictions for CDS hierarchies that are described under [DCL Restrictions for CDS Hierarchies](../abap-cds-access-control/abencds_f1_dcl_hierarchies.md).

- In the context of the [ABAP RESTful Application Programming Model](../../abap-glossary/abenarap_glosry.md), additional rules for using this annotation apply. They are described in the topic [RAP - CDS-Based Authorization](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_cds_based_auth.md).

- The value `#NOT_ALLOWED` disables implicit access control when the CDS view entity is accessed in ABAP SQL. To disable access control for views not annotated with this annotation, the addition [`WITH PRIVILEGED ACCESS`](../../abap-programming-language/abap-database-access/abapselect_data_source.md) can be used in the [`FROM`](../../abap-programming-language/abap-database-access/abapfrom_clause.md) clause.

- During update sessions the authorization check must be disabled with the annotation or with the ABAP SQL addition `WITH PRIVILEGED ACCESS`. If not, a [runtime error](../../abap-glossary/abenruntime_error_glosry.md) occurs.

- [CDS access control](../../abap-glossary/abencds_access_control_glosry.md) does not work for client-independent access. This is why in ABAP SQL, the addition `USING` can only be used when accessing CDS entities where access control is disabled. It is recommended that the annotation `AccessControl.authorizationCheck:#NOT_ALLOWED` is only specified for CDS objects that are subject to client-independent access.

- The obsolete addition `CLIENT SPECIFIED` can also only be used when accessing CDS objects where access control is disabled.
