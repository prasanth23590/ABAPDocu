---
title: "CDS DDL - Annotation Syntax, subannos"
source_file: abencds_annotations_syntax_subanno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - Specifying Annotations > CDS DDL - Annotation Syntax"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - Annotation Syntax, subannos

## Syntax

``` abap
... subAnno1[:   value  ] 
           |[: { subannos } ] 
           |[: [ arrelem ] ] 
           |[.subAnno[ ... ]], 
    subAnno2[:   value  ] 
           |[: { subannos } ] 
           |[: [ arrelem ] ] 
           |[.subAnno[ ... ]], 
    ...  
```

[`value`](abencds_annotations_syntax_value.md) · [`arrelem`](abencds_annotations_syntax_array.md) · [`.subAnno[ ... ]`](abencds_annotations_syntax_name.md) · [`value`](abencds_annotations_syntax_value.md) · [`arrelem`](abencds_annotations_syntax_array.md) · [`.subAnno[ ... ]`](abencds_annotations_syntax_name.md)

## Description

Comma-separated list of [subannotations](../../abap-glossary/abensub_annotation_glosry.md) `subAnno1`, `subAnno2`, ... in the curly brackets of an [annotation](abencds_annotations_syntax.md). The name of a subannotation can contain letters, numbers, and underscores only and must start with a letter. The same information can be specified after the name as specified after the [main annotation](../../abap-glossary/abenmain_annotation_glosry.md):

- A colon (`:`) followed by the following:

  - An [annotation value](../../abap-glossary/abenannotation_value_glosry.md) [`value`](abencds_annotations_syntax_value.md)

  - Further [subannotations](../../abap-glossary/abensub_annotation_glosry.md) `subannos` specified in curly brackets `{ ... }`.

  - Elements of an [annotation array](../../abap-glossary/abenannotation_array_glosry.md) [`arrelem`](abencds_annotations_syntax_array.md) in square brackets `[ ... ]`

- The chaining of the subannotations `subAnno1`, `subAnno2`, ... with a further subannotation [`subAnno`](abencds_annotations_syntax_name.md) using a period (`.`).

Only those subannotations should be specified that are supported by the associated [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md).

## Hint

As well as by using a comma-separated list in curly brackets, individual subannotations can also be specified using individual [structured annotation names](abencds_annotations_syntax_name.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) is available.

``` abap
@Scope:[#VIEW, #EXTEND_VIEW] 
define annotation 
  DemoSubAnnos: { 
    subAnno1: Boolean; 
    subAnno2: { subAnno1: Integer; 
                subAnno2: { subAnno1: Integer; 
                            subAnno2: Integer; } } };
```

The annotation can then, for example, be specified as follows:

``` abap
@DemoSubAnnos: {subAnno1: true, 
                subAnno2: { subAnno1: 1, 
                            subAnno2: { subAnno1: 1, 
                                        subAnno2: 2 } } }
```

This example has the same semantics as the example using [structured names](abencds_annotations_syntax_name.md).
