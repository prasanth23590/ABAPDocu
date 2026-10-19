---
title: "C0 Contract Rules for Consumers of RAP Behavior Definitions"
source_file: abenc0_consumer_rules_bdef.html
section: "ABAP APIs > Release Contracts > Contract Rules for API Consumers"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# C0 Contract Rules for Consumers of RAP Behavior Definitions

The provider rules for objects with a C0 contract ensure that released objects are changed only in a very restricted way and help to avoid errors and interruptions after an SAP upgrade. Nevertheless, the rules do not prescribe full downward compatibility and leave some room for necessary enhancements to [released APIs](../../abap-glossary/abenreleased_api_glosry.md). Therefore, the users of released APIs still have to consider the allowed compatible changes and access the APIs in such a way that the following errors and interruptions are avoided:

- Problems during an upgrade.

- Syntax errors after an upgrade.

- Runtime errors after an upgrade.

- Wrong behavior after an upgrade.

When extending BDEFs, consumers must obey the following naming rules to avoid naming conflicts.

## Naming Rules

The following applies to extensions in [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md):

- If the extension has a [namespace prefix](../../abap-glossary/abenname_space_prefix_glosry.md), such as `/PREFIX/`, its elements must also have this prefix.

1.  If the name of the extension starts with *Z* or with *Y*, its element names must begin with *ZZ* or with *YY*. Additionally, if the element name begins with *YY*, this prefix *YY* must not be followed by *A*, *M*, *S*, or the digits *1* to *9*.

2.  Otherwise, if the name of the extension does not start with *Z* or with *Y*, the element name must not begin with a namespace prefix, nor with *ZZ* or *YY*.

3.  If the behavior for an extension node is defined ([extension entity behavior definition](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_define_beh_extend.md)), the element names inside this entity must either be without prefix, or they are checked against the name of the extension according to the rules above.

The following applies to extensions in [Standard ABAP](../../abap-glossary/abenstandard_abap_glosry.md):

- Element names must either be without prefix, or the element names are checked against the name of the extension according to rules 1 - 3 listed above.

The checks apply to the following elements:

- [Alias names](../../abap-glossary/abenalias_glosry.md) of [RAP BO entities](../../abap-glossary/abenrap_bo_entity_glosry.md).

- External names of RAP BO entities, specified using the addition [`external`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_define_beh.md).

- Alias names of associations, specified using the addition [`abbreviation`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_association.md)

- Alias names of [RAP foreign entities](../../abap-glossary/abenrap_foreign_entity_glosry.md).

- Names of [RAP actions](../../abap-glossary/abenrap_action_glosry.md) and [RAP functions](../../abap-glossary/abenrap_function_glosry.md).

- External names of RAP actions and RAP functions, specified using the addition `external`.

- External names of action and function results, specified using the addition [`external`](../../abap-rap-business-objects/rap-behavior-definitions/abenbdl_action_output_para.md).

- Names of [RAP determinations](../../abap-glossary/abenrap_determination_glosry.md) and [RAP validations](../../abap-glossary/abenrap_validation_glosry.md).

- Names of [RAP BO determine actions](../../abap-glossary/abenrap_bo_det_action_glosry.md).

- Names of [RAP business events](../../abap-glossary/abenrap_entity_event_glosry.md).
