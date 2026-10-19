---
title: "READ TABLE, transport_options"
source_file: abapread_table_transport_options.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > READ TABLE itab > READ TABLE, result"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# READ TABLE, transport_options

## Syntax

``` abap
 ... [COMPARING { {comp1 comp2 ...}|{ALL FIELDS}|{NO FIELDS} }] 
    [TRANSPORTING { {comp1 comp2 ...}|{ALL FIELDS} }] ...  
```

[`comp1 comp2 ...`](abenitab_components.md) · [`comp1 comp2 ...`](abenitab_components.md)

## Description

The addition `COMPARING` compares the specified components `comp1 comp2 ...` or their subareas or attributes in a found line before they are transported with the corresponding components of the work area. If `ALL FIELDS` is specified, all components are compared. If no `NO FIELDS` is specified, no components are compared. If the content of the compared components is identical, `sy-subrc` is set to 0 and otherwise to 2. The line found is assigned to the work area independently of the result of the comparison.

If the addition `TRANSPORTING` is specified, only the specified components `comp1 comp2 ...` or their subareas in the found line are assigned to the corresponding components of the work area or its subareas. If `ALL FIELDS` is specified, all components are assigned.

`COMPARING` must be specified in front of `TRANSPORTING`. The components `comp1 comp2 ...` are specified according to the rules in the section [Specifying Components](abenitab_components.md), with the restriction that after `TRANSPORTING`, no attributes of classes can be addressed using the object component selector.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The `READ` statement uses a [`WHILE`](../abap-program-flow-logic/abapwhile.md) loop to read all lines of the table `sflight_tab` one after the other using the primary table index in the work area `sflight_wa`. Only fields that are also in the output are transported. The `COMPARING` addition is used to select all flights in which no seats have yet been booked.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: sflight_tab TYPE SORTED TABLE OF sflight 
                  WITH UNIQUE KEY carrid connid fldate, 
      sflight_wa  LIKE LINE OF sflight_tab, 
      output      TYPE TABLE OF string WITH EMPTY KEY. 
 
DATA subrc TYPE sy-subrc. 
 
SELECT * 
       FROM sflight 
       WHERE carrid = 'LH' 
       INTO TABLE @sflight_tab. 
 
subrc = sy-subrc. 
WHILE subrc = 0. 
  sflight_wa-seatsocc = 0. 
  READ TABLE sflight_tab 
       INDEX sy-index 
       INTO sflight_wa COMPARING seatsocc 
                       TRANSPORTING carrid 
                                    connid 
                                    fldate 
                                    seatsocc. 
  CASE sy-subrc. 
    WHEN 0. 
      APPEND |{ sflight_wa-carrid } { sflight_wa-connid } { 
                sflight_wa-fldate } { sflight_wa-seatsocc } <----!| 
        TO output. 
      subrc = sy-subrc. 
    WHEN 2. 
      APPEND |{ sflight_wa-carrid } { sflight_wa-connid } { 
                sflight_wa-fldate } { sflight_wa-seatsocc }| 
        TO output. 
      subrc = 0. 
    WHEN 4 OR 8. 
      EXIT. 
  ENDCASE. 
ENDWHILE. 
out->write( output ). 
 
out->display( ).
```
