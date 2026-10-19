---
title: "MODIFY writable_obj, source"
source_file: abapmodify_source.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML > MODIFY writable_obj"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MODIFY writable_obj, source

## Syntax

``` abap
... { { @wa|@( expr ) [indicators  | MAPPING FROM ENTITY  ] } 
  | { TABLE @itab [indicators  | MAPPING FROM ENTITY  ] } 
  | {( SELECT subquery_clauses [UNION| INTERSECT| EXCEPT ...] )} } ...  
```

[`indicators `](abapselect_indicators.md) · [`MAPPING FROM ENTITY `](../../abap-rap-business-objects/abap-for-rap-business-objects/abapmapping_from_entity.md) · [`indicators `](abapselect_indicators.md) · [`MAPPING FROM ENTITY `](../../abap-rap-business-objects/abap-for-rap-business-objects/abapmapping_from_entity.md) · [`subquery_clauses`](abapinsert_from_select.md) · [`UNION| INTERSECT| EXCEPT ...`](abapunion.md)

### Alternative

1\. ... @wa\|@( expr ) \[[`indicators`](abapselect_indicators.md)\| [`MAPPING FROM ENTITY`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapmapping_from_entity.md)\]

2\. ... TABLE @itab \[[`indicators`](abapselect_indicators.md)\| [`MAPPING FROM ENTITY`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapmapping_from_entity.md)\]

[3. `... SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] ...`](abapmodify_source.md#alternative-3)

## Overview

### Description

A non-table-like data object `wa` can be specified after `FROM` in the statement [`MODIFY`](abapmodify_dbtab.md) and an internal table or a parenthesized [subquery](abenabap_sql_host_variables.md) can be specified after `TABLE`. The work area and the internal table can be specified as a [host variable](abenabap_sql_host_variables.md) or a [host expression](abenabap_sql_host_expressions.md). On one hand, the content of the data objects or the result set of the subquery determines whether the rows are inserted or changed, and on the other hand, which values are inserted or used for changes.

## Alternative 1

`... @wa|@( expr ) [indicators| MAPPING FROM ENTITY]`

### Description

When a non-table-like work area that meets the [requirements](abenabap_sql_host_expressions.md) for use in ABAP SQL statements is specified as a host variable [`@wa`](abenabap_sql_host_variables.md) or host expression [`@( expr )`](abenabap_sql_host_expressions.md), a row is searched in the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) that has the same content in the [primary key](../../abap-glossary/abenprimary_key_glosry.md) as the corresponding initial part of the work area.

- If a row like this is found, this row is overwritten in accordance with the same rules as for the statement [`UPDATE`](abapupdate_source.md).

- If a row like this is not found, a new row is inserted according to the same rules as for the statement [`INSERT`](abapinsert_source.md).

If the change would produce a duplicate entry in a unique secondary index, it is not executed and `sy-subrc` is set to 4.

[Implicit ABAP SQL client handling](abenabap_sql_client_handling.md) applies, in which a [client ID](../../abap-glossary/abenclient_identifier_glosry.md) specified in `wa` is ignored. The [current client](../../abap-glossary/abencurrent_client_glosry.md) is used by default.

The `MAPPING FROM ENTITY` addition is used to handle structures and internal tables that are typed with [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md). Find more information in the topic [ABAP SQL Statements with `MAPPING FROM ENTITY`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapmapping_from_entity.md).

### Hints

- [indicators](abapselect_indicators.md) is not allowed in combination with [`MAPPING FROM ENTITY`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapmapping_from_entity.md).

- Exceptions due to invalid values can also be raised in compatible work areas. For example, components of the types `d` and `t` can contain invalid dates and times that are not accepted by columns of the types `DATN` and `TIMN`.

- If a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) is specified as a [host expression](abenabap_sql_host_expressions.md) for the work area `wa`, for which the data type is inferred using the `#` character, a structure consisting of all the database table columns is created as the type.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creating or changing a [message](../../abap-glossary/abenmessage_glosry.md) in a DDIC database table. If there is no message with the number 100 in the `MYMSGCLASS` message class in English, it will be created. Otherwise, only the text is changed.

``` abap
FINAL(message_wa) = VALUE t100( 
  sprsl = 'E' 
  arbgb = 'MYMSGCLASS' 
  msgnr = '100' 
  text =  'Some new message ...' ). 
 
MODIFY t100 FROM @message_wa.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The same example as before, but with a host expression.

``` abap
MODIFY t100 FROM @( VALUE #( 
  sprsl = 'E' 
  arbgb = 'MYMSGCLASS' 
  msgnr = '100' 
  text  = 'Some new message ...'  ) ).
```

## Alternative 2

`... TABLE @itab [indicators| MAPPING FROM ENTITY]`

### Description

When an internal table is specified as a host variable [`@itab`](abenabap_sql_host_variables.md) or host expression [`@( expr )`](abenabap_sql_host_expressions.md), its rows are evaluated to overwrite existing rows or to insert new rows. The row type of the internal table must meet the [prerequisites](abenabap_sql_wa.md) for use in ABAP SQL statements.

This behavior is platform-dependent and follows one of the following patterns depending on the database system:

- `UPDATE` followed by `INSERT`:

  - First, the same function as for [`UPDATE FROM TABLE`](abapupdate_source.md) is executed for all rows of the internal table.

  - Next, the same function as for [`INSERT FROM TABLE`](abapinsert_source.md) is executed for all rows. Here, any rows that have the same [primary key](../../abap-glossary/abenprimary_key_glosry.md) or unique [secondary index](../../abap-glossary/abensecondary_index_glosry.md) are ignored.

    The processing of the rows in the internal table can also be split into blocks depending on the database system.

- Row by row `MODIFY`

  In a loop, each row in the internal table is processed in accordance with the rule above for `MODIFY ... FROM wa`. Here, the database system specifies whether processing continues in cases where a row could not be inserted due to a unique secondary index.

These two platform-dependent processing methods can produce different results in cases where the DDIC database table has unique secondary indexes (see [executable example](abenbulk_modify_abexa.md)).

If the change to a row in the internal table would produce a duplicate entry in a unique secondary index, the corresponding row is not inserted and `sy-subrc` is set to 4. If the internal table is empty, no rows are processed. However, `sy-subrc` is still set to 0. The system field `sy-dbcnt` is set to the number of rows that are actually processed.

The `MAPPING FROM ENTITY` addition is used to handle structures and internal tables that are typed with [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md). Find more information in the topic [ABAP SQL Statements with `MAPPING FROM ENTITY`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapmapping_from_entity.md).

### Hints

- [indicators](abapselect_indicators.md) is not allowed in combination with [`MAPPING FROM ENTITY`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapmapping_from_entity.md). To prevent platform-dependent behavior, `MODIFY ... FROM itab` should only be applied to DDIC database tables without unique secondary indexes. If not, the required behavior must be programmed explicitly using `UPDATE` and `INSERT` or using `LOOP AT itab` and `MODIFY`.

- If a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) as a [host expression](abenabap_sql_host_expressions.md) is specified as an internal table `itab`, for which the data type is inferred using the `#` character, a structured standard table whose row type consists of all the database table columns with an empty table key is created as the type.

- When an internal table is specified, [locators](../../abap-glossary/abenlocator_glosry.md) can be used as a source, but no [writer streams](../../abap-glossary/abenwriter_stream_glosry.md) can be created.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation or changing of multiple rows in DDIC database table `DEMO_UPDATE`. This DDIC database table does not have a unique secondary index and the result is therefore not platform-dependent.

``` abap
TYPES itab TYPE TABLE OF demo_update WITH EMPTY KEY. 
 
FINAL(itab) = VALUE itab( 
  ( id = 'X' col1 =  1 col2 =  2 col3 =  3 col4 =  4 ) 
  ( id = 'Y' col1 = 11 col2 = 12 col3 = 13 col4 = 14 ) 
  ( id = 'Z' col1 = 21 col2 = 22 col3 = 23 col4 = 24 ) ). 
 
MODIFY demo_update FROM TABLE @itab.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The same example as before, but with a host expression.

``` abap
MODIFY demo_update FROM TABLE @( 
  VALUE #( ( id = 'X' col1 =  1 col2 =  2 col3 =  3 col4 =  4 ) 
           ( id = 'Y' col1 = 11 col2 = 12 col3 = 13 col4 = 14 ) 
           ( id = 'Z' col1 = 21 col2 = 22 col3 = 23 col4 = 24 ) ) ).
```

### Executable Example

[`MODIFY FROM TABLE`](abenbulk_modify_abexa.md)

## Alternative 3

`... ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] ) ...`

### Description

If a parenthesized [subquery](../../abap-glossary/abensubquery_glosry.md) is specified, the rows in the result set defined by [`subquery_clauses`](abapinsert_from_select.md) are evaluated to overwrite the existing rows or to insert new rows. The [set operators](../../abap-glossary/abencds_set_operators_glosry.md) [`UNION`](abapunion.md), [`INTERSECT`](abapunion.md), and [`EXCEPT`](abapunion.md) can be used to combine the result sets of multiple subqueries. In this case, special rules [`query_clauses`](abapunion_clause.md) apply to specifying clauses.

When used with a subquery, the statement `MODIFY` is platform-dependent, as above when an internal table is specified, and follows one of the two following database-dependent patterns:

- `UPDATE` followed by `INSERT`

- Row-by-row `MODIFY`

With respect to the following actions,

- client handling,

- inserting or modifying the data in the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) and

- handling of null values,

the same rules and notes apply as when using a subquery as a [data source](abapinsert_source.md) of the statement [`INSERT`](abapinsert_dbtab.md). In particular, a subquery cannot be used if [logging](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_protocol.md) is enabled for the table to be modified.

If the result set of the subquery is empty, no rows are processed and `sy-subrc` is set to 4.

A subquery in the statement `MODIFY` is not supported by all databases. If this is detected at runtime on a database that does not support the pragma, a catchable exception of the class `CX_SY_SQL_UNSUPPORTED_FEATURE` is raised.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A subquery of the statement `MODIFY` reads all rows in the database table `demo_join3` and uses the result set to modify the database table `demo_join1`. Two rows of the result set overwrite existing rows in `demo_join1` and a row is inserted. Only if logging is disabled for DDIC database table `DEMO_JOIN1`, a subquery can be used. Otherwise, the data must be inserted into an internal table that serves as a source for the modification.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DELETE FROM demo_join1. 
INSERT demo_join1 
  FROM TABLE @( VALUE #( ( a = 'a1' b = 'b1' c = 'c1' d = 'd1' ) 
                         ( a = 'a2' b = 'b2' c = 'c2' d = 'd2' ) ) ). 
DELETE FROM demo_join3. 
INSERT demo_join3 
  FROM TABLE @( VALUE #( ( i = 'a1' j = 'j1' k = 'k1' l = 'l1' ) 
                         ( i = 'a2' j = 'j2' k = 'k2' l = 'l2' ) 
                         ( i = 'i3' j = 'j3' k = 'k3' l = 'l3' ) ) ). 
 
IF cl_dbi_utilities=>is_logging_on( 'DEMO_JOIN1' ) IS INITIAL. 
  MODIFY demo_join1 FROM ( SELECT i, j, k, l FROM demo_join3 ) 
         ##logging_versus_from_select[demo_join1]. 
ELSE. 
  SELECT i, j, k, l FROM demo_join3 
    INTO TABLE @FINAL(buffer). 
  MODIFY demo_join1 FROM TABLE @buffer. 
ENDIF. 
 
SELECT * 
       FROM demo_join1 
       INTO TABLE @FINAL(result). 
 
out->write( result ). 
 
out->display( ).
```
