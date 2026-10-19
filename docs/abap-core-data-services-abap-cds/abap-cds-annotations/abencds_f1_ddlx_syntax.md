---
title: "ABAP CDS - DDL for Metadata Extensions"
source_file: abencds_f1_ddlx_syntax.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - Specifying Annotations > ABAP CDS - Metadata Extensions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - DDL for Metadata Extensions

Alongside the [DDL statements for data definitions](../abap-cds-data-definitions/abencds_f1_ddl_syntax.md), the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) in ABAP CDS makes it possible to define [metadata extensions](abencds_meta_data_extensions.md) for CDS entities in [`DDLX` source code](../../abap-glossary/abenddlx_source_code_glosry.md). The following statement is used here:

- [`ANNOTATE ENTITY, VIEW`](abencds_f1_annotate_view.md)

## Hints

- Two slashes (`//`) can be used as [comment characters](../abap-cds-syntax/abencds_general_syntax_rules.md) in [`DDLX` source code](../../abap-glossary/abenddlx_source_code_glosry.md) for metadata extensions, but not two dashes (`--`).

- The [`DDLX` source code](../../abap-glossary/abenddlx_source_code_glosry.md) of metadata extensions has its own editor in [ADT](../../abap-glossary/abenadt_glosry.md), which is documented there.
