---
title: "iXML - Direct Reads"
source_file: abenabap_ixml_lib_c_dom_direct_r.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud > iXML - Access to DOM > iXML - DOM Reads"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Direct Reads

Direct reads can be used to create references to the node objects in DOM. These references can then be used to access methods and to get the properties of the nodes. Here, any node can be used as the starting point for access to its subnodes.

- [Access by Root Element](abenabap_ixml_lib_c_dom_direct_r.md#access-by-root-element)

- [Access to Subnodes](abenabap_ixml_lib_c_dom_direct_r.md#access-to-subnodes)

  - [Access to Adjacent Subnodes](abenabap_ixml_lib_c_dom_direct_r.md#access-to-adjacent-subnodes)

  - [Access Using Node Lists](abenabap_ixml_lib_c_dom_direct_r.md#access-using-node-lists)

- [Access Using Element Names](abenabap_ixml_lib_c_dom_direct_r.md#access-using-element-names)

- [Access to Attributes](abenabap_ixml_lib_c_dom_direct_r.md#access-to-attributes)

  - [Attribute Access Using Lists](abenabap_ixml_lib_c_dom_direct_r.md#attribute-access-using-lists)

  - [Short Forms for Attribute Access](abenabap_ixml_lib_c_dom_direct_r.md#short-forms-for-attribute-access)

## Access by Root Element

The root element of the DOM, which represents the root element of the represented XML data, can be used as the initial node. The root element of an existing XML document that points to a reference variable `document` can be accessed as follows:

`DATA(element) = document->get_root_element( ).`

The static type of the reference variable `element` is then `IF_IXML_ELEMENT` and points to the node object of the root element. The subnodes are now accessed from this node object.

## Access to Subnodes

There are two basic methods of accessing subnodes:

### Access to Adjacent Subnodes

The method `GET_FIRST_CHILD` of the interface `IF_IXML_ELEMENT` returns the first subnode for an element:

`DATA(child) = element->get_first_child( ).`

The static type of the reference variable `child` is then `IF_IXML_NODE` and it points to the node object of the first subnode. If there are no subnodes, `child` is initial.

The method `GET_NEXT` of the interface `IF_IXML_NODE` returns the next adjacent node and can be used to read all subnodes in sequence:

`DATA(next_child) = child->get_next( ).`

The static type of the reference variable `next_child` is also `IF_IXML_NODE`. If no adjacent node is found, `child_next` is initial.

### Access Using Node Lists

The method `GET_CHILDREN` of the interface `IF_IXML_ELEMENT` returns a list of all subnodes for any element:

`DATA(children) = element->get_children( ).`

The static type of the reference variable `children` is then `IF_IXML_NODE_LIST` and points to an object containing an indexed list of subnodes. These subnodes can be accessed as follows:

`DATA(child) = nodes->get_item( index )`.

The static type of the reference variable `child` is then `IF_IXML_NODE` and it points to the subnode specified by the number `index`, where the count begins at zero.

### Hint

In sequential access to adjacent nodes, access to the node list is also optimized.

## Access Using Element Names

If the name is known of an element of an existing XML document pointed to by a reference variable `document`, it can be searched for as follows:

`DATA(element) = document->find_from_name_ns( name = ... ).`

The static type of the reference variable `element` is then `IF_IXML_ELEMENT` and it points to the node object that represents the first element being searched for. If the element is not found, `element` is initial. The optional parameter `DEPTH` of the method `FIND_FROM_NAME_NS` enables the search depth to be restricted.

A further method of the document interface can be used to collect all elements of a name. This method also enables the search depth to be restricted:

`DATA(elements) = document->get_elements_by_tag_name_ns( name = ... ).`

The static type of the reference variable `elements` is then `IF_IXML_NODE_COLLECTION` and points to an object containing an indexed list of the found elements. These subnodes can be accessed as follows:

`DATA(node) = item->get_item( index ).`

The static type of the reference variable `node` is then `IF_IXML_NODE` and it points to the node specified by the number `index`, where the count begins at zero.

## Access to Attributes

There are various methods for accessing the attributes of elements in DOM.

### Attribute Access Using Lists

A reference variable `node` with the type `IF_IXML_NODE`, which points to a node object, can be used to create a list of the attributes of the node as follows:

`DATA(attributes) = node->get_attributes( ).`

The static type of the reference variable `attributes` is then `IF_IXML_NAMED_NODE_MAP` and points to an object containing an indexed list of the attributes. These attributes can be accessed as follows:

`DATA(attribute) = attributes->get_item( index ).`

The static type of the reference variable `attribute` is then `IF_IXML_ATTRIBUTE` and it points to the object specified by the number `index`, where the count begins at zero.

Instead of the index, the lists of attributes can also be read using the attribute name:

`DATA(attribute) = attributes->get_named_item_ns( name = ... ).`

`attribute` then points to the object of attribute specified by the name or is initial.

### Short Forms for Attribute Access

Instead of first creating a list of the attributes, they can also be read directly from an element, using their names. A reference variable `element` with the type `IF_IXML_ELEMENT`, which points to an element, can be used to read an attribute as follows:

`DATA(attribute) = element->get_attribute_node_ns( name = ... )`.

The static type of the reference variable `attribute` is then `IF_IXML_ATTRIBUTE` and it points to the object of the attribute specified by the name or is initial.

It is also possible to write only the value of the attribute to a text string directly:

`DATA(value) = element->get_attribute_ns( name = ... ).`

The type of `value` is then `string` and contains the value of the attribute or is initial.

### Hint

Before the short forms with reference variables with the type `IF_IXML_NODE` can be executed, a downcast must be performed to the type `IF_IXML_ELEMENT`, because these methods are only contained in this interface.
