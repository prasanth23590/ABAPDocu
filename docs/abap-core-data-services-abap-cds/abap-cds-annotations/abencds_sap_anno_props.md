---
title: "ABAP CDS - Annotation Properties"
source_file: abencds_sap_anno_props.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Annotation Properties

The properties of [SAP annotations](../../abap-glossary/abensap_annotation_glosry.md) are shown in tables in the above topics. The following points explain the meaning of the table headers:

- **Kind**

  [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) or [framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md). The annotation is handled either by the [ABAP runtime framework](../../abap-glossary/abenabap_runtime_frmwk_glosry.md) or by another framework.

- **Syntax**

  Syntax of the annotation, where subannotations are shown via [chainings](abencds_annotations_syntax_name.md). If square brackets `[ ]` are specified after a name, this means that the annotation in front of the square brackets is an [annotation array](../../abap-glossary/abenannotation_array_glosry.md).

- **Scope**

  Scopes where the annotation can be specified. The scopes are shown by the enumeration symbols that are specified in the corresponding annotation definition for the `@Scope` annotation. The topic [Scopes for Annotations](abencds_annotations_scopes.md) maps these to source code positions.

- **Type**

  Type of the [annotation value](../../abap-glossary/abenannotation_value_glosry.md).

- **Enums**

  Enumeration symbols.

- **Default**

  Default value applied during the evaluation when the annotation is specified without a value. This value can differ from the value that is applied when the annotation is not specified at all.

- **Text**

  Indicates whether the annotation value is translatable text.

- **MDE**

  Indicates whether the annotation can be specified in a [metadata extension](../../abap-glossary/abencds_metadata_extension_glosry.md).

- **API**

  Indicates whether the annotation is [released as an API](../../abap-glossary/abenreleased_api_glosry.md).
