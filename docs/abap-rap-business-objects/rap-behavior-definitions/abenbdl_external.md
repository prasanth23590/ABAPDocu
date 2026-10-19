---
title: "RAP - external"
source_file: abenbdl_external.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - RAP BO Operation, Additions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - external

## Syntax

``` abap
... external 'ExternalName' ...  
```

## Description

The [RAP BO operation addition](abenbdl_operations_additions.md) `external` can be used to provide an alias name for external usage. This external name is exposed in the OData metadata, but it is not known by ABAP. It can be much longer than the actual action name.

The external name `ExternalName` is specified in single quotes (`'`).

An external name can be specified in all positions where this is documented, for example, for [entity behavior definitions](../../abap-glossary/abencds_entity_bdef_glosry.md), [actions](../../abap-glossary/abenrap_action_glosry.md), and [functions](../../abap-glossary/abenrap_function_glosry.md).

## Hint

In the case of a [RAP default values function](../../abap-glossary/abenrap_bo_defaulting_glosry.md), the optional external name must start with `GetDefaultsFor`. Otherwise, a syntax check error occurs. For further details, see the topic [RAP - `default function`](abenbdl_default_function.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following RAP BO interface defines an external name for the entity behavior definition.

``` abap
interface;
extensible;

define behavior for DEMO_INTF_M alias root_interface
  external 'ThisIsAnExternalName'
{
  use create;
  use update;
  use delete;
}
```
