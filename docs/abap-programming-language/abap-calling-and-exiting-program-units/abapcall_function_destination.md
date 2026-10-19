---
title: "CALL FUNCTION DESTINATION"
source_file: abapcall_function_destination.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > CALL FUNCTION > CALL FUNCTION, RFC"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CALL FUNCTION DESTINATION

## Syntax

``` abap
CALL FUNCTION func DESTINATION dest parameter_list.  
```

[`parameter_list`](abapcall_function_destination_para.md)

## Description

Synchronous call (sRFC). The addition `DESTINATION` is used to specify the destination in `dest`. `func` and `dest` expect character-like data objects. The calling program is continued after the `CALL FUNCTION` statement when the remotely called function has finished.

**More Information**

For more information about sRFC, see the documentation [RFC](https://help.sap.com/docs/ABAP_PLATFORM_NEW/753088fc00704d0a80e7fbd6803c8adb/4888068AD9134076E10000000A42189D) in SAP Help Portal.

## Hints

- If an empty string or a text field consisting only of blanks is specified for `dest`, the addition `DESTINATION` is ignored and a regular [`CALL FUNCTION func`](abapcall_function_general.md) call is performed.

- The synchronous RFC triggers a [database commit](../../abap-glossary/abendatabase_commit_glosry.md) in the calling program.

- The statement initializes `sy-msg*` components.
