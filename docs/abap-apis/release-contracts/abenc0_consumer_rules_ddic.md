---
title: "C0 Contract Rules for Consumers of DDIC Objects"
source_file: abenc0_consumer_rules_ddic.html
section: "ABAP APIs > Release Contracts > Contract Rules for API Consumers"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# C0 Contract Rules for Consumers of DDIC Objects

The provider rules for objects with the C0 contract ensure that released objects are changed only in a restricted way and help to avoid errors and interruptions after an SAP upgrade. Nevertheless, the rules do not prescribe full downward compatibility and leave some room for necessary enhancements to [released APIs](../../abap-glossary/abenreleased_api_glosry.md). Therefore, the users of released APIs still have to consider the allowed compatible changes access the APIs in such a way that the following errors and interruptions are avoided:

- Problems during an upgrade.

- Syntax errors after an upgrade.

- Runtime errors after an upgrade.

- Wrong behavior after an upgrade.

The following sections list rules for extensions to released APIs that must be considered when creating an extension.

- [Naming Rules](abenc0_consumer_rules_ddic.md#naming-rules)

- [Rules for Extensions](abenc0_consumer_rules_ddic.md#rules-for-extensions)

- [Rules for Using Released DDIC Objects](abenc0_consumer_rules_ddic.md#rules-for-using-released-ddic-objects)

## Naming Rules

- All extension field names must start with the correct namespace prefix.

- All extension fields must have the element suffix that is defined in the released API by means of the annotation [`@AbapCatalog.enhancement.fieldSuffix`](../../abap-dictionary-ddic/ddic-data-types/abenddicddl_define_ext_annos.md).

## Rules for Extensions

- Only [DDIC database tables](../../abap-glossary/abenddic_db_table_glosry.md) and [DDIC structures](../../abap-glossary/abenddic_structure_glosry.md) are available for [C0 developer extensibility](../../abap-glossary/abendev_extensibility_glosry.md) from a [restricted ABAP language version](../../abap-glossary/abenrestricted_version_glosry.md).

- The DDIC object must be released under the C0 contract for the corresponding language version ([ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md) or [ABAP for Key Users](../../abap-glossary/abenabap_for_key_users_glosry.md)).

- All extension fields must be typed with a [DDIC data element](../../abap-glossary/abendata_element_glosry.md) or with a built-in data type from the ABAP Dictionary using the syntax `abap.type[(n)|(n,m)]`. Typing with other structures or [DDIC table types](../../abap-glossary/abenddic_table_type_glosry.md) is not possible.

- The extension must fit the quota definition and quota distribution defined in the extended object by means of the annotations [`@AbapCatalog.enhancement.quotaMaximumFields`](../../abap-dictionary-ddic/ddic-data-types/abenddicddl_define_ext_annos.md), [`@AbapCatalog.enhancement.quotaMaximumBytes`](../../abap-dictionary-ddic/ddic-data-types/abenddicddl_define_ext_annos.md), [`@AbapCatalog.enhancement.quotaShareCustomer`](../../abap-dictionary-ddic/ddic-data-types/abenddicddl_define_ext_annos.md), and [`@AbapCatalog.enhancement.quotaSharePartner`](../../abap-dictionary-ddic/ddic-data-types/abenddicddl_define_ext_annos.md).

## Rules for Using Released DDIC Objects

- When using a C0 released structure as [include structure](../../abap-dictionary-ddic/ddic-data-types/abenddic_include_structure.md) of another dictionary object, the addition `WITH SUFFIX suffix` must not be used.

- When using a C0 released structure as [include structure](../../abap-dictionary-ddic/ddic-data-types/abenddic_include_structure.md), this include structure must not be defined as a key using the addition [`KEY`](../../abap-dictionary-ddic/ddic-database-tables/abenddicddl_define_table_incl.md).

- C0 released structures must not be used as [include structure](../../abap-dictionary-ddic/ddic-data-types/abenddic_include_structure.md) in any DDIC view.

- When using a C0 released structure as [include structure](../../abap-dictionary-ddic/ddic-data-types/abenddic_include_structure.md) of another dictionary object, the value of the annotation `@AbapCatalog.enhancement.category` of the enclosing object must be greater than or equal to the enhancement category of the included structure. `#EXTENSIBLE_ANY` is greater than `#EXTENSIBLE_CHARACTER_NUMERIC`.

- If a C0 released structure is included in any other DDIC object as [include structure](../../abap-dictionary-ddic/ddic-data-types/abenddic_include_structure.md) (syntax statement `include`), this inclusion must not be removed. The inclusion of a C0 released structure must remain stable. Otherwise, an [ATC](../../abap-glossary/abenatc_glosry.md) error occurs.

## Restrictions

- An extension must not define any element as a key field.

- The following data types are not supported in extensions to released APIs: [`LCHR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`LRAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`STRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`PREC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`RAWSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`GEOM_EWKB`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length \> 1333, [`RAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length \> 255.
