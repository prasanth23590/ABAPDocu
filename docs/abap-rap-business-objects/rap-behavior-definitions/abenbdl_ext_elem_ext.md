---
title: "RAP - Extending Elements"
source_file: abenbdl_ext_elem_ext.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - Base BDEF Extension > RAP - extension > RAP - EntityBehaviorExtension > RAP - ExtensionBody"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Extending Elements

## Syntax

``` abap
... 
    extend determine action 
  | extend draft determine action Prepare 
  | extend mapping for PartnerType 
  ...  
```

[`extend determine action`](abenbdl_determine_action_ext.md) · [`extend draft determine action Prepare`](abenbdl_draft_action_ext.md) · [`extend mapping for PartnerType`](abenbdl_type_mapping_ext.md)

## Description

Extends existing components of an existing RAP BO entity in the [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md). As a prerequisite, the respective components must be marked as extensible in the extended BDEF as described in the topic [RAP - Extensibility Enabling for Base BOs](abenbdl_extensibility_enabling_m_u.md). If explicitly enabled for extensibility, the following components can be extended:

- [`extend determine action`](abenbdl_determine_action_ext.md): [Extension](../../abap-glossary/abenrap_prefix_extension_glosry.md) [determinations](../../abap-glossary/abenrap_determination_glosry.md) and extension [validations](../../abap-glossary/abenrap_validation_glosry.md) can be added to an existing [determine action](../../abap-glossary/abenrap_bo_det_action_glosry.md).

  **Limitation:** Currently not supported in unmanaged RAP BOs.

- [`extend draft determine action Prepare`](abenbdl_draft_action_ext.md): Extension determinations and extension validations can be added to an existing draft determine action.

  **Limitation:** Currently not supported in unmanaged RAP BOs.

- [`extend mapping for PartnerType`](abenbdl_type_mapping_ext.md): An existing [RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md) can be extended with extension fields.
