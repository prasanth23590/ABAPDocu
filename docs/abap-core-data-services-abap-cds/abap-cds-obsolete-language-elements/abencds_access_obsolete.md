---
title: "Obsolete Access to CDS Entities"
source_file: abencds_access_obsolete.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Obsolete Access to CDS Entities

- **Access to and typing with [CDS-managed DDIC views](../../abap-glossary/abencds_mngdddic_view_glosry.md) is obsolete**

  A CDS-managed DDIC view (obsolete), specified using the annotation [`@AbapCatalog.sqlViewName`](abencds_define_view_v1.md) in a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), must be considered as purely technical helper construct and should not be used at all. In particular, accessing a CDS-managed DDIC view from ABAP SQL is obsolete.
