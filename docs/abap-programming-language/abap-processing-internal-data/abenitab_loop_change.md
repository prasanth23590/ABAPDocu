---
title: "itab - Modifying Internal Tables in a Loop"
source_file: abenitab_loop_change.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Modifying Internal Tables in a Loop

- [Inserting and Deleting Lines](abenitab_loop_change.md#inserting-and-deleting-lines)

- [Replacing or Clearing the Entire Table Body](abenitab_loop_change.md#replacing-or-clearing-the-entire-table-body)

## Inserting and Deleting Lines

In the statement block of a [`LOOP`](abaploop_at_itab_variants.md) control statement, the content of the currently processed internal table can be changed by inserting or deleting lines. The position of inserted or deleted lines with regard to the current line is determined by the line numbers in the corresponding [table index](../../abap-glossary/abentable_index_glosry.md) in the case of loops across index tables or when using a sorted key. In the case of loops on hashed tables and when using a hash key, the position depends on the order of insertion or the order of lines that might have been established by a previous [`SORT`](abapsort_itab.md) statement for the table.

- Inserting lines after the current line causes these new lines to be processed in the subsequent loop passes, which can produce an endless loop.

- Deleting lines after the current line causes the deleted lines to no longer be processed in the subsequent loop passes.

- Inserting lines in front of the current line causes the internal loop counter to be increased by one with each inserted line. This affects `sy-tabix` in the subsequent loop pass in the case of loops across index tables or when using a sorted key, and `sy-tabix` is increased accordingly.

- Deleting the current line or lines in front of the current line causes the internal loop counter to be decreased by one with each deleted line. In the case of loops across index tables or when using a sorted key, this affects `sy-tabix` in the subsequent loop pass, and `sy-tabix` is decreased accordingly.

## Replacing or Clearing the Entire Table Body

As a rule the replacement or clearing of the entire table body of the currently processed internal table is not allowed in the statement block of a [`LOOP`](abaploop_at_itab_variants.md) statement. Such a write access to the table body can be achieved with statements such as [`CLEAR`](abapclear.md), [`FREE`](abapfree_dataobject.md), `LOCAL`, [`SORT`](abapsort_itab.md), [`DELETE ... WHERE`](abapdelete_itab_lines.md), and with all types of assignments.

- If known statically, clearing or replacing the table body inside a loop results in a syntax error in classes and for `LOOP` statements with a statically known secondary key. Outside classes and for tables without secondary key, the syntax check gives only a warning for compatibility reasons.

- If it is not known statically, clearing or replacing the table body inside a loop raises the runtime error `TABLE_FREE_IN_LOOP` with the following exception: If the [output behavior](abaploop_at_itab_result.md) is defined with `INTO` or `TRANSPORTING NO FIELDS`, or with the obsolete short form, for compatibility reasons there is no runtime error and the loop is exited in an undefined way.

**Caution**

Since the result of replacing or clearing the entire table body within a loop can result in unpredictable program behavior, the exceptions to the rule should not be exploited.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Replacing the table body of an internal table within a loop over that table. The syntax check reports errors in classes and warnings outside classes. While the loop with `ASSIGNING` results in the runtime error `TABLE_FREE_IN_LOOP`, the loop with `INTO` is executed without runtime error. The latter is shown for demonstration purposes, but not recommended.

``` abap
DATA itab TYPE TABLE OF i. 
 
itab = VALUE #( ( 1 ) ( 2 ) ( 3 ) ). 
 
DATA jtab TYPE TABLE OF i. 
 
jtab = VALUE #( ( 4 ) ( 5 ) ). 
 
"Syntax error in a method, syntax warning otherwise 
"No runtime error, but undefined behavior 
LOOP AT itab INTO DATA(wa). 
  IF sy-tabix = 2. 
    itab = jtab. 
  ENDIF. 
ENDLOOP. 
 
itab = VALUE #( ( 1 ) ( 2 ) ). 
 
"Syntax error in a method, syntax warning otherwise 
"Runtime error 
LOOP AT itab ASSIGNING FIELD-SYMBOL(<fs>). 
  IF sy-tabix = 2. 
    itab = jtab. 
  ENDIF. 
ENDLOOP.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Deleting all lines of an internal table within a loop over that table. while the loop with `ASSIGNING` results in runtime error `TABLE_FREE_IN_LOOP` the loop with `INTO` is executed without runtime error. The latter is shown for demonstration purposes, but not recommended. Since the deletion happens in a method, it is not detected by the syntax check.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS clear_itab CHANGING itab TYPE ANY TABLE. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD clear_itab. 
    CLEAR itab. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA itab TYPE TABLE OF i. 
 
    itab = VALUE #( ( 1 ) ( 2 ) ). 
 
    "No runtime error, but undefined behavior 
    LOOP AT itab INTO FINAL(wa). 
      demo=>clear_itab( CHANGING itab = itab ). 
    ENDLOOP. 
 
    itab = VALUE #( ( 1 ) ( 2 ) ). 
 
    "Runtime error 
    LOOP AT itab ASSIGNING FIELD-SYMBOL(<fs>). 
      demo=>clear_itab(  CHANGING itab = itab ). 
    ENDLOOP. 
  ENDMETHOD. 
ENDCLASS.
```
