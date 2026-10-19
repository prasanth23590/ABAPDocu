---
title: "ABAP CDS - Client Handling in CDS Hierarchies"
source_file: abencds_hiera_client_handling.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Hierarchies"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Client Handling in CDS Hierarchies

For CDS hierarchies, client handling cannot be defined using annotations. Instead client handling is predefined as follows:

- Client dependency is determined by the client dependency of the CDS view used as its data source.

- In a client-dependent CDS hierarchy, all rows are removed implicitly from the result set of the CDS view specified as a data source that do not match the client ID currently contained in the [session variable](../../abap-glossary/abensession_variable_glosry.md) [`$session.client`](../abap-cds-obsolete-language-elements/abencds_session_variable_v1.md) (that addresses the HANA session variable `CDS_CLIENT`) before the hierarchy is generated.
