---
title: "JSON-XML - XML Representation of JSON"
source_file: abenabap_json_xml.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and JSON"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# JSON-XML - XML Representation of JSON

JSON XML is an SAP-specific representation of [JSON](../../abap-glossary/abenjson_glosry.md) data in XML format. The [single values](abenjson_oview.md), [arrays](abenjson_oview.md), and [objects](abenjson_oview.md) in JSON are represented as follows in XML.

- [Single Values](abenabap_json_xml.md#single-values)

  - [Character-Like Values](abenabap_json_xml.md#character-like-values)

  - [Number Values](abenabap_json_xml.md#number-values)

  - [Boolean Values](abenabap_json_xml.md#boolean-values)

  - [Null Values](abenabap_json_xml.md#null-values)

- [Data Structures](abenabap_json_xml.md#data-structures)

  - [Arrays](abenabap_json_xml.md#arrays)

  - [Objects](abenabap_json_xml.md#objects)

## Single Values

### Character-Like Values

`"..."` *-\>* `<str>...</str>`

### Number Values

`...` *-\>* `<num>...</num>`

### Boolean Values

`true` *-\>* `<bool>true</bool>`

`false` *-\>* `<bool>false</bool>`

### Null Values

`null` *-\>* `<null />`

## Data Structures

### Arrays

`[...]` *-\>* `<array>...</array>`

The comma-separated components of arrays are mapped as subelements of the element `<array>`, whereby the type-specific mapping rule applies to each element.

### Hint

Since the components of an array do not have names, the elements of an array in JSON-XML cannot have the corresponding attributes, unlike objects.

### Objects

`{...}` *-\>* `<object>...</object>`

The comma-separated components of objects are mapped as subelements of the element `<object>`. There are two representation methods:

- `"n":...` *-\>* `<... name="n">...</...>`

- `"n":...` *-\>* `<member name="n"><...>...</...></member>`

In the first shorter method, used by default, a component is mapped like an element of an array, with the name `n` added to the type-specific XML element of the component as the content of the attribute `name`.

In the second longer method, the type-specific XML element of a component is nested in an additional element `<member>`, which then has the attribute `name` with the name of the component.

### Hints

- In the longer alternative for object components, each component in JSON-XML is clearly marked by a `<member>` element, which can help to distinguish objects of arrays when only partial fragments of JSON data are processed.

- The longer alternative for object components with `<member>` elements can be a better option for [Simple Transformations](../../abap-glossary/abensimple_transformation_glosry.md), when ABAP data is serialized to JSON or deserialized from JSON.

- A [JSON writer](../../abap-glossary/abenjson_writer_glosry.md) that [renders](abenabap_json_sxml.md) JSON-XML to JSON accepts both alternatives for object components. A [JSON reader](../../abap-glossary/abenjson_reader_glosry.md) that [parses](abenabap_json_sxml.md) JSON data to JSON-XML creates the shorter variant by default. To create the longer variant with `<member>` elements, the method `SET_OPTION` of the interface `IF_SXML_READER` can be used to set the option `IF_SXML_READER=>CO_OPT_SEP_MEMBER`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

- The class `CL_DEMO_JSON_XML` shows examples of the default JSON-XML representation of valid JSON data.

- For information about the rendering and parsing of JSON-XML representations in both alternatives for object components, see [Object Components in JSON-XML](abenabap_json_xml_abexa.md).
