---
title: "iXML - Troubleshooting After Parsing"
source_file: abenabap_ixml_lib_c_parse_error.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud > iXML - Parsing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - Troubleshooting After Parsing

If a parser detects errors in the XML data to be parsed, its method `NUM_ERRORS` returns the number of errors. These can be analyzed using the objects created as follows:

`DATA(error) = parser->get_error( index = ... )`.

The static type of the reference variable `error` is then the interface `IF_IXML_PARSE_ERROR_CORE`. The number of the error can be passed to the parameter `index`. Counting begins at zero. If `index` has any other values, `error` remains initial.
