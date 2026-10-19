---
title: "RAP - Base BDEF Extension"
source_file: abenbdl_extensibility_managed_unm.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Base BDEF Extension

A [base BDEF extension](../../abap-glossary/abenrap_base_bdef_ext_glosry.md) is a repository object that extends a RAP behavior definition of type managed or unmanaged using the statement `extension`.

As a prerequisite, the respective BDEF must explicitly allow extensions as described in the topic [RAP - Extensibility Enabling for Base BOs](abenbdl_extensibility_enabling_m_u.md).

The following image shows the possible components of a BDEF extension: ![figure](images_bdef_extension_intro.jpg)

- The [BDEF extension header](../../abap-glossary/abenrap_bdef_ext_header_glosry.md) is a mandatory component that starts with `extension`.

- An [entity behavior extension](../../abap-glossary/abenrap_behavior_extension_glosry.md) is an optional component. It extends the behavior of an existing RAP BO entity. It starts with `extend behavior for`.

- An [extension entity behavior](../../abap-glossary/abenrap_ext_entity_behavior_glosry.md) is an optional component that defines the behavior for an extension node. It starts with `define behavior for`.

- An [authorization context for disable](../../abap-glossary/abencds_auth_context_glosry.md) can be added or a [full authorization context](../../abap-glossary/abencds_own_ac_glosry.md) may be extended.

**Caution**

For BDEF extensions for unmanaged RAP BOs, the following restrictions apply:

- No additional save can be defined.

- No determinations and validations can be defined.

- Node extensibility is not supported.
