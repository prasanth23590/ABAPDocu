---
title: "RAP Glossary"
source_file: abenrap_glossary.html
section: "ABAP RAP Business Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP Glossary

RAP stands for the [ABAP RESTful Application Programming Model](../abap-glossary/abenarap_glosry.md). In the following, terms of the [ABAP Glossary](../abap-glossary/abenabap_glossary.md) are listed, that are relevant for RAP.

**ABAP behavior pool**

ABP for short. A special [class pool](../abap-glossary/abenclass_pool_glosry.md) for an [ABAP behavior implementation](../abap-glossary/abenbehavior_implement_glosry.md). A behavior pool is based on a [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md). The name of the [global class](../abap-glossary/abenglobal_class_glosry.md) of a behavior pool is usually prefixed with `BP_` but does not implement the behavior itself. The [behavior implementation](../abap-glossary/abenbehavior_implement_glosry.md) is coded in local [ABP handler classes](../abap-glossary/abenabp_handler_class_glosry.md) and [ABP saver classes](../abap-glossary/abenabp_saver_class_glosry.md) in the [CCIMP include](../abap-glossary/abenccimp_glosry.md) of the behavior pool. These classes implement the [unmanaged RAP BO provider](../abap-glossary/abenunmanaged_rap_bo_prov_glosry.md) that is called by the [RAP runtime engine](../abap-glossary/abenrap_runtime_engine_glosry.md) when the [RAP BO](../abap-glossary/abenrap_bo_glosry.md) is accessed.

**ABAP contract checks**

ABAP contract checks summarize the following checks:

- [RAP BO contract](../abap-glossary/abenrap_bo_contract_glosry.md) checks: Check for violations of [RAP BO consumer](../abap-glossary/abenrap_bo_consumer_glosry.md) and [RAP BO provider](../abap-glossary/abenrap_bo_provider_glosry.md) implementations.

- [Transactional contract](../abap-glossary/abentransactional_contract_glosry.md) checks: Are implemented in the [controlled SAP LUW](../abap-glossary/abencontrolled_sap_luw_glosry.md) concept. Check for transactional consistency violations in a [transactional phase](../abap-glossary/abentr_phase_glosry.md).

**ABAP EML**

*-\>* [ABAP Entity Manipulation Language](../abap-glossary/abenaeml_glosry.md)

**ABAP Entity Manipulation Language**

ABAP EML or EML for short. Subset of ABAP that allows access to [RAP business objects](../abap-glossary/abenrap_bo_glosry.md) in an [ABAP program](../abap-glossary/abenabap_program_glosry.md). When EML statements are executed for a RAP BO, [RAP BO operations](../abap-glossary/abenrap_bo_operation_glosry.md) are called to access the [transactional buffer](../abap-glossary/abentransactional_buffer_glosry.md) of the BO. The communication between EML and the RAP BO consists of sending and receiving internal tables of special [BDEF derived types](../abap-glossary/abenrap_derived_type_glosry.md). ABAP EML can be used in any program to access RAP BOs and especially in the [ABAP behavior pool](../abap-glossary/abenbehavior_pool_glosry.md) in order to access the transactional buffer of the RAP BO.

**ABAP RAP**

*-\>* [ABAP RESTful Application Programming Model (RAP)](../abap-glossary/abenarap_glosry.md)

**ABAP RESTful Application Programming Model**

Also ABAP RESTful Programming Model, ABAP RAP, or RAP for short. ABAP programming model that is [RESTful](../abap-glossary/abenrestful_glosry.md) or that meets the requirements of a [REST](../abap-glossary/abenrest_glosry.md) architecture. In ABAP RAP, [AS ABAP](../abap-glossary/abenas_abap_glosry.md) plays the role of a stateless Web server. [OData](../abap-glossary/abenodata_glosry.md) serves as the RESTful protocol for requests from Web clients and the state of a session can be saved to the [standard database](../abap-glossary/abenstandard_db_glosry.md). The modeling is based on [CDS entities](../abap-glossary/abencds_entity_glosry.md) and [RAP behavior definitions](../abap-glossary/abencds_behavior_definition_glosry.md).

For queries, CDS entities can be directly exposed by [business services](../abap-glossary/abenbusiness_service_glosry.md) and all data can be retrieved by the [RAP query engine](../abap-glossary/abenrap_query_engine_glosry.md). For transactional access to data, the model offers [RAP business objects](../abap-glossary/abenrap_bo_glosry.md), whose behavior is provided by the [managed RAP BO provider](../abap-glossary/abenmanaged_rap_bo_prov_glosry.md), or is implemented in [ABAP behavior implementations](../abap-glossary/abenbehavior_implement_glosry.md).

RAP is the transactional programming model for [ABAP Cloud](../abap-glossary/abenabap_cloud_glosry.md).

**ABP auxiliary class**

A [global class](../abap-glossary/abenglobal_class_glosry.md) that refers to a [RAP BO](../abap-glossary/abenrap_bo_glosry.md) and has extended access rights to the referenced RAP BO. Its primary purpose is to support implementation in an [ABAP behavior pool](../abap-glossary/abenbehavior_pool_glosry.md). This is accomplished by providing reusable methods and allowing developers to concurrently implement [RAP behavior](../abap-glossary/abenrap_behavior_glosry.md).

**abstract BDEF extension**

A development object that extends a [RAP abstract behavior definition](../abap-glossary/abencds_abstract_bdef_glosry.md) using the statement [`extension for abstract`](rap-behavior-definitions/abenbdl_extensibility_abstract.md).

**ancestor association**

An [intra-BO association](../abap-glossary/abencds_intra_bo_assoc_glosry.md) whose [association target](../abap-glossary/abenassociation_target_glosry.md) is a [RAP BO entity](../abap-glossary/abenrap_bo_entity_glosry.md) between the current node and the [RAP BO root entity](../abap-glossary/abenrap_bo_root_entity_glosry.md). The association target must be higher in the hierarchical structure of the RAP composition tree, so it cannot be a sibling node or the [CDS parent entity](../abap-glossary/abenparent_entity_glosry.md) of the current node. An ancestor association is defined using the keyword [`ancestor`](rap-behavior-definitions/abenbdl_ancestor_ext.md). The purpose of ancestor associations is to make it possible to implicitly derive the path to a RAP BO's [authorization master entity](../abap-glossary/abenrap_auth_ma_ent_glosry.md), [lock master entity](../abap-glossary/abenrap_lock_ma_ent_glosry.md), and [ETag master entity](../abap-glossary/abenrap_etag_ma_ent_glosry.md), so the respective entities need not be defined explicitly.

**association implementation type**

Defines the [RAP BO provider](../abap-glossary/abenrap_bo_provider_glosry.md) that implements the [operations for associations](../abap-glossary/abenrap_operation_assoc_glosry.md). The association implementation types available are `managed` and `unmanaged`.

**base BDEF**

Synonym for projected BDEF. [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md) that serves as a basis for projections. It can be of [BDEF implementation type](../abap-glossary/abencds_bdef_impl_type_glosry.md) [managed](../abap-glossary/abenmanaged_rap_bo_glosry.md) or [unmanaged](../abap-glossary/abenunmanaged_rap_bo_glosry.md).

**base BDEF extension**

A development object that extends a [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md) of type [`managed`](../abap-glossary/abenmanaged_rap_bo_glosry.md) or [`unmanaged`](../abap-glossary/abenunmanaged_rap_bo_glosry.md) using the statement [`extension`](rap-behavior-definitions/abenbdl_extension_syntax.md).

**BDEF alternative key**

A user-defined BDEF key. User-defined BDEF keys exist in addition to the [primary key](../abap-glossary/abenprimary_key_glosry.md) of the underlying CDS data model and to the predefined [secondary table keys](../abap-glossary/abensecondary_table_key_glosry.md) for [BDEF derived types](../abap-glossary/abenrap_derived_type_glosry.md). There are two types of BDEF alternative keys:

- [BDEF pure key](../abap-glossary/abenrap_pure_key_glosry.md)

- [BDEF secondary key](../abap-glossary/abenrap_secondary_key_glosry.md)

BDEF alternative keys are used, for example, to define the signature of a [RAP key function](../abap-glossary/abenrap_key_function_glosry.md).

**BDEF derived type**

The type of an internal table or structure that is derived by the [RAP framework](../abap-glossary/abenrap_framework_glosry.md) from the [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md). Such internal tables and structures are used for the communication between [RAP BO consumers](../abap-glossary/abenrap_bo_consumer_glosry.md) and [RAP BO providers](../abap-glossary/abenrap_bo_provider_glosry.md). For that, the parameters of a method that implements [RAP BO behavior](../abap-glossary/abenrap_bo_behavior_glosry.md) are typed with BDEF derived types. In [ABAP programs](../abap-glossary/abenabap_program_glosry.md), BDEF derived types can be used to declare internal tables or structures to be passed to parameters of [RAP handler](../abap-glossary/abenabp_handler_class_glosry.md) and [saver classes](../abap-glossary/abenabp_saver_method_glosry.md).

**BDEF extension**

A [repository object](../abap-glossary/abenrepository_object_glosry.md) that extends a [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md).

There are the following types of BDEF extensions:

- [base BDEF extensions](../abap-glossary/abenrap_base_bdef_ext_glosry.md)

- [BDEF projection extensions](../abap-glossary/abenrap_projec_bdef_ext_glosry.md)

- [abstract BDEF extensions](../abap-glossary/abenrap_abs_bdef_ext_glosry.md)

It is possible to extend a BDEF extension with further BDEF extensions. This is referred to as [extension layering](../abap-glossary/abenrap_ext_layering_glosry.md).

**BDEF extension header**

The part of a [BDEF extension](../abap-glossary/abenrap_extension_glosry.md) that includes the first one to three lines of [BDL source code](../abap-glossary/abenbdl_source_code_glosry.md). It starts with&#x00A0; [`extension`](rap-behavior-definitions/abenbdl_extensibility_managed_unm.md) and may additionally define an implementation class and enable BDEF privileged mode.

**BDEF friend**

A BDEF friend is a [BDEF extension](../abap-glossary/abenrap_extension_glosry.md) whose implementation has unrestricted access to all components of the original [BDEF](../abap-glossary/abencds_behavior_definition_glosry.md). For example, a BDEF friend can call [internal RAP BO operations](../abap-glossary/abenrap_internal_operation_glosry.md) and read or modify RAP BO entities [`IN LOCAL MODE`](abap-for-rap-business-objects/abapin_local_mode.md). A BDEF friend is declared using the optional addition [`with friends`](rap-behavior-definitions/abenbdl_with_friends.md). BDEF friends can be used for modularization purposes.

**BDEF implementation type**

Type of [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md). There are five different implementation types of behavior definitions:

- [managed](../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [unmanaged](../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- [interface](../abap-glossary/abencds_interface_bdef_glosry.md)

- [projection](../abap-glossary/abenrap_projection_bo_glosry.md)

- [abstract](../abap-glossary/abencds_abstract_bdef_glosry.md)

The differences are, for example, the type of underlying [CDS entity](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_view_entity.md) and the degree of standardized vs. customized behavior implementation.

**BDEF privileged mode**

With BDEF privileged mode, [RAP BO consumers](../abap-glossary/abenrap_bo_consumer_glosry.md) can circumvent [authorization checks](../abap-glossary/abenauthorization_check_glosry.md), such as&#x00A0; [RAP authorization control](../abap-glossary/abenrap_auth_control_glosry.md). BDEF privileged mode is prerequisite to use the addition [`PRIVILEGED`](abap-for-rap-business-objects/abapeml_privileged.md) in [EML](../abap-glossary/abeneml_glosry.md) when consuming the [RAP BO](../abap-glossary/abenrap_bo_glosry.md).&#x00A0;&#x00A0;

**BDEF projection extension**

A development object that extends a [RAP projection behavior definition](../abap-glossary/abencds_proj_bdef_glosry.md) using the statement [`extension for projection`](rap-behavior-definitions/abenbdl_extensibility_projection.md).

**BDEF projection extension header**

The part of a [BDEF projection extension](../abap-glossary/abenrap_projec_bdef_ext_glosry.md) that starts with&#x00A0; [`extension for projection`](rap-behavior-definitions/abenbdl_extension_for_projection.md).

**BDEF pure key**

A [BDEF alternative key](../abap-glossary/abenrap_alternative_key_glosry.md) defined using [`define pure key`](rap-behavior-definitions/abenbdl_define_key.md).

**BDEF secondary key**

A [BDEF alternative key](../abap-glossary/abenrap_alternative_key_glosry.md) defined using [`define secondary key`](rap-behavior-definitions/abenbdl_define_key.md).

**BDEF strict mode**

BDEF strict mode applies additional syntax checks to [RAP behavior definitions](../abap-glossary/abencds_behavior_definition_glosry.md). It ensures, for example, that no outdated syntax is used, implicitly available operations are declared explicitly, and that a RAP BO complies to best practices. BDEF strict mode is continually enhanced with stricter versions that apply additional checks.

**BDL source code**

The source code for [RAP behavior definitions](../abap-glossary/abencds_behavior_definition_glosry.md) in [RAP BDL](../abap-glossary/abencds_bdl_glosry.md).

**BOPF-based RAP business object**

BOPF-based RAP BO for short. A BOPF-based RAP BO is the result of the migration of a [CDS-based BOPF business object](../abap-glossary/abencds_bopf_bo_glosry.md) to a RAP business object. Special syntax statements for BOPF-based RAP BOs are `managed by BOPF` and `with BOPF draft`. The [transactional buffer](../abap-glossary/abentransactional_buffer_glosry.md) of a BOPF-based RAP BO is provided by the [BOPF-managed RAP BO provider](../abap-glossary/abenbopf_man_rap_bo_prov_glosry.md). BOPF-based RAP BOs that are [draft-enabled](../abap-glossary/abendraft_rap_bo_glosry.md) are handled by the [BOPF-managed RAP draft provider](../abap-glossary/abenbopf_man_rap_dra_prov_glosry.md).

**BOPF-managed RAP BO provider**

The part of the [RAP BO provider](../abap-glossary/abenrap_bo_provider_glosry.md) that provides the [transactional buffer](../abap-glossary/abentransactional_buffer_glosry.md) for [BOPF-based RAP BOs](../abap-glossary/abenrap_bopf_bo_glosry.md).

**BOPF-managed RAP draft provider**

The draft provider of [BOPF-based RAP BOs](../abap-glossary/abenrap_bopf_bo_glosry.md) with BOPF-managed draft. The [draft handling](../abap-glossary/abenrap_draft_handling_glosry.md) is managed by the [Business Object Processing Framework](../abap-glossary/abenbo_processing_fw_glosry.md) (BOPF).

**CCIMP include**

An [include program](../abap-glossary/abeninclude_program_glosry.md) of a [class pool](../abap-glossary/abenclass_pool_glosry.md) that is included behind the [declaration part](../abap-glossary/abendeclaration_part_glosry.md) and in front of the [implementation part](../abap-glossary/abenimplementation_part_glosry.md) of the [global class](../abap-glossary/abenglobal_class_glosry.md). It can be edited in the Class Builder by navigating to *Local Definitions/Implementations* and in [ADT](../abap-glossary/abenadt_glosry.md) by navigating to *Local Types*. The internal name of the include program ends with `CCIMP`. See also [CCDEF include](../abap-glossary/abenccdef_glosry.md).

**CDS parent entity**

A [CDS entity](../abap-glossary/abencds_entity_glosry.md) of a [CDS composition tree](../abap-glossary/abencds_composition_tree_glosry.md) that uses a [to-child association](../abap-glossary/abento_child_association_glosry.md) to define a [child entity](../abap-glossary/abenchild_entity_glosry.md). A parent entity can have multiple child entities. Each child entity must define and expose a [to-parent association](../abap-glossary/abento_parent_association_glosry.md) to its parent entity.

**CDS root entity**

The top [CDS entity](../abap-glossary/abencds_entity_glosry.md) of a [CDS composition tree](../abap-glossary/abencds_composition_tree_glosry.md). The addition `ROOT` must be specified in the definition of a root entity with [CDS DDL](../abap-glossary/abencds_ddl_glosry.md). A root entity can be part of exactly one [RAP BO](../abap-glossary/abenrap_bo_glosry.md). A CDS root entity is typically a [CDS parent entity](../abap-glossary/abenparent_entity_glosry.md) and it is typically used as a [RAP BO root entity](../abap-glossary/abenrap_bo_root_entity_glosry.md) in the context of the [ABAP RESTful Application Programming Model](../abap-glossary/abenarap_glosry.md).

**CDS SDL**

The Service Definition Language of [ABAP CDS](../abap-glossary/abenabap_cds_glosry.md). CDS SDL contains language elements for [CDS service definitions](../abap-glossary/abencds_service_definition_glosry.md) in [`SDL` source code](../abap-glossary/abensdl_source_code_glosry.md).

**CDS service definition extension**

A transportable extension of a [CDS service definition](../abap-glossary/abencds_service_definition_glosry.md) using the [CDS SDL](../abap-glossary/abencds_sdl_glosry.md) statement [`EXTEND SERVICE`](../abap-core-data-services-abap-cds/abap-cds-service-definitions/abensrvd_extend_service.md). A CDS service definition extension can add further entities to an existing CDS service definition without modifying the original service definition.

**CDS virtual element**

An element in the element list of a [CDS DDL aspect](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_ddl_aspect_glosry.md) or a [projection view](../abap-glossary/abencds_projection_view_glosry.md). In projection views, this element is not included in the [projected entity](../abap-glossary/abencds_pv_projected_entity_glosry.md). Virtual elements are not persistent on the database, but calculated during runtime, usually in [ABAP classes](../abap-glossary/abenclass_glosry.md). In order to fill and analyze the virtual elements of a projection view, special frameworks like the [RAP query engine](../abap-glossary/abenrap_query_engine_glosry.md) have to be involved.

**CDS-based BOPF business object**

CDS-based BOPF BO for short. A [business object](../abap-glossary/abenbusiness_object_glosry.md) in the context of the [Business Object Processing Framework](../abap-glossary/abenbo_processing_fw_glosry.md) (BOPF). Built with the [ABAP programming model for SAP Fiori](../abap-glossary/abenabap_pm_for_fiori_glosry.md).

**change document object**

A part of the [SAP Change Document Solution](https://help.sap.com/docs/btp/sap-business-technology-platform/change-document-solution?version=Cloud). A change document object is a [repository object](../abap-glossary/abenrepository_object_glosry.md) responsible for managing the creation of documents for the database tables assigned to it. A change document object supports the logging of changes made to specific database tables that represent a business object in the system.

In a [RAP business object](../abap-glossary/abenrap_bo_glosry.md), a change document object is used to log changes to persisted BO data using [RAP change documents](../abap-glossary/abenrap_change_documents_glosry.md).

**change documents-enabled RAP BO entity**

A [RAP BO entity](../abap-glossary/abenrap_bo_entity_glosry.md) that supports change logging with [RAP change documents](../abap-glossary/abenrap_change_documents_glosry.md). A change documents-enabled RAP BO entity can be either a [change documents master entity](../abap-glossary/abenrap_change_doc_master_glosry.md) or a [change documents dependent entity](../abap-glossary/abenrap_change_doc_dpndnt_glosry.md)

**controlled SAP LUW**

An extension of the [SAP LUW](../abap-glossary/abensap_luw_glosry.md) concept. The controlled SAP LUW introduces a checking mechanism to detect transactional consistency violations. The controlled SAP LUW is automatically and implicitly supported by newer ABAP concepts such as [RAP](../abap-glossary/abenrap_glosry.md). In non-RAP transactions, the controlled SAP LUW can be used by explicitly setting transactional phases using the static methods of the [`CL_ABAP_TX`](../abap-programming-language/abap-database-access/abaprap_cl_abap_tx.md) class. In addition, [released APIs](../abap-glossary/abenreleased_api_glosry.md) can have special classifications (starting with [`IF_ABAP_TX...`](../abap-programming-language/abap-database-access/abapapi_classification.md)) that enable specific transactional contracts that are checked in the [transactional phases](../abap-glossary/abentr_phase_glosry.md).

**cross-BO association**

An [association](../abap-glossary/abencds_association_glosry.md) that is not part of a [RAP business object's](../abap-glossary/abenrap_bo_glosry.md) [composition tree](../abap-glossary/abencds_composition_tree_glosry.md), but has an [association target](../abap-glossary/abenassociation_target_glosry.md) that is part of a foreign business object. The opposite of a cross-BO association is an [intra BO association](../abap-glossary/abencds_intra_bo_assoc_glosry.md).

**CRUD operations**

An acronym for Create, Read, Update, and Delete, which are the four basic operations for persistent data storage.

- In [SQL](../abap-glossary/abensql_glosry.md), the four operations are implemented by;

  - [DQL](../abap-glossary/abendql_glosry.md) statements `SELECT`, `WITH`, `OPEN CURSOR` and `FETCH`.

  - [DML](../abap-glossary/abendml_glosry.md) statements `INSERT`, `UPDATE`, and `DELETE`.

- In the [ABAP RESTful Application Programming Model (RAP)](../abap-glossary/abenarap_glosry.md), the four operations can be specified in a [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md) using the [RAP BDL](../abap-glossary/abencds_bdl_glosry.md) syntax elements `create`, `read`, `update`, and `delete`.

**CUD operations**

An acronym for Create, Update, and Delete operations, which are part of the four basic [CRUD](../abap-glossary/abencrud_glosry.md) operations for persistent data storage.

- In [SQL](../abap-glossary/abensql_glosry.md), the three operations are implemented by the [DML](../abap-glossary/abendml_glosry.md) statements `INSERT`, `UPDATE`, and `DELETE`.

- In the [ABAP RESTful Application Programming Model (RAP)](../abap-glossary/abenarap_glosry.md), the three operations are represented by the [RAP modify operations](../abap-glossary/abenrap_modify_operation_glosry.md) [Create](../abap-glossary/abenrap_create_operation_glosry.md), [update](../abap-glossary/abenrap_update_operation_glosry.md), and [delete](../abap-glossary/abenrap_delete_operation_glosry.md) in [RAP BOs](../abap-glossary/abenrap_bo_glosry.md).

**draft-enabled RAP business object**

A [RAP BO](../abap-glossary/abenrap_bo_glosry.md) that supports [RAP draft handling](../abap-glossary/abenrap_draft_handling_glosry.md). A RAP BO is draft-enabled with the RAP BDL syntax addition [`with draft`](rap-behavior-definitions/abenbdl_with_draft.md) or [`with collaborative draft`](rap-behavior-definitions/abenbdl_with_coll_draft.md).

**EML**

*-\>* [ABAP Entity Manipulation Language](../abap-glossary/abenaeml_glosry.md)

**entity behavior body**

A part of an [entity behavior definition](../abap-glossary/abencds_entity_bdef_glosry.md) that is defined within curly brackets. The entity behavior body can include [RAP BO operations](../abap-glossary/abenrap_bo_operation_glosry.md), [validations](../abap-glossary/abenrap_validation_glosry.md), [determinations](../abap-glossary/abenrap_determination_glosry.md), and other elements.

**entity behavior characteristics**

A part of an [entity behavior definition](../abap-glossary/abencds_entity_bdef_glosry.md) that stand after `define behavior for` and before the curly brackets. The entity behavior characteristics define additional properties of a behavior definition on entity level.

**entity behavior definition**

A component of a [CDS behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md) (BDEF). A BDEF consists of a [header part](../abap-glossary/abencds_bdef_header_glosry.md) and at least one entity behavior definition, referring to a [RAP BO root entity](../abap-glossary/abenrap_bo_root_entity_glosry.md). Further entity behavior definitions referring to [child entities](../abap-glossary/abenchild_entity_glosry.md) are optional.

**foreign key association**

*-\>* [source-resolved association](../abap-glossary/abensource_resolved_assoc_glosry.md)

**foreign key RAP business object**

A [RAP business object](../abap-glossary/abenrap_bo_glosry.md) in a cross BO scenario that holds the [primary keys](../abap-glossary/abenprimary_key_glosry.md) or the [`%pid`](abap-for-rap-business-objects/abapderived_types_pid.md) of the associated [non-foreign key BO](../abap-glossary/abenrap_non_foreignkey_bo_glosry.md).

**input help**

A list of values that appears as help for an [input field](../abap-glossary/abeninput_field_glosry.md) on a user interface. Input help is also referred to as value help.

Input or value help is useful when the values for the input field must be taken from a predefined set of values. Depending on the UI technology, input help can appear as a dialog box when users choose an icon in an input field or when users choose the F4 key, for example.

For more information about value help in the ABAP RESTful Application Programming Model, see [*Adding Value Help*](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/d270bf220c3545dfba267bb59ae9dd3d) in the documentation for ABAP RESTful Application Programming Model.

**instance RAP BO operation**

A [RAP BO operation](../abap-glossary/abenrap_bo_operation_glosry.md) that is bound to a [RAP BO entity instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md).

**internal RAP BO operation**

A [RAP BO operation](../abap-glossary/abenrap_bo_operation_glosry.md) that can only be executed by the [RAP BO provider](../abap-glossary/abenrap_bo_provider_glosry.md) of the same [BO](../abap-glossary/abenrap_bo_glosry.md).

**intra-BO association**

A [CDS association](../abap-glossary/abencds_association_glosry.md) that is part of a [RAP business object's](../abap-glossary/abenrap_bo_glosry.md) [composition tree](../abap-glossary/abencds_composition_tree_glosry.md) and has an [association target](../abap-glossary/abenassociation_target_glosry.md) from the same RAP BO. The opposite of an intra-BO association is a [cross-BO association](../abap-glossary/abencds_cross_bo_assoc_glosry.md).

**leaf entity**

A [CDS entity](../abap-glossary/abencds_entity_glosry.md) of a [CDS composition tree](../abap-glossary/abencds_composition_tree_glosry.md) of a [RAP business object](../abap-glossary/abenrap_bo_glosry.md) that does not have any [child entities](../abap-glossary/abenchild_entity_glosry.md). The [root entity](../abap-glossary/abenroot_entity_glosry.md) can also be a leaf entity.

**managed RAP BO provider**

A part of the [RAP BO provider](../abap-glossary/abenrap_bo_provider_glosry.md) that provides [managed transactional buffers](../abap-glossary/abenmanaged_trans_buff_glosry.md) and managed behavior of [managed RAP BOs](../abap-glossary/abenmanaged_rap_bo_glosry.md) based on their [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md).

**managed RAP business object**

Managed RAP BO for short. A provisioning type of the [business object behavior](../abap-glossary/abenrap_bo_behavior_glosry.md) of a [RAP BO](../abap-glossary/abenrap_bo_glosry.md). The [transactional buffer](../abap-glossary/abentransactional_buffer_glosry.md) of a managed RAP BO is provided by the [managed RAP BO provider](../abap-glossary/abenmanaged_rap_bo_prov_glosry.md). The implementation can partly be provided by an [unmanaged RAP BO provider](../abap-glossary/abenunmanaged_rap_bo_prov_glosry.md) in an [ABAP behavior pool](../abap-glossary/abenbehavior_pool_glosry.md).

**managed transactional buffer**

The [transactional buffer](../abap-glossary/abentransactional_buffer_glosry.md) of a [managed RAP BO](../abap-glossary/abenmanaged_rap_bo_glosry.md) that is provided by the [managed RAP BO provider](../abap-glossary/abenmanaged_rap_bo_prov_glosry.md). A managed transactional buffer can be accessed in [ABAP programs](../abap-glossary/abenabap_program_glosry.md) by [ABAP EML](../abap-glossary/abenabap_eml_glosry.md) only.

**mandatory RAP BO field**

A [field](../abap-glossary/abenrap_bo_field_glosry.md) in a [RAP BO](../abap-glossary/abenrap_bo_glosry.md) that is defined as mandatory in the [behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md). A non-initial value must be passed to this field in every create request and it cannot be initialized in a [modify operation](../abap-glossary/abenrap_modify_operation_glosry.md).

**non-foreign key RAP business object**

A [RAP business object](../abap-glossary/abenrap_bo_glosry.md) in a cross BO scenario whose [primary keys](../abap-glossary/abenprimary_key_glosry.md) or the [`%pid`](abap-for-rap-business-objects/abapderived_types_pid.md) are held by the associated [foreign key BO](../abap-glossary/abenrap_foreignkey_bo_glosry.md).

**optimistic concurrency control**

Optimistic [concurrency control](../abap-glossary/abenrap_conc_control_glosry.md) enables transactional access to data by multiple users while avoiding inconsistencies by unintentional changes of already modified data. In [RAP](../abap-glossary/abenrap_glosry.md) this is ensured by using an [ETag field](rap-behavior-definitions/abenbdl_etag.md) in the [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md).

**payload**

In communications technology, *payload* is the term used to describe the data that is transported in a data packet during communication between two partners that does not contain any control or protocol information. Payload data includes voice, text, characters, images, and sounds.

In the context of [RAP business events](../abap-glossary/abenrap_entity_event_glosry.md), the payload is the data that is passed from the sender to the event consumers. The payload of a RAP business event is defined using an [output parameter](../abap-glossary/abenoutput_parameter_glosry.md).

**pessimistic concurrency control**

Pessimistic [concurrency control](../abap-glossary/abenrap_conc_control_glosry.md) prevents simultaneous modification access to data on the database by more than one user. In [RAP](../abap-glossary/abenrap_glosry.md) this is ensured by the [RAP locking mechanism](../abap-glossary/abenrap_locking_glosry.md).

**prefix extension**

A prefix that is used in the context of [RAP BO extensions](../abap-glossary/abenrap_bo_extension_glosry.md) to refer to an element or [repository object](../abap-glossary/abenrepository_object_glosry.md) from a RAP BO extension. Examples: extension behavior, extension node, extension field.

**RAP**

*-\>* [ABAP RESTful Application Programming Model](../abap-glossary/abenarap_glosry.md)

**RAP abstract behavior definition**

RAP abstract BDEF or abstract BDEF for short. A RAP abstract behavior definition is a [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md) of [implementation type](../abap-glossary/abencds_bdef_impl_type_glosry.md) abstract. It is based on a [CDS abstract entity](../abap-glossary/abencds_abstract_entity_glosry.md) and it mainly serves as typing mechanism for deep action or function parameters.

**RAP action**

A [RAP BO non-standard operation](../abap-glossary/abenrap_nstandard_operation_glosry.md) that modifies the state of a [RAP BO entity instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md).

There are different types or RAP actions:

- [RAP factory actions](../abap-glossary/abenrap_factory_action_glosry.md)

- [RAP non-factory actions](../abap-glossary/abenrap_non_fac_action_glosry.md)

**RAP active instance**

A [RAP BO entity instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md) in a [draft-enabled RAP business object](../abap-glossary/abendraft_rap_bo_glosry.md) for which a commit triggers the saving to the [persistent table](../abap-glossary/abenrap_persistent_table_glosry.md). The [BDEF derived type](../abap-glossary/abenrap_derived_type_glosry.md) of such an instance has the [draft indicator](../abap-glossary/abenrap_draft_indicator_glosry.md) set to *false*. An active instance can be produced by a [create operation](../abap-glossary/abenrap_create_operation_glosry.md) or by the [draft action](../abap-glossary/abenrap_bo_draft_action_glosry.md) `Activate` in draft scenarios.

**RAP additional save**

The save logic which can be added to [managed RAP BOs](../abap-glossary/abenmanaged_rap_bo_glosry.md) to enhance the default [save sequence](../abap-glossary/abenrap_save_seq_glosry.md). It can be applied to the complete [BO](../abap-glossary/abenrap_bo_glosry.md) by defining it in the [behavior definition header](../abap-glossary/abencds_bdef_header_glosry.md), or for an individual entity by defining it in the [behavior entity characteristics](../abap-glossary/abencds_entity_properties_glosry.md). It is implemented in the redefined [saver method](../abap-glossary/abenabp_saver_method_glosry.md) `save_modified`.

**RAP analytical table**

A kind of data visualization on a SAP Fiori UI that contains a set of structured data and provides several possibilities for aggregating the data. It allows analytical evaluations in applications built with the [ABAP RESTful Application Programming Model](../abap-glossary/abenarap_glosry.md). The modeling is based on [CDS views](../abap-glossary/abencds_view_glosry.md) annotated with [`@OData.applySupportedForAggregation: #FULL`](../abap-core-data-services-abap-cds/abap-cds-annotations/abencds_626623472_anno.md).

**RAP authorization context**

A container for [authorization objects](../abap-glossary/abenauthorization_object_glosry.md) that lists one or more authorization objects. There are different types of authorization contexts:

- [Full authorization context](../abap-glossary/abencds_own_ac_glosry.md)

- [Authorization context for disable](../abap-glossary/abencds_auth_context_glosry.md)

Optional component of a [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md).

**RAP authorization context for disable**

A [RAP authorization context](../abap-glossary/abencds_auth_con_glosry.md) that lists [authorization objects](../abap-glossary/abenauthorization_object_glosry.md) which can be skipped if the authorization context for disable in question is activated.

**RAP authorization control**

An access restriction that protects a [RAP BO](../abap-glossary/abenrap_bo_glosry.md) against unauthorized access to data. It limits access to data or the permission to perform [operations](../abap-glossary/abenrap_bo_operation_glosry.md). Authorization control can be global or instance or both.

- Global authorization is independent of individual [instances](../abap-glossary/abenrap_bo_instance_glosry.md).

- Instance authorization is dependent on the state of an [entity instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md).

**RAP authorization dependent entity**

A [RAP BO entity](../abap-glossary/abenrap_bo_entity_glosry.md) that uses the [authorization control](../abap-glossary/abenrap_auth_control_glosry.md) that is defined on its [authorization master entity](../abap-glossary/abenrap_auth_ma_ent_glosry.md). It delegates authorization requests to the implementation of the [authorization master entity](../abap-glossary/abenrap_auth_ma_ent_glosry.md).&#x00A0;

**RAP authorization master entity**

A [RAP BO entity](../abap-glossary/abenrap_bo_entity_glosry.md) that has its own authorization implementation. The implementation is used when requesting access to the authorization master entity or to any of its [authorization dependent entities](../abap-glossary/abenrap_auth_dep_ent_glosry.md).

**RAP base BO**

A [RAP business object](../abap-glossary/abenrap_bo_glosry.md) that is used as a basis of a [RAP projection BO](../abap-glossary/abenrap_projection_bo_glosry.md). It can be of [BDEF implementation type](../abap-glossary/abencds_bdef_impl_type_glosry.md) [managed](../abap-glossary/abenmanaged_rap_bo_glosry.md) or [unmanaged](../abap-glossary/abenunmanaged_rap_bo_glosry.md).

**RAP BDL**

Behavior Definition Language in ABAP RAP. The RAP BDL contains language elements for [RAP behavior definitions](../abap-glossary/abencds_behavior_definition_glosry.md) in [BDL source code](../abap-glossary/abenbdl_source_code_glosry.md).

**RAP behavior**

The part of a [RAP BO](../abap-glossary/abenrap_bo_glosry.md) that describes the abilities of the RAP BO in question. It is defined in a [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md) and implemented in the [RAP behavior implementation](../abap-glossary/abenbehavior_implement_glosry.md).

**RAP behavior definition**

RAP BDEF or BDEF for short. A RAP behavior definition describes a [RAP business object (RAP BO)](../abap-glossary/abenrap_bo_glosry.md) by defining its behavior for all its [BO entities](../abap-glossary/abenrap_bo_entity_glosry.md). A BDEF is written in [BDL source code](../abap-glossary/abenbdl_source_code_glosry.md) using language elements in [RAP BDL](../abap-glossary/abencds_bdl_glosry.md).

**RAP behavior definition header**

BDEF header short. A BDEF header is the part of a [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md) that defines the [implementation type](../abap-glossary/abencds_bdef_impl_type_glosry.md) and some global attributes that apply to the complete [business object](../abap-glossary/abenbusiness_object_glosry.md). It is the topmost part and includes all statements that are listed before the [entity behavior definition](../abap-glossary/abencds_entity_bdef_glosry.md), `define behavior for`.

**RAP Behavior Definition Language**

*-\>* [RAP BDL](../abap-glossary/abencds_bdl_glosry.md)

**RAP behavior extension body**

A part of an [entity behavior extension](../abap-glossary/abenrap_behavior_extension_glosry.md) that is defined within curly brackets after the statement [`extend behavior for`](rap-behavior-definitions/abenbdl_extend_beh.md). The entity behavior extension body can define [new extension elements](rap-behavior-definitions/abenbdl_new_elem_ext.md), such as extension determinations, extension validations, and extension actions. It may also [extend existing elements](rap-behavior-definitions/abenbdl_ext_elem_ext.md), such as RAP type mapping, and determine actions.

**RAP behavior implementation**

A RAP behavior implementation implements the [unmanaged RAP BO provider](../abap-glossary/abenunmanaged_rap_bo_prov_glosry.md). The implementation takes place in local classes of an [ABAP behavior pool (ABP)](../abap-glossary/abenbehavior_pool_glosry.md).

**RAP BO augmentation**

A [RAP BO operation](../abap-glossary/abenrap_bo_operation_glosry.md) addition that must be implemented by an [ABP handler method](../abap-glossary/abenabp_handler_method_glosry.md). Augmentation is defined in the [projection behavior definition](../abap-glossary/abencds_proj_bdef_glosry.md) for [RAP standard operations](../abap-glossary/abenrap_standard_operation_glosry.md).

The implementation is called when a [modify request](../abap-glossary/abenrap_modify_operation_glosry.md) reaches the [business object projection](../abap-glossary/abenrap_projection_bo_glosry.md) to add data to the request before it is passed to the corresponding handler of the [projected business object](../abap-glossary/abenrap_projected_bo_glosry.md).

**RAP BO consumer**

A piece of software that consumes the implementation of a [RAP BO](../abap-glossary/abenrap_bo_glosry.md). A RAP BO consumer is either the [RAP transactional engine](../abap-glossary/abenrap_transac_engine_glosry.md) that handles requests from outside the [AS ABAP](../abap-glossary/abenas_abap_glosry.md) or an [ABAP program](../abap-glossary/abenabap_program_glosry.md) using [ABAP EML](../abap-glossary/abenabap_eml_glosry.md).

**RAP BO contract**

A set of rules for the [RAP BO provider](../abap-glossary/abenrap_bo_provider_glosry.md) and [consumer](../abap-glossary/abenrap_bo_consumer_glosry.md) implementation to ensure consistency and reliability.

**RAP BO determine action**

A [RAP action](../abap-glossary/abenrap_action_glosry.md) that executes [determinations](../abap-glossary/abenrap_determination_glosry.md) and [validations](../abap-glossary/abenrap_validation_glosry.md) on request. The implementation is provided by the [managed RAP BO provider](../abap-glossary/abenmanaged_rap_bo_prov_glosry.md).

**RAP BO draft action**

A [RAP action](../abap-glossary/abenrap_action_glosry.md) that is invoked during the lifecycle of a [draft-enabled RAP BO](../abap-glossary/abendraft_rap_bo_glosry.md) to manage the state of [draft](../abap-glossary/abenrap_draft_instance_glosry.md) and [active instances](../abap-glossary/abenrap_active_instance_glosry.md). The implementation is provided by the [RAP managed draft provider](../abap-glossary/abenrap_man_draft_provider_glosry.md).

**RAP BO entity**

Also RAP BO node. A [CDS entity](../abap-glossary/abencds_entity_glosry.md) for which behavior is defined in a [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md) of a [RAP BO](../abap-glossary/abenrap_bo_glosry.md).

**RAP BO entity instance**

Also RAP BO node instance. A specific data set of a [RAP BO entity](../abap-glossary/abenrap_bo_entity_glosry.md) that is identified by a key. During a [RAP transaction](../abap-glossary/abenrap_luw_glosry.md), a RAP BO entity instance is processed in the [RAP transactional buffer](../abap-glossary/abentransactional_buffer_glosry.md) during the [RAP interaction phase](../abap-glossary/abenrap_int_phase_glosry.md). Then it is saved to the database table during the [save sequence](../abap-glossary/abenrap_save_seq_glosry.md).

**RAP BO extension**

A [repository object](../abap-glossary/abenrepository_object_glosry.md) that extends a [RAP BO](../abap-glossary/abenrap_bo_glosry.md). The following types of RAP BO extensions exist:

- [DDIC extensions](../abap-glossary/abenddic_extension_glosry.md) defined in [DDIC DDL](../abap-glossary/abenddic_dcl_glosry.md)

- [CDS entity extension](../abap-glossary/abencds_entity_extend_glosry.md) in [CDS DDL](../abap-glossary/abencds_ddl_glosry.md).

- [BDEF extensions](../abap-glossary/abenrap_extension_glosry.md) in [RAP BDL](../abap-glossary/abencds_bdl_glosry.md).

- [Service definition extensions](../abap-glossary/abencds_service_def_ext_glosry.md) in [CDS SDL](../abap-glossary/abencds_sdl_glosry.md).

**RAP BO field**

An element of a [RAP BO entity](../abap-glossary/abenrap_bo_entity_glosry.md).

**RAP BO instance**

A specific data set of a [BO composition tree](../abap-glossary/abencds_composition_tree_glosry.md). A BO instance at least consists of one [RAP BO root entity](../abap-glossary/abenrap_bo_root_entity_glosry.md) instance. Furthermore, it includes all [entity instances](../abap-glossary/abenrap_bo_entity_inst_glosry.md) with a compositional relationship to the root entity instance.

**RAP BO instance key component group**

A [component group](../abap-glossary/abencomponent_group_glosry.md) in [BDEF derived types](../abap-glossary/abenrap_derived_type_glosry.md) that contains primary key fields of a [RAP BO instance](../abap-glossary/abenrap_bo_instance_glosry.md): [`%key`](abap-for-rap-business-objects/abapderived_types_key.md), [`%tky`](abap-for-rap-business-objects/abapderived_types_tky.md), [`%pky`](abap-for-rap-business-objects/abapderived_types_pky.md).

**RAP BO interface**

A [RAP business object](../abap-glossary/abenrap_bo_glosry.md) that serves as interface for stable consumption. A RAP BO interface consists of a [CDS transactional interface](../abap-glossary/abencds_trans_interface_glosry.md) and a [RAP interface behavior definition](../abap-glossary/abencds_interface_bdef_glosry.md). A RAP BO interface does not have a runtime handler and cannot specify an implementation class for [ABAP behavior implementation](../abap-glossary/abenbehavior_implement_glosry.md). A RAP BO interface can only project behavior from the underlying RAP BO.

**RAP BO interface entity**

A component of a [RAP BO interface](../abap-glossary/abenrap_bo_interface_glosry.md). It describes the part of the [RAP data model](../abap-glossary/abenrap_data_model_glosry.md) that is included in the interface. A RAP BO interface entity is represented by a [CDS projection view](../abap-glossary/abencds_projection_view_glosry.md) with the provider contract [`TRANSACTIONAL_INTERFACE`](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_pv_provider_contract.md).

**RAP BO non-standard operation**

A [RAP BO operation](../abap-glossary/abenrap_bo_operation_glosry.md) that does not provide canonical transactional behavior for a [RAP BO](../abap-glossary/abenrap_bo_glosry.md), for example [actions](../abap-glossary/abenrap_action_glosry.md) and [functions](../abap-glossary/abenrap_function_glosry.md). Most non-standard operations must be implemented in the [ABAP behavior pool](../abap-glossary/abenbehavior_pool_glosry.md).

**RAP BO operation**

An operation of a [RAP BO](../abap-glossary/abenrap_bo_glosry.md). RAP BO operations are [CRUD](../abap-glossary/abencrud_glosry.md) operations, [non-standard operations](../abap-glossary/abenrap_nstandard_operation_glosry.md), the [lock operation](../abap-glossary/abenlock_operation_glosry.md), and [operations for associations](../abap-glossary/abenrap_operation_assoc_glosry.md). The implementation of a RAP BO operation implements the [RAP BO behavior](../abap-glossary/abenrap_bo_behavior_glosry.md) by accessing the [transactional buffer](../abap-glossary/abentransactional_buffer_glosry.md). A RAP BO can be accessed by using RAP operations. The parameters of a RAP BO method are mainly typed with special [BDEF derived types](../abap-glossary/abenrap_derived_type_glosry.md).

**RAP BO precheck**

A [RAP BO operation](../abap-glossary/abenrap_bo_operation_glosry.md) addition that must be implemented by a [RAP handler method](../abap-glossary/abenabp_handler_method_glosry.md). A precheck is defined for operations in the [behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md) of a base business object or in the [projection business object](../abap-glossary/abenrap_projection_bo_glosry.md).

The implementation method is called before a modify request is executed on the [transactional buffer](../abap-glossary/abentransactional_buffer_glosry.md) to prevent unwanted changes from reaching the transactional buffer.

**RAP BO provider**

A piece of software that provides the [transactional buffer](../abap-glossary/abentransactional_buffer_glosry.md) and the implementation of a [RAP BO](../abap-glossary/abenrap_bo_glosry.md) based on its [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md).

- A [managed RAP BO](../abap-glossary/abenmanaged_rap_bo_glosry.md) is provided fully or partly by the [managed RAP BO provider](../abap-glossary/abenmanaged_rap_bo_prov_glosry.md).

- An [unmanaged RAP BO](../abap-glossary/abenunmanaged_rap_bo_glosry.md) is fully provided by the [unmanaged RAP BO provider](../abap-glossary/abenunmanaged_rap_bo_prov_glosry.md).

- The draft data of a [draft-enabled RAP business object](../abap-glossary/abendraft_rap_bo_glosry.md) is provided by the [managed](../abap-glossary/abenrap_man_draft_provider_glosry.md) or [unmanaged draft provider](../abap-glossary/abenrap_un_draft_provider_glosry.md).

- A [BOPF-based RAP BO](../abap-glossary/abenrap_bopf_bo_glosry.md) is provided by the [BOPF-managed RAP BO provider](../abap-glossary/abenbopf_man_rap_bo_prov_glosry.md).

**RAP BO root entity**

A [RAP BO entity](../abap-glossary/abenrap_bo_entity_glosry.md) that defines the behavior of a [CDS root entity](../abap-glossary/abenroot_entity_glosry.md). The RAP BO root entity is the top-most entity of the hierarchical structure of a [RAP business object](../abap-glossary/abenrap_bo_glosry.md) and it represents the RAP business object.

**RAP BO service projection**

A RAP BO projection for a [RAP business service](../abap-glossary/abenbusiness_service_glosry.md). A service projection consists of a [CDS transactional query](../abap-glossary/abencds_transactional_pv_glosry.md) and a [RAP projection behavior definition](../abap-glossary/abencds_proj_bdef_glosry.md).

**RAP BO service projection entity**

A component of a [RAP BO service projection](../abap-glossary/abenrap_bo_service_proj_glosry.md). It describes the [RAP data model](../abap-glossary/abenrap_data_model_glosry.md) that is included in the service projection. The RAP BO service projection entity is represented by a [CDS projection view](../abap-glossary/abencds_projection_view_glosry.md) with the provider contract [`TRANSACTIONAL_QUERY`](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_pv_provider_contract.md).

**RAP BO standard operation**

A [RAP BO operation](../abap-glossary/abenrap_bo_operation_glosry.md) that provides canonical transactional behavior for a [RAP BO](../abap-glossary/abenrap_bo_glosry.md). In a [managed RAP BO](../abap-glossary/abenmanaged_rap_bo_glosry.md), standard operations can be provided by the [managed RAP BO provider](../abap-glossary/abenmanaged_rap_bo_prov_glosry.md).

[Create](../abap-glossary/abenrap_create_operation_glosry.md), [read](../abap-glossary/abenrap_read_operation_glosry.md), [update](../abap-glossary/abenrap_update_operation_glosry.md), [delete](../abap-glossary/abenrap_delete_operation_glosry.md) ([CRUD](../abap-glossary/abencrud_glosry.md)) and [lock](../abap-glossary/abenlock_operation_glosry.md) are standard operations. [Actions](../abap-glossary/abenrap_action_glosry.md) and [functions](../abap-glossary/abenrap_function_glosry.md), in contrast, are [non-standard operations](../abap-glossary/abenrap_nstandard_operation_glosry.md). That means they are application-specific and user-implemented.

**RAP buffer data**

Data on the [RAP transactional buffer](../abap-glossary/abentransactional_buffer_glosry.md) that is either in an active or a draft state.

**RAP business event**

A RAP business event is a business event that usually represents a piece of information about the outcome of a [CUD operation](../abap-glossary/abencud_glosry.md) in the context of a [RAP BO entity](../abap-glossary/abenrap_bo_entity_glosry.md). For example, the creation of a [RAP BO entity instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md) raises a RAP business event. Then, an interested party that has subscribed to this event can consume and process it. The information that is passed (i. e. the [payload](../abap-glossary/abenpayload_glosry.md) of the event) always includes the instance key and, if need be, further information like the action (CUD).

[RAP derived events](../abap-glossary/abenrap_derived_event_glosry.md) and [RAP business events for side effects](../abap-glossary/abenrap_side_effct_event_glosry.md) are special types of RAP business events.

**RAP business event for side effects**

A [RAP business event](../abap-glossary/abenrap_entity_event_glosry.md) that is defined with the syntax addition [`for side effects`](rap-behavior-definitions/abenbdl_event_side_effect.md). A RAP business event for side effects is defined to be used exclusively as a trigger for an [event-driven side effect](../abap-glossary/abenrap_event_sideef_glosry.md).

**RAP business object**

RAP BO for short. A [business object](../abap-glossary/abenbusiness_object_glosry.md) in the context of [ABAP RAP](../abap-glossary/abenabap_rap_glosry.md). A RAP BO is mainly described by a [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md) that defines the [RAP business object behavior](../abap-glossary/abenrap_bo_behavior_glosry.md) for a set of special hierarchical [CDS entities](../abap-glossary/abencds_entity_glosry.md) in form of RAP behavior operations and behavior characteristics. A RAP BO has [RAP BO operations](../abap-glossary/abenrap_bo_operation_glosry.md) to handle its data that is available in a [transactional buffer](../abap-glossary/abentransactional_buffer_glosry.md). There are two kinds of RAP BOs:

- [Managed RAP BOs](../abap-glossary/abenmanaged_rap_bo_glosry.md) that are fully or partly provided by the [managed RAP BO provider](../abap-glossary/abenmanaged_rap_bo_prov_glosry.md)

- [Unmanaged RAP BOs](../abap-glossary/abenunmanaged_rap_bo_glosry.md) that are provided by the [unmanaged RAP BO provider](../abap-glossary/abenunmanaged_rap_bo_prov_glosry.md) that is implemented in an [ABAP behavior implementation](../abap-glossary/abenbehavior_implement_glosry.md).

- [BOPF-based RAP business objects](../abap-glossary/abenrap_bopf_bo_glosry.md) that are provided by the [BOPF-managed RAP BO provider](../abap-glossary/abenbopf_man_rap_bo_prov_glosry.md).

A RAP BO can be exposed as a [RAP business service](../abap-glossary/abenbusiness_service_glosry.md) for access from outside [AS ABAP](../abap-glossary/abenas_abap_glosry.md) and is consumed by the [RAP transactional engine](../abap-glossary/abenrap_transac_engine_glosry.md) then. For access to RAP BOs from inside AS ABAP, ABAP contains a subset called [ABAP Entity Manipulation Language (EML)](../abap-glossary/abenaeml_glosry.md).

**RAP business object behavior**

The transactional behavior of a [RAP business object](../abap-glossary/abenrap_bo_glosry.md) that is defined in a [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md).

It includes [entity behavior characteristics](../abap-glossary/abencds_entity_properties_glosry.md), [RAP BO operations](../abap-glossary/abenrap_bo_operation_glosry.md), [validations](../abap-glossary/abenrap_validation_glosry.md), and [determinations](../abap-glossary/abenrap_determination_glosry.md) all of which are either provided by the [managed RAP BO provider](../abap-glossary/abenmanaged_rap_bo_prov_glosry.md) or implemented in the [ABAP behavior pool](../abap-glossary/abenbehavior_pool_glosry.md) ([unmanaged RAP BO provider](../abap-glossary/abenunmanaged_rap_bo_prov_glosry.md)).

**RAP business service**

RAP BS for short. A RAP business service is a [RESTful](../abap-glossary/abenrestful_glosry.md) [business service](../abap-glossary/abenbs_glosry.md) for the consumption of [RAP business objects](../abap-glossary/abenrap_bo_glosry.md). A RAP business service is published with an OData protocol.

**RAP change documents**

An optional part of an [entity behavior definition](../abap-glossary/abencds_entity_bdef_glosry.md) that enables change logging of persisted RAP BO data for a [change documents-enabled RAP BO entity](../abap-glossary/abenrap_change_doc_enabled_glosry.md). When enabled, changes are written to a [change document object](../abap-glossary/abenchange_document_obj_glosry.md). RAP change documents are a [RAP reuse service](../abap-glossary/abenrap_reuse_service_glosry.md).

**RAP change documents dependent entity**

A [change documents-enabled RAP BO entity](../abap-glossary/abenrap_change_doc_enabled_glosry.md) that uses the [change document object](../abap-glossary/abenchange_document_obj_glosry.md) that is defined in its [change documents master entity](../abap-glossary/abenrap_change_doc_master_glosry.md) to log changes to persisted data.

**RAP change documents master entity**

A [change documents-enabled RAP BO entity](../abap-glossary/abenrap_change_doc_enabled_glosry.md) that has its own [change document object](../abap-glossary/abenchange_document_obj_glosry.md) for logging changes to persisted data.

**RAP cleanup phase**

The final phase of the [RAP save sequence](../abap-glossary/abenrap_save_seq_glosry.md) in which the [`cleanup`](abap-for-rap-business-objects/abensaver_method_cleanup.md) [RAP saver method](../abap-glossary/abenabp_saver_method_glosry.md) is called.

**RAP collaborative draft**

A type of [RAP draft handling](../abap-glossary/abenrap_draft_handling_glosry.md) that allows multiple users to work concurrently on the same [draft instance](../abap-glossary/abenrap_draft_instance_glosry.md). All authorized users that have been invited with the [draft action](rap-behavior-definitions/abenbdl_draft_action.md) `Share` can make changes, view updates in real time, and work together on the draft without locking each other out. The creator of the draft instance and all other authorized users are allowed to modify, activate, or discard the draft instance.

**RAP concurrency control**

A concept in [RAP](../abap-glossary/abenrap_glosry.md) that ensures correct results for concurrent operations.

See also:

- [optimistic concurrency control](../abap-glossary/abenoptimistic_conc_control_glosry.md)

- [pessimistic concurrency control](../abap-glossary/abenpessimist_conc_control_glosry.md)

**RAP consumer hint**

A RAP BO field or behavior characteristic that is propagated to the [consumer](../abap-glossary/abenrap_bo_consumer_glosry.md) through the chosen protocol, derived from [RAP feature control](../abap-glossary/abenrap_feature_control_glosry.md) or [authorizations](../abap-glossary/abenrap_auth_control_glosry.md). RAP consumer hints are intended to optimize the usability of the [business service](../abap-glossary/abenbusiness_service_glosry.md). For example, RAP consumer hints can result in fields being marked as [*mandatory*](../abap-glossary/abenmandatory_rap_bo_field_glosry.md) on a UI with an asterisk or in fields being grayed out when they are set to [read-only](../abap-glossary/abenread_only_rap_bo_field_glosry.md).

**RAP content identifier**

A [RAP input identifier](../abap-glossary/abenrap_input_identifier_glosry.md) that uniquely identifies an operation on one [instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md). The content identifier is reflected in the [derived type](../abap-glossary/abenrap_derived_type_glosry.md) component `%cid`. It identifies an instance during the consumption of [static operations](../abap-glossary/abenrap_static_operation_glosry.md) before the instance is identified by an [instance identifier](../abap-glossary/abenrap_inst_identifier_glosry.md).

**RAP copy action**

A [RAP hierarchy action](../abap-glossary/abenrap_hierarchy_action_glosry.md) that determines how a hierarchy node can be duplicated in an editable [treeview](../abap-glossary/abenrap_treeview_glosry.md) scenario. It is useful for creating new hierarchy nodes based on an existing one in an editable treeview scenario. Copy actions are [factory actions](../abap-glossary/abenrap_factory_action_glosry.md), i.e. they offer [`%cid`](abap-for-rap-business-objects/abapderived_types_cid.md) handling for the result instance. Copy actions are user-implemented.

**RAP create operation**

A [RAP modify operation](../abap-glossary/abenrap_modify_operation_glosry.md) that creates new [instances](../abap-glossary/abenrap_bo_entity_inst_glosry.md) of a [RAP BO entity](../abap-glossary/abenrap_bo_entity_glosry.md).

**RAP create-by-association operation**

A [RAP modify operation](../abap-glossary/abenrap_modify_operation_glosry.md) that creates new [instances](../abap-glossary/abenrap_bo_entity_inst_glosry.md) of an associated [business object entity](../abap-glossary/abenrap_bo_entity_glosry.md).

**RAP data model**

A part of a [RAP BO](../abap-glossary/abenrap_bo_glosry.md) that defines the data that is used in the RAP BO. It consists of [RAP BO entities](../abap-glossary/abenrap_bo_entity_glosry.md) that are related by a [CDS composition tree](../abap-glossary/abencds_composition_tree_glosry.md).

**RAP data model extension**

An extension of the data model of a [RAP BO](../abap-glossary/abenrap_bo_glosry.md). May consist of [DDIC extensions](../abap-glossary/abenddic_extension_glosry.md) and [CDS entity extensions](../abap-glossary/abencds_entity_extend_glosry.md).

**RAP default values function**

A [RAP BO operation addition](rap-behavior-definitions/abenbdl_operations_additions.md) that defaults field values or input parameters for [RAP BO operations](../abap-glossary/abenrap_bo_operation_glosry.md) on the user interface. A RAP default values function must be implemented by an [ABP handler method](../abap-glossary/abenabp_handler_method_glosry.md).

**RAP delete operation**

A [RAP modify operation](../abap-glossary/abenrap_modify_operation_glosry.md) that deletes [RAP BO entity instances](../abap-glossary/abenrap_bo_entity_inst_glosry.md).

**RAP dependent BO**

A [RAP BO](../abap-glossary/abenrap_bo_glosry.md) in a [cross-BO scenario](../abap-glossary/abencds_cross_bo_assoc_glosry.md) that delegates [locking](../abap-glossary/abenrap_locking_glosry.md), [permission handling](../abap-glossary/abenauthorization_glosry.md) and [deletion](../abap-glossary/abenrap_delete_operation_glosry.md) to its [host BO](../abap-glossary/abenhost_computer_glosry.md). If associated to a [host BO](../abap-glossary/abenhost_computer_glosry.md), it establishes a [composition-like relationship](../abap-glossary/abencds_composition_glosry.md) to the host. A [dependent object](../abap-glossary/abenrap_bo_entity_glosry.md) uses the syntax `dependent` in the header of the [BDEF](../abap-glossary/abencds_bdef_header_glosry.md).

**RAP dependent draft BO**

A [draft-enabled RAP business object](../abap-glossary/abendraft_rap_bo_glosry.md) in a [cross-BO association](../abap-glossary/abencds_cross_bo_assoc_glosry.md) scenario whose [draft management](../abap-glossary/abenrap_draft_handling_glosry.md) is delegated to the associated principal draft BO. That means that its [instances](../abap-glossary/abeninstance_glosry.md) can only be set to draft if the associated instances of the principal draft BO are set to draft. A dependent draft BO has the header syntax `use draft as dependent` in the [projection view](../abap-glossary/abencds_projection_view_glosry.md) BDEF.

**RAP derived event**

A RAP derived event redefines the [payload](../abap-glossary/abenpayload_glosry.md) of an existing [RAP business event](../abap-glossary/abenrap_entity_event_glosry.md). A RAP derived event is defined with reference to an already implemented event and allows the definition of a payload that deviates from the payload of the referenced event. A derived event is automatically raised when the referenced event is raised. No implementation in an [ABAP behavior pool](../abap-glossary/abenbehavior_pool_glosry.md) is required.

**RAP determination**

An optional part of the [RAP BO behavior](../abap-glossary/abenrap_bo_behavior_glosry.md) that modifies [RAP BO instances](../abap-glossary/abenrap_bo_instance_glosry.md) based on trigger conditions.&#x00A0;

**RAP draft handling**

A concept in RAP that allows the content of the [transactional buffer](../abap-glossary/abentransactional_buffer_glosry.md) to be stored in intermediate storages ([draft tables](../abap-glossary/abendraft_table_glosry.md)) in order to allow transactions to expand over different [ABAP sessions](../abap-glossary/abenabap_session_glosry.md). Introduced by the keyword [`with draft`](rap-behavior-definitions/abenbdl_with_draft.md) or [`with collaborative draft`](rap-behavior-definitions/abenbdl_with_coll_draft.md) in the [behavior definition header](../abap-glossary/abencds_bdef_header_glosry.md) of a [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md).

**RAP draft indicator**

A [BDEF derived type](../abap-glossary/abenrap_derived_type_glosry.md) component that is used to indicate whether a [RAP BO instance](../abap-glossary/abenrap_bo_instance_glosry.md) is a [draft instance](../abap-glossary/abenrap_draft_instance_glosry.md) or an [active instance](../abap-glossary/abenrap_active_instance_glosry.md). It is contained in the component group [`%tky`](abap-for-rap-business-objects/abapderived_types_tky.md) as [`%is_draft`](abap-for-rap-business-objects/abapderived_types_is_draft.md).

**RAP draft instance**

A [RAP BO entity instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md) in a [draft-enabled RAP business object](../abap-glossary/abendraft_rap_bo_glosry.md) for which a commit triggers the saving to the [RAP draft table](../abap-glossary/abendraft_table_glosry.md). The [BDEF derived type](../abap-glossary/abenrap_derived_type_glosry.md) of such an instance has the [draft indicator](../abap-glossary/abenrap_draft_indicator_glosry.md) set to *true*. A draft instance can be produced by a [create operation](../abap-glossary/abenrap_create_operation_glosry.md) ( [new-draft instances](../abap-glossary/abenrap_new_draft_inst_glosry.md)) or by the [draft action](../abap-glossary/abenrap_bo_draft_action_glosry.md) `Edit` ([edit-draft instances](../abap-glossary/abenrap_edit_draft_inst_glosry.md)) in draft scenarios. There are [exclusive draft](../abap-glossary/abenrap_exclusive_draft_glosry.md) instances, where only a single user is allowed to edit a draft, and [collaborative draft](../abap-glossary/abenrap_collaborative_draft_glosry.md) instances, where multiple users can work concurrently on the same draft.

**RAP draft query view**

A [CDS view entity](../abap-glossary/abencds_v2_view_glosry.md) or [CDS DDIC-based view (obsolete)](../abap-glossary/abencds_v1_view_glosry.md) that selects from the [RAP draft table](../abap-glossary/abendraft_table_glosry.md) and contains all fields from the draft table including the administrative fields. It can be specified in a [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md) using the syntax addition&#x00A0; [query](rap-behavior-definitions/abenbdl_draft_query_view.md). A draft query view allows developers to define read access limitations for the draft data of a [draft-enabled RAP business object](../abap-glossary/abendraft_rap_bo_glosry.md) using the CDS data control language [CDS DCL](../abap-glossary/abencds_dcl_glosry.md).

**RAP draft scope**

A feature in [cross-BO scenarios](../abap-glossary/abencds_cross_bo_assoc_glosry.md) that enables consistent [draft management](../abap-glossary/abenrap_draft_handling_glosry.md) between [draft-enabled RAP business objects](../abap-glossary/abendraft_rap_bo_glosry.md). This means that multiple associated [business objects](../abap-glossary/abenbusiness_object_glosry.md) can be edited within a single [logical unit of work](../abap-glossary/abenluw_glosry.md).

**RAP draft table**

A [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) that is generated for a [draft-enabled RAP business object](../abap-glossary/abendraft_rap_bo_glosry.md). It contains draft administrative data that is used for [RAP draft handling](../abap-glossary/abenrap_draft_handling_glosry.md). A draft table should be accessed by the [RAP framework](../abap-glossary/abenrap_framework_glosry.md) only.

**RAP dynamic field characteristic**

A [field characteristic](../abap-glossary/abenrap_field_char_glosry.md) that defines usage restrictions for a [RAP BO field](../abap-glossary/abenrap_bo_field_glosry.md) depending on the state of a [RAP BO entity instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md). For example, a field can be dynamically defined as [read-only](../abap-glossary/abenread_only_rap_bo_field_glosry.md), [mandatory](../abap-glossary/abenmandatory_rap_bo_field_glosry.md), or without restrictions.

**RAP early numbering**

A [numbering](../abap-glossary/abenrap_numbering_glosry.md) concept in which key values are assigned during the [interaction phase](../abap-glossary/abenrap_int_phase_glosry.md).

**RAP early save phase**

The early phase of the [RAP save sequence](../abap-glossary/abenrap_save_seq_glosry.md) that covers the [RAP saver methods](../abap-glossary/abenabp_saver_method_glosry.md) [`finalize`](abap-for-rap-business-objects/abensaver_finalize.md), [`check_before_save`](abap-for-rap-business-objects/abensaver_check_before_save.md) and [`cleanup_finalize`](abap-for-rap-business-objects/abapsaver_class_cleanup_finalize.md) methods.

**RAP edit draft instance**

A [draft instance](../abap-glossary/abenrap_draft_instance_glosry.md) that is produced by the [draft action](../abap-glossary/abenrap_bo_draft_action_glosry.md) `Edit`. For an edit draft instance, there exists a corresponding active instance in parallel.

See also: [RAP new draft instance](../abap-glossary/abenrap_new_draft_inst_glosry.md)

**RAP entity behavior extension**

Short behavior extension. A component of a [BDEF extension](../abap-glossary/abenrap_extension_glosry.md) that extends the behavior of an existing RAP BO entity. An entity behavior extension is defined using [`extend behavior for EntityName`](rap-behavior-definitions/abenbdl_extend_beh.md).

**RAP entity projection extension**

Projection extension for short. A component of a [BDEF projection extension](../abap-glossary/abenrap_projec_bdef_ext_glosry.md) that extends the behavior of an existing RAP BO entity in a [RAP projection behavior definition](../abap-glossary/abencds_proj_bdef_glosry.md). An entity projection extension is defined using [`extend behavior for EntityName`](rap-behavior-definitions/abenbdl_extend_beh_proj.md).

**RAP ETag**

ETag is short for entity tag. A RAP ETag field is a field of a [RAP BO entity](../abap-glossary/abenrap_bo_entity_glosry.md) that is used to describe the state of the instance as an entity tag for [optimistic concurrency control](../abap-glossary/abenoptimistic_conc_control_glosry.md). It is updated on every change of the [RAP BO entity instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md).

**RAP ETag dependent entity**

A [RAP BO entity](../abap-glossary/abenrap_bo_entity_glosry.md) that uses the [ETag](../abap-glossary/abenrap_etag_glosry.md) field of another entity for [optimistic concurrency control](../abap-glossary/abenoptimistic_conc_control_glosry.md). Defined using the keyword [`etag dependent by _Assoc`](rap-behavior-definitions/abenbdl_etag.md).

**RAP ETag master entity**

A [RAP BO entity](../abap-glossary/abenrap_bo_entity_glosry.md) that has its own [ETag](../abap-glossary/abenrap_etag_glosry.md) field defined using the keyword [`etag master MasterField`](rap-behavior-definitions/abenbdl_etag.md).

**RAP event handler class**

The [class pool](../abap-glossary/abenclass_pool_glosry.md) that is used to implement [RAP event handler methods](../abap-glossary/abenrap_event_handler_meth_glosry.md).

**RAP event handler method**

A method that is declared and implemented in the [CCIMP include](../abap-glossary/abenccimp_glosry.md) of a [RAP event handler class](../abap-glossary/abenrap_event_handler_class_glosry.md). It is used to process logic that is implemented in this method when [RAP business events](../abap-glossary/abenrap_entity_event_glosry.md) are raised and consumed locally in the system in which they are raised.

RAP event handler methods are called asynchronously.

**RAP event-driven side effect**

A [RAP side effect](../abap-glossary/abenrap_side_effects_glosry.md) that is triggered by a [business event for side effects](../abap-glossary/abenrap_side_effct_event_glosry.md). The business event in question is defined to be used exclusively for a side effect with the syntax [`event MyEvent for side effects`](rap-behavior-definitions/abenbdl_event.md).

**RAP exclusive draft**

A type of [RAP draft handling](../abap-glossary/abenrap_draft_handling_glosry.md) where [draft instances](../abap-glossary/abenrap_draft_instance_glosry.md) are exclusively locked or reserved for a single user. When a user creates a draft instance, they have exclusive modify access to it, preventing other users from editing the same draft concurrently. The creator of the draft instance is the sole draft instance owner. Only the draft instance owner is allowed to modify, activate, or discard the draft instance.

**RAP extensibility**

Extending a [RAP business object](../abap-glossary/abenrap_bo_glosry.md) with the respective [RAP BO extensions](../abap-glossary/abenrap_bo_extension_glosry.md). Before a RAP BO can be extended, extensions must be technically enabled by means of [RAP extensibility enablement](../abap-glossary/abenrap_ext_enablement_glosry.md). Extensibility use cases include field extensibility, behavior extensibility, and node extensibility.

RAP extensibility is used as part of [developer extensibility](../abap-glossary/abendev_extensibility_glosry.md), available in on-premise and cloud environments. In the context of [ABAP for Cloud Development](../abap-glossary/abenabap_for_cloud_dev_glosry.md), RAP extensibility relies on the [C0 (extend) contract](../abap-glossary/abenc0_contract_glosry.md) to ensure stability at the dedicated extension points.

**RAP extensibility enablement**

Preparing a [RAP business object](../abap-glossary/abenrap_bo_glosry.md) to fulfill all technical requirements for [RAP extensibility](../abap-glossary/abenrap_extensibility_glosry.md). This may include preparing the RAP data model for extensibility by means of extensibility annotations and preparing the [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md) for extensibility by defining dedicated extension points.

**RAP extension entity behavior**

Node extension for short. A component of a [BDEF extension](../abap-glossary/abenrap_extension_glosry.md) that defines the behavior for an extension node. Extension entity behavior is defined using [`define behavior for`](rap-behavior-definitions/abenbdl_define_beh_extend.md).&#x00A0;The extension node must be added to the current RAP BO's data model via [RAP data model extensions](../abap-glossary/abenrap_data_model_ext_glosry.md).

**RAP extension layering**

It is possible to extend a [BDEF extension](../abap-glossary/abenrap_extension_glosry.md) with further BDEF extensions. This is referred to as extension layering. Before a BDEF extension can be extended, extensions must be technically enabled by means of [RAP extensibility enablement](../abap-glossary/abenrap_ext_enablement_glosry.md). Technically, a BDEF extension that extends another extension is a regular extension and the rules for BDEF extensions apply.

**RAP external numbering**

A [numbering concept](../abap-glossary/abenrap_numbering_glosry.md) in which key values are provided by the [RAP BO consumer](../abap-glossary/abenrap_bo_consumer_glosry.md).

**RAP factory action**

A [RAP action](../abap-glossary/abenrap_action_glosry.md) that creates new [RAP BO entity instances](../abap-glossary/abenrap_bo_entity_inst_glosry.md) where you can add functionality to the create process, for example, retrieving BO-specific default values. In contrast to a [non-factory action](../abap-glossary/abenrap_non_fac_action_glosry.md), the [BDEF derived type](../abap-glossary/abenrap_derived_type_glosry.md) of a factory action contains a [`%cid`](abap-for-rap-business-objects/abapderived_types_cid.md) component.

**RAP feature control**

An access restriction that enables or disables [RAP BO operations](../abap-glossary/abenrap_bo_operation_glosry.md) or defines field attributes dynamically for [RAP BO consumers](../abap-glossary/abenrap_bo_consumer_glosry.md). Feature control can be static or dynamic, [instance-based](../abap-glossary/abenrap_ins_feature_control_glosry.md) or [global](../abap-glossary/abenrap_glo_feature_control_glosry.md).

**RAP field characteristic**

A property of a [RAP BO field](../abap-glossary/abenrap_bo_field_glosry.md) that restricts access to the field in question. Field characteristics can be [static](../abap-glossary/abenrap_static_field_char_glosry.md) or [dynamic](../abap-glossary/abenrap_dyn_field_char_glosry.md).

**RAP foreign entity**

A [RAP BO entity](../abap-glossary/abenrap_bo_entity_glosry.md) which is not part of the [BO composition tree](../abap-glossary/abencds_composition_tree_glosry.md) for which it is defined. Defining a foreign entity in the [behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md) enables cross-BO message mapping between the two [BOs](../abap-glossary/abenrap_bo_glosry.md).

**RAP framework**

The framework for the [ABAP RESTful Application Programming Model (RAP)](../abap-glossary/abenrap_glosry.md) on [AS ABAP](../abap-glossary/abenas_abap_glosry.md). It consists of the [RAP runtime engine](../abap-glossary/abenrap_runtime_engine_glosry.md) and the RAP development environment.

**RAP full authorization context**

A [RAP authorization context](../abap-glossary/abencds_auth_con_glosry.md) that serves as a container for [authorization objects](../abap-glossary/abenauthorization_object_glosry.md). Specified using the syntax [`define own authorization context`](rap-behavior-definitions/abenbdl_def_own_auth_context.md). A full authorization context documents the authorization objects used in the implementation of the RAP BO in question.

**RAP function**

A [non-standard RAP BO operation](../abap-glossary/abenrap_nstandard_operation_glosry.md) that returns information without modifying [RAP BO entity instances](../abap-glossary/abenrap_bo_entity_inst_glosry.md).

**RAP global feature control**

A kind of [feature control](../abap-glossary/abenrap_feature_control_glosry.md) that defines access restrictions independently of the state of a [BO entity instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md). Global feature control can be defined for [operations](../abap-glossary/abenrap_bo_operation_glosry.md) only.

**RAP handler class**

A [local class](../abap-glossary/abenlocal_class_glosry.md) in a [CCIMP include](../abap-glossary/abenccimp_glosry.md) of an [ABAP behavior pool (ABP)](../abap-glossary/abenbehavior_pool_glosry.md) for implementing [RAP handler methods](../abap-glossary/abenabp_handler_method_glosry.md) that is executed during the [RAP interaction phase](../abap-glossary/abenrap_int_phase_glosry.md).

**RAP handler method**

A method in a [RAP handler class](../abap-glossary/abenabp_handler_class_glosry.md) of an [ABAP behavior pool](../abap-glossary/abenbehavior_pool_glosry.md) that is called during the [RAP interaction phase](../abap-glossary/abenrap_int_phase_glosry.md). The names of handler methods can be freely chosen except for [draft actions](../abap-glossary/abenrap_bo_draft_action_glosry.md) and [augmentation](../abap-glossary/abenrap_bo_augmentation_glosry.md).

**RAP hierarchy action**

A [RAP action](../abap-glossary/abenrap_action_glosry.md) that can be used in the context of editable [treeviews](../abap-glossary/abenrap_treeview_glosry.md) for performing operations on hierarchical data.

The following types of RAP hierarchy actions are available:

- [RAP copy action](../abap-glossary/abenrap_copy_action_glosry.md)

- [RAP reorder action](../abap-glossary/abenrap_reorder_action_glosry.md)

**RAP host BO**

A [RAP BO](../abap-glossary/abenrap_bo_glosry.md) in a [cross-BO scenario](../abap-glossary/abencds_cross_bo_assoc_glosry.md) that has an [association](../abap-glossary/abenassociation_glosry.md) to a dependent [BO](../abap-glossary/abenrap_bo_glosry.md). An [association](../abap-glossary/abenassociation_glosry.md) to a dependent [BO](../abap-glossary/abenrap_bo_glosry.md) establishes a [composition-like relationship](../abap-glossary/abencds_composition_glosry.md) where the [host BO](../abap-glossary/abenrap_bo_glosry.md) takes over [locking](../abap-glossary/abenlock_glosry.md), [permission handling](../abap-glossary/abenauthorization_glosry.md) and [deletion](../abap-glossary/abenrap_delete_operation_glosry.md) for its dependent [BO](../abap-glossary/abenrap_bo_glosry.md). A [host BO](../abap-glossary/abenrap_bo_glosry.md) uses the [syntax](../abap-glossary/abensyntax_check_glosry.md) `to dependent` on the [association](../abap-glossary/abenassociation_glosry.md) to the dependent [BO](../abap-glossary/abenrap_bo_glosry.md).

**RAP input derived type**

A [BDEF derived type](../abap-glossary/abenrap_derived_type_glosry.md) that is used for importing parameters in methods in the [ABP](../abap-glossary/abenbehavior_pool_glosry.md).

**RAP input identifier**

A [structure](../abap-glossary/abenstructure_glosry.md) that is imported into implementation methods in the [ABAP behavior pool](../abap-glossary/abenbehavior_pool_glosry.md). It consists of all components that are relevant to identify one [instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md) for the current method.

An input identifier can either be the [instance identifier](../abap-glossary/abenrap_inst_identifier_glosry.md) or the [content identifier](../abap-glossary/abenrap_cont_identifier_glosry.md), or both.

**RAP instance feature control**

A kind of [feature control](../abap-glossary/abenrap_feature_control_glosry.md) that defines access restrictions for a [field](../abap-glossary/abenrap_bo_field_glosry.md) or an [operation](../abap-glossary/abenrap_bo_operation_glosry.md). It can be static or dynamic.

**RAP instance identifier**

A [structure](../abap-glossary/abenstructure_glosry.md) that uniquely identifies a [RAP BO instance](../abap-glossary/abenrap_bo_instance_glosry.md). It consists of the primary key fields and all relevant [derived type](../abap-glossary/abenrap_derived_type_glosry.md) components, for example `%is_draft`, `%pid`. The instance identifier is represented by the component groups `%tky` or `%pky`.

See also: [RAP input identifier](../abap-glossary/abenrap_input_identifier_glosry.md).

**RAP instance transition message**

A [transition message](../abap-glossary/abenrap_trans_mes_glosry.md) that refers to an [instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md) of a business object entity and contains a key reference.

**RAP interaction phase**

A part of the [RAP BO](../abap-glossary/abenrap_bo_glosry.md) runtime during which data is modified on the [transactional buffer](../abap-glossary/abentransactional_buffer_glosry.md).

**RAP interface behavior definition**

Interface BDEF for short. A component of a [RAP BO interface](../abap-glossary/abenrap_bo_interface_glosry.md). It defines the behavior that is included in the interface. A RAP BO interface behavior definition is represented by a [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md) with the [BDEF implementation type](../abap-glossary/abencds_bdef_impl_type_glosry.md) `interface`.

**RAP internal numbering**

A [numbering concept](../abap-glossary/abenrap_numbering_glosry.md) in which key values are assigned by the [RAP BO provider](../abap-glossary/abenrap_bo_provider_glosry.md).

**RAP inverse function**

A [RAP non-standard operation for associations](../abap-glossary/abenrap_standard_op_assoc_glosry.md) that receives the values of the [foreign key fields](../abap-glossary/abenforeign_key_field_glosry.md) of the [association target](../abap-glossary/abenassociation_target_glosry.md) instances as input and provides the corresponding [association source](../abap-glossary/abenassociation_source_glosry.md) instances as result. It can be used, for example, to enable [read-by-association operations](../abap-glossary/abenrap_rba_operation_glosry.md) in a [cross-BO](../abap-glossary/abencds_cross_bo_assoc_glosry.md) scenario.

**RAP key function**

A predefined [RAP function](../abap-glossary/abenrap_function_glosry.md) that is defined for a [BDEF alternative key](../abap-glossary/abenrap_alternative_key_glosry.md). It receives the values of an alternative key as input and returns the [entity instances](../abap-glossary/abenrap_bo_entity_inst_glosry.md) with matching values. Key functions are used, for example, to enable [read-by-association](../abap-glossary/abenrap_rba_operation_glosry.md) operations in RAP BOs with [cross-BO associations](../abap-glossary/abencds_cross_bo_assoc_glosry.md) involving RAP reuse objects.

**RAP late numbering**

A [numbering concept](../abap-glossary/abenrap_numbering_glosry.md) in which key values are assigned during the [RAP save sequence](../abap-glossary/abenrap_save_seq_glosry.md).

The final key value is only assigned in the [RAP saver method](../abap-glossary/abenabp_saver_method_glosry.md) [`adjust_numbers`](abap-for-rap-business-objects/abensaver_adjust_numbers.md).&#x00A0;

**RAP late save phase**

The phase of the [RAP save sequence](../abap-glossary/abenrap_save_seq_glosry.md) that covers the [RAP saver methods](../abap-glossary/abenabp_saver_method_glosry.md) [`adjust_numbers`](abap-for-rap-business-objects/abensaver_adjust_numbers.md) and [`save`](abap-for-rap-business-objects/abensaver_method_save.md) (or [`save_modified`](abap-for-rap-business-objects/abaprap_saver_meth_save_modified.md) respectively). The [`cleanup`](abap-for-rap-business-objects/abensaver_method_cleanup.md) method is called following a successful save.

**RAP link action**

A [RAP non-standard operation for associations](../abap-glossary/abenrap_nonst_op_assoc_glosry.md) that associates a [RAP BO entity instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md) to another RAP BO entity instance by setting the [foreign key](../abap-glossary/abenforeign_key_glosry.md). The link action can be defined for [intra-BO associations](../abap-glossary/abencds_intra_bo_assoc_glosry.md) and for [cross-BO associations](../abap-glossary/abencds_cross_bo_assoc_glosry.md).

See also: [RAP unlink action](../abap-glossary/abenrap_unlink_action_glosry.md)

**RAP lock dependent entity**

A [RAP BO entity](../abap-glossary/abenrap_bo_entity_glosry.md) whose locking requests are delegated to the [lock master entity](../abap-glossary/abenrap_lock_ma_ent_glosry.md). Defined using the keyword [`lock dependent by _Assoc`](rap-behavior-definitions/abenbdl_locking.md).

**RAP lock master entity**

A [RAP BO entity](../abap-glossary/abenrap_bo_entity_glosry.md) that is locked on each locking request of one of its [lock dependent entities](../abap-glossary/abenrap_lock_dep_ent_glosry.md). On each locking request the lock master and all its lock dependent entities are locked.

**RAP lock operation**

A [RAP BO operation](../abap-glossary/abenrap_bo_operation_glosry.md) that locks [RAP BO entity instances](../abap-glossary/abenrap_bo_entity_inst_glosry.md) on the [persistent table](../abap-glossary/abenrap_persistent_table_glosry.md) during a [RAP transaction](../abap-glossary/abenrap_luw_glosry.md).

**RAP locking**

A locking mechanism that is based on the SAP lock concept. It uses lock function modules for [pessimistic concurrency control](../abap-glossary/abenpessimist_conc_control_glosry.md).

**RAP managed draft provider**

A part of the [RAP BO provider](../abap-glossary/abenrap_bo_provider_glosry.md) that manages draft data on the [transactional buffer](../abap-glossary/abentransactional_buffer_glosry.md) during the [interaction phase](../abap-glossary/abenrap_int_phase_glosry.md) and provides [draft actions](../abap-glossary/abenrap_bo_draft_action_glosry.md) and the total ETag handling in draft-enabled [RAP BOs](../abap-glossary/abenrap_bo_glosry.md).

**RAP message**

A message that is represented by an instance of a class that implements the interface `IF_ABAP_BEHV_MESSAGE` and is used in [RAP BO provider](../abap-glossary/abenrap_bo_provider_glosry.md) implementations.

Each application can create its own classes. For convenience, each [behavior pool](../abap-glossary/abenbehavior_pool_glosry.md) contains a predefined local [exception class](../abap-glossary/abenexception_class_glosry.md) `CL_ABAP_BEHV_MSG` inherited from `CX_NO_CHECK` that implements `IF_ABAP_BEHV_MESSAGE` in a minimalistic way. It can be used for RAP messages as well as for raising [exceptions](../abap-glossary/abenexception_glosry.md) where appropriate.

**RAP modify operation**

A synonym for [CUD operations](../abap-glossary/abencud_glosry.md). [RAP BO operation](../abap-glossary/abenrap_bo_operation_glosry.md) that changes data of a [RAP BO entity instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md). [Create](../abap-glossary/abenrap_create_operation_glosry.md), [update](../abap-glossary/abenrap_update_operation_glosry.md), and [delete](../abap-glossary/abenrap_delete_operation_glosry.md) are RAP modify operations.

**RAP new draft instance**

A [draft instance](../abap-glossary/abenrap_draft_instance_glosry.md) that is produced by a [create operation](../abap-glossary/abenrap_create_operation_glosry.md) with the [draft indicator](../abap-glossary/abenrap_draft_indicator_glosry.md) set to *true*. The data of new draft instances is not yet persisted on the active database table and there is no corresponding active instance available.

See also: [RAP edit draft instance](../abap-glossary/abenrap_edit_draft_inst_glosry.md)

**RAP non-factory action**

A [RAP action](../abap-glossary/abenrap_action_glosry.md) that is not a factory action. In contrast to factory actions, the [BDEF derived type](../abap-glossary/abenrap_derived_type_glosry.md) of a non-factory action does not contain a [`%cid`](abap-for-rap-business-objects/abapderived_types_cid.md) component.

**RAP nonstandard operation for associations**

An [operation for associations](../abap-glossary/abenrap_operation_assoc_glosry.md) that provides noncanonical behavior along an [association path](../abap-glossary/abencds_association_path_glosry.md) from an [association source](../abap-glossary/abenassociation_source_glosry.md) to an [association target](../abap-glossary/abenassociation_target_glosry.md). For example, the [link action](../abap-glossary/abenrap_link_action_glosry.md), the [unlink action](../abap-glossary/abenrap_unlink_action_glosry.md), the [reorder action](../abap-glossary/abenrap_reorder_action_glosry.md), and the [inverse function](../abap-glossary/abenrap_inverse_function_glosry.md) are predefined nonstandard operations for associations.

**RAP numbering**

A concept that deals with setting values for primary key fields of [RAP BO entity instances](../abap-glossary/abenrap_bo_entity_inst_glosry.md).

The following numbering concepts are available:

- [early numbering](../abap-glossary/abenrap_early_numbering_glosry.md)

- [external numbering](../abap-glossary/abenrap_ext_numbering_glosry.md)

- [internal numbering](../abap-glossary/abenrap_int_numbering_glosry.md)

- [late numbering](../abap-glossary/abenrap_late_numbering_glosry.md)

**RAP operation for associations**

A [RAP BO operation](../abap-glossary/abenrap_bo_operation_glosry.md) that operates along an [association path](../abap-glossary/abencds_association_path_glosry.md) and affects the [association target](../abap-glossary/abenassociation_target_glosry.md). They are defined in the [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md) for the association. There are [standard operations for associations](../abap-glossary/abenrap_standard_op_assoc_glosry.md) and [non-standard operations for associations](../abap-glossary/abenrap_nonst_op_assoc_glosry.md).

**RAP output derived type**

A [BDEF derived type](../abap-glossary/abenrap_derived_type_glosry.md) that is used for changing parameters in methods in the [ABP](../abap-glossary/abenbehavior_pool_glosry.md).

**RAP persistent data**

Data on the [RAP persistent table](../abap-glossary/abenrap_persistent_table_glosry.md).

**RAP persistent state**

The state of a [business object](../abap-glossary/abenrap_bo_glosry.md) or its [instances](../abap-glossary/abenrap_bo_instance_glosry.md) as it is on the [persistent database table](../abap-glossary/abenrap_persistent_table_glosry.md).

**RAP persistent table**

The [DDIC database table](../abap-glossary/abenddic_db_table_glosry.md) a [RAP BO](../abap-glossary/abenrap_bo_glosry.md) is based on. For transactional changes of RAP persistent table data, the data is loaded into the [transactional buffer](../abap-glossary/abentransactional_buffer_glosry.md). At the end of a [RAP transaction](../abap-glossary/abenrap_luw_glosry.md), changes in the transactional buffer are either written back to the persistent table (commit) or discarded (rollback).

**RAP principal draft BO**

A [draft-enabled RAP business object](../abap-glossary/abendraft_rap_bo_glosry.md) in a [cross-BO association](../abap-glossary/abencds_cross_bo_assoc_glosry.md) scenario that assigns the draft state of its [instances](../abap-glossary/abeninstance_glosry.md) to the associated instances of the dependent draft RAP business object. All associated instances are set to draft and activated. A principal draft RAP business object has the syntax `with dependent draft` on the cross-BO association in the projection [BDEF](../abap-glossary/abencds_behavior_definition_glosry.md).

**RAP projection behavior definition**

RAP projection BDEF or projection BDEF for short. A RAP projection behavior definition is a [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md) of [implementation type](../abap-glossary/abencds_bdef_impl_type_glosry.md) `projection`. It is based on a [CDS transactional query](../abap-glossary/abencds_transactional_pv_glosry.md) and it projects a [base BDEF](../abap-glossary/abenrap_base_bdef_glosry.md).

**RAP projection business object**

A [RAP business object](../abap-glossary/abenrap_bo_glosry.md) that is defined in a [RAP projection behavior definition](../abap-glossary/abencds_proj_bdef_glosry.md). It has a [CDS projection view](../abap-glossary/abencds_projection_view_glosry.md) as [root view](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_view_as_projection.md).

**RAP projection extension entity**

Defines the node extension in the projection layer. A component of a [BDEF projection extension](../abap-glossary/abenrap_projec_bdef_ext_glosry.md) that defines the behavior for an extension node in the projection layer. Projection extension entity behavior is defined using [`define behavior for`](rap-behavior-definitions/abenbdl_proj_ext_entity.md) in the context of a [BDEF projection extension](../abap-glossary/abenrap_projec_bdef_ext_glosry.md). The extension node must be added to the current RAP BO's data model via [RAP data model extensions](../abap-glossary/abenrap_data_model_ext_glosry.md).

**RAP query**

A consumption option in RAP that provides read-only consumption of data defined in [CDS entities](../abap-glossary/abencds_entity_glosry.md). A RAP query is executed by the [RAP query engine](../abap-glossary/abenrap_query_engine_glosry.md).

**RAP query engine**

A part of the [RAP runtime engine](../abap-glossary/abenrap_runtime_engine_glosry.md) that handles the non-transactional consumption of [RAP BOs](../abap-glossary/abenrap_bo_glosry.md). The RAP query engine is provided by the [RAP framework](../abap-glossary/abenrap_framework_glosry.md) but can be adapted by implementing an [unmanaged query](../abap-glossary/abenrap_unmanged_query_glosry.md).

**RAP read operation**

[RAP BO operation](../abap-glossary/abenrap_bo_operation_glosry.md) that retrieves data of a [RAP BO entity instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md) from the [RAP transactional buffer](../abap-glossary/abentransactional_buffer_glosry.md) or from the database table if the instance in not available in the transactional buffer.

See also: [CRUD operations](../abap-glossary/abencrud_glosry.md)

**RAP read-by-association operation**

[RAP read operation](../abap-glossary/abenrap_read_operation_glosry.md) that retrieves data of an [association target](../abap-glossary/abenassociation_target_glosry.md) of a [RAP BO entity](../abap-glossary/abenrap_bo_entity_glosry.md).

**RAP recommendation**

Input assistance that proposes field values for [input fields](../abap-glossary/abeninput_field_glosry.md) in a RAP application on an SAP Fiori UI, based on the user input and interaction history.

RAP recommendations can be implemented using generative AI or using deterministic rules in the [behavior pool](../abap-glossary/abenbehavior_pool_glosry.md) of the [RAP business object](../abap-glossary/abenrap_bo_glosry.md). In SAP Fiori, a RAP recommendation is exposed as a recommendation pattern of type input assistance.

**RAP reorder action**

A [RAP hierarchy action](../abap-glossary/abenrap_hierarchy_action_glosry.md) that moves a [hierarchy node](../abap-glossary/abenhierarchy_node_glosry.md) to a dedicated position among its siblings in editable [treeview scenarios](../abap-glossary/abenrap_treeview_glosry.md) by recalculating the hierarchy index fields of all sibling instances. The reorder action can be managed or unmanaged.

**RAP repeatable operation**

[RAP action](../abap-glossary/abenrap_action_glosry.md) or [RAP function](../abap-glossary/abenrap_function_glosry.md) that can be executed multiple times on the same [RAP BO entity instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md) within the same [ABAP EML](../abap-glossary/abenabap_eml_glosry.md) or [OData](../abap-glossary/abenodata_glosry.md) request. The [BDEF derived type](../abap-glossary/abenrap_derived_type_glosry.md) of a repeatable operation contains a [`%cid`](abap-for-rap-business-objects/abapderived_types_cid.md) component and the [RAP response parameters](../abap-glossary/abenrap_response_param_glosry.md) are filled for each execution individually.

**RAP response**

Information a [RAP BO consumer](../abap-glossary/abenrap_bo_consumer_glosry.md) is provided with by a [RAP BO provider](../abap-glossary/abenrap_bo_provider_glosry.md) via the [RAP response parameters](../abap-glossary/abenrap_response_param_glosry.md) `mapped`, `failed` and `reported` of individual [RAP handler methods](../abap-glossary/abenabp_handler_method_glosry.md) and [RAP saver methods](../abap-glossary/abenabp_saver_method_glosry.md).

Depending on the availability of these response parameters in the said methods, the information that is provided can comprise the following:

- `mapped`: Used to provided mapping information on [RAP BO instances](../abap-glossary/abenrap_bo_instance_glosry.md), for example, which key values were created for given content IDs ([`%cid`](abap-for-rap-business-objects/abapderived_types_cid.md)).

- `failed`: Information for identifying the data set for which an error occurred in a RAP operation.

- `reported`: Used to exchange error messages for each entity defined in the BDEF and [not related to a specific entity](abap-for-rap-business-objects/abapderived_types_other.md).

**RAP response parameter**

Implicit changing parameters of [RAP handler methods](../abap-glossary/abenabp_handler_method_glosry.md) and [RAP saver methods](../abap-glossary/abenabp_saver_method_glosry.md) (implicitly) typed with the [BDEF derived type](../abap-glossary/abenrap_derived_type_glosry.md) [`... TYPE RESPONSE FOR ...`](abap-for-rap-business-objects/abaptype_response_for.md). Depending on the RAP handler or saver method, the signatures of the individual methods can include all of the following three formal parameters `mapped`, `failed` and `reported`, a subset or none of them. The names of the parameters are predefined. They are used to provide a [RAP BO consumer](../abap-glossary/abenrap_bo_consumer_glosry.md) with information by a [RAP BO provider](../abap-glossary/abenrap_bo_provider_glosry.md).

Parameters:

- `failed`: Information for identifying the data set for which an error occurred in a RAP operation

- `reported`: Used to exchange messages (for example, error messages) for each entity defined in the BDEF and [not related to a specific entity](abap-for-rap-business-objects/abapderived_types_other.md).

- `mapped`: Used to provide mapping information on [RAP BO instances](../abap-glossary/abenrap_bo_instance_glosry.md), for example, which key values were created for given content IDs ([`%cid`](abap-for-rap-business-objects/abapderived_types_cid.md)).

**RAP reuse service**

A RAP reuse service is a [reuse service](../abap-glossary/abenreuse_service_glosry.md) that is natively integrated in [RAP](../abap-glossary/abenrap_glosry.md). For example, [RAP change documents](../abap-glossary/abenrap_change_documents_glosry.md) are a RAP reuse service.

**RAP runtime engine**

Processor that handles the consumption of [RAP queries](../abap-glossary/abenrap_query_glosry.md) and [RAP BOs](../abap-glossary/abenrap_bo_glosry.md). There is the [RAP query engine](../abap-glossary/abenrap_query_engine_glosry.md) for non-transactional consumption and the [RAP transactional engine](../abap-glossary/abenrap_transac_engine_glosry.md) for transactional consumption.

**RAP runtime framework**

Part of the [RAP framework](../abap-glossary/abenrap_framework_glosry.md) that is provided by the [ABAP runtime framework](../abap-glossary/abenabap_runtime_frmwk_glosry.md) for consuming [RAP business objects](../abap-glossary/abenrap_bo_glosry.md) from outside [AS ABAP](../abap-glossary/abenas_abap_glosry.md) or from [ABAP programs](../abap-glossary/abenabap_program_glosry.md). In order to handle open protocols such as [OData](../abap-glossary/abenodata_glosry.md) when a RAP BO is exposed as a [business service](../abap-glossary/abenbusiness_service_glosry.md), the RAP runtime framework involves components of [SAP Gateway](../abap-glossary/abensap_gateway_glosry.md). In order to control the runtime behavior of a RAP business object, the RAP runtime framework uses [SADL](../abap-glossary/abensadl_glosry.md) as an orchestration framework. [ABAP EML](../abap-glossary/abenabap_eml_glosry.md) statements that are used to access RAP BOs from inside an ABAP program, also trigger processes in the RAP runtime framework.

**RAP save action**

[RAP action](../abap-glossary/abenrap_action_glosry.md) that can only be executed during the [RAP save sequence](../abap-glossary/abenrap_save_seq_glosry.md). Any attempt to execute a RAP save action during the [RAP interaction phase](../abap-glossary/abenrap_int_phase_glosry.md) results in a [short dump](../abap-glossary/abenshort_dump_glosry.md).

**RAP save sequence**

The RAP save sequence is part of the [RAP BO](../abap-glossary/abenrap_bo_glosry.md) runtime and is triggered after at least one successful modification was performed during the [interaction phase](../abap-glossary/abenrap_int_phase_glosry.md). It saves data from the [transactional buffer](../abap-glossary/abentransactional_buffer_glosry.md) on the database.

The RAP save sequence is divided into three phases that are entered in this order:

- [RAP early save phase](../abap-glossary/abenearly_rap_save_phase_glosry.md)

- [RAP late save phase](../abap-glossary/abenlate_rap_save_phase_glosry.md)

- [RAP cleanup phase](../abap-glossary/abenrap_cleanup_phase_glosry.md)

**RAP saver class**

[Local class](../abap-glossary/abenlocal_class_glosry.md) in a [CCIMP include](../abap-glossary/abenccimp_glosry.md) of an [ABAP behavior pool (ABP)](../abap-glossary/abenbehavior_pool_glosry.md) for implementing [RAP saver methods](../abap-glossary/abenabp_saver_method_glosry.md) that are called during the [save sequence](../abap-glossary/abenrap_save_seq_glosry.md).

**RAP saver method**

Special method in a [RAP saver class](../abap-glossary/abenabp_saver_class_glosry.md) of an [ABAP behavior pool](../abap-glossary/abenbehavior_pool_glosry.md) that is called during the [RAP save sequence](../abap-glossary/abenrap_save_seq_glosry.md). The names of saver methods are predefined and cannot be changed.&#x00A0;

**RAP side effect**

An optional part of a [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md) that defines interdependencies among BO properties that trigger a reload of the affected properties on the user interface. Introduced by the keyword [`side effects`](rap-behavior-definitions/abenbdl_side_effects.md) in the [entity behavior body](../abap-glossary/abencds_entity_body_glosry.md) of a RAP behavior definition.

**RAP standard operation for associations**

[Operation for associations](../abap-glossary/abenrap_operation_assoc_glosry.md) that provides canonical behavior along an [association path](../abap-glossary/abencds_association_path_glosry.md) from an [association source](../abap-glossary/abenassociation_source_glosry.md) to an [association target](../abap-glossary/abenassociation_target_glosry.md). [Create-by-association](../abap-glossary/abenrap_cba_operation_glosry.md) and [read-by-association](../abap-glossary/abenrap_rba_operation_glosry.md) are standard operations for associations.

**RAP state message**

A [message](../abap-glossary/abenrap_message_glosry.md) in the [`reported`](abap-for-rap-business-objects/abapeml_response.md) [RAP response parameter](../abap-glossary/abenrap_response_param_glosry.md) of a [RAP business object](../abap-glossary/abenrap_bo_glosry.md) that refers to the state of an [entity instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md). A state message is defined with the parameter [`%state_area`](abap-for-rap-business-objects/abapderived_types_state_area.md), which assigns it to the corresponding state area. A state message is persisted with the instance it refers to in [draft-enabled BOs](../abap-glossary/abendraft_rap_bo_glosry.md).

RAP state messages are relevant in the following contexts:

- Draft-enabled RAP BOs

- The [`cleanup_finalize`](abap-for-rap-business-objects/abapsaver_class_cleanup_finalize.md) and [`check_before_save`](abap-for-rap-business-objects/abensaver_check_before_save.md) [RAP saver methods](../abap-glossary/abenabp_saver_method_glosry.md) in [unmanaged RAP BOs](../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- [Determinations](../abap-glossary/abenrap_determination_glosry.md) and [validations](../abap-glossary/abenrap_validation_glosry.md) in [managed RAP BOs](../abap-glossary/abenmanaged_rap_bo_glosry.md)

**RAP static field characteristic**

[Field characteristic](../abap-glossary/abenrap_field_char_glosry.md) that defines usage restrictions for a [RAP BO field](../abap-glossary/abenrap_bo_field_glosry.md) independently of the state of a [RAP BO entity instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md). For example, [read-only](../abap-glossary/abenread_only_rap_bo_field_glosry.md) and [mandatory](../abap-glossary/abenmandatory_rap_bo_field_glosry.md) are static field characteristics.

**RAP static transition message**

A [transition message](../abap-glossary/abenrap_trans_mes_glosry.md) that refers to a [RAP BO entity](../abap-glossary/abenrap_bo_entity_glosry.md), but not to a specific [instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md). Unlike a [RAP instance transition message](../abap-glossary/abeninstance_rap_trans_mes_glosry.md), it does not contain a key reference.

**RAP total ETag**

A field of a [draft-enabled RAP BO](../abap-glossary/abendraft_rap_bo_glosry.md) that enables [optimistic concurrency checks](../abap-glossary/abenoptimistic_conc_control_glosry.md) during the transition form draft to [persistent data](../abap-glossary/abenrap_persistent_data_glosry.md).

**RAP transaction**

A RAP transaction ...

- is the sum of all operations and workflows that are used to transfer data from one consistent state to another.

- begins with creating new data on the [RAP transactional buffer](../abap-glossary/abentransactional_buffer_glosry.md) or by retrieving data from the database to the transactional buffer.

- is terminated with [`COMMIT ENTITIES`](abap-for-rap-business-objects/abapcommit_entities.md) or [`ROLLBACK ENTITIES`](abap-for-rap-business-objects/abaprollback_entities.md).

**RAP transactional buffer**

Storage where the data that is used during one [RAP transaction](../abap-glossary/abenrap_luw_glosry.md) is kept. It includes the [RAP BO instance](../abap-glossary/abenrap_bo_instance_glosry.md) that are being worked on.

A distinction is drawn between the following kinds of transactional buffer:

- [managed transactional buffer](../abap-glossary/abenmanaged_trans_buff_glosry.md) for [managed RAP BOs](../abap-glossary/abenmanaged_rap_bo_glosry.md).

- [unmanaged transactional buffer](../abap-glossary/abenunmanaged_trans_buff_glosry.md) for [unmanaged RAP BOs](../abap-glossary/abenunmanaged_rap_bo_glosry.md).

**RAP transactional engine**

Part of the [RAP runtime engine](../abap-glossary/abenrap_runtime_engine_glosry.md) that handles the transactional consumption of [RAP BOs](../abap-glossary/abenrap_bo_glosry.md).

**RAP transactional framework**

Part of the [RAP framework](../abap-glossary/abenrap_framework_glosry.md) that consists of the [RAP transactional engine](../abap-glossary/abenrap_transac_engine_glosry.md) and the development environment for [RAP business objects](../abap-glossary/abenrap_bo_glosry.md).

**RAP transactional phase**

The [RAP interaction phase](../abap-glossary/abenrap_int_phase_glosry.md) and [RAP save sequence](../abap-glossary/abenrap_save_seq_glosry.md) are RAP transactional phases.

**RAP transition message**

A message in the [`reported`](abap-for-rap-business-objects/abapeml_response.md) [RAP response parameter](../abap-glossary/abenrap_response_param_glosry.md) that is semantically related to the current ABAP EML `MODIFY` request and independent of the state of the [entity instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md). Unlike [RAP state messages](../abap-glossary/abenrap_state_mes_glosry.md), transition messages are [RAP messages](../abap-glossary/abenrap_message_glosry.md) that do not have a state area assigned ([`%state_area`](abap-for-rap-business-objects/abapderived_types_state_area.md)) and are not persisted with the state. Therefore, these messages cannot be accessed at a later point in time.

There are [instance transition messages](../abap-glossary/abeninstance_rap_trans_mes_glosry.md) and [static transition messages](../abap-glossary/abenstatic_rap_trans_mes_glosry.md).

**RAP type mapping**

Mapping between data types of the data model that is defined in CDS for a [RAP business object](../abap-glossary/abenrap_bo_glosry.md) to other data types that do not match a [BDEF derived type](../abap-glossary/abenrap_derived_type_glosry.md) component pattern.

For example, it is used in the behavior definition to map database field names to CDS element names.

**RAP unlink action**

A [RAP non-standard operation for associations](../abap-glossary/abenrap_nonst_op_assoc_glosry.md) that disconnects two associated [RAP BO entity instances](../abap-glossary/abenrap_bo_entity_inst_glosry.md) by removing the value of the [foreign key](../abap-glossary/abenforeign_key_glosry.md) field. The unlink action can be defined for [intra-BO associations](../abap-glossary/abencds_intra_bo_assoc_glosry.md) and for [cross-BO associations](../abap-glossary/abencds_cross_bo_assoc_glosry.md).

See also: [RAP link action](../abap-glossary/abenrap_link_action_glosry.md)

**RAP unmanaged draft provider**

Draft [provider](../abap-glossary/abenrap_bo_provider_glosry.md) of [BOs](../abap-glossary/abenrap_bo_glosry.md) with unmanaged draft. The [draft handling](../abap-glossary/abenrap_draft_handling_glosry.md) is implemented in the [ABAP behavior pool](../abap-glossary/abenbehavior_pool_glosry.md).

**RAP unmanaged query**

An implementation type of the RAP query for which parts of the [RAP query engine](../abap-glossary/abenrap_query_engine_glosry.md) must be implemented in an [ABAP class](../abap-glossary/abenclass_glosry.md) that is referenced in a [CDS custom entity](../abap-glossary/abencds_custom_entity_glosry.md).

**RAP unmanaged save**

Save logic which replaces the default save method in [managed RAP BOs](../abap-glossary/abenmanaged_rap_bo_glosry.md). It can be applied to the complete [BO](../abap-glossary/abenrap_bo_glosry.md) by defining it in the [behavior definition header](../abap-glossary/abencds_bdef_header_glosry.md), or for an individual entity by defining it in the [behavior entity characteristics](../abap-glossary/abencds_entity_properties_glosry.md). It is implemented in the redefined [saver method](../abap-glossary/abenabp_saver_method_glosry.md) `save_modified`.

**RAP update operation**

A [RAP modify operation](../abap-glossary/abenrap_modify_operation_glosry.md) that changes [field](../abap-glossary/abenrap_bo_field_glosry.md) values of existing [RAP BO entity instances](../abap-glossary/abenrap_bo_entity_inst_glosry.md).

**RAP validation**

An optional part of the [RAP BO behavior](../abap-glossary/abenrap_bo_behavior_glosry.md) that checks the consistency of [RAP BO instance](../abap-glossary/abenrap_bo_instance_glosry.md) based on trigger conditions.

**read-only RAP BO field**

A [field](../abap-glossary/abenrap_bo_field_glosry.md) in a [RAP BO](../abap-glossary/abenrap_bo_glosry.md) that is defined as read-only in the [behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md). Changes to this field are only allowed by the [RAP BO provider](../abap-glossary/abenrap_bo_provider_glosry.md) in local mode.

**REST**

Short for Representational State Transfer. An architecture concept for Web services. One of the essential conditions for a [RESTful](../abap-glossary/abenrestful_glosry.md) programming model is a stateless Web server. No client-dependent information can be saved on a Web server between the Web client requests made to the server. The status of a session is managed by the Web client and all necessary information is transferred to the Web server with requests. However, a Web server can also be a client of a persistence layer such as a [database system](../abap-glossary/abendatabase_system_glosry.md), in which the status of a session is saved persistently for its duration. ABAP supports REST in [ABAP RAP](../abap-glossary/abenabap_rap_glosry.md).

[***-\>* More about**](https://en.wikipedia.org/wiki/Representational_state_transfer)

**RESTful**

Programming models and their services, APIs, and protocols are called RESTful if they meet the [REST](../abap-glossary/abenrest_glosry.md) principles. See also [ABAP RESTful Application Programming Model](../abap-glossary/abenarap_glosry.md).

**reverse foreign key association**

*-\>* [target-resolved association](../abap-glossary/abentarget_resolved_assoc_glosry.md)

**SADL**

Short for Service Adaptation Definition Language. Infrastructure for model-based reading and processing of data. The [RAP runtime framework](../abap-glossary/abenrap_runt_framework_glosry.md) uses SADL internally for its [query engine](../abap-glossary/abenrap_query_engine_glosry.md) and its orchestration framework, which controls the runtime behavior of [RAP business objects](../abap-glossary/abenrap_bo_glosry.md).

**source-resolved association**

Also known as [foreign key association](../abap-glossary/abenforeign_key_assoc_glosry.md). An [association](../abap-glossary/abencds_association_glosry.md) relationship in which the [foreign key](../abap-glossary/abenforeign_key_glosry.md) is stored in the [association source](../abap-glossary/abenassociation_source_glosry.md) entity.

**static RAP BO operation**

A [RAP BO operation](../abap-glossary/abenrap_bo_operation_glosry.md) that is not bound to any [RAP BO entity instance](../abap-glossary/abenrap_bo_entity_inst_glosry.md) but relates to the complete [RAP BO entity](../abap-glossary/abenrap_bo_entity_glosry.md). Defined using the optional addition [`static`](rap-behavior-definitions/abenbdl_static.md).

**target-resolved association**

Also known as [reverse foreign key association](../abap-glossary/abenreverse_fk_assoc_glosry.md). An [association](../abap-glossary/abencds_association_glosry.md) relationship in which the [foreign key](../abap-glossary/abenforeign_key_glosry.md) is stored in the [association target](../abap-glossary/abenassociation_target_glosry.md) entity.

**transactional phase**

Specifies the concrete phase of a transaction. It is either the modify or the save transactional phase. They are set either implicitly, as in the case of, for example, [RAP handler](../abap-glossary/abenabp_handler_method_glosry.md) and [saver](../abap-glossary/abenabp_saver_method_glosry.md) methods, or explicitly using the static methods of class [`CL_ABAP_TX`](../abap-programming-language/abap-database-access/abaprap_cl_abap_tx.md).

In a [RAP transaction](../abap-glossary/abenrap_luw_glosry.md), the transactional phases are as follows:

- Modify: Includes the [RAP interaction phase](../abap-glossary/abenrap_int_phase_glosry.md) and the [early save phase](../abap-glossary/abenearly_rap_save_phase_glosry.md) of the [RAP save sequence](../abap-glossary/abenrap_save_seq_glosry.md).

- Save: Includes the [RAP late save phase](../abap-glossary/abenlate_rap_save_phase_glosry.md).

**treeview**

In the context of the [ABAP RESTful Application Programming Model](../abap-glossary/abenarap_glosry.md), a treeview visualizes data modeled by a [CDS hierarchy](../abap-glossary/abencds_hierarchy_glosry.md) e.g. by using a SAP Fiori Elements treetable. A treeview can be read-only or editable.

**unmanaged RAP BO provider**

Part of the [RAP BO provider](../abap-glossary/abenrap_bo_provider_glosry.md) that must be implemented in the [ABAP behavior pool](../abap-glossary/abenbehavior_pool_glosry.md).

**unmanaged RAP business object**

Unmanaged RAP BO for short. Provisioning type of the [business object behavior](../abap-glossary/abenrap_bo_behavior_glosry.md) of a [RAP BO](../abap-glossary/abenrap_bo_glosry.md). The [transactional buffer](../abap-glossary/abentransactional_buffer_glosry.md) of an unmanaged RAP BO is provided by an [ABAP behavior implementation](../abap-glossary/abenbehavior_implement_glosry.md). The implementation of an unmanaged RAP BO is fully provided by the [unmanaged RAP BO provider](../abap-glossary/abenunmanaged_rap_bo_prov_glosry.md) in an [ABAP behavior pool](../abap-glossary/abenbehavior_pool_glosry.md).

**unmanaged transactional buffer**

[Transactional buffer](../abap-glossary/abentransactional_buffer_glosry.md) of an [unmanaged RAP BO](../abap-glossary/abenunmanaged_rap_bo_glosry.md) that is provided and accessed by the [unmanaged RAP BO provider](../abap-glossary/abenunmanaged_rap_bo_prov_glosry.md).

**value help**

*-\>* [Input help](../abap-glossary/abeninput_help_glosry.md)

**web API**

[OData](../abap-glossary/abenodata_glosry.md) consumer of a [RAP business service](../abap-glossary/abenbusiness_service_glosry.md) that serves as an API without UI-specific metadata.
