---
title: "RAP - side effects"
source_file: abenbdl_side_effects.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - side effects

## Syntax

``` abap
side effects { field MyField affects Targets; } 
           | { $self affects Targets; } 
           | { action MyAction affects Targets; } 
           | { determine action MyDetermineAction 
               executed on Sources 
               affects Targets; } 
           | { event MyEvent affects Targets; } 
           | { recommendation function MyRecommendationFunction executed on Sources; }  
```

[`Targets`](abenbdl_side_effects_target.md) · [`Targets`](abenbdl_side_effects_target.md) · [`Targets`](abenbdl_side_effects_target.md) · [`Targets`](abenbdl_side_effects_target.md) · [`Targets`](abenbdl_side_effects_target.md)

### Variant

[1. `... field MyField affects Targets`](abenbdl_side_effects.md#variant-1)

[2. `... $self affects Targets`](abenbdl_side_effects.md#variant-2)

[3. `... action MyAction affects Targets`](abenbdl_side_effects.md#variant-3)

[4. `... determine action MyDetermineAction ...`](abenbdl_side_effects.md#variant-4)

[5. ... event MyEvent affects Targets](abenbdl_side_effects.md#variant-5)

[6. `... recommendation function MyRecommendationFunction executed on Sources ...`](abenbdl_side_effects.md#variant-6)

## Overview

### Description

Defines [RAP side effects](../../abap-glossary/abenrap_side_effects_glosry.md) in the [entity behavior body](../../abap-glossary/abencds_entity_body_glosry.md) of a RAP BO. RAP side effects are an optional part of a RAP behavior definition that define interdependencies among BO properties that trigger a reload of the affected properties on the user interface. Side effects are translated into annotations in the OData metadata of a RAP service. An implementation in an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is not required.

The following trigger properties are possible:

- Field `field MyField` as trigger

  Whenever a defined field is changed on the user interface, the side effect is triggered and the defined targets [`Targets`](abenbdl_side_effects_target.md) are reloaded.

- `$self`

  Whenever the current [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md) is modified using a [CUD operation](../../abap-glossary/abencud_glosry.md), the side effect is triggered and the defined targets [`Targets`](abenbdl_side_effects_target.md) are reloaded.

- Action `action MyAction` as trigger

  Whenever the action is executed on the user interface, the side effect is triggered and the defined targets [`Targets`](abenbdl_side_effects_target.md) are reloaded.

- Side effect that triggers a determine action `determine action MyDetermineAction`

  Whenever the defined source `Sources` is changed, the determine action is triggered and the defined [targets](abenbdl_side_effects_target.md) are reloaded.

- Event `event MyEvent` as trigger

  Whenever a defined event is changed on the user interface, the side effect is triggered and the defined targets [`Targets`](abenbdl_side_effects_target.md) are reloaded.

- Side effect that triggers a [recommendation function](abenbdl_recommendations.md) `MyRecommendationFunction`

  Whenever a defined field or entity has been changed on the user interface, the side effect is triggered, the recommendation function is called, and the defined targets are reloaded. Targets are fields for which [RAP recommendation](../../abap-glossary/abenrecommendation_glosry.md) are displayed.

The RAP BO properties that can be specified as target [`Targets`](abenbdl_side_effects_target.md) of a side effect are described in [RAP - `side effect`, `Targets`](abenbdl_side_effects_target.md), except for recommendation functions. Targets of side effects with recommendation functions are described in [RAP - `FieldCharacteristics`](abenbdl_field_char.md).

The syntax `side effects` can be specified exactly once for each RAP BO entity in the [entity behavior definition](../../abap-glossary/abencds_entity_bdef_glosry.md). Multiple side effects can be summarized within curly brackets, separated by a semicolon (`;`), if required.

## Restriction

[Static](../../abap-glossary/abenrap_static_operation_glosry.md) actions defined using the addition [`static`](abenbdl_action.md) must not be used as a side effect trigger, nor as a side effect target.

## Availability

- [Managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BOs](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- [Projection BDEFs](../../abap-glossary/abencds_proj_bdef_glosry.md)

- In a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md) and in a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md), side effects from the [base BO](../../abap-glossary/abenrap_projected_bo_glosry.md) can be reused. For details on reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

  **Note:** In projection BDEFs, RAP side effects from the base BDEF can be reused or new side effects can be defined. In an interface BDEF, on the other hand, only reuse is possible.

### Hint

RAP side effects are useful in UI scenarios based on draft-enabled RAP BOs to make a Fiori Elements UI aware that data changes of defined fields require the recalculation of other data values, permissions, or messages. In these cases, side effects contribute to data consistency on the UI.

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [*Side Effects*](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/b30b48c58ed94ff786980ab9aa18882f?version=sap_cross_product_abap).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF that defines five different side effects with different trigger properties and targets. They are summarized in curly brackets after the statement `side effects`.

``` abap
managed implementation in class bp_demo_rap_side_effects unique;
strict ( 2 );
with draft;

define behavior for DEMO_RAP_SIDE_EFFECTS alias Root
persistent table demo_dbtab_root
draft table demo_dbtab_dr1
lock master
total etag lchg_date_time
authorization master ( none )
{
  create;
  update;
  delete;

  field ( readonly : update ) key_field;
  field ( readonly ) lchg_date_time;
  field(features:instance) crea_date_time;

  action(features:instance) MyActionFC;

  action MyAction;

  determine action someDetermineAction;

  draft action ( features : instance ) Edit;
  draft action Activate optimized;
  draft action Discard;
  draft action Resume;
  draft determine action Prepare;

  side effects {

    // Side effect with single source property
    field char_field affects field char_field_2;

    // Side effect with multiple source properties and trigger action
    determine action someDetermineAction
    // trigger field group
      executed on field dec_field,
                  field char_field,
                  field _Assoc.data_field
      affects field data_field;

    // Side effect that triggers the reload of feature control
    field data_field affects permissions(field crea_date_time);

    // Side effect on an action with operation control and messages
    action MyActionFC affects field *,
                      permissions(action MyActionFC),
                      messages;

    // Side effect for refreshing data of an entity
    action MyAction affects field char_field, entity _Assoc;

  }
}
```

## Variant 1

`... field MyField affects Targets`

### Description

Defines a side effect for the field `MyField`. Whenever the field `MyField` is changed on the user interface, the side effect is triggered and the defined targets [`Targets`](abenbdl_side_effects_target.md) are reloaded. Exactly one field must be specified as trigger property. Multiple properties `Targets` can be specified after the syntax `affects`.

## Variant 2

`... $self affects Targets`

### Description

Defines a side effect for the current RAP BO entity. Whenever the current RAP BO entity is modified using a CUD operation, the side effect is triggered and the defined targets [`Targets`](abenbdl_side_effects_target.md) are reloaded. Multiple properties `Targets` can be specified after the syntax `affects`.

**Limitation:** In case of the trigger property `$self`, the following limitations apply to the targets that can be specified:

- No fields of the current entity `$self` can be specified. However, fields from associated entities can be defined using path expressions.

- The current entity `$self` cannot be specified as target.

## Variant 3

`... action MyAction affects Targets`

### Description

Defines a side effect for the action `MyAction`. Whenever the action `MyAction` is executed on the user interface, the side effect is triggered and the defined targets [`Targets`](abenbdl_side_effects_target.md) are reloaded. Exactly one action must be specified as trigger property. Multiple properties `Targets` can be specified after the syntax `affects`.

## Variant 4

`... determine action MyDetermineAction ...`

### Description

Defines a side effect that triggers the determine action `MyDetermineAction`. Whenever one of the defined sources `Sources` is changed, the determine action is executed and the defined targets [`Targets`](abenbdl_side_effects_target.md) are reloaded.

One or more sources `Sources` can be specified after the syntax `executed on`. The following BO properties can be used as sources `Sources`:

- `field MyField`:

  - The determine action is triggered whenever the field `MyField` is changed. You can specify one or more fields as the trigger for a determine action.

  - **Note:** By using more than one field as source for the determine action side effect, the fields are implicitly considered as a field group. The side effect is only triggered if the cursor is set outside of the group of source fields after changing at least one of them.

  - You can also use fields from other entity instances as sources. They must be defined via an association path: `_assoc.MyField`.

- `$self`:

  - The determine action is triggered whenever anything on its own entity instance is changed (such as fields, create child, delete child).

- `entity _Assoc`:

  - The determine action is triggered whenever anything on the specified entity `_Assoc` is changed (fields, create, delete).

- `global`:

  - The determine action is triggered whenever the user requests a global refresh by pressing Enter on any input field. You can define `global` only once per side effect.

    Example: `side effects { determine action MyDetermineAction executed on global affects field MyField; }`

It is possible to group multiple `sources` using parentheses. The following groupings are possible:

- ` ... executed on field(Field1, Field2) ...`

- ` ... executed on field _Assoc.(Field1, Field2) ...`

Multiple properties `Targets` can be specified after the syntax `affects`.

## Variant 5

`... event MyEvent affects Targets`

### Description

Defines a [business event for side effects](../../abap-glossary/abenrap_side_effct_event_glosry.md) event `MyEvent` for a [event-driven side effect](../../abap-glossary/abenrap_event_sideef_glosry.md). Whenever the defined event `MyEvent` is raised by the application server, a side effect is triggered and the defined targets [`Targets`](abenbdl_side_effects_target.md) are reloaded. Exactly one event must be specified as trigger property. Multiple properties `Targets` can be specified after the syntax `affects`. For more information on event-driven side effect, see the development guide for the ABAP RESTful Application Programming Model, section [Event-Driven Side Effect](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/35e99dd3b0694d1ebbac3c865dd72d3a?version=sap_cross_product_abap).

## Variant 6

`... recommendation function MyRecommendationFunction executed on Sources ...`

### Description

Defines a side effect that triggers the [recommendation function](abenbdl_recommendations.md) `MyRecommendationFunction`. Whenever one of the defined sources `Sources` has been changed, the recommendation function is executed, and recommendation target fields are reloaded. After the reload, [RAP recommendations](../../abap-glossary/abenrecommendation_glosry.md) that the recommendation function calculated are displayed.

One or more sources `Sources` can be specified after the syntax `executed on`. The following BO properties can be used as sources:

- field `myField`:

  - The recommendation function is triggered whenever the field `MyField` has been changed. You can specify one or more fields as the trigger for a recommendation function.

  - The side effect is only triggered if the cursor is set outside a source field after the field has been changed.

  - You can also use fields from other entity instances as sources. Define them using an association path: `_assoc.MyField`.

- `$self`:

  - The recommendation function is triggered whenever anything on its own entity instance has been changed (such as fields, create child, delete child).

- entity `_Assoc`:

  - The recommendation function is triggered whenever anything on the specified entity `_Assoc` has been changed (fields, create, delete).

You can group multiple fields as sources using parentheses. The following groupings are possible:

- `... executed on field(Field1, Field2) ...`

- `... executed on field _Assoc.(Field1, Field2) ...`

### Hint

Only fields are possible as targets of the side effects for the recommendation function. You must define these fields in the behavior definition using the syntax [`field(recommendations ) Field1, Field2, ...`](abenbdl_field_char.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [*Adding RAP Recommendations*](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/9d9cc97cab9d48fdaa35d5c333526ba0)
