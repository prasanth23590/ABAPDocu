---
title: "itab - Standard Key"
source_file: abenitab_standard_key.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > Internal Tables > itab - Table Key > itab - Primary Table Key"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Standard Key

The standard key is a special [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) of an internal table.

- [Key Fields of the Standard Key](abenitab_standard_key.md#key-fields-of-the-standard-key)

- [Declaration of the Standard Key](abenitab_standard_key.md#declaration-of-the-standard-key)

- [Notes on Use](abenitab_standard_key.md#notes-on-use)

## Key Fields of the Standard Key

The key fields of the standard key are defined as follows:

- In tables with a structured line type, the standard key is formed from all components with [character-like](../../abap-glossary/abencharlike_data_type_glosry.md) and [byte-like data types](../../abap-glossary/abenbyte_like_data_typ_glosry.md), while resolving any substructures into elementary components. If the line type does not contain any components like these, the standard key is [empty](abenitab_empty_key.md) for standard tables, meaning it does not contain any key fields.

- The standard key for tables with non-structured line types is the entire table line, if the line type itself is not table-like. If the line type is table-like, the standard key is [empty](abenitab_empty_key.md) for standard tables.

Empty standard keys are not possible for sorted tables and hashed tables, and an error occurs if an attempt is made to create a key like this.

### Hints

- In tables with non-structured line types, the standard key can also have a numeric type or reference type. This does not apply to the key fields if the line types are structured.

- The [static boxes](../../abap-glossary/abenstatic_box_glosry.md) of a structured line type are handled like regular components with respect to the standard key.

## Declaration of the Standard Key

The standard key can be declared as follows:

- Explicitly, using the additions [`UNIQUE|NON-UNIQUE KEY`](../abap-declarations/abaptypes_primary_key.md) of the statements [`TYPES`](../abap-declarations/abaptypes_primary_key.md), [`DATA`](../abap-declarations/abapdata_primary_key.md) and so on, where the addition `DEFAULT KEY` is specified instead of the list of components.

- Implicitly, if no explicit primary key specification is made in the declaration of a standard table with the statement [`DATA`](../abap-declarations/abapdata_primary_key.md).

- Implicitly, if a standard table type with a [generic primary table key](../abap-declarations/abaptypes_keydef.md) is specified behind `TYPE` in the statement [`DATA`](../abap-declarations/abapdata_referring.md).

## Notes on Use

Using standard keys is critical for the following reasons:

- It is not usually enough to identify the key fields using their data type and not their semantic properties. This often leads to unexpected behavior in sorts and other accesses.

- The fact that standard keys in standard tables can be [empty](abenitab_empty_key.md) often causes unexpected behavior as well. For example, using keys like this for [sorting](../abap-processing-internal-data/abapsort_itab.md) has no effect, whereas a corresponding [read](../abap-processing-internal-data/abapread_table.md) finds the first line.

- The standard key often contains too many key fields, which can produce performance problems in key accesses.

- If using the standard key and a structured line type, all character-like and byte-like fields of sorted tables and hashed tables are read-only, which can cause unexpected runtime errors.

For this reason, the primary key should be declared by listing the components explicitly, if possible. In particular, the primary key must not be set as the standard key by mistake, the key must not be forgotten in declarations of standard tables using `DATA`, and the generic table type must not be used unknowingly.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Internal table with standard key. In the structure `SCARR`, all five components meet the requirements for the standard key and are used as key fields. In a key access using a [table expression](../../abap-glossary/abentable_expression_glosry.md), the syntax check requires that each key field of the primary table key is specified.

``` abap
DATA scarr_tab 
  TYPE HASHED TABLE OF scarr 
       WITH UNIQUE DEFAULT KEY. 
 
... 
 
FINAL(scarr_line) = 
  VALUE #( scarr_tab[ KEY primary_key 
                      mandt    = sy-mandt 
                      carrid   = '...' 
                      carrname = '...' 
                      currcode = '...' 
                      url      = '...' ] OPTIONAL ).
```
