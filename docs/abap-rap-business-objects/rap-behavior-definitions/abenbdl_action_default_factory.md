---
title: "RAP - Default Factory Action"
source_file: abenbdl_action_default_factory.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - Non-Standard Operations > RAP - action > RAP - action, factory"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Default Factory Action

## Syntax

``` abap
[internal] static default factory action 
                  [( 
                  [features: global] 
                  [precheck] 
                  [authorization:none] 
                  [authorization:global] 
                   )] 
                   ActionName [external 'ExternalName'] 
                  [InputParameter] 
                   [cardinality] 
                  [{default function GetDefaultsForActName [external 'GetDefaultsForExtName'];}]  
```

[`internal`](abenbdl_internal.md) · [`static`](abenbdl_static.md) · [`features: global`](abenbdl_actions_fc.md) · [`precheck`](abenbdl_precheck.md) · [`authorization:none`](abenbdl_actions_auth.md) · [`authorization:global`](abenbdl_actions_auth_global.md) · [`external`](abenbdl_external.md) · [`InputParameter`](abenbdl_action_input_param.md) · [`{default function GetDefaultsForActName [external 'GetDefaultsForExtName'];}`](abenbdl_default_function.md)

## Description

Exactly one static factory action per [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md) can be defined as default static factory action using the syntax addition `default`. The same rules apply as for factory actions, see topic [RAP - `action`, `factory`](abenbdl_action_factory.md).

The addition `default` is evaluated by consuming frameworks, such as OData. These frameworks use the default factory action as standard action in certain scenarios.

Possible [RAP BO operation additions](abenbdl_operations_additions.md) to default factory actions:

- [`internal`](abenbdl_internal.md)

- [`static`](abenbdl_static.md)

- [`features:global`](abenbdl_actions_fc.md)

- [`precheck`](abenbdl_precheck.md)

- [`authorization:none`](abenbdl_actions_auth.md)

- [`authorization:global`](abenbdl_actions_auth_global.md)

- [`external`](abenbdl_external.md)

- [`InputParameter`](abenbdl_action_input_param.md)

- [`default function`](abenbdl_default_function.md)

## Availability

- [Managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- For [projection BOs](../../abap-glossary/abenrap_projection_bo_glosry.md), the following rules apply:

  - The default factory action from the [base BDEF](../../abap-glossary/abenrap_base_bdef_glosry.md) can be reused. For details on reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

  - It is also possible to specify a new default factory action in the projection layer. If the default factory action from the base BO is reused, and at the same time, a new default factory action is defined in the projection BDEF, the default factory from the projection is considered to be the default. It overwrites the default factory action from the base BDEF. Further details on actions and functions in projection BDEFs are described in topic [RAP BDL - Actions and Functions](abenbdl_nonstandard_projection.md).

- In [RAP BO interfaces](../../abap-glossary/abenrap_bo_interface_glosry.md), default factory action from the base BDEF can be reused. For details on reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

## Restriction

The specification of default factory actions in a [BDEF extension](../../abap-glossary/abenrap_extension_glosry.md) is not allowed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF which defines a static default factory action:

``` abap
managed
 implementation in class bp_demo_rap_default_factory_a unique;
strict ( 2 );

define behavior for DEMO_RAP_DEFAULT_FACTORY_A alias Root
persistent table demo_dbtab_root
lock master
authorization master ( none )
{
  create;
  update;
  delete;

  field(readonly:update) key_field;

  static default factory action sdfa [1..*];

  static factory action sfa [0..1];
}
```

The projection BDEF reuses the static default factory action from the base BDEF and specifies a new static default factory action. Consuming frameworks consider the static default factory action from the projection BDEF as default.

``` abap
projection
implementation in class bp_demo_rap_dfa_pv unique;
strict ( 2 );

define behavior for DEMO_RAP_DFA_PV alias RootProjection
{
  use create;
  use update;
  use delete;

  use action sdfa;
  use action sfa;

  static default factory action sdfa_proj [1];
}
```
