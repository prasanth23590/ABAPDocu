---
title: "ST - Literal XML Elements and Attributes"
source_file: abenst_xml_literals.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Literal Template Content"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Literal XML Elements and Attributes

Literal XML elements are XML elements that are not ST statements or that are not in the namespace `http://www.sap.com/transformation-templates` (namespace prefix `tt`). Attributes of literal XML elements that are not in this namespace are called literal attributes.

During serialization, literal XML elements and their literal attributes are passed to the target XML document unchanged. In deserializations they are compared with the XML source document word by word. In addition to the literal attributes, literal XML elements can also contain certain attributes with the namespace prefix `tt`, that is, ST-specific attributes, to set the current node and to control behavior during deserialization.

- [ST - General Literal XML Elements](abenst_xml_literals_general.md)

- [ST - Special Form of Literal XML Elements](abenst_xml_literals_special.md)
