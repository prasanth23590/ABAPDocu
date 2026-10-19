---
title: "itab - keyname"
source_file: abenkeyname.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - keyname

The name of the [table key](../../abap-glossary/abentable_key_glosry.md) can be specified in a range of statements and in table expressions for the processing of internal tables. The table key name can used to access a table line or to control processing. The following syntax applies to `keyname`:

## Syntax

``` abap
... key_name | (name)  ...  
```

## Description

The name of a table key can either be specified directly, as `key_name`, or dynamically, as the content of a parenthesized character-like data object `name`. This is not case-sensitive. If the name is specified directly, it must be known statically that the internal table has this key. With generic data types, the name can only be specified dynamically. If the name is specified dynamically and is incorrect, this raises an uncatchable exception.

The following can be specified:

- a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) using its name

- the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) using its predefined name `primary_key`

- the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) using an alias

- the table key used in a [`LOOP`](abaploop_at_itab_cond.md)-loop using its predefined name `loop_key`. In this case, the statement must be executed within the loop.

## Hints

- Normally secondary table keys are specified. Only if [searches](abentable_exp_itab_line.md) are to be performed explicitly in a [table expression](abentable_expressions.md) using the primary table key does the key need be specified using its predefined name `primary_key` or an alias name.

- When specifying the primary table key using `primary_key`, it is important to note that it can also be [empty](../abap-data-types-and-data-objects/abenitab_empty_key.md) for standard tables. This can produce unexpected behavior in statements where the key is used to specify the lines to be processed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Dynamic specification of the key according to which the `LOOP` loop is executed. The loop can be executed with the entries `skey` and `primary_key`. This is not case sensitive. Any other entries produce a runtime error.

``` abap
DATA(key) = `skey`. 
cl_demo_input=>request( CHANGING field = key ). 
 
DATA itab TYPE TABLE OF i 
          WITH NON-UNIQUE KEY primary_key COMPONENTS table_line 
          WITH NON-UNIQUE SORTED KEY skey COMPONENTS table_line. 
 
itab = VALUE #( ( 3 ) ( 2 ) ( 1 ) ). 
 
LOOP AT itab INTO FINAL(wa) USING KEY (key). 
  cl_demo_output=>write( wa ). 
ENDLOOP. 
cl_demo_output=>display( ).
```
