---
title: "RAP - auxiliary class"
source_file: abenbdl_auxiliary_class.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - BehaviorDefinitionHeader"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - auxiliary class

## Syntax

``` abap
... auxiliary class ClassName1 [,ClassName2][,ClassName3] [, ...];  
```

## Description

Specifies additional [ABP auxiliary classes](../../abap-glossary/abenabp_aux_class_glosry.md) `ClassName1`, `ClassName2`, ... with enhanced access rights to the referenced RAP BO. The primary purpose of an ABP auxiliary class is to support implementation in an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). This is accomplished by providing reusable methods and allowing developers to concurrently implement [RAP behavior](../../abap-glossary/abenrap_behavior_glosry.md).

An auxiliary class refers to exactly one RAP BO and it has enhanced access rights to this RAP BO, for example, it can access the RAP BO in question using the ABAP EML statement [`IN LOCAL MODE`](../abap-for-rap-business-objects/abapin_local_mode.md). This makes it possible to implement reusable methods for an ABP, to outsource functionality, and to facilitate concurrent work. For details on the implementation of an ABP auxiliary class, see the topic [ABP Auxiliary Class](../abap-for-rap-business-objects/abaprap_auxiliary_class.md).

The auxiliary classes `ClassName1`, `ClassName2`, ... cannot be named after [`implementation in class ClassName unique`](abenbdl_in_class_unique.md), this means, the auxiliary classes and the ABAP behavior pool are separate classes. Each auxiliary class can be specified exactly once in a RAP BO. An auxiliary class refers to exactly one RAP BO and it must not be reused in different RAP BOs.

As a prerequisite for specifying the auxiliary class, [BDEF strict mode](../../abap-glossary/abenrap_strict_mode_glosry.md) must be switched on using the syntax `strict(version)`.

## Availability

- [Managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BOs](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- The syntax `auxiliary class` is not available in any other [BDEF implementation type](../../abap-glossary/abencds_bdef_impl_type_glosry.md) and it is not available in [BDEF extensions](../../abap-glossary/abenrap_extension_glosry.md).

## Hint

Another way to divide the implementation-relevant parts of a [RAP behavior implementation](../../abap-glossary/abenbehavior_implement_glosry.md) is by using implementation groups, defined using the syntax [`group`](abenbdl_grouping.md). The difference is that implementation groups can implement [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) and [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md), so that the implementation can be distributed to different implementation classes. Auxiliary classes, on the other hand, cannot implement any [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) and [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md). They have enhanced access rights to the RAP BO they refer to and they can implement functionality that can be called from the ABAP behavior pool of the respective RAP BO. In other words, an auxiliary class can be used to outsource functionality from an ABAP behavior pool. For further details on implementation grouping, see the topic [RAP - `group`](abenbdl_grouping.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_AUX_M` specifies an auxiliary class:

``` abap
managed implementation in class bp_demo_aux_m unique;
strict ( 2 );
auxiliary class cl_demo_rap_abp_aux_cl;

define behavior for demo_aux_m
persistent table demo_tab_root_8
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  field ( readonly:update ) key_field;
  action div;
  action multiply;
  action powers;
}
```

## More Information

[ABP Auxiliary Class](../abap-for-rap-business-objects/abaprap_auxiliary_class.md)

## Executable Example

[ABP Auxiliary Class](../abap-for-rap-business-objects/abenabp_aux_cl_abexa.md)
