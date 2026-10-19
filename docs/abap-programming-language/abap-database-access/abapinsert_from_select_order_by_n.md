---
title: "INSERT, MODIFY writable_obj, subquery, ORDER BY n"
source_file: abapinsert_from_select_order_by_n.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML > INSERT, MODIFY writable_obj, subquery_clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INSERT, MODIFY writable_obj, subquery, ORDER BY n

If the [target](abapiumd_target.md) is [client-independent](../../abap-glossary/abenclient_independent_glosry.md) the variant [`ORDER BY n`](abaporderby_clause.md) that specifies a column via its position in the result set of a [subquery](abapinsert_from_select.md) used in the statements [`INSERT`](abapinsert_dbtab.md) and [`MODIFY`](abapmodify_dbtab.md), works in the same way as in a main query.

If the target is [client-dependent](../../abap-glossary/abenclient_dependent_glosry.md), the following special rules apply:

- If none of the additions `USING CLIENT, CLIENTS` or the obsolete `CLIENT SPECIFIED` are specified in the `FROM` clause of the subquery, the first field of the result set of the subquery is the client column that is automatically added by the ABAP runtime framework and filled with a fixed value. The actual columns of the result set are counted from 2 on. If columns of the result set are defined by `*` or `data_source~*` in the [`SELECT` list](abapselect_list.md), the respective client columns are omitted.

- If an addition `USING CLIENT, CLIENTS` or the obsolete `CLIENT SPECIFIED` is specified in the `FROM` clause of the subquery:

  - If the [`SELECT`](abapselect_list.md) list is `*` or starts with `data_source~*`, a client column of the first data source is taken into account and client columns of further `data_source~*` are omitted when counting. If the first data source is a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), the implicitly added client column is taken into account.

  - If the [`SELECT`](abapselect_list.md) list starts with a column specification [`col_spec`](abapselect_clause_col_spec.md), this column is handled as the client column and is counted as the first column and client columns of further `data_source~*` are omitted when counting.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the rule expressed in the first bullet point above. `ORDER BY 2` specifies the column `CARRID` of the subquery and `ORDER BY 3` specifies the column `CARRNAME`.

``` abap
DATA itab TYPE TABLE OF scarr WITH EMPTY KEY. 
 
FINAL(out) = cl_demo_output=>new( ). 
 
itab = VALUE #( (  carrid = '11' carrname = 'zzz' ) 
                (  carrid = '22' carrname = 'yyy' ) 
                (  carrid = '33' carrname = 'xxx' ) ). 
 
DELETE FROM scarr 
             WHERE carrid = '11' OR carrid = '22' OR carrid = '33'. 
INSERT scarr FROM ( SELECT carrid, carrname, currcode, url 
                           FROM @itab AS itab 
                           ORDER BY 2 DESCENDING ). 
SELECT * 
       FROM scarr 
       WHERE carrid = '11' OR carrid = '22' OR carrid = '33' 
       INTO TABLE @FINAL(scarr_tab1). 
out->write( scarr_tab1 ). 
 
DELETE FROM scarr 
       WHERE carrid = '11' OR carrid = '22' OR carrid = '33'. 
INSERT scarr FROM ( SELECT carrid, carrname, currcode, url 
                           FROM @itab AS itab 
                           ORDER BY 3 ). 
SELECT * 
       FROM scarr 
       WHERE carrid = '11' OR carrid = '22' OR carrid = '33' 
       INTO TABLE @FINAL(scarr_tab2). 
out->write( scarr_tab2 ). 
 
ASSERT scarr_tab1 = scarr_tab2. 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

If the [`SELECT`](abapselect_list.md) list of the subquery is

`source1~*, source2~*`

where both sources are client dependent, then the first rule of the second bullet point applies: for counting with `n`:

- 1 is the client column of `source1`.

- 2 to *N*, where *N* is the number of columns of `source1`, are the other columns of `source1`.

- *N* + 1, ... are the columns of `source2` behind its client column.
