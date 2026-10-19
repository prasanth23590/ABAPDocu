---
title: "CDS DDL - Annotation Syntax, arrelem"
source_file: abencds_annotations_syntax_array.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - Specifying Annotations > CDS DDL - Annotation Syntax"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - Annotation Syntax, arrelem

## Syntax

``` abap
...  value1|{subannos1}, 
     value2|{subannos2}, 
     ...  
```

[`value1`](abencds_annotations_syntax_value.md) · [`subannos1`](abencds_annotations_syntax_subanno.md) · [`value2`](abencds_annotations_syntax_value.md) · [`subannos2`](abencds_annotations_syntax_subanno.md)

## Description

Comma-separated list of array elements in the square brackets of an [annotation](abencds_annotations_syntax.md). This makes the annotation specified in front of the colon into an [annotation array](../../abap-glossary/abenannotation_array_glosry.md) with the elements specified in the brackets. The possible elements of an array are:

- [Annotation values](../../abap-glossary/abenannotation_value_glosry.md) [`value1`](abencds_annotations_syntax_value.md), [`value2`](abencds_annotations_syntax_value.md), ...

- [Subannotations](../../abap-glossary/abensub_annotation_glosry.md) [`subannos1`](abencds_annotations_syntax_subanno.md), [`subannos2`](abencds_annotations_syntax_subanno.md), ... in curly brackets.

Arrays are not intended to be nested directly and one element in an array represents an annotation to which the same rules apply as to single annotations. The difference is that an array element does not have an explicit name. In the internal repository of the metadata defined by an annotation, however, an array element is identified uniquely using an index appended to the name of the array. This makes it possible to find the array element when it is evaluated.

Array elements should only be specified for annotations for which this is noted in the associated [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md).

## Hints

- Annotation arrays with elements of different types and categories can be specified in the syntax of the [DDL for data definitions](../abap-cds-data-definitions/abencds_f1_ddl_syntax.md). Arrays of this type are not supported in [annotation definitions](../../abap-glossary/abencds_anno_definition_glosry.md). Square brackets for annotation arrays can be nested directly in data definitions. The nesting of arrays is also not supported in annotation definitions. The internal metadata repository counts the nested arrays when indexing the elements, but otherwise they are ignored.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) is available.

``` abap
@Scope:[#VIEW, #EXTEND_VIEW] 
define annotation 
  DemoAnnoStringArray: array of String(1);  
```

The annotation can then, for example, be specified as follows:

@DemoAnnoStringArray:\['a', 'b', 'c'\]

The annotation array has three elements, each of which is assigned a suitable annotation value. Evaluating the annotation using the method `GET_DIRECT_ANNOS_4_ENTITY` of the class `CL_DD_DDL_ANNOTATION_SERVICE` produces the following

| **ANNONAME**             | **VALUE** |
|--------------------------|-----------|
| `DEMOANNOSTRINGARRAY$1$` | `'a'`     |
| `DEMOANNOSTRINGARRAY$2$` | `'b'`     |
| `DEMOANNOSTRINGARRAY$3$` | `'c'`     |

The elements are indicated using the indexes `$1$`, `$2$`, and `$3$`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) is available. This is the definition of a structured annotation array.

``` abap
@Scope:[#VIEW, #EXTEND_VIEW]
define annotation 
  DemoAnnoArray: array of { subAnno1: Integer; 
                            subAnno2: Integer; 
                            subAnno3: Integer; } 
```

The annotation can then, for example, be specified with four structured array elements as follows:

``` abap
@DemoAnnoArray:[ {subAnno1:11, subAnno2:12, subAnno3:13}, 
                 {subAnno1:21, subAnno2:22, subAnno3:23}, 
                 {subAnno1:31, subAnno2:32, subAnno3:33}, 
                 {subAnno1:41, subAnno2:42, subAnno3:43} ]
```

## Executable Example

ABAP CDS, Annotation Array
