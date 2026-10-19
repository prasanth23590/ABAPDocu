---
title: "RAP - use DefaultValuesFunction"
source_file: abenbdl_use_default_function.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Projection Behavior Definitions > RAP - EntityBehaviorDefinition, Projection BDEF > RAP - EntityBehaviorBody, Projection BDEF > RAP - use, Projection and Interface BDEF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - use DefaultValuesFunction

## Syntax

``` abap
 ... use function DefaultValuesFunction;  
```

## Description

Reuses a [RAP default values function](../../abap-glossary/abenrap_bo_defaulting_glosry.md) in a projection BDEF or in an interface BDEF. Both the operation in question and the default values function must be reused separately:

- The operation for which a default values function is defined is reused as described in the topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

- The default values function is reused using the syntax `use function DefaultValuesFunction`. No further additions are possible.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following projection BDEF is based on the managed BDEF `DEMO_RAP_DEFAULT_VALUES_FUNC`. It reuses multiple default values functions from the base BDEF.

``` abap
projection;
strict ( 2 );

define behavior for DEMO_RAP_DEFAULT_VALUES_C alias Root
{

//reuse of create + default values function for create
  use create;
  use function GetDefaultsForCreate;

  //reuse of action + default values function for the action
  use action InstanceAction;
  use function GetDefaultsForAction;


  //reuse of function + default values function for the function
  use function StaticFunction;
  use function GetDefaultsForStaticFunction;

  //reuse of association + default values function
  //for create-by-association
  use association _to_child { create; }
  use function GetDefaultsForChild;
}

define behavior for DEMO_RAP_DEFAULT_VALUES_CHLD_C alias Child
{
  use update;
  use delete;

  use association _to_parent;
}
```
