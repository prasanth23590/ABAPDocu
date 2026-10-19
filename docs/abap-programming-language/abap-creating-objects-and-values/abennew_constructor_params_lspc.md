---
title: "NEW, line_spec"
source_file: abennew_constructor_params_lspc.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > NEW, Instance Operator > NEW, Internal Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# NEW, line_spec

## Syntax

``` abap
... line 
  | {LINES OF jtab [FROM idx1] [TO idx2] [STEP n] [USING KEY keyname]} ...  
```

### Alternative

[1. `... line`](abennew_constructor_params_lspc.md#alternative-1)

[2. `... LINES OF jtab [FROM idx1] [TO idx2] [STEP n] [USING KEY keyname]`](abennew_constructor_params_lspc.md#alternative-2)

## Overview

### Description

Specification of one or more lines to be inserted when constructing an internal table with the instance operator [`NEW`](abennew_constructor_params_itab.md).

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
NEW dtype|#( [let_exp] 
             [BASE itab] 
             col1 = dobj11 ... ( col2 = dobj12 col3 = dobj13 ... ) 
                               ( col2 = dobj22 col3 = dobj23 ... ) 
                               ... 
             col1 = dobj31 col2 = dobj32 ... ( col3 = dobj33 ... ) 
                                             ( col3 = dobj43 ... ) 
             ... ).
```

This has the same semantics as the following form:

``` abap
NEW dtype|#( [let_exp] 
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

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Construction of an anonymous internal table with a structured line type with a short form for the first column:

``` abap
TYPES: 
  BEGIN OF t_line, 
    col1 TYPE i, 
    col2 TYPE i, 
  END OF t_line, 
  t_itab TYPE TABLE OF t_line WITH EMPTY KEY. 
 
FINAL(dref) = NEW t_itab( col1 = 1 ( col2 = 11 ) 
                                  ( col2 = 12 ) 
                                  ( col2 = 13 ) 
                         col1 = 2 ( col2 = 21 ) 
                                  ( col2 = 22 ) 
                                  ( col2 = 23 ) ). 
 
cl_demo_output=>display( dref->* ).
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

Construction of an internal table `itab` that contains the first three lines and last three lines of the previously constructed internal table `alpha`.

``` abap
DATA: 
  alpha TYPE TABLE OF string WITH EMPTY KEY, 
  itab  LIKE REF TO alpha. 
 
FINAL(abcde) = `abcdefghijklmnopqrstuvwxyz`. 
alpha = VALUE #(  FOR j = 0 UNTIL j >= strlen( abcde ) 
                  ( substring( val = abcde 
                               off = j 
                               len = 1  ) ) ). 
 
itab = NEW #( ( LINES OF alpha FROM 1 TO 3 ) 
              ( `-` ) 
              ( LINES OF alpha FROM lines( alpha ) - 2 
                               TO   lines( alpha ) ) ). 
cl_demo_output=>display( itab->* ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Construction of an internal table `itab` that contains lines of the previously constructed internal table `jtab`. The additions `FROM` and `STEP` define the step size for processing the table `jtab`: First, every second line starting at the third line is read, second, every third line starting at the second line is read.

``` abap
TYPES: t_itab TYPE TABLE OF i WITH EMPTY KEY. 
 
FINAL(jtab) = VALUE t_itab( FOR i = 1 UNTIL i > 10 ( i ) ). 
 
FINAL(itab) = NEW t_itab( ( LINES OF jtab FROM 3 STEP 2 ) 
                         ( LINES OF jtab FROM 2 STEP 3 ) ).
```
