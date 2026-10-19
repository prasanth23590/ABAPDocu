---
title: "RAP - extend mapping"
source_file: abenbdl_type_mapping_ext.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - Base BDEF Extension > RAP - extension > RAP - EntityBehaviorExtension > RAP - ExtensionBody > RAP - Extending Elements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - extend mapping

## Syntax

``` abap
... extend mapping for PartnerType    [control ControlType] 
                                      {[corresponding [except Comp1,Comp2, ...]]} 
    { 
      EntityComp1      = PartnerComp1 [control ControlComp]; 
     [EntityComp2      = PartnerComp2 [control ControlComp];] 
     [parameter Param1 = PartnerComp;] 
     [... ;] 
    } 
  | mapping for PartnerType           [control ControlComp] 
                                       corresponding [except Comp1,Comp2, ...]; 
...  
```

## Description

Extends an existing [RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md) with extension fields. The syntax is similar to the syntax for RAP type mapping in original RAP BOs, see the topic [RAP - `TypeMapping`](abenbdl_type_mapping.md). As a prerequisite, the respective type mapping must be explicitly defined as extensible as described in the topic [RAP - Extensibility Enabling for Base BOs](abenbdl_extensibility_enabling_m_u.md).

## Hint

In a BDEF extension, you can either add a new RAP type mapping using the syntax [`mapping for ...`](abenbdl_new_elem_ext.md), or you can extend an existing type mapping from the original behavior definition using the syntax `extend type mapping`. If the partner type is identical, both variants are equivalent. There is no difference between `mapping for PartnerType ...` and `extend mapping for PartnerType ...`
