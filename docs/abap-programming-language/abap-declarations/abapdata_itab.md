---
title: "DATA, TABLE OF"
source_file: abapdata_itab.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Objects > DATA"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DATA, TABLE OF

## Syntax

``` abap
DATA itab { {TYPE [STANDARD]|SORTED|HASHED TABLE OF [REF TO] type}   
          | {LIKE [STANDARD]|SORTED|HASHED TABLE OF dobj} }   
          [tabkeys]   
          [INITIAL SIZE n]   
          [VALUE IS INITIAL]   
          [READ-ONLY].  
```

[`tabkeys`](abapdata_keydef.md) · [`[VALUE IS INITIAL]`](abapdata_options.md) · [`[READ-ONLY]`](abapdata_options.md)

## Description

This statement defines an internal table. The definition of the line type, the table category ([`STANDARD TABLE`](abaptypes_tabcat.md), [`SORTED TABLE`](abaptypes_tabcat.md), or [`HASHED TABLE`](abaptypes_tabcat.md)), and the [initial memory requirement](../../abap-glossary/abeninitial_mem_req_glosry.md) [`INITIAL SIZE`](abaptypes_itab.md) matches the definition of table categories in the section [`TYPES` - `TABLE OF`](abaptypes_itab.md) exactly. Using `DATA`, these additions create a bound table type. The generic types `ANY TABLE` and `INDEX TABLE` cannot be used with `DATA`.

[`tabkeys`](abapdata_keydef.md) is used to define the [table keys](../../abap-glossary/abentable_key_glosry.md) of the internal table, which, unlike data types, cannot be generic.

## Hints

- When an internal table is created as a data object, only the administrative entry of an internal table is generated. The actual table lines are only inserted at runtime.

- When an internal table is defined, the start value after the addition [`VALUE`](abapdata_options.md) must be `IS INITIAL`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of an internal hashed table. The line type corresponds to the structure of the database table `SPFLI`. Two key fields are defined for the primary table key. The other statements demonstrate the filling of the table with lines from the DDIC database table `SPFLI` and how a line is read.

``` abap
DATA: spfli_tab TYPE HASHED TABLE OF spfli 
                WITH UNIQUE KEY carrid connid, 
      spfli_wa  LIKE LINE OF spfli_tab. 
 
SELECT * 
       FROM spfli 
       WHERE  carrid = 'LH' 
       INTO TABLE @spfli_tab. 
 
spfli_wa = spfli_tab[ KEY primary_key 
                          carrid =  'LH' connid =  '0400' ]. 
 
...
```
