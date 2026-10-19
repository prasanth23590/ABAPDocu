---
title: "TYPES, key"
source_file: abaptypes_primary_key.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES > TYPES, TABLE OF > TYPES, tabkeys"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPES, key

## Syntax

``` abap
... { [UNIQUE | NON-UNIQUE]   
      { {KEY [primary_key [ALIAS alias_name] COMPONENTS] comp1 comp2 ...}   
      | {DEFAULT KEY} }  }   
  | { EMPTY KEY } ...  
```

### Alternative

[1. `... [UNIQUE|NON-UNIQUE] {KEY ...}|{DEFAULT KEY}`](abaptypes_primary_key.md#alternative-1)

[2. `... EMPTY KEY`](abaptypes_primary_key.md#alternative-2)

## Alternative 1

`... [UNIQUE|NON-UNIQUE] {KEY ...}|{DEFAULT KEY}`

### Addition

[1. ` ... primary_key COMPONENTS`](abaptypes_primary_key.md#addition-1)

[2. `... ALIAS alias_name`](abaptypes_primary_key.md#addition-2)

### Description

Definition of the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) of a table type by specifying components or by specifying it as a standard key.

**Name of the Primary Key**

Like [secondary keys](abaptypes_secondary_key.md), the primary key also has a name with which it can be addressed. This name cannot be freely selected and is specified as `primary_key` instead. It does not have to be explicitly specified when the table is defined since it is always set implicitly. However, it can also be specified before the addition `COMPONENTS`.

**Key Fields**

The key fields of the primary key can be defined in the following ways, whereby the order is significant:

- Individual components `comp1 comp2 ...` of the line type are listed after `KEY`. The line type must be structured, and the components cannot be table types, nor can they contain table types as components. For elementary line types, `table_line` is the only component that can be specified.

- If the whole table line is to be defined as a key, the [pseudo component](../../abap-glossary/abenpseudo_component_glosry.md) `table_line` can be specified as the only component `comp` after `KEY`. This is possible for all line types that are not table types or that do not contain table types as components. For structured line types, `table_line` works like a listing of each individual component.

- Specification of the [standard key](../../abap-glossary/abenstandard_key_glosry.md) `DEFAULT KEY`. The standard key fields of a structured line type are all fields with a non-numeric elementary data type. The standard key for non-structured line types is the entire table line if the line type itself is not a table type. If there is no corresponding component or if the line type is itself a table type, the standard key is [empty](../abap-data-types-and-data-objects/abenitab_empty_key.md), which is only possible for standard tables.

The key fields of the primary table key are generally read-only in all operations that change the content of individual lines of a sorted table or hashed table.

**Uniqueness of the Primary Key**

The specifications `UNIQUE` or `NON-UNIQUE` determine the uniqueness of the primary table key. In the case of a primary table key specified with `UNIQUE`, a line with specific content of the key fields can occur only once in an internal table of this type. Only `NON-UNIQUE` can be used for [standard tables](../../abap-glossary/abenstandard_table_glosry.md). `UNIQUE` must be used for [hashed tables](../../abap-glossary/abenhashed_table_glosry.md) and both can be specified for [sorted tables](../../abap-glossary/abensorted_table_glosry.md).

Uniqueness does not have to be specified, which makes the table type partially generic with respect to the entry of the primary key. The table type can then only be used for [typing](../../abap-glossary/abentyping_glosry.md) of formal parameters or field symbols. The table categories differ as follows:

- The addition `NON-UNIQUE` is added implicitly for types for standard tables. A standard table is never generic with respect to uniqueness.

- Types for sorted tables can be completely generic with respect to uniqueness.

- Types for hashed tables can be completely generic with respect to uniqueness, but a concrete hashed table always has a unique primary key.

- Uniqueness cannot be specified for the generic table categories `ANY TABLE` or `INDEX TABLE`.

### Hints

- The declaration of the primary table key as a [standard key](../../abap-glossary/abenstandard_key_glosry.md) can be [critical](../abap-data-types-and-data-objects/abenitab_standard_key.md) for various reasons. Instead, key fields should be specified explicitly.

- Structured components can be explicitly specified when specifying key fields, provided that the components meet the other requirements. When a structured key field is evaluated, the rules for [structure comparisons](../abap-program-flow-logic/abenlogexp_rules_operands_struc.md) apply.

- Key fields can also have [reference types](../../abap-glossary/abenreference_type_glosry.md). However, this is not recommended particularly for sorted keys, since sorting reference variables is questionable. For non-initial invalid references, no order is defined. A runtime error occurs if such a reference must be compared in the context of a key access.

- The addition `DEFAULT KEY` must not be confused with the addition `EMPTY KEY`. A standard key declared using the addition `DEFAULT KEY` can be [empty](../abap-data-types-and-data-objects/abenitab_empty_key.md) unexpectedly in a standard table, whereas `EMPTY KEY` declares explicitly empty primary table keys explicitly for tables with any line types.

- [Static boxes](../../abap-glossary/abenstatic_box_glosry.md) and their components can be key fields of internal tables.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example contains internal table declarations with different primary table key definitions. In some cases, concretely specified components or an `ALIAS` addition is used.

``` abap
TYPES: BEGIN OF ts_example, 
             component_1 TYPE i, 
             component_2 TYPE string, 
             component_3 TYPE c LENGTH 10, 
           END OF ts_example. 
 
"UNIQUE KEY 
"UNIQUE KEY with explicit component list 
DATA itab_1 TYPE SORTED TABLE OF ts_example 
      WITH UNIQUE KEY component_1. 
"UNIQUE KEY with named primary key without ALIAS 
DATA itab_2 TYPE SORTED TABLE OF ts_example 
      WITH UNIQUE KEY primary_key COMPONENTS component_1. 
"UNIQUE KEY with named primary key with ALIAS 
DATA itab_3 TYPE SORTED TABLE OF ts_example 
      WITH UNIQUE KEY primary_key 
      ALIAS alias_name COMPONENTS component_1 component_3. 
"UNIQUE KEY with a hashed table type 
"with named primary key without ALIAS 
DATA itab_4 TYPE HASHED TABLE OF ts_example 
      WITH UNIQUE KEY primary_key 
      COMPONENTS component_1 component_2. 
 
"NON-UNIQUE KEY 
"NON-UNIQUE KEY with explicit component list 
DATA itab_5  TYPE STANDARD TABLE OF ts_example 
      WITH NON-UNIQUE KEY component_1. 
"NON-UNIQUE KEY with named primary key without ALIAS 
DATA itab_6 TYPE STANDARD TABLE OF ts_example 
      WITH NON-UNIQUE KEY primary_key COMPONENTS component_2. 
"NON-UNIQUE KEY with named primary key with ALIAS 
DATA itab_7 TYPE SORTED TABLE OF ts_example 
      WITH NON-UNIQUE KEY primary_key 
      ALIAS alias_name COMPONENTS component_1 component_2 component_3. 
"NON-UNIQUE DEFAULT KEY 
DATA itab_8 TYPE STANDARD TABLE OF ts_example 
      WITH NON-UNIQUE DEFAULT KEY. 
 
"DEFAULT KEY 
"UNIQUE DEFAULT KEY 
DATA itab_9 TYPE SORTED TABLE OF ts_example 
      WITH UNIQUE DEFAULT KEY. 
 
"EMPTY KEY 
DATA itab_10 TYPE STANDARD TABLE OF ts_example WITH EMPTY KEY.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of a primary key without explicit name specification. The statement has the same meaning as in the following example.

``` abap
TYPES sbook_tab 
      TYPE SORTED TABLE 
      OF sbook 
      WITH UNIQUE KEY carrid connid fldate bookid.
```

## Addition 1

` ... primary_key COMPONENTS`

### Description

If the key fields are defined by specifying components, the name of the primary key can be specified explicitly in the statement `TYPES`. However, the predefined name `primary_key` must be specified for `primary_key`. The addition `COMPONENTS` must then also be specified before the component is specified.

### Hint

Explicitly specifying the name `primary_key` does not enable the predefined name `primary_key` to be changed but enables an alias name to be specified using the addition `ALIAS`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of a primary key with explicit name specification. The statement has the same meaning as in the previous example.

``` abap
TYPES sbook_tab 
      TYPE SORTED TABLE 
      OF sbook 
      WITH UNIQUE KEY primary_key 
           COMPONENTS carrid connid fldate bookid.
```

## Addition 2

`... ALIAS alias_name`

### Description

An alias name `alias_name` can be defined for the primary key in sorted tables and hashed tables, for as long as the primary key is not generic. The alias name is in the namespace of the secondary key, must comply with the [naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md), and must be unique. It cannot be one of the predefined names `primary_key` or `loop_key`. It enables the primary key to be addressed like a secondary key by means of a user-defined name. The syntax requires the name `primary_key` to be specified explicitly when defining an alias name.

An alias name is part of the technical type properties of a table type. Two table types with otherwise identical technical properties, but different alias names, are not [compatible](../../abap-glossary/abencompatible_glosry.md).

### Hint

A primary key with an alias name can be addressed by the alias name `alias_name` as well as by the predefined name `primary_key`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of a primary key with an explicit name specification and its use in a [table expression](../../abap-glossary/abentable_expression_glosry.md).

``` abap
TYPES sbook_tab 
      TYPE SORTED TABLE 
      OF sbook 
      WITH UNIQUE KEY primary_key ALIAS full_table_key 
           COMPONENTS carrid connid fldate bookid. 
 
DATA bookings TYPE sbook_tab. 
 
FINAL(customid) = bookings[ KEY full_table_key COMPONENTS 
                               carrid = 'LH' 
                               connid = '400' 
                               fldate = '20240905' 
                               bookid = '12345678'  ]-customid.
```

## Alternative 2

`... EMPTY KEY`

### Description

Definition of an [empty primary key](../abap-data-types-and-data-objects/abenitab_empty_key.md) of a table type. This variant is only possible for standard tables. An empty table key does not contain any key fields.

### Hints

- When an empty table key is defined explicitly, this means that the internal table is to be handled like an array in which there is no order specified by key values.

- The order of a standard table with an empty primary key is determined primarily by the [primary index](../../abap-glossary/abenprimary_table_index_glosry.md). There are no restrictions on related index accesses and loop processing.

- In statements that evaluate the primary table key to identify lines to be processed, an empty table key generally produces unexpected behavior and therefore a syntax check warning. For a list of these statements, see [Empty Table Key](../abap-data-types-and-data-objects/abenitab_empty_key.md).

- A table key where `EMPTY KEY` is used to declare an empty table key explicitly is not generic with respect to its primary key. This means that the addition `EMPTY KEY` can be used to prevent a table type from being too generic with respect to its primary key.

- The explicit declaration of an empty table key using `EMPTY KEY` is independent of the line type.

- A standard table with an empty primary key can have non-empty [secondary keys](../../abap-glossary/abensecondary_key_glosry.md).

- Empty table keys can also be created implicitly when the [standard key](../abap-data-types-and-data-objects/abenitab_standard_key.md) is used for standard tables. If an empty table key is required, it is preferable to declare it explicitly using `EMPTY KEY`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The table in the example below is only intended for loop processing in which all lines of the table are processed in a random order.

``` abap
CLASS mail_manager DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS send 
      IMPORTING 
        address TYPE s_email 
        text    TYPE string. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS mail_manager IMPLEMENTATION. 
  METHOD send. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    TYPES addresses TYPE STANDARD TABLE OF scustom-email WITH EMPTY KEY. 
 
    DATA  email_tab TYPE addresses. 
 
    FIELD-SYMBOLS <email> LIKE LINE OF email_tab. 
 
    ... 
 
    SELECT email 
           FROM scustom 
           INTO TABLE @email_tab. 
    ... 
 
    LOOP AT email_tab ASSIGNING <email> USING KEY primary_key. 
      mail_manager=>send( address = <email> text = `text` ). 
    ENDLOOP. 
  ENDMETHOD. 
ENDCLASS.
```
