---
title: "DELETE writable_obj, source"
source_file: abapdelete_source.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML > DELETE writable_obj"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DELETE writable_obj, source

## Syntax

``` abap
... {@wa|@( expr )[MAPPING FROM ENTITY  ]} 
  | {TABLE @itab|@( expr )[MAPPING FROM ENTITY  ]} ...   
```

[`MAPPING FROM ENTITY `](../../abap-rap-business-objects/abap-for-rap-business-objects/abapmapping_from_entity.md) · [`MAPPING FROM ENTITY `](../../abap-rap-business-objects/abap-for-rap-business-objects/abapmapping_from_entity.md)

### Alternative

[1. `... @wa|@( expr ) [MAPPING FROM ENTITY]`](abapdelete_source.md#alternative-1)

[2. `... TABLE @itab|@( expr ) [MAPPING FROM ENTITY]`](abapdelete_source.md#alternative-2)

## Overview

### Description

In the variant `DELETE target FROM` of the statement [`DELETE`](abapdelete_dbtab.md), a non-table-like data object can be specified after `FROM`, or an internal table after `TABLE` can be specified as a [host variable](abenabap_sql_host_variables.md) or [host expression](abenabap_sql_host_expressions.md). The content of the data objects determines which rows are deleted. Like every [host variable](abenabap_sql_host_variables.md), the name of the work area or internal table must be prefixed by the escape character `@`.

## Alternative 1

`... @wa|@( expr ) [MAPPING FROM ENTITY]`

### Description

If a non-table-like work area is specified as a host variable [`@wa`](abenabap_sql_host_variables.md) or host expression [`@( expr )`](abenabap_sql_host_expressions.md), a row is searched in the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) whose [primary key](../../abap-glossary/abenprimary_key_glosry.md) content is the same as that of the corresponding initial part of the work area. The content of the work area is not converted and is interpreted according to the structure of the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md). This row is deleted. The work area must meet the [prerequisites](abenabap_sql_wa.md) for use in ABAP SQL statements.

If there is no row in the database with the same content as the primary key, no row is deleted and `sy-subrc` is set to 4.

[Implicit ABAP SQL client handling](abenabap_sql_client_handling.md) applies, in which a [client ID](../../abap-glossary/abenclient_identifier_glosry.md) specified in `wa` is ignored. The [current client](../../abap-glossary/abencurrent_client_glosry.md) is used by default.

The `MAPPING FROM ENTITY` addition is used to handle structures and internal tables that are typed with [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md). Find more information in the topic [ABAP SQL Statements with `MAPPING FROM ENTITY`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapmapping_from_entity.md).

### Hints

- The work area `wa` should be declared with reference to the DDIC database table or DDIC view in ABAP Dictionary using the length of the primary key.

- If a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) is specified as a [host expression](abenabap_sql_host_expressions.md) for the work area `wa`, for which the data type is inferred using the `#` character, a structure consisting of the components of the primary key of the DDIC database table is created as the type.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Deletion of a carrier from the DDIC database table `SCARR` using a host expression.

``` abap
DELETE scarr FROM @( VALUE #( carrid   = 'FF' ) ).
```

## Alternative 2

`... TABLE @itab|@( expr ) [MAPPING FROM ENTITY]`

### Description

If an internal table is specified as a host variable [`@itab`](abenabap_sql_host_variables.md) or host expression [`@( expr )`](abenabap_sql_host_expressions.md), the system processes all rows of the internal table in accordance with the rules for the work area `wa`. The row type of the internal table must meet the [prerequisites](abenabap_sql_wa.md) for use in ABAP SQL statements.

If there is no row in the database with the same content as the primary key for a row of the internal table, the corresponding row is ignored and `sy-subrc` is set to 4. If the internal table is empty, no rows are deleted. However, `sy-subrc` is still set to 0. The system field `sy-dbcnt` is set to the number of rows that are actually deleted.

The `MAPPING FROM ENTITY` addition is used to handle structures and internal tables that are typed with [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md). Find more information in the topic [ABAP SQL Statements with `MAPPING FROM ENTITY`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapmapping_from_entity.md).

### Hints

- When an internal table is used, package-by-package processing causes some of the rows being deleted to still be visible to any read access running in parallel with `DELETE`.

- If an internal table `itab` is specified using a [host expression](abenabap_sql_host_expressions.md) that is a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) for which the data type is inferred using the `#` character, a structured standard table with an empty table key whose row type consists of the components of the primary key of the DDIC database table is created as the type.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Deletion of all today's flights of an airline in which no seats are occupied from the DDIC database table `SFLIGHT`. The internal table from which the key values of the deleted rows are taken is obtained in a host expression using a method call. The client field must occur in the row structure of the internal table with the type `sflight_key_tab` to ensure that its components match the primary key of the DDIC database table. This example works in the same way as [`DELETE writable_obj`, `cond`](abapdelete_where.md), but it requires the database to be accessed twice.

``` abap
TYPES: 
  BEGIN OF sflight_key, 
    mandt  TYPE sflight-mandt, 
    carrid TYPE sflight-carrid, 
    connid TYPE sflight-connid, 
    fldate TYPE sflight-fldate, 
  END OF sflight_key, 
  sflight_key_tab TYPE STANDARD TABLE OF sflight_key WITH EMPTY KEY. 
 
CLASS sflight_methods DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS 
      get_empty_flights IMPORTING carrid   TYPE sflight-carrid 
                                  date     TYPE d 
                        RETURNING VALUE(r) TYPE sflight_key_tab. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS sflight_methods IMPLEMENTATION. 
  METHOD get_empty_flights. 
    SELECT mandt, carrid, connid, fldate 
           FROM sflight 
           WHERE carrid = @carrid AND 
                 fldate = @date AND 
                 NOT seatsocc > 0 
           INTO TABLE @r. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
 
    DATA carrid TYPE sflight-carrid. 
    cl_demo_input=>request( CHANGING field = carrid ). 
    FINAL(date) = cl_demo_date_time=>get_user_date( ). 
    DELETE sflight FROM TABLE @( 
      sflight_methods=>get_empty_flights( carrid = carrid 
                                          date   = date ) ). 
  ENDMETHOD. 
ENDCLASS.
```
