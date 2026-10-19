---
title: "ABAP SQL - Exceptions"
source_file: abenabap_sql_exceptions.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Exceptions

## Catchable Exceptions

`CX_SY_OPEN_SQL_DB`

- *Cause:* A general database error occurred.

  *Runtime error:* `DBIF_RSQL_SQL_ERROR`

- *Cause:* Error in module `RSQL` of the database interface.

  *Runtime error:* `DBIF_RSQL_INVALID_RSQL`

- *Cause:* No data found for the specified key.

  *Runtime error:* `DBIF_RSQL_KEY_NOT_FOUND`

- *Cause:* Unexpected end of data when accessing a table.

  *Runtime error:* `DBIF_RSQL_END_OF_DATA`

- *Cause:* The key for a table was not completely specified.

  *Runtime error:* `DBIF_RSQL_KEY_NOT_SPECIFIED`

- *Cause:* An invalid database cursor was used.

  *Runtime error:* `DBIF_RSQL_INVALID_CURSOR`

- *Cause:* An attempt was made to access a closed database cursor.

  *Runtime error:* `SAPSQL_SQLS_INVALID_CURSOR`

- *Cause:* The length of an ABAP target field does not match the size of the database field.

  *Runtime error:* `DBSQL_DBSL_LENGTH_ERROR`

`CX_SY_DYNAMIC_OSQL_ERROR`

- `CX_SY_DYNAMIC_OSQL_SEMANTICS`

  - *Cause:* The database column whose values are to be aggregated does not have a numeric type.

    *Runtime error:* `SAPSQL_HAVING_AVG_TYPE`

  - *Cause:* The database column whose values are to be aggregated does not have a numeric type.

    *Runtime error:* `SAPSQL_HAVING_SUM_TYPE`

  - *Cause:* Search pattern not specified in a character literal.

    *Runtime error:* `SAPSQL_LIKE_VAL_TYPE`

  - *Cause:* A token cannot be interpreted as a literal or in the current context of valid variable names.

    *Runtime error:* `SAPSQL_WHERE_ILLEGAL_VALUE` and `SAPSQL_SET_ILLEGAL_VALUE`

  - *Cause:* A table name is too long.

    *Runtime error:* `SAPSQL_TABNAME_TOO_LONG`

  - *Runtime error:* A field name is too long.

    *Runtime error:* `SAPSQL_FIELDNAME_TOO_LONG`

  - *Cause:* No table exists with the specified name.

    *Runtime error:* `SAPSQL_INVALID_TABLENAME`

  - *Cause:* A field name is ambiguous.

    *Runtime error:* `SAPSQL_AMBIGUOUS_FIELDNAME`

  - *Cause:* No column exists with the specified name.

    *Runtime error:* `SAPSQL_INVALID_FIELDNAME`

  - *Cause:* The specified table is not declared as a table or view in the ABAP Dictionary.

    *Runtime error:* `SAPSQL_NO_DBTAB_OR_VIEW`

  - *Cause:* An attempt was made to select the sum of a non-numeric field.

    *Runtime error:* `SAPSQL_FIELDLIST_SUM_TYPE`

  - *Cause:* An attempt was made to select the average of a non-numeric field.

    *Runtime error:* `SAPSQL_FIELDLIST_AVG_TYPE`

  - *Cause:* An attempt was made to create an aggregate function using a [LOB column](../../abap-glossary/abenlob_glosry.md).

    *Runtime error:* `SAPSQL_AGGREGATE_LOB`

  - *Cause:* An attempt was made to sort the values of a [LOB column](../../abap-glossary/abenlob_glosry.md).

    *Runtime error:* `SAPSQL_ORDER_BY_LOB`

  - *Cause:* An attempt was made to use the addition `DISTINCT` on a [LOB column](../../abap-glossary/abenlob_glosry.md).

    *Runtime error:* `SAPSQL_DISTINCT_AND_LOB`

  - *Cause:* An alias is too long.

    *Runtime error:* `SAPSQL_ALIASNAME_TOO_LONG`

  - *Cause:* An attempt was made to sort the values of a [LOB column](../../abap-glossary/abenlob_glosry.md).

    *Runtime error:* `SAPSQL_GROUP_BY_LOB`

  - *Cause:* An attempt was made to use a [LOB column](../../abap-glossary/abenlob_glosry.md) in a logical expression.

    *Runtime error:* `SAPSQL_BOUND_LONG_STRING`

  - *Cause:* A pattern specified in `LIKE` is too long.

    *Runtime error:* `SAPSQL_LIKE_PATTERN_TOO_LONG` and `SAPSQL_LIKE_PATTERN_TOO_LONG`

  - *Cause:* A field, whose value is to be changed with `+` or `-`, has a non-numeric type

    *Runtime error:* `SAPSQL_SET_PLUS_MINUS_TYPE`

- `CX_SY_DYNAMIC_OSQL_SYNTAX`

  - *Cause:* An error occurred while parsing a dynamic entry.

    *Runtime error:* `SAPSQL_PARSE_ERROR`

  - *Cause:* The keyword `AND` is missing after the lower comparison value of `BETWEEN`.

    *Runtime error:* `SAPSQL_BETWEEN_MISSING_AND`

  - *Cause:* The logical expression has incorrect parentheses.

    *Runtime error:* `SAPSQL_HAVING_PARENTHESES`

  - *Cause:* An unknown aggregate function was found.

    *Runtime error:* `SAPSQL_ILLEGAL_AGGREGATE`

  - *Cause:* The operator `IS NULL` is not followed by the keyword `NULL`.

    *Runtime error:* `SAPSQL_ILLEGAL_IS_NULL`

  - *Cause:* The operator `IN` has incorrect parentheses.

    *Runtime error:* `SAPSQL_IN_ILLEGAL_LIST`

  - *Cause:* The logical expression contains a text field literal that does not have a closing quotation mark.

    *Runtime error:* `SAPSQL_LIKE_QUOTES`

  - *Cause:* The logical expression ends unexpectedly.

    *Runtime error:* `SAPSQL_MISSING_LOG_CONDITION`

  - *Cause:* The Escape character is missing after the addition `ESCAPE`.

    *Runtime error:* `SAPSQL_WHERE_MISSING_ESCAPE`

  - *Cause:* An operator is missing in the logical expression.

    *Runtime error:* `SAPSQL_WHERE_MISSING_OPERATOR`

  - *Cause:* A literal or name of an ABAP variable is missing in the logical expression.

    *Runtime error:* `SAPSQL_WHERE_MISSING_VALUE`

  - *Cause:* The logical expression has incorrect parentheses.

    *Runtime error:* `SAPSQL_WHERE_PARENTHESES`

  - *Cause:* The logical expression contains a text field literal that does not have a closing quotation mark.

    *Runtime error:* `SAPSQL_WHERE_QUOTES`

  - *Cause:* An unknown operator is used in the logical expression.

    *Runtime error:* `SAPSQL_WHERE_UNKNOWN_OPERATOR`

  - *Cause:* An alias is missing.

    *Runtime error:* `SAPSQL_MISSING_ALIAS`

  - *Cause:* A column from the right side of a `LEFT OUTER JOIN` is used in a `WHERE` condition.

    *Runtime error:* `SAPSQL_ACCESS_TO_RHS_TABLE`

  - *Cause:* Syntax error when the addition [`CREATING`](abapselect_creating.md) was specified dynamically.

    *Runtime error:* `SAPSQL_NO_LOB_COLUMN`

    *Runtime error:* `SAPSQL_TWICE_DEFINITION`

    *Runtime error:* `SAPSQL_UNION_POSSIBLE`

    *Runtime error:* `SAPSQL_MISSING_FOR_COLUMNS`

    *Runtime error:* `SAPSQL_OTHER_ONLY_AT_THE_END`

The following exceptions can only occur when using the statement **[`UPDATE`](abapupdate.md)**:

- *Cause:* An attempt was made to change a database field using an operator other than `+` or `-`.

  *Runtime error:* `SAPSQL_SET_NOT_PLUS_MINUS`

- *Cause:* An unknown operator was used in the statement `SET`.

  *Runtime error:* `SAPSQL_SET_UNKNOWN_OPERATOR`

- *Cause:* A literal or name of an ABAP variable is missing in the statement `SET`.

  *Runtime error:* `SAPSQL_SET_MISSING_VALUE`

- *Cause:* The statement `SET` contains a text field literal that does not have a closing quotation mark.

  *Runtime error:* `SAPSQL_SET_QUOTES`

`CX_SY_SQL_UNSUPPORTED_FEATURE`

- *Cause:* A database feature is used that is not supported by the current database system.

  *Runtime error:* `SAPSQL_UNSUPPORTED_FEATURE`
