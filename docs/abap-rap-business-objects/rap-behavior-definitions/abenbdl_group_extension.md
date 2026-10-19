---
title: "RAP - group, Extension"
source_file: abenbdl_group_extension.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - Base BDEF Extension > RAP - extension > RAP - EntityBehaviorExtension"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - group, Extension

## Syntax

``` abap
... 
group Group1 implementation in class Class1 unique 
{ 
  // implementation-relevant content 
} 
 
group Group2 implementation in class Class2 unique 
{ 
  //implementation-relevant content 
} 
 
[group Group3 ...] 
...  
```

[`implementation in class Class1 unique`](abenbdl_in_class_unique_ext.md) · [`implementation in class Class2 unique`](abenbdl_in_class_unique_ext.md)

## Description

Grouping divides the implementation-relevant parts of a [business object's](../../abap-glossary/abenrap_bo_glosry.md) business logic into multiple groups for behavior implementation. Each group is assigned to a separate [implementation class](abenbdl_in_class_unique_ext.md). This works for BDEF extensions in the same way as for RAP BOs, see the topic [RAP - `group`](abenbdl_grouping.md).

The original BDEF may divide the implementation into multiple groups, and the extension can add further groups. An individual group from the original BDEF cannot be extended.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The BDEF extension `DEMO_RAP_EXTENSION_GROUP` extends the RAP behavior definition `DEMO_RAP_BASE_GROUP`. It divides the implementation-relevant content into two groups.

Original BDEF: explicitly allows extensions

``` abap
managed implementation in class bp_demo_rap_base_group unique;
strict ( 2 );
extensible
{ with determinations on modify;
  with determinations on save;
  with validations on save; }

define behavior for DEMO_RAP_BASE_GROUP
persistent table demo_dbtab_root
lock master
authorization master ( instance, global )
extensible
{
  field ( readonly : update ) key_field;
  group demo_a implementation in class cl_group_demo_a unique
  {
    create;
    update;
    delete;
  }

  group demo_b implementation in class cl_group_demo_b unique
  {
    field ( features : instance ) char_field;
  }

  group demo_c implementation in class cl_group_demo_c unique
  {
    determination DemoDet on save { create; }
  }
}
```

BDEF interface:

``` abap
interface;
extensible;

define behavior for DEMO_RAP_I_GROUP alias Root
{
  use create;
  use update;
  use delete;
}
```

Extension BDEF: defines two groups with separate ABPs.

``` abap
extension using interface DEMO_RAP_I_GROUP
  implementation in class bp_demo_rap_extension_group unique;

extend behavior for Root
{
  group demo_ext_a implementation in class cl_demo_ext_a unique
  {
    validation DemoValidation on save { field data_field; }
    action (authorization:none) DemoAction result [1] $self;
    action ( features : instance, authorization:none )
    DemoAction1 result [1] $self;
  }
  group demo_ext_b implementation in class cl_demo_ext_b unique
  {
    validation DemoValidation2 on save { field dec_field; }
    action (authorization:none) DemoAction2 result [1] $self;
    action ( features : instance, authorization:none )
    DemoAction1b result [1] $self;
  }
}
```
