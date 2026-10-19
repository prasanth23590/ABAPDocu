---
title: "Text Environment Language and Text Environment"
source_file: abentext_environment.html
section: "ABAP Programming Language > ABAP - Language Environment > Language Settings"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Text Environment Language and Text Environment

- [Text Environment Language](abentext_environment.md#text-environment-language)

- [Text Environment](abentext_environment.md#text-environment)

## Text Environment Language

The [text environment language](../../abap-glossary/abentext_env_langu_glosry.md) is part of the [language settings](abenlanguage_settings.md) of an ABAP program and determines its [text environment](../../abap-glossary/abentext_environment_glosry.md). It is valid during an [internal session](../../abap-glossary/abeninternal_session_glosry.md).

- The text environment language is set at the start of each internal session to the [logon language](../../abap-glossary/abenlogon_language_glosry.md) of the current [user session](../../abap-glossary/abenuser_session_glosry.md).

- It can also be set to a different language for the current internal session using a suitable API.

The current text environment language is the nominal content of the system field [`sy-langu`](../abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md).

## Text Environment

All programs in an [internal session](../../abap-glossary/abeninternal_session_glosry.md) work in a shared text environment that is determined by the text environment language. Besides the language, the text environment includes:

- A **code page**

  The [code page](../../abap-glossary/abencodepage_glosry.md) of the text environment is always the [system code page](../../abap-glossary/abensystem_codepage_glosry.md) [UTF-16](../../abap-glossary/abenutf16_glosry.md) of the AS instances of a [Unicode system](../../abap-glossary/abenunicode_system_glosry.md) and cannot be changed.

- A **locale**

  The [locale](../../abap-glossary/abenlocale_glosry.md) properties that belong to the text environment language and country are defined in an ICU (International Components for Unicode) library. This library is made available for AS ABAP and is independent of the operating system of the [host computer](../../abap-glossary/abenhost_computer_glosry.md) of the [AS instances](../../abap-glossary/abenas_instance_glosry.md).

The main purpose of the text environment it to handle texts in character-like data objects:

- The [code page](../../abap-glossary/abencodepage_glosry.md) of the text environment affects all operations that depend on the current character set, such as

  - Casting character-like data objects to byte-like types

  - Transferring data from and to external storage

  - Transferring data using data and communication interfaces

- The [locale](../../abap-glossary/abenlocale_glosry.md) of the text environment affects all statements that sort character-like data objects as text, such as

  - [`SORT AS TEXT`](../abap-processing-internal-data/abapsort_itab.md)

  - [`CONVERT TEXT INTO SORTABLE CODE`](../abap-processing-internal-data/abapconvert_text.md)

- In addition, the text environment language, and not the logon language, is used in the following cases:

  - The ABAP-specific [session variable](../../abap-glossary/abensession_variable_glosry.md) `LOCALE_SAP` in SAP HANA and the session variable [`system_language`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_session_variable_v2.md) in ABAP CDS contain the current text environment language in reads from ABAP or ABAP SQL.

  - If the logon language for the RFC session is not defined in the RFC destination in a remote function call, it is determined by the current text environment language.

  - The exception texts returned by [exception classes](../../abap-glossary/abenexception_class_glosry.md) are determined by the current text environment language.

    Any further frameworks based on the nominal value of the system field `sy-langu` access the current text environment language and not the logon language.

### Hints

- The ABAP programming language supports a subset covered by [UCS-2](../../abap-glossary/abenucs2_glosry.md) and not the full scope of UTF-16. This contains all [UTF](../../abap-glossary/abenutf_glosry.md) characters except those in the [surrogate area](../../abap-glossary/abensurrogate_area_glosry.md). ABAP interprets a character from the surrogate area as two characters.
