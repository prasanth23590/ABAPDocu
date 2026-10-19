---
title: "iXML - DOM Writes"
source_file: abenabap_ixml_lib_c_dom_access_w.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud > iXML - Access to DOM"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - DOM Writes

Writes enable an XML document to be constructed from scratch in the memory or an existing document to be modified. The most important methods used for constructing a DOM create elements and add attributes to elements. These methods are declared in the interface `IF_IXML_DOCUMENT` and are briefly introduced here. Other methods are used to remove elements from a DOM, which is described in the interface documentation.

- [Adding Nodes](abenabap_ixml_lib_c_dom_access_w.md#adding-nodes)

- [Adding Elements](abenabap_ixml_lib_c_dom_access_w.md#adding-elements)

- [Adding Attributes](abenabap_ixml_lib_c_dom_access_w.md#adding-attributes)

## Hints

- Writes to the DOM must be avoided during [sequential parsing](abenabap_ixml_lib_c_parse_event.md), since this can produce undefined behavior.

- iXML documents can also be specified as an XML target for XSL transformations called using [`CALL TRANSFORMATION`](abapcall_transformation.md).

- If writes produce content of elements or attributes, the characters *\<*, *\>*, *&*, *"*, and *'* are transformed automatically to the associated [XML](abenxml_oview.md) notation.

## Adding Nodes

Nodes are usually added to existing nodes as subnodes. To create an element, a reference variable `document` with type `IF_IXML_DOCUMENT` that points to an XML document can be used to call the following method:

`element = document->create_element_ns( name = ... ).`

The static type of the reference variable `element` is then `IF_IXML_ELEMENT` and it points to an element called `name` that is not yet part of the tree structure. The following call can be used to insert the element in the tree structure:

`parent->append_child( element ).`

Here, `parent` is a reference variable that points to an existing node object of the XML document. A reference variable, `document`, can be specified for `parent` for the document itself as an access point to an empty document.

The elements created using `CREATE_ELEMENT_NS` are empty. The following method can be used to create content:

`DATA(text) = document->create_text( ... )`.

The static type of the reference variable `text` is then `IF_IXML_TEXT` and it points to literal content that is not yet part of the tree structure. This can be inserted in an element using the method `APPEND_CHILD`.

## Adding Elements

The steps above used to add content to an element

- create element

- add element

- create content

- add content

can also be performed using a single method call as follows:

``` abap
element = document->create_simple_element_ns( 
            name   = ... 
            value  = ... 
            parent = ... ).
```

This creates the element, with the content passed to `value`, and appends it to the node passed to `parent` as a subnode. For this reason, the individual steps described above are generally only used for more specific tasks.

## Adding Attributes

The following method can be used to add an attribute to an element of an XML document to which a reference variable `element` points:

`element->set_attribute_ns( name = ... value = ... ).`

This creates an attribute called `name` with the value passed to `value`.

## Executable Examples
