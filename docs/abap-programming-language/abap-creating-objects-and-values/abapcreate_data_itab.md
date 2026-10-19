---
title: "CREATE DATA, TABLE OF"
source_file: abapcreate_data_itab.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > CREATE DATA"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CREATE DATA, TABLE OF

## Syntax

``` abap
CREATE DATA dref     
                 { {TYPE [STANDARD]|SORTED|HASHED TABLE OF [REF TO] {type|(name)}}   
                 | {LIKE [STANDARD]|SORTED|HASHED TABLE OF dobj} }   
                 [ WITH { {[UNIQUE|NON-UNIQUE] 
                           {KEY {comp1 comp2 ...}|(keytab)}|  {DEFAULT KEY}}}   
                        | {EMPTY KEY}  ]   
                 [INITIAL SIZE n].  
```

## Description

The statement `CREATE DATA` uses the addition `tabkind OF` to create an internal table. The meaning of the additions is the same as when declaring internal tables using the statement [`DATA`](../abap-declarations/abapdata_itab.md), but with special rules for [`CREATE DATA`](abapcreate_data_existing.md) if `dobj` is specified after `LIKE`. The explicit definition of the primary table key is only optional if a [standard table](../../abap-glossary/abenstandard_table_glosry.md) is created.

Whereas for `DATA` all specifications must be static, the following dynamic specifications are possible for `CREATE DATA`:

- The line type after `TYPE` or the static type of a line flagged as a reference variable after `TYPE REF TO` can be specified as the content of a character-like data object called `name`, whereby the same rules apply as in the other variants of `CREATE DATA`.

- For the definition of the primary table key a parenthesized internal table `keytab` can be specified instead of static components `comp1 comp2 ...`. The table `keytab` must have a character-like data type and, when the statement is executed, it must contain the name of a valid component in each line or the identifier `table_line` for the primary table key in a single line.

- A numeric data object can be specified for `n` after `INITIAL SIZE`.

## Hints

- The following restrictions apply to the definition of the table key, unlike to `DATA`:

  - No [secondary table keys](../../abap-glossary/abensecondary_table_key_glosry.md) can be defined in the statement `CREATE DATA`.

  - The name [`primary_key`](../abap-declarations/abapdata_primary_key.md) and the addition [`COMPONENTS`](../abap-declarations/abapdata_primary_key.md) cannot be specified explicitly in the definition of the primary key.

    [Runtime type creation](../../abap-glossary/abenrun_time_type_creation_glosry.md) should be used instead to create dynamic table types with secondary keys. The same applies to the dynamic creation of an [empty table key](../abap-data-types-and-data-objects/abenitab_empty_key.md), since the internal table `keytab` can only be used to define non-empty keys.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation and use of an anonymous hashed table.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA dref TYPE REF TO data. 
 
CREATE DATA dref TYPE HASHED TABLE OF scarr 
                 WITH UNIQUE KEY carrid. 
 
SELECT * 
       FROM scarr 
       INTO TABLE @dref->*. 
 
out->write( dref->* ). 
 
out->display( ).
```

## Executable Example

[Creating Tabular Data Objects](abencreate_tabular_data_abexa.md)
