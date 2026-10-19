---
title: "DDIC - Ranges Table Type"
source_file: abenddic_table_types_ranges.html
section: "ABAP Dictionary (DDIC) > DDIC - Data Types > DDIC - Table Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Ranges Table Type

A ranges table type is a table type for a [ranges table](../../abap-glossary/abenranges_table_glosry.md). A ranges table is a standard table with a standard key. Its line type is structured specifically to be used in general logical expressions with the relational expression [`IN range tab`](../../abap-programming-language/abap-program-flow-logic/abenlogexp_select_option.md) or used after `WHERE` in ABAP SQL with the relational expression [`IN range tab`](../../abap-programming-language/abap-database-access/abenwhere_logexp_seltab.md). In the ABAP Dictionary, ranges table types are created in the same way as with the statement [`TYPES ... RANGE OF`](../../abap-programming-language/abap-declarations/abaptypes_ranges.md).

The data types of the components `SIGN` and `OPTION` are the data elements `DDSIGN` and `DDOPTION`. The data type for the components `LOW` and `HIGH` must be elementary and can be specified directly as a [built-in data type](../ddic-built-in-data-types/abenddic_builtin_types.md) or using a [data element](abenddic_data_elements.md).

The structure of a ranges table must be a standalone ABAP Dictionary object. It can be generated from the type specifications for the components `LOW` and `HIGH` when the ranges table type is defined.

## Hints

- In ABAP programs, ranges tables can also be defined with reference to data types other than elementary data types.

- In ABAP programs, the structure of a ranges table does not need to be a standalone structure.
