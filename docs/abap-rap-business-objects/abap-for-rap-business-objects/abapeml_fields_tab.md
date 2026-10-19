---
title: "ABAP EML - fields_tab"
source_file: abapeml_fields_tab.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > ABAP EML - Common EML Statements and Operands"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - fields_tab

Internal table that is typed with the required [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) (`TYPE TABLE FOR ...`) containing specific components for the communication between a [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) and [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md). The components are determined by the context in which the internal table is used, i. e. the use and number of the components of the internal table to be specified, for example, for a delete or create operation differ. See the details of the type ([`TYPE TABLE FOR`](abaptype_table_for.md)) and components ([Components of Derived Types](abapderived_types_comp.md)) in the respective documentation.

The internal table can be constructed in an [operand position](../../abap-glossary/abenoperand_position_glosry.md) using [constructor expressions](../../abap-glossary/abenconstructor_expression_glosry.md), for example with the [value operator](../../abap-glossary/abenvalue_operator_glosry.md) (`VALUE`) and other [constructor operators](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenconstructor_expressions.md) to fill the internal table with instances as input parameters after the respective keyword (for example, `FROM`).

## Hint

If a field of a parent or child entity is marked as `readonly` in the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md), it cannot be changed and assigned a new value with any of the [modify operations](../../abap-glossary/abenrap_modify_operation_glosry.md). A modification can only be done using the addition `IN LOCAL MODE`. See more details in the documentation for [`IN LOCAL MODE`](abapin_local_mode.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following code example shows an internal table that is explicitly declared with a BDEF derived type. It is then used in a `MODIFY` statement (assuming that `create_root` contains values). This is also true for the second example. Yet, the internal table following the statement `CREATE SET FIELDS WITH` is declared inline using the value operator.

``` abap
... 
DATA create_root TYPE TABLE FOR CREATE demo_managed_root. 
 
MODIFY ENTITY demo_managed_root 
    CREATE SET FIELDS WITH create_root. 
 
... 
 
MODIFY ENTITY demo_managed_root 
    CREATE SET FIELDS WITH VALUE 
      #( ( %cid = 'cid1' key_field = '1' data_field1_root = 'aaa' 
           data_field2_root = 'bbb') 
         ( %cid = 'cid2' key_field = '2' data_field1_root = 'ccc' 
           data_field2_root = 'ddd') 
       ). 
...
```
