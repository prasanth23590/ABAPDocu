---
title: "RAP - with managed instance filter"
source_file: abenbdl_mngd_instance_check_proj.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Projection Behavior Definitions > RAP - BehaviorDefinitionHeader, Projection BDEF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - with managed instance filter

## Syntax

``` abap
... 
with managed instance filter; 
 ...  
```

## Description

Optional addition for [projection BDEFs](../../abap-glossary/abencds_proj_bdef_glosry.md) and [interface BDEFs](../../abap-glossary/abencds_interface_bdef_glosry.md). It is specified in the [behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md) and it is valid for all [RAP BO entities](../../abap-glossary/abenrap_bo_entity_glosry.md) that are part of the current RAP BO.

The effect is that the [`WHERE`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_proj_view_cond_expr.md) condition of the underlying [CDS transactional query](../../abap-glossary/abencds_transactional_pv_glosry.md) or [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md) is evaluated when the BDEF is accessed with [ABAP EML](../../abap-glossary/abenabap_eml_glosry.md) or [OData](../../abap-glossary/abenodata_glosry.md) requests from Web clients, both for [active](../../abap-glossary/abenrap_active_instance_glosry.md) and for [draft instances](../../abap-glossary/abenrap_draft_instance_glosry.md). If an entity within the BDEF does not have a `WHERE` clause, this addition does not have any effect, but as soon as a `WHERE` clause is added, the checks are activated.

If this addition is not specified, the `WHERE` clause is ignored when the BDEF is accessed with [ABAP EML](../../abap-glossary/abenabap_eml_glosry.md) or [OData](../../abap-glossary/abenodata_glosry.md) requests from Web clients. This means that it is possible to read and modify entity instances that are not part of the result set of the projection BDEF or interface BDEF in question.

The instances for the following operations are checked *before* every EML or OData call:

- [Read operation](../../abap-glossary/abenrap_read_operation_glosry.md)

- [Update operation](../../abap-glossary/abenrap_update_operation_glosry.md)

- [Delete operation](../../abap-glossary/abenrap_delete_operation_glosry.md)

- Executing [instance RAP BO operations](../../abap-glossary/abenrap_instance_operation_glosry.md)

- [Read by association operation](../../abap-glossary/abenrap_rba_operation_glosry.md)

- EML permissions ([`GET PERMISSIONS`](../abap-for-rap-business-objects/abapget_permissions.md))

If an entity instance does not fulfill the `WHERE` clause, it is returned in the [response parameter](../../abap-glossary/abenrap_response_param_glosry.md) [`FAILED`](../abap-for-rap-business-objects/abapeml_response.md). It is not passed to the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) of the operation in question.

The `WHERE` clause is evaluated and the instance check takes place before the RAP handler method is called but after the [RAP BO augmentation](../../abap-glossary/abenrap_bo_augmentation_glosry.md), so the [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) can modify incoming requests with the operation augmentation in such a way that they fulfill the `WHERE` clause, for example, if fields are defined as `readonly` in the projection.

During an update request, if instances are modified in a way that they no longer fulfill the `WHERE` clause of the underlying CDS entity, then no further operations on these instances are possible via the current projection or interface BDEF.

For the operations [create](../../abap-glossary/abenrap_create_operation_glosry.md) and [create-by-association](../../abap-glossary/abenrap_cba_operation_glosry.md), the RAP BO provider must ensure via RAP handler methods and the operation augmentation that only valid entity instances are created. The managed RAP BO provider does not evaluate the `WHERE` clause for these operations. Therefore, creating RAP BO entity instances that do not fulfill the `WHERE` condition is possible, but no further operations on these instances are possible.

In the case of the read-by-association operation, the requested RAP BO entity instances of the [association target](../../abap-glossary/abenassociation_target_glosry.md) instances are checked *after* every EML or OData call. If an entity instance does not fulfill the `WHERE` clause of the child entity, it is removed from the [`RESULT`](../abap-for-rap-business-objects/abapeml_result.md) and [`LINK`](../abap-for-rap-business-objects/abapread_entity_entities_op.md) set, but it is not added to the response parameter `FAILED`.

If a projection BDEF is based on an interface BDEF and the underlying projection views both have a `WHERE` clause, then always the requested entity decides whether the instance filter is active or not. For example, if only the projection BDEF specifies `with managed instance checks` and a RAP BO consumer requests this projection BDEF, then both `WHERE` clauses (the one for the interface and the one for the projection) are evaluated and instances are filtered out.

## Availability

- [RAP projection behavior definition](../../abap-glossary/abencds_proj_bdef_glosry.md)

- [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md)

## Restrictions

The `WHERE` clause is not evaluated when executing [static RAP BO operations](../../abap-glossary/abenrap_static_operation_glosry.md).

## Hints

- Without the `with managed instance checks` addition, instances that are not part of the projection may be read and modified using ABAP EML or OData, potentially posing a security risk.

- When using [`IN LOCAL MODE`](../abap-for-rap-business-objects/abapin_local_mode.md), `with managed instance checks` does not have any effect.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example demonstrates the effect of the addition `with managed instance filter` in a projection BDEF.

First of all, it demonstrates that the `WHERE` clause of a CDS transactional interface is ignored in an ABAP EML call if the addition `with managed instance filter` is *not* specified.

CDS transactional interface that uses a `WHERE` clause to filter the result set to include only instances with that have the value *AA* in the field `carrid`.

``` abap
@EndUserText.label: 'CDS transactional query'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_RAP_INSTANCE_FILTER_TQ
  provider contract transactional_query
  as projection on DEMO_RAP_INSTANCE_FILTER
{
  key carrid,
  key connid,
      countryfr
}
where carrid = 'AA'
```

Projection BDEF without managed instance filter:

``` abap
projection;
strict ( 2 );
with managed instance filter;
define behavior for DEMO_RAP_INSTANCE_FILTER_TQ alias Root
{
  use create;
  use update;
  use delete;

}
```

Accessing the projection BDEF:

- The projection BDEF is first accessed using ABAP SQL. The `WHERE` condition of the transactional interface is evaluated and the result set contains only instances that have the value *AA* in the field `carrid`.

- Then, the projection BDEF is accessed using ABAP EML. The `WHERE` condition is *not* evaluated and the result set also contains an instance with the value *LH* in the field `carrid`.

``` abap
"ABAP SQL read on projection 
SELECT FROM DEMO_RAP_INSTANCE_FILTER_TQ 
  FIELDS carrid, connid, countryfr 
  INTO TABLE @FINAL(select_res). 
 
"ABAP EML read entity on projection 
READ ENTITY DEMO_RAP_INSTANCE_FILTER_TQ 
ALL FIELDS WITH VALUE #( 
                       ( carrid = 'AA' connid = '0017' ) 
                       ( carrid = 'AA' connid = '0064' ) 
                       ( carrid = 'LH' connid = '0400' ) 
) 
RESULT DATA(read_res) 
FAILED DATA(read_failed). 
 
  FINAL(o) = cl_demo_output=>new(  ). 
  o->next_section( 'SELECT with ABAP SQL' 
    )->write( select_res 
    )->next_section( 'READ with ABAP EML' 
    )->write( read_res 
    )->display(  ).
```

Result: The entity instance highlighted in red should not be part of the result set. It should be filtered out by the `WHERE` clause. ![figure](images_instance_filter.jpg)

If, however, the projection BDEF specified the addition `with managed instance filter`, the `WHERE` clause is evaluated.

Projection BDEF with managed instance filter:

``` abap
projection;
strict ( 2 );

with managed instance filter;

define behavior for DEMO_RAP_INSTANCE_FILTER_TQ1
{
  use create;
  use update;
  use delete;

}
```

Accessing the projection BDEF with managed instance filter:

- The projection BDEF with a managed instance filter is accessed first using ABAP SQL and then using ABAP EML. The `WHERE` clause is evaluated in both cases and the result set is identical.

``` abap
"ABAP SQL read on projection 
SELECT FROM demo_rap_instance_filter_tq1 
  FIELDS carrid, connid, countryfr 
  INTO TABLE @FINAL(select_res1). 
 
"ABAP EML read entity on projection 
READ ENTITY demo_rap_instance_filter_tq1 
FIELDS ( carrid connid countryfr ) 
WITH VALUE #( ( %key-carrid = 'AA ' %key-connid = '0017' ) 
              ( %key-carrid = 'AA'  %key-connid = '0064' ) 
              ( %key-carrid = 'LH'  %key-connid = '0400' ) ) 
 
RESULT DATA(read_res1) 
FAILED DATA(read_failed1). 
 
FINAL(o) = cl_demo_output=>new(  ). 
o->next_section( 'SELECT with ABAP SQL' 
  )->write( select_res1 
  )->next_section( 'READ with ABAP EML' 
  )->write( read_res1 
  )->display(  ).
```

- Result:

  ![figure](images_instance_filter2.jpg)
