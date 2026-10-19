---
title: "Language Settings"
source_file: abenlanguage_settings.html
section: "ABAP Programming Language > ABAP - Language Environment"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Language Settings

The [language setting](../../abap-glossary/abenlanguage_setting_glosry.md) includes the following settings:

- [Logon language](abenlogon_language.md)

  The logon language is the language of the current [user session](../../abap-glossary/abenuser_session_glosry.md). It affects the selection of various texts.

- [Text environment language](abentext_environment.md)

  The text environment language is the language of the [text environment](../../abap-glossary/abentext_environment_glosry.md) of the current [internal session](../../abap-glossary/abeninternal_session_glosry.md). By default, this is the logon language. It affects the general language-dependent behavior of an ABAP program.

## Hints

- The system field [`sy-langu`](../abap-built-in-types-data-objects-functions-and-constructors/abensystem_fields.md) contains the text environment language. It only represents the logon language if the text environment language was not set to a different value.
