---
title: "Release Contracts"
source_file: abenabap_release_contracts.html
section: "ABAP APIs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Release Contracts

A repository object can be classified by a [release contract](../../abap-glossary/abenrelease_contract_glosry.md). A release contract is the prerequisite for classifying a repository object as a [released API](../../abap-glossary/abenreleased_api_glosry.md) that can be accessed in a [restricted ABAP language version](../../abap-glossary/abenrestricted_version_glosry.md). It ensures a certain stability regarding consistency and compatibility of repository objects that are released as APIs. For repository objects delivered by SAP, compliance with a release contract is checked by special [ATC checks](../../abap-glossary/abenatc_glosry.md).

The following release contracts are available:

- **Extend (C0)**

  This contract ensures stability at dedicated extension points to allow for a certain extensibility. Contract C0 is relevant for repository objects that are enhanced by enhancement tools, e.g. of the [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md) or [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md). For more information, see [Extend (C0)](https://help.sap.com/docs/ABAP_PLATFORM_NEW/c238d694b825421f940829321ffa326a/2ce344a782d74d8aab073fa188af5116) on SAP Help Portal.

- **Use System-Internally (C1)**

  This contract ensures a technically stable public interface for system-internal use. Existing visible components, for example parameters, elements, or CDS associations, must not be changed in an incompatible way. Optional components might be added later. Contract C1 is relevant for repository objects that are accessed by different [ABAP language versions](../../abap-glossary/abenabap_version_glosry.md). For more information, see [Use System-Internally (C1)](https://help.sap.com/docs/ABAP_PLATFORM_NEW/c238d694b825421f940829321ffa326a/3ccb57a1a4d04ee192fdc2a849a89158).

- **Use as Remote API (C2)**

  This contract ensures a technically stable public interface for use as remote API. It is similar to C1 but additionally guarantees, that external consumers of the API do not need to be adjusted after an upgrade. Contract C2 is relevant only for external consumption. For more information, see [Use as Remote API (C2)](https://help.sap.com/docs/ABAP_PLATFORM_NEW/c238d694b825421f940829321ffa326a/9c7f9ba825064053874d5870bcb991fb).

- **Manage Configuration Content (C3)**

  This contract ensures a stable persistence for own configuration content that can be exported, imported, displayed and edited using dedicated APIs. No key or other fields must be changed. Non-key fields might be added later. Contract C3 is relevant for Business Configuration Tools.

- **Use in ABAP-Managed Database Procedures (AMDP) (C4)**

  This contract ensures a technically stable public interface for use in [ABAP Managed Database Procedures](../../abap-glossary/abenabap_managed_db_proc_glosry.md). It is similar to C1 but in contrast to C1, no optional components can be added later. No changes are allowed. Contract C4 is relevant for [AMDP methods](../../abap-glossary/abenamdp_method_glosry.md) that are accessed by other AMDP methods, such as [BAdI methods](../../abap-glossary/abenbadi_method_glosry.md) implemented as AMDP-methods. For more information, see [Use in ABAP-Managed Database Procedures (C4)](https://help.sap.com/docs/ABAP_PLATFORM_NEW/c238d694b825421f940829321ffa326a/288854b83f764fc2b7ae8c5f62140cfe).

## Hints

- For consistency reasons, a repository object with release contract C1 must be classified as visible for a least one [restricted ABAP language version](../../abap-glossary/abenrestricted_version_glosry.md). and thus be released as an API.

- See also [Contract Checks for Released APIs](abenrestricted_apis_atc_checks.md) for an overview of the according rules.
