---
title: "CDS DDL - CDS Simple Type, data_element"
source_file: abencds_dtel.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Type Definitions > CDS DDL - DEFINE TYPE > ABAP CDS - Simple Types > CDS DDL - DEFINE TYPE simple_type"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS Simple Type, data_element

## Syntax

``` abap
... data_element ...  
```

## Description

A [CDS simple type](../../abap-glossary/abencds_simple_type_glosry.md) can be typed using a [DDIC data element](../../abap-glossary/abendata_element_glosry.md) `data_element`. `data_element` can have any ABAP Dictionary type listed in the topic [ABAP CDS - Built-In Data Types](../abap-cds-data-types/abencds_overview_builtin_types.md). ABAP Dictionary types which are not listed there, such as `abap.fltp`, are not available for [CDS user-defined types](../../abap-glossary/abencds_user_defined_type_glosry.md).

The technical properties of a DDIC data element are inherited from the data element by the CDS simple type. This means that the data type, length, and decimal places are inherited.

The following semantic DDIC properties are also inherited from a data element to a CDS simple type:

- [Conversion exit](../../abap-glossary/abenconversion_exit_glosry.md)

- [**Lowercase letters**](../../abap-dictionary-ddic/ddic-data-types/abenddic_domains_sema.md)

- [**Change document**](../../abap-dictionary-ddic/ddic-data-types/abenddic_data_elements_sema.md)

The DDIC properties are translated into annotation values of a simple type. The following table shows a mapping from a DDIC property to a CDS simple type annotation:

| **DDIC property**                                            | **CDS simple type annotation**                                                 |
|--------------------------------------------------------------|--------------------------------------------------------------------------------|
| [Conversion exit](../../abap-dictionary-ddic/ddic-data-types/abenddic_domains_sema.md)                | [`AbapCatalog.typeSpec.conversionExit`](abencds_simple_type_anno.md)         |
| [Lowercase letters](../../abap-dictionary-ddic/ddic-data-types/abenddic_domains_sema.md)              | [`ObjectModel.upperCase`](abencds_simple_type_anno.md)                       |
| [Flag for change document](../../abap-dictionary-ddic/ddic-data-types/abenddic_data_elements_sema.md) | [`AbapCatalog.typeSpec.changeDocumentRelevant`](abencds_simple_type_anno.md) |
| [Field label, Heading](../../abap-dictionary-ddic/ddic-data-types/abenddic_data_elements_sema.md)     | [`EndUserText.heading`](abencds_simple_type_anno.md)                         |
| [Field label, Medium](../../abap-dictionary-ddic/ddic-data-types/abenddic_data_elements_sema.md)      | [`EndUserText.label`](abencds_simple_type_anno.md)                           |
| [Short text](../../abap-dictionary-ddic/ddic-data-types/abenddic_data_elements_sema.md)               | [`EndUserText.quickInfo`](abencds_simple_type_anno.md)                       |

Details about these properties can be found in the following documentation: [DDIC - Semantic Properties of Domains](../../abap-dictionary-ddic/ddic-data-types/abenddic_domains_sema.md) and [DDIC - Semantic Properties of Data Elements](../../abap-dictionary-ddic/ddic-data-types/abenddic_data_elements_sema.md).

The properties that are inherited from a DDIC type can be overridden in the CDS simple type if necessary.

## Restrictions

- [Search helps](../../abap-glossary/abensearch_help_glosry.md) are not inherited. Search helps can be defined in CDS simple types using the annotation `Consumption.valueHelpDefinition`.

- The short label and long label of DDIC data elements have no corresponding annotation in CDS simple types. This information is not inherited.

- The output length of a DDIC domain is not inherited. The output length is derived from the context, if necessary.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows how annotations are inherited from DDIC objects to CDS simple types.

- The DDIC domain `DEMO_BT_INHERITANCE` has the following properties:

  - Data type `CHAR1`, length 1

  - Output length 2

  - Conversion exit `ALV1`

  - It is not case sensitive, so all letters are converted to uppercase.

- The DDIC data element `DEMO_BT_INHERITANCE` inherits the technical properties from the domain. Additionally, it specifies field labels.

- The CDS simple type `DEMO_SIMPLE_TYPE_INHERITANCE` is based on the data element `DEMO_BT_INHERITANCE` and inherits its properties and texts:

define type demo_simple_type_inheritance: demo_bt_inheritance;

- The CDS view entity `DEMO_CDS_BT` uses the CDS simple type `DEMO_SIMPLE_TYPE_INHERITANCE` for a cast expression. As a result, the field `Char1Field` inherits the properties and texts from the CDS simple type.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, simple type'
define root view entity DEMO_CDS_BT
  as select from demo_ddic_types
{
  key id,
      int4,
      cast(char1 as demo_simple_type_inheritance) as Char1Field
}
```
