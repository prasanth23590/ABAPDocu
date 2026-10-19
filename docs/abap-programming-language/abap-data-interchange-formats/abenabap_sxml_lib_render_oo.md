---
title: "sXML - Object-Oriented Rendering"
source_file: abenabap_sxml_lib_render_oo.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > sXML Library > sXML - Rendering"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sXML - Object-Oriented Rendering

Just as in [token-based rendering](abenabap_sxml_lib_render_token.md), object-oriented rendering creates an XML writer. The nodes are not written, however, using a separate method for each node type, but using a single method, `WRITE_NODE`. This method is linked with a node object with the required [node type](abenabap_sxml_lib_entities.md) using its input parameters and a corresponding node is appended to the current write position.

- [Basic Approach](abenabap_sxml_lib_render_oo.md#basic-approach)

- [Methods for Object-Oriented Rendering](abenabap_sxml_lib_render_oo.md#methods-for-object-oriented-rendering)

## Basic Approach

As in [token-based rendering](abenabap_sxml_lib_render_token.md), the XML writer is created using the factory method `CREATE` of the required class, for example:

`DATA(writer) = CAST if_sxml_writer( cl_sxml_string_writer=>create( ... ) ).`

Before the node object is written, it can be created using one of the dedicated methods of the interface `IF_SXML_READER`, such as `NEW_OPEN_ELEMENT`, `NEW_CLOSE_ELEMENT`, and `NEW_VALUE` or it can be taken from another source, such as an object-oriented read, for example:

``` abap
DATA(open_element) = writer->new_open_element( ... ). 
writer->write_node( open_element ). 
DATA(value) = writer->new_value( ). 
value->set_value( ... ). 
writer->write_node( value ). 
DATA(close_element) = writer->new_close_element( ... ). 
writer->write_node( close_element ).
```

The node object of an element opening has methods that can be used to insert XML attributes.

### Executable Example

[Object-Oriented Rendering](abensxml_oo_rendering_abexa.md)

## Methods for Object-Oriented Rendering

The following methods of the interface `IF_SXML_WRITER` are designed specifically for object-oriented rendering:

- `NEW_OPEN_ELEMENT` - Creates a node object for an element opening.

- `NEW_VALUE` - Creates a node object for a character-like value.

- `NEW_VALUE_RAW` - Creates a node object for byte-like raw data.

- `NEW_CLOSE_ELEMENT` - Creates a node object for an end of element.

- `WRITE_NODE` - Creates a node in accordance with the passed node object.

The values are written as in [token-based rendering](abenabap_sxml_lib_render_token.md).

### Hints

- [Token-based rendering](abenabap_sxml_lib_render_token.md) and object-oriented rendering are not strictly separated. The corresponding methods for writing nodes can be called alternately in the same program. This is not recommended, however, for reasons of readability.

- In object-oriented rendering, node objects can be written directly that were returned by an [object-oriented parser](abenabap_sxml_lib_parse_oo.md) and possibly modified.

- Object-oriented rendering can demonstrate poorer performance than token-based rendering due to the extra objects that are created.

## Executable Examples

- [Modifying XML Data](abensxml_reader_writer_abexa.md)

- [Transforming JSON Names](abenabap_json_names_to_upper_abexa.md)
