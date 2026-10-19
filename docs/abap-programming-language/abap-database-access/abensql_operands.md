---
title: "ABAP SQL - SQL Operands sql_elem"
source_file: abensql_operands.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - SQL Operands sql_elem

## Syntax

``` abap
... col 
  | literal | @dobj | @( expr ) ...  
```

[`col`](abenabap_sql_columns.md) · [`literal`](abenabap_sql_literals.md) · [`@dobj`](abenabap_sql_host_variables.md) · [`@( expr )`](abenabap_sql_host_expressions.md)

## Description

Specifies a column [`col`](abenabap_sql_columns.md), a literal [`literal`](abenabap_sql_literals.md), a host variable [`@dobj`](abenabap_sql_host_variables.md), or a host expression [`@( expr )`](abenabap_sql_host_expressions.md) as an elementary [SQL operand](../../abap-glossary/abensql_operand_glosry.md) in an ABAP SQL operand position.

These elementary operands can have the following properties:

- They can be specified as [elementary SQL expressions](abensql_elem.md) in all operand positions in which [SQL expressions](abapsql_expr.md) are possible.

- They can also occur in specific operand positions in which no SQL expressions or restricted SQL expressions are possible.

To operand positions in which host variables are handled as SQL expressions, the associated rules for the expressions apply. The rules of the respective position apply in operand positions in which no SQL expressions are possible.

While the value of a column `col` or a [typed literal](abenabap_sql_typed_literals.md) is determined on the database, the values of [untyped literals](abenabap_sql_untyped_literals.md), host variables, and host expressions are passed from ABAP to the database system before the SQL statement is executed or copied from the database system after it is executed. The operand position determines how the value of such an ABAP object is handled:

- An ABAP object specified as an [elementary SQL expression](abensql_elem.md) in a read position is mapped to a dictionary type as described there, passed to the database with this type, and handled accordingly. The database rules apply.

- In operand positions in which an ABAP object is not handled as an SQL expression, a conversion between the respective types takes place according to [ABAP conversion rules](../abap-processing-internal-data/abenconversion_rules.md) if necessary. The mapping of [ABAP Dictionary types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) to [ABAP types](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) is respected if necessary. If an [untyped literal](abenabap_sql_untyped_literals.md), a [host variable](abenabap_sql_host_variables.md), or a [host expression](abenabap_sql_host_expressions.md) is read, conversions are subject to the [rules for lossless assignments](../abap-processing-internal-data/abapmove_exact.md). If the assignment cannot be lossless, an exception is raised. Literals and [host constants](../../abap-glossary/abenhost_constant_glosry.md) produce syntax warnings or syntax errors.

## Hint

[Typed literals](abenabap_sql_typed_literals.md) are always handled as elementary SQL expressions, while [untyped literals](abenabap_sql_untyped_literals.md) can also be handled as host variables, depending on the operand position.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

SQL expressions are possible on the left and right side of the [`WHERE`](abapwhere.md) condition. The specified column `carrid` can be placed in parentheses as an elementary SQL expression. General SQL expressions are also possible on the right side of the condition. The literal `CHAR`UA\`\` as an elementary SQL expression can be used and also be set in parentheses.

``` abap
SELECT * 
       FROM scarr 
       WHERE ( carrid ) =  CHAR`UA` 
       INTO TABLE @FINAL(itab).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the first `SELECT` statement, the host variable `@field` is in an [operand position](abenwhere_logexp_operand_in.md) in which it is not handled as an elementary SQL expression. Their content must comply with the [rules for lossless assignments](../abap-processing-internal-data/abapmove_exact.md), which is not the case here. This is why an exception of the class `CX_SY_OPEN_SQL_DATA_ERROR` is raised. In the second `SELECT` statement, the same host variable is in an [operand position](abenwhere_logexp_list_in.md) in which it is evaluated as an elementary SQL expression and a [mapping](abensql_elem.md) takes place to a dictionary type and the value is evaluated using this type on the database. No exception is raised in this case.

``` abap
DATA field TYPE c LENGTH 100 VALUE 'XXXXXXXXXXXXXXX'. 
 
TRY. 
    SELECT * 
           FROM scarr 
           WHERE carrid IN ( @field ) 
           INTO TABLE @FINAL(rtab1). 
  CATCH cx_sy_open_sql_data_error. 
    cl_demo_output=>write( 'Data loss in conversion' ). 
ENDTRY. 
 
TRY. 
    SELECT * 
           FROM scarr 
           WHERE ( carrid, carrname ) IN ( ( @field, CHAR` ` ) ) 
           INTO TABLE @FINAL(rtab2). 
  CATCH cx_sy_open_sql_error. 
    cl_demo_output=>write( 'Error in mapping' ). 
ENDTRY. 
 
cl_demo_output=>display( ).
```
