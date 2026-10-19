---
title: "ABAP CDS - Aspects"
source_file: abencds_aspects.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Aspects

A [CDS DDL aspect](abencds_ddl_aspect_glosry.md) is a [CDS object](../../abap-glossary/abencds_object_glosry.md) defined using the statement [`DEFINE ASPECT`](abencds_define_aspect.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) of ABAP Core Data Services (CDS). A CDS aspect can be used to reuse dedicated parts of CDS entities, such as annotations, fields, or calculations. CDS aspects only generate a runtime artifact, which means that no [SQL view](../../abap-glossary/abensql_view_glosry.md) is generated on the database and cannot be accessed using an ABAP `SELECT` statement.

Once a CDS aspect has been defined and activated, it can be bound to one or more [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) or [CDS projection views](abencds_proj_views.md) using the syntax [`BIND ASPECT`](abencds_bind_aspect.md) behind the [`DEFINE VIEW ENTITY`](abencds_define_view_entity.md) statement. Using the syntax [`INCLUDE aspect`](abencds_include_aspect.md), the aspect can then be included in the [select statement](abencds_select_statement_v2.md) of a CDS view entity. If all fields of a CDS aspect are included with the syntax [`INCLUDE aspect.*`](abencds_include_aspect.md), fields can be excluded using the syntax [`EXCLUDE aspect.field`](abencds_include_aspect.md).

## Hints

- CDS Aspects are supported by analytical runtimes such as the [ABAP Analytical Engine](../../abap-glossary/abenabap_ae_glosry.md).

- CDS aspects can currently **not** be used in OData scenarios and in Fiori applications built with the [ABAP RESTful Application Programming Model](../../abap-glossary/abenarap_glosry.md).
