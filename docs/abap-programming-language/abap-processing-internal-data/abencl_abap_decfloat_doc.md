---
title: "System Class CL_ABAP_DECFLOAT"
source_file: abencl_abap_decfloat_doc.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > System Classes for Numbers"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# System Class CL_ABAP_DECFLOAT

The system class `CL_ABAP_DECFLOAT` contains methods for handling [decimal floating point numbers](../../abap-glossary/abendecfloat_glosry.md).

- The methods `READ_DECFLOAT34` and `READ_DECFLOAT16` convert strings to decimal floating point numbers. The exceptions of these methods are more significant than those of a regular assignment. Furthermore, the methods return a return value that reveals information about the roundings performed.

- The methods `CONVERT_CURR_TO_DECFLOAT` and `CONVERT_DECFLOAT_TO_CURR` convert currency amounts to decimal floating point numbers as specified by a currency key and vice versa.
