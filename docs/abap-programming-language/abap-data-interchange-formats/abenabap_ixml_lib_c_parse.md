---
title: "iXML - Parsing"
source_file: abenabap_ixml_lib_c_parse.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Parsing

XML data is parsed by a validating XML parser, which can be created using the iXML factory as follows:

``` abap
DATA(ixml)  = cl_ixml_core=>create( ). 
 
... 
 
DATA(parser) = ixml->create_parser( 
                 document       = ... 
                 istream        = ... 
                 stream_factory = ... ).
```

The static type of the reference variable `parser` is then the interface `IF_IXML_PARSER_CORE`. The parser requires the following input parameters:

- An XML document [`document`](abenabap_ixml_lib_c_input_output.md), to which the stream is parsed.

- The input stream [`istream`](abenabap_ixml_lib_c_input_output.md) to be parsed.

- A factory [`stream_factory`](abenabap_ixml_lib_c_input_output.md) must be specified for streams. This enables the parser to create corresponding streams if external sources are addressed in the parsed document.

A parser created in this way works like an iterator on the input stream. XML data can be parsed to a DOM representation in a single action or sequential parsing can be used, where the parser stops after certain steps and passes control to the application.

## Hint

A parser can only be used once for the associated input stream and the associated XML document. Once it has parsed the input stream to a document, the parser can be passed to the garbage collector. A parser cannot be reused for the same XML data or for any other data.
