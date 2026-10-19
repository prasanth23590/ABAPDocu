---
title: "RAP - Extensibility Enabling for RAP BO Interfaces"
source_file: abenbdl_extensibility_enablng_intf.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - BDEF Extension, Extensibility Enabling"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Extensibility Enabling for RAP BO Interfaces

## Syntax

``` abap
interface 
[...] 
extensible 
{ entity behavior definition } 
...  
```

[`interface`](abenbdl_bo_interface_header.md) · [`extensible`](abenbdl_extensible.md) · [`entity behavior definition`](abenbdl_define_beh_interface.md)

## Description

In a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md), the keyword `extensible` can be specified in the BDEF header to allow for [BDEF extensions](../../abap-glossary/abenrap_extension_glosry.md). This specification includes all RAP BO entities and components that are included in the interface.

A RAP BO interface cannot be extended directly, but extensions always refer to the underlying base BO. The base BO refers to the RAP BO interface with the addition [`using interface`](abenbdl_using_interface.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The RAP BO interface `DEMO_RAP_EXT_DET_ACT_INT` is declared as `extensible`.

``` abap
interface;
use draft;
extensible;
use side effects;

define behavior for DEMO_RAP_EXT_DET_ACT_INT alias Root
{
  use create;
  use update;
  use delete;

  use action trigger_all;

  use action Activate;
  use action Discard;
  use action Edit;
  use action Resume;
  use action Prepare;

  use association _child { create; with draft; }
}

define behavior for DEMO_RAP_EXT_DET_ACT_INT_CH alias Child
{
  use update;
  use delete;

  use association _parent { with draft; }
}
```

It can now be used for base BDEF extensions with the addition [`using interface`](abenbdl_using_interface.md).
