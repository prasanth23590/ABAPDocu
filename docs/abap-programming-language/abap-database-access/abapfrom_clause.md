---
title: "SELECT, FROM"
source_file: abapfrom_clause.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, FROM

## Syntax

``` abap
... FROM { {data_source [AS tabalias]}   
         | join   
         | {(source_syntax) [AS tabalias]} }   
 ...  
```

[`data_source`](abapselect_data_source.md) · [`join`](abapselect_join.md)

### Alternative

[1. `... data_source`](abapfrom_clause.md#alternative-1)

[2. `... join`](abapfrom_clause.md#alternative-2)

[3. `... (source_syntax)`](abapfrom_clause.md#alternative-3)

### Addition

[`... AS tabalias`](abapfrom_clause.md#addition)

## Overview

### Description

The specifications after `FROM` determine whether a [query](../../abap-glossary/abenasql_query_glosry.md) accesses a [DDIC database table](../../abap-glossary/abenddic_db_table_glosry.md), [CDS entity](../../abap-glossary/abencds_entity_glosry.md), an [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md), or an [internal table](abapselect_itab.md) as a data source [`data_source`](abapselect_data_source.md), or whether multiple data sources are accessed in a [join expression](abapselect_join.md). The optional addition `AS` defines an alias name for the data source.

## Alternative 1

`... data_source`

### Description

Specification of a single data source [`data_source`](abapselect_data_source.md).

### Hint

If a data source is specified multiple times after `FROM` in a join expression, an alias name `tabalias` must be defined after `AS` to avoid ambiguities.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specification of the DDIC database table `SCARR` as the only data source of a [`SELECT`](abapselect.md) statement.

``` abap
SELECT FROM scarr 
       FIELDS * 
       INTO TABLE @FINAL(result).
```

## Alternative 2

`... join`

### Description

Specifies a [join expression](abapselect_join.md) that joins multiple data sources with one another.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specification of the DDIC database tables `SCARR` and `SPFLI` in a join expression.

``` abap
SELECT FROM scarr 
         INNER JOIN spfli 
           ON scarr~carrid = spfli~carrid 
       FIELDS scarr~carrname, 
              spfli~connid, 
              spfli~cityfrom, 
              spfli~cityto 
       INTO TABLE @FINAL(result).
```

## Alternative 3

`... (source_syntax)`

### Description

Instead of static specifications, a data object `source_syntax` can be specified in parentheses. When the statement is executed, the data object must contain the syntax shown in the static specification. The data object `source_syntax` can be a character-like data object or a [standard table](../../abap-glossary/abenstandard_table_glosry.md) with a character-like row type. The syntax in `source_syntax` is not case-sensitive. When an internal table is specified, the syntax can be distributed across multiple rows. Invalid syntax raises a catchable exception of class `CX_SY_DYNAMIC_OSQL_ERROR`.

The addition `AS` used to specify an alias name statically can be specified only if `source_syntax` contains only the name of a single data source. The addition has the same meaning for this data source as when specified statically. In `source_syntax`, static attributes or constants of a class cannot be accessed from outside if the class has a static constructor that has not yet been executed.

### Security Hint

If used incorrectly, dynamic programming techniques can present a serious security risk. Any dynamic content that is passed to a program from the outside must be checked thoroughly or escaped before it is used in dynamic statements. This can be done using the system class `CL_ABAP_DYN_PRG` or the built-in function [`escape`](../abap-processing-internal-data/abenescape_functions.md).

### Hints

- If `source_syntax` is an internal table with a [header line](../../abap-glossary/abenheader_line_glosry.md), the header line and not the [table body](../../abap-glossary/abentable_body_glosry.md) is evaluated.

- The addition `AS` can be used as part of the dynamic syntax in `source_syntax` without restrictions.

- More specifically, if `AS` is specified statically outside the dynamic specification, `source_syntax` cannot contain any [path expressions](abenabap_sql_path.md).

- The class `CL_ABAP_DYN_PRG` contains methods that support the creation of correct and secure dynamic code.

- The literals of the dynamically specified ABAP SQL statements can span multiple rows of a token specified dynamically as an internal table.

- When specified dynamically, ABAP SQL statements can contain the comment characters [`*`](../abap-syntax-elements-of-an-abap-program/abencomment.md) and [`"`](../abap-syntax-elements-of-an-abap-program/abencomment.md) as follows:

  - In a dynamic token specified as a character-like data object, all content is ignored from the first comment character `"`.

  - In a dynamic token specified as an internal table, all rows are ignored that start with the comment character `*`. In the row, all content is ignored from the first comment character `"`.

    Comment characters placed within literals are, however, part of the literal.

- The dynamic forms of the statements [`WITH`](abapwith.md) enable fully dynamic `SELECT` statements, where all clauses except the `INTO` clause and the ABAP-specific additions can be specified in one dynamic token.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Displays the flight connections (flight date, airline name, and flight number) for a departure city and a destination city. The `FROM` clause, including any inner [joins](abapselect_join.md) is dynamic. The column specified after `SELECT` is also dynamic. When specified dynamically, the input values are specified indirectly using the name of the respective data object and are not chained directly. Otherwise, a special security check would be required for this input.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: cityfr TYPE spfli-cityfrom VALUE 'FRANKFURT', 
      cityto TYPE spfli-cityto   VALUE 'NEW YORK'. 
 
cl_demo_input=>new( 
  )->add_field( CHANGING field = cityfr 
  )->add_field( CHANGING field = cityto )->request( ). 
 
DATA: 
  BEGIN OF wa, 
    fldate   TYPE sflight-fldate, 
    carrname TYPE scarr-carrname, 
    connid   TYPE spfli-connid, 
  END OF wa, 
  itab LIKE SORTED TABLE OF wa 
            WITH UNIQUE KEY fldate carrname connid. 
 
FINAL(column_syntax) = `c~carrname, p~connid, f~fldate`. 
 
FINAL(source_syntax) = `( ( scarr AS c ` 
  & ` INNER JOIN spfli AS p ON p~carrid  = c~carrid` 
  & ` AND p~cityfrom = @cityfr` 
  & ` AND p~cityto   = @cityto )` 
  & ` INNER JOIN sflight AS f ON f~carrid = p~carrid ` 
  & ` AND f~connid = p~connid )`. 
 
SELECT (column_syntax) 
       FROM (source_syntax) 
       INTO CORRESPONDING FIELDS OF TABLE @itab. 
 
out->write_data( itab ). 
 
out->display( ).
```

### Executable Example

[`SELECT`, Dynamically Specified Tokens](abendynamic_sql_abexa.md)

## Addition

`... AS tabalias`

### Description

An alias name `tabalias` can be assigned to the data source using the addition `AS`. This name is only valid during the `SELECT` statement and in all other positions where this specified data source is addressed. If addressed, the alias name must be used instead of the actual name.

The alias name `tabalias` must follow the [naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md) for internal program names and the name `table_line` cannot be used.

### Hints

- An alias name `tabalias` prevents the original name [`data_source`](abapselect_data_source.md) from being used, which in principle also applies to dynamic tokens.

- If an alias name is to be named exactly like an addition of the `SELECT` statement, it may be necessary to prefix it with the [escape character `!`](../abap-operands/abennames_escaping.md).

- A [path expression](abenabap_sql_path.md) in the [data source](abapselect_data_source.md) of the `FROM` clause should have an alias name defined with `AS`. This is checked in strict mode from ABAP release 7.67.

- Outside of the strict syntax check mode from ABAP release 7.77, an alias can also contain the minus character (`-`).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of alias names for two data sources of a join expression and their use in the `SELECT` list and in the `ORDER BY` clause.

``` abap
SELECT FROM scarr AS c 
         INNER JOIN spfli AS p 
           ON c~carrid = p~carrid 
       FIELDS   c~carrname, p~connid, p~cityfrom, p~cityto 
       ORDER BY c~carrname, p~connid, p~cityfrom, p~cityto 
       INTO TABLE @FINAL(result).
```
