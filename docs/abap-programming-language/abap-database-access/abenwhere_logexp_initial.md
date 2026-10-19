---
title: "sql_cond - IS INITIAL"
source_file: abenwhere_logexp_initial.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Conditions sql_cond > sql_cond - rel_exp for Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_cond - IS INITIAL

## Syntax

``` abap
... operand IS [NOT] INITIAL ...  
```

## Description

This relational expression is true if the value of the operand `operand` is (is not) the [initial value](../../abap-glossary/abeninitial_value_glosry.md) of its [built-in dictionary type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

The following applies to `operand`:

- [SQL expressions](abapsql_expr.md) except for [aggregate expressions](abapselect_aggregate.md) and [window expressions](abapselect_over.md) can be specified.

- In a [`HAVING`](abaphaving_clause.md) clause, [aggregate expressions](../../abap-glossary/abenaggregate_expression_glosry.md) can also be used.

## Hints

- The expression `IS [NOT] INITIAL` is suitable for checking the type-dependent initial value, regardless of its actual data type, instead of comparing it with a type-compliant operand that contains the initial value. This is of particular use in [dynamic conditions](abenwhere_logexp_dynamic.md).

- The expression `IS [NOT] INITIAL` must not be confused with the expression [`IS [NOT] NULL`](abenwhere_logexp_null.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reads the rows of the DDIC database table `DEMO_DDIC_TYPES` in which a dynamically specified column contains its type-dependent initial value.

``` abap
DATA column TYPE string VALUE `INT8`. 
cl_demo_input=>request( CHANGING field = column ). 
column = to_upper( column ). 
 
FINAL(components) = CAST cl_abap_structdescr( 
  cl_abap_typedescr=>describe_by_name( 'DEMO_DDIC_TYPES' ) 
    )->components. 
 
IF NOT line_exists( components[ name = column ] ). 
  cl_demo_output=>display( `Invalid request` ). 
  RETURN. 
ENDIF. 
 
FINAL(cond) = column && ` IS INITIAL`. 
 
TRY. 
    SELECT * 
           FROM demo_ddic_types 
           WHERE (cond) 
           INTO TABLE @FINAL(result). 
  CATCH cx_sy_dynamic_osql_semantics INTO FINAL(xref). 
    cl_demo_output=>display( xref->get_text( ) ). 
ENDTRY.
```
