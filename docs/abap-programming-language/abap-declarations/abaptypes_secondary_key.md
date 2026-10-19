---
title: "TYPES, secondary_key"
source_file: abaptypes_secondary_key.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES > TYPES, TABLE OF > TYPES, tabkeys"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPES, secondary_key

## Syntax

``` abap
... {UNIQUE HASHED}|{UNIQUE SORTED}|{NON-UNIQUE SORTED}   
    KEY key_name [ALIAS alias_name] COMPONENTS comp1 comp2 ...  
```

### Addition

[`... ALIAS alias_name`](abaptypes_secondary_key.md#addition)

## Overview

### Description

Definition of a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) with an internal table type. An internal table can have up to 15 secondary keys.

**Types of Secondary Keys**

There are three types of secondary keys that are distinguished by the type of access and their uniqueness:

- Unique secondary [hash keys](../../abap-glossary/abenhash_key_glosry.md) defined using `UNIQUE HASHED` that are linked to table lines using a [hash algorithm](../../abap-glossary/abenhash_algorithm_glosry.md).

- Unique secondary [sorted keys](../../abap-glossary/abensorted_key_glosry.md) defined using `UNIQUE SORTED` that are linked to table lines using a [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md) in which the key fields are sorted in ascending order.

- Non-unique secondary [sorted keys](../../abap-glossary/abensorted_key_glosry.md) defined using `NON-UNIQUE SORTED` that are linked to table lines using a [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md) in which the key fields are sorted in ascending order.

**Names of Secondary Keys**

Each secondary key has a unique name with which it can be addressed. The name must be specified directly as `key_name` and must comply with the [naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md). The name specified cannot be one of the predefined names `primary_key` or `loop_key`. In addition, the names of secondary keys and any alias name for the [primary key](abaptypes_primary_key.md) must be unique.

**Key Fields**

The key fields of the secondary key can be defined in the following ways, whereby the order is significant:

- Individual components `comp1 comp2 ...` of the line type are listed after `KEY`. The line type must be structured, and the components cannot be table types nor can they contain table types as components.

- If the whole table line is to be defined as a key, the [pseudo component](../../abap-glossary/abenpseudo_component_glosry.md) `table_line` can be specified as the only component `comp` after `KEY`. This is possible for all line types that are not table types or that do not contain table types as components.

In an operation that changes the content of individual lines of an internal table, the key fields of a secondary table key are read-only only if the secondary key is used during this operation.

### Hints

- When internal tables are accessed using the statements [`READ TABLE itab`](../abap-processing-internal-data/abapread_table.md), [`LOOP AT itab`](../abap-processing-internal-data/abaploop_at_itab.md), [`MODIFY itab`](../abap-processing-internal-data/abapmodify_itab.md), and [`DELETE itab`](../abap-processing-internal-data/abapdelete_itab.md) or in reads using [table expressions](../abap-processing-internal-data/abentable_expressions.md) and in [mesh types](abaptypes_mesh.md) and [mesh paths](../abap-processing-internal-data/abenmesh_pathes.md), a secondary key can be used to determine the lines to be processed or the processing order. To do this, the additions `WITH [TABLE] KEY ... COMPONENTS` or `USING KEY` must be specified. A secondary key is never used implicitly.

- The statement [`INSERT itab`](../abap-processing-internal-data/abapinsert_itab.md) determines the insert position exclusively using the primary key and primary index only. A secondary key can only be specified for the source table from which multiple lines are copied. The latter also applies to the statement [`APPEND`](../abap-processing-internal-data/abapappend.md).

- A secondary key is never generic. When it is defined, all key fields and the uniqueness must be specified completely. An internal table type can, however, be generic with respect to its number of secondary keys.

- [`DEFAULT KEY`](abaptypes_primary_key.md) cannot be specified for secondary keys.

- Structured components can be specified as key fields, provided that the components meet the other requirements. When a structured key field is evaluated, the rules for [structure comparisons](../abap-program-flow-logic/abenlogexp_rules_operands_struc.md) apply.

- If different table keys for an internal table contain the same components, a syntax check warning occurs, which can be hidden using a pragma.

- Apart from the restrictions described above, the names of secondary keys can be freely selected, but they should not use the component names of the internal table. The name `loop_key` is reserved for the explicitly specifying the key used for [`LOOP`](../abap-processing-internal-data/abaploop_at_itab.md) processing.

- Key fields can also have [reference types](../../abap-glossary/abenreference_type_glosry.md). However, particularly for sorted keys this is not recommended, as sorting reference variables is questionable. For non-initial invalid references, no order is defined. A runtime error occurs if such a reference must be compared in the context of a key access.

- The internal management of secondary keys in an internal table can involve significant [memory consumption](../abap-data-types-and-data-objects/abenitab_key_memory.md) and [updates](../abap-data-types-and-data-objects/abenitab_key_secondary_update.md). For this reason, secondary keys should be used sparingly and only be implemented if their benefits outweigh the costs.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of a table type with a primary key and two secondary keys `hash_key` and `sort_key`. The primary key in a standard table must not be unique. The secondary key `hash_key` has the same components as the primary key and must be a unique hash key. The sorted key `sort_key` could also be defined as unique, but this is not beneficial in the example shown here, since a customer ID can appear more than once in the reservation table. The two syntax forms shown here differ in the specification of the name `primary_key` for the primary key, but they have the same meaning.

Syntax form without the name `primary_key` specified:

``` abap
TYPES sbook_tab 
      TYPE STANDARD TABLE 
      OF sbook 
      WITH NON-UNIQUE KEY carrid connid fldate bookid 
      WITH UNIQUE HASHED KEY hash_key 
           COMPONENTS carrid connid fldate bookid 
      WITH NON-UNIQUE SORTED KEY sort_key 
           COMPONENTS customid.
```

Syntax form with the name `primary_key` specified:

``` abap
TYPES sbook_tab 
      TYPE STANDARD TABLE 
      OF sbook 
      WITH NON-UNIQUE KEY primary_key 
           COMPONENTS carrid connid fldate bookid 
      WITH UNIQUE HASHED KEY hash_key 
           COMPONENTS carrid connid fldate bookid 
      WITH NON-UNIQUE SORTED KEY sort_key 
           COMPONENTS customid.
```

## Addition

`... ALIAS alias_name`

### Description

An alias name `alias_name` can be defined for each secondary key of an internal table. The alias name is in the namespace of the secondary key, must comply with the [naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md), and must be unique. It cannot be one of the predefined names `primary_key` or `loop_key`. It enables the secondary key to be addressed by means of an additional user-defined name.

An alias name is part of the technical type properties of a table type. Two table types with otherwise identical technical properties, but different alias names, are not [compatible](../../abap-glossary/abencompatible_glosry.md).

### Hints

- A secondary key with an alias name can be addressed by the alias name `alias_name` as well as by its name `key_name`.

- An alias name can be used when changing the secondary keys of an existing table type in order to avoid the invalidation of existing users.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of a secondary key `carrname` with an alias name `carriername`. Both names can be used in the `USING KEY` addition of a `LOOP` statement.

``` abap
TYPES scarr_tab 
      TYPE HASHED TABLE OF scarr 
      WITH UNIQUE KEY carrid 
      WITH UNIQUE SORTED KEY 
        carrname ALIAS carrier_name COMPONENTS carrname. 
 
DATA carriers TYPE scarr_tab. 
 
... 
 
LOOP AT carriers ASSIGNING FIELD-SYMBOL(<carrier>) 
                 USING KEY carrname. 
  ... 
ENDLOOP. 
 
LOOP AT carriers ASSIGNING <carrier> 
                 USING KEY carrier_name. 
  ... 
ENDLOOP.
```
