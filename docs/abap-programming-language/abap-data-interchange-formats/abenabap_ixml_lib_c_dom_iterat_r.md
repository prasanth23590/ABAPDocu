---
title: "iXML - Reads Using Iterators"
source_file: abenabap_ixml_lib_c_dom_iterat_r.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud > iXML - Access to DOM > iXML - DOM Reads"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Reads Using Iterators

The section [Direct Read](abenabap_ixml_lib_c_dom_direct_r.md) demonstrates how to access the DOM nodes directly using the following objects:

- Objects with the `IF_IXML_NODE` interface for individual nodes

- Objects with the `IF_IXML_NODE_LIST` interface for lists of subnodes

- Objects with the `IF_IXML_NODE_COLLECTION` interface for lists of element names

- Objects with the `IF_IXML_NAMED_NODE_MAP` interface for lists of attributes

An iterator can be created for each of these objects. This iterator makes it possible to iterate using the DOM elements represented by the objects. The interface of every iterator provides the same options for accessing the objects iterated by the iterator.

- [Iterator for Nodes](abenabap_ixml_lib_c_dom_iterat_r.md#iterator-for-nodes)

- [Iterators for Lists](abenabap_ixml_lib_c_dom_iterat_r.md#iterators-for-lists)

## Hint

The iterators shown here are forward iterators that iterate from left to right or from top to bottom. The interfaces of the objects also make it possible to create backward iterators, which iterate from right to left or from bottom to top.

## Iterator for Nodes

A reference variable `document` with the type `IF_IXML_NODE`, which points to an XML document, can be used to create an iterator for all the nodes of the document as follows:

`DATA(iterator) = document->create_iterator( [depth] ).`

The static type of the reference variable `iterator` is then `IF_IXML_NODE_ITERATOR` and it points to the iterator whose methods can iterate using the nodes. The optional input parameter `depth` can be used to specify the depth of the nodes in the tree structure that are to be used for the iteration. To create an iterator for iterating the subnodes of a specific node, it is possible to use a reference variable `node` of type `IF_IXML_NODE`, instead of `document`. This reference variable points to a node object.

Iterator nodes can be iterated using the following method:

`DATA(node) = iterator->get_next( ).`

The static type of the reference variable `node` is then `IF_IXML_NODE` and it points to the object of the current iterator node. If no more nodes exist, `node` is initial.

### Hints

- Unlike a node [direct read](abenabap_ixml_lib_c_dom_direct_r.md), which can be restricted to the elements of the represented XML data, an iterator captures all nodes in an XML document, including nodes that only contain structural information. The method `GET_TYPE` of interface `IF_IXML_NODE` should be used to read the node type and compare it to constants of this interface. [Filter](abenabap_ixml_lib_c_dom_filter_r.md) or Downcasts provide further options for only selecting specified nodes.

- In addition to the iterator for subnodes shown here, an inline iterator is also available with the interface `IF_IXML_INLINE_ITERATOR` for iterating neighboring nodes.

## Iterators for Lists

An iterator can be created for all of the lists under [Direct Read](abenabap_ixml_lib_c_dom_direct_r.md):

- Node list (`IF_IXML_NODE_LIST`)

- Element list (`IF_IXML_NODE_COLLECTION`)

- Attribute list (`IF_IXML_NAMED_NODE_MAP`)

  `DATA(iterator) = {nodes|elements|attributes}->create_iterator( ).`

In all three cases, the reference variable has the static type `IF_IXML_NODE_ITERATOR` and points to an iterator for the elements of the relevant list. This iterator can be used as shown above.

### Hint

Since the lists only contain the required elements, it is usually not necessary to query the type, as is the case when iterating the entire document or subtrees.
