---
title: "%chg"
source_file: abapderived_types_chg.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Miscellaneous Components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %chg

## Use

`%chg` is a [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) component, providing information on accumulated change operation information for [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) within a [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md), that is, the value of `%chg` indicates whether the operations performed on instances are, for example, create, update or delete operations.

The component is used in the following contexts:

- Read results of ABAP EML `READ` statements using the [`WITH CHANGES`](abapeml_read_with_changes.md) addition. The possible `%chg` values are outlined in the table below. **Note:** For [RAP draft instances](../../abap-glossary/abenrap_draft_instance_glosry.md), the `%chg` value refers to the accumulated operations on the associated active instance.

- [RAP BO draft actions](../../abap-glossary/abenrap_bo_draft_action_glosry.md) that are specified with `additionalsave` in the [BDEF](../../abap-glossary/abencds_entity_bdef_glosry.md). Here, the values can be specified using the structured constant outlined in the following table can be used: `if_abap_behv=>cop-create`, `if_abap_behv=>cop-update`, and `if_abap_behv=>cop-delete`.

The structured constant `cop` of the interface `IF_ABAP_BEHV` is used to specify the value for `%chg`:

| **Component** | **Value** | **Description**                                                                                                                                                                                                                                      |
|---------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `create`      | `C`       | The instance is created in the current RAP transaction and has not existed before.                                                                                                                                                                   |
| `update`      | `U`       | The instance has existed before and is modified in the current RAP transaction.                                                                                                                                                                      |
| `delete`      | `D`       | The instance has existed before and is removed in the current RAP transaction.                                                                                                                                                                       |
| `recreate`    | `R`       | The instance has existed before, is deleted, and then created again in the current RAP transaction.                                                                                                                                                  |
| `redelete`    | `L`       | The instance has not existed before, is created, and then deleted again in the current transaction. This is only relevant when a RAP BO has child entities, and the child entities are operated in [draft](../../abap-glossary/abenrap_draft_handling_glosry.md) mode. |
| `unchanged`   | `N`       | The instance has existed before and remains unchanged in the current RAP transaction.                                                                                                                                                                |

**Type**

The components are typed with `ABP_BEHV_MNGD_OP`.

**Where used**

This component can occur in the following type declarations of [`TYPE TABLE FOR ...`](abaptype_table_for.md) and [`TYPE STRUCTURE FOR ...`](abaptype_structure_for.md):

- `READ CHANGES`

The component can also be used in the method implementation [`... FOR MODIFY ... ACTION bdef~additionalsave ...`](abaphandler_meth_modify.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code snippet shows how accumulated changes may be processed in the implementation of method [`... FOR MODIFY ... ACTION bdef~additionalsave ...`](abaphandler_meth_modify.md).

``` abap
CLASS lhc_bdef DEFINITION INHERITING FROM cl_abap_behavior_handler. 
  PRIVATE SECTION. 
    ... 
    METHODS additionalsave FOR MODIFY 
      IMPORTING keys FOR ACTION bdef~additionalsave. 
    ... 
ENDCLASS. 
 
CLASS lhc_bdef IMPLEMENTATION. 
  ... 
  METHOD additionalsave. 
    ... 
    LOOP AT keys INTO DATA(key). 
      ... 
      LOOP AT key-%param-some_entity INTO DATA(k). 
        IF k-%chg = if_abap_behv=>cop-create. 
          ... 
        ENDIF. 
        IF k-%chg = if_abap_behv=>cop-update. 
          ... 
        ENDIF. 
        IF k-%chg = if_abap_behv=>cop-delete. 
          ... 
        ENDIF. 
      ENDLOOP. 
    ... 
    ENDLOOP. 
    ... 
  ENDMETHOD. 
  ... 
ENDCLASS.
```
