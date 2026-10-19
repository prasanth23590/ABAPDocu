---
title: "CDS DDL - Annotation Syntax"
source_file: abencds_annotations_syntax.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - Specifying Annotations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - Annotation Syntax

## Syntax

``` abap
@[<]Anno[: value ] 
       |[: { subannos } ] 
       |[: [ arrelem ] ] 
       |[.subAnno[ ... ]]  
```

[`value`](abencds_annotations_syntax_value.md) · [`subannos`](abencds_annotations_syntax_subanno.md) · [`arrelem`](abencds_annotations_syntax_array.md) · [`.subAnno[ ... ]`](abencds_annotations_syntax_name.md)

## Description

A [CDS annotation](abencds_annotations.md) is specified in [CDS source code](../../abap-glossary/abencds_source_code_glosry.md) by using fixed [annotation syntax](../../abap-glossary/abencds_annotation_syntax_glosry.md). This syntax specifies the following:

- The annotation is introduced using the character `@` or the characters `@<`.

  `@<` can be used in the CDS DDL for CDS entities except for [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) in order to specify the annotation after a list element in a comma-separated or semicolon-separated list.

- A [main annotation](../../abap-glossary/abenmain_annotation_glosry.md) `Anno` consisting of letters, numbers, and underscores and starting with a letter. A main annotation that is not structured using [subannotations](../../abap-glossary/abensub_annotation_glosry.md) can be specified exactly once in a [scope](abencds_annotations_scopes.md).

- One of the following optional alternatives specified after a colon (`:`):

  - An [annotation value](../../abap-glossary/abenannotation_value_glosry.md) [`value`](abencds_annotations_syntax_value.md)

  - [Subannotations](../../abap-glossary/abensub_annotation_glosry.md) [`subannos`](abencds_annotations_syntax_subanno.md) specified in curly brackets `{ ... }`.

  - Elements of an [annotation array](../../abap-glossary/abenannotation_array_glosry.md) [`arrelem`](abencds_annotations_syntax_array.md) specified in square brackets `[ ... ]`.

- The [main annotation](../../abap-glossary/abenmain_annotation_glosry.md) `Anno` chained with a [subannotation](../../abap-glossary/abensub_annotation_glosry.md) [`subAnno`](abencds_annotations_syntax_name.md) using a period (`.`). The combination `Anno.subAnno` is a structured annotation name that can be extended using further subannotations.

An annotation name must be unique within a [scope](abencds_annotations_scopes.md). Only those annotations should be specified for which a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) exists. Alongside the syntax rules above, the annotation definition also specifies the following:

- The statement `define annotation` defines the name, the possible [annotation values](../../abap-glossary/abenannotation_value_glosry.md), the layout of the [subannotations](../../abap-glossary/abensub_annotation_glosry.md), and whether the annotation in question is an [annotation array](../../abap-glossary/abenannotation_array_glosry.md).

- The annotations of an annotation definition specify the scope of the annotation, whether it can be moved to metadata extensions, and whether a particular annotation value is translatable text.

In the [DCL source code](../../abap-glossary/abendcl_source_code_glosry.md) for [CDS roles](../../abap-glossary/abencds_role_glosry.md), [`DDLX` source code](../../abap-glossary/abenddlx_source_code_glosry.md) for [metadata extensions](../../abap-glossary/abencds_metadata_extension_glosry.md), and the [`DDLA` source code](../../abap-glossary/abenddla_source_code_glosry.md) for [annotation definitions](../../abap-glossary/abencds_anno_definition_glosry.md), the syntax check allows only those annotations that follow the rules of an annotation definition. In the [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md) for [data definitions](../../abap-glossary/abencds_data_definition_glosry.md), annotation definitions modify the source code colors and code completion in [ADT](../../abap-glossary/abenadt_glosry.md). Currently, however, they are not covered by the syntax check.

## Hints

- The evaluation of the annotations of CDS source code is currently the responsibility of the framework in which the [CDS object](../../abap-glossary/abencds_object_glosry.md) is used.

- The annotations specified in the DDL source code of a CDS entity can be supplemented or overridden using the annotations of [CDS metadata extensions](../../abap-glossary/abencds_metadata_extension_glosry.md). Here the annotations are specified with the same syntax as in the DDL source code of a CDS entity, with the following restrictions:

  - `@<` cannot be used for introducing an annotation.

  - Only those annotations can be specified for which this is noted in their [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md).

- There is a set of [SAP annotations](abencds_annotations_sap.md) predefined by SAP, comprising [ABAP annotations](../../abap-glossary/abenabap_annotation_glosry.md) evaluated by the ABAP runtime framework and [framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) evaluated by other frameworks. All other annotations are not usually evaluated. It cannot be guaranteed, however, that a framework allows all annotations.

- The program `ABAP_DOCU_CDS_ANNOS_OVERVIEW` shows all SAP annotations and their properties.
