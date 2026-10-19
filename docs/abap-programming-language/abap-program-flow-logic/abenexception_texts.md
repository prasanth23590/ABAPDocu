---
title: "Exception Texts"
source_file: abenexception_texts.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Exception Handling > Class-Based Exceptions > Exception Classes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Exception Texts

Each exception is assigned a text that can be parameterized by attributes and that describes the exception situation. This text is displayed in the [short dump](../../abap-glossary/abenshort_dump_glosry.md) of the runtime error if the exception is not handled. If the exception is handled in the program, the text can be read using the method `GET_TEXT` of the interface `IF_MESSAGE`, which is implemented by every exception class. Any long text can be read using the method `GET_LONGTEXT`. A global exception class has a predefined exception text with the same name as the exception class. This predefined text can be edited and further exception texts can be defined.

From a technical perspective, each exception text is defined by an identically named static constant in the public visibility section of the exception class that defines its properties. The instance constructor of an exception class has an input parameter `TEXTID` to which such a constant can be passed when the exception is raised to determine the exception text. If the parameter is not passed, the predefined exception text with the same name as the exception class is used.

The exception texts of an exception class are usually defined by referring to [messages](../../abap-glossary/abenmessage_glosry.md) in the table `T100`. In predefined system classes, OTR (Online Text Repository) texts can also be used.

- [Messages as Exception Texts](abenexception_texts_t100.md)

- [Exception Texts for System Classes](abenexception_texts_internal.md)

## Hints

- The names of the exception texts or the associated constants should be understood as keys of the existing texts for an exception class. This means that when an exception is raised, only the constants of the exception class with the same name should be passed to the parameter `TEXTID` to determine the exception text.
