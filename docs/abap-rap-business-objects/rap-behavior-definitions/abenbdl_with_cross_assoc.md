---
title: "RAP - with cross associations"
source_file: abenbdl_with_cross_assoc.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - BehaviorDefinitionHeader"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - with cross associations

## Syntax

``` abap
... 
with cross associations; 
...  
```

## Description

The addition `with cross associations` prepares a [managed RAP business objects](../../abap-glossary/abenmanaged_rap_bo_glosry.md) for cross-BO transactional interaction. It offers an improved runtime implementation for all operations for associations that are defined in the behavior definition. This includes syntax checks and error handling concerning cross-BO modeling. If not defined differently by using the `unmanaged` [association implementation type](../../abap-glossary/abenrap_assoc_impl_type_glosry.md) for individual associations, all [operations for associations](../../abap-glossary/abenrap_operation_assoc_glosry.md) are handled and orchestrated by the [managed BO provider](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md). They do not have to be implemented in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md).

**Note:** The same functionality can be achieved by other syntax elements that are defined for the individual association, for example by using the `managed` [association implementation type](../../abap-glossary/abenrap_assoc_impl_type_glosry.md) or [association \_assoc using TargetEntity {...}](abenbdl_association.md).

The syntax `with cross associations` is added in the [RAP behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md) as it enables the functionality for the entire business object. It is not possible to define `with cross associations` for individual [entities](../../abap-glossary/abenrap_bo_entity_glosry.md) within a business object. In extension BDEFs `with cross associations` can be defined independently from the usage of this syntax in the core BDEF.

## Hint

The keyword `with cross associations` is necessary to ensure that transactional enablement works for the most common associations. For example, it supports cross-BO scenarios with a target entity that has [RAP late numbering](../../abap-glossary/abenrap_late_numbering_glosry.md), which would not work without it.

## Availability

- [Managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- In [projection BDEFs](../../abap-glossary/abenrap_projection_bo_glosry.md) and in [interface BDEFs](../../abap-glossary/abencds_interface_bdef_glosry.md), cross-BO transactional enablement is switched on automatically for all used associations if it was specified in the base behavior definition header with `with cross associations`.

**Dependencies**

The addition with cross associations enables cross-BO transactional enablement to all associated BO entities of foreign business objects. There are several related syntax elements in the behavior definition:

- [`unmanaged`](abenbdl_assoc_impl_type.md) association AssociationName;:

  You can define an association in a [managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md) for which `with cross associations` is defined as `unmanaged`. In that case, the implementation methods for all defined [operation&#x00B4;s for associations](../../abap-glossary/abenrap_operation_assoc_glosry.md) (standard and nonstandard) must be implemented in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md).

- [`association`](abenbdl_association.md) AssociationName { };:

  The association is read-enabled. In [managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md) with the definition `with cross associations` the `read-by-association` implementation is given by the managed RAP BO provider for all association targets if the association is not specified as `unmanaged`.

- [`association`](abenbdl_association.md) AssociationName { create; }:

  The association is create-enabled. In [managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md) with the definition `with cross associations` the `create-by-association` implementation is given by the managed RAP BO provider for all association targets if the association is not specified as `unmanaged`.

- association AssociationName { [`inverse function`](abenbdl_inverse_funct.md) InverseFunctionName; }:

  The [inverse function](../../abap-glossary/abenrap_inverse_function_glosry.md) is relevant to retrieve all entity instances of targets in [target-resolved associations](../../abap-glossary/abentarget_resolved_assoc_glosry.md). The inverse function on the target entity's association is then executed. In managed RAP BOs with `with cross associations` on BDEF header, the function is available to RAP BO consumers without any implementation in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) if the association is not specified as `unmanaged`. The inverse function can only be declared for [source-resolved associations](../../abap-glossary/abensource_resolved_assoc_glosry.md).

- associations AssociationName { [`link action`](abenbdl_link_unlink_action.md) LinkActionName; [`unlink action`](abenbdl_link_unlink_action.md) UnlinkActionName; }:

  These [operations for associations](../../abap-glossary/abenrap_operation_assoc_glosry.md) are responsible to connect and disconnect associated entity instances of source and target entities in cross-BO associations. For associations with implementation type managed, the actions are available to RAP BO consumers without any implementation in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) if the association is not specified as `unmanaged`. The link and unlink action of a cross-BO association can only be declared on [source-resolved associations](../../abap-glossary/abensource_resolved_assoc_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example is based on two separate BOs, `DEMO_R_A` serving as the source and `DEMO_R_B` serving as the target entity. `DEMO_R_A` has the BDEF header definition `with cross associations` enabling the association `_b` to target a late numbering BO in a source-resolved association. For this association the managed BO provider implements the relevant operations for associations that are specified for the association, namely `read by association`, `create by association`, `link action`, `unlink action` and `inverse function`.

``` abap
managed implementation in class bp_demo_r_a unique;
strict ( 2 );
with cross associations;

define behavior for DEMO_R_A //alias <alias_name>
persistent table demo_db_a
lock master
authorization master ( none )

{
  create ;
  update;
  delete;
  field ( readonly : update ) AKey, Bkey;

  association _b abbreviation B
  {
    create;
    link action link_B;
    unlink action unlink_B;
    inverse function inverse_function;
     }

  mapping for demo_db_a
    {
      aKey      = a_key;
      bKey      = B_key;
      CharField = char_field;
    }

}
```

When a `create by association` is executed creating an instance of `DEMO_R_B` the temporary key `%pid` is written to the `%pid_b` field of the associated instance of entity A in the transactional buffer. This can be retrieved by reading the associated instance of entity A.

``` abap
***Reset Tables 
    DELETE FROM demo_db_a. 
    DELETE FROM demo_db_b. 
 
*** Cross-BO CBA,  create instance of A, 
*** create instance of B with preliminary key 
    MODIFY ENTITIES OF demo_r_a 
     ENTITY demo_r_a 
     CREATE 
      FIELDS ( AKey CharField ) 
      WITH VALUE #( (  %cid      = 'MyCid_Create_A' 
                       AKey      = '002' 
                       CharField = 'xxx' ) ) 
     CREATE BY \_b 
       FIELDS ( BKey CharField ) 
       WITH VALUE #( ( %cid_ref = 'MyCid_Create_A' 
                       %target  = VALUE #( ( %cid     = 'MyCid_CBA' 
                                            charfield = 'YYY' ) ) 
 
                      ) ) 
     FAILED DATA(failed) 
     MAPPED DATA(mapped) 
     REPORTED DATA(reported). 
 
 
*** read newly created instance of A, 
*** %pid_B is filled, Bkey empty 
    READ ENTITIES OF demo_r_a 
         ENTITY demo_r_a 
         ALL FIELDS WITH VALUE #( ( akey = '002' ) ) 
    RESULT DATA(result_a).
```

The following figure displays the read result. ![figure](images_abdoc_result_a_xbo.png)

When committing the modify and read request, the save handlers of both BOs are called. The save handler of `DEMO_R_B` calls the `adjust_numbers` method, which assigns the final key value of `BKey`. The save handler of `DEMO_R_A` then invokes the `link action` to update the foreign key field `BKey` with the final value. A subsequent read, shows the result of the saved instance with the foreign key value set.

``` abap
**** commit entities --> Finalize A, finalize B, adjust numbers B, 
**** save A + B(including link action = update of A with foreign keyB) 
    COMMIT ENTITIES. 
 
**** read saved instances of A, Bkey is set 
    READ ENTITIES OF demo_r_a 
         ENTITY demo_r_a 
         ALL FIELDS WITH VALUE #( ( akey = '002' ) ) 
    RESULT DATA(result_a_after_save).
```

The following figure displays the read result of the saved instance. ![figure](images_result_a_after_save.png)

This example demonstrates that the RAP managed runtime implements and orchestrates the respective handler methods in cross-BO scenarios, when `with cross associations` is defined.
