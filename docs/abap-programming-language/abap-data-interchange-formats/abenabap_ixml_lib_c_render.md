---
title: "iXML - Rendering"
source_file: abenabap_ixml_lib_c_render.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Rendering

## Hint

When data is rendered as character-like XML data, this data is prefixed with the byte order mark (BOM) that is required by the XML standard.

## Rendering a Complete XML Document

An XML document in DOM representation is rendered using an XML renderer that can be created as follows using the iXML factory:

``` abap
DATA(ixml)  = cl_ixml_core=>create( ). 
 
... 
 
DATA(renderer) = ixml->create_renderer( 
                   ostream        = ... 
                   document       = ... ).
```

The static type of the reference variable `renderer` is then the interface `IF_IXML_RENDERER_CORE`. A separate renderer is needed for each XML document. The renderer requires the following input parameters:

- The output stream [`ostream`](abenabap_ixml_lib_c_input_output.md) that is the target of the rendering.

- The XML document [`document`](abenabap_ixml_lib_c_input_output.md) to be rendered.

A renderer created in this way can be used to render the entire XML document as follows:

`renderer->render( ).`

The rendered document is added to the data sink of the output stream.

### Hint

When the entire document is rendered, the data sink of the output stream should usually be initial beforehand. Otherwise, all the XML data is appended to existing content.
