---
title: "sXML - Token-Based Parsing"
source_file: abenabap_sxml_lib_parse_iterative.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library > sXML - Parsing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - Token-Based Parsing

In token-based parsing, the parser iterates across all nodes (tokens) in the tree structure of the XML data, one after the other. By default, the iterator passes across all subnode branches until the final node. The parser pauses after every iteration step on a node whose properties are available in the attributes of the XML reader. If the parser pauses on the node for an element opening, the list of the XML attributes there can be accessed.

- [Basic Approach](abenabap_sxml_lib_parse_iterative.md#basic-approach)

- [Methods and Attributes for Token-Based Parsing](abenabap_sxml_lib_parse_iterative.md#methods-and-attributes-for-token-based-parsing)

  - [Methods for Token-Based Parsing](abenabap_sxml_lib_parse_iterative.md#methods-for-token-based-parsing)

  - [Attributes for Token-Based Parsing](abenabap_sxml_lib_parse_iterative.md#attributes-for-token-based-parsing)

## Basic Approach

An XML reader is created using the factory method `CREATE` of the required class and by passing the source `xml` to the XML data, for example:

`DATA(reader) = cl_sxml_string_reader=>create( xml ).`

The static type of the reference variables is then the interface `IF_SXML_READER` and its methods and attributes can be addressed directly.

In the simplest parsing case, the method `NEXT_NODE` is applied as many times as it takes to reach the end of the XML:

`reader->next_node( ).`

Once the method is called, the attributes of the reader with the required properties of the node can be accessed directly. If the parser is on the node of an element opening, the method `NEXT_ATTRIBUTE` can be used to iterate across the list of attributes of an XML element:

`reader->next_attribute( ).`

After this method, the attributes of the reader object contain the name and the value of the current XML attribute. The end of the data is represented by the value of the constants `IF_SXML_NODE=>CO_NT_FINAL` in the attribute `NODE_TYPE`. Any [exceptions](abenabap_sxml_lib_exceptions.md) should be caught and handled in a `TRY` control structure.

### Executable Example

[Token-based parsing](abensxml_parsing_abexa.md)

## Methods and Attributes for Token-Based Parsing

### Methods for Token-Based Parsing

In addition to the simple iteration across nodes and attributes, the interfaces `IF_SXML_READER` offers several other methods for token-based parsing, summarized below:

- Methods for parsing using nodes

  - `NEXT_NODE` - Moves the parser to the next node

  - `CURRENT_NODE` - Resets the parser to the node for the element opening of the current node, if available. This method is ignored by value nodes or closed elements.

  - `PUSH_BACK` - Resets the parser to the node for the element opening of the direct parent node.

  - `SKIP_NODE` - Parses all nodes from a node for an element opening to the associated end of element. The parser is then at the end of the element. If required, the current node and all subnodes are passed to an XML writer. This method has no effect for value nodes or closed elements.

- Methods for reading the attribute list

  - `NEXT_ATTRIBUTE` - Reads the next attribute in the list

  - `NEXT_ATTRIBUTE_VALUE` - Sets the attribute `VALUE` or `VALUE_RAW` of the read explicitly to the value of the current attribute

  - `GET_ATTRIBUTE_VALUE` - Sets the attribute `VALUE` of the reader to the value of a specific attribute

### Hints

- The method `CURRENT_NODE` is most useful when reading an attribute list, to return to the start.

- If an XML element has multiple identically named attributes, all of these attributes are respected in the order in which they appear (see example class `CL_DEMO_XML_ATTRIBUTES`)

- Apart from simply skipping nodes, the method `SKIP_NODE` can also be used to check the subtrees or the entire tree for errors or to copy trees. In particular, the format of the copied tree or subtree can be transformed into a different format.

## Executable Examples

- [Steps in Token-Based Parsing](abensxml_parsing_steps_abexa.md)

- [Methods for token-based parsing](abensxml_parsing_methods_abexa.md)

### Attributes for Token-Based Parsing

The attributes of the reader with the properties of the current node are:

- `NODE_TYPE` - Node type in accordance with the constants of the interface `IF_SXML_NODE`

- `PREFIX` - Namespace prefix

- `NAME` - Element name

- `NSURI` - Namespace

- `VALUE_TYPE` - Type of the value in accordance with the constants of the interface `IF_SXML_VALUE`:

  - `CO_VT_TEXT` - Text data in the attribute `VALUE`

  - `CO_VT_TEXT` - Raw data in the attribute `VALUE_RAW`

- `VALUE` - Character-like value (if text data)

- `VALUE_RAW` - Byte-like value (if raw data)

The value of the constants `IF_SXML_NODE=>CO_NT_FINAL` in the attribute `NODE_TYPE` indicate that the end of the XML data was reached.

### Hints

- When parsing, the attributes of a reader are only overwritten by non-initial content. If the parser is set to a literal element without a name, for example, the preceding content of the attribute `NAME` is kept. This applies particularly to the attribute `VALUE`, which is not initialized if a node has no value.

- The attributes are declared in the interface `IF_SXML_READER`. In a reader class, they can also be addressed using alias names.
