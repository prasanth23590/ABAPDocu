---
title: "RAP - draft table"
source_file: abenbdl_draft_table.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorCharacteristics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - draft table

## Syntax

``` abap
... 
draft table DraftTableName [query DraftQueryView] 
...  
```

[`query DraftQueryView`](abenbdl_draft_query_view.md)

## Description

A [RAP draft table](../../abap-glossary/abendraft_table_glosry.md) is a [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md) used to store draft data. The draft table must reflect the fields of the underlying CDS entity. It must meet the following requirements:

- It contains a field for each field of the CDS entity that the current entity is based on. The order of the fields is not relevant.

- The first field must be a client field that has the data type `CLNT`.

- The field names of the fields of the draft tables are the same as the field names of the underlying CDS entity. If the CDS entity has assigned alias names, these alias names must be used.

- The data types and field lengths must match exactly.

- Additionally, the draft table must contain some technical information the [RAP transactional engine](../../abap-glossary/abenrap_transac_engine_glosry.md) needs to handle the draft. This technical information is added automatically with the draft admin include. The draft admin include is the predefined [DDIC include structure](../../abap-dictionary-ddic/ddic-data-types/abenddic_include_structure.md) `SYCH_BDL_DRAFT_ADMIN_INC`.

Here's an example:

``` abap
define table DraftTable { 
  key client        : abap.clnt not null; 
    ... 
    "%admin"        : include sych_bdl_draft_admin_inc;}
```

The optional addition [`query`](abenbdl_draft_query_view.md) can be used to specify a [draft query view](../../abap-glossary/abendraft_query_view_glosry.md) `DraftQueryView`. A draft query view allows the definition of read access limitations for draft data based on the [data control language (DCL)](../../abap-glossary/abencds_dcl_glosry.md).

## Availability

- A draft database table is relevant for [draft-enabled RAP business objects](../../abap-glossary/abendraft_rap_bo_glosry.md) of the implementation types `managed` and `unmanaged` and for these, it is mandatory.

- In a [projection behavior definition](../../abap-glossary/abencds_proj_bdef_glosry.md) and in an [interface behavior definition](../../abap-glossary/abencds_interface_bdef_glosry.md), the draft table is automatically inherited and does not need to be explicitly defined. For details, see the topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

## Hints

- The draft database table can be generated automatically via a quick fix in the behavior definition, which is offered as soon as RAP draft handling is enabled for the business object.

- When using [`late numbering`](abenbdl_late_numbering.md) for a draft-enabled RAP BO, it is mandatory that the draft table has an additional key field `DRAFTUUID` of data type `raw(16)`.

- A draft table is a regular [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md) and can be accessed as such. Access with [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) and [AMDP](../../abap-glossary/abenamdp_glosry.md) is technically possible, but not recommended. It is recommended that a draft table is accessed using the [RAP framework](../../abap-glossary/abenrap_framework_glosry.md) only, for example, with [EML](../../abap-glossary/abeneml_glosry.md), so that the draft metadata get updated automatically.

## More Information

Development guide for the ABAP RESTful Application Programming Model, topic [Draft Database Table](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/0c86bebb4c7f47aaa8eda6068176abd8?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example demonstrates why ABAP SQL is not suitable to access draft database tables.

It shows a managed BDEF based on the CDS root view entity `DEMO_RAP_MANAGED_DRAFT_1`. The BDEF is draft-enabled and it defines the persistent database table `DEMO_DBTAB_ROOT` and the draft database table `DEMO_DBTAB_DRAFT`.

**Note:** This example does not fully meet the requirements of the [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). It is intentionally kept short and simple and serves demonstration purposes only. See more information on the RAP BO contract in the [Development guide for the ABAP RESTful Application Programming Model](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

``` abap
managed
implementation in class bp_demo_rap_managed_draft_1 unique;
strict ( 2 );
with draft;

define behavior for DEMO_RAP_MANAGED_DRAFT_1 alias ParentEntity
persistent table demo_dbtab_root
draft table demo_dbtab_draft
lock master
total etag Timestamp
etag master LastChangedAt
authorization master ( none )

{
  create;
  update;
  delete;
  field ( readonly : update ) KeyFieldRoot;
  field ( readonly ) Timestamp, LastChangedAt;

  draft action Activate optimized;
  draft action Discard;
  draft action Edit;
  draft action Resume;
  draft determine action Prepare;

  mapping for demo_dbtab_root
    {
      KeyFieldRoot  = key_field;
      DataFieldRoot = data_field;
      CharFieldRoot = char_field;
      Timestamp     = crea_date_time;
      LastChangedAt = lchg_date_time;
    }
}
```

The class `CL_DEMO_RAP_MANAGED_DRAFT_1` accesses the business object using [EML](../../abap-glossary/abeneml_glosry.md). It contains the same code block twice: first, it clears the draft database table using the ABAP SQL statement `DELETE FROM`. Then, it creates a new draft instance with the key value '3' using the EML statement `MODIFY ENTITIES` and commits this entity instance to the draft database table.

Code snippet - this code block is repeated twice:

``` abap
DELETE FROM demo_dbtab_draft. 
MODIFY ENTITIES OF demo_rap_managed_draft_1 
      ENTITY ParentEntity 
        CREATE FROM 
        VALUE #( ( %is_draft = if_abap_behv=>mk-on 
        %control-KeyFieldRoot = if_abap_behv=>mk-on 
        %data-KeyFieldRoot = 3 ) ) 
 
  REPORTED FINAL(create_reported) 
  FAILED FINAL(create_failed) 
  MAPPED FINAL(create_mapped). 
 
COMMIT ENTITIES.
```

The first time, this entry is written to the draft database table and displayed as screen output. The second time, however, the creation of the new draft instance fails and the draft database table remains empty. The reason is that the draft database table cannot be emptied using ABAP SQL. It contains metadata which cannot be deleted with ABAP SQL and therefore, the key is considered to be a duplicate, even though the draft database table was cleared. ![figure](images_abdoc_draft_table.png)

This demonstrates why the draft database table should only be accessed using the RAP framework, in this case, using either the EML statement [`DELETE`](../abap-for-rap-business-objects/abapmodify_entity_entities_op.md) or the [draft action `Discard`](abenbdl_draft_action.md) to clear all entries from the draft database table.

The class `CL_DEMO_RAP_MANAGED_DRAFT_2` demonstrates how to correctly clear a draft database table:

- It creates a new draft instance with the key value '4' and discards it using the draft action `Discard`.

- Then, it successfully creates the same instance again.

- The instance is deleted again using the EML statement `DELETE FROM` and created once again.

Result: the creation of a new draft instance with the same key value works three times in a row, because `Discard` and `DELETE FROM` clear the entries of the draft table as well as the metadata. ![figure](images_abdoc_draft_table.jpg)
