---
title: "BDEF friend"
source_file: abenrap_bdef_friend_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# BDEF friend

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

A BDEF friend is a [BDEF extension](abenrap_extension_glosry.md) whose implementation has unrestricted access to all components of the original [BDEF](abencds_behavior_definition_glosry.md). For example, a BDEF friend can call [internal RAP BO operations](abenrap_internal_operation_glosry.md) and read or modify RAP BO entities [`IN LOCAL MODE`](../abap-rap-business-objects/abap-for-rap-business-objects/abapin_local_mode.md). A BDEF friend is declared using the optional addition [`with friends`](../abap-rap-business-objects/rap-behavior-definitions/abenbdl_with_friends.md). BDEF friends can be used for modularization purposes.

[***-\>* More about**](../abap-rap-business-objects/rap-behavior-definitions/abenbdl_with_friends.md)
