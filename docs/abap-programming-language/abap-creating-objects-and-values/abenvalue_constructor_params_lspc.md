---
title: "VALUE, line_spec"
source_file: abenvalue_constructor_params_lspc.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > VALUE, Value Operator > VALUE, Internal Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# VALUE, line_spec

## Syntax

``` abap
... line 
  | {LINES OF itab [FROM idx1] [TO idx2] [STEP n] [USING KEY keyname]} ...  
```

### Alternative

[1. `... line`](abenvalue_constructor_params_lspc.md#alternative-1)

[2. `... LINES OF jtab [FROM idx1] [TO idx2] [STEP n] [USING KEY keyname]`](abenvalue_constructor_params_lspc.md#alternative-2)

## Overview

### Description

Specification of one or more lines to be inserted when constructing an internal table with the value operator [`VALUE`](abenvalue_constructor_params_itab.md).

### Hint

If lines from the target table or the entire target table are used in `line_spec` in an assignment of a constructor expression using the value operator [`VALUE`](abenvalue_constructor_params_itab.md) to an internal table, these lines are deleted or overwritten with a start value before both variants of `line_spec` are evaluated. The target table must therefore be saved in an auxiliary variable first, for which a [`LET`](../abap-declarations/abaplet.md) expression can be used.

## Alternative 1

`... line`

### Description

Specification of a line. For `line`, the exact same specifications can be made as in the parentheses of an expression [`NEW line_type( ... )`](abenconstructor_expression_new.md), where `line_type` is the line type of the internal table and a corresponding line is constructed. The following special features apply here:

- If a data object is specified for `line`, this object must be compatible with the line type.

- If an expression (built-in function, functional method, calculation expression, constructor expression, or table expression) is specified for `line`, the result of the expression must be convertible to the line type.

- The syntax does not allow further parentheses for constructing tabular line types to be nested directly in `line`.

**Short Form for Structured Line Types**

If the line type of the internal table is a structured type, the following short form can be used:

``` abap
VALUE dtype|#( [let_exp] 
               [BASE itab] 
               col1 = dobj11 ... ( col2 = dobj12 col3 = dobj13 ... ) 
                                 ( col2 = dobj22 col3 = dobj23 ... ) 
                                 ... 
               col1 = dobj31 col2 = dobj32 ... ( col3 = dobj33 ... ) 
                                               ( col3 = dobj43 ... ) 
               ... ).
```

This has the same semantics as the following:

``` abap
VALUE dtype|#( [let_exp] 
               [BASE itab] 
               ( col1 = dobj11 ... col2 = dobj12 col3 = dobj13 ... ) 
               ( col1 = dobj11 ... col2 = dobj22 col3 = dobj23 ... ) 
               ... 
               ( col1 = dobj31 col2 = dobj32 ... col3 = dobj33 ... ) 
               ( col1 = dobj31 col2 = dobj32 ... col3 = dobj43 ... ) 
               ... ).
```

Values can be assigned to individual structure components outside of the inner parentheses. An assignment of this type applies to all subsequent inner parentheses until the next assignment is made to the corresponding component. Assignments outside of the inner parentheses must be followed by at least one inner parenthesis. Since a component cannot be assigned a value more than once in the [construction of a structure](abennew_constructor_params_struct.md), a component that has been assigned a value outside of the inner parentheses can no longer be listed in an inner parenthesis. A component can be specified again outside the inner parentheses and any components previously specified in an inner parenthesis can also be listed outside the parenthesis.

### Hints

- The restriction that the content of tabular line types cannot be constructed directly in `line` is introduced for reasons of legibility (for humans and for machines) and is not a functional restriction. The expression [`VALUE line_type( ... )`](abenconstructor_expression_value.md) can be specified for `line` to construct the content of a tabular line, where `line_type` is the tabular line type.

- The compatibility requirement for the line type can be met by specifying [`CONV line_type( ... )`](../abap-processing-internal-data/abenconstructor_expression_conv.md) for the values to be inserted.

- The short form for structured line types enables columns of internal tables that are to contain an identical value in blocks to be filled more easily.

- In `VALUE`, the table lines are constructed in accordance with the rules for the instance operator [`NEW`](abenconstructor_expression_new.md), since new table lines are created here and the restriction for `VALUE` dictating that no values of elementary data objects can be constructed cannot be applied.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Construction of a [ranges table](../../abap-glossary/abenranges_table_glosry.md) and filling it with four lines while using the short form for structured line types.

``` abap
DATA itab TYPE RANGE OF i. 
 
itab = VALUE #( sign = 'I'  option = 'BT' ( low = 1  high = 10 ) 
                                          ( low = 21 high = 30 ) 
                                          ( low = 41 high = 50 ) 
                            option = 'GE' ( low = 61 )  ).
```

## Alternative 2

`... LINES OF jtab [FROM idx1] [TO idx2] [STEP n] [USING KEY keyname]`

### Description

Specification of multiple lines. The lines are taken from the internal table `jtab` and inserted into the target table as a block. The same applies to `jtab` and the additions `FROM`, `TO`, `STEP` and `USING KEY` as to the addition [`LINES OF`](../abap-processing-internal-data/abapinsert_itab_linespec.md) of the statement [`INSERT`](../abap-processing-internal-data/abapinsert_itab.md) and the block is inserted in accordance with these rules. `jtab` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md).

### Hints

- Since the lines from `jtab` are inserted into the target table using only the table key, `jtab` must be compatible with the target type.

- If there is a conflict with an existing unique table key, an uncatchable exception is always raised when inserting multiple lines from an internal table using the statement [`INSERT`](../abap-processing-internal-data/abapinsert_itab.md).

- When standard tables are created, the lines of the table `jtab` are appended to the target table in the same way as with the statement [`APPEND LINES OF`](../abap-processing-internal-data/abapappend_linespec.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Construction of an internal table with an elementary line type. `jtab` is filled with three lines and `itab` with six lines. The first line inserted in `itab` is initial and the last three lines are taken from the table `jtab` filled previously.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES t_itab TYPE TABLE OF i WITH EMPTY KEY. 
 
FINAL(jtab) = VALUE t_itab( ( 10 ) ( 20 ) ( 30 ) ). 
 
FINAL(itab) = VALUE t_itab( ( ) ( 1 ) ( 2 ) ( LINES OF jtab ) ). 
 
out->write( itab ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Construction of an internal table with an elementary line type. `jtab` is filled with ten lines and `itab` with six lines. The first line inserted in `itab` is initial and the last three lines are taken from the table `jtab` filled previously. The additions `FROM` and `STEP` define the step size for processing the table `jtab`: Every second line starting at the sixth line is read.

``` abap
TYPES t_itab TYPE TABLE OF i WITH EMPTY KEY. 
 
FINAL(jtab) = VALUE t_itab( FOR i = 10 THEN i + 10 
  UNTIL i > 100 ( i ) ). 
 
FINAL(itab) = VALUE t_itab( ( ) ( 20 ) ( 40 ) 
  ( LINES OF jtab FROM 6 STEP 2 ) ).
```
