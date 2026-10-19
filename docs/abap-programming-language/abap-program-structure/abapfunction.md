---
title: "FUNCTION"
source_file: abapfunction.html
section: "ABAP Programming Language > ABAP - Program Structure > Modularization Statements > Procedures > Function Modules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FUNCTION

## Syntax

``` abap
FUNCTION func.   
*"---------------------------------------------------------   
*" Local Interface:   
*" parameter_interface   
*"---------------------------------------------------------   
  ...   
ENDFUNCTION.  
```

[`parameter_interface`](abenfunction.md)

## Description

Between the statements `FUNCTION` and `ENDFUNCTION`, the functionality of a [function module](../../abap-glossary/abenfunction_module_glosry.md) `func` is implemented in a function pool. The function module and its interface are defined in the [ABAP development tools for Eclipse](../../abap-glossary/abenadt_glosry.md).

Within the function module, local data types and data objects can be declared. There is also access to the formal parameters of the function module and to the global data types and data objects of the function pool. A function module is called using the statement [`CALL FUNCTION`](../abap-calling-and-exiting-program-units/abapcall_function.md).

## Hint

The [predicate expression](../../abap-glossary/abenpredicate_expression_glosry.md) [`IS SUPPLIED`](../abap-program-flow-logic/abenlogexp_supplied.md) can be used in the function module to determine whether an actual parameter has been specified for when a formal parameter is called.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Implements a function module that reads data in a table-like formal parameter `flight_tab` under the condition of an elementary formal parameter `id`. The [parameter interface](abenfunction.md) defined in Function Builder is visible as a comment.

``` abap
FUNCTION read_spfli_into_table. 
*"--------------------------------------------------------- 
*" Local Interface: 
*"       IMPORTING 
*"             VALUE(ID) LIKE  SPFLI-CARRID DEFAULT 'LH ' 
*"       EXPORTING 
*"             FLIGHT_TAB TYPE  SPFLI_TAB 
*"--------------------------------------------------------- 
  SELECT * 
         FROM spfli 
         WHERE carrid = @id 
         INTO TABLE @flight_tab. 
ENDFUNCTION.
```
