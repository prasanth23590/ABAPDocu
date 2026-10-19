---
title: "Class for Compressing Character Strings and Byte Strings"
source_file: abencl_abap_gzip.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > System Classes for Character String and Byte String Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Class for Compressing Character Strings and Byte Strings

These classes offer a range of methods that enable text in text fields or text strings, or binary data in byte fields or byte strings to be compressed or decompressed using `GZIP`.

- `CL_ABAP_GZIP`

- `CL_ABAP_GZIP_BINARY_STREAM`

- `CL_ABAP_GZIP_TEXT_STREAM`

- `CL_ABAP_UNGZIP_BINARY_STREAM`

- `CL_ABAP_UNGZIP_TEXT_STREAM`

For more information, see the individual classes and methods.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Compression and decompression of text.

``` abap
DATA zip TYPE xstring. 
cl_abap_gzip=>compress_text( 
  EXPORTING text_in  = `Hello!` 
  IMPORTING gzip_out = zip ). 
 
DATA txt TYPE string. 
cl_abap_gzip=>decompress_text( 
  EXPORTING gzip_in  = zip 
  IMPORTING text_out = txt ). 
 
ASSERT txt = `Hello!`.
```
