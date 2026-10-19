---
title: "asXML - Mapping of Internal Tables"
source_file: abenabap_xslt_asxml_table.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML) > asXML - Mapping of ABAP Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asXML - Mapping of Internal Tables

The asXML representation of internal tables is significant mainly for XSL transformations. In Simple Transformations, this representation is important only when using the statement [`tt:copy`](abenst_tt_copy.md).

The lines of an internal table are represented in asXML as a sequence of subelements of the table element. The content of each subelement matches the canonical representation of the line value. The name of a subelement is not relevant. If the canonical XML representation is created by a serialization, the name from the ABAP Dictionary is used when it is referred to, otherwise the name is `item`. All table categories are allowed. Serializations do not pass any information about the table category to the XML data. If the target field of an [XSL transformation](../../abap-glossary/abenxsl_transformation_glosry.md) is a [sorted table](../../abap-glossary/abensorted_table_glosry.md), the lines are sorted accordingly in the deserialization.

If the required XML element does not exist in deserializations to an internal table, the internal table retains its previous content. If an empty element is assigned to an internal table, it is set to its type-dependent initial value, that is, it is emptied. To initialize the internal table in either case, the transformation option [`clear`](abapcall_transformation_options.md) with the value *all* can be used.

## Executable Example

[asXML, Mapping of Tables](abenasxml_table_abexa.md)
