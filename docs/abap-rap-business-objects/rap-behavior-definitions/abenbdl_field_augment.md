---
title: "RAP - FieldAugmentation, Projection BDEF"
source_file: abenbdl_field_augment.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Projection Behavior Definitions > RAP - EntityBehaviorDefinition, Projection BDEF > RAP - EntityBehaviorBody, Projection BDEF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - FieldAugmentation, Projection BDEF

## Syntax

``` abap
...field(modify[,FieldChar]) Field1[, Field2] [, ...];  
```

## Description

[RAP BO augmentation](../../abap-glossary/abenrap_bo_augmentation_glosry.md) for read-only fields in a CDS projection behavior definition.

[CDS projection views](../../abap-glossary/abencds_projection_view_glosry.md) may contain [CDS virtual elements](../../abap-glossary/abencds_virtual_element_glosry.md) (defined using the keyword [`VIRTUAL`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_proj_view_virtual_element.md)), [fields defined by association traversal](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_proj_view_element.md) ([path expressions](../../abap-glossary/abenpath_expression_glosry.md)), or [CDS localized fields](../../abap-glossary/abencds_localized_field_glosry.md) (defined using the keyword [`LOCALIZED`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_localized.md)). These fields are by default excluded from the [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) for the [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md), because they are non-transactional in character. Augmentation provides a means to include these fields in transactional handling. As a prerequisite, they must be marked in the projection BDEF as follows:

`field (modify) Field1 [, Field2][, ...];`

The effect is that the fields `Field1`, `Field2`, ... appear in derived types such as [`TYPE TABLE FOR CREATE`](../abap-for-rap-business-objects/abaptype_table_for.md) for the projection BDEF.

The following field characteristics `FieldChar` are available for augmented fields:

- `mandatory`

- `readonly`

- `mandatory:create`

- `readonly:update`

- `features:instance`

  - A prerequisite for using `features:instance` on an augmented field is that [BDEF strict mode](../../abap-glossary/abenrap_strict_mode_glosry.md) is enabled.

  - An implementation in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR INSTANCE FEATURES`](../abap-for-rap-business-objects/abaphandler_meth_features.md) in the ABAP behavior pool of the projection layer is required.

## More Information

- Development guide for the ABAP RESTful Application Programming Model, section [Operation Augmentation](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/346c2b7516ce4176bbb4daebaa80c2ca?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a projection BDEF that augments a virtual element. The base BDEF is `DEMO_RAP_MANAGED_ASSOC_ROOT`.

``` abap
projection
implementation in class bp_demo_rap_proj_augment unique;
strict ( 2 );

define behavior for DEMO_RAP_PROJ_AUGMENT alias _Parent
{
  use create ( augment );
  use update ( augment );
  use delete;

  use association _child { create ( augment ); }

  field ( modify ) VirtualElement;
  field ( readonly ) DecFieldRoot;
}

define behavior for DEMO_RAP_PROJ_AUGMENT_CHILD alias _Child
{
  use update;
  use delete;

  use association _parent;
}
```

As a result, the field is part of the BDEF derived types: ![figure](images_abdoc_virtual.jpg)

For a complete end-to-end example, see the Development guide for the ABAP RESTful Application Programming Model, section [Editing Language-Dependent Fields](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/fc374ac9b02e4dbcba356afc77432dc2?version=sap_cross_product_abap).
