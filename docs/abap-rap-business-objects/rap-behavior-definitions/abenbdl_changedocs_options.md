---
title: "RAP - changedocuments, Options"
source_file: abenbdl_changedocs_options.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - changedocuments, Options

## Syntax

``` abap
changedocuments([create:Option][,update:Option] [,delete:Option]);  
```

## Description

Defines logging options for [RAP change documents](../../abap-glossary/abenrap_change_documents_glosry.md) in the [entity behavior body](../../abap-glossary/abencds_entity_body_glosry.md) of a RAP BO. As a prerequisite, the entity in question must be enabled for RAP change documents as described in the topic [RAP - `changedocuments`](abenbdl_change_documents.md).

Logging options can be defined for the [standard operations](../../abap-glossary/abenrap_standard_operation_glosry.md) `create`, `update`, and `delete`. The following logging options `Options` are available:

- `none`: Defines that for the operation in question, no change document data is recorded.

- `key`: Defines that for the operation in question, only key values are recorded in the change documents.

- `data`: Defines that for the operation in question, all the data for change-document-relevant fields is recorded. A field is considered as relevant for change documents when it is typed with a [CDS simple type](../../abap-glossary/abencds_simple_type_glosry.md) with the annotation [`AbapCatalog.typeSpec.changeDocumentRelevant`](../../abap-core-data-services-abap-cds/abap-cds-annotations/abencds_2016919924-_anno.md) set to *true*, or a [DDIC data element](../../abap-glossary/abendata_element_glosry.md) where the **change document** flag is set.

For each standard operation, exactly one option can be defined. At least one option for a standard operation must be defined in brackets. If several options are defined, they are separated by a comma (`,`). They can occur in any order.

`create` and `delete` can be followed by all available options, `update` can be followed by the options `none` or `data`.

For the setting `update:data`, for each update of each change-document-relevant field, its value before *and* after the update operation is stored.

If no options are defined explicitly, the following default options apply implicitly:

`changedocuments( create:key, update:data, delete:key )`

## Availability

- [Change documents-enabled RAP BO entities](../../abap-glossary/abenrap_change_doc_enabled_glosry.md) in [managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

## Hints

- [Change document objects](../../abap-glossary/abenchange_document_obj_glosry.md) contain logging options for the generation of change documents. In RAP, these options are not evaluated. The BDEF syntax is considered instead.

- For [RAP BO non-standard operations](../../abap-glossary/abenrap_nstandard_operation_glosry.md), such as [RAP actions](../../abap-glossary/abenrap_action_glosry.md), changes to [change documents-enabled RAP BO entities](../../abap-glossary/abenrap_change_doc_enabled_glosry.md) are also logged. Non-standard operations are usually implemented as a combination of standard operations, and the logging works according to the logging options for the standard operations.

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [Integrating Change Documents](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/0dd9323b464244538295fc7457c39d8f?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF based on the CDS root view entity `DEMO_RAP_CHANGE_DOCS`.

- The root entity is defined as change documents master entity.

- The change document object `DEMO_CHGDOC` is used for logging changes.

- The child entity is defined as change documents dependent entity.

- The association `_parent` is defined in the entity behavior body of the child entity, thereby ensuring that changes in the child entity are logged in the change document object `DEMO_CHGDOC`.

- The logging options are defined in the entity behavior body.

**Note:** This example does not fully meet the requirements of the [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). It is intentionally kept short and simple and serves demonstration purposes only. For more information about the RAP BO contract, see the [Development guide for the ABAP RESTful Application Programming Model](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

``` abap
managed implementation in class bp_demo_rap_change_docs unique;
strict ( 2 );

define behavior for DEMO_RAP_CHANGE_DOCS alias Root
persistent table demo_dbtab_root
lock master
authorization master ( none )
changedocuments master ( DEMO_CHGDOC )
{

  changedocuments(create:key, update:data, delete:none);
  create;
  update;
  delete;
  field ( readonly:update ) key_field;
  association _child { create; }

  mapping for demo_dbtab_root corresponding
  {
  change_logging = char_field;
  }
}

define behavior for DEMO_RAP_CHANGE_DOC_CHILD alias Child
persistent table demo_dbtab_child
lock dependent by _parent
authorization dependent by _parent
changedocuments dependent by _parent
{
  changedocuments(delete:data, create:data);
  update;
  delete;
  field ( readonly:update ) key_field, key_field_child;
  association _parent;
}
```
