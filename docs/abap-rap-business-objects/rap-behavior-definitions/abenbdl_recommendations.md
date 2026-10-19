---
title: "RAP - recommendation function"
source_file: abenbdl_recommendations.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - recommendation function

## Syntax

``` abap
recommendation function MyRecommendationFunction;  
```

## Description

Recommendation functions calculate [RAP recommendations](../../abap-glossary/abenrecommendation_glosry.md), which provide input assistance on the SAP Fiori UI based on the user input and interaction history.

The name `MyRecommendationFunction` must comply with the general naming rules for RAP behavior definitions described in [RAP BDL - General Syntax Rules](abenbdl_general_syntax_rules.md). The function name can have a maximum of 30 characters.

The result of the recommendation function is displayed as recommended values in recommendation target fields on the UI. A recommendation target field is defined using the syntax `field(recommendations)`.

Only one recommendation function is possible for each behavior definition.

**Trigger Conditions**

A recommendation function is triggered by [RAP side effects](../../abap-glossary/abenrap_side_effects_glosry.md). By adding a side effect definition, the trigger of the recommendation function is defined separately from the recommendation function itself. Whenever a recommendation function is executed, the target fields of the RAP recommendation are reloaded and recommended values are shown on the UI.

## Availability

- [Managed](../../abap-glossary/abenmanaged_rap_bo_glosry.md) [draft-enabled](../../abap-glossary/abendraft_rap_bo_glosry.md) RAP BOs

- [Unmanaged](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) draft-enabled RAP BOs

- For a RAP recommendation to work, RAP recommendations and related side effects from the base BDEF must be reused in a [RAP projection BO](../../abap-glossary/abencds_proj_bdef_glosry.md) using the syntax `use recommendations`. For more information about reuse, see [RAP - use, Projection and Interface BDEF](abenbdl_use_projection.md).

## More Information

[*Adding RAP Recommendations*](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/9d9cc97cab9d48fdaa35d5c333526ba0) in the development guide for the ABAP RESTful Application Programming Model.
