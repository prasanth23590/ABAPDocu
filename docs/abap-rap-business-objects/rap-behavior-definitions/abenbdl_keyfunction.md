---
title: "RAP - key function"
source_file: abenbdl_keyfunction.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - Non-Standard Operations > RAP - function"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - key function

## Syntax

``` abap
[internal] key (AlternativeKey) function FunctionName 
  [external 'ExternalName'] 
  [result selective [cardinality] $self];  
```

[`internal`](abenbdl_internal.md) · [`external`](abenbdl_external.md)

## Description

A [RAP key function](../../abap-glossary/abenrap_key_function_glosry.md) is a predefined [RAP function](../../abap-glossary/abenrap_function_glosry.md) that is defined for a [BDEF alternative key](../../abap-glossary/abenrap_alternative_key_glosry.md). It receives the values of an alternative key `AlternativeKey` as input and returns the matching [entity instances](../../abap-glossary/abenrap_bo_entity_inst_glosry.md).

In a managed RAP BO, key functions are handled by the [managed RAP BO provider](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md), so that no implementation in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is required. In an unmanaged RAP BO, key functions must be implemented manually in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR READ ... FUNCTION`](../abap-for-rap-business-objects/abaphandler_meth_read.md) in the behavior pool.

The following [RAP BDL operation additions](abenbdl_operations_additions.md) are possible:

- [`internal`](abenbdl_internal.md): An internal key function is accessible only from within the business object implementation.

- [`external`](abenbdl_external.md): Can be used to provide an alias name for the key function for external usage. This external name is exposed in the OData metadata, but it is not known by ABAP. It can be much longer than the actual action name.

- An explicit output parameter is optional. If specified, the syntax for the output parameter is `result selective [cardinality] $self`. The cardinality specification can be `[0..1]`, `[0..*]`, or `[1]`. If no output parameter is specified, the implicit default is `result selective [1] $self`. For further details on output parameters, see [RAP - `OutputParameter`](abenbdl_action_output_para.md).

## Use

Key functions are used, for example, to enable [read-by-association](../../abap-glossary/abenrap_rba_operation_glosry.md) operations in RAP BOs with [cross-BO associations](../../abap-glossary/abencds_cross_bo_assoc_glosry.md) involving RAP reuse objects.

## Availability

- [Managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BOs](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- [Projection BO](../../abap-glossary/abenrap_projection_bo_glosry.md):

  - Key functions from the base BDEF can be reused using the syntax `use function`. For details on reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

  - It is also possible to specify new key functions.

- [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md): Functions from the base BDEF can be reused. For details on the reuse, see the topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF based on the CDS root view entity `DEMO_RAP_PURE_KEY`. It defines a pure key `MyAltKey` which defines the field `char_field` as an alternative key. The key function `GetByAltKey` is defined with reference to `MyAltKey`.

``` abap
managed implementation in class bp_demo_rap_pure_key unique;
strict ( 2 );

define behavior for DEMO_RAP_PURE_KEY alias Root
persistent table demo_dbtab_root
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  field ( readonly ) key_field;

  define pure key MyAltKey { char_field; }

  key ( MyAltKey ) function GetByAltKey;
}
```

The following code snippet first inserts data into the persistent database table and then it executes the key function.

``` abap
*insert data 
DELETE FROM demo_dbtab_root. 
INSERT demo_dbtab_root FROM TABLE @( VALUE #( 
  ( key_field = 1 char_field = 'aaa' ) 
  ( key_field = 2 char_field = 'aaa' ) 
  ( key_field = 3 char_field = 'ccc' ) 
  ( key_field = 4 char_field = 'ddd' ) 
  ( key_field = 5 char_field = 'aaa' ) ) ). 
 
*execute key function 
READ ENTITIES OF demo_rap_pure_key 
ENTITY root 
EXECUTE getbyaltkey FROM VALUE #( 
  ( %cid = '1' %param-char_field = 'aaa' ) ) 
RESULT DATA(result) 
FAILED DATA(failed) 
REPORTED DATA(reported).
```

As a result, all entity instances with the value *aaa* for `char_field` are returned: ![figure](images_keyfunctionresult.png)
