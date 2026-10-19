---
title: "Exception Texts for System Classes"
source_file: abenexception_texts_internal.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Class-Based Exceptions > Exception Classes > Exception Texts"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Exception Texts for System Classes

**This function is for internal use only. Do not use it in application programs.**

If an exception class does not implement the interface `IF_T100_MESSAGE`, texts stored in OTR (Online Text Repository) are used as exception texts. These texts can be defined with any number of placeholders. Each placeholder is represented by the name of an attribute of the exception class, which is enclosed by the *&* characters. When the exception is raised, the placeholders are replaced by the content of the attributes. The maintenance of exception texts is only possible in one tool:

- The [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md) do not support any exception texts from OTR. No exception texts can be defined for the OTR and no UUIDs are created.

The input parameter `TEXTID` of the instance constructor has the data type `SOTR_CONC`. When an exception with these exception texts is raised, a UUID that identifies a text from OTR can be passed to the constructor. It is strongly recommended that only the constants that exist in the class for the predefined exception texts are passed, which selects a text defined for the exception. The attributes assigned to the placeholders of the text can be supplied with values using the input parameters of the same name of the instance constructor.

## Hints

- From a technical perspective, any UUID that specifies any text from OTR can also be passed to the input parameter `TEXTID` of the instance constructor. This is strongly discouraged, however, because an exception should only be raised with specific texts.
