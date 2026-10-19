---
title: "surrogates"
source_file: abensurrogates_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# surrogates

[General](abenabap_glossary.md)

## Definition

Also referred to as surrogate pair. Combination of special low and high surrogate characters for addressing characters in the [surrogate area](abensurrogate_area_glosry.md) when using [UTF-16](abenutf16_glosry.md). High surrogate characters range from `U+D800` to `U+DBFF`. Low surrogate characters range from `U+DC00` to `U+DFFF`. They are called surrogates because they do not directly represent one character but only as a pair. High and low surrogates can only be part of a surrogate pair and cannot appear on their own in a valid UTF-16 string. While UTF-16 with surrogates is the [system code page](abensystem_codepage_glosry.md) of an [AS ABAP](abenas_abap_glosry.md) the ABAP programming language supports [UCS-2](abenucs2_glosry.md) and interprets a surrogate character as two characters.
