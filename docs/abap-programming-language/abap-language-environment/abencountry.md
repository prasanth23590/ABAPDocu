---
title: "Formatting Settings"
source_file: abencountry.html
section: "ABAP Programming Language > ABAP - Language Environment"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Formatting Settings

## Formats

The formatting settings of the [language environment](abenlanguage.md) determine

- the number format (decimal and thousands separators)

- The date format (separators and order)

- The time format (24 hour or 12 hour format)

- The time stamp format (composed of date format and time format)

for formatted output.

## Definition

The formatting settings are set as follows:

- At the start of an [internal session](../../abap-glossary/abeninternal_session_glosry.md), they are determined by the corresponding *Defaults* in the [user master record](../../abap-glossary/abenuser_master_record_glosry.md) of the current user.

- This default setting for the current internal session can be overwritten by [country-specific formats](abencountry_formats.md) using a suitable API.

## Effect

The formatting settings affect the following ABAP language elements:

- Specification of the parameter [`ENVIRONMENT`](../abap-processing-internal-data/abapcompute_string_format_options.md) for the formatting options [`NUMBER`](../abap-processing-internal-data/abapcompute_string_format_options.md), [`DATE`](../abap-processing-internal-data/abapcompute_string_format_options.md), [`TIME`](../abap-processing-internal-data/abapcompute_string_format_options.md), and [`TIMESTAMP`](../abap-processing-internal-data/abapcompute_string_format_options.md) for [embedded expressions](../abap-processing-internal-data/abenstring_templates_expressions.md) in [string templates](../abap-processing-internal-data/abenstring_templates.md).

## Handling Invalid Values

The content of data object of the types `d` or `t` is normally formatted independently from their content. [Invalid values](../abap-processing-internal-data/abenchar_date_time_fields_validity.md) are also interpreted as date or time specifications. For time output in the 12 hour format, the separators are inserted at the respective points for invalid values and the output of the AM/am or PM/pm abbreviation is undefined.

Time stamp fields of the type `utclong` must contain valid values for [UTC time stamps](../../abap-glossary/abenutc_timestamp_glosry.md) according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md) to be able to be represented as dynpro fields on dynpros and only valid values can be entered. Invalid values can be produced by castings.

## Hints

- The classes `CL_ABAP_DATFM` and `CL_ABAP_TIMEFM` contain helper methods for handling date and time formats.
