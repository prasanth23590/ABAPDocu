---
title: "RAP - EntityBehaviorBody, Interface BDEF"
source_file: abenbdl_body_interface.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Interface Behavior Definition > RAP - EntityBehaviorDefinition, Interface BDEF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - EntityBehaviorBody, Interface BDEF

## Syntax

``` abap
 
... [use  ]; 
    [FieldCharacteristics]; 
...  
```

[`use `](abenbdl_use_projection.md) · [`FieldCharacteristics]`](abenbdl_field_interface.html)

## Description

In the [entity behavior body](../../abap-glossary/abencds_entity_body_glosry.md) of an [interface BDEF](../../abap-glossary/abencds_interface_bdef_glosry.md), elements of the projected BDEF can be reused and field characteristics can be specified:

- [`use`](abenbdl_use_projection.md):

  [Reuse](abenbdl_use_projection.md) of [RAP BO operations](../../abap-glossary/abenrap_bo_operation_glosry.md) and [RAP business events](../../abap-glossary/abenrap_entity_event_glosry.md). All operations (standard operations, operations for associations, actions, [functions](../../abap-glossary/abenrap_function_glosry.md), and draft actions) and events that are to be reused from the [base BO](../../abap-glossary/abenrap_projected_bo_glosry.md) must be explicitly specified using the keyword `use`. Reuse works as described in topic [RAP BDL - use](abenbdl_use_projection.md) with one exception: the additions `precheck` and `augment` are not available for interface BDEFs.

- [`FieldCharacteristics`](abenbdl_field_interface.md):

  An interface BDEF automatically and implicitly inherits all field characteristics of the underlying base BO and it can add further field attributes, as long as they do not contradict the field attributes from the base layer. A list of available field characteristics in interface BDEFs is provided in topic [Field Characteristics, Interface BDEF](abenbdl_field_interface.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows an interface BDEF. The projected BO is `DEMO_RAP_UNMANAGED_DRAFT_ROOT`. The interface BDEF reuses draft handling and standard operations from the underlying BO. It also defines a foreign entity and excludes a field from the BDEF derived types.

``` abap
interface;
use draft;
foreign entity demo_cds_validation;
define behavior for DEMO_RAP_INTERFACE_DRAFT alias Root
use etag
{
  use create;
  use update;
  use delete;

  use action Activate;
  use action Discard;
  use action Edit;
  use action Resume;
  use action Prepare;

  field(suppress) DataFieldRoot;

}
```
