---
title: "ABAP SQL Statements with MAPPING FROM ENTITY"
source_file: abapmapping_from_entity.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > Other RAP-Related ABAP Language Elements and Topics > Type Mapping for RAP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL Statements with MAPPING FROM ENTITY

## Syntax

``` abap
  { INSERT ... } 
| { MODIFY ... } 
| { UPDATE ... [INDICATORS SET STRUCTURE %control] } 
| { DELETE ... } MAPPING FROM ENTITY.  
```

[`INSERT ...`](../../abap-programming-language/abap-database-access/abapinsert_dbtab.md) · [`MODIFY ...`](../../abap-programming-language/abap-database-access/abapmodify_dbtab.md) · [`UPDATE ... [INDICATORS SET STRUCTURE %control]`](../../abap-programming-language/abap-database-access/abapupdate.md) · [`DELETE ...`](../../abap-programming-language/abap-database-access/abapdelete_dbtab.md)

### Variant

[1. `INSERT ... MAPPING FROM ENTITY.`](abapmapping_from_entity.md#variant-1)

[2. `MODIFY ... MAPPING FROM ENTITY.`](abapmapping_from_entity.md#variant-2)

[3. `UPDATE ... [INDICATORS SET STRUCTURE %control] MAPPING FROM ENTITY.`](abapmapping_from_entity.md#variant-3)

[4. `DELETE ... MAPPING FROM ENTITY.`](abapmapping_from_entity.md#variant-4)

## Overview

### Description

The addition `MAPPING FROM ENTITY` of the modifying ABAP SQL statements [`INSERT`](../../abap-programming-language/abap-database-access/abapinsert_dbtab.md), [`UPDATE`](../../abap-programming-language/abap-database-access/abapupdate.md), [`MODIFY`](../../abap-programming-language/abap-database-access/abapmodify_dbtab.md), and [`DELETE`](../../abap-programming-language/abap-database-access/abapdelete_dbtab.md) is used to handle structures and internal tables that are typed with [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md), especially in cases where a [type mapping](../rap-behavior-definitions/abenbdl_type_mapping.md) is specified in the [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md).

### Hints

- In case of a problematic type conversion when using these statements, for example `INT4` to `NUMC`, a [`... CORRESPONDING #( ... MAPPING FROM ENTITY ) ...`](abapeml_corresponding.md) is automatically carried out without an explicit programming.

- The catchable exception `CX_SY_CONVERSION_ERROR` occurs in case of type conversion errors.

## Variant 1

`INSERT ... MAPPING FROM ENTITY.`

### Description

Used to insert one or more rows from a [source](../../abap-programming-language/abap-database-access/abapinsert_source.md) into a [target](../../abap-programming-language/abap-database-access/abapiumd_target.md). See the detailed syntax options for `INSERT` in the [`INSERT` topic](../../abap-programming-language/abap-database-access/abapinsert_dbtab.md).

The sources, i. e. a structure or an internal table, must be typed with the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) [`TYPE STRUCTURE FOR`](abaptype_structure_for.md) and [`TYPE TABLE FOR`](abaptype_table_for.md) respectively. In this case, the types `... FOR UPDATE ...`, `... FOR CREATE ...`, `... FOR DELETE ...`, and `... FOR CHANGE ...` are possible.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows multiple `INSERT` statements with the `MAPPING FROM ENTITY` addition.

``` abap
DATA: ins_tab TYPE TABLE FOR CREATE demo_managed_root_map, 
      ins_wa  TYPE STRUCTURE FOR CREATE demo_managed_root_map. 
... 
INSERT demo_tab_root_3 FROM @ins_wa MAPPING FROM ENTITY. 
INSERT demo_tab_root_3 FROM TABLE @ins_tab MAPPING FROM ENTITY.
```

## Variant 2

`MODIFY ... MAPPING FROM ENTITY.`

### Description

Used to insert one or more rows into a [target](../../abap-programming-language/abap-database-access/abapiumd_target.md) or update existing rows based on the specification in a [source](../../abap-programming-language/abap-database-access/abapinsert_source.md). See the detailed syntax options for `MODIFY` in the [`MODIFY` topic](../../abap-programming-language/abap-database-access/abapmodify_dbtab.md).

The sources, i. e. a structure or an internal table, must be typed with the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) [`TYPE STRUCTURE FOR`](abaptype_structure_for.md) and [`TYPE TABLE FOR`](abaptype_table_for.md) respectively. In this case, the types `... FOR UPDATE ...`, `... FOR CREATE ...`, `... FOR DELETE ...`, and `... FOR CHANGE ...` are possible.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows multiple `MODIFY` statements with the `MAPPING FROM ENTITY` addition.

``` abap
DATA: mod_tab TYPE TABLE FOR CREATE demo_managed_root_map, 
      mod_wa  TYPE STRUCTURE FOR CREATE demo_managed_root_map. 
... 
MODIFY demo_tab_root_3 FROM @mod_wa MAPPING FROM ENTITY. 
MODIFY demo_tab_root_3 FROM TABLE @mod_tab MAPPING FROM ENTITY.
```

## Variant 3

`UPDATE ... [INDICATORS SET STRUCTURE %control] MAPPING FROM ENTITY.`

### Description

Used to change one or more rows in a [target](../../abap-programming-language/abap-database-access/abapiumd_target.md) based on specifications in a [source](../../abap-programming-language/abap-database-access/abapinsert_source.md). See the detailed syntax options for `...` in the [`UPDATE` topic](../../abap-programming-language/abap-database-access/abapupdate.md).

The sources, i. e. a structure or an internal table, must be typed with the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) [`TYPE STRUCTURE FOR`](abaptype_structure_for.md) and [`TYPE TABLE FOR`](abaptype_table_for.md) respectively. In this case, the types `... FOR UPDATE ...`, `... FOR CREATE ...`, `... FOR DELETE ...`, and `... FOR CHANGE ...` are possible.

The `UPDATE` statement can also be used with the addition [`INDICATORS SET STRUCTURE`](../../abap-programming-language/abap-database-access/abapupdate_set_indicator.md) that includes the [`%control`](abapderived_types_control.md) structure to determine which fields are to be changed.

Currently, this variant is only possible in a context in which the related [RAP behavior definition (BDEF)](../../abap-glossary/abencds_behavior_definition_glosry.md) includes the notation [`persistent table`](../rap-behavior-definitions/abenbdl_persistent_table.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows multiple `UPDATE` statements with the `MAPPING FROM ENTITY` addition.

``` abap
DATA: up_tab TYPE TABLE FOR UPDATE demo_managed_root_map, 
      up_wa  TYPE STRUCTURE FOR UPDATE demo_managed_root_map. 
... 
UPDATE demo_tab_root_3 FROM @up_wa MAPPING FROM ENTITY. 
UPDATE demo_tab_root_3 FROM TABLE @up_tab MAPPING FROM ENTITY. 
UPDATE demo_tab_root_3 FROM @up_wa 
   INDICATORS SET STRUCTURE %control MAPPING FROM ENTITY. 
UPDATE demo_tab_root_3 FROM TABLE @up_tab 
   INDICATORS SET STRUCTURE %control MAPPING FROM ENTITY.
```

## Variant 4

`DELETE ... MAPPING FROM ENTITY.`

### Description

Used to delete one or more rows in a [target](../../abap-programming-language/abap-database-access/abapiumd_target.md) based on the specification in a [source](../../abap-programming-language/abap-database-access/abapinsert_source.md). See the detailed syntax options for `DELETE` in the [`DELETE` topic](../../abap-programming-language/abap-database-access/abapdelete_dbtab.md).

The sources, i. e. a structure or an internal table, must be typed with the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) [`TYPE STRUCTURE FOR`](abaptype_structure_for.md) and [`TYPE TABLE FOR`](abaptype_table_for.md) respectively. In this case, the type `... FOR DELETE ...` is possible.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows multiple `DELETE` statements with the `MAPPING FROM ENTITY` addition.

``` abap
DATA: del_tab TYPE TABLE FOR DELETE demo_managed_root_map, 
      del_wa  TYPE STRUCTURE FOR DELETE demo_managed_root_map. 
... 
DELETE demo_tab_root_3 FROM @del_wa MAPPING FROM ENTITY. 
DELETE demo_tab_root_3 FROM TABLE @del_tab MAPPING FROM ENTITY.
```

### Executable Example

The example [ABAP SQL Statements with the Addition `MAPPING FROM ENTITY`](abensql_mapping_from_entity_abexa.md) demonstrates the different variants.
