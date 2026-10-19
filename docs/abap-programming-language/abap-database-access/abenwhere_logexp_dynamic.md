---
title: "sql_cond - (cond_syntax)"
source_file: abenwhere_logexp_dynamic.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Conditions sql_cond > sql_cond - rel_exp for Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_cond - (cond_syntax)

## Syntax

``` abap
... (cond_syntax) ...  
```

## Description

A relational expression can be specified dynamically as a parenthesized data object `cond_syntax` that contains the syntax of a logical expression [`sql_cond`](abenasql_cond.md) valid here or is initial when the statement is executed. The result of the relational expression `(cond_syntax)` is determined by the result of the contained logical expression. If `cond_syntax` is initial when the statement is executed, the relational expression is true.

The data object `cond_syntax` can be a character-like data object or a [standard table](../../abap-glossary/abenstandard_table_glosry.md) with a character-like line type. The syntax in `cond_syntax` is not case-sensitive as in the static syntax. When specifying an internal table, the syntax can be distributed across multiple rows. Invalid syntax raises a catchable exception from the class `CX_SY_DYNAMIC_OSQL_ERROR`.

The logical expression in `cond_syntax` can be joined using `AND` or `OR` or negated using `NOT` and a dynamic logical expression `(cond_syntax)` can be specified as a single relational expression of a composite logical expression. [Host expressions](../../abap-glossary/abenhost_expression_glosry.md) are not allowed in dynamic logical expressions.

If a dynamic SQL condition `(cond_syntax)` is used for a read, the content of `cond_syntax` is evaluated once for each [query](../../abap-glossary/abenasql_query_glosry.md). Any changes made to the content of `cond_syntax` in a `SELECT` loop or `WITH` loop are ignored by the relational expression.

## Security Hint

If used incorrectly, dynamic programming techniques can present a serious security risk. Any dynamic content that is passed to a program from the outside must be checked thoroughly or escaped before it is used in dynamic statements. This can be done using the system class `CL_ABAP_DYN_PRG` or the built-in function [`escape`](../abap-processing-internal-data/abenescape_functions.md).

## Hints

- It is also possible to evaluate an internal table specified after the addition [`FOR ALL ENTRIES`](abenwhere_all_entries.md) of a [main query](../../abap-glossary/abenmainquery_glosry.md) in a dynamic relational expression.

- It is possible to check a [ranges table](../../abap-glossary/abenranges_table_glosry.md) in a dynamic relational expression.

- If `cond_syntax` is an internal table with a [header line](../../abap-glossary/abenheader_line_glosry.md), the [table body](../../abap-glossary/abentable_body_glosry.md) is evaluated, and not the header line.

- Dynamic relational expressions can also be created interactively using dynamic selections.

- When a condition is specified dynamically, the syntax check can take place only at runtime. Therefore, specifying a relational expression at runtime requires more execution time than a corresponding specification specified in the program text.

- The data objects specified in a dynamic condition should be declared in the same context, if possible, since searches in higher contexts at runtime are more time-consuming.

- The class `CL_ABAP_DYN_PRG` contains methods that support the creation of correct and secure dynamic SQL conditions.

- The literals of the dynamically specified ABAP SQL statements can span multiple rows of a token specified dynamically as an internal table.

- When specified dynamically, ABAP SQL statements can contain the comment characters [`*`](../abap-syntax-elements-of-an-abap-program/abencomment.md) and [`"`](../abap-syntax-elements-of-an-abap-program/abencomment.md) as follows:

  - In a dynamic token specified as a character-like data object, all content is ignored from the first comment character `"`.

  - In a dynamic token specified as an internal table, all rows are ignored that start with the comment character `*`. In the row, all content is ignored from the first comment character `"`.

    Comment characters placed within literals are, however, part of the literal.

- In dynamic SQL conditions, static attributes or constants of a class cannot be accessed from outside in cases where the class has a static constructor and the constructor was not yet executed.

- When a [subquery](../../abap-glossary/abensubquery_glosry.md) is specified dynamically, the syntax check is performed in a strict mode, which handles the statement more strictly than the regular syntax check.

- If the conditions in `(cond_syntax)` are to be expressed statically, they should be embedded in [parentheses](abenwhere_logexp_andornot.md) in order to preserve the priority of processing.

- The dynamic forms of the statements [`WITH`](abapwith.md) enable fully dynamic `SELECT` statements, where all clauses except the `INTO` clause and the ABAP-specific additions can be specified in one dynamic token.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of a dynamic comparison from user input. In the case of incorrect syntax or incorrect semantics, exceptions are raised that are handled using the common superclass. Any SQL injections are prevented by checks on the specified column name. If this were not the case, a user could, for example, enter *CARRID \<\> value OR CARRID* in the field `column`, producing a condition *CARRID \<\> value OR CARRID = value*, which would be true regardless of the entry made in the field `value`.

``` abap
DATA: column TYPE c LENGTH 30, 
      value  TYPE c LENGTH 30. 
 
cl_demo_input=>new( 
  )->add_field( CHANGING field = column 
  )->add_field( CHANGING field = value )->request( ). 
 
TRY. 
    cl_abap_dyn_prg=>check_column_name( column ). 
  CATCH cx_abap_invalid_name. 
    cl_demo_output=>display( 'Invalid column name' ). 
    RETURN. 
ENDTRY. 
 
FINAL(cond_syntax) = column &&  ` = @value`. 
TRY. 
    SELECT * 
           FROM spfli 
           WHERE (cond_syntax) 
           INTO TABLE @FINAL(spfli_tab). 
  CATCH cx_sy_dynamic_osql_error cx_sy_open_sql_data_error. 
    cl_demo_output=>display( `Wrong WHERE condition!` ). 
    RETURN. 
ENDTRY. 
 
cl_demo_output=>display( spfli_tab ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following creation of a dynamic `WHERE` condition by concatenating the values of user input as shown below is even more risky than the previous example. Any SQL injections must be prevented by transforming quotation marks in the entry `value`. A user can, for example, enter *CARRID* in `column` and *LH' OR CARRID \<\> 'LH* in `value`, which would produce the always true condition *CARRID = 'LH' OR CARRID \<\> 'LH'* if the quotation marks were not transformed. After the conversion using the method `QUOTE` of the class `CL_ABAP_DYN_PRG`, which also adds quotation marks at the beginning and end, the condition *CARRID = 'LH'' OR CARRID \<\> ''LH'* is created. The handling of consecutive quotation marks in [text field literals](../abap-declarations/abenuntyped_character_literals.md) results in the column `CARRID` being compared exactly with the entered value, making the result of the condition always false.

``` abap
DATA: column TYPE c LENGTH 30, 
      value  TYPE c LENGTH 30. 
 
cl_demo_input=>new( 
  )->add_field( CHANGING field = column 
  )->add_field( CHANGING field = value )->request( ). 
 
TRY. 
    cl_abap_dyn_prg=>check_column_name( column ). 
  CATCH cx_abap_invalid_name. 
    cl_demo_output=>display( 'Invalid column name' ). 
    RETURN. 
ENDTRY. 
 
FINAL(cond_syntax) = column && ` = ` && cl_abap_dyn_prg=>quote( value ). 
 
TRY. 
    SELECT * 
           FROM spfli 
           WHERE (cond_syntax) 
           INTO TABLE @FINAL(spfli_tab). 
  CATCH cx_sy_dynamic_osql_error cx_sy_open_sql_data_error. 
    cl_demo_output=>display( `Wrong WHERE condition!` ). 
    RETURN. 
ENDTRY. 
 
cl_demo_output=>display( spfli_tab ).
```
