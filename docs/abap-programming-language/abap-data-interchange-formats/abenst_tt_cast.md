---
title: "ST - tt:cast, Downcast"
source_file: abenst_tt_cast.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Value Assignments"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:cast, Downcast

## Syntax

``` abap
<tt:cast [to-ref="node"|to-var="variable"] 
         [ref="node"|var="variable"] />  
```

## Description

The `tt:cast` statement can be used to assign the content of one reference variable to another reference variable when the static type of the source variable is more general than the static type of the target variable. This is called a [downcast](../../abap-glossary/abendown_cast_glosry.md).

The `tt:cast` statement is a special case of the [`tt:assign`](abenst_tt_assign.md) statement, in which only reference variables can be declared as source fields and target fields. Reference variables can be declared as follows:

- A node `node` declared in accordance with the [addressing rules](abenst_addressing.md) and to which an ABAP reference variable is bound

- A [variable](abenst_tt_variable.md) or [parameter](abenst_tt_parameter.md) `variable` defined as a reference variable using `tt:ref-type`.

If the downcast fails because the static type of the target variable is more specific than the dynamic type of the source variable when the statement is executed, the ST program terminates with the `CX_ST_RUNTIME_ERROR` exception.
