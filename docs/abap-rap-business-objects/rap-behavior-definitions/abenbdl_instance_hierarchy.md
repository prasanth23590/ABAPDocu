---
title: "RAP - instance hierarchy"
source_file: abenbdl_instance_hierarchy.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - instance hierarchy

## Syntax

``` abap
instance hierarchy CDSHierarchyName 
{ 
  [copy action] 
  [reorder action] 
}  
```

[`copy action`](abenbdl_copy_action.md) · [`reorder action`](abenbdl_reorder_action.md)

## Description

The syntax `instance hierarchy { ... }` specifies parts of the behavior of a editable [treeview](../../abap-glossary/abenrap_treeview_glosry.md) for a managed or unmanaged RAP BO. A treeview visualizes data modeled by a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md) on a SAP Fiori UI. [RAP hierarchy actions](../../abap-glossary/abenrap_hierarchy_action_glosry.md) can be specified in curly brackets to define how hierarchy nodes are copied and reordered.

As a prerequisite, the RAP BO must include a CDS hierarchy. A step-by-step procedure on how to define the CDS data model for an editable treeview scenario is described in the RAP guide under [Editable Treeviews with Draft Capabilities](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/718e0f84564043afad76cf56e03e1528?version=sap_cross_product_abap).

`CDSHierarchyName` is the name of the [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md) defined for the RAP BO in question.

The following hierarchy actions are available:

- [RAP copy action](../../abap-glossary/abenrap_copy_action_glosry.md): A RAP hierarchy action that determines how a hierarchy node can be duplicated in an editable treeview scenario. For more information, see [RAP - `copy action`](abenbdl_copy_action.md).

- [RAP reorder action](../../abap-glossary/abenrap_reorder_action_glosry.md): A RAP hierarchy action that moves a hierarchy node to a dedicated position among its siblings in editable treeview scenario. Can be managed or unmanaged. For more information, see [RAP - `reorder action`](abenbdl_reorder_action.md).

The copy action and the reorder action are optional elements. The can be specified in curly brackets to offer the respective functionality. It is also possible to specify the syntax `instance hierarchy { }` without any addition. In this case, it does not have any effect.

## Availability

- [Managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- In a [projection BO](../../abap-glossary/abenrap_projection_bo_glosry.md) and in a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md), the syntax `instance hierarchy` cannot be specified or reused. The hierarchy actions, on the other hand, must be reused in a projection or interface BDEF.

## Hint

If you want your editable treeview scenario to allow moving a node to another parent node, the [link action](../../abap-glossary/abenrap_link_action_glosry.md) and the [unlink action](../../abap-glossary/abenrap_unlink_action_glosry.md) must be defined for the hierarchy self-association.

## More Information

For guidance on how to create a complete end-to-end scenario, see the development guide for the ABAP RESTful Application Programming Model, section [Editable Treeviews with Draft Capabilities](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/718e0f84564043afad76cf56e03e1528?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed behavior definition which enables the editable treeview scenario. It defines a copy action and a managed reorder action within curly brackets introduced by the syntax `instance hierarchy`.

**Note:** This example does not fully meet the requirements of the [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). It is intentionally kept short and simple and serves demonstration purposes only.

``` abap
managed implementation in class bp_demo_rap_inst_hier_p unique;
strict ( 2 );

define behavior for DEMO_RAP_INST_HIER_P
persistent table demo_tab_hier_p
lock master
authorization master ( instance )

{
  create ( authorization : global );
  update;
  delete;
  field ( readonly ) hier_p;
  association _Child { create; }
}

define behavior for DEMO_RAP_INST_HIER_C
persistent table demo_tab_hier_c
lock dependent by _Parent
authorization dependent by _Parent

{
  update;
  delete;
  field ( readonly ) hier_c, hier_p,
  sibling_order_number, assoc_number;
  association _Parent;

  instance hierarchy demo_rap_inst_hier_hn
  {
    managed reorder action changeNextSibling;
    field ( hierarchy-index ) sibling_order_number;
    copy action copyAction;
    ascending association _AscendingAssociation;
    descending association _DecendingAssociation { with cascading delete; }
  }
}
```
