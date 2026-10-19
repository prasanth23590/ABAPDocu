---
title: "Checking Internal Tables"
source_file: abenmove_exact_itab.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Lossless Assignments > Lossless Assignments, Rules"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Checking Internal Tables

The operator [`EXACT`](abenconstructor_expression_exact.md) checks a table specified as an operand line-by-line against the tabular target type:

- If the line types are elementary, each line is checked for [elementary data objects](abenmove_exact_elementary.md).

- If the line types are structured, each line is checked for [structures](abenmove_exact_structure.md).

- If the line types are tabular, the check described here is performed. If the inner table is a table with an elementary line type, the line types must be compatible.

The [table category](../../abap-glossary/abentable_category_glosry.md) and the [table key](../../abap-glossary/abentable_key_glosry.md) are ignored by the check.

If the check raises an exception due to an invalid value or loss of values, the target table is filled with all lines assigned up to that point.

## Hints

- If an internal table with elementary line type is converted, this line type does not have to be compatible with the target line type but only needs to be convertible according to the conditions of `EXACT`. If an internal table with elementary line type is converted that occurs as an inner table of another table, it is handled like a structure component and the line types must be compatible.

- If internal tables are converted using the operator `EXACT`, only internal tables with elementary line type can raise an exception.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first seven lines of the internal table `itab` are assigned to the internal table `jtab`. When the eighth line is assigned, the exception `CX_SY_CONVERSION_NO_DATE` occurs.

``` abap
DATA itab TYPE STANDARD TABLE OF d 
          WITH EMPTY KEY. 
 
FINAL(invalid_date) = '20160&#x00DF;01'. 
 
itab = VALUE #( ( CONV d( '20160101' ) ) 
                ( CONV d( '20160201' ) ) 
                ( CONV d( '20160301' ) ) 
                ( CONV d( '20160401' ) ) 
                ( CONV d( '20160501' ) ) 
                ( CONV d( '20160601' ) ) 
                ( CONV d( '20160701' ) ) 
                ( CONV d( invalid_date ) ) 
                ( CONV d( '20160901' ) ) 
                ( CONV d( '20161001' ) ) 
                ( CONV d( '20161101' ) ) 
                ( CONV d( '20161201' ) ) ). 
 
DATA jtab TYPE SORTED TABLE OF string 
          WITH UNIQUE KEY table_line. 
 
TRY. 
    jtab = EXACT #( itab ). 
  CATCH cx_sy_conversion_no_date. 
ENDTRY. 
 
cl_demo_output=>display( jtab ).
```
