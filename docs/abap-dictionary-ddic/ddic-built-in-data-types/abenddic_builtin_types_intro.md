---
title: "DDIC - Built-In Data Types"
source_file: abenddic_builtin_types_intro.html
section: "ABAP Dictionary (DDIC)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Built-In Data Types

The built-in data types in ABAP Dictionary are used as follows:

- To construct user-defined DDIC data types (DDIC data elements, DDIC structures, including DDIC database tables and DDIC views, and DDIC table types) in the ABAP Dictionary. They can also be used in [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md). They cannot be addressed directly in ABAP programs, with the exception of some type specifications in ABAP SQL. Built-in dictionary data types can only be addressed in ABAP programs by using dictionary objects or CDS objects and this is why they are also called external data types.

- They have special technical and semantic properties and can be used to model semantic models.

- They represent an interface between the built-in ABAP types and all possible vendor-specific data types of the supported databases. A mapping takes place in both directions.

The following sections describe the properties of the built-in data types in ABAP Dictionary:

- [Overview of All Built-In Dictionary Types](abenddic_builtin_types.md)

- [Properties of the Built-In Dictionary Types](abenddic_builtin_types_prop.md)

- [Use of the Built-In Dictionary Types](abenddic_builtin_type_usage.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The DDIC database table `DEMO_DDIC_TYPES` has columns with many different built-in ABAP Dictionary data types. The executable example [Built-In Dictionary Types](abenddic_types_abexa.md) shows how to fill each of these columns with literal values.
