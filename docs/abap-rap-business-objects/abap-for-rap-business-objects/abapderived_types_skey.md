---
title: "%skey"
source_file: abapderived_types_skey.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Components Related to Keys and RAP BO Instance Identification"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %skey

## Use

`%skey` is a [component group](../../abap-glossary/abencomponent_group_glosry.md) in [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md). It is contained as component of [`%param`](abapderived_types_param.md) and occurs in the context of [RAP key functions](../../abap-glossary/abenrap_key_function_glosry.md). `%skey` contains either the [BDEF pure key](../../abap-glossary/abenrap_pure_key_glosry.md) or [BDEF secondary key](../../abap-glossary/abenrap_secondary_key_glosry.md) that are specified in the [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) (BDEF).

## More Information

[RAP - `key function`](../rap-behavior-definitions/abenbdl_keyfunction.md)

**Where used**

This component can occur in the following type declarations of [`TYPE TABLE FOR ...`](abaptype_table_for.md) and [`TYPE STRUCTURE FOR ...`](abaptype_structure_for.md):

- `FUNCTION IMPORT` (RAP key function)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code demonstrates the use of `%skey`. The explicit specification of `%skey` is optional.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DELETE FROM demo_dbtab_root. 
INSERT demo_dbtab_root FROM TABLE @( VALUE #( 
( key_field = 1  data_field = `A` char_field = 'X' char_field_2 = 'A' ) 
( key_field = 2  data_field = `A` char_field = 'Y' char_field_2 = 'B' ) 
( key_field = 3  data_field = `D` char_field = 'Z' char_field_2 = 'C' ) 
( key_field = 4  data_field = `A` char_field = 'X' char_field_2 = 'D' ) 
( key_field = 5  data_field = `E` char_field = 'Y' char_field_2 = 'E' ) 
( key_field = 6  data_field = `A` char_field = 'Z' char_field_2 = 'F' ) 
( key_field = 7  data_field = `A` char_field = 'W' char_field_2 = 'G' ) 
) ). 
 
DATA func_imp TYPE 
  TABLE FOR FUNCTION IMPORT demo_rap_pure_key~GetByAltKey. 
func_imp = VALUE #( ( %cid = `cid1` %param-%skey-char_field = 'W' ) 
                    ( %cid = `cid2` %param-%skey = 'X' ) 
                    ( %cid = `cid3` %param-char_field = 'Y' ) 
                    ( %cid = 'cid4' %param = 'Z' ) ). 
 
READ ENTITY demo_rap_pure_key 
  EXECUTE GetByAltKey FROM func_imp 
  RESULT DATA(res) 
  FAILED DATA(f) 
  REPORTED DATA(r). 
 
out->write( res ). 
 
out->display( ).
```
