---
title: "INSERT writable_obj, source"
source_file: abapinsert_source.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML > INSERT writable_obj"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INSERT writable_obj, source

## Syntax

``` abap
...  @wa|@( expr ) [MAPPING FROM ENTITY  ]   
  | { TABLE @itab|@( expr ) [MAPPING FROM ENTITY  ] [ACCEPTING DUPLICATE KEYS] }   
  | ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] ) ...  
```

[`MAPPING FROM ENTITY `](../../abap-rap-business-objects/abap-for-rap-business-objects/abapmapping_from_entity.md) · [`MAPPING FROM ENTITY `](../../abap-rap-business-objects/abap-for-rap-business-objects/abapmapping_from_entity.md) · [`subquery_clauses`](abapinsert_from_select.md) · [`UNION|INTERSECT|EXCEPT ...`](abapunion.md)

### Alternative

[1. `... @wa|@( expr ) [MAPPING FROM ENTITY] ...`](abapinsert_source.md#alternative-1)

[2. `... TABLE @itab|@( expr ) [MAPPING FROM ENTITY] [ACCEPTING DUPLICATE KEYS] ...`](abapinsert_source.md#alternative-2)

[3. `... ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] ) ...`](abapinsert_source.md#alternative-3)

## Overview

### Description

Data sources of the ABAP SQL [`INSERT`](abapinsert_dbtab.md) statement:

- After the additions `VALUES` and `FROM`, a non-table-like data object can be specified as a host variable [`@wa`](abenabap_sql_host_variables.md) or host expression [`@( expr )`](abenabap_sql_host_expressions.md).

- After `FROM TABLE`, an internal table can be specified as a host variable [`@itab`](abenabap_sql_host_variables.md) or host expression [`@( expr )`](abenabap_sql_host_expressions.md).

- After `FROM TABLE`, a [subquery](abapinsert_from_select.md) can be specified.

The content of the row or rows to be inserted is taken from these data objects or from the result set of the subquery.

## Alternative 1

`... @wa|@( expr ) [MAPPING FROM ENTITY] ...`

### Description

After [`VALUES`](abapinsert_dbtab.md) and [`FROM`](abapinsert_dbtab.md), a non-table-like work area can be specified as a host variable [`@wa`](abenabap_sql_host_variables.md) or as a host expression [`@( expr )`](abenabap_sql_host_expressions.md), from whose content a row is created for insertion into the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md). The work area must meet the [prerequisites](abenabap_sql_wa.md) for use in ABAP SQL statements.

- When specifying a work area that does not contain any reference variables for [LOB handles](../../abap-glossary/abenlob_handle_glosry.md), the content of the row to be inserted is taken from the work area `wa` while ignoring its data type and from left to right in accordance with the structure of the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md). No conversion is made to the ABAP type that is assigned to a column using its [dictionary type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- When a [LOB handle structure](../../abap-glossary/abenlob_handle_structure_glosry.md) is specified, it must be constructed exactly like the structure of the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md), in accordance with the [prerequisites](abenabap_sql_wa.md). The components of the work area that are not [LOB Handle components](../../abap-glossary/abenlob_handle_component_glosry.md) are assigned directly to the corresponding columns of the new row. In the case of a LOB handle component of a read stream type, this type is created. In the case of a type for a locator, this must exist and is used as a source. For details, see [LOB handles](abenium_lob.md).

The new row is inserted into the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) if it does not already contain a row with the same [primary key](../../abap-glossary/abenprimary_key_glosry.md) or the same unique secondary index. If it does, the row is not inserted and `sy-subrc` is set to 4. When the row is inserted, the content of the work area assigned to the individual columns of the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) is mapped by the [database interface](../../abap-glossary/abendatabase_interface_glosry.md) to its data types and converted if necessary. If content is not suitable, overflows or invalid values may raise exceptions.

[Implicit ABAP SQL client handling](abenabap_sql_client_handling.md) applies, in which a [client ID](../../abap-glossary/abenclient_identifier_glosry.md) specified in `wa` is ignored. The [current client](../../abap-glossary/abencurrent_client_glosry.md) is used by default.

The `MAPPING FROM ENTITY` addition is used to handle structures and internal tables that are typed with [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md). Find more information in the topic [ABAP SQL Statements with `MAPPING FROM ENTITY`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapmapping_from_entity.md).

### Hints

- The work area `wa` should always be declared in relation to the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md). For the derivation of [LOB handle structures](../../abap-glossary/abenlob_handle_structure_glosry.md), there are special [additions](../abap-declarations/abaptypes_lob_handle.md) of the statements `TYPES` and `[CLASS-]DATA`.

- Exceptions due to invalid values can be raised in compatible work areas. For example, components of the types `d` and `t` can contain invalid dates and times that are not accepted by columns of the types `DATN` and `TIMN`.

- If a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) is specified as a [host expression](abenabap_sql_host_expressions.md) for the work area `wa`, for which the data type is inferred using the `#` character, a structure consisting of all the database table columns is created as the type.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Insertion of a new airline into the DDIC database table `SCARR` using a work area `wa`.

``` abap
DATA scarr_wa TYPE scarr. 
 
scarr_wa = VALUE #( 
  carrid   = 'FF' 
  carrname = 'Funny Flyers' 
  currcode = 'EUR' 
  url      = 'http://www.funnyfly.com' ). 
 
INSERT INTO scarr VALUES @scarr_wa.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Insertion of a new airline into the DDIC database table `SCARR` with the value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) in a [host expression](abenabap_sql_host_expressions.md).

``` abap
INSERT INTO scarr VALUES @( VALUE #( 
  carrid   = 'FF' 
  carrname = 'Funny Flyers' 
  currcode = 'EUR' 
  url      = 'http://www.funnyfly.com' ) ).
```

## Alternative 2

`... TABLE @itab|@( expr ) [MAPPING FROM ENTITY] [ACCEPTING DUPLICATE KEYS] ...`

### Description

An internal table `itab` can be specified as a host variable [`@itab`](abenabap_sql_host_variables.md) or host expression [`@( expr )`](abenabap_sql_host_expressions.md) after [`FROM`](abapinsert_dbtab.md) and `TABLE`, from whose content multiple rows are created for insertion into the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md). The row type of the internal table must meet the [prerequisites](abenabap_sql_wa.md) for use in ABAP SQL statements.

The content of each row of the internal table is assembled into a row to be inserted using the same rules as for a single work area `wa` with the exception that when inserting from an internal table, [locators](../../abap-glossary/abenlocator_glosry.md) operate as the source but no [writer streams](../../abap-glossary/abenwriter_stream_glosry.md) can be created.

If no row with the same [primary key](../../abap-glossary/abenprimary_key_glosry.md) or with the same unique secondary index exists in the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) for any of the rows to be inserted, all rows are inserted and `sy-subrc` is set to 0. If the internal table is empty, no rows are inserted. However, `sy-subrc` is still set to 0. The system field `sy-dbcnt` is set to the number of rows that are inserted.

If a row with the same primary key or the same unique secondary index exists in the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) for one or more of the rows to be inserted, these rows cannot be inserted. In this situation, there are the following options:

- Use of `ACCEPTING DUPLICATE KEYS`

  If the addition `ACCEPTING DUPLICATE KEYS` is specified, all rows are inserted for which this is possible. All rows that would produce duplicate entries with respect to the primary key or to a unique secondary index are discarded and `sy-subrc` set to 4. The system field `sy-dbcnt` is set to the number of rows that are inserted.

- No use of `ACCEPTING DUPLICATE KEYS`

  - Handling of the exception `CX_SY_OPEN_SQL_DB`

    If the addition `ACCEPTING DUPLICATE KEYS` is not specified, the catchable exception `CX_SY_OPEN_SQL_DB` is raised when a duplicate row is inserted. Rows continue to be inserted until the exception is raised and handled. The number of inserted rows is undefined. The system fields `sy-subrc` and `sy-dbcnt` retain their previous value.

  - No handling of the exception `CX_SY_OPEN_SQL_DB`

    If the addition `ACCEPTING DUPLICATE KEYS` is not specified and if the exception is not handled, a runtime error occurs when a duplicate row is inserted. This executes a [database rollback](abendb_rollback.md) that undoes all changes to the current [database LUW](abendb_transaction.md). This applies in particular to rows that were inserted before the duplicate entry was made.

The `MAPPING FROM ENTITY` addition is used to handle structures and internal tables that are typed with [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md). Find more information in the topic [ABAP SQL Statements with `MAPPING FROM ENTITY`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapmapping_from_entity.md).

### Hints

- The addition `ACCEPTING DUPLICATE KEYS` does not indicate that duplicate key entries are accepted in the strict sense of the word. More specifically, no change is made to an existing entry as is the case when [`MODIFY`](abapmodify_dbtab.md) is used. Instead, `ACCEPTING DUPLICATE KEYS` prevents the associated exception from being raised and sets the return code `sy-subrc` to 4.

- If the runtime error produced by inserting existing rows is prevented by handling an exception instead of using the addition `ACCEPTING DUPLICATE KEYS`, a database rollback must be initiated explicitly, if required.

- If an internal table is used, package-by-package processing causes any read accesses running in parallel to `INSERT` to view only some of the rows to be inserted.

- If a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) as a [host expression](abenabap_sql_host_expressions.md) is specified as an internal table `itab`, for which the data type is inferred using the `#` character, a structured standard table whose row type consists of all the database table columns with an empty table key is created as the type.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Insertion of multiple rows in a [host expression](abenabap_sql_host_expressions.md) using the value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md). This example shows the two ways of dealing with duplicate rows.

``` abap
TRY. 
    INSERT scarr FROM TABLE @( VALUE #( 
      ( carrid   = 'FF' 
        carrname = 'Funny Flyers' 
        currcode = 'EUR' 
        url      = 'http://www.funnyfly.com' ) 
      ( carrid   = 'XXL' 
        carrname = 'Extra Large Line' 
        currcode = 'USD' 
        url      = 'http://www.xxlline.com' ) ) ). 
  CATCH cx_sy_open_sql_db. 
    ... 
ENDTRY. 
 
INSERT scarr FROM TABLE @( VALUE #( 
  ( carrid   = 'FF' 
    carrname = 'Funny Flyers' 
    currcode = 'EUR' 
    url      = 'http://www.funnyfly.com' ) 
  ( carrid   = 'XXL' 
    carrname = 'Extra Large Line' 
    currcode = 'USD' 
    url      = 'http://www.xxlline.com' ) ) ) ACCEPTING DUPLICATE KEYS. 
IF sy-subrc = 4. 
  ... 
ENDIF.
```

## Alternative 3

`... ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] ) ...`

### Description

A parenthesized [subquery](../../abap-glossary/abensubquery_glosry.md) can be specified as a data source after [`FROM`](abapinsert_dbtab.md). The rows of the result set of a subquery are inserted, which is defined by the corresponding clauses [`subquery_clauses`](abapinsert_from_select.md). The [set operators](../../abap-glossary/abencds_set_operators_glosry.md) [`UNION`](abapunion.md), [`INTERSECT`](abapunion.md), and [`EXCEPT`](abapunion.md) can be used to combine the result sets of multiple subqueries. In this case, special rules [`query_clauses`](abapunion_clause.md) apply when specifying clauses.

The statement `INSERT` with subquery cannot be used if [logging](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_protocol.md) is enabled for the table to be filled. If used for a DDIC database table with logging enabled, the uncatchable exception `DBSQL_DBPRT_STATEMENT` is raised. The corresponding warning from the syntax check can be switched off with the pragma `##logging_versus_from_select`.

The data from the result set is inserted into the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) to be filled column by column in the database system. Columns are assigned using their position. The columns names in the result set are not important for assignment purposes. The columns assigned to each other must have the same type properties with respect to [built-in data type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), length, and number of decimal places, with the following exceptions:

- In the case of the numeric types [`INT1`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT2`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`INT4`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), and [`INT8`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), columns with a smaller value range can be assigned to a column with a greater value range.

- In the case of the numeric type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), columns with shorter lengths can be assigned to columns with greater lengths. Furthermore, columns with fewer decimal places can be assigned to columns with more decimal places, as long as there are enough integer digits. The corresponding special types [`CURR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`QUAN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) are handled here like [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- The numeric types [`DF16_DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`DF34_DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) are handled like the numbers of type [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) as they are stored and the rule above applies with respect to lengths and decimal places.

- In the case of the character-like type [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), columns with shorter lengths can be assigned to columns with greater lengths. The corresponding special types [`CLNT`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`LANG`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`CUKY`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), and [`UNIT`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) are handled here like [`CHAR`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

All other types must be exactly the same. This applies specifically to [`NUMC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`RAW`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), where the lengths must match. The different categories of [strings](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_character_byte_types.md) cannot be combined either.

The statement `INSERT` with subquery does not insert [null values](../../abap-glossary/abennull_value_glosry.md) into the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) to be filled. Null values to be inserted can be produced in the following cases:

- As results of [outer joins](abapselect_join.md) in the `FORM` clause of the subquery.

- As results of [SQL expressions](abapsql_expr.md) in the `SELECT` list of the subquery.

- If a field read by the subquery already contains a null value.

In these cases, the following is done instead of inserting a null value:

- The type-dependent [initial value](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is inserted for columns that are not [key fields](../../abap-glossary/abenkey_field_glosry.md) of the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) to be filled.

- A catchable exception of exception class `CX_SY_OPEN_SQL_DB` is raised in the case of columns that are [key fields](../../abap-glossary/abenkey_field_glosry.md) of the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) to be filled. If it is known statically that null values can be inserted into key fields, a syntax check warning that can be hidden by the pragma `null_values` is produced.

Columns of the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) to be filled that do not have a column in the result set of the subquery are also filled with their type-dependent initial value.

If it was possible to insert all rows of the result set, `sy-subrc` is set to 0. If it was not possible to insert a row from the result set, since a row with the same [primary key](../../abap-glossary/abenprimary_key_glosry.md) or an identical unique secondary index exists, all previously inserted rows are discarded and a catchable exception of the class `CX_SY_OPEN_SQL_DB` is raised. If the result set of the subquery is empty, no row is inserted and `sy-subrc` is set to 4.

### Hints

- Using subqueries has better performance than using standalone `SELECT` statements to read data into an internal table and using this table as a data source.

- Unlike when inserting rows from an internal table `itab`, the content of the modified [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) is always defined after the exception `CX_SY_OPEN_SQL_DB` is handled.

- This variant of the `INSERT` statement is particularly well suited for filling [global temporary tables](../../abap-glossary/abenglobal_temporary_table_glosry.md).

- In certain circumstances, [`CAST` expressions](abensql_cast.md) can be used in the `SELECT` list of the subquery for combinations between columns that are forbidden by the rules above.

- A [`SELECT` list](abapselect_list.md) of the subquery specified using `*` ignores all client columns, which means that client-dependent [CDS entities](../../abap-glossary/abencds_entity_glosry.md) whose result sets do not have a client column can be accessed without any problems.

- Attempts to fill [key fields](../../abap-glossary/abenkey_field_glosry.md) with null values raise an exception which prevents duplicate entries from being made in the writable database object to be filled.

- Writable database objects accessed using this variant of the `INSERT` statement should not be expanded independently of each other to avoid syntax errors.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Insertion of all rows of a union set of the DDIC database tables `DEMO_JOIN1` and `DEMO_JOIN2` into the table `DEMO_JOIN3`. Only if logging is disabled for `DEMO_JOIN3`, a subquery can be used. Otherwise, the data must be inserted into an internal table using selection.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DELETE FROM demo_join1. 
INSERT demo_join1 
  FROM TABLE @( VALUE #( ( a = 'a1' b = 'b1' c = 'c1' d = 'd1' ) 
                         ( a = 'a2' b = 'b2' c = 'c2' d = 'd2' ) 
                         ( a = 'a3' b = 'b3' c = 'd3' d = 'd3' ) ) ). 
DELETE FROM demo_join2. 
INSERT demo_join2 
  FROM TABLE @( VALUE #( ( d = 'd1' e = 'e1' f = 'f1' g = 'g1' ) 
                         ( d = 'd2' e = 'e2' f = 'f2' g = 'g2' ) 
                         ( d = 'd3' e = 'e3' f = 'f3' g = 'g3' ) ) ). 
 
DELETE FROM demo_join3. 
IF cl_dbi_utilities=>is_logging_on( 'DEMO_JOIN3' ) IS INITIAL. 
  INSERT demo_join3 FROM ( SELECT a,b,c,d FROM demo_join1 
                             UNION 
                               SELECT d,e,f,g FROM demo_join2 ) 
                           ##logging_versus_from_select[demo_join3]. 
ELSE. 
  SELECT a,b,c,d FROM demo_join1 
    UNION 
      SELECT d AS a, e AS b, f AS c, g AS d FROM demo_join2 
      INTO TABLE @FINAL(buffer). 
  INSERT demo_join3 FROM TABLE @buffer. 
ENDIF. 
 
SELECT * 
       FROM demo_join3 
       INTO TABLE @FINAL(result). 
 
out->write( result ). 
 
out->display( ).
```

## Executable Examples

- [`INSERT, FROM SELECT`](abeninsert_from_select_abexa.md)

- [Union with Global Temporary Table](abenselect_union_sum_gtt_abexa.md)
