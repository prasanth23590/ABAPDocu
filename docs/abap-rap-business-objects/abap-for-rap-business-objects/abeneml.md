---
title: "ABAP EML - Consuming RAP BOs"
source_file: abeneml.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - Consuming RAP BOs

The [ABAP Entity Manipulation Language (EML)](../../abap-glossary/abenaeml_glosry.md) is a subset of ABAP for accessing RAP business objects (RAP BOs) and RAP BO interfaces. EML statements allow the data content of a RAP BO (transactional buffer) to be read or modified and the persistent storage of modified data to be triggered.

ABAP EML can be used in all ABAP programs to consume RAP BOs. In particular, they can be used in the implementation of a RAP BO in an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) itself. For the latter there are some special [EML variants](abeneml_in_abp.md).

The execution of an EML statement triggers processes in the [RAP runtime framework](../../abap-glossary/abenrap_runt_framework_glosry.md) that call the implementation of the RAP BOs. For [unmanaged RAP BOs](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) or unmanaged parts of [managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md) the implementation is part of an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). Otherwise, it is part of the RAP provider framework.

The operands of EML statements are primarily special messenger tables, user for transmitting data to RAP BOs and receiving results or messages from them. These messenger tables are internal tables whose line type is designed for this purpose.

The following topics are covered in this section:

- [ABAP EML - Common EML Statements and Operands](abapcommon_eml_elements.md)

- [`COMMIT ENTITIES`](abapcommit_entities.md)

- [`GET PERMISSIONS`](abapget_permissions.md)

- [`MODIFY ENTITY`, `ENTITIES`](abapmodify_entity_entities.md)

- [`READ ENTITY`, `ENTITIES`](abapread_entity_entities.md)

- [`ROLLBACK ENTITIES`](abaprollback_entities.md)

- [`SET LOCKS`](abapset_locks.md)

- [`CONVERT KEY`](abapconvert_key.md)

## More Information

When implementing RAP operations, ensure that you comply with [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). Follow the implementation guidelines in the development guide for the ABAP RESTful Application Programming Model, section [RAP Business Object Contract](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

You can find a selected set of guidelines in [here](abaprap_impl_rules.md).
