---
title: "METHOD, BY DATABASE PROCEDURE, FUNCTION, GRAPH WORKSPACE"
source_file: abapmethod_by_db_proc.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# METHOD, BY DATABASE PROCEDURE, FUNCTION, GRAPH WORKSPACE

## Syntax

``` abap
METHOD meth BY DATABASE PROCEDURE|FUNCTION|{GRAPH WORKSPACE} 
            FOR db 
            LANGUAGE db_lang 
            [OPTIONS db_options] 
            [USING   entities] 
            [USING   SCHEMA schema1 OBJECTS db_entities] 
            [USING   SCHEMA schema2 OBJECTS db_entities] 
            ... . 
  ... 
ENDMETHOD.  
```

### Addition

[1. `... FOR db`](abapmethod_by_db_proc.md#addition-1)

[2. `... LANGUAGE db_lang`](abapmethod_by_db_proc.md#addition-2)

[3. `... OPTIONS db_options`](abapmethod_by_db_proc.md#addition-3)

[4. `... USING entities`](abapmethod_by_db_proc.md#addition-4)

[5. `... USING SCHEMA schema OBJECTS db_entities`](abapmethod_by_db_proc.md#addition-5)

## Overview

### Description

Implements an [AMDP procedure](../../abap-glossary/abenamdp_procedure_glosry.md), an [AMDP function](../../abap-glossary/abenamdp_function_glosry.md), or a [graph workspace](../../abap-glossary/abengraph_workspace_glosry.md) in an [AMDP class](../../abap-glossary/abenamdp_class_glosry.md). The addition `BY DATABASE PROCEDURE`, `BY DATABASE FUNCTION` or `BY DATABASE GRAPH WORKSPACE` can be specified in the [implementation part](../../abap-glossary/abenimplementation_part_glosry.md) of a [global class](../../abap-glossary/abenglobal_class_glosry.md) that contains an appropriate tag interface [`IF_AMDP_MARKER_...`](abenamdp_classes.md) for [AMDP classes](../../abap-glossary/abenamdp_class_glosry.md).

- The addition `BY DATABASE PROCEDURE` defines an [AMDP procedure implementation](abenamdp_procedure_methods.md) for implementing a [database procedure](../../abap-glossary/abendatabase_procedure_glosry.md).

- The addition `BY DATABASE FUNCTION` defines an [AMDP function implementation](abenamdp_function_methods.md) for implementing a [database function](../../abap-glossary/abendatabase_function_glosry.md).

- The addition `BY DATABASE GRAPH WORKSPACE` defines a [graph workspace](../../abap-glossary/abengraph_workspace_glosry.md) that can be consumed by a [graph procedure](../../abap-glossary/abengraph_procedure_glosry.md) using [GraphScript](../../abap-glossary/abengraphscript_glosry.md), see [Graph Processing](abenamdp_hdb_graph.md).

The parameter interface of the method declared in the [declaration part](../../abap-glossary/abendeclaration_part_glosry.md) must meet the prerequisites for [AMDP procedure implementations](abenamdp_procedure_methods.md) or [AMDP function implementations](abenamdp_function_methods.md). The parameter interface of an AMDP function implementation that implements a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md) is taken from the definition of the CDS table function specified after the addition [`FOR TABLE FUNCTION`](abapclass-methods_for_tabfunc.md) in the declaration of the method. The parameter interface of an AMDP function implementation that implements a [CDS scalar function](../../abap-glossary/abencds_scalar_function_glosry.md) is taken from the definition of the CDS scalar function specified after the addition [`FOR SCALAR FUNCTION`](abapclass-methods_for_scalfunc.md) in the declaration of the method.

The addition `FOR db` defines the database system where the method is used. The addition `LANGUAGE` defines the database-specific language in which the method is implemented. `OPTIONS` is used to specify database-specific options. `USING` is used to declare database objects managed by ABAP that are used in the AMDP method.

## Executable Examples

AMDP - Examples

## Addition 1

`... FOR db`

### Description

Determines the database system for which the AMDP method is used. The AMDP class must contain the appropriate tag interface. The following table shows the syntax that can be specified for `db`, the database system it identifies, and the required tag interface.

| `db`  | **Database System** | **Tag Interface**    |
|-------|---------------------|----------------------|
| `HDB` | SAP HANA database   | `IF_AMDP_MARKER_HDB` |

The AMDP method can only be called in an AS ABAP whose [standard database](../../abap-glossary/abenstandard_db_glosry.md) is managed by the specified database system. Otherwise a runtime error occurs.

### Hints

- Currently, the only available database is the SAP HANA database.

- Additional regular methods can be provided to make an AMDP class with [AMDP procedure implementations](abenamdp_procedure_methods.md) generally available. These methods call the AMDP methods depending on the database system of the current standard AS ABAP database. In database systems that do not yet support AMDP, an alternative implementation in ABAP SQL can be created in regular methods.

## Addition 2

`... LANGUAGE db_lang`

### Description

Determines the database-specific language in which the AMDP is implemented. The following table shows the syntax for `db_lang` used to specify the language depending on the specified database system `db`, the meaning, and a link to further information.

| `db`  | `db_lang`   | **Language**                               | **More Information**                                               |
|-------|-------------|--------------------------------------------|--------------------------------------------------------------------|
| `HDB` | `SQLSCRIPT` | [SQLScript](../../abap-glossary/abensql_script_glosry.md)    | [SQLScript for the SAP HANA Database](abenamdp_hdb_sqlscript.md) |
| `HDB` | `SQL`       | DDL                                        | Not yet documented                                                 |
| `HDB` | `GRAPH`     | [GraphScript](../../abap-glossary/abengraphscript_glosry.md) | [Graph Processing](abenamdp_hdb_graph.md)                        |

The ABAP syntax check examines the implementation of the method for the specified language as far as possible. This is possible only if the check takes place on an AS ABAP whose standard database is managed by the specified database system. The check is performed with respect to the currently installed version of the database. No checks take place on an AS ABAP with a different database system.

## Addition 3

`... OPTIONS db_options`

### Description

Specifies database-specific options for the AMDP procedure or function. The following table shows the syntax for `option` depending on the specified database system `db` and the associated meaning.

| `db`  | `option`                 | **Meaning**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `HDB` | `READ-ONLY`              | Only reads are allowed on the database tables in the database procedure or database function. Other AMDP methods can be called only if they are also flagged as `READ-ONLY`.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `HDB` | `DETERMINISTIC`          | For [AMDP scalar functions](../../abap-glossary/abenamdp_scalar_function_glosry.md) only. If a query calls an AMDP scalar function more than once with the same values for the input parameters and with the option `DETERMINISTIC`, the function is performed only once, and the result is buffered for the duration of the query. In AMDP scalar functions like this, no functions are allowed that could return different values in different calls. For more information, see [SAP Hana SQLScript Reference](https://help.sap.com/docs/SAP_HANA_PLATFORM/de2486ee947e43e684d39702027f8a94/28f2d64d4fab4e789ee0070be418419d). |
| `HDB` | `SUPPRESS SYNTAX ERRORS` | This syntax is not available in the current ABAP language version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

The option `READ-ONLY` can also be specified with the addition [`AMDP OPTIONS`](abapmethods_amdp_options.md) in the declaration of an AMDP method. It applies when specified either in the implementation or in the declaration of the method, or in both places.

In the current ABAP language version [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md), the addition `READ-ONLY` must be specified at least once.

The syntax check examines the specified options at runtime.

### Hint

The option `SUPPRESS SYNTAX ERRORS` does not affect database objects managed by ABAP that are specified after `USING`.

## Addition 4

`... USING entities`

### Description

Declares one of the following:

- the database objects managed by ABAP accessed in the AMDP procedure or function.

- the [DDL object](../../abap-glossary/abenddl_object_glosry.md) in methods using the syntax `... BY DATABASE GRAPH WORKSPACE ...`.

After `USING`, all database objects from the current [ABAP database schema](../../abap-glossary/abenabap_db_schema_glosry.md) that are used in the implementation must be specified. More specifically, the following database objects must be specified after `USING`:

- [CDS entities](../../abap-glossary/abencds_entity_glosry.md), such as [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md), [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md), and [CDS hierarchies](../../abap-glossary/abencds_hierarchy_glosry.md), using the name of the CDS entity.

- Database tables from the ABAP Dictionary using the name defined in ABAP Dictionary.

- Procedures and functions managed by AMDP. An AMDP procedure or function is specified using the syntax `class=>meth`. Here, `class` is the name of its AMDP class and `meth` is the name of the AMDP procedure implementation or function implementation.

The names of the database objects must be specified without specifying the database schema.

Each database object specified after `USING` must also be used in the procedure or function. No other database objects than those listed above can be specified after `USING` and the procedure or function can only access database objects specified after `USING`.

In summary, database objects of the current database schema can only be accessed in a database procedure or database function managed by AMDP if they are managed by ABAP and specified after `USING`.

### Hints

- `USING` is integrated into the [ABAP runtime framework](../../abap-glossary/abenabap_runtime_frmwk_glosry.md) and the names of database objects `entities` must be specified as usual in ABAP. After `USING`, the implementation in the database-specific language starts and the entities must be addressed accordingly in the implementation. For example, in SQLScript, the following rules apply when addressing database objects `entities`:

  - If specified without quotation marks, the names are not case-sensitive.

  - If specified with double quotation marks, the names must be written in uppercase letters.

  - Special characters enforce the use of double quotation marks and uppercase letters. For example, a namespace prefix usually has a slash (*/*) and therefore enforces double quotation marks and uppercase letters.

  - Example:

    ` ... USING cl_my_class=>my_method. [...] select * from "CL_MY_CLASS=>MY_METHOD" ...`

- Explicit declarations of database objects used in the procedure or function are required for various static checks, such as where-used lists or package checks, and also makes the AMDP method visible on the database level.

- Objects specified after `USING` must be visible at this position. An AMDP method from a different class can be specified only if it can be used by the current class. This applies the visibility concept of ABAP Objects to the database system, even if the database system does not have a similar concept.

- In the case of DDIC database tables, the order of the fields defined in the ABAP Dictionary may differ from the order of the fields on the database. For DDIC database tables specified after `USING`, the AMDP framework ensures that the order of the fields defined in the dictionary is respected when the tables are accessed statically.

- When an AMDP method `class=>meth` is specified after `USING`, the ABAP runtime framework identifies this as a use of the class `class` and its [static constructor](../../abap-glossary/abenstatic_constructor_glosry.md) is executed before the first call of the AMDP method. If an AMDP procedure or function uses other AMDP procedures or functions, it can therefore be assumed that the corresponding static constructor was executed.

- AMDP methods defined and implemented in the same class must also be specified after `USING`, if they are used in the procedure or function.

## Addition 5

`... USING SCHEMA schema OBJECTS db_entities`

\*\* This syntax is not available in the current ABAP language version.\*\*
