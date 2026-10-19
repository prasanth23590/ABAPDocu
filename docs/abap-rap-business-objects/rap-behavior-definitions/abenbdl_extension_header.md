---
title: "RAP - ExtensionHeader"
source_file: abenbdl_extension_header.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - Base BDEF Extension > RAP - extension"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - ExtensionHeader

## Syntax

``` abap
... 
[implementation in class ClassName unique;] 
[with privileged mode disabling ContextName;] 
[extensible  ;] 
...  
```

[`implementation in class ClassName unique`](abenbdl_in_class_unique_ext.md) · [`with privileged mode disabling ContextName`](abenbdl_privileged_mode_extension.md) · [`extensible `](abenbdl_ext_enabl_ext_base.md)

## Description

The following elements are supported in a [BDEF extension header](../../abap-glossary/abenrap_bdef_ext_header_glosry.md):

- [`implementation in class ClassName unique`](abenbdl_in_class_unique_ext.md): Specifies an [extension](../../abap-glossary/abenrap_prefix_extension_glosry.md) [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) for the extension behavior implementation of a [BDEF extension](../../abap-glossary/abenrap_extension_glosry.md). Optional and only required if the [BDEF extension](../../abap-glossary/abenrap_extension_glosry.md) defines implementation-relevant components.

- [`with privileged mode disabling AuthContext`](abenbdl_privileged_mode_extension.md): Enables [BDEF privileged mode](../../abap-glossary/abenrap_privileged_mode_glosry.md). The effect is that the [authorization context for disable](../../abap-glossary/abencds_auth_context_glosry.md)`ContextName` is automatically disabled when a [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) accesses the business object in question with a [privileged EML call](../abap-for-rap-business-objects/abapeml_privileged.md).

- [`extensible`](abenbdl_ext_enabl_ext_base.md): If specified, [extension layering](../../abap-glossary/abenrap_ext_layering_glosry.md) is allowed. For details, see [RAP - Extensibility Enabling for Base BDEF Extensions](abenbdl_ext_enabl_ext_base.md).
