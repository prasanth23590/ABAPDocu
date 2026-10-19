---
title: "Methods for Handling Code Pages"
source_file: abencl_abap_conv_codepage.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > System Classes for Character String and Byte String Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Methods for Handling Code Pages

The methods `CONVERT` of the interfaces `IF_ABAP_CONV_OUT` and `IF_ABAP_CONV_IN` of objects created with the class `CL_ABAP_CONV_CODEPAGE` make it possible to convert strings to the binary representation of various code pages and vice versa.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Conversion of the content of a string into its UTF-8 representation. The value *UTF-8* is the default value for the parameter `CODEPAGE` and can also be omitted. The statement [`ASSERT`](../abap-program-maintenance/abapassert.md) shows that the reverse conversion creates the original text again.

``` abap
FINAL(str) = `Blah blah ...`. 
 
FINAL(xstr) = 
  cl_abap_conv_codepage=>create_out( codepage = `UTF-8` 
    )->convert( source = str ). 
 
ASSERT 
  cl_abap_conv_codepage=>create_in( codepage = `UTF-8` 
    )->convert( source = xstr ) = str.
```
