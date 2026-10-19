---
title: "UPDATE writable_obj, source"
source_file: abapupdate_source.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML > UPDATE writable_obj"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# UPDATE writable_obj, source

## Syntax

``` abap
... { {SET set_expression1, set_expression2, ... [WHERE sql_cond] [db_hints]}   
    | {FROM @wa|@( expr )[indicators] | [INDICATORS [NOT] SET STRUCTURE set_ind] [MAPPING FROM ENTITY  ]}   
    | {TABLE @itab [indicators] | [INDICATORS [NOT] SET STRUCTURE set_ind] [MAPPING FROM  ENTITY  ]}}  
```

[`set_expression1`](abapupdate_set_expression.md) · [`set_expression2`](abapupdate_set_expression.md) · [`sql_cond`](abenabap_sql_stmt_logexp.md) · [`db_hints`](abenabap_sql_db_hints.md) · [`indicators`](abapselect_indicators.md) · [`INDICATORS [NOT] SET STRUCTURE set_ind`](abapupdate_set_indicator.md) · [`MAPPING FROM ENTITY ]`](abapmapping_from_entity.html) · [`indicators`](abapselect_indicators.md) · [`INDICATORS [NOT] SET STRUCTURE set_ind`](abapupdate_set_indicator.md) · [`MAPPING FROM ENTITY ]`](abapmapping_from_entity.html)

### Alternative

[1. `... SET set_expression1, set_expression2, ... [WHERE sql_cond] [db_hints]`](abapupdate_source.md#alternative-1)

[2. `... FROM @wa|@( expr ) [indicators] | [INDICATORS [NOT] SET STRUCTURE set_ind] [MAPPING FROM ENTITY]`](abapupdate_source.html#alternative-2)

[3. `... TABLE @itab [indicators] | [INDICATORS [NOT] SET STRUCTURE set_ind] [MAPPING FROM ENTITY]`](abapupdate_source.html#alternative-3)

## Overview

### Description

The specifications in `source` define which rows and columns are changed. Either individual columns are changed using the addition `SET` or entire rows are overwritten using the addition `FROM`.

After `FROM` a non-table-like data object, or after `TABLE` an internal table, can be specified as a [host variable](abenabap_sql_host_variables.md) or [host expression](abenabap_sql_host_expressions.md). The content of these objects determines which rows are changed and which values are used to overwrite the rows.

After `FROM`, [set indicators](abapupdate_set_indicator.md) can be used to define individual fields within a row to be changed (instead of overwriting the entire content of a row).

## Alternative 1

`... SET set_expression1, set_expression2, ... [WHERE sql_cond] [db_hints]`

### Addition

[1. `... WHERE sql_cond`](abapupdate_source.md#addition-1)

[2. `... db_hints`](abapupdate_source.md#addition-2)

### Description

After the addition `SET`, the changes are specified in a list of set expressions: [`set_expression1`](abapupdate_set_expression.md), [`set_expression2`](abapupdate_set_expression.md), `...`

The content of primary key fields can be modified only if the affected [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) is not linked with a search help. If these changes would create a row which would produce duplicate entries in the primary key or a unique secondary index of the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md), no rows are changed and `sy-subrc` is set to 4.

If the value of a column with type `LRAW` or `LCHR` is modified, the associated `INT2` or `INT4` field must also be given a value.

### Executable Example

[`UPDATE`, Use of `SET`](abenupdate_set_abexa.md)

## Addition 1

`... WHERE sql_cond`

### Description

The addition `WHERE` determines in which rows of the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) the changes are made. Those rows are changed for which the logical expression [`sql_cond`](abenabap_sql_stmt_logexp.md) is true. The [relational expressions](abenabap_sql_stmt_logexp.md) of the logical expression [`sql_cond`](abenasql_cond.md) are subject to the restriction that no [subqueries](../../abap-glossary/abensubquery_glosry.md) can be evaluated on the modified [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md). If no `WHERE` condition is specified, all the rows in the target of the statement are modified by default. In a client-dependent target, these are the rows of the [current client](../../abap-glossary/abencurrent_client_glosry.md). The [client column](../../abap-glossary/abenclient_column_glosry.md) of a client-dependent target cannot be specified in the `WHERE` condition.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Sets multiple columns in a row determined using a `WHERE` condition.

``` abap
DELETE FROM demo_update. 
INSERT demo_update FROM @( VALUE #( id = 'X' ) ). 
 
UPDATE demo_update SET col1 = 100, 
                       col2 = 200, 
                       col3 = 300, 
                       col4 = 400 WHERE id = 'X'.
```

## Addition 2

`... db_hints`

### Description

In this variant, [database hints](../../abap-glossary/abendatabase_hint_glosry.md) can be specified using [`db_hints`](abenabap_sql_db_hints.md).

## Alternative 2

`... FROM @wa|@( expr ) [indicators] | [INDICATORS [NOT] SET STRUCTURE set_ind] [MAPPING FROM ENTITY]`

### Description

If a non-table-like work area is specified as a host variable [`@wa`](abenabap_sql_host_variables.md) or host expression [`@( expr )`](abenabap_sql_host_expressions.md), a row is searched in the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) whose primary key content is the same as that of the corresponding initial part of the work area. The work area must meet the [prerequisites](abenabap_sql_wa.md) for use in ABAP SQL statements.

- If a work area that does not contain any reference variables for [LOB handles](../../abap-glossary/abenlob_handle_glosry.md) is specified, the content of the work area is used unconverted and according to the structure of the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md). The content of the work area is assigned to the rows found. The assignment takes place without conversion, from left to right according to the structure of the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md).

- When a [LOB handle structure](../../abap-glossary/abenlob_handle_structure_glosry.md) is specified, it must be structured exactly like the structure of the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) in accordance with the [prerequisites](abenabap_sql_wa.md). Work area components that are not [LOB handle components](../../abap-glossary/abenlob_handle_structure_glosry.md) are assigned directly to the corresponding column of the row found. In the case of a LOB handle component of a reader stream type, the reader is created. If it is a type for a locator, the locator must exist and is used as a source. For details, see [LOB handles](abenium_lob.md).

- When set indicators are specified with the addition [`INDICATORS`](abapupdate_set_indicator.md) and the work area does not contain any reference variables for [LOB handles](../../abap-glossary/abenlob_handle_glosry.md), it must be compatible with the structure of the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md). In the case of a [LOB handle structure](../../abap-glossary/abenlob_handle_structure_glosry.md), the LOB handle components can be mapped to the data types `STRING` or `RAWSTRING` and are handled as described above.

If there is no row with the same content for the primary key in the database or if the change would produce a duplicate entry in a unique secondary index, the row is not changed and `sy-subrc` is set to 4.

[Implicit ABAP SQL client handling](abenabap_sql_client_handling.md) applies, in which a [client ID](../../abap-glossary/abenclient_identifier_glosry.md) specified in `wa` is ignored. The [current client](../../abap-glossary/abencurrent_client_glosry.md) is used by default.

The addition `INDICATORS` can be used to specify [null indicators](../../abap-glossary/abennull_indicator_glosry.md). It describes whether individual fields contain a [null value](abenabap_sql_null_values.md) or not.

The `MAPPING FROM ENTITY` addition is used to handle structures and internal tables that are typed with [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md). Find more information in the topic [ABAP SQL Statements with `MAPPING FROM ENTITY`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapmapping_from_entity.md).

### Hints

- The work area `wa` should always be declared with reference to the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md). For the derivation of [LOB handle structures](../../abap-glossary/abenlob_handle_structure_glosry.md), there are special [additions](../abap-declarations/abaptypes_lob_handle.md) of the statements `TYPES` and `[CLASS-]DATA`.

- Exceptions due to invalid values can also be raised in compatible work areas. For example, components of the types `d` and `t` can contain invalid dates and times that are not accepted by columns of the types `DATN` and `TIMN`.

- If a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) is specified as a [host expression](abenabap_sql_host_expressions.md) for the work area `wa`, for which the data type is inferred using the `#` character, a structure consisting of all the database table columns is created as the type.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Changing of the discount rate of the customer with customer number '00017777' (in the current client) to 3 percent.

``` abap
DATA wa TYPE scustom. 
 
SELECT SINGLE * 
       FROM scustom 
       WHERE id = '00017777' 
       INTO @wa. 
 
wa-discount = '003'. 
UPDATE scustom FROM @wa.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The same example as before but with an inline declaration and a host expression.

``` abap
SELECT SINGLE * 
       FROM scustom 
       WHERE id = '00017777' 
       INTO @FINAL(wa). 
 
UPDATE scustom FROM @( VALUE #( BASE wa discount = '003' ) ).
```

## Alternative 3

`... TABLE itab [indicators] | [INDICATORS [NOT] SET STRUCTURE set_ind] [MAPPING FROM ENTITY]`

### Description

If an internal table is specified as a host variable [`@itab`](abenabap_sql_host_variables.md) or host expression [`@( expr )`](abenabap_sql_host_expressions.md), the system processes all rows of the internal table in accordance with the rules for the work area `wa`, with the exception that when specifying an internal table, [locators](../../abap-glossary/abenlocator_glosry.md) are used as a source but [writer streams](../../abap-glossary/abenwriter_stream_glosry.md) cannot be created.

The row type of the internal table must meet the [prerequisites](abenabap_sql_wa.md) for use in ABAP SQL statements.

If there is no row with the same content of the [primary key](../../abap-glossary/abenprimary_key_glosry.md) for a row of the internal table in the database or if the change would produce a duplicate entry in a unique secondary index, the corresponding row is not changed and `sy-subrc` is set to 4. Processing then continues with the next row.

If the internal table is empty, no rows are changed. However, `sy-subrc` is still set to 0. The system field `sy-dbcnt` is set to the number of rows that are actually inserted.

The addition `INDICATORS` can be used to specify [null indicators](../../abap-glossary/abennull_indicator_glosry.md). It describes whether individual fields contain a [null value](abenabap_sql_null_values.md) or not.

The `MAPPING FROM ENTITY` addition is used to handle structures and internal tables that are typed with [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md). Find more information in the topic [ABAP SQL Statements with `MAPPING FROM ENTITY`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapmapping_from_entity.md).

### Hints

- If an internal table is used, package-by-package processing performs a read in parallel to an `UPDATE` on the same rows that partially shows the new status and partially shows the old status.

- The statement `UPDATE FROM TABLE` changes all rows for which this is possible. If `sy-subrc` contains the value 4 after the statement has been executed, this does not mean that no rows were changed. It simply means that not all of the rows in the internal table could be respected.

- If a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) as a [host expression](abenabap_sql_host_expressions.md) is specified as an internal table `itab`, for which the data type is inferred using the `#` character, a structured standard table whose row type consists of all the database table columns with an empty table key is created as the type.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reduction of the flight price for all of today's flights of an airline carrier in the DDIC database table `SFLIGHT` by the percentage `percent`. The new price is calculated in an internal table `sflight_tab` that is declared inline and the DDIC database table is changed by using the internal table as a source.

``` abap
DATA: carrid  TYPE sflight-carrid, 
      percent TYPE p LENGTH 1 DECIMALS 0. 
 
cl_demo_input=>new( 
  )->add_field( CHANGING field = carrid 
  )->add_field( CHANGING field = percent )->request( ). 
 
SELECT * 
       FROM sflight 
       WHERE carrid = @carrid AND 
             fldate = @( cl_demo_date_time=>get_user_date( ) ) 
       INTO TABLE @FINAL(sflight_tab). 
 
IF sy-subrc = 0. 
  LOOP AT sflight_tab ASSIGNING FIELD-SYMBOL(<sflight>). 
    <sflight>-price *= 1 - percent / 100. 
  ENDLOOP. 
ENDIF. 
 
UPDATE sflight FROM TABLE @sflight_tab.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The same example as above, but the new price is calculated in a host expression for the internal table.

``` abap
DATA: carrid  TYPE sflight-carrid, 
      percent TYPE p LENGTH 1 DECIMALS 0. 
 
cl_demo_input=>new( 
  )->add_field( CHANGING field = carrid 
  )->add_field( CHANGING field = percent )->request( ). 
 
SELECT * 
       FROM sflight 
       WHERE carrid = @carrid AND 
             fldate = @( cl_demo_date_time=>get_user_date( ) ) 
       INTO TABLE @FINAL(sflight_tab). 
 
IF sy-subrc = 0. 
  UPDATE sflight FROM TABLE @( VALUE #( 
    FOR <sflight> IN sflight_tab 
      ( VALUE #( 
          BASE <sflight> 
          price = <sflight>-price * ( 1 - percent / 100 ) ) ) ) ). 
ENDIF.
```
