---
title: "RAP - Extension Layering"
source_file: abenbdl_extension_layering.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Extension Layering

It is possible to extend a [BDEF extension](../../abap-glossary/abenrap_extension_glosry.md) with further BDEF extensions. This is referred to as [extension layering](../../abap-glossary/abenrap_ext_layering_glosry.md). As a prerequisite, a BDEF extension must be explicitly enabled for extensibility as described in the topic [RAP - Extensibility Enabling for BDEF Extensions](abenbdl_extensibility_enabling_ext.md).

The following general rules apply to BDEF extensions that extend another BDEF extension:

- A BDEF extension always extends the original RAP BO. When a new extension is created, the original RAP BO and all existing extensions are merged into one and define the extensible scope.

- Regarding the [RAP extensibility enablement](../../abap-glossary/abenrap_ext_enablement_glosry.md), the rule is that the [repository object](../../abap-glossary/abenrepository_object_glosry.md) that defines an extensible component defines the extensible scope. For example, if an extension node is defined in a BDEF extension, the extensibility enablement of the BDEF extension is respected. If the BDEF extension allows `validations on save` in an extension, then this RAP BO entity can be extended with `validations on save`. The RAP extensibility enablement of the original RAP BO is not relevant in this case. This rule applies to RAP BO entities and other extensible components, such as RAP type mappings and determine actions. The extensibility enablement is determined by the repository object that defines the component to be extended.

- Technically, a BDEF extension that extends another extension is a regular extension and there are no special rules. Like regular extensions, it refers to the original RAP BO, it can extend all components that are enabled for extensibility, and the feature scope is the same as for regular BDEF extensions. The general rules for BDEF extensions are described under:

  - Topic [RAP - Base BDEF Extension](abenbdl_extensibility_managed_unm.md)

  - Topic [RAP - BDEF Projection Extension](abenbdl_extensibility_projection.md)

  - Topic [RAP - Abstract BDEF Extension](abenbdl_extensibility_abstract.md)

- Each BDEF extension automatically inherits the [release contract](../../abap-glossary/abenrelease_contract_glosry.md) of the original RAP BO. Therefore, BDEF extensions must also meet the specifications of the release contract and need to be kept stable.

## More Information

- Development guide for the ABAP RESTful Application Programming Model, section [About RAP Extensibility](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/0e485d31120f484db63381e74755a94c?version=sap_cross_product_abap).
