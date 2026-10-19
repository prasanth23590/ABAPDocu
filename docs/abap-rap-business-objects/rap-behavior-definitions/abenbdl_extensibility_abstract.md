---
title: "RAP - Abstract BDEF Extension"
source_file: abenbdl_extensibility_abstract.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Abstract BDEF Extension

An [abstract BDEF extension](../../abap-glossary/abenrap_abs_bdef_ext_glosry.md) is a repository object that extends an [abstract behavior definition](../../abap-glossary/abencds_abstract_bdef_glosry.md) using the statement [`extension for abstract`](abenbdl_extension_for_abstract.md).

As a prerequisite, the respective abstract BDEF must explicitly allow extensions as described in topic [RAP - Extensibility Enabling for Abstract BDEFs](abenbdl_ext_enabling_abstract.md).

The following extensions are possible:

- Extending an existing node using the statement `extend behavior for AbstractEntity`.

- Adding new nodes to the hierarchical type of the abstract BDEF using the statement `define behavior for AbstractEntity`.

- Adding new scalar entities to the hierarchical type using the statement `scalar entity AbstractEntity`.

Details are described in the topic [RAP - `extension for abstract`](abenbdl_extension_for_abstract.md).
