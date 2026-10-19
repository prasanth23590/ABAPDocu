---
title: "CDS DDL - CDS Projection View, Transactional Interface"
source_file: abencds_pv_transactional_interface.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS Projection View, Transactional Interface

A [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md) is a [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md) that is intended to serve as stable public interface. A CDS transactional interface should be released internally in the system under the [C1 contract](../../abap-glossary/abenc1_contract_glosry.md), and it can be released additionally under the [C0 contract](../../abap-glossary/abenc0_contract_glosry.md) for extensions. A CDS transactional interface is typically used in the context of the [ABAP RESTful Application Programming Model](../../abap-glossary/abenarap_glosry.md) to provide the basis for a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md). The feature set is restricted to projecting elements from the underlying [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md). No new associations, [virtual elements](../../abap-glossary/abencds_virtual_element_glosry.md), or fields can be defined.

As a global data type, a CDS projection view of type transactional interface represents a structured type with the elements of the CDS projection view as components. Usage:

- CDS transactional interfaces can be used as data source for CDS transactional queries. They cannot be used as data source for any other CDS entity.

- They can be used in ABAP programs as a data type for definitions and in ABAP SQL read statements.

## More Information

- Development guide for the ABAP RESTful Application Programming Model, topic [Business Object Interface](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/7caa146ddc4b4f24a58efd33f0f789b4?version=sap_cross_product_abap).

- ABAP Data Models guide, section about [CDS transactional interfaces](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/c947d462983e4738a641a6f3a792ac0e?version=sap_cross_product_abap).
