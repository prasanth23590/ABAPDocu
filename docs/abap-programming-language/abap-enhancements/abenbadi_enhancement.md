---
title: "Enhancements Using BAdIs"
source_file: abenbadi_enhancement.html
section: "ABAP Programming Language > ABAP - Enhancements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Enhancements Using BAdIs

BAdIs are part of the [enhancements](../../abap-glossary/abenenhancement_glosry.md) made available by the ABAP Enhancement Framework. BAdIs, together with their calling positions in ABAP programs, form explicit [enhancement options](../../abap-glossary/abenenhancement_point_glosry.md) of these programs and are assigned to [enhancement spots](../../abap-glossary/abenenhancement_spot_glosry.md).

If BAdIs and their calling positions are defined in a system, [enhancements](../../abap-glossary/abenenhancement_glosry.md) can be made in follow-on systems by creating [BAdI](../../abap-glossary/abenbadi_implementation_glosry.md) implementations in these systems. A BAdI implementation consists mainly of a [BAdI implementation class](../../abap-glossary/abenbadi_implement_class_glosry.md) whose instances enhance the functions of an ABAP program at runtime in the form of an [object plug-in](../../abap-glossary/abenobject_plugin_glosry.md). In the ABAP Enhancement Framework, a BAdI implementation is an [enhancement implementation element](../../abap-glossary/abenenhancement_impl_elem_glosry.md) and is administrated by [enhancement implementations](../../abap-glossary/abenenhancement_impl_glosry.md).

A BAdI consists mainly of a [BAdI interface](../../abap-glossary/abenbadi_interface_glosry.md) that contains the declaration of [BAdI methods](../../abap-glossary/abenbadi_method_glosry.md), and a set of filters. The filters enable certain BAdI implementations to be selected for use. The following settings can be made in the definition of a BAdI, in addition to the selection of the [BAdI interface](../../abap-glossary/abenbadi_interface_glosry.md):

- Whether a BAdI is intended for single or multiple use. If a BAdI is intended for single use, only a single [BAdI implementation](../../abap-glossary/abenbadi_implementation_glosry.md) can be used in an [internal session](../../abap-glossary/abeninternal_session_glosry.md), and one BAdI implementation must be available for each use.

- A fallback [BAdI implementation class](../../abap-glossary/abenbadi_implement_class_glosry.md) can be specified to be used if no BAdI implementation matches the filter conditions.

- A BAdI can be defined as context-free or context-dependent. This setting controls the instantiation of the [object plug-ins](../../abap-glossary/abenobject_plugin_glosry.md). In context-free BAdIs, it is possible to define whether an object plug-in can be created only once or multiple times within an internal session. In context-dependent BAdIs, the object plug-ins are linked with a [context object](../../abap-glossary/abenbadi_context_object_glosry.md).

BAdIs of the ABAP Enhancement Framework are supported by the ABAP runtime framework by the following ABAP statements:

- [`GET BADI`](abapget_badi.md)

  Creates a [BAdI object](../../abap-glossary/abenbadi_object_glosry.md) as a handle for [object plug-ins](../../abap-glossary/abenobject_plugin_glosry.md).

- [`CALL BADI`](abapcall_badi.md)

  Calls [BAdI methods](../../abap-glossary/abenbadi_method_glosry.md) in [object plug-ins](../../abap-glossary/abenobject_plugin_glosry.md).

The BAdIs of the ABAP Enhancement Framework are also freely switchable using switches from the [Switch Framework](../../abap-glossary/abenswitch_framework_glosry.md).

## Hints

- For a BAdI that is intended for single use, it is best to always specify a fallback implementation class and to implement it in the same system as the BAdI.

- The implementation of the [BAdI methods](../../abap-glossary/abenbadi_method_glosry.md) of a [BAdI interface](../../abap-glossary/abenbadi_interface_glosry.md) can be made optional, like any other interface method, by using the addition [`DEFAULT`](../abap-declarations/abapmethods_default.md).

- See also the documentation [Enhancement Framework](https://help.sap.com/docs/ABAP_PLATFORM_NEW/46a2cfc13d25463b8b9a3d2a3c3ba0d9/949cdc40132a8531e10000000a1550b0) in SAP Help Portal.
