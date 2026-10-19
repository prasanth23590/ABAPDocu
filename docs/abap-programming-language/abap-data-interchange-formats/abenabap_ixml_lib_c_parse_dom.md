---
title: "iXML - Complete Parse to DOM"
source_file: abenabap_ixml_lib_c_parse_dom.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud > iXML - Parsing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Complete Parse to DOM

To parse XML data to a DOM representation in a single action, a [parser](abenabap_ixml_lib_c_parse.md) created for this purpose is used as follows:

`DATA(rc) = parser->parse( ).`

Here, `parser` is a reference variable that points to the parser. The parser checks whether the XML data of the input stream [`istream`](abenabap_ixml_lib_c_input_output.md) is correct and creates a DOM representation of this file in the memory. The return value of the method `PARSE` has the type `i`.

If the parsing is successful, the XML document [`document`](abenabap_ixml_lib_c_input_output.md) linked with the parser can be used to [access the DOM](abenabap_ixml_lib_c_dom_access.md) stored in the memory.

## Hints

- If an XML element has multiple attributes with the same name, only one of these attributes is passed to DOM, which is given the value of the last identically named attribute.

- An alternative for complete parsing of XML data to the DOM representation is to call the [identity transformation](../../abap-glossary/abenid_trafo_glosry.md) `ID` with [`CALL TRANSFORMATION`](abapcall_transformation.md). No streams and factories need to be created explicitly here.
