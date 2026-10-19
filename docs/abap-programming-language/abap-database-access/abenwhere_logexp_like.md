---
title: "sql_cond - LIKE"
source_file: abenwhere_logexp_like.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Conditions sql_cond > sql_cond - rel_exp for Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_cond - LIKE

## Syntax

``` abap
... operand1 [NOT] LIKE operand2 [ESCAPE esc] ...  
```

### Addition

[`... ESCAPE esc`](abenwhere_logexp_like.md#addition)

## Overview

### Description

This relational expression is true if the value of the operand `operand1` matches (does not match) the pattern in the operand `operand2`.

- The following applies to `operand1`:

  - [SQL expressions](abapsql_expr.md) except for [aggregate expressions](abapselect_aggregate.md) and [window expressions](abapselect_over.md) can be specified.

  - The data type can be one of the character-like [dictionary types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) `CHAR`, `NUMC`, `CLNT`, `LANG`, `DATS`, `TIMS`, `ACCP`, `CUKY`, `UNIT`, or `SSTRING`.

  - In a [`HAVING`](abaphaving_clause.md) clause, [aggregate expressions](../../abap-glossary/abenaggregate_expression_glosry.md) can also be used.

- The following applies to `operand2`:

  - [Literals](abenabap_sql_literals.md) and [host variables](abenabap_sql_host_variables.md) can be specified.

  - The data type must be [`c`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md) or [`string`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md).

  - Any trailing blanks are ignored by the pattern, even in the data type `string`.

  - The content can have a maximum of three times as many characters as the length of `operand1` but no more than 1333 characters. [Character literals](../../abap-glossary/abencharacter_literal_glosry.md) and [constants](../../abap-glossary/abenconstant_glosry.md) respect any trailing blanks and a syntax error occurs if this rule is broken. All other data objects ignore trailing blanks and a runtime error occurs if this rule is broken.

  - The content of untyped literals and host variables must match the data type of `operand1` in accordance with the rules for [lossless assignments](../../abap-glossary/abenlossless_assignment_glosry.md).

A pattern in `operand2` is defined using the following wildcard characters:

- *%* is any character string, including an empty string.

- *\_* stands for any character.

The pattern is case-sensitive. If the pattern in `operand2` consists of exactly one *%* character, the evaluation of the condition in the database interface is optimized so that the condition is not passed to the database and `operand1 LIKE '%'` is always true regardless of the content of `operand1` and `operand1 NOT LIKE '%'` is always false instead.

### Hints

- The wildcard characters *\_* and *%* are used as in standard SQL. Elsewhere in ABAP, the wildcard characters *+* and *\** are used in similar relational expressions, in particular when [ranges table](../../abap-glossary/abenranges_table_glosry.md) are used.

- It is not usually beneficial to define patterns in `operand2` without wildcard characters. Instead, it is best to perform a comparison using [`=`](abenwhere_logexp_compare.md).

- Patterns that are closed by wildcard characters should not be used to search for trailing blanks. The semantics of searches of this type depend on the database system that is used and in general do not produce the required result.

- Due to ABAP SQL-specific optimization, `operand1 LIKE '%'` is also true if the operand `operand1` contains [null values](../../abap-glossary/abennull_value_glosry.md).

- No columns [`col`](abenabap_sql_columns.md) and no [host expressions](abenabap_sql_host_expressions.md) can be specified here on the right side.

- The fact that trailing blanks in `operand2` are also ignored for the data type `string` is different to all other operand positions in ABAP.

- The special character-like types [`n`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md), [`d`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md), and [`t`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md) cannot be used on the right side, since the wildcard characters *\_* and *%* required for patterns are invalid content for these types.

- The maximum number of characters on the right side is three times the maximum in `operand1` because, in theory, each character can be prefixed with an escape character defined using `ESCAPE`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Full text search in a table with text columns.

``` abap
DATA srch_str TYPE string. 
cl_demo_input=>request( CHANGING field = srch_str ). 
 
IF srch_str IS INITIAL. 
  RETURN. 
ENDIF. 
 
srch_str = '%' && srch_str && '%'. 
 
SELECT * 
       FROM doktl 
       WHERE id      = 'SD'      AND 
             object  LIKE 'AB%'  AND 
             langu   = @sy-langu AND 
             typ     = 'E'       AND 
             doktext LIKE @srch_str 
       INTO TABLE @FINAL(text_tab) 
       UP TO 100 ROWS. 
 
IF sy-subrc = 0. 
  cl_demo_output=>display( text_tab ). 
ENDIF.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Pattern comparison for a numeric column of the table `DEMO_EXPRESSIONS`. A [`CAST` expression](abensql_cast.md) is used here to create the required character-like data type.

``` abap
DELETE FROM demo_expressions. 
INSERT demo_expressions FROM TABLE @( 
  VALUE #( ( id = 'X' num1 = 111 ) 
           ( id = 'Y' num1 = 222 ) 
           ( id = 'Z' num1 = 333 ) ) ). 
 
SELECT FROM demo_expressions 
       FIELDS id, num1 
       WHERE CAST( num1 AS CHAR ) LIKE '2%' 
       INTO TABLE @FINAL(result). 
 
cl_demo_output=>display( result ).
```

## Addition

`... ESCAPE esc` .### Description

The addition `ESCAPE` can be used to define a single-character [escape character](../../abap-glossary/abenescape_character_glosry.md). `esc` expects a [flat](../../abap-glossary/abenflat_glosry.md) [character-like](../../abap-glossary/abencharlike_data_object_glosry.md) data object with the length 1 containing the escape character. A [literal](abenabap_sql_literals.md) or a [host variable](abenabap_sql_host_variables.md) can be specified. In the pattern in `operand2`, the escape character in `esc` may only be placed in front of a wildcard character or in front of the escape character itself. In this case, they lose their special meaning.

If an escape character in `operand2` is not placed in front of a valid character, an exception of the class `CX_SY_OPEN_SQL_DB` is raised.

### Hints

- The character *\#* is recommended for the escape character `esc`.

- If the pattern in `operand2` is created dynamically or comes from outside of the program, it must be ensured that no escape character contained in the pattern is placed in front of any character other than *\_*, *%*, or the escape character itself. To prevent the corresponding exception, escape characters that are part of the pattern must be escaped by themselves before being used.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

To search for the pattern '100%', the following expression can be used with `#` as the escape character.

... LIKE '100#%' ESCAPE '#' ...
