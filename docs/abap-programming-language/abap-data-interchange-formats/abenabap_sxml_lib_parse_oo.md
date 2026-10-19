---
title: "sXML - Object-Oriented Parsing"
source_file: abenabap_sxml_lib_parse_oo.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library > sXML - Parsing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - Object-Oriented Parsing

Just as in [token-based parsing](abenabap_sxml_lib_parse_iterative.md), object-oriented parsing creates an XML reader and uses its methods to iterate across the XML data. Sometimes, however, other methods are used. The methods used for object-oriented parsing wrap methods for token-based parsing and provide object-oriented access to the current node. Instead of having to read the attributes of the reader directly after a parser step, the methods used for object-oriented parsing return references to objects that represent the current node. The methods and attributes of the [classes and interfaces](abenabap_sxml_lib_entities.md) of these objects can be used to access the properties of the node. Unlike in token-based parsing, only the relevant values are available.

- [Basic Approach](abenabap_sxml_lib_parse_oo.md#basic-approach)

- [Methods for Object-Oriented Parsing](abenabap_sxml_lib_parse_oo.md#methods-for-object-oriented-parsing)

## Basic Approach

An XML reader is created using the factory method `CREATE` of the required class, as in [token-based parsing](abenabap_sxml_lib_parse_iterative.md), and the source `xml` of the XML data is passed, for example:

`DATA(reader) = cl_sxml_string_reader=>create( xml ).`

In the simplest parsing case, the method `READ_NEXT_NODE` is applied as many times as it takes to reach the end of the XML data:

`DATA(node) = reader->read_next_node( ).`

The static type of the reference variable `node` is then `IF_SXML_NODE`, which points to a node object. The return value is initial at the end of the XML data. The attribute `TYPE` of the node object represents the type of the node in accordance with the constants `CO_NT_...` of the interface `IF_SXML_NODE`. This means that a downcast can be performed to a more specific reference variable for `node`, which makes it possible to access the properties of the current node. If the parser is located on the node of an element opening, the node object has the class `CL_SXML_OPEN_ELEMENT` with the interface `IF_SXML_OPEN_ELEMENT`. The methods of this interface enable access to the XML attributes of the element. For example, `GET_ATTRIBUTES` can be used to place references to attribute objects for all attributes in an internal table.

Any [exceptions](abenabap_sxml_lib_exceptions.md) should be caught and handled in a `TRY` control structure.

### Executable Example

[Object-Oriented Parsing](abensxml_oo_parsing_abexa.md)

## Methods for Object-Oriented Parsing

The following methods of the interface `IF_SXML_READER` are designed especially for object-oriented parsing. They return a reference with the static type `IF_SXML_NODE`, which points to a node object and can be cast to its more concrete object type.

- `READ_NEXT_NODE` - Like [`NEXT_NODE`](abenabap_sxml_lib_parse_iterative.md) but with the return value `NODE`.

- `READ_CURRENT_NODE` - Like [`CURRENT_NODE`](abenabap_sxml_lib_parse_iterative.md) but with the return value `NODE`.

If the current node is to be accessed after `PUSH_BACK`, the node object can be obtained using `READ_CURRENT_NODE`.

These methods are sufficient for all simple parsing tasks. For accessing XML attributes, a node object of an element opening contains the appropriate methods. To reset the parser to a preceding node or to parse the current node with its subnodes, the methods [`PUSH_BACK`](abenabap_sxml_lib_parse_iterative.md) and [`SKIP_NODE`](abenabap_sxml_lib_parse_iterative.md) can also be used here. Further token-based parsing methods should not usually be used at the same time.

### Hints

- [Token-based parsing](abenabap_sxml_lib_parse_iterative.md) and object-oriented parsing are not strictly separated. Methods such as `NEXT_NODE` and `READ_NEXT_NODE` can be called alternately in the same program. The attributes of the reader can always be used to access the properties of a node in object-oriented parsing too. This is not recommended, however, for reasons of readability.

- If an XML element has multiple identically named attributes, only one of these attributes is used in object-oriented parsing (unlike in [token-based parsing](abenabap_sxml_lib_parse_iterative.md)). This attribute has the value of the last identically named attribute (see example class `CL_DEMO_XML_ATTRIBUTES`).

- A node object returned in object-oriented parsing can be passed directly to an [object-oriented XML writer](abenabap_sxml_lib_render_oo.md).

- Object-oriented parsing is more convenient than token-based parsing, but the many extra objects that are created can affect performance negatively.
