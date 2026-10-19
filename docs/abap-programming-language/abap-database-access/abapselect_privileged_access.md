---
title: "SELECT, PRIVILEGED ACCESS"
source_file: abapselect_privileged_access.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, OPTIONS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, PRIVILEGED ACCESS

## Syntax

``` abap
... PRIVILEGED ACCESS ...  
```

## Description

The addition `PRIVILEGED ACCESS` disables [CDS access control](../../abap-glossary/abencds_access_control_glosry.md) for all [CDS entities](../../abap-glossary/abencds_entity_glosry.md) accessed in the current `SELECT` statement. Any [access conditions](../../abap-glossary/abenaccess_condition_glosry.md) that are defined for a CDS entity by a [CDS role](../../abap-glossary/abencds_role_glosry.md) are not evaluated.

The addition `PRIVILEGED ACCESS` cannot be used together with the following additions:

- [`WITH PRIVILEGED ACCESS`](abapselect_data_source.md) of the `FROM` clause that affects only one CDS entity.

## Hints

- The addition `PRIVILEGED ACCESS` overrides all delivered and user-defined roles.

- CDS access control can also be disabled using the annotation `@AccessControl.authorizationCheck:#NOT_ALLOWED` when a [CDS persistent entity](../../abap-glossary/abencds_sql_entity_glosry.md) is defined.

- In contrast to the addition [`WITH PRIVILEGED ACCESS`](abapselect_data_source.md) of the `FROM` clause, `PRIVILEGED ACCESS` prevents the evaluation of any conditions from CDS access control for the complete `SELECT` statement. In particular, CDS access control is also disabled for entities that are addressed by a [SQL path expression](abenabap_sql_path.md).

- The addition `PRIVILEGED ACCESS` should not be specified without the explicit addition [`OPTIONS`](abapselect_options.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of the addition `PRIVILEGED ACCESS` for a `SELECT` statement that accesses the CDS view `DEMO_CDS_AUTHORITY_LITERAL_2`, which is linked with the following CDS role:

``` abap
CDS or DDIC source code was not found
```

Unlike using the class `CL_DEMO_CDS_AUTH_LITERAL`, all data of the view are read.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT * 
       FROM demo_cds_authority_literal_2 
       ORDER BY carrid 
       INTO TABLE @FINAL(result) 
       OPTIONS 
         PRIVILEGED ACCESS. 
 
out->write( result ). 
 
out->display( ).
```
