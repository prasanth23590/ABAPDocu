---
title: "RAP - BDEF Strict Mode"
source_file: abenbdl_strict.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - BehaviorDefinitionHeader"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - BDEF Strict Mode

## Syntax

``` abap
... strict; 
  | strict(2);  
```

## Description

[BDEF strict mode](../../abap-glossary/abenrap_strict_mode_glosry.md) applies additional syntax checks to [RAP behavior definitions](../../abap-glossary/abencds_behavior_definition_glosry.md). It ensures, for example, that no outdated syntax is used, implicitly available operations are declared explicitly, and the RAP BO in question complies to best practices. BDEF strict mode is provided by the [RAP framework](../../abap-glossary/abenrap_framework_glosry.md), no implementation in an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is required.

Currently, the following versions of strict mode are available:

- Strict mode version 1, specified using [`strict`](abenbdl_strict_1.md)

- Strict mode version 2, specified using [`strict(2)`](abenbdl_strict_2.md)

Strict mode version 2 covers all rules from strict mode version 1, plus some additional checks.

It is recommended that the most recent version of strict mode is used. In some scenarios, strict mode is even mandatory, for example when declaring a RAP BO as [`extensible`](abenbdl_extensible.md) or when releasing a BDEF as [released API](../../abap-glossary/abenreleased_api_glosry.md).

This documentation handles all statements according to the requirements of BDEF strict mode.

## Availability

BDEF strict mode is available for RAP behavior definitions of the following [BDEF implementation types](../../abap-glossary/abencds_bdef_impl_type_glosry.md):

- [`managed`](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [`unmanaged`](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- [`projection`](../../abap-glossary/abencds_proj_bdef_glosry.md): To use BDEF strict mode in a RAP projection behavior definition, the base BDEF must use strict mode as a prerequisite. Base and projection must use the same version of strict mode.

- [`abstract`](../../abap-glossary/abencds_abstract_bdef_glosry.md)

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [Strict Mode](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/cbb86e63a8464e63bbdd43b7bfa5fc4f?version=sap_cross_product_abap).
