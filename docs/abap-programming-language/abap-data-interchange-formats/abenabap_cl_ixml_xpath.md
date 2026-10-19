---
title: "iXML - XPath Evaluation"
source_file: abenabap_cl_ixml_xpath.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - XPath Evaluation

The class `CL_IXML_XPATH` provides XPath evaluations only.

- [Static Method](abenabap_cl_ixml_xpath.md#static-method)

  - [`CREATE`](abenabap_cl_ixml_xpath.md#create)

- [Static Method](abenabap_cl_ixml_xpath.md#static-method)

  - [`IF_IXML_XPATH~EVALUATE_EXPRESSION`](abenabap_cl_ixml_xpath.md#if_ixml_xpathevaluate_expression)

## Static Method

### `CREATE`

**Input Parameters**

- `EXPRESSION` of type `STRING`

  Contains an [XPath](../../abap-glossary/abenxpath_regex_glosry.md) expression.

- `NSDECLARATIONS` of type `TT_NSDECLARATION` with the property `OPTIONAL`

  Internal table whose lines contain information about namespaces. The components of the lines are as follows:

  - `PREFIX`

    Prefix of a namespace.

  - `URI`

    URI of a namespace.

**Return Value**

- `RVAL` of type `REF TO if_ixml_xpath`

## Static Method

### `IF_IXML_XPATH~EVALUATE_EXPRESSION`

Method of interface `IF_IXML_XPATH` that evaluates an XPath expression.

**Input Parameters**

- `NODE` of type `REF TO if_ixml_node`

- `PARAMETERS` of type `sxsltepars` with the property `OPTIONAL`

- `IDS_ARE_ORDERED` of type `abap_bool`

**Return Value**

- `NODES` of type `REF TO if_ixml_node_collection`

### Hint

`CL_IXML_XPATH` can be used in ABAP for Cloud Development and Standard ABAP.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates the evaluation of the expression `f1:flight/f1:seat` within a namespace context.

``` abap
DATA xml_string TYPE string. 
DATA xml_xstring TYPE xstring. 
 
xml_string = `<?xml version="1.0"?>` && 
             `<f1:flight xmlns:f1="http://f1.docu/f">` && 
             `<f1:seat>83</f1:seat>` && 
             `</f1:flight>`. 
 
CALL TRANSFORMATION id 
  SOURCE XML xml_string 
  RESULT XML xml_xstring. 
 
FINAL(ixml) = cl_ixml_core=>create( ). 
FINAL(document) = ixml->create_document( ). 
FINAL(stream_factory) = ixml->create_stream_factory( ). 
 
FINAL(istream) = stream_factory->create_istream_xstring( xml_xstring ). 
FINAL(parser) = ixml->create_parser( document = document 
                                     istream = istream 
                                     stream_factory = stream_factory ). 
 
parser->parse(  ). 
 
FINAL(xpath) = cl_ixml_xpath=>create( expression = 'f1:flight/f1:seat' 
                                      nsdeclarations = VALUE #( ( 
                                        prefix = 'f1' 
                                        uri = 'http://f1.docu/f' ) ) 
                                    ). 
 
FINAL(node_list) = xpath->evaluate_expression( node = document ). 
 
FINAL(count) = node_list->get_length(  ). 
FINAL(node) = node_list->get_item( 0 ). 
FINAL(name) = node->get_name( ). 
FINAL(node_value) = node->get_value( ).
```
