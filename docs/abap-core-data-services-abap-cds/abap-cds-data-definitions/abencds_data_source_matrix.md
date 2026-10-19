---
title: "ABAP CDS - Data Source Matrix"
source_file: abencds_data_source_matrix.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Data Source Matrix

The following tables show all possible data sources of all available [CDS entities](../../abap-glossary/abencds_entity_glosry.md):

- Direct data sources defined after `FROM`.

- [Association targets](../../abap-glossary/abenassociation_target_glosry.md) of [CDS associations](../../abap-glossary/abencds_association_glosry.md).

- Association targets of [CDS compositions](../../abap-glossary/abencds_composition_glosry.md).

Content:

- [Data Sources After `FROM`](abencds_data_source_matrix.md#data-sources-after-from)

- [Association Targets of CDS Associations](abencds_data_source_matrix.md#association-targets-of-cds-associations)

- [Association Targets of CDS Compositions](abencds_data_source_matrix.md#association-targets-of-cds-compositions)

## Data Sources After `FROM`

The following table lists all available CDS entities and which data sources they accept after `FROM`, both directly and joined via a join.

**Note:** [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) and [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) can define a [join](../../abap-glossary/abenjoin_glosry.md) between two data sources. The data sources that can be specified directly after `FROM` and by means of a join are the same. There is no difference.

| **CDS entity/`FROM`**                                                   | **CDS view entity** | **CDS transactional interface** | \*\* CDS table function\*\* | **CDS hierarchy** | **Static external entity** | **CDS DDIC-based view** | **DDIC database table** | \*\* [DDIC database view](../../abap-glossary/abendatabase_view_glosry.md)\*\* | **DDIC external view** |
|-------------------------------------------------------------------------|---------------------|---------------------------------|-----------------------------|-------------------|----------------------------|-------------------------|-------------------------|--------------------------------------------------------------|------------------------|
| **[CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md)**                      | x                   | \-                              | x                           | x                 | x                          | x                       | x                       | \-                                                           | \-                     |
| **[CDS transactional query](../../abap-glossary/abencds_transactional_pv_glosry.md)**     | x                   | x                               | \-                          | \-                | \-                         | x                       | \-                      | \-                                                           | \-                     |
| **[CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md)**  | x                   | \-                              | \-                          | \-                | \-                         | x                       | \-                      | \-                                                           | \-                     |
| **[CDS analytical projection view](../../abap-glossary/abencds_analytical_pv_glosry.md)** | x                   | \-                              | \-                          | \-                | \-                         | x                       | \-                      | \-                                                           | \-                     |
| **[CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md)**                      | x                   | \-                              | \-                          | \-                | \-                         | x                       | \-                      | \-                                                           | \-                     |
| **[CDS DDIC-based view](../../abap-glossary/abencds_v1_view_glosry.md)**                  | x                   | \-                              | x                           | x                 | \-                         | x                       | x                       | x                                                            | x                      |

- [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md), [CDS custom entities](../../abap-glossary/abencds_custom_entity_glosry.md), and [CDS abstract entities](../../abap-glossary/abencds_abstract_entity_glosry.md) do not specify any data source. They do not have a `FROM` clause.

- CDS custom entities and CDS abstract entities cannot be used as data source of another CDS entity.

- [CDS projection views](../../abap-glossary/abencds_projection_view_glosry.md) can generally not be used as data source of another CDS entity. There is only one exception: A projection view of type [transactional query](../../abap-glossary/abencds_transactional_pv_glosry.md) can have a projection view of type [transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md) as data source.

- CDS projection views can have CDS view entities or CDS DDIC-based views (obsolete) as data source. This applies to all [provider contracts](abencds_pv_provider_contract.md). There are some special rules for certain provider contracts:

  - For CDS transactional interfaces and CDS transactional queries, the data source must be part of a [RAP business object](../../abap-glossary/abenrap_bo_glosry.md). This means it must either be a [CDS root entity](../../abap-glossary/abenroot_entity_glosry.md) itself, or be part of a [CDS composition tree](../../abap-glossary/abencds_composition_tree_glosry.md) which includes a root node.

  - For projection views of provider contract [`ANALYTICAL_QUERY`](abencds_analytical_query_apv.md), the data source must be an [analytical cube view](../../abap-glossary/abencds_analytical_cube_glosry.md) or an [analytical dimension view](../../abap-glossary/abencds_anal_dim_view_glosry.md).

## Association Targets of CDS Associations

The following table lists all CDS entities that can define CDS associations and shows which other entities they accept as association target.

**Note:** The table is only about *defining* associations and not about exposing associations.

| **CDS entity/association target** | **CDS table entity** | **CDS view entity** | **CDS projection view** | \*\* CDS table function\*\* | **Static external entity** | **CDS hierarchy** | **CDS custom entity** | **CDS abstract entity** | **CDS DDIC-based view** | **DDIC database table** | \*\* [DDIC database view](../../abap-glossary/abendatabase_view_glosry.md)\*\* | **DDIC external view** |
|-----------------------------------|----------------------|---------------------|-------------------------|-----------------------------|----------------------------|-------------------|-----------------------|-------------------------|-------------------------|-------------------------|--------------------------------------------------------------|------------------------|
| **CDS table entity**              | x                    | \-                  | \-                      | \-                          | x                          | \-                | \-                    | \-                      | \-                      | \-                      | \-                                                           | \-                     |
| **CDS view entity**               | \-                   | x                   | x                       | x                           | x                          | x                 | x                     | x                       | x                       | x                       | \-                                                           | \-                     |
| **CDS transactional query**       | \-                   | x                   | x                       | x                           | x                          | x                 | x                     | x                       | x                       | x                       | \-                                                           | \-                     |
| **CDS custom entity**             | \-                   | x                   | \-                      | x                           | x                          | x                 | x                     | x                       | x                       | x                       | x                                                            | \-                     |
| **CDS abstract entity**           | \-                   | x                   | \-                      | x                           | x                          | x                 | x                     | x                       | x                       | x                       | x                                                            | \-                     |
| **CDS DDIC-based view**           | \-                   | x                   | \-                      | x                           | x                          | x                 | x                     | x                       | x                       | x                       | x                                                            | x                      |

- In CDS table functions and CDS hierarchies, associations cannot be specified. Therefore, they are not listed here.

- A CDS entity can define itself as association target. [Self-associations](../../abap-glossary/abenself_association_glosry.md) are generally supported. They are mainly relevant for CDS hierarchies.

- CDS projection views with provider contract `ANALYTICAL_QUERY` and `TRANSACTIONAL_INTERFACE` cannot define associations. This table applies only to CDS projection views of type [`TRANSACTIONAL_QUERY`](abencds_pv_transactional_query.md) and to projection views [without provider contract](abencds_pv_no_contract.md) (not recommended).

## Association Targets of CDS Compositions

The following table lists all CDS entities that can define CDS compositions and shows with which entity they can be connected via a parent-child relationship by means of CDS compositions.

| **CDS entity/composition of or to-parent association** | **CDS table entity** | **CDS view entity** | ,**CDS custom entity** | **CDS abstract entity** | **CDS DDIC-based view** |
|--------------------------------------------------------|----------------------|---------------------|------------------------|-------------------------|-------------------------|
| **CDS table entity**                                   | x                    | \-                  | \-                     | \-                      | \-                      |
| **CDS view entity**                                    | \-                   | x                   | x                      | x                       | x                       |
| **CDS custom entity**                                  | \-                   | x                   | x                      | x                       | x                       |
| **CDS abstract entity**                                | \-                   | x                   | x                      | x                       | x                       |
| **CDS DDIC-based view**                                | \-                   | x                   | x                      | x                       | x                       |

- CDS hierarchies and CDS table functions cannot define CDS composition relations.

- CDS projection views can [expose](abencds_proj_view_expose_assoc.md) and [redirect](abencds_pv_assoc_redirected.md) compositions. The association target of a redirected composition must be another CDS projection view. However, a CDS projection view cannot define any new composition.
