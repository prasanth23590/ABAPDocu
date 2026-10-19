---
title: "sXML - Parsing"
source_file: abenabap_sxml_lib_parse.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - Parsing

XML data can be read using sXML Library or its syntax checked by being linked with an XML reader and using its methods. A reader like this is validating, meaning that invalid XML data raises an [exception](abenabap_sxml_lib_exceptions.md). It interprets the XML data as a hierarchical tree-like structure where each token is represented by a node assigned uniquely to a subnode (see [W3C Information Set](http://www.w3.org/TR/xml-infoset/)). An element with a literal value, for example, is interpreted as follows:

``` abap
| 
|--CO_NT_ELEMENT_OPEN 
|    | 
|    |--CO_NT_VALUE 
| 
|--CO_NT_ELEMENT_CLOSE
```

The value is a subnode of the node that represents the opening of an element. The names of the nodes here are the same as the constants of the interface `IF_SXML_READER` that describe the type of a node. The attributes of an element have a special task. They are assigned as a list to the node with the type `CO_NT_ELEMENT_OPEN` and can be accessed using special methods when the parser is on the opening of the element.

The [classes and interfaces](abenabap_sxml_lib_reader.md) in sXML Library available for parsing XML data are organized so that there are separate XML reader classes for different requirements. These classes inherit from the abstract superclass `CL_SXML_READER`. The abstract superclass contains implementations of functions required by all readers and includes the interface `IF_SXML_READER`, which contains the components shared by all readers. This interface enables all readers to be accessed in the same way. If special components need to be accessed that are not declared in the interface, a downcast must be used on the corresponding class.

The specialized reader classes are:

- `CL_SXML_STRING_READER`

  Readers in this class parse XML data in a byte string.

- `CL_SXML_TABLE_READER`

  Readers in this class parse XML data in an internal table with a flat byte-like line type.

The XML data to be parsed is passed to the factory method `CREATE` of each reader. Readers detect the [format](abenabap_sxml_lib_formats.md) and the character format of the data themselves. Instructions on standardization and handling empty space can be passed to the factory method if the format is suitable.

The methods of the interface `IF_SXML_READER` enable serial parsing of the passed XML data. There are two basic ways to do this:

- [Token-based parsing](abenabap_sxml_lib_parse_iterative.md)

- [Object-based parsing](abenabap_sxml_lib_parse_oo.md)

A reader cannot be used more than once for the same XML data or for other XML data. The read position of a reader is controlled during parsing using its methods. The actions allowed by a reader depend on its current read position. For example, a reader located at the end of the parsed XML data can no longer be used as an XML source of the statement `CALL TRANSFORMATION`. No method exists that can restore the reader to its initial state. A new reader can be created instead.

## Hints

- An XML reader in sXML Library can be specified as an XML source of the statement [`CALL TRANSFORMATION`](abapcall_transformation.md). This enables transformations to be performed for all sources supported by sXML readers in all supported [formats](abenabap_sxml_lib_formats.md). In particular, this makes it possible for [JSON data](abenabap_json.md) to also be consumed directly in ABAP data objects.

- The method `SKIP_NODE`, which can be used in both token-based and object-oriented parsing, offers various simple ways of checking the validity of a subtree or the entire tree or of copying a tree to a writer, whereby the format can be changed.

- If the content of elements or attributes contain the notations `&lt;`, `&gt;`, `&amp;`, `&quot;`, or `&apos;`, they are transformed automatically to the corresponding [characters](abenxml_oview.md) when parsed.

- The parser of the sXML Library is a more strict validator than the parser of the [iXML Library](abenabap_ixml_lib_cloud.md). A namespace prefix must be declared in the same element or in a superelement. Preceding declarations in a parallel element are interpreted as errors.

## Executable Example

[Deserialization with XML Reader](abensxml_trafo_from_reader_abexa.md)
