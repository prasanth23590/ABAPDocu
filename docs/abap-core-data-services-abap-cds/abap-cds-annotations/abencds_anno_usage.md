---
title: "ABAP CDS - Specifying Annotations"
source_file: abencds_anno_usage.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Specifying Annotations

[CDS entities](../../abap-glossary/abencds_entity_glosry.md) and [CDS roles](../../abap-glossary/abencds_role_glosry.md) plus [CDS annotation definitions](../../abap-glossary/abencds_anno_definition_glosry.md) themselves can (or must) be annotated with metadata using [CDS annotations](../../abap-glossary/abencds_annotation_glosry.md). This is done by specifying annotations directly in the associated [CDS source code](../../abap-glossary/abencds_source_code_glosry.md) or in [CDS metadata extensions](../../abap-glossary/abencds_metadata_extension_glosry.md). The annotations of [CDS metadata extensions](../../abap-glossary/abencds_metadata_extension_glosry.md) expand (or override) the annotations specified in the source code of a CDS entity.

An annotation is specified in fixed [annotation syntax](../../abap-glossary/abencds_annotation_syntax_glosry.md). This is then checked by the syntax check of the annotated source code. Only those annotations should be specified that are defined as a [CDS object](../../abap-glossary/abencds_anno_definition_glosry.md) in a [CDS annotation definition](../../abap-glossary/abencds_object_glosry.md). An annotation definition specifies the precise way an annotation must be specified. [ADT](../../abap-glossary/abenadt_glosry.md) supports the specification of valid annotations (namely annotations with an annotation definition) by using colors in the source code and code completion. The syntax check for the definition of a CDS entity in [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md) for CDS entities does not yet evaluate the annotation definitions. [`DDLA` source code](../../abap-glossary/abenddla_source_code_glosry.md) and [`DDLX` source code](../../abap-glossary/abenddlx_source_code_glosry.md) also check annotations with respect to their annotation definitions.

- [CDS annotation syntax](abencds_annotations_syntax.md)

- [CDS metadata extensions](abencds_meta_data_extensions.md)

- [Scopes for annotations](abencds_annotations_scopes.md)

## Hints

- [CDS annotation definitions](../../abap-glossary/abencds_anno_definition_glosry.md) can currently only be made by SAP, which means that only [SAP annotations](../../abap-glossary/abensap_annotation_glosry.md) should currently be specified in [CDS source code](../../abap-glossary/abencds_source_code_glosry.md).

- The program `ABAP_DOCU_CDS_ANNOS_OVERVIEW` shows all SAP annotations and their properties.
