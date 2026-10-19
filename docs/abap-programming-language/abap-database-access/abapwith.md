---
title: "WITH"
source_file: abapwith.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# WITH

## Syntax Forms

**Static Form**

``` abap
WITH 
  +cte1[( name1, name2, ... )] AS ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] ), 
    [hierarchy] 
    [associations][, 
  +cte2[( name1, name2, ... )] AS ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] ), 
    [hierarchy] 
    [associations], 
  ... ] 
  SELECT mainquery_clauses 
         [UNION|INTERSECT|EXCEPT ...] 
         INTO|APPENDING target 
         [UP TO ...] [OFFSET ...] 
         [OPTIONS ...]. 
  ... 
[ENDWITH].
```

**Dynamic Form**

``` abap
WITH 
  (select_syntax) 
         INTO|APPENDING target 
         [UP TO ...] [OFFSET ...] 
         [OPTIONS ...]. 
  ... 
[ENDWITH].
```

[`subquery_clauses`](abapwith_subquery.md) · [`UNION|INTERSECT|EXCEPT ...`](abapunion.md) · [`hierarchy`](abapwith_hierarchy.md) · [`associations`](abapwith_associations.md) · [`subquery_clauses`](abapwith_subquery.md) · [`UNION|INTERSECT|EXCEPT ...`](abapunion.md) · [`hierarchy`](abapwith_hierarchy.md) · [`associations`](abapwith_associations.md) · [`mainquery_clauses`](abapwith_mainquery.md) · [`UNION|INTERSECT|EXCEPT ...`](abapunion.md) · [`INTO|APPENDING`](abapinto_clause.md) · [`UP TO ...] [OFFSET ...]`](abapselect_up_to_offset.html) · [`OPTIONS ...`](abapselect_options.md) · [`INTO|APPENDING`](abapinto_clause.md) · [`UP TO ...] [OFFSET ...]`](abapselect_up_to_offset.html) · [`OPTIONS ...`](abapselect_options.md)

### Variant

[Static Form](abapwith.md#variant-1)

[Dynamic Form](abapwith.md#variant-2)

## Overview

### Description

The [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) keyword `WITH` introduces `SELECT` statements with query clauses that produce a result set that is handled by an [`INTO`](abapinto_clause.md) clause and optionally by [`UP TO`](abapselect_up_to_offset.md) and [`OPTIONS`](abapselect_options.md) additions. There are a static and a dynamic form:

- The static form contains the static specification of [common table expressions](../../abap-glossary/abencommon_table_expression_glosry.md) (CTE for short) to be used in a final [main query](../../abap-glossary/abenmainquery_glosry.md). There must be at least one definition of a CTE.

- The dynamic form contains one dynamic token `select_syntax` in parenthesis that can contain the definitions of the CTEs and the main query at runtime. In contrast to the static form, it may contain the main query only. It must not contain the definition of CTEs.

### Hints

- The static form can be partly dynamic because its subquery clauses and the main query clause can itself contain dynamic tokens.

- The dynamic form offers the possibility to express a main query with or without CTEs completely dynamically.

## Variant 1

**Static Form**

``` abap
WITH 
  +cte1[( name1, name2, ... )] AS ( SELECT `subquery_clauses` [`UNION|INTERSECT|EXCEPT ...`] ), 
    [`hierarchy`] 
    [`associations`][, 
  +cte2[( name1, name2, ... )] AS ( SELECT `subquery_clauses` [`UNION|INTERSECT|EXCEPT ...`] ), 
    [`hierarchy`] 
    [`associations`], 
  ... ] 
  SELECT `mainquery_clauses` 
         [`UNION|INTERSECT|EXCEPT ...`] 
         `INTO|APPENDING` target 
         [`UP TO ...] [OFFSET ...]` 
         [`OPTIONS ...`]. 
  ... 
[ENDWITH].
```

### Addition

[`... ( name1, name2, ... )`](abapwith.md#addition)

### Description

The static form of the statement `WITH` introduces the definition of at least one common table expression (CTE) and one main query. The static form of `WITH` can be used as a standalone statement, as shown here, or after the statement `OPEN CURSOR`.

Each common table expression creates a tabular result set in a [subquery](../../abap-glossary/abensubquery_glosry.md), which can be used in the subsequent queries of the `WITH` statement as data source [`data_source`](abapselect_data_source.md). The `WITH` statement consists of the following parts:

- A comma-separated list with at least one definition of a common table expression

  - Each common table expression has a unique name `+cte1`, `+cte2`, ... . The names `cte` can have a maximum of 30 characters, and can contain letters, numbers, and underscores. They must start with either a letter or an underscore. In addition, the name must be prefixed with the character `+`. The initial `+` character is part of the name, but cannot stand alone and must not be followed by a number.

  - An optional name list (`( name1, name2, ... )`) for the columns of the result set of the common table expression can be specified directly after the name (see below).

  - A parenthesized subquery `SELECT` [`subquery_clauses`](abapwith_subquery.md) follows the `AS`. This subquery creates the tabular result set of the common table expression. The [set operators](../../abap-glossary/abencds_set_operators_glosry.md) [`UNION`](abapunion.md), [`INTERSECT`](abapunion.md), and [`EXCEPT`](abapunion.md) can be used to combine the result sets of multiple subqueries. In this case, special rules [`query_clauses`](abapunion_clause.md) apply when specifying clauses.

- A closing main query `SELECT` [`mainquery_clauses`](abapwith_mainquery.md), which can contain the same [clauses and additions](abenselect_clauses.md), apart from [`FOR ALL ENTRIES`](abenwhere_all_entries.md), as a standalone [`SELECT`](abapselect.md) statement, and works in the same way:

  - The result set of the main query is assigned to ABAP data objects according to the [`INTO`](abapinto_clause.md) clause.

  - As described in [`SELECT`](abapselect.md), a single- or multirow result set is created and, depending on the target area specified in the [`INTO`](abapinto_clause.md) clause, a `SELECT` loop is either opened or not.

  - A `SELECT` loop must be closed with the [`ENDWITH`](abapendwith.md) statement. `ENDWITH` has exactly the same meaning for `WITH ... SELECT` as [`ENDSELECT`](abapendselect.md) for a standalone [`SELECT`](abapselect.md) loop.

  - In the main query, each of the previously defined common table expressions `+cte1`, `+cte2`, and so on, can be used as the data source [`data_source`](abapselect_data_source.md).

The [set operators](../../abap-glossary/abencds_set_operators_glosry.md) [`UNION`](abapunion.md), [`INTERSECT`](abapunion.md), and [`EXCEPT`](abapunion.md) can be used to combine the result sets of multiple main queries. In this case, additional rules [`query_clauses`](abapunion_clause.md) apply when specifying clauses.

A common table expression defined in the `WITH` statement can be used after its definition in the subquery of another common table expression and in the main query as the data source [`data_source`](abapselect_data_source.md). It cannot be used in its own subquery or in the subqueries of preceding definitions. A common table expression is only known within the current `WITH` statement.

Each common table expression defined in a `WITH` statement must be used at least once within the `WITH` statement, either in another common table expression or in the main query. This means that the main query must access at least one common table expression.

The name `+cte` of a common table expression is valid across the entire `WITH` statement. The character `+` is omitted from the name of the substructure only when a substructure is created as a data source for a common table expression in an inline declaration with [`@DATA(...)`](abapselect_into_target.md) in the [`INTO`](abapinto_clause.md) clause.

Generally, the result set of a common table expression has no [client column](../../abap-glossary/abenclient_column_glosry.md). Even if the client column of a client-dependent data source is included explicitly in the subquery to its `SELECT` list, it does not behave as such in the result set.. This behavior can be changed with the addition [`DECLARE CLIENT`](abapselect_declare_client.md). With that addition, any column of type `CHAR` with length 3 can be declared as a client column. Then, the result set of the CTE is handled as client-dependent, implicit client handling is applied.

The following additions can be used to expose hierarchies and associations for use in the current `WITH` statement:

- The addition [`hierarchy`](abapwith_hierarchy.md) can be used to expose the common table expression as a [CTE hierarchy](../../abap-glossary/abencte_hierarchy_glosry.md).

- The addition [`associations`](abapwith_associations.md) can be used to do the following:

  - [Expose](abapwith_associations_using.md) the [CDS associations](../../abap-glossary/abencds_association_glosry.md) of a common table expression when [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) or [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) are accessed.

  - [Define and expose](../../abap-glossary/abencte_association_glosry.md) dedicated [CTE associations](../../abap-glossary/abencte_association_glosry.md).

    The associations can be used in [path expressions](abenabap_sql_path.md) of the subsequent queries of the current `WITH` statement.

### Hints

- A common table expression creates a temporary tabular result set, which can be accessed during execution of the `WITH` statement. Common table expressions can therefore be considered temporary views, which only exist for the duration of the database access.

- Common table expressions can be used whenever intermediate results are required in a `SELECT` statement. ABAP SQL statements are more readable if common table expressions are used, and a common table expression is always useful if intermediate results are required more than once. If required, common table expressions can also perform the tasks of [GTTs](../../abap-glossary/abenglobal_temporary_table_glosry.md).

- Using common table expressions as a data source also provides the option of selecting directly from a subquery `SELECT FROM subquery`, which is not possible in ABAP SQL.

- The character `+` in front of the name of a common table expression marks it as such, just like the character `@` for host variables. Due to the character `+`, a common table expression cannot have the same name as a table from the ABAP Dictionary and hence cannot be hidden.

- For `WITH` loops that are closed with `ENDWITH`, the same notes apply as to [`SELECT`](abapselect.md) loops. In particular, `WITH` loops should not be nested.

- In the main query of the `WITH` statement, if `*` is specified in the `SELECT` list, this means that there is no unconverted transfer to a work area specified after [`INTO`](abapinto_clause.md).

- Only `WITH` statements that access only [internal tables](abapselect_itab.md) but no database tables can be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md). If a database table is accessed at any position of the statement, the ABAP SQL statement bypasses the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result set of the common table expression `+cities` is a list of all cities that are flown from or to by an airline. The common table expression is used in the main query as the data source of the subquery of the `WHERE` condition.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA carrid TYPE spfli-carrid VALUE 'LH'. 
cl_demo_input=>request( CHANGING field = carrid ). 
 
WITH 
  +cities AS ( 
    SELECT cityfrom AS city 
           FROM spfli 
           WHERE carrid = @carrid 
    UNION DISTINCT 
    SELECT cityto AS city 
           FROM spfli 
           WHERE carrid = @carrid ) 
  SELECT * 
         FROM sgeocity 
         WHERE city IN ( SELECT city 
                                FROM +cities ) 
         INTO TABLE @FINAL(result). 
 
out->write( result ). 
 
out->display( ).
```

## Executable Examples

- [`WITH`, Common Table Expressions](abenwith_cte_abexa.md)

- [`WITH`, Aggregation for Join Set](abenwith_agg_union_abexa.md)

## Addition

`... ( name1, name2, ... )`

### Description

Defines the column names of a common table expression `+cte`. The specified names `name1`, `name2`, ... are assigned to the columns defined in the [`SELECT` list](abapselect_list.md) of the [subquery](abapwith_subquery.md) of the common table expression in the order given. The names work like the alias names defined in the `SELECT` list using `AS` and overwrite these names.

- If a name list is specified, it must contain a name for each column of the common table expression.

- If no name list is specified, the columns of the results list have the names defined in the [`SELECT` list](abapselect_list.md) of the [subquery](abapwith_subquery.md).

The opening parenthesis must be directly after the name `+cte1`, `+cte2`, and so on. At least one blank must be placed after the opening parenthesis and in front of the closing parenthesis. There can be blanks in the comma-separated list of names.

The names can have a maximum of 30 characters, and can contain letters, numbers, and underscores. They must start with either a letter or an underscore.

### Hint

It is possible to specify a name list if all columns with `*` are selected in the [`SELECT` list](abapselect_list.md) of the [subquery](abapwith_subquery.md). This can lead to syntax errors if the data source of the subquery is subsequently extended.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result sets of both common table expressions `+connections` and `+sum_seats` are merged in the subquery of the common table expression `+result` in a join expression. An explicit name list assigns names to the resulting columns. These names are used in the main query to sort the results. For each flight connection of the selected airline, the total number of occupied seats is output from the DDIC database table `SFLIGHT`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA from_id TYPE spfli-carrid VALUE 'AA'. 
cl_demo_input=>add_field( CHANGING field = from_id ). 
DATA to_id TYPE spfli-carrid VALUE 'UA'. 
cl_demo_input=>request( CHANGING field = to_id ). 
from_id = to_upper( from_id ). 
to_id   = to_upper( to_id ). 
 
WITH 
  +connections AS ( 
    SELECT spfli~carrid, carrname, connid, cityfrom, cityto 
           FROM spfli 
           INNER JOIN scarr 
             ON scarr~carrid = spfli~carrid 
           WHERE spfli~carrid BETWEEN @from_id AND @to_id ), 
  +sum_seats AS ( 
    SELECT carrid, connid, SUM( seatsocc ) AS sum_seats 
           FROM sflight 
           WHERE carrid BETWEEN @from_id AND @to_id 
           GROUP BY carrid, connid ), 
  +result( name, connection, departure, arrival, occupied ) AS ( 
    SELECT carrname, c~connid, cityfrom, cityto, sum_seats 
           FROM +connections AS c 
             INNER JOIN +sum_seats AS s 
               ON c~carrid = s~carrid AND 
                  c~connid = s~connid ) 
  SELECT * 
         FROM +result 
         ORDER BY name, connection 
         INTO TABLE @FINAL(result). 
 
out->write( result ). 
 
out->display( ).
```

## Variant 2

**Dynamic Form**

``` abap
WITH 
  (select_syntax) 
         `INTO|APPENDING` target 
         [`UP TO ...] [OFFSET ...]` 
         [`OPTIONS ...`]. 
  ... 
[ENDWITH].
```

### Description

In the dynamic form of the statement `WITH`, a data object `select_syntax` is specified in parentheses. When the statement is executed, the data object can contain the complete syntax that is possible at the respective position for the static form between `WITH` and the `INTO` clause. The dynamic form of `WITH` cannot be used after the statement `OPEN CURSOR`.

The data object `select_syntax` can be a character-like data object or a standard table with a character-like row type. The syntax in `select_syntax` is not case-sensitive. When an internal table is specified, the syntax can be distributed across multiple rows. The subquery clauses and the main query clause specified in `select_syntax` must not contain further dynamic tokens. Invalid syntax raises a catchable exception of class `CX_SY_DYNAMIC_OSQL_ERROR`.

In contrast to the static form, the syntax in `select_syntax` must not contain the definition of CTEs. It may contain the main query only.

### Security Hint

If used incorrectly, dynamic programming techniques can present a serious security risk. Any dynamic content that is passed to a program from the outside must be checked thoroughly or escaped before it is used in dynamic statements. This can be done using the system class `CL_ABAP_DYN_PRG` or the built-in function [`escape`](../abap-processing-internal-data/abenescape_functions.md).

### Hints

- If `select_syntax` contains a main query but no CTEs, it presents a fully dynamic `SELECT` statement.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Dynamic `SELECT` statement without CTEs in a text string. The example indicates that the SQL statement can be seen as a template that can be modified dynamically.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA result TYPE TABLE OF string WITH EMPTY KEY. 
 
DATA(select_source) = 
  `SELECT carrid && ' ' && carrname AS carrier` & 
  `  FROM scarr`  & 
  `  WHERE carrid BETWEEN 'LH' AND 'UA'` & 
  `  ORDER BY carrid`. 
 
* Modify SQL statement 
... 
 
TRY. 
    WITH 
     (select_source) 
       INTO TABLE @result. 
  CATCH cx_sy_dynamic_osql_error INTO FINAL(exc). 
    out->write( exc->get_text( ) ). 
    RETURN. 
ENDTRY. 
 
out->write( result ). 
 
out->display( ).
```

## Executable Examples

- [`WITH`, Dynamic Form](abenwith_dynamic_abexa.md)

- [`SELECT`, Dynamic Query Clauses](abendynamic_select_abexa.md)
