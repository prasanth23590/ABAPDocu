---
title: "Released APIs"
source_file: abenabap_api_release.html
section: "ABAP APIs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Released APIs

As stated in [ABAP - Language Versions](../abenabap_language_versions.md), repository objects with a [restricted ABAP language version](../../abap-glossary/abenrestricted_version_glosry.md) cannot freely access other repository objects. Besides some allowed accesses, for example inside the same software component, only access to those repository objects is allowed that are a [released API](../../abap-glossary/abenreleased_api_glosry.md) for that language version. Releasing an API for a restricted ABAP language version comprises two classifications:

- The repository object must be classified with an appropriate [release contract](../../abap-glossary/abenrelease_contract_glosry.md).

- The repository object must be classified as visible for the [restricted ABAP language version](../../abap-glossary/abenrestricted_version_glosry.md).

Repository objects with release contracts C0 and C1 can be made visible for the [Restricted ABAP language versions](../../abap-glossary/abenrestricted_version_glosry.md) [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md) and [ABAP for Key Users](../../abap-glossary/abenabap_for_key_users_glosry.md). For accessing released APIs from other repository objects of certain ABAP language versions, only release contract C1 is relevant.

The classification of a repository object as a released API is part of the development process. The classification must be part of the same software component or even package as the repository object itself. This ensures that APIs can be released only by organizations that are responsible for the repository objects.

See [Released APIs of the Current System](abenreleased_apis.md) for a list of repository objects that are released as APIs in the current system.

## Hints

- It is recommended that released APIs are subject to an approval process, as it is the case at SAP.

- For more information, see [Released APIs](https://help.sap.com/docs/ABAP_PLATFORM_NEW/c238d694b825421f940829321ffa326a/c479660d07374c15a1a5fe83fdbb1337).

- See [Contract Checks for Released APIs](../release-contracts/abenrestricted_apis_atc_checks.md) for rules that must be obeyed by providers and consumers.

- When a data object is explicitly passed to an API in another software component, the object's type does not generally need to be released for the API to inspect and access it. Data references define what can be addressed directly: if a reference is passed, the API can access and inspect the reference, but not the data object it points to, unless the type is released. This also applies to references within a passed data object, such as a structure component that holds a reference. This approach supports generic frameworks by eliminating the need to release every type when an object of that type is passed to an API in another software component.
