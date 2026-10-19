---
title: "ABAP development environment"
source_file: abenabap_dev_envir_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP development environment

[ABAP](../abap-programming-language/abap-overview/abentechno_glossary.md)

## Definition

ABAP DE for short. Development environment provided by the [ABAP technology](abenabap_techno_glosry.md) for [repository objects](abenrepository_object_glosry.md) that form ABAP applications. It mainly consists of:

- Its main programming language [ABAP](abenabala_glosry.md) and other programming languages such as [CDS DDL](abencds_ddl_glosry.md) for metadata definitions.

- Development tools such as [ABAP development tools for Eclipse (ADT)](abenadt_glosry.md) or the ABAP Workbench.

- Other [repository objects](abenrepository_object_glosry.md) that can be accessed as APIs.

Depending on the programming paradigm [ABAP Cloud](abenabap_cloud_glosry.md) or [classic ABAP](abenclassic_abap_glosry.md), ABAP development environments are either restricted or unrestricted.

- In [ABAP Cloud](abenabap_cloud_glosry.md):

  - The [ABAP language version](abenabap_version_glosry.md) is restricted to [ABAP for Cloud Development](abenabap_for_cloud_dev_glosry.md).

  - Access to other [repository objects](abenrepository_object_glosry.md) is restricted to [released APIs](abenreleased_api_glosry.md).

  - Only [ABAP development tools for Eclipse (ADT)](abenadt_glosry.md) can be used. There is no access to SAP GUI.

- In [classic ABAP](abenclassic_abap_glosry.md):

  - The [ABAP language version](abenabap_version_glosry.md) can be chosen freely.

  - [ABAP development tools for Eclipse (ADT)](abenadt_glosry.md) and the ABAP Workbench can both be used.

  - Access to other [repository objects](abenrepository_object_glosry.md) is not restricted.

The deployment of repository objects is managed by an integrated [Change and Transport System (CTS)](abencts_glosry.md).
