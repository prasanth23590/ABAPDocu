---
title: "CALL FUNCTION IN REMOTE SESSION, parameter_list"
source_file: abapcall_function_remote_para.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > CALL FUNCTION > CALL FUNCTION, RFC > CALL FUNCTION, IN REMOTE SESSION"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CALL FUNCTION IN REMOTE SESSION, parameter_list

## Syntax

``` abap
... [EXPORTING    p1 = a1 p2 = a2 ... ]   
    [IMPORTING    p1 = a1 p2 = a2 ... ]   
    [TABLES       t1 = itab1 t2 = itab2 ...] ...   
    [CHANGING     p1 = a1 p2 = a2 ...] ...   
    [PARAMETER-TABLE ptab] ...  
```

## Description

These additions are used to assign actual parameters to the formal parameters of the function module. The additions have the same meaning as in [synchronous RFC](abapcall_function_destination_para.md) with the exception that no return values can be assigned to non-class-based exceptions.
