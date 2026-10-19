---
title: "iXML - Streams and Documents"
source_file: abenabap_ixml_lib_c_input_output.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Streams and Documents

- [Input Streams and Output Streams](abenabap_ixml_lib_c_input_output.md#input-streams-and-output-streams)

- [XML Documents](abenabap_ixml_lib_c_input_output.md#xml-documents)

## Input Streams and Output Streams

Input streams are used for the input of XML data into the parser and output streams are used to pass XML data from the renderer. A factory is needed to create a stream, which can be created using the iXML factory as follows:

``` abap
DATA(ixml) = cl_ixml_core=>create( ). 
... 
DATA(stream_factory) = ixml->create_stream_factory( ).
```

The static type of the reference variable `stream_factory` is then the interface `IF_IXML_STREAM_FACTORY_CORE`, which contains factory methods `CREATE_ISTREAM_...` for input streams and `CREATE_OSTREAM_...` for output streams.

Different streams can be created for different data sources and data sinks, such as strings, internal tables, or files specified by URIs.

### Hints

- iXML input streams can be specified as an XML source and iXML output streams can be used as an XML target for XSL transformations called using [`CALL TRANSFORMATION`](abapcall_transformation.md).

- If output streams are bound to internal tables with byte-like line types, the last line is not usually filled completely with content from the stream. The length of the actual data in the line can be determined using the return value of the method `GET_NUM_WRITTEN_RAW` of the output stream modulo of the number of table lines.

## XML Documents

Each XML document stored in DOM format in the memory is managed using a separate object. An object of this type can be created as follows:

``` abap
DATA(ixml) = cl_ixml_core=>create( ). 
... 
DATA(document) = ixml->create_document( ).
```

The static type of the reference variable `document` is `IF_IXML_DOCUMENT`. A document created in this way

- is used to address an XML document stored as DOM,

- can be bound to the parser to fill it,

- can be used to construct new XML data or modify existing data,

- can be passed to the renderer to be output.

### Hint

iXML documents can be defined as an XML target, iXML documents and their nodes can be specified as an XML source for XSL transformations called using [`CALL TRANSFORMATION`](abapcall_transformation.md).
