---
title: "Date Formats"
source_file: abendate_formats.html
section: "ABAP Programming Language > ABAP - Language Environment > Formatting Settings > Country-Specific Formats"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Date Formats

The country-specific format of dates is determined by the fixed values of the [DDIC domain](../../abap-glossary/abendomain_glosry.md) `XUDATFM`. The mapping between countries and formats happens in a system table The following table shows the date formats represented by the fixed values of the domain, where *mm*, *dd*, and *yyyy* stand for day, month, and year:

| **Fixed Value of `XUDATFM`** | **Date Format**              |
|------------------------------|------------------------------|
| *1*                          | `dd.mm.yyyy`                 |
| *2*                          | `mm/dd/yyyy`                 |
| *3*                          | `mm-dd-yyyy`                 |
| *4*                          | `yyyy.mm.dd`                 |
| *5*                          | `yyyy/mm/dd`                 |
| *6*                          | `yyyy-mm-dd`                 |
| *7*                          | `ggyy.mm.dd`, Japanese date  |
| *8*                          | `ggyy/mm/dd`, Japanese date  |
| *9*                          | `ggyy-mm-dd`, Japanese date  |
| *A*                          | `yyyy/mm/dd`, Islamic date 1 |
| *B*                          | `yyyy/mm/dd`, Islamic date 2 |
| *C*                          | `yyyy/mm/dd`, Iranian date   |

- In the Japanese formats for the values *7*, *8*, and *9*, the first two characters *gg* of a four-digit year are formatted as a Japanese Unicode character for the current Japanese Emperor. The last two characters *yy* signify the year of his reign.

- In the Islamic formats for the values *A* and *B*, the date is formatted according to the Islamic moon calendar, which calculates time since 16th July 622, which is the date on which Mohammed left Mecca (Hijra). Since this calculation can be different in different Islamic countries, two formats are offered, each of which can be set individually. The corresponding settings are in the database table `TISLCAL`, and can be changed using the program `I18N_MAINTAIN_TISLCAL`.

- The Iranian format for value *C* is based on an Islamic sun calendar, which calculates the time in sun years since the Hijra.

The setting for the date format also affects the formatting of UTC time stamps in [time stamp fields](../../abap-glossary/abentimestamp_field_glosry.md).

## Hint

The class `CL_ABAP_DATFM` contains helper methods for dealing with date formats.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Output of a date and time stamps with different date formats. By specifying a country that s available in the system table, the respective country-specific format is selected.

``` abap
cl_demo_output=>display( 
  |{ cl_demo_date_time=>get_user_date( ) COUNTRY = 'DE ' }\n{ 
     cl_demo_date_time=>get_user_date( ) COUNTRY = 'US ' }\n{ 
     utclong_current( )                  COUNTRY = 'DE ' }\n{ 
     utclong_current( )                  COUNTRY = 'US ' }| ).
```

## Executable Examples
