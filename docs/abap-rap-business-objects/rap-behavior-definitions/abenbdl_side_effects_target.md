---
title: "RAP - side effect, Targets"
source_file: abenbdl_side_effects_target.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - side effects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - side effect, Targets

## Syntax

``` abap
... field { MyField 
          | * 
          | _assoc.MyField } 
   | permissions {( field MyField ) 
                 | ( action MyAction ) 
                 | ( _assoc.{field | action} ) 
                 | ( update | delete ) 
                 | ( {create | update | delete} _assoc ) } 
   | $self 
   | entity _MyAssoc 
   | messages  
```

### Variant

[1. `... field ...`](abenbdl_side_effects_target.md#variant-1)

[2. `... permissions ...`](abenbdl_side_effects_target.md#variant-2)

[3. `... $self`](abenbdl_side_effects_target.md#variant-3)

[4. `... entity`](abenbdl_side_effects_target.md#variant-4)

[5. `... messages`](abenbdl_side_effects_target.md#variant-5)

## Overview

### Description

This topic lists the BO properties that can be used as targets `Targets` for [side effects](abenbdl_side_effects.md).

``` abap
One type of side effect can affect multiple targets\. The specifier determining the type of target must be defined explicitly for each target\. Example: 
`side effects { field MyField affects field Field1, field Field2, action Action1, action Action2[, ...]` \}
```

It is possible to group multiple targets using parentheses. For example, the following groupings are possible:

- ` ... affects field(Field1, Field2) ...`

- ` ... affects field _Assoc.(Field1, Field2) ...`

- ` ... affects permissions(field (Field1, Field2)) ...`

- ` ... affects permissions(field Field1, field Field2) ...`

- ` ... affects entity (_Assoc1, _Assoc2) ...`

- ` ... affects entity _Assoc1.(_ItemAssoc1, _ItemAssoc2) ...`

## Variant 1

`... field ...`

### Description

- The specified field `MyField` is reloaded when the side effect is triggered. One or more fields can be specified as side effect target.

- The asterisk `*` reloads all fields of the same entity instance.

- It is also possible to specify fields from other entity instances as targets. They must be defined via an association path `_assoc.MyField`.

- **Limitation:** In case of the trigger property `$self`, the target cannot be a field of the current entity `$self`. However, fields from associated entities can be defined using path expressions.

## Variant 2

`... permissions ...`

### Description

The [feature](../../abap-glossary/abenrap_feature_control_glosry.md) and [authorization control](../../abap-glossary/abenrap_auth_control_glosry.md) of the specified properties are reloaded when the side effect is triggered. The following permissions are available:

- Fields: `permissions(field MyField)`

- Actions: `permissions(field MyField)`

- Update or delete operation: `permissions (update|delete)`

You can also specify permissions for elements and operations of associated entities via association path:

- Fields and actions: `permissions ( _assoc.{field|action} )`

- Operations: `permissions ( {create|update|delete} _assoc )`

Multiple permissions can be listed in parentheses, separated by commas. Example: `permissions(action MyActionFC, update)`.

## Variant 3

`... $self`

### Description

The current RAP BO entity is reloaded.

**Limitation:** In case of the trigger property `$self`, it is not allowed to specify the current entity `$self` as target.

## Variant 4

`... entity`

### Description

The specified associated entity `_MyAssoc` is reloaded when the side effect is triggered.

## Variant 5

`... messages`

### Description

All messages stored in the [response parameter](../../abap-glossary/abenrap_response_param_glosry.md) `reported` are reloaded when the side effect is triggered.
