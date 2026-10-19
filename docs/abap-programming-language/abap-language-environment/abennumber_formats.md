---
title: "Number Formats"
source_file: abennumber_formats.html
section: "ABAP Programming Language > ABAP - Language Environment > Formatting Settings > Country-Specific Formats"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Number Formats

The country-specific format of numbers is determined by the fixed values of the [DDIC domain](../../abap-glossary/abendomain_glosry.md) `XUDCPFM`. The mapping between countries and formats happens in a system table The following table shows the decimal and thousands separators represented by the fixed values of the domain.

| **Fixed Value of `XUDCPFM`** | **Decimal Separator** | **Thousands Separator** |
|------------------------------|-----------------------|-------------------------|
| blank                        | ","                   | "."                     |
| `X`                          | "."                   | ","                     |
| `Y`                          | ","                   | blank                   |

The setting for the decimal separator also affects the formatting of UTC time stamps in [time stamp fields](../../abap-glossary/abentimestamp_field_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Output of a number and time stamp with different separators. By specifying a country that s available in the system table, the respective country-specific format is selected.

``` abap
DATA pack TYPE p DECIMALS 2 VALUE '1234.56'. 
FINAL(utcl) =  utclong_current( ). 
 
cl_demo_output=>display( 
  |{ pack COUNTRY = 'DE ' }\n{ 
     pack COUNTRY = 'US ' }\n{ 
     utcl COUNTRY = 'DE ' }\n{ 
     utcl COUNTRY = 'US ' }| ).
```

## Executable Example

For the representation of a number in all possible number formats, see the associated example with string templates.
