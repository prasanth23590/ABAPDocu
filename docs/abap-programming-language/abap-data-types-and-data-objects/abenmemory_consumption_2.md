---
title: "Maximum Size of Dynamic Data Objects"
source_file: abenmemory_consumption_2.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > Memory Management of Deep Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Maximum Size of Dynamic Data Objects

In addition to the maximum memory size that the current [internal session](../../abap-glossary/abeninternal_session_glosry.md) can request for [dynamic data objects](../../abap-glossary/abendynamic_data_object_glosry.md), their maximum size is limited by the following factors:

- An upper limit for the number of places in strings or lines of internal tables results from the fact that 4 byte integers are used to address them internally and in ABAP statements, which limits them to 2147483647.

- The size of strings and hashed tables is limited by the biggest memory block that can be requested in one piece.

If an operation with a dynamic data object exceeds its maximum size, an exception occurs:

- For internal tables, such an exception is uncatchable and always results in a [runtime error](../../abap-glossary/abenruntime_error_glosry.md). There are different runtime errors for different situations, as for example [`TSV_TNEW_PAGE_ALLOC_FAILED`](https://launchpad.support.sap.com/#/notes/20527).

- For strings, the exception is class-based and connected to exception class `CX_SY_STRING_SIZE_TOO_LARGE`. The runtime error `STRING_SIZE_TOO_LARGE` only occurs if the exception is not handled. After this exception is caught, the respective string contains the content it had directly before the exception. This is usually the content it had before the entire operation (statement, function). Exceptions from this rule are statements like [`CONCATENATE LINES OF`](../abap-processing-internal-data/abapconcatenate.md) or functions like [`concat_lines_of`](../abap-processing-internal-data/abenconcatenation_functions.md), which can change the string before the exception occurs.

## Hints

- If there is only little memory space available, it may be better to use an internal table, because its memory space is requested in blocks, while the entire memory space required for a string must always be free as a whole.

- It is strongly recommended that the content of a string after catching an exception `CX_SY_STRING_SIZE_TOO_LARGE` is regarded as undefined and that it is deleted as soon as possible.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following `DO` loop of class `CL_DEMO_STRING_SIZE_TOO_LARGE`, a string is concatenated with itself until it exceeds its maximum size and an exception occurs. After catching the exception, the byte-length of the string is determined before its content is deleted.

``` abap
DATA(txt) = `X`. 
TRY. 
    DO. 
      txt = txt && txt. 
    ENDDO. 
  CATCH cx_sy_string_size_too_large INTO FINAL(exc). 
    cl_demo_output=>display( 
      |{ exc->get_text( ) 
       }.\nThe resulting string has a length of { 
         xstrlen( cl_abap_codepage=>convert_to( 
                    source = txt 
                    codepage = 'UTF-16' ) ) } bytes.| ). 
    CLEAR txt. 
ENDTRY.
```
