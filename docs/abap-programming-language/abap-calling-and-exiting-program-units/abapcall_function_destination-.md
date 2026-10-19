---
title: "CALL FUNCTION, RFC"
source_file: abapcall_function_destination-.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > CALL FUNCTION"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CALL FUNCTION, RFC

## Syntax Forms

**Synchronous RFC**

``` abap
1. CALL FUNCTION func DESTINATION dest 
                parameter_list. 
| CALL FUNCTION func IN REMOTE SESSION session 
                parameter_list.
```

[`DESTINATION`](abapcall_function_destination.md) · [`parameter_list`](abapcall_function_destination_para.md) · [`IN REMOTE SESSION`](abapcall_function_remote_session.md) · [`parameter_list.`](abapcall_function_remote_para.md)

## Description

A function module or a function is called using the RFC interface. The same applies to the specification `func` as to [general function module calls](abapcall_function_general.md).
