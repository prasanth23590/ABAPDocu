---
title: "SELECT, ORDER BY, col_additions"
source_file: abaporderby_clause_additions.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, ORDER BY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, ORDER BY, col_additions

## Syntax

``` abap
... [ASCENDING|DESCENDING] 
    [{NULLS FIRST}|{NULLS LAST}] ...  
```

### Addition

[1. `... ASCENDING|DESCENDING`](abaporderby_clause_additions.md#addition-1)

[2. `... {NULLS FIRST}|{NULLS LAST}`](abaporderby_clause_additions.md#addition-2)

## Overview

### Description

These additions to single column specifications in the [`ORDER BY`](abaporderby_clause.md) clause of a `SELECT` statement determine the sort direction and the handling of [null values](../../abap-glossary/abennull_value_glosry.md).

## Addition 1

`... ASCENDING|DESCENDING`

### Description

The additions `ASCENDING` and `DESCENDING` determine whether the column or expression in question is sorted in ascending or descending order. If neither addition is specified, the column or expression is sorted in ascending order. The priority of sorting is based on the order in which the components `col1, col2...` or `a1, a2 ...` are specified.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The rows of DDIC database table `sflight` are grouped by the columns `carrid` and `connid`, where for each group the minimum of column `seatsocc` is determined. The selection is sorted in ascending order by `carrid` and in descending order by the minimum of occupied seats. The alternative name `min` is used for the aggregate expression.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT carrid, connid, MIN( seatsocc ) AS min 
       FROM sflight 
       GROUP BY carrid, connid 
       ORDER BY carrid ASCENDING, min DESCENDING 
       INTO TABLE @FINAL(result). 
 
out->write_data( result ). 
 
out->display( ).
```

## Addition 2

`... {NULLS FIRST}|{NULLS LAST}`

### Description

The additions `NULLS FIRST` and `NULLS LAST` determine whether [null values](../../abap-glossary/abennull_value_glosry.md) are placed in front of or after non-null values. If neither addition is specified, potential [null values](../../abap-glossary/abennull_value_glosry.md) are placed at the beginning of the result set. If only `DESCENDING` is specified and no [nulls](../../abap-glossary/abennull_value_glosry.md) occur, [null values](../../abap-glossary/abennull_value_glosry.md) are placed at the end of the result set.

The following table shows the default behavior of the additions `ASCENDING`, `DESCENDING`, `NULLS FIRST`, and `NULLS LAST`.

| **Addition** | **Default Behavior of Result Set** |
|--------------|------------------------------------|
| No addition  | `ASCENDING` + `NULLS FIRST`        |
| `NULLS LAST` | `ASCENDING` + `NULLS LAST`         |
| `DESCENDING` | `DESCENDING` + `NULLS LAST`        |

Columns specified after `ORDER BY` cannot be of the [type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) `LCHR`, `LRAW`, `STRING`, `RAWSTRING`, or `GEOM_EWKB`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

To generate null values, a left outer join is performed on table `DEMO_SFLIGHT_AGG` and the result set is sorted by its column `CARRID` with nulls at the end of the table. The class `CL_DEMO_SELECT_ORDER_NULLS` executes the statement and displays the result.

``` abap
SELECT FROM demo_sflight_agg AS a LEFT OUTER JOIN demo_sflight_agg AS b 
      ON a~carrid = b~carrid AND 
         a~connid = b~connid AND 
         a~fldate = b~fldate AND 
         a~connid LIKE '04%' 
      FIELDS a~carrid, 
             a~fldate AS a_fldate, 
             a~connid, 
             a~seatsocc, 
             b~carrid AS b_carrid, 
             b~fldate AS b_fldate, 
             b~connid AS b_connid, 
             b~seatsocc AS b_seatsocc 
      WHERE a~carrid LIKE 'A%' 
           AND a~fldate LIKE '%' 
           AND a~connid LIKE '0%' 
      ORDER BY b~carrid NULLS LAST 
      INTO TABLE @FINAL(result).
```

  
![figure](images_abdoc_select_order_null.png)
