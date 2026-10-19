---
title: "CDS DDL - PROPAGATE VIEW ENTITY BUFFER (Obsolete)"
source_file: abencds_propagate_buffer.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - PROPAGATE VIEW ENTITY BUFFER (Obsolete)

It is still possible, but not recommended, to create CDS propagated buffers. However, this is advised against, as there are no longer performance gains to be had.

## Syntax

``` abap
PROPAGATE VIEW ENTITY BUFFER ON cds_entity 
{ 
  propagated_field1[, 
  propagated_field2][, 
  ...] 
}[;]  
```

## Description

Defines a [CDS propagated buffer](../../abap-glossary/abencds_prop_buffer_glosry.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) for a [CDS entity](../../abap-glossary/abencds_entity_glosry.md).

A CDS propagated buffer is a [CDS entity buffer](../../abap-glossary/abencds_entity_buffer_glosry.md) that defines [SQL path target fields](../../abap-glossary/abensql_target_field_glosry.md) for [buffer propagation](../../abap-glossary/abencds_buffer_propagation_glosry.md) for a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) or a [CDS transactional query](../../abap-glossary/abencds_transactional_pv_glosry.md). Buffer propagation means that the joins defined by a [CDS association](../../abap-glossary/abencds_association_glosry.md) are processed by the [ABAP SQL in-memory engine](../../abap-programming-language/abap-database-access/abenabap_sql_inmemeng.md) on data stored in the [table buffer](../../abap-glossary/abentable_buffer_glosry.md). Instead of using joins instantiated on the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md), temporary joins are created on [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) to process the table buffer. This can result in performance gains.

As a prerequisite, the definition of the CDS view entity or CDS transactional interface must contain the following annotation: [`@AbapCatalog.entityBuffer.propagationAllowed:true`](../abap-cds-annotations/abencds_1859277801_anno.md).

This annotation entails additional syntax checks. It is only allowed if the CDS entity in question meets certain prerequisites. These prerequisites are described in topic [ABAP CDS - Table Buffering of CDS View Entities](../abap-cds-data-definitions/abencds_v2_view_buffering.md).

If a CDS propagated buffer is active for a CDS entity, the annotation cannot be removed there.

`cds_entity` can be a CDS view entity or a [CDS transactional query](../../abap-glossary/abencds_transactional_pv_glosry.md).

A propagated buffer must define at least one field `propagated_field1`, `propagated_field2`, ... in curly brackets. A maximum of ten fields is possible. The fields must be [SQL path target fields](../../abap-glossary/abensql_target_field_glosry.md) that are defined in the [select list](../abap-cds-data-definitions/abencds_select_list_entry_v2.md) or [projection list](../abap-cds-data-definitions/abencds_proj_view_element.md) of the CDS entity `cds_entity` for which buffer propagation is defined. In addition, the [CDS association path](../../abap-glossary/abencds_association_path_glosry.md) must consist of at least one association, for example: `_assoc.field`. A longer association path is also possible. For the propagated fields, the following rules apply:

- `propagated_field1`, `propagated_field2`, ... must not be the result of a calculation in the CDS entity `cds_entity` for which buffer propagation is defined. This means, they must not be used as operands of expressions and functions. The only exception to this rule is a [cast expression](../abap-cds-data-definitions/abencds_cast_expression_v2.md) with the addition `PRESERVING TYPE`. `propagated_field1`, `propagated_field2` can be used as operands of a cast expression with the addition `PRESERVING TYPE`.

- `propagated_field1`, `propagated_field2`, ... must not be defined as key fields [`KEY`](../abap-cds-data-definitions/abencds_select_list_entry_v2.md) in the CDS entity `cds_entity` for which buffer propagation is defined. Key fields are not allowed to be propagated.

- `propagated_field1`, `propagated_field2`, ... must not be used in a `WHERE`, `GROUP BY`, or `HAVING` clause, not in the `ON` condition of a join, or the `ON` condition of an association in the CDS entity `cds_entity` for which buffer propagation is defined.

- Each propagated field can be specified only once and must have a unique name.

The following rules apply to the CDS association path that is used to specify the propagated fields:

``` abap
**Note:** In the following, the terms *first association*, *intermediate association*, and *last association* are used to specify the place of an association in an association path\. For example, if an association path consists of four CDS associations `_assoc1._assoc2._assoc3._assoc4.field`, the terms are used as follows: 
\- `assoc1` is the first association 
\- `assoc2` and `assoc3` are the intermediate associations 
\- `assoc4` is the last association\. The last association is the origin of the SQL path target field\.
```

- The [source cardinality](../../abap-glossary/abensource_cardinality_glosry.md) of the first association is irrelevant. The [target cardinality](../../abap-glossary/abentarget_cardinality_glosry.md) of the first association must be `TO EXACT ONE`.

- The source and target cardinalities of the intermediate associations must be `[TO] EXACT ONE`.

- The source cardinality of the last association must be `EXACT ONE`. The target cardinality of the last association must be `TO ONE` or `TO EXACT ONE`.

- If the CDS association path consists of exactly one association, the source cardinality of that association is irrelevant and the target cardinality can be `TO ONE` or `TO EXACT ONE`.

- The data source that is the origin of the propagated field must have the buffering type [full buffering](../../abap-programming-language/abap-database-access/abenbuffer_complete_buffering.md). No other buffering types are currently supported.

- If the association path consists of more than one association, the `ON` conditions and all filter conditions of all associations involved must be compatible to each other. This means that the same number of fields must be used in the `ON` conditions, the fields used must be compatible and the filter conditions, if any, must be identical.

- The first association of the association path of the propagated field must bind all of the key fields of the association target in its `ON` condition using the [comparison operator](../abap-cds-data-definitions/abencds_cond_expr_comp_v2.md) `=`. All of the fields of the `ON` condition of this first association must be specified in the `SELECT` list.

- If the association to the original data source of the propagated field has a [filter condition](../abap-cds-data-definitions/abencds_path_expression_filter_v2.md), the filter condition must not have any input parameters as operands.

- Fields from [CDS entity extensions](../../abap-glossary/abencds_entity_extend_glosry.md) can be propagated fields as long as they meet all the prerequisites.

- The path expression must be instantiated as a [left outer join](../../abap-glossary/abenleft_outer_join_glosry.md) in the SQL statement generated on the database. No other [join type](../../abap-glossary/abenjoin_type_glosry.md) type is supported. For details on associations and joins, see [CDS DDL - CDS View Entity, Associations and Joins](../abap-cds-data-definitions/abencds_assoc_join_v2.md).

One or more propagated buffers can be specified for a CDS entity `cds_entity`. If more than one propagated buffer is specified, the distinct union set of all buffer propagations is used. This means that the fields from all buffer propagations are combined and duplicates are removed. The distinct union set can have a maximum of ten fields.

## Hints

- For technical reasons, CDS buffer propagation must be explicitly triggered using an [ABAP tuning object](../../abap-glossary/abenabap_tuning_object_glosry.md). An implicit and automatic join with the existing table buffer on AS ABAP is not possible.

- The name of a CDS propagated buffer is not reflected in its definition. It only occurs as the name of the repository object in ADT.

- The propagated fields defined in a CDS propagated buffer are typically fields that are not changed, such as localized text fields.

- In the language version [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md), SAP customers and partners cannot define CDS propagated buffers for CDS entities delivered by SAP. Buffer propagation is not covered by any [release contract](../../abap-glossary/abenrelease_contract_glosry.md) and SAP does not guarantee stable elements for buffer propagation.

- If not all the fields of an association are propagated, the join to the respective entity is executed on the SAP HANA database and there is no performance gain.

- Buffer propagation does not have any effect on [CDS access control](../../abap-glossary/abencds_access_control_glosry.md). If there is access control defined for a CDS entity, it is applied as usual.

- Buffer propagation is available only for SQL path target fields defined using a CDS association path. Joins or associations defined in ABAP SQL are not covered.

## More Information

ABAP Data Models guide, section about [CDS Propagated Buffers](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/6c69199817ce41f4a6201ca943c6d81a?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following definition demonstrates the syntax for a CDS propagated buffer.

``` abap
propagate view entity buffer on DEMO_SALES_PV_MATERIAL 
{ 
  MaterialName 
}
```

The propagated buffer refers to the CDS transactional query `DEMO_SALES_PV_MATERIAL`. This transactional query contains the annotation `@AbapCatalog.entityBuffer.propagationAllowed: true`. Additionally, the original data source of the propagated field, `DEMO_SALES_CDS_MAT_TEXT`, is fully buffered.
