---
title: "SQL Injections Using Dynamic Tokens in ABAP SQL"
source_file: abensql_inj_dyn_tokens_scrty.html
section: "ABAP Programming Language > ABAP Security Notes > Security Risks Caused by Input from Outside > SQL Injections"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SQL Injections Using Dynamic Tokens in ABAP SQL

The [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) syntax allows almost every clause of an ABAP SQL statement to be specified dynamically as the content of a data object specified in parentheses. If all or part of the content of one of these data objects originates from outside of the program, there is a risk of one of the following SQL injections:

- [Access to Non-Permitted Database Tables](abensql_inj_dyn_tokens_scrty.md#access-to-non-permitted-database-tables)

- [Access to Non-Permitted Table Columns](abensql_inj_dyn_tokens_scrty.md#access-to-non-permitted-table-columns)

- [Manipulation of the Dynamic WHERE Condition](abensql_inj_dyn_tokens_scrty.md#manipulation-of-the-dynamic-where-condition)

- [Fully Dynamic `SELECT` Statement](abensql_inj_dyn_tokens_scrty.md#fully-dynamic-select-statement)

- [Manipulation of a Dynamic Set Expression](abensql_inj_dyn_tokens_scrty.md#manipulation-of-a-dynamic-set-expression)

## Hint

In a dynamic token, it is more secure to specify the name of an ABAP data object as an operand, instead of entering a value as a literal.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first dynamic `WHERE` condition is insecure against an SQL injection, if `input` is an external input, which is not checked or escaped beforehand. This is not necessary for the second dynamic `WHERE` condition.

``` abap
DATA(sql_cond1) = `CARRID = '` && input && `'`. 
SELECT SINGLE * FROM scarr WHERE (sql_cond1) INTO @wa. 
 
DATA(sql_cond2) = `CARRID = @input`. 
SELECT SINGLE * FROM scarr WHERE (sql_cond2) INTO @wa.
```

## Access to Non-Permitted Database Tables

If dynamically specified database tables [`source_syntax`](../abap-database-access/abapfrom_clause.md) for the statement [`SELECT`](../abap-database-access/abapselect.md) or `target_syntax` for [writes](../abap-database-access/abenabap_sql_writing.md) originate in full or in part from outside the program, users could potentially access databases for which they usually do not have authorization. If the use of external input in dynamically specified database tables is unavoidable, the input must be properly checked. For example, the class `CL_ABAP_DYN_PRG` can be used to make a comparison with a include list.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following program section, the method `CHECK_TABLE_NAME_STR` only allows access to tables of the flight data model. Input from other or nonexistent database tables are rejected. Access to oversized database tables is also not allowed, to avoid putting too much strain on system performance.

``` abap
DATA dbtab TYPE string. 
cl_demo_input=>request( CHANGING field = dbtab ). 
 
TRY. 
    dbtab = 
      cl_abap_dyn_prg=>check_table_name_str( 
        val = to_upper( dbtab ) 
        packages = 'SAPBC_DATAMODEL' ). 
  CATCH cx_abap_not_a_table cx_abap_not_in_package. 
    cl_demo_output=>display( 'Wrong input' ). 
    RETURN. 
ENDTRY. 
 
DATA dref TYPE REF TO data. 
CREATE DATA dref TYPE STANDARD TABLE OF (dbtab) 
                 WITH EMPTY KEY. 
 
DATA lines TYPE i. 
SELECT COUNT(*) 
       FROM (dbtab) 
       INTO (@lines). 
IF lines > 1000. 
  cl_demo_output=>display( 'Table too large' ). 
  RETURN. 
ENDIF. 
 
SELECT * 
       FROM (dbtab) 
       INTO TABLE @dref->*. 
cl_demo_output=>display( dref->* ).
```

## Access to Non-Permitted Table Columns

If the dynamically specified table columns `column_syntax` in the [`SELECT` list](../abap-database-access/abapselect_list.md) of the statement [`SELECT`](../abap-database-access/abapselect.md) originate fully or in part from outside the program, users could potentially access table columns for which they usually do not have authorization. Users could also rename columns without permission or use aggregate functions to perform unauthorized calculations. If the use of external input in a dynamically specified table columns is unavoidable, the input must be properly checked. For example, the class `CL_ABAP_DYN_PRG` can be used to make a comparison with an include list.

### Hint

When specifying columns after [`GROUP BY`](../abap-database-access/abapgroupby_clause.md), the same security advice applies as to columns specified dynamically directly after `SELECT`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

See the example in [`column _syntax`](../abap-database-access/abapselect_list.md). Here only columns from an include list are allowed to be read.

## Manipulation of the Dynamic WHERE Condition

If a dynamic `WHERE` condition [`cond_syntax`](../abap-database-access/abenwhere_logexp_dynamic.md) originates completely or partially from outside the program, then users could potentially access data for which they usually do not have authorization. If the use of external input in a dynamic `WHERE` condition cannot be avoided, the input must be properly checked and usually escaped as well. To do this, you can sue the methods of class `CL_ABAP_DYN_PRG`.

### Hint

When dynamically specifying a [`HAVING`](../abap-database-access/abaphaving_clause.md) condition, the same security advice applies as for the dynamic `WHERE` condition.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following program section, a potential SQL injection is prevented by using the method `QUOTE` of the class `CL_ABAP_DYN_PRG`, which adds quotation marks at the beginning and end. If this method is not used, and if *x' OR name \<\> '* is entered, for example, all the data in the `SCUSTOM` table would be displayed.

``` abap
DATA name TYPE string. 
DATA customers TYPE TABLE OF scustom WITH EMPTY KEY. 
 
cl_demo_input=>request( CHANGING field = name ). 
 
FINAL(cond) = `country = 'DE' AND name = ` && 
             cl_abap_dyn_prg=>quote( CONV scustom-name( name ) ). 
 
TRY. 
    SELECT * FROM scustom 
             WHERE (cond) 
             INTO TABLE @customers. 
    cl_demo_output=>display( customers ). 
  CATCH cx_sy_dynamic_osql_syntax. 
    cl_demo_output=>display( 'Wrong input' ). 
ENDTRY.
```

More examples under [dynamic `WHERE` condition](../abap-database-access/abenwhere_logexp_dynamic.md).

## Fully Dynamic `SELECT` Statement

The dynamic forms of statements [`WITH`](../abap-database-access/abapwith.md) and `OPEN CURSOR` enable the specification of all of the above clauses within one dynamic token. If all of part of the dynamic token originates from outside of the program, there is a risk of an SQL injection.

To prevent SQL Injections, make sure that the `SELECT` statement within the dynamic token contains as few parts as possible that originate from outside of the program. If the statement does contain parts from outside the program, the content of these parts must be checked thoroughly using the `CL_ABAP_DYN_PRG` class as described for the individual dynamic tokens above.

## Manipulation of a Dynamic Set Expression

If a dynamic set expression [`expr_syntax`](../abap-database-access/abapupdate_set_expression.md) for the statement [`UPDATE`](../abap-database-access/abapupdate.md) originates completely or partially from outside the program, then users could potentially change data for which they usually do not have authorization. If the use of external input in a dynamic set expression cannot be avoided, the input must be properly checked and usually escaped as well. To do this, you can sue the methods of class `CL_ABAP_DYN_PRG`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following program section, a potential SQL injection is prevented by using the method `QUOTE` of the class `CL_ABAP_DYN_PRG`, which adds quotation marks at the beginning and end. If this method is not used, and if *...' discount = '90*, for example, is entered in one of the input fields, the discount for the relevant customer would be set to 90.

``` abap
DATA in TYPE REF TO if_demo_input. 
 
DATA customer TYPE scustom. 
 
DATA: id TYPE scustom-id, 
      name     TYPE string, 
      street   TYPE string, 
      city     TYPE string, 
      postcode TYPE string. 
 
id = '00000001'. 
SELECT SINGLE * 
       FROM scustom 
       WHERE id = @id 
       INTO @customer. 
 
name    = customer-name. 
street  = customer-street. 
city    = customer-city. 
postcode = customer-postcode. 
 
in = cl_demo_input=>new( ). 
in->add_field( CHANGING field = name 
 )->add_field( CHANGING field = street 
 )->add_field( CHANGING field = city 
 )->add_field( CHANGING field = postcode 
 )->request( ). 
 
FINAL(set_expr) = 
  COND string( WHEN name IS NOT INITIAL 
               THEN ` NAME = ` && 
               cl_abap_dyn_prg=>quote( name ) ) && 
  COND string( WHEN street IS NOT INITIAL 
               THEN ` STREET = `   && 
               cl_abap_dyn_prg=>quote( street ) ) && 
  COND string( WHEN city IS NOT INITIAL 
               THEN ` CITY = ` && 
               cl_abap_dyn_prg=>quote( city ) ) && 
  COND string( WHEN postcode IS NOT INITIAL 
               THEN ` POSTCODE = ` && 
               cl_abap_dyn_prg=>quote( postcode ) ). 
 
TRY. 
    UPDATE scustom SET (set_expr) WHERE id = @id. 
  CATCH cx_sy_dynamic_osql_syntax. 
    cl_demo_output=>display( 'Wrong input' ). 
ENDTRY.
```
