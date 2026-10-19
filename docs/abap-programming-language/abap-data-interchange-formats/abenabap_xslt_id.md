---
title: "XSL - Identity Transformation"
source_file: abenabap_xslt_id.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > XSL Transformations > XSL - Serialization from and Deserialization to ABAP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# XSL - Identity Transformation

Under the name `ID`, SAP provides an identity transformation that is specially handled by the runtime framework depending on the source and target:

- An identity transformation from XML to XML produces a result that is a normalized copy of the source document in which the attributes of an element are sorted alphabetically.

- An identity transformation from ABAP to XML produces the canonical XML representation ([asXML](abenabap_xslt_asxml.md)) of the ABAP data (explicit serialization).

- An identity transformation from XML to ABAP transforms a canonical XML representation to ABAP data (explicit deserialization).

- In the case of an identity transformation with [JSON](../../abap-glossary/abenjson_glosry.md) data as an XML source or an [JSON writer](../../abap-glossary/abenjson_writer_glosry.md) as an XML target, a special type of [handling](abenabap_json_trafo_id.md) is performed for [JSON](../../abap-glossary/abenjson_glosry.md).

In each transformation from XML, the identity transformation validates the outbound data. If an XML element has multiple identically named attributes, only one of these is respected, which is given the value of the last identically named attribute (see example class `CL_DEMO_XML_ATTRIBUTES`). The identity transformation implicitly uses canonical XML formats for all transformations apart from XML to XML to transform non-XML data (ABAP, JSON) into the XML format. The identity transformation is used internally for this purpose and can also be called explicitly if the formats it creates are sufficient or are to be analyzed.

## Hints

- The identity transformation `ID` is not completely symmetrical. When text strings that contain only blanks are serialized, a node with the same number of blanks is created. When nodes that contain only spaces (such as blanks or line breaks) are deserialized, however, an empty text is created.

- The identity transformation `ID` exists as an XSLT program in the repository, but this program is not always executed. When the identity transformation `ID` is called, an optimized ID engine of the runtime framework might be called, depending on the source and target. This ID engine creates the result described above.

- If the identity transformation `ID` is used, the way element names are written in XML or object names written in JSON cannot be modified. If XML data or JSON data is to be deserialized to ABAP data, however, the names of the corresponding elements or objects must be in uppercase letters. If this is not the case in the source data, either transformations must be created, or the data must be modified in advance.

## Executable Example

[Identity Transformation to the asXML Format](abenxslt_abexa.md)
