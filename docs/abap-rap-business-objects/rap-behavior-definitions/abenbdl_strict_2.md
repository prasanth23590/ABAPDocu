---
title: "RAP - strict(2)"
source_file: abenbdl_strict_2.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - BehaviorDefinitionHeader > RAP - BDEF Strict Mode"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - strict(2)

``` abap
`... 
strict(2); 
 ...`
```

## Description

The addition `strict(2)` enables [BDEF strict mode](../../abap-glossary/abenrap_strict_mode_glosry.md), version 2. When strict mode is switched on, outdated syntax which normally produces a syntax check warning leads to a syntax check error. Strict mode version 2 introduces mainly stricter checks for the [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). Contract violations lead to [runtime errors](../../abap-glossary/abenruntime_error_glosry.md), instead of failed [assertions](../../abap-glossary/abenassertion_glosry.md). Strict mode version 2 is a prerequisite for releasing a RAP BO under the [C0 contract for extensibility](../../abap-glossary/abenc0_contract_glosry.md).

Strict mode version 2 must always appear as the second line in a [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md).

Strict mode version 2 applies all checks from strict mode version 1, plus some additional syntax checks.

A complete list of additional syntax requirements in BDEF strict mode version 2 is provided in the development guide for the ABAP RESTful Application Programming Model, section [Strict Mode - Implementation Requirements](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/761d389302e8463a9c3509907f22f22f?version=sap_cross_product_abap).

Related information:

[RAP BDL - BDEF Strict Mode](abenbdl_strict.md)

[RAP BDL - `strict`](abenbdl_strict_1.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following RAP behavior definition `DEMO_RAP_BASE_DET_VAL` is based on the CDS view entity `DEMO_RAP_BASE_DET_VAL`. It is intended to be released as API for extensibility under the C0 contract. Therefore, it uses `strict(2)`.

**Note:** This RAP behavior definition demonstrates the design of a released API, but it is not actually released for C0.

**Note:** This example is intentionally kept short and simple and serves demonstration purposes only. The [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) of the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) are not implemented here.

``` abap
managed implementation in class bp_demo_rap_base_det_val unique;
strict ( 2 );
extensible
{ with determinations on modify;
  with determinations on save;
  with validations on save; }

define behavior for DEMO_RAP_BASE_DET_VAL
persistent table demo_dbtab_root
lock master
authorization master ( none )
extensible
{
  create;
  update;
  delete;
  field ( readonly : update ) key_field;
}
```
