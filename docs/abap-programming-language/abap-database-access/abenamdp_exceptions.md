---
title: "AMDP - Exception Classes"
source_file: abenamdp_exceptions.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - Exception Classes

The names of the exception classes of the exceptions that can be handled when an [AMDP procedure implementation](abenamdp_procedure_methods.md) is called start with the prefix `CX_AMDP`. The exceptions are all in the category `CX_DYNAMIC_CHECK` and must be declared explicitly using [`RAISING`](../abap-declarations/abapmethods_general.md) in the definition of an [AMDP procedure implementation](../../abap-glossary/abenamdp_procedure_method_glosry.md) to be catchable when this method is called. The meaning of the exception classes is documented in their semantic properties in the class library.

``` abap
 
CX_ROOT 
  | 
  |--CX_DYNAMIC_CHECK 
       | 
       |--CX_AMDP_ERROR 
           | 
           |--CX_AMDP_VERSION_ERROR 
           |    | 
           |    |--CX_AMDP_VERSION_MISMATCH 
           | 
           |--CX_AMDP_CREATION_ERROR 
           |    | 
           |    |--CX_AMDP_DBPROC_GENERATE_FAILED 
           |    | 
           |    |--CX_AMDP_DBPROC_CREATE_FAILED 
           |    | 
           |    |--CX_AMDP_NATIVE_DBCALL_FAILED 
           |    | 
           |    |--CX_AMDP_WRONG_DBSYS 
           | 
           |--CX_AMDP_EXECUTION_ERROR 
           |    | 
           |    |--CX_AMDP_EXECUTION_FAILED 
           |    | 
           |    |--CX_AMDP_IMPORT_TABLE_ERROR 
           |    | 
           |    |--CX_AMDP_RESULT_TABLE_ERROR 
           | 
           |--CX_AMDP_CONNECTION_ERROR 
                | 
                |--CX_AMDP_NO_CONNECTION 
                | 
                |--CX_AMDP_NO_CONNECTION_FOR_CALL 
                | 
                |--CX_AMDP_WRONG_CONNECTION
```

## Hint

No exceptions can be declared for [AMDP function implementations](abenamdp_function_methods.md).
