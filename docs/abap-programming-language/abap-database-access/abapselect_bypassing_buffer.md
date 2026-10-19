---
title: "SELECT, BYPASSING BUFFER"
source_file: abapselect_bypassing_buffer.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, OPTIONS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, BYPASSING BUFFER

## Syntax

``` abap
... BYPASSING BUFFER ...  
```

## Description

This addition causes the `SELECT` statement to bypass the [table buffering](../../abap-glossary/abentable_buffering_glosry.md) of buffered DDIC database tables or DDIC views. Any buffers on the current [AS instance](../../abap-glossary/abenas_instance_glosry.md) are not accessed and the database is accessed directly instead.

## Hints

- The addition `BYPASSING BUFFER` can be used if it is vital that the current data is accessed for a buffered table instead of the buffer.

- The addition `BYPASSING BUFFER` can be specified for unbuffered DDIC database tables or views, but then describes the regular behavior.

- The addition `BYPASSING BUFFER` does not ensure that data in an internal table is transported to the database when reads are performed on the table using [`FROM ... @itab`](abapselect_data_source.md).

- The addition `BYPASSING BUFFER` should not be specified without the explicit addition [`OPTIONS`](abapselect_options.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Access to the most current data of the fully buffered DDIC database table `SPFLI`.

``` abap
SELECT * 
       FROM spfli 
       INTO TABLE @FINAL(result) 
       OPTIONS 
         BYPASSING BUFFER.
```
