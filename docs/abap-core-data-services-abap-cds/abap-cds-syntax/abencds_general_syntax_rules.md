---
title: "ABAP CDS - General Syntax Rules"
source_file: abencds_general_syntax_rules.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Syntax"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - General Syntax Rules

The general syntax rules for the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) and [CDS DCL](../../abap-glossary/abencds_dcl_glosry.md) for defining [CDS objects](../../abap-glossary/abencds_object_glosry.md) in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) are as follows:

- Keywords

  - Keywords must be all uppercase, all lowercase, or in lowercase with an uppercase initial letter. Other mixes of uppercase and lowercase are not allowed.

- Names

  - Names are not case-sensitive.

  - A name must contain at least 2 characters but no more than 30 characters.

  - A name can consist of letters, numbers, underscores (`_`), and slashes (`/`).

  - A name must start with a letter, slash character, or underscore. Underscores are recommended as the naming convention for [CDS associations](../../abap-glossary/abencds_association_glosry.md).

  - The separator for names with multiple parts is a period (`.`). Names with multiple parts can be paths, columns with a prefixed data source, and structured annotations.

  - The following CDS keywords cannot be used as names:

    `ALL`, `AND`, `AS`, `ASSOCIATION`, `AVG`, `CASE`, `CAST`, `COUNT`, `CROSS`, `DISTINCT`, `EXISTS`, `EXTEND`, `FROM`, `FULL`, `GROUP`, `HAVING`, `INNER`, `JOIN`, `KEY`, `LEFT`, `MAX`, `MIN`, `NOT`, `NULL`, `ON`, `OR`, `ORDER`, `RIGHT`, `SELECT`, `SUM`, `UNION`, `VIEW`, `WHEN`, `WHERE`

- Literals

  - In general ABAP CDS, [untyped](../../abap-glossary/abenuntyped_literal_glosry.md) numeric and untyped character literals are available:

    An untyped character literal is a character string enclosed in single quotation marks (`'`).

    An untyped numeric literal is a series of digits between 0 and 9. It can be directly prefixed by a `+` or `-` sign and can contain a decimal point (`.`) after the first digit.

  - In [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md), [typed literals](../../abap-glossary/abentyped_literal_glosry.md) are available for [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) and [CDS hierarchies](../../abap-glossary/abencds_hierarchy_glosry.md). Typed literals are available for almost all built-in ABAP Dictionary data types. A typed literal is specified by writing an ABAP Dictionary data type with the type namespace `abap.` as prefix followed by the character-like representation of the value in single quotation marks (`'`).

    Example: `abap.dats'20200101'`

  - Escaping literals in ABAP CDS:

    A single quote (') is escaped with a single quote:`'...''...'`.

    A backslash (\\ is escaped with a backslash: `'...\\...'` **Exception:** Escaping with a backslash is not supported in [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md).

  - For more information about literals in ABAP CDS, see the topic [CDS DDL - CDS View Entity, `literal`](../abap-cds-data-definitions/abencds_literal_v2.md).

- Comments

  - Two forward slashes (`//`) introduce a comment, which continues until the end of the line.

  - Comments within lines or that span multiple lines are enclosed by the characters `/*` and `*/`.

- Suppressing syntax check warnings

  - To suppress syntax check warnings in a [CDS object](../../abap-glossary/abencds_object_glosry.md), surround the warning with the following comments:

    `/* start suppress warning *identifier* */ *warning* /* end supporess warning *identifier* */`

  - The identifier for suppressing a particular warning can be found in the long text of the error message of the warning. Not all warnings can be suppressed.

  - For further details, see the [Knowledge Transfer Document](../../abap-glossary/abenktd_glosry.md) `DD_SUPPRESS_WARNING`.

- Separators

  - Statements can be closed using a semicolon (`;`). Sometimes this is mandatory.

- Protected words

  - Certain keywords are protected and cannot be used as user-defined names. The reserved names that cannot be used are specified in the DDIC database table `TRESE`.

## Hints

- The closing semicolon after a statement is sometimes optional because one piece of CDS source code can currently only contain a single statement.

- In [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md) for [CDS data definitions](../../abap-glossary/abencds_data_definition_glosry.md) and [DCL source code](../../abap-glossary/abendcl_source_code_glosry.md) for [CDS roles](../../abap-glossary/abencds_role_glosry.md), as well as two slashes, two dashes (`--`) can also be used to introduce a comment. Slashes (`//`), however, are the recommended method. Two dashes are not allowed in [`DDLA` source code](../../abap-glossary/abenddla_source_code_glosry.md) for [annotation definitions](../../abap-glossary/abencds_anno_definition_glosry.md) and in [`DDLX` source code](../../abap-glossary/abenddlx_source_code_glosry.md) for [metadata extensions](../../abap-glossary/abencds_metadata_extension_glosry.md).
