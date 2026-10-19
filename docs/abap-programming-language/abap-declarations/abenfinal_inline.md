---
title: "FINAL, Inline Declaration for Immutable Variables"
source_file: abenfinal_inline.html
section: "ABAP Programming Language > ABAP - Declarations > Inline Declarations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FINAL, Inline Declaration for Immutable Variables

## Syntax

``` abap
... FINAL(var) ...  
```

## Description

Declaration of an [immutable variable](../../abap-glossary/abenimmutable_variable_glosry.md). A declaration expression with the declaration operator `FINAL` in general works in the same way as an inline declaration with the declaration operator [`DATA`](abendata_inline.md) and the same general rules apply.

While `DATA` declares a regular variable, `FINAL` declares an immutable variable: The write position where the variable `var` is declared with `FINAL` is the only one, where a value can be assigned to that variable in the current [context](../../abap-glossary/abenobj_context_glosry.md). In all other positions, any write access leads either to a syntax error or the uncatchable exception `MOVE_TO_LIT_NOTALLOWED_NODATA`.

The declaration operator `FINAL` can be used in the same [declaration positions](../../abap-glossary/abendeclaration_position_glosry.md) as the operator `DATA` with one exception: `FINAL` cannot be used behind `OPEN CURSOR` because usually there is always a second write access with `CLOSE CURSOR` in the same context.

## Hints

- The fact that there is only one write position for `FINAL` in a context does not mean that only one write access can be executed at runtime. For example, the declaration operator `FINAL` can be positioned inside a loop or it can be used after `INTO` in a [`LOOP`](../abap-processing-internal-data/abaploop_at_itab.md) statement. Then a value is assigned multiple times to `var`, but `var` cannot be changed in any other write position.

- If an immutable variable is a [reference variable](../../abap-glossary/abenreference_variable_glosry.md), the immutability concerns the [reference](../../abap-glossary/abenreference_glosry.md) but not the content of the object referred by the reference. An immutable reference variable followed by the [object component selector](../../abap-glossary/abenobject_component_select_glosry.md) (`->`) can be used in [write positions](../../abap-glossary/abenwrite_position_glosry.md).

- If a data object called `final` already exists in the current context, `FINAL(var)` is interpreted as a [substring access](../abap-operands/abenoffset_length.md) and not as an inline declaration.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Four immutable variables `date`, `yesterday`, `result`, and `wa` are declared inline with `FINAL`. They can be used at read positions but any attempt using them at write positions would lead to a syntax error or an exception.

``` abap
FINAL(date) = cl_demo_date_time=>get_user_date( ). 
FINAL(yesterday) = CONV d( date - 1 ). 
 
"yesterday -= 1. <-- Syntax error 
 
SELECT carrid, connid, seatsocc 
       FROM sflight 
       WHERE fldate = @yesterday 
       INTO TABLE @FINAL(result). 
 
LOOP AT result INTO FINAL(wa). 
  ... 
  "wa-seatsocc = 0. <-- Syntax error 
  ... 
ENDLOOP. 
 
"APPEND wa TO result. <-- Syntax error
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Inline declaration of an internal table as a target field of a [`SELECT`](../abap-database-access/abapselect.md) statement and inline declaration of a variable for the table transformed to HTML. The data type of the variable is determined by the return value of the method.

``` abap
SELECT * 
       FROM scarr 
       INTO TABLE @FINAL(itab). 
 
FINAL(html) = cl_demo_output=>get( itab ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The content of the variable `num` referred by the immutable reference variable `dref` can be changed, but not the content of the immutable reference variable itself. `dref` always points to `num` in the following code snippet.

``` abap
DATA num TYPE i. 
 
FINAL(dref) = REF i( num ). 
 
dref->* = 111. 
 
"dref = REF i( 111 ). "Syntax error
```
