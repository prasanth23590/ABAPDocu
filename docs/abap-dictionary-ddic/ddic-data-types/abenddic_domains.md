---
title: "DDIC - Domains"
source_file: abenddic_domains.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types > DDIC - Data Elements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Domains

A [DDIC domain](../../abap-glossary/abendomain_glosry.md) is a standalone dictionary object that defines technical and semantic properties of elementary data types. [Data elements](abenddic_data_elements.md) can be defined with reference to a domain and inherit the properties defined there. Domains can only be used in DDIC data elements. A domain can be used by any number of data elements.

- [Technical properties of domains](abenddic_domains_tech.md)

- [Semantic properties of domains](abenddic_domains_sema.md)

The name of a domain must follow the [naming rules for DDIC data types](abenddic_types_names.md) but it is located in a different namespace from data types. A domain can have the exact same name as a data type and, more particularly, a data element.

## Hints

- Redundant domains should not occur within an application component or a package. Domains that only have technical properties should be created as reusable domains in central basis packages. One example is the domain `CHAR255`.

- The [fixed values](../../abap-glossary/abenfixed_value_glosry.md) of a domain can be used as special kinds of literals in [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md).

- As of ABAP release 7.93, [ABAP Core Data Services](../../abap-glossary/abenabap_core_data_services_glosry.md) offer [CDS enumerated types](../../abap-glossary/abencds_enum_type_glosry.md) for defining [enumerated data types](../../abap-glossary/abenenum_type_glosry.md) natively in ABAP CDS. CDS enumerated types provide functionality similar to domains with [fixed values](../../abap-glossary/abenfixed_value_glosry.md) and are recommended when working with data models in ABAP CDS.

- A domain determines properties of an elementary data type but is not a data type itself. A domain cannot be specified after a `TYPE` addition in ABAP.
