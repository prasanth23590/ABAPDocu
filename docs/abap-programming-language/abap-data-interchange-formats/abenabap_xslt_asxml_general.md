---
title: "asXML - General Format"
source_file: abenabap_xslt_asxml_general.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Canonical XML Representation (asXML)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# asXML - General Format

The following lines show the general format of the [canonical XML](../../abap-glossary/abencanonical_xml_represent_glosry.md) representation without the XML header, whereby line breaks and indents were inserted for clarification purposes only.

The asXML format is a general format that cannot be completely defined by an XML pattern. The reason for this is that various ABAP types are referred to.

``` abap
<asx:abap version = "1.0" 
          xmlns:asx = "http://www.sap.com/abapxml"> 
  <asx:values> 
    <bn1>...</bn1> 
    <bn2>...</bn2> 
    ... 
  </asx:values> 
  <asx:heap> 
    ... 
  </asx:heap> 
</asx:abap>
```

The root element is `abap` in the namespace (XML namespace) `http://www.sap.com/abapxml`. The optional attribute `version` currently always has the value *1.0* and is intended for future enhancements of asXML. The root element `abap` must contain the subelement `values` of the same namespace. The subelements `bn1`, `bn2` ... of `values` represent the ABAP data objects specified in the addition `source` of the statement [`CALL TRANSFORMATION`](abapcall_transformation.md) as `e1` `e2` ... or in the addition `result` as `f1` `f2` ... The names of the elements `bn1`, `bn2`, ... are the names specified there in uppercase. The text content of the elements `<bn1>...</bn1>`, `<bn2>...</bn2>` ... (or `<bn1 ... />`, `<bn2 ... />` ...) represent the content of named data objects except reference variables in accordance with the mapping described in the following sections. Reference variables are represented by elements without content but with a special attribute. The optional element `heap` contains the content of referenced [anonymous data objects](../../abap-glossary/abenanonymous_data_object_glosry.md) and objects.

The format of the names of the elements `bn1`, `bn2` ... depend on their format in the ABAP runtime framework, with the exception of the special cases in the table below. When names are specified statically in the additions `source` and `result` of the statement `CALL TRANSFORMATION`, they are specified in uppercase letters. When specified dynamically in an internal table, the format depends on how the names are specified there.

The names specified in the statement `CALL TRANSFORMATION` (or components of structures or objects) can only be used as names for XML elements if they contain only the characters *a* to *z*, *A* to *Z*, *0* to *9*, or *\_*, with the first character being a letter or *\_*. Other characters are replaced in accordance with the following table.

| **Character in ABAP Name**                                                                                                | **Escape Character in XML Name**                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ASCII characters other than *a* to *z*, *A* to *Z*, *0* to *9*, or *\_* and characters *0* to *9* as the first character. | *\_--hex(c)*, where *hex(c)* is the two-character hexadecimal representation of the ASCII code for the character *c*. |
| */*                                                                                                                       | *\_-*                                                                                                                 |
| *XML* as the first three characters in any combination of uppercase and lowercase letters.                                | *X-ML* in the appropriate combination of uppercase and lowercase letters.                                             |

## Executable Example

[Example of an Identity Transformation](abenxslt_abexa.md)
