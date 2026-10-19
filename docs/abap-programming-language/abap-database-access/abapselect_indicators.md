---
title: "indicators"
source_file: abapselect_indicators.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Overview > ABAP SQL - Null Values"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# indicators

## Syntax

``` abap
... INDICATORS {[NOT] NULL STRUCTURE null_ind} 
             | {[NOT] NULL BITFIELD null_ind} 
             | {(indicator_syntax)}...  
```

### Alternative

[1. `... INDICATORS [NOT] NULL STRUCTURE null_ind`](abapselect_indicators.md#alternative-1)

[2. `... INDICATORS [NOT] NULL BITFIELD null_ind`](abapselect_indicators.md#alternative-2)

[3. `... INDICATORS (indicator_syntax)`](abapselect_indicators.md#alternative-3)

## Overview

### Description

The addition `INDICATORS` can be used for [`INSERT`](abapinsert_dbtab.md), [`MODIFY`](abapmodify_dbtab.md), [`SELECT`](abapselect.md), [`UPDATE`](abapupdate.md) to specify [null indicators](../../abap-glossary/abennull_indicator_glosry.md). It describes whether individual fields contain a [null value](abenabap_sql_null_values.md) or not. It is used with structured target areas.

`SELECT` can be specified for existing data objects, in combination with the additions [`CORRESPONDING FIELDS`](abapinto_clause.md), [`NEW`](abapselect_into_target.md), and with [inline declarations](abapselect_into_target.md).

There are two static variants:

- A structured indicator that is a substructure of the structured target area.

- A [byte field](../../abap-glossary/abenbyte_field_glosry.md) indicator that is a [byte field type](../../abap-glossary/abenbyte_field_type_glosry.md) component of the structured target area.

A dynamic variant allows the syntax of the static variants to be specified as a dynamic token.

## Restriction

For null indicators the following restrictions apply:

- Null indicators are only evaluated for nullable columns. Primary key fields are not nullable. If a table contains no nullable columns, the null indicators have no effect.

- The addition can be specified only for structured work areas `wa` or internal tables `itab` with a structured line type. For `INSERT`, `UPDATE` and `MODIFY`, the names of the components must match the `dbtab` names, `wa` names and `itab` names. The order and number of components must correspond to the database columns. The components must be a homogenous structure of X(1) or C(1).

- The addition is not supported for `MERGE`, `DELETE` and long forms such as `MODIFY FROM SELECT`.

## Alternative 1

`... INDICATORS [NOT] NULL STRUCTURE null_ind`

### Description

Specifies the [substructure](../../abap-glossary/abensubstructure_glosry.md) `null_ind` of a structured target area as a [null indicator](../../abap-glossary/abennull_indicator_glosry.md).

The indicator structure describes for each supplied column whether the column contains the null value or not.

The substructure must contain at least as many components as the number of columns that are inserted, updated, modified or selected. Each component must be of type `x` or `c` with length 1.

For the common case (positional mapping, no `CORRESPONDING FIELDS`):

- The indicator structure must be the last component of `wa` or `itab`.

  - **Exception:** If null indicators are used in combination with [UPDATE writable_obj, set indicators.](abapupdate_set_indicator.md) the null indicator must be the next to last component before the update set indicator.

- It must have the same name as a column.

- Component names of the indicator structure are ignored.

- Indicator components are evaluated from left to right by position corresponding to the target columns.

The addition `INDICATORS ... STRUCTURE` after an [inline declaration](../../abap-glossary/abeninline_declaration_glosry.md) with `@DATA|@FINAL(wa)` or `@DATA|@FINAL(itab)` adds an [indicator structure](../../abap-glossary/abenindicator_structure_glosry.md) named `null_ind` to the end of the declared structure or line type. For each supplied column, this substructure contains an identically named component of type `x` and length 1 in the same order.

With `SELECT` and the addition `CORRESPONDING FIELDS`:

- The indicator structure can appear at any position of `wa` or `itab`.

- It must not have the same name as a column.

- For each supplied component, a component with the same name must exist in the indicator structure.

If preceding components of the structure declared inline are substructures, the substructure `null_ind` is also structured accordingly.

The name `null_ind` must not be used as the name of a column.

The indicator components are evaluated based on whether they are set or initial:

- Without the addition `NOT`:

  - A set indicator (value '1' for type x, value 'X' for type c) means that the corresponding column contains NULL.

  - Otherwise, the component is initial.

- With the addition `NOT`:

  - A set indicator means that the corresponding column does not contain NULL.

  - Otherwise, the component is initial.

When indicators are read, initial means not null and not initial means null.

For `SELECT`, it is recommended and for `INSERT`, `MODIFY` and `UPDATE` it is required, that the components of the null indicator have exactly the same names and order as the corresponding columns and that the null indicator is placed as an [indicator structure](../../abap-glossary/abenindicator_structure_glosry.md) behind all other components of the target structures.

Work areas with [indicator structures](../../abap-glossary/abenindicator_structure_glosry.md) can be defined using the addition [TYPES, INDICATORS](../abap-declarations/abaptypes_indicators.md) of the [`TYPES`](../abap-declarations/abaptypes.md) statement.

## Alternative 2

`... INDICATORS [NOT] NULL BITFIELD null_ind`

### Description

Specifies the [byte field type](../../abap-glossary/abenbyte_field_type_glosry.md) component `null_ind` of a structured target area as a [null indicator](../../abap-glossary/abennull_indicator_glosry.md).

The bitfield must provide at least one bit per target column. The length must be at least as calculated with ( n + 7 ) [`DIV`](../abap-processing-internal-data/abenarith_operators.md) 8 where n is the number of target columns.

For `SELECT` the position and evaluation of the byte field depend on whether `CORRESPONDING FIELDS` is specified:

For the common case (positional mapping, no `CORRESPONDING FIELDS`):

- The byte field must be the last component of `wa` or `itab`.

  - **Exception:** If null indicators are used in combination with [UPDATE writable_obj, set indicators](abapupdate_set_indicator.md) the null indicator must be the next to last component before the update set indicator.

- Bit positions are interpreted from left to right, corresponding to the target columns by position.

With `SELECT` and the addition `CORRESPONDING FIELDS`:

- The byte field can appear at any position in wa or itab, but must not have the same name as a column.

- It is recommended that bitfields are placed behind all other components.

- Bit positions are mapped to the target structure by name; only bits corresponding to supplied components are evaluated, all others are set to 0.

The indicator values are set as follows:

- If the optional addition `NOT` is not specified, a bit value 1 means that the corresponding column contains the null value. For columns that do not contain the null value, the corresponding bits are set to 0.

- If the optional addition `NOT` is specified, a bit value 1 means that the corresponding column does not contain the null value. For columns that contain the null value, the corresponding bits are set to 0.

Trailing excess bits of the byte field that are not covered by the above rules are always set to 0.

[Condensed indicator structures](../../abap-glossary/abencondensed_ind_structure_glosry.md) for the null indicators can be defined with the addition [INDICATORS ... AS BITFIELD](../abap-declarations/abaptypes_indicators.md) in the [TYPES](../abap-declarations/abaptypes.md) statement.

The statement [`GET BIT`](../abap-processing-internal-data/abapget_bit.md) or [bit operators](../abap-processing-internal-data/abenbit_operators.md) can be used to evaluate\` null indicators represented by bits.

### Executable Example

The executable example [`SELECT`, Byte Field Indicators](abenselect_ind_bitfield_abexa.md) shows the difference between position-based and name-based assignments without and with `CORRESPONDING FIELDS`.

## Alternative 3

`... INDICATORS (indicator_syntax)`

### Description

Instead of the static specifications above, a dynamic specification can be provided. The dynamic variant behaves identically to the static variants. The same restrictions apply. The data object `indicator_syntax` must contain valid indicator syntax. The syntax is not case-sensitive. When an internal table is specified, the syntax can be distributed across multiple rows. Invalid syntax raises a catchable exception from the class `CX_SY_DYNAMIC_OSQL_ERROR`. If the content of `indicator_syntax` is initial, the addition `INDICATORS` is ignored.

### Security Hint

If used incorrectly, dynamic programming techniques can present a serious security risk. Any dynamic content that is passed to a program from the outside must be checked thoroughly or escaped before it is used in dynamic statements. This can be done using the system class `CL_ABAP_DYN_PRG` or the built-in function [`escape`](../abap-processing-internal-data/abenescape_functions.md).
