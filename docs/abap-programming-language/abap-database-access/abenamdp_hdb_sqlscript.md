---
title: "AMDP - SQLScript for the SAP HANA Database"
source_file: abenamdp_hdb_sqlscript.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Methods > METHOD, BY DATABASE PROCEDURE, FUNCTION, GRAPH WORKSPACE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AMDP - SQLScript for the SAP HANA Database

[SQLScript](../../abap-glossary/abensql_script_glosry.md) is a script language, documented in the [SAP HANA SQLScript Reference](https://help.sap.com/docs/SAP_HANA_PLATFORM/de2486ee947e43e684d39702027f8a94/28f2d64d4fab4e789ee0070be418419d), and used to program [SQLScript procedures](../../abap-glossary/abensql_script_procedure_glosry.md) and [SQLScript functions](../../abap-glossary/abensql_script_function_glosry.md) in the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md). It is the implementation language of an [AMDP method](abenamdp_methods.md) that specifies the addition [`FOR HDB LANGUAGE SQLSCRIPT`](abapmethod_by_db_proc.md) in the statement `METHOD`.

- [AMDP Procedures and Functions in SAP HANA](abenamdp_hdb_sqlscript.md#amdp-procedures-and-functions-in-sap-hana)

- [Syntax](abenamdp_hdb_sqlscript.md#syntax)

- [Parameter Interface](abenamdp_hdb_sqlscript.md#parameter-interface)

  - [SQLScript Procedures](abenamdp_hdb_sqlscript.md#sqlscript-procedures)

  - [SQLScript Functions](abenamdp_hdb_sqlscript.md#sqlscript-functions)

- [Use](abenamdp_hdb_sqlscript.md#use)

- [Access to ABAP Types](abenamdp_hdb_sqlscript.md#access-to-abap-types)

- [Access to Database Schemas](abenamdp_hdb_sqlscript.md#access-to-database-schemas)

## Hints

- AS ABAP requires the following authorizations as a user of the database system to be able to manage SQLScript procedures and functions on the SAP HANA database:

  - Privilege `Execute` on the object `GET_PROCEDURE_OBJECTS` of the schema `SYS`

  - Privilege `Execute` on the object `TRUNCATE_PROCEDURE_OBJECTS` of the schema `SYS`

    Further authorizations are required for debugging AMDP methods in the [ABAP development tools for Eclipse (ADT)](../../abap-glossary/abenadt_glosry.md). Missing authorizations can be identified using transaction `SICK`.

## AMDP Procedures and Functions in SAP HANA

The SQLScript implementation of an AMDP method with the name `meth` that belongs to an AMDP class `class` is stored by the ABAP runtime framework as an SQLScript procedure under the name `CLASS=>METH` in the [ABAP database schema](../../abap-glossary/abenabap_db_schema_glosry.md) of the SAP HANA database. The names must be written in uppercase letters when used in the database system. AS ABAP is responsible for all transports, administration, and access control. SQLScript procedures and functions managed using AMDP can be accessed as follows:

- Calls from ABAP

  - Call of an [AMDP procedure](../../abap-glossary/abenamdp_procedure_glosry.md) or [AMDP scalar function](../../abap-glossary/abenamdp_table_function_glosry.md) with standard method call [`meth( ... )`](../abap-calling-and-exiting-program-units/abapcall_method_static_short.md) in ABAP programs. For `meth`, the associated [AMDP procedure implementation](abenamdp_procedure_methods.md) is specified.

  - Calls an [AMDP table function](../../abap-glossary/abenamdp_table_function_glosry.md) by specifying the assigned [CDS table function](../../abap-glossary/abencds_table_function_glosry.md) or a [CDS view](../../abap-glossary/abencds_table_function_glosry.md) that uses a CDS table function in an ABAP SQL read statement.

- Calls from other AMDP procedures or functions

  - An AMDP procedure or function implemented using SQLScript in the same class or a different class can call another AMDP procedure with the usual [SQLScript syntax](https://help.sap.com/docs/SAP_HANA_PLATFORM/de2486ee947e43e684d39702027f8a94/28f2d64d4fab4e789ee0070be418419d):

    `CALL "CLASS=>METH"( f1 => a1, f2 => a2, ... );` The called AMDP procedure implementation `CLASS=>METH` must be specified after the addition [`USING`](abapmethod_by_db_proc.md) of the calling method. The usual visibility rules from ABAP Objects apply. A database procedure or database function implemented in a class cannot call a procedure implemented in a private AMDP procedure implementation of a different class, unless a friendship exists between the classes.

  - An AMDP procedure or function implemented using SQLScript in the same class or a different class can call another AMDP function implemented with SQLScript using the usual [SQLScript syntax](https://help.sap.com/docs/SAP_HANA_PLATFORM/de2486ee947e43e684d39702027f8a94/28f2d64d4fab4e789ee0070be418419d):

    `SELECT ... FROM "CLASS=>METH"( f1 => a1, f2 => a2, ... );` The specified AMDP function implementation `CLASS=>METH` must be specified after the addition [`USING`](abapmethod_by_db_proc.md) of the calling method. An AMDP function implementation is always public.

## Syntax

The syntax of a [SQLScript procedure](../../abap-glossary/abensql_script_procedure_glosry.md) or [function](../../abap-glossary/abensql_script_function_glosry.md) written in SQLScript is exactly as described under [SAP Hana SQLScript Reference](https://help.sap.com/docs/SAP_HANA_PLATFORM/de2486ee947e43e684d39702027f8a94/28f2d64d4fab4e789ee0070be418419d), with one exception: The character `*` at the start of a line indicates a [comment](../abap-syntax-elements-of-an-abap-program/abencomment.md), as in ABAP. When the procedure or function is saved in the database system, the asterisk, `*`, is transformed to the usual double hyphens, `--`.

### Hints

- Support for ABAP comments introduced using `*` enables the use of change entries inserted by the *Modification Assistant* tool in ABAP programs. This property should not be used when creating AMDP methods in the regular way.

- The syntax is checked only on an AS ABAP whose standard database is a SAP HANA database. Here, a temporary database procedure or function is created that checks the syntax.

- The use of the dynamic options under SQLScript syntax is strongly discouraged due to the reasons specified under [AMDP](abenamdp.md). This applies in particular to statements such as `EXEC`, `EXECUTE IMMEDIATE`, or `APPLY FILTER`.

## Parameter Interface

The elementary ABAP types of interface parameters of an AMDP method are mapped to the appropriate types in SQLScript. as shown in the [mapping tables](abenamdp_hdb_sqlscript_mapping.md).

### SQLScript Procedures

The parameter interface of an [SQLScript procedure](../../abap-glossary/abensql_script_procedure_glosry.md) supports input parameters declared using `IN`, output parameters declared using `OUT`, and input/output parameters declared using `INOUT`&#x200E;. All parameters can be scalar and tabular with the exception of input/output parameters, which can only be scalar. When used in the procedure, certain operand positions must or can be prefixed with a colon (`:`) in certain operand positions.

The parameter interface of an [AMDP procedure implementation](abenamdp_procedure_methods.md) that implements an SQLScript procedure is transformed as follows:

- An input parameter of the method defined using `IMPORTING` becomes an input parameter of the procedure declared using `IN`.

- An output parameter of the method defined using `EXPORTING` becomes an output parameter of the procedure declared using `OUT`.

- If `CHANGING` is used to define a

  - scalar input/output parameter of the method, the parameter becomes an input/output parameter of the database procedure declared using `INOUT`.

  - tabular input/output parameter of the method, it is transformed to a pair of input and output parameters declared using `IN` and `OUT` on the database, since SQLScript does not support `INOUT` parameters. The `CHANGING` parameter becomes an `OUT` parameter of the procedure with the same name as the `CHANGING` parameter. The `IN` parameter is created with an internal name consisting of the name of the `CHANGING` parameter and a postfix `__IN__`. The `IN` parameter is assigned to the `OUT` parameter before the start of the actual AMDP procedure. This transformation and the corresponding call are generally transparent for all ABAP developers. It becomes visible only when the database procedure is displayed in a tool or called from another database procedure (see the [executable example](abenamdp_changing_cs_abexa.md)).

Elementary and tabular method parameters become scalar and tabular parameters of the database procedure respectively. As well as the restrictions for the parameter interface of an AMDP method described under [AMDP](abenamdp.md), the following restrictions apply in the implementation with SQLScript:

- An [input/output parameter](../../abap-glossary/abeninput_output_parameter_glosry.md) declared using [`CHANGING`](../abap-declarations/abapmethods_general.md) cannot have the type `string` or `xstring`. An exception this rule are parameters that are typed with reference to the built-in type [`SSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) from the ABAP Dictionary.

- The length of a parameter typed with the type `c` or `n` is restricted to a maximum of 5000 characters.

- Parameters of the types `string` and `xstring` cannot be assigned a replacement value using [`DEFAULT`](../abap-declarations/abapmethods_parameters.md), which means they cannot be optional parameters. Since release 7.78, parameters of the types `f`, `decfloat16`, `decfloat34`, and `sstring` can be assigned a replacement value using `DEFAULT`.

### Hint

In SQLScript, tabular parameters are handled as temporary database tables. An internal table passed to SQLScript can be accessed just like a database table.

### SQLScript Functions

The parameter interface of an [SQLScript function](../../abap-glossary/abensql_script_function_glosry.md) supports input parameters declared using `IN` and a return value declared using `RETURNS`. The input parameters of a scalar function must be scalar, and the input parameters of a table function can be scalar and tabular. The return value of a scalar function is scalar, and the return value of a table function is tabular.

The parameter interface of an [AMDP function implementation](abenamdp_function_methods.md) that implements an SQLScript procedure is transformed as follows:

- An input parameter of the method defined using `IMPORTING` becomes an input parameter of the function declared using `IN`.

- The return value of the method defined using `RETURN` becomes the return value of the procedure declared using `RETURNS`.

The same restrictions apply as in SQLScript procedures, as well as the following:

- AMDP scalar functions cannot have any output parameters besides the return value.

- AMDP table functions for [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md) can only have scalar input parameters.

## Use

As described above, SQLScript procedures and functions managed in the SAP HANA database using AMDP can be used in ABAP programs and in other AMDP procedures according to the visibility of the AMDP methods. Recursive and cyclical calls are forbidden in the HANA database system, which means that

- an SQLScript procedure or function cannot use itself

- an AMDP method that implements an SQLScript procedure cannot call any database procedures or use any database functions that themselves use the AMDP procedure or function.

## Access to ABAP Types

In an SQLScript procedure, the [`AMDP macro`](../../abap-glossary/abenamdp_macro_glosry.md) [`$ABAP.type`](abenamdp_abap_types.md) can be used to access ABAP types that have a corresponding type in SQLScript. The type mapping is described in the [mapping tables](abenamdp_hdb_sqlscript_mapping.md).

## Access to Database Schemas

In an SQLScript procedure, it is possible to access objects in the same database schema directly. The name of the current database schema must not be specified here. To access an object in another database schema, the name of the database schema can be specified as prefix separated by a period, as usual in SQLScript.

## Executable Examples

- [AMDP - Examples (Client-safe)](abenamdp_cs_abexas.md)
