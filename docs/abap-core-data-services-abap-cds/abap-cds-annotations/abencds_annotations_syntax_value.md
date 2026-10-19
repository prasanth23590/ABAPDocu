---
title: "CDS DDL - Annotation Syntax, value"
source_file: abencds_annotations_syntax_value.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - Specifying Annotations > CDS DDL - Annotation Syntax"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - Annotation Syntax, value

## Syntax

``` abap
... literal   
  | #SYMBOL   
  | true|false   
  | #(unchecked expression)   
  | null  
```

## Description

An [annotation value](../../abap-glossary/abenannotation_value_glosry.md) can be specified directly after the colon `:` of an [annotation](abencds_annotations_syntax.md). The following can be specified for the annotation value:

- Literals

  Character literals enclosed in quotation marks or numeric literals. A numeric literal can have a period (`.`) as a decimal separator and can be specified with an exponent in scientific notation.

  A single quote can be used to escape another single quote or, alternatively, using a backslash \\

  Example: `@EndUserText.quickInfo: 'Customer''s first name'` is resolved into *Customer's first name*.

  Alternative: `@EndUserText.quickInfo: 'Customer\'s first name'` is resolved into *Customer's first name*.

- Enumeration symbols `#SYMBOL`

  Enumeration symbols are specified directly after the `#` character and without quotation marks.

- Unchecked expressions

  Unchecked expressions are specified in parentheses after the `#` character. Unchecked expressions can be [elementary operands](../abap-cds-data-definitions/abencds_operands_v2.md), [CDS DDL expressions](../../abap-glossary/abencds_expression_glosry.md), reused expressions from the `SELECT` list ([`$projection.reuse_exp`](../abap-cds-data-definitions/abencds_reusable_expression_v2.md)), or [SQL path expressions](../../abap-glossary/abensql_path_expression_glosry.md). Possible elementary operands are [CDS source fields](../../abap-glossary/abencds_field_glosry.md), [untyped literals](../../abap-glossary/abenuntyped_literal_glosry.md), [input parameters](../../abap-glossary/abeninput_parameter_glosry.md), and [session variables](../../abap-glossary/abensession_variable_glosry.md). [Typed literals](../../abap-glossary/abentyped_literal_glosry.md) and [enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md) are not supported. Unchecked expressions are not checked at design time or at activation. They are evaluated at runtime by the respective frameworks. Example: `@DemoAnnoValues: #(substring('hallo',3,2) + 3 * 4)`

- Truth values `true` and `false`

  These values can be enclosed in quotation marks but do not have to be.

- Null value `null`

  This value can be specified without quotation marks for [element annotations](../abap-cds-data-definitions/abencds_f1_element_annotation.md). This means that the annotations are ignored in the evaluation by default. The value `null` cannot be specified as an [element](abencds_annotations_syntax_array.md) of [annotation arrays](../../abap-glossary/abenannotation_array_glosry.md) and can only be specified in the [scope](abencds_annotations_scopes.md) of the element annotations.

Only those annotation values should be specified that are supported by the specified type of the associated [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md). Unless a default value is specified, a value should be specified in all cases. Non-specified annotation values are not replaced by the default value when the annotation is saved internally and evaluated.

## Hints

- No syntax checks are performed on an annotation value in the [DDL for data definitions](../abap-cds-data-definitions/abencds_f1_ddl_syntax.md), except for the formal rules above. The annotation is generally only handled correctly when evaluated or activated or by the framework if the annotation value follows the rule in the [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md).

- The framework in question is responsible for applying the correct default value if annotation values are not specified.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) is available.

``` abap
@Scope:[#VIEW, #EXTEND_VIEW] 
define annotation 
  DemoAnnoValues { 
    subAnno1: Boolean; 
    subAnno2: String(5) enum{FLAG1;FLAG2;FLAG3;}; 
    subAnno3: Integer; 
    subAnno4: Decimal(31,2); 
    subAnno5: DecimalFloat;
    subAnno6: EntityRef;  }; 
```

The annotation can then, for example, be specified with the following annotation values:

``` abap
@DemoAnnoValues: {subAnno1: false, 
                  subAnno2: #FLAG1, 
                  subAnno3: 1234, 
                  subAnno4: 123456.78, 
                  subAnno5: 1234.5678E-4 
                  subAnno6: "DEMO_CDS_SPFLI"}
```
