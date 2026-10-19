---
title: "TYPES, tabkeys"
source_file: abaptypes_keydef.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES > TYPES, TABLE OF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPES, tabkeys

## Syntax

``` abap
... [ WITH key ]   
    [ WITH secondary_key1 ] [ WITH secondary_key2 ] ...   
    [ {WITH|WITHOUT} FURTHER SECONDARY KEYS ] ...  
```

[`key`](abaptypes_primary_key.md) · [`secondary_key1`](abaptypes_secondary_key.md) · [`secondary_key2`](abaptypes_secondary_key.md)

### Addition

[1. `... WITH FURTHER SECONDARY KEYS`](abaptypes_keydef.md#addition-1)

[2. `... WITHOUT FURTHER SECONDARY KEYS`](abaptypes_keydef.md#addition-2)

## Overview

### Description

Definition of the table key of a table type. The following can be defined:

- A [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) using [`key`](abaptypes_primary_key.md)

- Up to 15 [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md) using [`secondary_key1`](abaptypes_secondary_key.md), [`secondary_key2`](abaptypes_secondary_key.md), `...`

The order in which the components of a table key are defined is significant for the table type. The additions `WITH|WITHOUT FURTHER SECONDARY KEYS` determine the genericness with respect to the secondary table key.

An internal table type that has no table key or an incomplete table key is generic with respect to the table key. Such a table type can only be used for [typing](../../abap-glossary/abentyping_glosry.md) formal parameters or field symbols. A standard table type with a generic primary table key only can be specified for [`DATA`](abapdata_referring.md) after `TYPE`. This creates a bound table type with a [standard key](../../abap-glossary/abenstandard_key_glosry.md).

**Primary Key**

The genericity of a table type with respect to the primary key is determined as follows:

- If WITH [`key`](abaptypes_primary_key.md) is not specified, a table type is fully generic with respect to the primary key.

- If there is no declaration about the uniqueness of the key in [`key`](abaptypes_primary_key.md), a table type is partly generic with respect to the key.

- If a key declaration with a uniqueness declaration is made in [`key`](abaptypes_primary_key.md), a table type is not generic with respect to the primary key.

The non-generic table categories can be split up as follows:

- If no primary key is declared for standard tables, this primary key is generic with respect to the key fields and defined implicitly as non-unique.

- If no primary key is declared for sorted tables, this primary key is generic with respect to the key fields and uniqueness.

- If no primary key is declared for hashed tables, this primary key is generic with respect to the key fields and uniqueness. However, it is important to note that concrete hashed tables can have only one unique key.

**Secondary Key**

The genericity of a table type with respect to the secondary keys depends on that of the primary key by default and can be overridden using the additions `WITH|WITHOUT FURTHER SECONDARY KEYS`.

- If the primary key is completely or partially generic, the table type is by default generic with respect to the secondary keys. The default behavior can be expressed using the addition `WITH FURTHER SECONDARY KEYS`. However, if the addition `WITHOUT FURTHER SECONDARY KEYS` is specified, the table type is generic with respect to the primary key but not with respect to the secondary key.

- If the primary key is not generic, then the table type is by default not generic with respect to the secondary key either. The default behavior can be expressed using the addition `WITHOUT FURTHER SECONDARY KEYS`. However, if the addition `WITH FURTHER SECONDARY KEYS` is specified, the table type is generic with respect to the secondary key but not with respect to the primary key.

### Hint

A generic table type must not be used as a component of a [structured type](abaptypes_struc.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of a table type for a [hashed table](../../abap-glossary/abenhashed_table_glosry.md) with a unique primary key as well as two non-unique secondary [sorted keys](../../abap-glossary/abensorted_key_glosry.md), `cityfrom_to` and `airp_from_to`.

``` abap
TYPES spfli_tab TYPE HASHED TABLE OF spfli 
  WITH UNIQUE KEY            carrid connid 
  WITH NON-UNIQUE SORTED KEY cityfrom_to  COMPONENTS cityfrom cityto 
  WITH NON-UNIQUE SORTED KEY airp_from_to COMPONENTS airpfrom airpto.
```

## Addition 1

`... WITH FURTHER SECONDARY KEYS`

### Description

This addition explicitly specifies that the table type is generic with respect to the secondary key. This means that it includes table types that can have further secondary keys in addition to the optional secondary keys specified using WITH [`secondary_key`](abaptypes_secondary_key.md) ....

If 15 secondary keys are already defined, the addition `WITH FURTHER SECONDARY KEYS` cannot be specified.

### Hints

- This addition expresses the default behavior in table types with a generic primary key.

- In table types with a non-generic primary key, `WITH FURTHER SECONDARY KEYS` can be used to override the default behavior and make it generic with respect to the secondary keys.

## Addition 2

`... WITHOUT FURTHER SECONDARY KEYS`

### Description

This addition explicitly specifies that the table type is not generic with respect to the secondary key. This means that it includes only table types that have exactly those secondary keys specified using WITH [`secondary_key`](abaptypes_secondary_key.md) ....

### Hint

This addition expresses the default behavior in table types with a generic primary key.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The addition `WITH FURTHER SECONDARY KEYS` in the declaration of the tabular type `itab` enables the passing of internal tables with any secondary keys to the parameter `p` of the method `meth`. Without this addition, the addition `WITHOUT FURTHER SECONDARY KEYS` would be used implicitly and the method call shown would not be possible.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    TYPES itab TYPE SORTED TABLE OF scarr 
               WITH UNIQUE KEY carrid 
               WITH FURTHER SECONDARY KEYS. 
    CLASS-METHODS meth IMPORTING p TYPE itab. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD meth. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA itab TYPE SORTED TABLE OF scarr 
              WITH UNIQUE KEY carrid 
              WITH NON-UNIQUE SORTED KEY name COMPONENTS carrname. 
 
    demo=>meth( itab ). 
  ENDMETHOD. 
ENDCLASS.
```
