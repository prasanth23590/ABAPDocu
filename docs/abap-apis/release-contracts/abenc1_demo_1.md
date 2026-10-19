---
title: "Example: Consumption of APIs with C1 Contract"
source_file: abenc1_demo_1.html
section: "ABAP APIs > Release Contracts > Contract Rules for API Consumers"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Example: Consumption of APIs with C1 Contract

The first part of the example simulates data types from the ABAP Dictionary by data types defined in the program. The second part represents consumer code working with these data types in an unfavorable way by mixing them with locally defined types. If changes allowed by C1 contract\< are applied to the pseudo external types, syntax errors and exceptions occur.

``` abap
*Pseudo DDIC types 
 
TYPES: 
  ddic_de_i TYPE i, 
  ddic_de_c TYPE c LENGTH 3, 
 
  BEGIN OF ddic_struc, 
    text TYPE ddic_de_c, 
    int  TYPE ddic_de_i, 
  END OF ddic_struc. 
 
DATA ddic_dbtab TYPE HASHED TABLE OF ddic_struc WITH UNIQUE key text. 
 
*Consumer Code 
 
DATA int TYPE ddic_de_i. 
 
"Exception when DDIC_DE_I is changed to int8 
"and int exceeds value range of i 
DO int TIMES. 
  ... 
ENDDO. 
 
"Syntax error when DDDIC_DE_I is changed to int8 
DATA dref TYPE REF TO i. 
dref = REF #( int ). 
 
"Syntax error when DDIC_DE_I is changed to int8 
DATA itab TYPE SORTED TABLE OF i WITH NON-UNIQUE KEY table_line. 
INSERT int INTO TABLE itab. 
 
DATA char TYPE ddic_de_c. 
 
"Exception when length of DDIC_DE_C is increased 
"and char contains more than three relevant characters 
SELECT carrname 
       FROM scarr 
       WHERE carrid = @char 
       INTO TABLE @FINAL(result). 
 
DATA: 
  struc1 TYPE ddic_struc, 
  BEGIN OF struc2, 
    text TYPE c LENGTH 3, 
    int  TYPE i, 
  END OF struc2. 
 
"Syntax errors when DDIC_DE_I is changed to int8 
"or when the length of DDIC_DE_C is increased 
"or when a component is added to DDIC_STRUC 
struc1 = struc2. 
IF struc1 = struc2. 
  ... 
ENDIF. 
 
"Syntax error when DDIC_DE_I is changed to int8 
"or when the length of DDIC_DE_C is increased 
"or when a component is added to DDIC_STRUC 
FIELD-SYMBOLS <fs> TYPE ddic_struc. 
ASSIGN struc2 TO <fs> CASTING. 
 
"Syntax error when DDIC_DE_I is changed to int8 
"or when the length of DDIC_DE_C is increased 
"or when a component is added to DDIC_STRUC 
SELECT single * 
       from @ddic_dbtab as dbtab 
       into @struc2.
```
