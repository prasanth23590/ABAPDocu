---
title: "CDS DDL - DEFINE EXTERNAL ENTITY, element"
source_file: abencds_ee_element.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - External Entities > CDS DDL - DEFINE EXTERNAL ENTITY > CDS DDL - DEFINE EXTERNAL ENTITY, element_list"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE EXTERNAL ENTITY, element

## Syntax

``` abap
... [@element_annot1] 
    [@element_annot2] 
    ... 
    { [KEY] name1 : typing [EXTERNAL NAME ext_name1] [DEFAULT default_value1]; } 
        [ { name2 : typing [EXTERNAL NAME ext_name2]; [DEFAULT default_value|INITIAL] } ] 
        [...]  
```

[`@element_annot1`](abencds_f1_return_list_annotation.md) · [`@element_annot2`](abencds_f1_return_list_annotation.md) · [`typing`](abencds_typing.md) · [`typing`](abencds_typing.md)

### Addition

[1. `... @element_annot`](abencds_ee_element.md#addition-1)

[2. `... KEY`](abencds_ee_element.md#addition-2)

[3. `... DEFAULT`](abencds_ee_element.md#addition-3)

## Overview

### Description

Specifies elements `name1`, `name2`, ... of a [CDS external entity](../../abap-glossary/abencds_external_entity_glosry.md). These elements specify the names of the components of the CDS entity. At least one element must be defined as a key element using the keyword `KEY`. The elements must be assigned a data type that is compatible with the data type of the corresponding element of the remote source. Typing can be done using a [CDS built-in type](../../abap-glossary/abencds_built_in_type_glosry.md), a [DDIC data element](../../abap-glossary/abendata_element_glosry.md), or a [CDS simple type](../../abap-glossary/abencds_simple_type_glosry.md).

The following rules apply:

- The element names `name1`, `name2`, ... can be used when accessing the external entity in ABAP. They must be unique and conform to the naming rules for CDS objects described in the topic about [ABAP CDS - General Syntax Rules](../abap-cds-syntax/abencds_general_syntax_rules.md).

- The element names of the external entity must exactly match the element names of the remote data source. To do this, it is possible to specify an external name `ext_name1`, `ext_name2`, ... using the syntax `EXTERNAL NAME`. These names are case-sensitive and they do not need to conform to the naming rules for CDS objects. They can be escaped using double quotes. This might be useful, for example, if the name contains characters not supported by ABAP.

- The data types of the elements must be compatible with the data types of the elements of the remote database object.

  **Note:** If an element of the remote database object has a boolean data type, the external entity can consume this as `abap.char(1)` with *X* and *' '* as resulting values. **Note:** If an element of the remote database object has the data type `decimal` with length \> 31 or scale \> 14, external entities allow the type adoption `abap.d34n`.

- Each field of the external entity must have a corresponding field in the remote database object. However, not all the fields of the remote database object must be used in the external entity. It is also possible to define only a subset of the fields of the remote database object. The order of the fields is not relevant. Mapping is done implicitly according to the element names.

- An element `name1`, `name2`, ... can optionally be defined as key element using the keyword `KEY`.

- The default value for an element can be defined using the keyword `DEFAULT`.

- Each element must be typed with an elementary data type [`typing`](abencds_typing.md). The rules for typing are described in the topic [CDS DDL - `typing`](abencds_typing.md).

## Addition 1

`... @element_annot`

### Description

Specifies annotations for an element. The annotations can be specified in front of every element using [`@element_annot`](abencds_f1_element_annotation.md). Element annotations can be used to annotate the elements of a CDS external entity with semantic properties.

## Addition 2

`... KEY`

### Description

`KEY` is used to define the current element as a key element of the current CDS external entity. Those elements of the [element list](abencds_ee_elem_list.md) can be defined as key elements that are placed at the beginning of the list without gaps. At least the first element **must** be a key element. The primary key of an external entity does not have to match the primary key of the remote data source.

**Caution**

The key elements of a CDS entity do not define unique lines in its result with regard to the key. An application or framework accessing a CDS entity must expect duplicate entries for the key fields in the result set. If the lines of a result set should be unique in respect to a set of key elements, it is the task of the application or framework that provides the CDS entity to define them appropriately and to document the view accordingly.

## Addition 3

`... DEFAULT`

### Description

`DEFAULT` can be used to specify a default value for an element. The default value is returned when there is no matching element name in the remote data source. Note that the matching mechanism is case-sensitive. If a remote element with the same name exists, the `DEFAULT` clause is ignored.

Default values are handled as [typed literals](../../abap-programming-language/abap-database-access/abenabap_sql_typed_literals.md) (except for enumerated constants). The type is taken from the definition of the element, as in the following examples:

- `f1 : abap.int4 default 1`: The default value type is interpreted as `abap.int4`1\`\`.

- `f2 : abap.char(5) default 'A'`: The default value type is interpreted as `abap.char`A\`\`.

The following rules apply:

- Default values of character-like types must be written in single quotes.

- Default values of numeric types must be written without quotes.

### Hint

The default values must comply with the defined type of the element and be within the value range of the data type. Therefore, examples such as the following result in syntax errors:

- `f1 : abap.char(3) DEFAULT '1234'` =\> error

- `f1 : abap.dec(4,2) DEFAULT 1.234` =\> error

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following simplified example illustrates some uses of `DEFAULT`:

``` abap
define external entity ... 
{ 
key key1 : abap.char(10)                          DEFAULT 'ABC'; 
    field1 : abap.dec(10,5)                       DEFAULT 123.12345; 
    field2 : abap.char(10) EXTERNAL NAME ext_name DEFAULT 'ABC'; 
} 
...
```
