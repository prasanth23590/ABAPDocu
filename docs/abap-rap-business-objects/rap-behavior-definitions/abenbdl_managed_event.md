---
title: "RAP - managed event"
source_file: abenbdl_managed_event.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - Events"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - managed event

## Syntax

``` abap
managed event DerivedEventName on RefEvent parameter ViewEntityName;  
```

## Description

Defines a [RAP derived event](../../abap-glossary/abenrap_derived_event_glosry.md) `DerivedEventName` in a [managed](../../abap-glossary/abenmanaged_rap_bo_glosry.md) or [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md). A derived event is defined with reference to an already implemented event `RefEvent` and allows the definition of a [payload](../../abap-glossary/abenpayload_glosry.md) that deviates from the payload of the referenced event. When the referenced event is raised, the derived event is raised as well with its custom payload. No implementation in an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is required for the derived event.

- The name `DerivedEventName` defines the name of the derived event. It must comply with the naming rules for CDS BDL that are described in the topic [RAP BDL - General Syntax Rules](abenbdl_general_syntax_rules.md).

- After the keyword `ON`, the referenced event `RefEvent` is specified. The referenced event must be an event from the current behavior definition. In case of an extension, the referenced event must be specified in the original BDEF that is currently being extended.

- An [input parameter](../../abap-glossary/abeninput_parameter_glosry.md) `ViewEntityName` must be defined. It redefines the payload of the event `RefEvent`. The following rules apply:

  - The input parameter `ViewEntityName` must be a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) without any associations.

  - The key fields of the view entity used as the input parameter `ViewEntityName` must match the key fields of the entity the referenced event is defined for.

    **Note:** The input parameter of a derived event is always flat. Deep structures or view entities with associations are not supported.

## Availability

- RAP derived events can be defined in [managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md) and in [unmanaged RAP BOs](../../abap-glossary/abenunmanaged_rap_bo_glosry.md).

## Hint

The payload of a managed event is defined using a CDS view entity. By default, the [RAP framework](../../abap-glossary/abenrap_framework_glosry.md) accesses this view entity with [`PRIVILEGED`](../abap-for-rap-business-objects/abapeml_privileged.md) access rights. This means that no authorization checks are performed when reading the payload data.

## More Information

Development guide for the ABAP RESTful Application Programming Model, section about [Derived Events](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/c081abb9243045d098197321213fde29?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows an unmanaged BDEF based on the CDS root view entity `DEMO_RAP_DERIVED_EVENT`. It defines the event `MyEvent`.

``` abap
unmanaged implementation in class bp_demo_rap_derived_event unique;
strict ( 2 );
extensible;

define behavior for DEMO_RAP_DERIVED_EVENT

lock master
authorization master ( none )
extensible
{
  create;
  update;
  delete;

  field ( readonly : update ) keyfield;

  event MyEvent;
}
```

The following CDS view entity is used as an input parameter of the derived event. Its key fields match the key fields of the root view entity `DEMO_RAP_DERIVED_EVENT`.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, demo for derived event'
define root view entity DEMO_RAP_DERIVED_EVENT_PARAM
  as select from demo_dbtab_root
{
  key key_field    as KeyField,
      data_field   as DataField
}
```

The following BDEF extension redefines the event `MyEvent` from the base BDEF. The derived event has the name `MyDerivedEvent`.

``` abap
extension using interface DEMO_RAP_DERIVED_EVENT_PV;

extend behavior for RootInterface
{

  managed event MyDerivedEvent on MyEvent
    parameter DEMO_RAP_DERIVED_EVENT_PARAM;
}
```
