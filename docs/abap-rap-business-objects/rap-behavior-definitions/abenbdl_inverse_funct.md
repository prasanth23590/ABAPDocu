---
title: "RAP - Inverse Function"
source_file: abenbdl_inverse_funct.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - Operations for Associations > RAP - NonstandardOperationsForAssoc"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Inverse Function

## Syntax

``` abap
...{ 
        [internal] 
        inverse function FunctionName 
        [result selective [cardinality] $self]; 
   }  
```

[`internal`](abenbdl_internal.md)

## Description

An inverse function is a static function that can be defined for a [foreign key association](../../abap-glossary/abenforeign_key_assoc_glosry.md). For a given value of the foreign key of that association, the inverse function returns all instances of the [association source](../../abap-glossary/abenassociation_source_glosry.md) entity where the supplied value of the foreign key matches.

Like any static function, you can use the inverse function as a standalone [EML](../../abap-glossary/abeneml_glosry.md) operation. However, its main use case lies in enabling a managed [read by association](../../abap-glossary/abenrap_rba_operation_glosry.md) of a [target-resolved](../../abap-glossary/abentarget_resolved_assoc_glosry.md) [cross-BO association](../../abap-glossary/abencds_cross_bo_assoc_glosry.md).

An explicit output parameter is optional. If specified, the syntax for the output parameter is `result selective [cardinality] $self`. The cardinality specification can be `[0..1]`, `[0..*]`, or `[1]`. If no output parameter is specified, the implicit default is `result selective [1] $self`. For further details on output parameters, see [RAP - `OutputParameter`](abenbdl_action_output_para.md).

The link and unlink actions are handled by the managed RAP BO provider. No implementation in an ABAP behavior pool is required.

**RAP BDL Operation Additions**

The following [RAP BDL operation additions](abenbdl_operations_additions.md) are possible:

- [internal](abenbdl_internal.md) to make the respective action accessible only from within the business object implementation.

## Availability

- Managed RAP BO: In a [managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md), the link and unlink actions do not require an [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md), since they are completely handled by the managed RAP BO provider, unless the association is unmanaged.

- Unmanaged RAP BO: In an [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md), the link and unlink actions must be implemented in the ABAP behavior pool in the [RAP handler method](../abap-for-rap-business-objects/abapmethods_for_rap_behv.md) [`FOR MODIFY`](../abap-for-rap-business-objects/abaphandler_meth_modify.md), unless the associations is managed.

- Projection BO and RAP BO Interface: In a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md) and in a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md), the link and unlink actions can be reused from the [base BDEF](../../abap-glossary/abenrap_base_bdef_glosry.md). This can be done using the keyword `use` for the association, listing the respective operations again. For further details, see topic [RAP BDL - use, projection BDEF](abenbdl_use_projection.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [Inverse Function](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/14fedb7fb9dc4ac68830bd0bb845244f?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In this example, a target entity instance with the primary key `TargetKey = 100` is supplied in the parameter of the inverse function. As a result, all source entity instances with the foreign key `TargetKey = 100` are returned.

BDEF of the source entity:

``` abap
managed implementation in class bp_demo_rap_inverse_func_src unique;
strict ( 2 );

define behavior for DEMO_RAP_INVERSE_FUNC_SRC
persistent table demo_invfct_src
lock master
authorization master ( instance )

{
  create ( authorization : global );
  update;
  delete;
  field ( readonly : update ) SourceKey;

  association _CROSS_ASSOC
  {
    inverse function inverse_function;
  }

  mapping for demo_invfct_src
    {
      SourceKey = source_key;
      TargetKey = target_key;
      CharField = char_field;
    }

}
```

The source table in this example is filled with the following instances:

\|SOURCE_KEY\|TARGET_KEY\|CHARFIELD \|

\|1\|100\|source 1 \| \|2\|200\|source 2 \| \|3\|300\|source 3\|

The `inverse function` can be executed with EML as demonstrated in the following code snippet:

``` abap
READ ENTITIES OF demo_rap_inverse_func_src 
  ENTITY demo_rap_inverse_func_src 
  EXECUTE inverse_function FROM VALUE #( ( 
 
    %cid = 'mycid' 
    %param-TargetKey = '100' 
 
  ) ) 
 
  RESULT DATA(result).
```

The output delivers the following results:

\|%CID\|%PARAM \|

\|mycid\|SOURCEKEY\|TARGETKEY\|CHARFIELD \| \| \|1\|100\|source 1 \| \|mycid\|SOURCEKEY\|TARGETKEY\|CHARFIELD \| \| \|2\|100\|source 2\|
