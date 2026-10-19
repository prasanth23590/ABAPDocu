---
title: "Built-In Functions, Hiding by Methods"
source_file: abenbuilt_in_functions_hiding.html
section: "ABAP Programming Language > ABAP - Built-In Types, Data Objects, Functions, and Constructors > Built-In Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Built-In Functions, Hiding by Methods

Within a class, a built-in function is always hidden by [methods](../../abap-glossary/abenmethod_glosry.md) of the class if they have the same name, regardless of the number and type of its parameters. The function is also hidden regardless of the number and type of method parameters. This especially takes place in method calls for which no selector `=>` or `->` is specified in front of the method name:

- A [static method](../../abap-glossary/abenstatic_method_glosry.md) hides a built-in function with the same name in all methods of the associated class.

- An [instance method](../../abap-glossary/abeninstance_method_glosry.md) hides a built-in function with the same name in the instance methods of the associated class.

The function is hidden regardless of the operand position. More specifically, any built-in functions used as arguments of other functions are also hidden.

## Hint

Methods should never be given the same name as a built-in function.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following class returns a syntax error. The specification of `strlen` on the right side of the assignment addresses the method of the class and not the built-in function. It cannot be specified in this operand position since it is not a functional method with a return value.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
    CLASS-METHODS strlen IMPORTING text TYPE string 
                         EXPORTING len  TYPE i. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD main. 
    DATA(len) = strlen( `xxx` ). 
  ENDMETHOD. 
  METHOD strlen. 
    ... 
  ENDMETHOD. 
ENDCLASS.
```
