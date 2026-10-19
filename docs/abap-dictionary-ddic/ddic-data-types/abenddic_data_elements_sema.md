---
title: "DDIC - Semantic Properties of Data Elements"
source_file: abenddic_data_elements_sema.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types > DDIC - Data Elements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Semantic Properties of Data Elements

The semantic properties of data elements are mainly significant when they are used as types of fields on user interfaces. The only exceptions to this are the default component name and the flag for the change document. ABAP data objects declared with reference to a data element ignore the semantic properties of the data element.

- **Short text**

  Short text of the data element.

- **Field label**

  The short, medium, and long field labels assigned to a data element, as well as the header, can be used on screens as descriptions or column names for fields defined with direct or indirect reference to a data element. A user-defined maximum length, which has varying upper limits for the different field labels, must be set. It applies to all languages.

- **Documentation**

  Documentation of the data element.

- **Documentation status**

  The status of the documentation for a data element can be noted as follows for any check tools:

  - **Object is documented**

    The default setting, indicating that the data element has documentation.

  - **Object not used on a screen**

    The data element is not intended for screen fields and no documentation is required.

  - **Object is documented by its short text.**

    The short text provides enough documentation.

  - **Documentation is currently on hold**

    The data element requires documentation, but it does not yet exist.

- **Search help**

  A data element with an elementary data type can be assigned a [search help](../../abap-glossary/abensearch_help_glosry.md) and a parameter can be passed to this search help. Search helps cannot be assigned to a data element with a reference type.

- **SPA/GPA parameter**

  A data element with an elementary data type can be linked with an SPA/GPA parameter. A data element with a reference type cannot be linked with an SPA/GPA parameter.

- **Flag for input history**

  The flag for the input history defines whether the input history is active for fields defined with direct or indirect reference to the data element. This makes it possible to switch the input history off for sensitive fields.

- **Flag for bidirectional fonts**

  These flags define the behavior of fields defined with direct or indirect reference to the data element when handling bidirectional fonts (such as Hebrew or Arabic).

  - **Writing direction**

    This flag can specify the writing direction of a field as *from left to right*, which overwrites the direction *from right to left* specified by logons in a bidirectional font. This flag can be useful for fields with numeric texts.

  - **BIDI filter**

    This flag can be used to prevent the Unicode formatting characters that affect the writing direction of bidirectional fonts in data transports between GUI and AS ABAP from being filtered out, regardless of the global system settings. The global system setting is made in the program `I18N_SET_DATAELEMENT_FLAGS`.

- **Default component name**

  The default component name of a data element is a naming suggestion for structure components or table fields defined with reference to this data element. Structures used in APIs in particular should follow this proposal.

- **Flag for change document**

  The flag for change documents specifies whether changes to fields in DDIC database tables defined with reference to this data element are logged when change document objects are involved. A change document object groups multiple tables and is used to generate function modules that can be integrated into ABAP programs and that log changes. This flag cannot be set for data elements with a reference type.

- Further semantic properties can be defined in the [domain](abenddic_domains.md) referenced by a data element.

The texts in the semantic properties (the short text, field labels, and documentation) are, like all AS ABAP texts, connected to the translation tools.
