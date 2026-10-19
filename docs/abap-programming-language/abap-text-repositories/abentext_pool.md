---
title: "Text Pools"
source_file: abentext_pool.html
section: "ABAP Programming Language > ABAP - Text Repositories"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Text Pools

Text pools are persistent repositories for the following [text elements](../../abap-glossary/abentext_element_glosry.md):

- [Text symbols](../../abap-glossary/abentext_symbol_glosry.md)

There is one text pool for the original language of the program and one text pool for each translation language.

From which text pool an ABAP program takes its texts depends on the [logon language](../../abap-glossary/abenlogon_language_glosry.md) or a [secondary language](../../abap-glossary/abensecondary_language_glosry.md).

- When a program is loaded into an [internal session](../../abap-glossary/abeninternal_session_glosry.md), the text elements of the text pool of the [logon language](../../abap-glossary/abenlogon_language_glosry.md) are imported by default. If this text pool does not exist, the text pool of the [secondary language](../../abap-glossary/abensecondary_language_glosry.md) of AS ABAP is used. If none of these text pools exist, an empty text pool without text elements is loaded.

## Hint

In [global classes](../../abap-glossary/abenglobal_class_glosry.md) and [function pools](../../abap-glossary/abenfunction_pool_glosry.md), the text pools are assigned to the relevant master program. In the repository, this program has a different name than the class or function pool.
