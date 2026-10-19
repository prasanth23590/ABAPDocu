---
title: "XSL - User-Defined XSLT Serializations and Deserializations"
source_file: abenabap_xslt_user_def_serial.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > XSL Transformations > XSL - Serialization from and Deserialization to ABAP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# XSL - User-Defined XSLT Serializations and Deserializations

The following image shows the mapping of an XML tree to an ABAP tree using an XSLT program and the mapping of an ABAP tree to an XML tree using an identity transformation and an XSLT program. ![figure](images_abdoc_asxml.gif)

- In the case of transformations that use ABAP data as a source, the ABAP data is first serialized to a canonical [XML representation (asXML)](abenabap_xslt_asxml.md) with the predefined [identity transformation](abenabap_xslt_id.md) `ID`. This intermediate result is then used as the actual source for the XSL transformation. If the transformation `ID` itself is called in `CALL TRANSFORMATION`, the intermediate result is in the direct output.

- In the case of transformations that have ABAP data as a result, the result of the XSL transformation is deserialized directly to the ABAP data. A prerequisite for the deserialization is that the result represents a canonical XML representation. When transforming XML to ABAP, there are also two conceptual steps: First, a virtual asXML structure is transformed and then deserialized. Technically, these take place in only one transformation step.

## Executable Examples

[XSL Transformations](abenxslt_spec_abexa.md)

[XSL Transformations Using Parameters](abenxslt_parameters_abexa.md)

[XSL Transformations Using ABAP Method Calls](abenxslt_abap_abexa.md)
