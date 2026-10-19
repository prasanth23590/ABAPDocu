---
title: "RAP - RedefinedParameter"
source_file: abenbdl_redefine_param.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Projection Behavior Definitions > RAP - EntityBehaviorDefinition, Projection BDEF > RAP - EntityBehaviorBody, Projection BDEF > RAP - use, Projection and Interface BDEF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - RedefinedParameter

## Syntax Forms

**Redefined Input Parameter for RAP Actions and RAP Functions**

``` abap
 ... deep parameter RedefinedAbstractBDEF ...
```

**Redefined Output Parameter for RAP Actions and RAP Functions**

``` abap
... deep result RedefinedAbstractBDEF ...
```

**Redefined Output Parameter for RAP Business Events**

``` abap
 ... deep parameter RedefinedAbstractBDEF ...
```

### Alternative

[1. `... deep parameter RedefinedAbstractBDEF`](abenbdl_redefine_param.md#alternative-1)

[2. `... deep result RedefinedAbstractBDEF`](abenbdl_redefine_param.md#alternative-2)

[3. `... deep parameter RedefinedAbstractBDEF`](abenbdl_redefine_param.md#alternative-3)

## Overview

### Description

Redefines the input parameter or output parameter of a [RAP action](../../abap-glossary/abenrap_action_glosry.md), [RAP function](../../abap-glossary/abenrap_function_glosry.md), or a [RAP business event](../../abap-glossary/abenrap_entity_event_glosry.md) that is reused in a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md) or an [interface BDEF](../../abap-glossary/abencds_interface_bdef_glosry.md).

The redefinition is optional and if not specified, the input and output parameters of the base BDEF are reused.

As a prerequisite for redefining a parameter, the parameter in question must be defined as a deep parameter using the addition `deep` with an [abstract BDEF](../../abap-glossary/abencds_abstract_bdef_glosry.md) in the underlying base BDEF.

The following rules apply to the redefined parameter `RedefinedAbstractBDEF`:

- It must be an abstract behavior definition `with hierarchy`.

- It must be a subset of the data type of the base operation or event. This means that it can have fewer components than the parameter of the base operation and that each component must be compatible or convertible to a component of the base parameter. The [assignment and conversion rules](../../abap-programming-language/abap-processing-internal-data/abenconversion_rules.md) for elementary data objects apply.

- It must define a [type mapping](abenbdl_type_mapping_abstract.md) to the abstract BDEF that is used as a parameter of the base operation or event. The names of the components of the derived type of `RedefinedAbstractBDEF` can differ from the names of the underlying data type.

If a field is defined as [`mandatory:execute`](abenbdl_field_abstract.md) in the abstract BDEF used as a parameter of the base operation, then it must be included in the data type of the redefined parameter and it must be included in the type mapping of the redefined parameter. This rule applies only to action and function parameters. In RAP business events, the field attribute `mandatory:execute` is ignored.

The base parameter and the redefined parameter `RedefinedAbstractBDEF` must either both specify [`with control`](abenbdl_define_beh_abstract.md), or they both must not specify `with control`.

### Hint

If a projection BDEF is based on an interface BDEF, redefining parameters is not possible. Only a parameter from the base BDEF can be changed in an interface BDEF or in a projection BDEF. A projection over an interface cannot change the parameter exposed by the interface.

## More Information

Development guide for the ABAP RESTful Application Programming Model, topic [Modeling Parameters for Non-Standard Operations](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/d891bf474d5444cb939a85d222b75fdf?version=sap_cross_product_abap).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows an interface BDEF based on the managed BDEF `DEMO_RAP_REDEFINE_PARAM`. It reuses an action, two functions, and a RAP business event from the base BDEF and redefines the input and output parameters:

- The base BDEF uses the abstract BDEF `DEMO_RAP_ABSTRACT_ALL_FIELDS` as a parameter.

- The interface BDEF uses the abstract BDEF `DEMO_RAP_ABSTRACT_SUB_FIELDS` as a parameter. This abstract BDEF is a subset of the underlying data type, which means its derived type has one component less than the derived type of the underlying base BDEF.

``` abap
interface;
extensible;

define behavior for DEMO_RAP_REDEFINE_PARAM_I alias Interface
{
  use create;
  use update;
  use delete;

  use action Action1 deep parameter DEMO_RAP_ABSTRACT_SUB_FIELDS ;
  use function Function1 deep result DEMO_RAP_ABSTRACT_SUB_FIELDS;
  use function Function2 deep parameter DEMO_RAP_ABSTRACT_SUB_FIELDS;

  use event Event1 deep parameter DEMO_RAP_ABSTRACT_SUB_FIELDS;
}
```

### Executable Example

The executable example topic [RAP - Reuse with Redefined Parameter](abenbdl_redef_param_abexa.md) explains the example above in detail.

## Alternative 1

`... deep parameter AbstractBDEF ...`

## Prerequisite

Redefining an input parameter is possible under the condition that the base BDEF specifies an abstract BDEF as a deep input parameter for the action or function in question.

### Description

- Redefines the input parameter for a RAP action or a RAP function that is reused in a projection BDEF or interface BDEF.

- The deep input parameter `AbstractBDEF` must be an abstract behavior definition and it must be a subset of the underlying data type of the base operation.

- The deep input parameter `AbstractBDEF` must define a type mapping to the abstract BDEF that is used as a parameter of the base operation.

## Alternative 2

`... deep result AbstractBDEF ...`

## Prerequisite

Redefining an output parameter is possible under the condition that the base BDEF specifies an abstract BDEF as a deep output parameter for the action or function in question.

### Description

- Redefines the output parameter for a RAP action or a RAP function that is reused in a projection BDEF or interface BDEF.

- The deep output parameter `AbstractBDEF` must be an abstract behavior definition and it must be a subset of the underlying data type of the base operation.

- The deep output parameter `AbstractBDEF` must define a type mapping to the abstract BDEF that is used as a parameter of the base operation.

## Alternative 3

`... deep parameter AbstractBDEF ...`

## Prerequisite

Redefining an input parameter is possible under the condition that the base BDEF specifies an abstract BDEF as a deep input parameter for the action or function in question.

### Description

- Redefines the output parameter for a RAP business event that is reused in an interface BDEF.

- The deep output parameter `AbstractBDEF` must be an abstract behavior definition and it must be a subset of the underlying data type of the base operation.

- The deep output parameter `AbstractBDEF` must define a type mapping to the abstract BDEF that is used as a parameter of the base operation.
