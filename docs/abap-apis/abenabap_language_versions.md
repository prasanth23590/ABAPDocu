---
title: "ABAP Language Versions"
source_file: abenabap_language_versions.html
section: "ABAP APIs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Language Versions

[ABAP programs](../abap-glossary/abenabap_program_glosry.md) as well as other [repository objects](../abap-glossary/abenrepository_object_glosry.md) have an attribute called [ABAP language version](../abap-glossary/abenabap_version_glosry.md). For an ABAP program, its language version defines the syntax rules and set of repository objects that can be addressed as APIs. For other repository objects the ABAP language version mainly defines the usable APIs.

Two main ABAP language versions are supported:

- [ABAP for Cloud Development](../abap-glossary/abenabap_for_cloud_dev_glosry.md)

  [Restricted ABAP language version](../abap-glossary/abenrestricted_version_glosry.md) for [ABAP Cloud](../abap-glossary/abenabap_cloud_glosry.md).

  - It covers a subset of the ABAP language scope.

    See Language Elements in ABAP Versions for a list of ABAP language elements that are allowed in the ABAP for Cloud Development compared to Standard ABAP.

  - Access to APIs is restricted.

    Repository objects with language version ABAP for Cloud Development can access objects which are [released APIs](../abap-glossary/abenreleased_api_glosry.md) for ABAP for Cloud Development or are in the same software component. In addition, objects of a local software component with language version ABAP for Cloud Development can access the objects of all other local and custom, production software components, which also are of ABAP for Cloud Development. If access to a software component was granted using a Software Component Relations object, the objects of that software component are permitted as well.

  - Client isolation

    [Client isolation](../abap-glossary/abenclient_isolation_glosry.md) is enforced by the implicit [client handling](../abap-glossary/abenclient_handling_glosry.md) in [ABAP SQL](../abap-glossary/abenabap_sql_glosry.md) and by the fact, that [AMDP methods](../abap-glossary/abenamdp_method_glosry.md) can use [client-safe](../abap-glossary/abenclient_safe_glosry.md) repository objects only.

- [Standard ABAP](../abap-glossary/abenstandard_abap_glosry.md)

  [Unrestricted ABAP language version](../abap-glossary/abenunrestricted_version_glosry.md) for [classic ABAP](../abap-glossary/abenclassic_abap_glosry.md). It covers the entire language scope of ABAP and besides the [package concept](../abap-glossary/abenpackage_concept_glosry.md) there are no restrictions for accessing APIs.

## Hints

- The ABAP language version of a repository object can either be set explicitly or is derived implicitly, e.g. from the package or the software component.

- Another [restricted ABAP language version](../abap-glossary/abenrestricted_version_glosry.md) is [ABAP for Key Users](../abap-glossary/abenabap_for_key_users_glosry.md) that is used for development objects created using key user apps. Repository objects with language version ABAP for Key Users can access objects which are [released APIs](../abap-glossary/abenreleased_api_glosry.md) for key user apps or were created by key user apps and marked for use by other key user apps. For more information, see [Key User Extensibility](https://help.sap.com/docs/ABAP_PLATFORM_NEW/0f69f8fb28ac4bf48d2b57b9637e81fa/3ccb50e724b045508fea8b2cf1774b2b).

- For more information about the ABAP language version of an ABAP program see [ABAP Language Versions](../abap-programming-language/abap-overview/abenabap_versions.md).
