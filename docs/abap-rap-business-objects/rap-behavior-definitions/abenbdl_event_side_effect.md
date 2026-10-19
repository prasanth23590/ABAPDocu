---
title: "RAP - event for side effects"
source_file: abenbdl_event_side_effect.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - Events"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - event for side effects

## Syntax

``` abap
event EventName for side effects;  
```

## Description

Defines a [RAP business event for side effects](../../abap-glossary/abenrap_side_effct_event_glosry.md) used exclusively for an [event-driven side effect](../../abap-glossary/abenrap_event_sideef_glosry.md) in a [managed](../../abap-glossary/abenmanaged_rap_bo_glosry.md) or [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md).

A RAP business event must be raised in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) of the RAP BO in question with the [ABAP EML](../../abap-glossary/abenabap_eml_glosry.md) statement [`RAISE ENTITY EVENT`](../abap-for-rap-business-objects/abapraise_entity_event.md) in the [RAP late save phase](../../abap-glossary/abenlate_rap_save_phase_glosry.md). In managed RAP BOs, it is recommended that a [RAP additional save](../../abap-glossary/abenrap_add_save_glosry.md) is specified using the syntax addition [`with additional save`](abenbdl_saving.md) and raise the RAP business event in this additional save implementation.

## Availability

- RAP business events for side effects can be defined in [managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md) and in [unmanaged RAP BOs](../../abap-glossary/abenunmanaged_rap_bo_glosry.md).

- RAP business events for side effects can be reused in [RAP interface behavior definitions](../../abap-glossary/abencds_interface_bdef_glosry.md) and in [RAP projection behavior definitions](../../abap-glossary/abencds_proj_bdef_glosry.md) using the keyword [`use event`](abenbdl_use_projection.md).

## More Information

- Development guide for the ABAP RESTful Application Programming Model, section about [Event-Driven Side Effects](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/35e99dd3b0694d1ebbac3c865dd72d3a?version=sap_cross_product_abap).

- [RAP - `side effects`](abenbdl_side_effects.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF based on the CDS root view entity `DEMO_RAP_SIDE_EFFECT_EVENT`. The business event for side effects is defined with the syntax `event MyEvent for side effects`.

``` abap
managed with additional save
implementation in class bp_demo_rap_side_effect_event unique;
strict ( 2 );

define behavior for DEMO_RAP_SIDE_EFFECT_EVENT alias Root
persistent table demo_dbtab_root
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  field ( readonly ) key_field;

  event myEvent for side effects;

  side effects
  {
    event MyEvent affects field char_field;
  }
}
```
