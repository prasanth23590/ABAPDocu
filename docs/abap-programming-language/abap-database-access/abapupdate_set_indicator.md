---
title: "UPDATE writable_obj, set indicators"
source_file: abapupdate_set_indicator.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML > UPDATE writable_obj > UPDATE writable_obj, source"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# UPDATE writable_obj, set indicators

## Syntax

``` abap
... INDICATORS {[NOT] SET STRUCTURE set_ind} 
             | (indicator_syntax) ...  
```

### Alternative

[1. `... INDICATORS [NOT] SET STRUCTURE set_ind`](abapupdate_set_indicator.md#alternative-1)

[2. `... INDICATORS (indicator_syntax)`](abapupdate_set_indicator.md#alternative-2)

## Overview

### Description

The addition `INDICATORS` of the `UPDATE FROM` clause can be used to specify [set indicators](../../abap-glossary/abenset_indicator_glosry.md) for a [work area](../../abap-glossary/abenwork_area_glosry.md) or an [internal table](../../abap-glossary/abeninternal_table_glosry.md). The purpose of set indicators is to indicate columns to be changed. `UPDATE FROM` without indicators overwrites all fields of a row but when set indicators are used, only the indicated fields are updated. The addition can be specified only after `UPDATE FROM` for structured work areas `wa` or internal tables `itab` with a structured row type. The source work area or source internal table must have a structure `set_ind` as the last field with the same number of components as the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) to be updated, where each component serves as a set indicator for one row. There is a static variant and a dynamic variant.

## Alternative 1

`... INDICATORS [NOT] SET STRUCTURE set_ind`

### Description

The [set indicator](../../abap-glossary/abenset_indicator_glosry.md) `set_ind` indicates which fields of a database are to be updated by the `UPDATE FROM` clause. `set_ind` must be included in the source work area or source internal table as the last field and it must contain one component for each column of the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) to be changed. All individual components of `set_ind` must have either the data type `c` and length 1, or the data type `x` and length 1. The `UPDATE FROM` clause checks the content of `set_ind` and updates only fields that are marked with *X* (data type `c`) or hexadecimal *1* (data type `x`). Fields that contain any other character or hexadecimal value are not updated.

When using the addition `INDICATORS NOT SET`, the reverse logic is applied: all fields are updated, except the ones marked with *X* (data type `c`) or hexadecimal *1* (data type `x`).

Key fields must always be included in the indicator structure. However, the set indicators do not have any effect on key fields.

### Hints

- Set indicators work for regular structures, as well as for [LOB handle structures](../../abap-glossary/abenlob_handle_structure_glosry.md). If the source work area or source internal table contains [LOB handle components](../../abap-glossary/abenlob_handle_component_glosry.md) that are not marked for update, the [LOBs](../../abap-glossary/abenlob_glosry.md) they refer to are not updated either. As without set indicators, [LOB handles](../../abap-glossary/abenlob_handle_glosry.md) should always be closed, regardless of whether they were marked for update or not.

- Work areas with set indicators can be defined with the addition [`INDICATORS`](../abap-declarations/abaptypes_indicators.md) of the [`TYPES`](../abap-declarations/abaptypes.md) statement.

- The addition [`BITFIELD`](abapselect_indicators.md) that is possible for `SELECT` cannot be used for `UPDATE`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

An internal table `ind_tab` is defined as the source structure. When using the addition [`INDICATORS`](../abap-declarations/abaptypes_indicators.md) of the [`TYPES`](../abap-declarations/abaptypes.md) statement, it consists of the structure of the table entity `DEMO_CDS_UPDATE_TE` as well as the [indicator structures](../../abap-glossary/abenindicator_structure_glosry.md) `col_ind` as the last component, which mirrors the structure of the CDS table entity. Three rows are chosen to be updated. From these rows, however, only the field `COL4` is marked for update. When the `UPDATE FROM` statement is carried out, only the three indicated fields are updated. Without the set indicators, the three rows would have been overwritten entirely and all fields for which no value was specified would have been initialized (see image below).

**Note:** The following code is an extract from the executable example [`UPDATE, SET INDICATORS`](abenupdate_set_indicators_abexa.md). The results shown in the image can be replicated with the executable example.

``` abap
TYPES ind_wa TYPE demo_cds_update_te WITH INDICATORS col_ind 
             TYPE abap_boolean. 
DATA ind_tab TYPE TABLE OF ind_wa. 
 
ind_tab = VALUE #( 
       ( id = 'D' col4 = 4000 col_ind-col4 = abap_true ) 
       ( id = 'E' col4 = 5000 col_ind-col4 = abap_true ) 
       ( id = 'F' col4 = 6000 col_ind-col4 = abap_true ) ). 
 
UPDATE demo_cds_update_te FROM TABLE @ind_tab 
                   INDICATORS SET STRUCTURE col_ind.
```abap
`result1` shows the result with set indicators, `result2` without set indicators\. 
```

  
![figure](images_abdoc_set_indicators.png)  

### Executable Example

[`UPDATE, SET INDICATORS`](abenupdate_set_indicators_abexa.md)

## Alternative 2

`... INDICATORS (indicator_syntax)`

### Description

Instead of the static specification, a parenthesized data object `indicator_syntax` can be specified after `INDICATORS`. This data object must contain the syntax shown for the static specification when the statement is executed. The syntax in `indicator_syntax` is not case-sensitive. If the data object `indicator_syntax` has no content, then the addition has no effect.

### Security Hint

If used incorrectly, dynamic programming techniques can present a serious security risk. Any dynamic content that is passed to a program from the outside must be checked thoroughly or escaped before it is used in dynamic statements. This can be done using the system class `CL_ABAP_DYN_PRG` or the built-in function [`escape`](../abap-processing-internal-data/abenescape_functions.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example is similar to the example for specifying information statically. The CDS table entity `DEMO_CDS_UPDATE_TE` is updated from the work area `col_ind` and only the column `COL4` is marked for update. In contrast to the first example, the set indicator is specified dynamically. The class `CL_DEMO_UPDATE_SET_IND_DYN` fills the CDS table entity with values, carries out the `UPDATE FROM` statement, and displays the result.

``` abap
TYPES ind_wa TYPE demo_cds_update_te WITH INDICATORS col_ind. 
DATA  ind_wa TYPE ind_wa. 
 
FINAL(indicator_syntax) = `SET STRUCTURE col_ind`. 
 
ind_wa = VALUE #( id = 'I' col4 = 4000 col_ind-col4 = '01' ). 
 
UPDATE demo_cds_update_te FROM @ind_wa INDICATORS (indicator_syntax).
```
