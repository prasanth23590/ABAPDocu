---
title: "ABAP RAP Business Objects"
source_file: abenabap_rap.html
section: "ABAP RAP Business Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP RAP Business Objects

This section of the ABAP keyword documentation describes the syntax and semantics of all language elements of [ABAP RAP](../abap-glossary/abenabap_rap_glosry.md).

A RAP business object (RAP BO) is a [business object (BO)](../abap-glossary/abenbusiness_object_glosry.md) that plays a central role in [ABAP RAP](../abap-glossary/abenabap_rap_glosry.md) by enabling transactional access to data that are described by [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). A business object is not a repository object, but it is made up from the following components and their relations. The RAP behavior definition plays a central role here in bringing the individual components together.

- Data model

  The data modeling of a business object takes place using CDS entities that construct a [CDS composition tree](../abap-glossary/abencds_composition_tree_glosry.md), which is itself defined using [CDS compositions](../abap-glossary/abencds_composition_glosry.md) and [to-parent associations](../abap-glossary/abento_parent_association_glosry.md). The components of a [tree hierarchy](../abap-glossary/abentree_hierarchy_glosry.md) of this type are as follows:

  - [RAP BO root entity](../abap-glossary/abenrap_bo_root_entity_glosry.md):

    Each business object has exactly one root entity. A root entity is a [CDS view](../abap-glossary/abencds_view_glosry.md), a [CDS custom entity](../abap-glossary/abencds_custom_entity_glosry.md), or an [CDS abstract entity](../abap-glossary/abencds_abstract_entity_glosry.md) defined using the addition `ROOT`. The root entity represents the business object. A root entity can have one or more child entities but cannot have a parent entity.

  - [Child entity](../abap-glossary/abenchild_entity_glosry.md)

    [CDS compositions](../abap-glossary/abencds_composition_glosry.md) can be used to define one or more child entities for each CDS entity of a business object. Before a CDS entity can be defined as a child entity, it must contain a [to-parent association](../abap-glossary/abento_parent_association_glosry.md) with the parent entity and expose it.

  - [Parent entity](../abap-glossary/abenparent_entity_glosry.md)

    A CDS entity of a business object that uses [CDS compositions](../abap-glossary/abencds_composition_glosry.md) to define child entities is their parent entity. Each child entity can have exactly one parent entity and the syntax guarantees this by defining and exposing exactly one [to-parent association](../abap-glossary/abento_parent_association_glosry.md) in each child entity.

  - [Leaf entity](../abap-glossary/abenleaf_entity_glosry.md)

    A CDS entity of a business object that is not a parent entity or in which no child entities are defined using [CDS compositions](../abap-glossary/abencds_composition_glosry.md) is a leaf entity.

- Behavior

  The [RAP business object behavior](../abap-glossary/abenrap_bo_behavior_glosry.md) is defined in a [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md) (BDEF). The BDEF defines the main characteristics of a RAP BO and which [CRUD](../abap-glossary/abencrud_glosry.md) operations or other actions it provides. There are two kinds of RAP BOs, managed and unmanaged:

  - For a [managed RAP BO](../abap-glossary/abenmanaged_rap_bo_glosry.md), its behavior is fully or partly provided by the managed RAP BO provider.

  - For an [unmanaged RAP BO](../abap-glossary/abenunmanaged_rap_bo_glosry.md), its behavior must be fully provided by an [ABAP behavior implementation](../abap-glossary/abenbehavior_implement_glosry.md).

    The BDEF also defines the communication between the consumer and the provider of a RAP BO. This communication takes place by using internal tables of so-called [BDEF derived types](../abap-glossary/abenrap_derived_type_glosry.md) that depend on the behavior definition:

  - The [RAP BO provider](../abap-glossary/abenrap_bo_provider_glosry.md) implements methods with parameters that are typed with BDEF derived types.

  - The [RAP BO consumer](../abap-glossary/abenrap_bo_consumer_glosry.md) sends or receives internal tables of BDEF derived types to or from the RAP BO provider.

- RAP business service

  A RAP business service provides access to CDS entities by Web clients from outside an AS ABAP. Such an access can be a pure read access (query) or a transactional request.

  - For read accesses (queries), all accesses from the AS ABAP to the underlying database are encapsulated by the [RAP transactional engine](../abap-glossary/abenrap_transac_engine_glosry.md). Normally, no own ABAP programming is necessary. Only in exceptional cases, special [CDS custom entities](../abap-glossary/abencds_custom_entity_glosry.md) can be used, that are implemented in ABAP classes.

  - For transactional requests, RAP business objects (RAP BOs) are required. In a RAP BO, a behavior is defined by a RAP behavior definition for a CDS entity, that can be exposed by a RAP business service. The behavior is implemented by the managed RAP BO provider or in ABAP behavior implementations.

The main purpose of RAP BOs is to fulfill transactional OData requests from Web clients to the AS ABAP in accordance to the [RESTful](../abap-glossary/abenrestful_glosry.md) paradigm. Besides that, accesses from ABAP programs to RAP BOs of the same AS ABAP are possible by using [ABAP EML](../abap-glossary/abenabap_eml_glosry.md).

The following sections describe [RAP business services](../abap-glossary/abenbusiness_service_glosry.md), the RAP behavior definition language (RAP BDL), and the ABAP statements for RAP.

- [RAP - Business Services (BS)](abencds_business_services.md)

- [RAP - Behavior Definitions](rap-behavior-definitions/abencds_bdef.md)

- [ABAP for RAP Business Objects](abap-for-rap-business-objects/abenabap_for_rap_bos.md)

- [RAP Glossary](abenrap_glossary.md)

More information about ABAP RAP can be found under [ABAP RESTful Programming Model](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/289477a81eec4d4e84c0302fb6835035?version=sap_cross_product_abap).
