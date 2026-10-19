---
title: "RAP - Behavior Definitions"
source_file: abencds_bdef.html
section: "ABAP RAP Business Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Behavior Definitions

A [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) (BDEF for short) is an ABAP repository object that defines the transactional behavior of a [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) in the context of [ABAP RAP](../../abap-glossary/abenabap_rap_glosry.md). The transactional behavior defines and restricts how a RAP BO can be accessed by a [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md). A BDEF is always based on a CDS data model that consists of at least one [root entity](../../abap-glossary/abenroot_entity_glosry.md) and it refers to the root entity. A root entity can have no more than one BDEF.

A RAP behavior definition consists of a [header part](../../abap-glossary/abencds_bdef_header_glosry.md) and at least one [entity behavior definition](../../abap-glossary/abencds_entity_bdef_glosry.md). The entity behavior definition, in turn, is made up of [entity characteristics](../../abap-glossary/abencds_entity_properties_glosry.md) and a [body](../../abap-glossary/abencds_entity_body_glosry.md). One or more [authorization contexts](../../abap-glossary/abencds_auth_con_glosry.md) can optionally be defined.

The following image shows the structure of a RAP behavior definition: ![figure](images_abdoc_bdef_structure.png)

Further details on the parts of a RAP behavior definition can be found in the following sections:

- [BDEF header](abenbdl_bdef_header.md)

- [entity behavior definition](abenbdl_define_beh.md)

- [entity behavior characteristics](abenbdl_character.md)

- [entity behavior body](abenbdl_body.md)

- [authorization context](abenbdl_authorization_context.md)

## More Information

An exhaustive description of RAP business objects, behavior characteristics, and transactional behavior can be found in the development guide for the RESTful Application Programming Model, in the section [Business Object](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/a3ff9dcdb25a4f1a9408422b8ba5fa00?version=sap_cross_product_abap).
