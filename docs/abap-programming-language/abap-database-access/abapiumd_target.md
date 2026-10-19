---
title: "INSERT, UPDATE, MODIFY, DELETE, target"
source_file: abapiumd_target.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INSERT, UPDATE, MODIFY, DELETE, target

## Syntax

``` abap
... writable_obj | (target_syntax) [client_handling] ...  
```

### Alternative

[1. `... writable_obj`](abapiumd_target.md#alternative-1)

## Overview

### Description

In the modifying ABAP SQL statements [`INSERT`](abapinsert_dbtab.md), [`UPDATE`](abapupdate.md), [`MODIFY`](abapmodify_dbtab.md), and [`DELETE`](abapdelete_dbtab.md), these elements specify statically or dynamically which [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) is accessed. Optional additions `client_handling` control [client handling](../../abap-glossary/abenclient_handling_glosry.md).

## Alternative 1

`... writable_obj`

### Description

`writable_obj` can be a [CDS table entity](../../abap-glossary/abencds_table_entity_glosry.md), a [writable CDS view entity](../../abap-glossary/abenwritable_v2_glosry.md), a DDIC database table defined in the ABAP Dictionary.

### Hint

The [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) must be specified using the exact name defined for it. More specifically, no name for the [database schema](../../abap-glossary/abendatabase_schema_glosry.md) can be prefixed. An ABAP SQL statement always accesses the database schema assigned to the current [database user name](../../abap-glossary/abendatabase_user_name_glosry.md). In cases where the [standard connection](../../abap-glossary/abenstandard_db_connection_glosry.md) or a [service connection](../../abap-glossary/abenservice_connection_glosry.md) is used, this is the [ABAP database schema](../../abap-glossary/abenabap_db_schema_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Static specification of a CDS table entity in different writing ABAP SQL statements.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DELETE FROM demo_cds_expressions. 
 
INSERT demo_cds_expressions FROM TABLE @( VALUE #( 
  ( id = 'X' num1 = 1 num2 = 10 ) 
  ( id = 'Y' num1 = 2 num2 = 20 ) 
  ( id = 'Z' num1 = 3 num2 = 30 ) ) ). 
 
UPDATE demo_cds_expressions 
  SET num2 = num2 + demo_cds_expressions~num1 
  WHERE id = 'X'. 
 
MODIFY demo_cds_expressions FROM @( VALUE #( 
  id = 'Y' num1 = 20 num2 = 200 ) ). 
 
DELETE FROM demo_cds_expressions WHERE id = 'Z'. 
 
SELECT id, num1, num2 
       FROM demo_cds_expressions 
       INTO TABLE @FINAL(itab). 
 
out->write( itab ). 
 
out->display( ).
```

## Alternative 2

`... (target_syntax)`

### Description

Instead of specifying an object statically, a parenthesized data object `target_syntax` can be specified that must contain the name of the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) when the statement is executed. A character-like data object or a [standard table](../../abap-glossary/abenstandard_table_glosry.md) with a character-like row type can be specified for the data object `target_syntax`. The syntax in `target_syntax` is not case-sensitive. Invalid syntax raises a catchable exception from the class `CX_SY_DYNAMIC_OSQL_ERROR`.

### Security Hint

If used incorrectly, dynamic programming techniques can present a serious security risk. Any dynamic content that is passed to a program from the outside must be checked thoroughly or escaped before it is used in dynamic statements. This can be done using the system class `CL_ABAP_DYN_PRG` or the built-in function [`escape`](../abap-processing-internal-data/abenescape_functions.md).

### Hint

When specified dynamically, ABAP SQL statements can contain the comment characters [`*`](../abap-syntax-elements-of-an-abap-program/abencomment.md) and [`"`](../abap-syntax-elements-of-an-abap-program/abencomment.md) as follows:

- In a dynamic token specified as a character-like data object, all content is ignored from the first comment character `"`.

- In a dynamic token specified as an internal table, all rows are ignored that start with the comment character `*`. In the row, all content is ignored from the first comment character `"`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specification of a DDIC database table in a `DELETE` statement to delete all rows of the [current client](../../abap-glossary/abencurrent_client_glosry.md) dynamically. A check is made to verify whether the object entered is in a particular package and any exceptions are handled.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(dbtab) = `demo_update`. 
cl_demo_input=>request( CHANGING field = dbtab ). 
TRY. 
    dbtab = 
      cl_abap_dyn_prg=>check_table_name_str( 
        val = to_upper( dbtab ) 
        packages = 'SABAPDEMOS' ). 
  CATCH cx_abap_not_a_table cx_abap_not_in_package. 
    out->write( 'Object must be in package SABAPDEMOS' 
      )->display( ). 
    RETURN. 
ENDTRY. 
 
TRY. 
    DELETE FROM (dbtab). 
    out->write( |Deleted { sy-dbcnt } lines| ). 
  CATCH cx_sy_dynamic_osql_semantics. 
    out->write( 'Deletion failed' ). 
ENDTRY. 
 
out->display( ).
```
