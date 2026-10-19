---
title: "Calling Procedures"
source_file: abencall_procedures.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Calling Procedures

[Procedures](../../abap-glossary/abenprocedure_glosry.md) can be called both internally and externally. The following figure shows the most important internal and external calls.

  
![figure](images_abdoc_call_proc.gif)  

The statements for calling procedures are

- for methods:

  [`meth( ... )`](abapcall_method_static_short.md) [`CALL METHOD dynamic_meth ...`](abapcall_method_dynamic.md)

These statements supply the parameter interfaces of the procedures. When the call is terminated correctly, control returns to the statement after the call position.
