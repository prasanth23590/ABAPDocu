---
title: "DDIC - Quantity Fields"
source_file: abenddic_quantity_field.html
section: "ABAP Dictionary (DDIC) > DDIC - Built-In Data Types > DDIC - Properties of the Built-In Dictionary Types > DDIC - Special Dictionary Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Quantity Fields

A quantity field is a component of a DDIC structure, DDIC database table, or DDIC view used to store a quantity in a specific unit. A quantity field can have data type `QUAN`, `DECFLOAT16`, or `DECFLOAT34`. In case of data type `QUAN`, a field is automatically interpreted as quantity field and a reference to a unit key is mandatory. In case of the other data types, this reference is not mandatory, but if it is assigned, it turns the field into a quantity field.

The unit key defines the unit and the number of decimal places. It is a component of a DDIC structure, DDIC database table, or DDIC view of type `UNIT` and can contain a [unit ID](../../abap-glossary/abenunit_id_glosry.md) from the DDIC database table `T006`.

- [Handling in ABAP Dictionary](abenddic_quantity_field.md#handling-in-abap-dictionary)

- [Handling in ABAP Programs](abenddic_quantity_field.md#handling-in-abap-programs)

## Hints

- Quantities and units are handled as specified by the data saved in the DDIC database tables `T006...` in the package `SZME`. This data can be maintained using the transaction `CUNI`.

- Quantity fields in ABAP CDS are described in topic [ABAP CDS - Quantity Fields](../../abap-core-data-services-abap-cds/abap-cds-data-types/abencds_quantity_field.md).

## Handling in ABAP Dictionary

A data element of data type [`QUAN`](abenddic_builtin_types.md) is handled as a field of data type [`DEC`](abenddic_builtin_types_int_pack.md) and is stored in DDIC database tables in the [BCD](../../abap-glossary/abenbcd_glosry.md) format. When creating a data element or a structure component of the data type `QUAN` in an ABAP Dictionary tool, any number of decimal places can be defined. The default value is no decimal places.

A quantity field of data type `DECFLOAT16` or `DECFLOAT34` is handled according to its data type.

For every structure component of data type `QUAN`, a component of the same structure or of a different structure, DDIC database table, or DDIC view must be defined as a [reference field](../ddic-data-types/abenddic_structures_sema.md) with the data type [`UNIT`](abenddic_builtin_types.md). This field is the [unit key](../../abap-glossary/abenunit_glosry.md) that defines the unit of the quantity. From a technical perspective, the data type `UNIT` is handled like a type `CHAR` with length 2.

### Hints

- As in [general packed numbers](abenddic_builtin_types_int_pack.md), the number of places in type `QUAN` should be odd.

## Handling in ABAP Programs

The ABAP type that corresponds to the data type `QUAN` is `p`. An ABAP data object declared with reference to a dictionary type of type `QUAN` has the number of decimal places defined there. These decimal places are respected for all operations and calculations, as for all packed numbers. When quantity currency fields with [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), no special handling takes place.

The unit defined for a quantity field only plays a part in ABAP programs if it is specified after the addition `UNIT` of the statement `WRITE [TO]`. The addition `UNIT` of the statement `WRITE [TO]` can be used only for quantity fields of data type `QUAN`, not for quantity fields of any other data type.
