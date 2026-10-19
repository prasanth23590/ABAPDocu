---
title: "RAP - extensible"
source_file: abenbdl_extensible.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - BehaviorDefinitionHeader"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - extensible

## Syntax

``` abap
... 
extensible [{ 
  [with validations on save;] 
  [with determinations on save;] 
  [with determinations on modify;] 
  [with additional save;] 
}] 
 ...  
```

## Description

The addition `extensible` can be used to allow [BDEF extensions](abenbdl_extension.md). If it is not specified, then extensions are not allowed. As a prerequisite, [BDEF strict mode](abenbdl_strict.md) must be switched on.

The keyword `extensible` must be specified in two places:

- It must be declared in the [BDEF header](../../abap-glossary/abencds_bdef_header_glosry.md)

- It must be declared in the [entity behavior characteristics](../../abap-glossary/abencds_entity_properties_glosry.md) for each individual entity that allows BDEF extensions.

In the header declaration, the following optional additions are available:

- `with validations on save`

- `with determinations on save`

- `with determinations on modify`

- `with additional save`

These additions explicitly allow the kinds of [validations](abenbdl_validations.md), [determinations](abenbdl_determinations.md), or a [RAP additional save](../../abap-glossary/abenrap_add_save_glosry.md) in a [RAP entity behavior extension](../../abap-glossary/abenrap_behavior_extension_glosry.md). If not declared explicitly, the respective type of determination, validation, and the additional save must not be defined in an extension to an existing RAP BO entity.

**Note:** This declaration refers only to extensions of existing RAP BO entities ([`extend behavior for`](abenbdl_extend_beh.md)). In extension nodes ([`define behavior for`](abenbdl_define_beh_extend.md)), validations, determinations, and an additional save are always possible and no explicit permission is required.

## Availability

Currently, the keyword `extensible` is available for

- [managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [projection BDEFs](../../abap-glossary/abenrap_projection_bo_glosry.md)

- [interface BDEFs](../../abap-glossary/abencds_interface_bdef_glosry.md)

- [abstract BDEFs](../../abap-glossary/abencds_abstract_bdef_glosry.md)

- [BDEF extensions](../../abap-glossary/abenrap_extension_glosry.md): A BDEF extension itself can be extended with further extensions. This is referred to as [extension layering](../../abap-glossary/abenrap_ext_layering_glosry.md). As a prerequisite, extensions must be explicitly allowed.

In projection BDEFs, interface BDEFs, abstract BDEFs, and BDEF extensions, only the keyword `extensible` is possible, without any further additions.

In interface BDEFs, `extensible` can be specified only in the BDEF header and strict mode is not available.

In BDEF extensions, strict mode is not available.

## More Information

A complete overview of extension points and extensibility enabling for behavior definitions is described in section [Extensibility Enabling](abenbdl_extensibility_enabling.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The RAP behavior definition for `DEMO_RAP_EXTENSIBLE` enables BDEF extensions by specifying multiple extension points.

**Note:** This example is intentionally kept short and simple and serves demonstration purposes only. For example, some [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) of the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) are not implemented here.

``` abap
managed implementation in class bp_demo_rap_extensible unique;
strict(2);
with draft;
extensible
{
  with validations on save;
  with determinations on save;
  with determinations on modify;
  with additional save;
}

define behavior for DEMO_RAP_EXTENSIBLE
persistent table demo_dbtab_root
draft table demo_dbtab_draf1
lock master
total etag Timestamp
authorization master ( global )
extensible
{
  create;
  update;
  delete;

  draft action Edit;
  draft action Activate optimized;
  draft action Discard;
  draft action Resume;
  draft determine action Prepare extensible;

  field(readonly:update) KeyField;
  field(readonly) Timestamp;

  determination setID on save { create; }

  determine action trigger_all extensible
  {
    determination ( always ) setID;
  }

  mapping for demo_dbtab_root corresponding extensible
  {
    KeyField = key_field;
    DataField = data_field;
    Timestamp = crea_date_time;
  }


}
```

The extension `DEMO_RAP_EXTEND1` extends the RAP behavior definition `DEMO_RAP_EXTENSIBLE`.

``` abap
extension implementation in class bp_demo_rap_extend1 unique;

extend behavior for DEMO_RAP_EXTENSIBLE {

 determination MyDet1 on save { create; update; }
 extend determine action trigger_all {determination MyDet1; }
}
```
