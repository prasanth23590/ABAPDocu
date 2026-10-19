---
title: "C1 Contract Rules for Consuming Elementary Types"
source_file: abenc1_consumer_rules_elem.html
section: "ABAP APIs > Release Contracts > Contract Rules for API Consumers"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# C1 Contract Rules for Consuming Elementary Types

The data type of

- DDIC domains or DDIC data elements

- components of DDIC structures and DDIC database tables or elements of CDS entities

- public types of global ABAP classes or interfaces

are allowed to be changed by the API provider as follows:

- Integer types `INT1`, `INT2`, and `INT4` or `b`, `s`, and `i` can be replaced by integer types of a larger value range.

- The length of data types `CHAR`, `SSTRING`, `DEC`, `CURR`, `QUAN`, `DF16_DEC`, `DF34_DEC` or `c`, `p` can be increased.

- The number of decimal places of data types `DEC`, `CURR`, `QUAN`, `DF16_DEC`, `DF34_DEC` or `p` can be increased.

All these changes result in a larger value range compared with the original data type. A consumer must be able to handle larger values. This impacts all operations with elementary data objects that are typed with such a type as well as operations with structured data that contain components of such a type.

- [Operations with Elementary Data Objects](abenc1_consumer_rules_elem.md#operations-with-elementary-data-objects)

- [Operations with Structures](abenc1_consumer_rules_elem.md#operations-with-structures)

## Operations with Elementary Data Objects

When working with elementary data objects of one of the above types the behavior after an allowed type change depends on the type, the operand position and the content.

**Possible Problems**

Examples for possible problems are:

- In assignments of data objects that have a changed type to data objects whose type is not changed, content can be cut off or overflow exceptions may occur.

- In statements that require compatible data types, syntax errors can occur. Examples are:

  - Assignments between [data reference variables](../../abap-glossary/abendata_reference_variable_glosry.md).

  - Access to internal tables with an elementary line type using a table key.

  - Importing data from data clusters with [`IMPORT`](../../abap-programming-language/abap-data-cluster/abapimport_data_cluster.md).

- In statements that require lossless assignments, exceptions can occur. Examples are:

  - [Lossless operator `EXACT`](../../abap-programming-language/abap-processing-internal-data/abenconstructor_expression_exact.md)

  - [Host variables](../../abap-programming-language/abap-database-access/abenabap_sql_host_variables.md) in read position ABAP SQL.

**Mitigation**

When declaring data objects, always refer to the released data types themselves. Do not refer to user-defined types. Use data objects referring to released types only at operand positions where changing the type cannot produce an error.

## Operations with Structures

Changing the data type of a component of a structure changes the [technical type](../../abap-glossary/abentechnical_type_prpt_glosry.md) of the complete structure. This has a large impact since there are many operand positions, where compatibility is required for structures and generally, the same errors can occur that result from changing the elements of structures described below and the same mitigations apply.
