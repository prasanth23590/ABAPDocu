---
title: "itab - Loop with Step Size"
source_file: abenloop_at_itab_step_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, Basic Form > LOOP AT itab, cond"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Loop with Step Size

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates the execution of the statement `LOOP AT itab` with different `STEP` additions.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_loop_at_itab_using_stp DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_loop_at_itab_using_stp IMPLEMENTATION. 
  METHOD main. 
 
    TYPES: 
      BEGIN OF line, 
        tabix TYPE sy-tabix, 
        value TYPE i, 
      END OF line. 
    DATA result TYPE TABLE OF line WITH EMPTY KEY. 
 
    out->write_doc( 
      `An internal table itab is declared and filled as follows:` 
      )->begin_code( `itab` ). 
 
    DATA itab TYPE HASHED TABLE OF i WITH UNIQUE KEY table_line 
                          WITH NON-UNIQUE SORTED KEY sec_key 
                          COMPONENTS table_line 
                          ##TABKEY[PRIMARY_KEY][SEC_KEY]. 
 
    itab = VALUE #( ( 4 ) ( 3 ) ( 7 ) ( 11 ) ( 1 ) ( 5 ) ). 
 
    out->end_code( `itab` ). 
 
    out->next_section( `itab` 
      )->write( itab ). 
 
    LOOP AT itab ASSIGNING FIELD-SYMBOL(<fs>). 
      DATA(tabix) = sy-tabix. 
      result = VALUE #( BASE result ( tabix = tabix value = <fs> ) ). 
    ENDLOOP. 
 
    out->next_section( `LOOP AT itab` 
      )->write( result ). 
 
    CLEAR result. 
    LOOP AT itab ASSIGNING <fs> STEP -1. 
      tabix = sy-tabix. 
      result = VALUE #( BASE result ( tabix = tabix value = <fs> ) ). 
    ENDLOOP. 
 
    out->next_section( `LOOP AT itab STEP -1` 
       )->write( result ). 
 
    CLEAR result. 
    LOOP AT itab ASSIGNING <fs> STEP 2. 
      tabix = sy-tabix. 
      result = VALUE #( BASE result ( tabix = tabix value = <fs> ) ). 
    ENDLOOP. 
 
    out->next_section( `LOOP AT itab STEP 2` 
       )->write( result ). 
 
    CLEAR result. 
    LOOP AT itab ASSIGNING <fs> STEP -2. 
      tabix = sy-tabix. 
      result = VALUE #( BASE result ( tabix = tabix value = <fs> ) ). 
    ENDLOOP. 
 
    out->next_section( `LOOP AT itab STEP -2` 
       )->write( result ). 
 
    CLEAR result. 
    LOOP AT itab ASSIGNING <fs> USING KEY sec_key. 
      tabix = sy-tabix. 
      result = VALUE #( BASE result ( tabix = tabix value = <fs> ) ). 
    ENDLOOP. 
 
    out->next_section( `LOOP AT itab USING KEY sec_key` 
      )->write( result ). 
 
    CLEAR result. 
    LOOP AT itab ASSIGNING <fs> STEP -1 USING KEY sec_key. 
      tabix = sy-tabix. 
      result = VALUE #( BASE result ( tabix = tabix value = <fs> ) ). 
    ENDLOOP. 
 
    out->next_section( `LOOP AT itab STEP -1 USING KEY sec_key` 
       )->write( result ). 
 
    CLEAR result. 
    LOOP AT itab ASSIGNING <fs> STEP 2 USING KEY sec_key. 
      tabix = sy-tabix. 
      result = VALUE #( BASE result ( tabix = tabix value = <fs> ) ). 
    ENDLOOP. 
 
    out->next_section( `LOOP AT itab STEP 2 USING KEY sec_key` 
       )->write( result ). 
 
    CLEAR result. 
    LOOP AT itab ASSIGNING <fs> STEP -2 USING KEY sec_key. 
      tabix = sy-tabix. 
      result = VALUE #( BASE result ( tabix = tabix value = <fs> ) ). 
    ENDLOOP. 
 
    out->next_section( `LOOP AT itab STEP -2 USING KEY sec_key` 
       )->write( result ). 
 
    CLEAR result. 
    LOOP AT itab ASSIGNING <fs> FROM 1 TO 3 STEP 1 USING KEY sec_key. 
      tabix = sy-tabix. 
      result = VALUE #( BASE result ( tabix = tabix value = <fs> ) ). 
    ENDLOOP. 
 
    out->next_section( 
       `LOOP AT itab FROM 1 TO 3 STEP 1 USING KEY sec_key` 
       )->write( result ). 
 
    CLEAR result. 
    LOOP AT itab ASSIGNING <fs> FROM 3 TO 1 STEP -1 USING KEY sec_key. 
      tabix = sy-tabix. 
      result = VALUE #( BASE result ( tabix = tabix value = <fs> ) ). 
    ENDLOOP. 
 
    out->next_section( 
       `LOOP AT itab FROM 3 TO 1 STEP -1 USING KEY sec_key` 
       )->write( result ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The table `itab` is a hashed table with a unique key and a non-unique sorted key. Using `STEP` additions, the step size and the direction of a loop can be defined. The first table output displays the values for the hashed table in the order in which the table is filled.

1.  The `LOOP` is performed without a key specification and without a step size. The table output is in the order in which the table is filled and with the `sy-tabix` of 0. Each table line is read because the step size is automatically interpreted as 1.

2.  The `LOOP` is performed without a key specification and with the step size of -1. The table output is in the reverse order in which the table is filled and with the `sy-tabix` of 0.

3.  The `LOOP` is performed without a key specification and with the step size of 2. The table output is in the order in which the table is filled and with the `sy-tabix` of 0. Every second table line is read, starting with the first table line.

4.  The `LOOP` is performed without a key specification and with the step size of -2. The table output is in the reverse order in which the table is filled and with the `sy-tabix` of 0. Every second table line is read, starting with the last table line.

5.  The `LOOP` is performed with the sorted key `sec_key` and without a step size. The table output is in a sorted order from the lowest to the highest number and with the value of `sy-tabix` displaying the number of the respective table line in the secondary table index of `sec_key`. Each table line is read because the step size is automatically interpreted as 1.

6.  The `LOOP` is performed with the sorted key `sec_key` and with the step size of -1. The table output is in a reverse sorted order from the highest to the lowest number and with the value of `sy-tabix` displaying the number of the respective table line in the secondary table index of `sec_key`.

7.  The `LOOP` is performed with the sorted key `sec_key` and with the step size of 2. The table output is in a sorted order from the lowest to the highest number and with the value of `sy-tabix` displaying the number of the respective table line in the secondary table index of `sec_key`. Every second table line is read, starting with the first table line.

8.  The `LOOP` is performed with the sorted key `sec_key` and with the step size of -2. The table output is in a reverse sorted order from the highest to the lowest number and with the value of `sy-tabix` displaying the number of the respective table line in the secondary table index of `sec_key`. Every second table line is read, starting with the last table line.

9.  The `LOOP` is performed with the sorted key `sec_key`, with the step size of 1, and with the addition of `FROM` 1 `TO` 3. The table output is in a sorted order from table line 1 to 3 and with the value of `sy-tabix` displaying the number of the respective table line in the secondary table index of `sec_key`. Each table line is read, starting with the first table line.

10. The `LOOP` is performed with the sorted key `sec_key`, with the step size of -1, and with the addition of `FROM` 3 `TO` 1. The table output is in a reverse sorted order from table line 1 to 3 and with the value of `sy-tabix` displaying the number of the respective table line in the secondary table index of `sec_key`. Each table line is read, starting with the last table line.

See also the [executable example](abentable_cmprhnsns_step_abexa.md) for the `FOR` expression using the addition `STEP`.
