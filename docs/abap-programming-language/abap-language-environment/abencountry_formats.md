---
title: "Country-Specific Formats"
source_file: abencountry_formats.html
section: "ABAP Programming Language > ABAP - Language Environment > Formatting Settings"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Country-Specific Formats

The country-specific formatting settings for numbers, dates, and times are stored in a different system table.

- [Number Formats](abennumber_formats.md)

- [Date Formats](abendate_formats.md)

- [Time Formats](abentime_formats.md)

For a time stamp, the date format and time format affect the respective parts and the decimal separator follows the number format.

The settings for a specific country can

- be set for an [internal session](../../abap-glossary/abeninternal_session_glosry.md) using a suitable API

- be used in [string templates](../abap-processing-internal-data/abenstring_templates.md) using the formatting option [`COUNTRY`](../abap-processing-internal-data/abapcompute_string_format_options.md) for the formatting of an [embedded expression](../abap-processing-internal-data/abenstring_templates_expressions.md).
