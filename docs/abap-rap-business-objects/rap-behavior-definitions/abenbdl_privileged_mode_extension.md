---
title: "RAP - with privileged mode, Extension"
source_file: abenbdl_privileged_mode_extension.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - Base BDEF Extension > RAP - extension > RAP - ExtensionHeader"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - with privileged mode, Extension

## Syntax

``` abap
... 
with privileged mode disabling ContextName; 
...  
```

## Description

Enables [BDEF privileged mode](../../abap-glossary/abenrap_privileged_mode_glosry.md) for an extended RAP BO. BDEF privileged mode is a prerequisite for using the addition [`PRIVILEGED`](../abap-for-rap-business-objects/abapeml_privileged.md) in [ABAP EML](../../abap-glossary/abenabap_eml_glosry.md) when consuming the extended RAP BO.

`ContextName` must be an [authorization context for disable](../../abap-glossary/abencds_auth_context_glosry.md) that is specified in the same BDEF extension. Only one authorization context for disable can be specified after `with privileged mode disabling`.

The effect is that the [authorization context](../../abap-glossary/abencds_auth_context_glosry.md) `ContextName` is automatically disabled when a [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) uses [privileged access](../abap-for-rap-business-objects/abapeml_privileged.md) to the extended RAP BO in question.

Privileged access with [ABAP EML](../../abap-glossary/abenabap_eml_glosry.md) is possible as soon as either the original BDEF or one of its extensions specifies privileged mode. The following rules apply:

- If the base BDEF specifies BDEF privileged mode, but the extension does not specify privileged mode, privileged EML access is allowed.

- If the base BDEF does not specify BDEF privileged mode, but an extension specifies BDEF privileged mode, privileged EML access is allowed, but a syntax check warning occurs. This is because the base BDEF itself does not enable BDEF privileged mode, and privileged access depends on the extension. If the extension were deleted, the privileged call would get syntax check errors.

For further details, see

- [RAP BDL - `with privileged mode`](abenbdl_privileged_mode.md).

- [ABAP EML - `PRIVILEGED`](../abap-for-rap-business-objects/abapeml_privileged.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code shows BDEF extension `DEMO_RAP_EXTENSION_2`. It extends BDEF `DEMO_RAP_EXTENSIBLE_ROOT`. The extension defines an authorization context for disable `Context02`, which is disabled in privileged mode.

``` abap
extension using interface demo_rap_ext_using_interface;
with privileged mode disabling Context02;

extend behavior for RootInterface
{
}

define authorization context Context02
{
  'AUTHOBJ8';
}
```
