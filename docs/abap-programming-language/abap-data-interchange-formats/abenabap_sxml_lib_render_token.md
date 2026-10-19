---
title: "sXML - Token-Based Rendering"
source_file: abenabap_sxml_lib_render_token.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library > sXML - Rendering"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - Token-Based Rendering

In token-based rendering, each node is written to the XML data using a method. Each node type has its own method. If a node can have specific values, the respective method has appropriate input parameters. The methods must be called in such a way that valid XML is created. XML attributes can be added to an element directly after it has been opened.

## Basic Approach

An XML writer is created using the factory method `CREATE` of the required class. The format and character format can also be defined, for example:

``` abap
DATA(writer) = cl_sxml_string_writer=>create( type = 
                                              encoding = ... ).
```

Here, the static type of the reference variables is the type of the class itself, since more class-specific methods exist than in readers. The interface `IF_SXML_WRITER` can still be used to access a writer using upcasts:

`DATA(writer) = CAST if_sxml_writer( cl_sxml_string_writer=>create( ... ) ).`

Once the writer is created, nodes can be written. The order of the nodes is important, for example:

``` abap
writer->open_element( ... ). 
writer->write_attribute( ... ). 
writer->write_value( ... ). 
writer->close_element( ).
```

Once a complete valid record of XML data has been written, the data can be read if the correct writers are being used, for example:

`DATA(xml) = CAST cl_sxml_string_writer( writer )->get_output( ).`

Since the method is a class-specific method, a downcast is required if an interface reference variable is used.

### Executable Example

[Token-Based Rendering](abensxml_rendering_abexa.md)

## Methods for Token-Based Rendering

The following methods are declared in the interface `IF_SXML_WRITER` for token-based rendering:

- `OPEN_ELEMENT` - Writes an element opening. The name, a namespace prefix, and a namespace URI can be passed.

- `WRITE_NAMESPACE_DECLARATION` - Writes a namespace declaration to an element opening.

- `WRITE_ATTRIBUTE` - Writes an XML attribute to an element opening. A name, namespace prefix, a namespace URI, and a character-like value can be passed.

- `WRITE_ATTRIBUTE_RAW` - Writes an XML attribute with raw data to an element opening. A name, namespace prefix, a namespace URI, and a byte-like value can be passed.

- `WRITE_VALUE` - Writes a character-like value behind an element opening.

- `WRITE_VALUE_RAW` - Writes a byte-like value behind an element opening.

- `CLOSE_ELEMENT` - Writes an end of element.

If text-like data is written, this data is converted automatically from the current system code page to the representation of the XML data, which is determined by the chosen [format](abenabap_sxml_lib_formats.md). If byte-like raw data is written, this data is also converted in accordance with the chosen [format](abenabap_sxml_lib_formats.md), for example to the format [Base64](../../abap-glossary/abenbase64_glosry.md) for XML 1.0 or to the binary part of the XOP package for [XOP](../../abap-glossary/abenxop_glosry.md).

### Executable Example

[Namespace Declarations in Token-Based Rendering](abensxml_renderering_ns_abexa.md)
