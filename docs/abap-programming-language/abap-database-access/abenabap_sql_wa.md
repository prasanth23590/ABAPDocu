---
title: "ABAP SQL - Work Areas in Statements"
source_file: abenabap_sql_wa.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Work Areas in Statements

If any of the ABAP SQL statements listed below specify work areas `wa` or internal tables `itab` as the target or source areas, the following prerequisites apply to the work area or row type of the internal table.

- `SELECT` or `FETCH` without the addition `CORRESPONDING FIELDS`,

- `INSERT`, `UPDATE`, `MODIFY`, or `DELETE`

If these prerequisites are ignored, a syntax error occurs or an exception is raised.

- [Regular Work Areas](abenabap_sql_wa.md#regular-work-areas)

## Regular Work Areas

The following rules apply to work areas :

- The data type of the work area or row type of the internal table must not be [deep](../../abap-glossary/abendeep_glosry.md) or contain deep components. This excludes strings and special work areas for [streaming](abenabap_sql_streaming.md) and [locators](abenlocators.md).

- The data type of the work area and the row type of the internal table must not contain any [enumerated types](../../abap-glossary/abenenum_type_glosry.md).

- The work area or row type of the internal table must be at least as long as the database structure and the [alignment](../../abap-glossary/abenalignment_glosry.md) must match. In the statement `DELETE`, this prerequisite must only be met in the length of the [primary key](../../abap-glossary/abenprimary_key_glosry.md).

- If the work area or rows of the internal table are structured, the [fragment view](../../abap-glossary/abenunicode_fragment_view_glosry.md) of the database structure must match that of the work area or the internal table.

- If the work area or rows of the internal table are elementary, they must be character-like and [flat](../../abap-glossary/abenflat_glosry.md). The columns of the database structure must also be character-like and flat.

- If the work area contains strings as components or is itself a string, or if columns of type [`SSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`STRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`RAWSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), or `GEOM_EWKB` appear in the database structure, the work area must be compatible with the database structure.

- If the column specification `*` is used in the statement `SELECT` to access a [CDS entity](../../abap-glossary/abencds_entity_glosry.md), the work area is always checked as if it contained a string as a component.

- For the modifying operations `INSERT`, `UPDATE`, and `MODIFY`, the passed values must match the value range of the columns of the DDIC database tables. Otherwise, corresponding exceptions are raised. This applies in particular to the following:

  - Columns with numeric data types.

  - Columns of the types `SSTRING`, `STRING`, `RAWSTRING`, or `GEOM_EWKB`. The strings of the work area must not be longer than the maximum length of the columns in the database structure. This length can be determined using the built-in function [`dbmaxlen`](../abap-processing-internal-data/abenlength_functions.md).

  - Columns of the types `DATN`, `TIMN`, and `UTCLONG`. Only valid dates, times, and UTC time stamps according to the [POSIX standard](../../abap-glossary/abenposix_timestamp_glosry.md) can be passed.

### Hint

The work area or row structure of the internal table should always be structured in the same way as the database structure. If a single data source is used in the ABAP SQL statement, a data object built in the same way can be declared with reference to the relevant DDIC structure. If multiple data sources are used (in the statement `SELECT`), a data object built in the same way can be constructed as a nested structure, which contains the structures of the single data sources in the order specified in the statement as substructures. No structure should be used in which all components are on one level, because this ignores potential [alignment gaps](../../abap-glossary/abenalignment_gap_glosry.md) between the individual data sources.
