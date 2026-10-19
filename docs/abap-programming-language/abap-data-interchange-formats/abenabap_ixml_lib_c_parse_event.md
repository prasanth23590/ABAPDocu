---
title: "iXML - Sequential Parsing"
source_file: abenabap_ixml_lib_c_parse_event.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud > iXML - Parsing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Sequential Parsing

To parse XML data sequentially, a dedicated [parser](abenabap_ixml_lib_c_parse.md) is called repeatedly as follows:

`DATA(event) = parser->parse_event( ).`

Here, `parser` is a reference variable that points to the parser. The method `PARSE_EVENT` returns a reference variable with the type `IF_IXML_EVENT` that points to an object that represents an event that occurred during parsing. The parser processes the input stream [`istream`](abenabap_ixml_lib_c_input_output.md) in sequences defined by the events for which the caller registered itself previously. The possible events are stored as constants `co_event...` in the interface `IF_IXML_EVENT`. They are registered using the method

``` abap
parser->set_event_subscription( events = if_ixml_event=>co_event... + 
                                         if_ixml_event=>co_event... + 
                                         ... ).
```

The parser stops after every event registered in this way and returns the properties of the current sequence using the object referenced by `event`. The method `PARSE_EVENT` must be called again to process the next sequence. If all XML data has been parsed or if an error occurs, the return value of `PARSE_EVENT` is initial.

By default, DOM-based XML documents are constructed bit by bit in the memory during sequential processing. Once processing is complete, they are available in the same ways as after the method [`PARSE`](abenabap_ixml_lib_c_parse_dom.md). [Troubleshooting](abenabap_ixml_lib_c_parse_error.md) is also similar. During sequential parsing, the document represents a valid XML document with the elements parsed up until now. If sequential parsing is ended before all elements of the input stream have been processed, the XML document represents the part of the input stream parsed so far. The method `SET_DOM_GENERATING` of the parser can be used to deactivate the generation of the DOM representation.

## Hints

- A parsing event is an iterator concept and not an event raised by [`EVENTS`](../abap-declarations/abapevents.md) in ABAP Objects.

- If the caller does not register any events before `PARSE_EVENT` is called, `PARSE_EVENT` works like `PARSE`.

- The sequential parsing described here is not a variant of SAX (Simple API for XML). Callback methods are not called when an event occurs.
