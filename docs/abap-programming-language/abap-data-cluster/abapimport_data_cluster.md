---
title: "IMPORT"
source_file: abapimport_data_cluster.html
section: "ABAP Programming Language > ABAP - Data Cluster"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# IMPORT

## Syntax

``` abap
IMPORT parameter_list FROM medium [conversion_options].  
```

[`parameter_list`](abapimport_parameterlist.md) · [`medium`](abapimport_medium.md) · [`conversion_options`](abapimport_conversion.md)

## Description

Imports data objects specified in [`parameter_list`](abapimport_parameterlist.md) from a [data cluster](../../abap-glossary/abendata_cluster_glosry.md) stored in storage medium [`medium`](abapimport_medium.md) with statement [`EXPORT`](abapexport_data_cluster.md). If necessary, the data is automatically converted to the current byte order (endian) and character format. The additions [`conversion_options`](abapimport_conversion.md) can be used to make adaptations to the current platform.

## System Fields

| **`sy-subrc`** | **Meaning**                                                                                                                                                                |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0              | The specified data cluster was found and the content of the parameters in the data cluster was passed to the respective data objects. Nonexistent parameters were ignored. |
| 4              | The specified data cluster was not found.                                                                                                                                  |

If the internal addition `USING subr` is used, a different rule applies to `sy-subrc`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Writing and reading of a byte string of two numbers.

``` abap
DATA buffer TYPE xstring. 
DATA num1 TYPE i. DATA num2 TYPE i. 
 
EXPORT name1 = 1 name2 = 2 TO DATA BUFFER buffer. 
IMPORT name1 = num1 name2 = num2 FROM DATA BUFFER buffer.
```
