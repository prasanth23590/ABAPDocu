---
title: "CDS DDL - DDIC-Based View, SELECT, Associations"
source_file: abencds_association_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, SELECT, Associations

[CDS associations](../../abap-glossary/abencds_association_glosry.md) offer an advanced modelling capability for CDS data models. A CDS association defines a relationship between two [CDS entities](../../abap-glossary/abencds_entity_glosry.md). A CDS association can be used to include fields from the [association target](../../abap-glossary/abenassociation_target_glosry.md) in the current view, and/or it can be published for usage in other CDS entities or in ABAP SQL.

As soon as an association is used in a [path expression](../../abap-glossary/abenpath_expression_glosry.md), for example, to specify a field from the [association target](../../abap-glossary/abenassociation_target_glosry.md) in the element list of a view, it is internally transformed into a [join](../../abap-glossary/abenjoin_glosry.md). So technically, a CDS association is instantiated as join. The benefit of a CDS association compared to a join is that it can be reused in different positions and that it renders the task of coding complex [join expressions](../../abap-glossary/abenjoin_expression_glosry.md) superfluous. Further details about the use cases of CDS associations and by which join type they are represented are explained in the topic below about CDS associations and joins.

[Compositions](../../abap-glossary/abencds_composition_glosry.md) are special kinds of CDS associations. A CDS composition consists of a [CDS to-parent association](../../abap-glossary/abento_parent_association_glosry.md) and a [CDS to-child association](../../abap-glossary/abento_child_association_glosry.md) and it defines an existential dependency of the composition child to its composition parent. For example, a sales order item (composition child) always belongs to a sales order header (composition parent).

For an overview of all possible association targets of all CDS entities that can define associations, see [Data Source Matrix](../abap-cds-data-definitions/abencds_data_source_matrix.md).

For further details, read the following sections:

- [Details on CDS Associations: Use cases and Join types](abencds_assoc_join_v1.md)

- [Association](abencds_simple_association_v1.md)

- [Composition](abencds_composition_v1.md)

- [To-parent Association](abencds_to_parent_assoc_v1.md)
