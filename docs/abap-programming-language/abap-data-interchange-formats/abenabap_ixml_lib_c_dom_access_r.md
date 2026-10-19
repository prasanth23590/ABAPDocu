---
title: "iXML - DOM Reads"
source_file: abenabap_ixml_lib_c_dom_access_r.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Class Libraries > iXML Library for ABAP Cloud > iXML - Access to DOM"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# iXML - DOM Reads

## Hints

- iXML documents and their nodes can also be specified as an XML source for XSL transformations called using [`CALL TRANSFORMATION`](abapcall_transformation.md) so that they are also read.

- If the content of elements or attributes contain the notations `&lt;`, `&gt;`, `&amp;`, `&quot;`, or `&apos;`, they are transformed automatically to the corresponding [characters](abenxml_oview.md) when read.
