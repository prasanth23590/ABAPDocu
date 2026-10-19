---
title: "RAP - authorization, Projection BDEF"
source_file: abenbdl_authorization_projection.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Projection Behavior Definitions > RAP - EntityBehaviorDefinition, Projection BDEF > RAP - EntityBehaviorCharacteristics, Projection BDEF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - authorization, Projection BDEF

## Syntax

``` abap
 ... authorization {( global ) 
                  |( instance ) 
                  |( global,instance )}  ...  
```

## Description

In a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md), the [authorization control](../../abap-glossary/abenrap_auth_control_glosry.md) from the underlying [base BDEF](../../abap-glossary/abenrap_base_bdef_glosry.md) is inherited. This controls [CRUD operations](../../abap-glossary/abencrud_glosry.md), [actions](abenbdl_action.md), and [functions](abenbdl_function.md) that are reused in the projection using the [`use action`](abenbdl_use_projection.md) or [`use function`](abenbdl_use_projection.md) syntax.

Projection BDEFs can also define their own actions and functions as described in the topics [RAP - `action`, Projection BDEF](abenbdl_nonstandard_projection.md) and [RAP - `function`, Projection BDEF](abenbdl_function_projection.md). For these actions and functions, it is possible to configure authorization control in the projection layer. For global authorization, this is done in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR GLOBAL AUTHORIZATION`](../abap-for-rap-business-objects/abaphandler_meth_global_auth.md) in the local [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). For instance authorization, this is done in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR INSTANCE AUTHORIZATION`](../abap-for-rap-business-objects/abaphandler_meth_auth.md) in the local [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md).

Authorization control in projection BDEFs is similar to authorizations in base BDEFs (see topic [RAP - Authorization](abenbdl_authorization.md)). Here are the main differences:

- To define authorization control in a projection BDEF, the projection BDEF must enable [BDEF strict mode](../../abap-glossary/abenrap_strict_mode_glosry.md) using the syntax [`strict[(version)]`](abenbdl_strict.md).

- There is no master/dependent relation. Each projection definition must declare for itself whether it has instance authorization, global authorization, or both.

The authorization control that is defined for a RAP BO entity applies to all RAP BO operations of that entity. The following RAP BO operation additions can be used to control the authorization checks for individual RAP BO operations:

- [`authorization:none`](abenbdl_actions_auth.md) excludes the operation in question from authorization checks. See the topic [RAP - `authorization:none`](abenbdl_actions_auth.md) for further details.

- If [`authorization:update`](abenbdl_actions_auth_update.md) is used, the operation in question has the same authorization control that is defined in the base BDEF for the update operation. As a prerequisite, it is required that the projection BDEF defines authorization control in its entity behavior characteristics. This configuration in the projection BDEF, however, (`instance` or `global`) has no impact, the settings from the base BO (`instance`, `global`, or both) are fully reused. See the second example listed in this topic. See the topic [RAP - `authorization:update`](abenbdl_actions_auth_update.md) for further details.

- [`authorization:global`](abenbdl_actions_auth_global.md) specifies global authorization control for the action in question. If authorization control is also defined at entity level, the specification at action level replaces the specification at entity level. Authorization control at entity level is not a prerequisite though. See the topic [RAP - `authorization:global`](abenbdl_actions_auth_global.md) for further details.

- [`authorization:instance`](abenbdl_actions_auth_instance.md) specifies instance authorization control for the action in question. If authorization control is also defined at entity level, the specification at action level replaces the specification at entity level. Authorization control at entity level is not a prerequisite though. See topic [RAP - `authorization:instance`](abenbdl_actions_auth_instance.md) for further details.

- `authorization:global, authorization:instance` performs both instance authorization control and global authorization control for the action in question.

## Hint

In UI scenarios, authorization control is displayed as [RAP consumer hint](../../abap-glossary/abenrap_consumer_hint_glosry.md).

## More Information

- Development guide for the ABAP RESTful Application Programming Model, topic [Authorization Definition](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/2a26db5640364b46b843dca786c495d1?version=sap_cross_product_abap).
