---
title: "C0 Contract Rules for Consumers of CDS Entities"
source_file: abenc0_consumer_rules_cds.html
section: "ABAP APIs > Release Contracts > Contract Rules for API Consumers"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# C0 Contract Rules for Consumers of CDS Entities

The provider rules for objects with the C0 contract ensure that released objects are changed only in a restricted way and help to avoid errors and interruptions after an SAP upgrade. Nevertheless, the rules do not prescribe full downward compatibility and leave some room for necessary enhancements to [released APIs](../../abap-glossary/abenreleased_api_glosry.md). Therefore, users of released APIs still have to consider the allowed compatible changes and access the APIs in such a way that the following errors and interruptions are avoided:

- Problems during an upgrade. Syntax errors after an upgrade. Runtime errors after an upgrade. Wrong behavior after an upgrade.

The following sections list allowed extensions to released APIs that must be considered when creating an extension.

- [Naming Rules](abenc0_consumer_rules_cds.md#naming-rules)

- [General Rules](abenc0_consumer_rules_cds.md#general-rules)

- [Restrictions](abenc0_consumer_rules_cds.md#restrictions)

## Naming Rules

- The alias name for elements and associations must start with the correct namespace prefix. For customers and partners, this means that either `ZZ` or `YY` must be used as prefix. For associations, it is strongly recommended that the alias name starts with an underscore (\_) followed by the correct namespace prefix.

- All elements and associations defined in the extension must have the element suffix that is defined in the released API by means of the annotation [`@AbapCatalog.extensibility.elementSuffix`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_entity_annotations.md).

- In extensions to [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) and [CDS projection views](../../abap-glossary/abencds_projection_view_glosry.md), all elements and associations defined in the extension must have the alias name of a stable data source, defined by the annotation [`@AbapCatalog.extensibility.dataSources`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_view_entity_anno.md), as prefix.

Examples for correct names:

- `DatasourceAlias.field as ZZ_customerField_suffix`

- `DatasourceAlias._assoc as _YY_assoc_suffix`

## General Rules

- Currently, [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md), [CDS projection views](../../abap-glossary/abencds_projection_view_glosry.md), [CDS abstract entities](../../abap-glossary/abencds_abstract_entity_glosry.md), and [CDS custom entities](../../abap-glossary/abencds_abstract_entity_glosry.md) can be extended.

- The extended CDS entity must be released under the C0 contract for the corresponding language version ([ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md) or [ABAP for Key Users](../../abap-glossary/abenabap_for_key_users_glosry.md)).

- The extension must fit the quota definition defined in the extended entity by means of the annotations [`AbapCatalog.extensibility.quota.maximumBytes`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_entity_annotations.md) and [`AbapCatalog.extensibility.quota.maximumFields`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_entity_annotations.md). That means that the maximum number of fields and the maximum number of bytes must not be exceeded.

**Rules for Extension Fields**

- To define an additional field for a C0 released API that is selected from another data source, the field must either belong to the same software component, or be C1 released.

- To define additional fields for a released API, in a scenario where these additional fields are selected from another extension, both extensions must be assigned to the same software component or the extended entity must be C1 released.

**Rules for Node Extension**

- Adding new child nodes to a released API by means of [CDS compositions](../../abap-glossary/abencds_composition_glosry.md) is allowed if the annotation [`@AbapCatalog.extensibility.allowNewCompositions`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_entity_annotations.md) is set to `true`.

**Rules for Associations**

- Associations that are released with a stable alias name by the extended entity, using the annotation `AbapCatalog.extensibility.dataSources`, must not be exposed in the element list.

- To define a new association in an extension, the association target must be [C1 released](../../abap-glossary/abenc1_contract_glosry.md) or created in the same software component.

- Newly defined, local associations can be exposed in the element list. The name of a newly defined, local association must comply with the naming rules described in section **Naming**.

**Rules for Path Expressions:**

- In an extension to a released API, exposed associations and associations used within path expressions can have a target [cardinality](../../abap-glossary/abencardinality_glosry.md) of 0 or 1. A target cardinality greater than 1 is not allowed.

- Path traversing with the exact length of 1 is allowed for released data sources with stable alias names.

- Path traversing with the exact length of 1 is **not** allowed for locally defined associations.

- Path traversing with a length greater than 1 is only allowed in the following cases:

  - The extended object must be a CDS projection view.

  - The annotation [`@AbapCatalog.extensibility.allowNewDatasources`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_view_entity_anno.md) is set to `true`.

  - All traversed objects of the path are CDS view entities or CDS DDIC-based views.

  - Examples for path lengths:

    `BaseObjectAlias.fieldName` //path length of 1 `BaseObjectAlias._assoc.fieldName` //path length of 2

## Restrictions

- The following data types are not supported in extensions to released APIs: [`LCHR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`LRAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`STRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`RAWSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`GEOM_EWKB`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- Reusing expressions using [`$projection`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_reusable_expression_v2.md) as pointer is not supported when extending a released API.

- [Session variables](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_session_variable_v2.md) are not supported when extending a released API.

- The built-in function [`utcl_current`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_timestamp_functions_v2.md) is not supported in extensions to released APIs.
