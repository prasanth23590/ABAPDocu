---
title: "CDS DDL - CDS View Entity, SELECT, Associations"
source_file: abencds_association_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, SELECT, Associations

[CDS associations](../../abap-glossary/abencds_association_glosry.md) offer an advanced modelling capability for CDS data models. A CDS association defines a relationship between two [CDS entities](../../abap-glossary/abencds_entity_glosry.md). A CDS association can be used to include fields from the [association target](../../abap-glossary/abenassociation_target_glosry.md) in the current view, and/or it can be published for usage in other CDS entities or in ABAP SQL.

As soon as an association is used in a [path expression](../../abap-glossary/abenpath_expression_glosry.md), for example, to specify a field from the [association target](../../abap-glossary/abenassociation_target_glosry.md) in the element list of a view, it is internally transformed into a [join](../../abap-glossary/abenjoin_glosry.md). So technically, a CDS association is instantiated as join. The benefit of a CDS association compared to a join is that it can be reused in different positions and that it renders the task of coding complex [join expressions](../../abap-glossary/abenjoin_expression_glosry.md) superfluous. Further details about the use cases of CDS associations and by which join type they are represented are explained in the topic below about CDS associations and joins.

[Compositions](../../abap-glossary/abencds_composition_glosry.md) are special kinds of CDS associations. A CDS composition consists of a [CDS to-parent association](../../abap-glossary/abento_parent_association_glosry.md) and a [CDS to-child association](../../abap-glossary/abento_child_association_glosry.md) and it defines an existential dependency of the composition child to its composition parent. For example, a sales order item (composition child) always belongs to a sales order header (composition parent).

For an overview of all possible association targets of all CDS entities that can define associations, see [Data Source Matrix](abencds_data_source_matrix.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The CDS view entity `DEMO_SALES_CDS_SO_I_VE` shown below returns information about sales order items. It defines three associations:

- A to-parent association `_SalesOrder`: A sales order item must always belong to a sales order, so there is an existential dependency.

- A to-child association `_ScheduleLine`: each sales order item can have one or more schedule lines, so the CDS view entity that contains information about schedule lines is defined as composition child.

- A simple association `_Material`: this association can be used to enrich a sales order item with information about the material.

In the `SELECT` list, `_SalesOrder` and `_ScheduleLine` are exposed. They can be accessed externally, but the current view does not use any data from them and no join is generated. From the association `_Material`, the field `material` is included in the view. This means that this association is instantiated as join. Since it is not published, it cannot be used in other CDS view entities or in ABAP SQL. ![figure](images_abdoc_assoc_expl.png)

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_SALES_CDS_SO_I_VE
  as select from
    demo_sales_so_i
    association        to parent DEMO_SALES_CDS_SO_VE as _SalesOrder
      on $projection.parent_key = _SalesOrder.so_key
    composition of exact one to many DEMO_SALES_CDS_SO_I_SL_VE   
                                                      as _ScheduleLine
    
    
    association of many to one DEMO_SALES_CDS_MATERIAL_VE  
                                                      as _Material
      on $projection.material = _Material.material
    {
      key so_item_key,
          parent_key,
          posnr,
          material,
          @Semantics.amount.currencyCode: 'currency'
          gross_amount,
          currency,
          @Semantics.quantity.unitOfMeasure: 'unit'
          quantity,
          unit,
          _SalesOrder,
          _ScheduleLine,
          _Material.material_type as Type
    }

    
    
    
```

For further details, see the following sections:

- [Details on CDS Associations: Use Cases and Join Types](abencds_assoc_join_v2.md)

- [Association](abencds_simple_association_v2.md)

- [Composition](abencds_composition_v2.md)

- [To-parent Association](abencds_to_parent_assoc_v2.md)
