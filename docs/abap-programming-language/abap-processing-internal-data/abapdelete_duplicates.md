---
title: "DELETE itab, duplicates"
source_file: abapdelete_duplicates.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > DELETE itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DELETE itab, duplicates

## Syntax

``` abap
... [ADJACENT] DUPLICATES FROM itab [USING KEY keyname]   
             [COMPARING {comp1 comp2 ...}|{ALL FIELDS}] ...  
```

[`keyname`](abenkeyname.md) · [`comp1`](abenitab_components.md) · [`comp2`](abenitab_components.md)

### Addition

[1. `... USING KEY keyname`](abapdelete_duplicates.md#addition-1)

[2. `... COMPARING {comp1 comp2 ...}|{ALL FIELDS}`](abapdelete_duplicates.md#addition-2)

## Overview

### Description

Using these additions, the statement `DELETE` deletes all lines except for the first line in groups where several lines have the same content in certain components. With the addition `ADJACENT`, only adjacent duplicates of the internal table are deleted. In this case, all lines except for the first line are deleted in groups where several adjacent lines have the same content. If the addition `COMPARING` is not specified, the groups are determined by the content of the key fields of the table key used. If no explicit table key is specified, the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) is used implicitly.

The order of the table lines that are used to form the groups is determined by the table key used. If no key `keyname` is specified after `USING KEY`, the order is the same as when processing a statement [`LOOP`](abaploop_at_itab.md) without an explicit key specification.

Lines are considered to be duplicate if their content matches in the components examined. In the case of multiple duplicate lines following one another, all but the first line are deleted.

If the [primary table key](../../abap-glossary/abenprimary_key_glosry.md) is used to access a [standard table](../../abap-glossary/abenstandard_table_glosry.md) and the key is [empty](../abap-data-types-and-data-objects/abenitab_empty_key.md), special behavior occurs. If this is known statically, the syntax check produces a warning.

- `DELETE ADJACENT DUPLICATES FROM...`: No lines are deleted.

- `DELETE DUPLICATES FROM...`: All lines are deleted except the first line, because all lines have the same empty key value.

### Hints

- The use of `ADJACENT DUPLICATES` usually requires a suitable sorting by the components compared in the statement.

- When using the primary table key, it should be noted that this key can be the [standard key](../../abap-glossary/abenstandard_key_glosry.md), which can also have unexpected consequences:

  - For structured line types, the standard key covers all character-like and byte-like components.

  - The standard key of a standard table can be [empty](../abap-data-types-and-data-objects/abenitab_empty_key.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Deletion of all multiple adjacent lines with respect to the primary key in the internal table `city_connections`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: BEGIN OF city_connection, 
         cityfrom TYPE spfli-cityfrom, 
         cityto   TYPE spfli-cityto, 
         distid   TYPE spfli-distid, 
         distance TYPE spfli-distance, 
       END OF city_connection. 
 
DATA city_connections TYPE SORTED TABLE OF city_connection 
                      WITH NON-UNIQUE KEY cityfrom cityto 
                                          distid distance. 
 
SELECT cityfrom, cityto, distid, distance 
       FROM spfli 
       INTO TABLE @city_connections. 
 
DELETE ADJACENT DUPLICATES FROM city_connections. 
 
out->write( city_connections ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Deletion of all multiple lines with respect to the primary key in the internal table `itab_orders`.

``` abap
TYPES: BEGIN OF ts_orders, 
             customer_name TYPE string, 
             product_name  TYPE string, 
             order_date    TYPE d, 
       END OF ts_orders. 
 
TYPES tt_orders TYPE STANDARD TABLE OF ts_orders WITH KEY primary_key 
COMPONENTS customer_name. 
 
DATA itab_orders TYPE tt_orders. 
 
itab_orders = VALUE #( 
( customer_name = `Max Mustermann` product_name = `Product 1` 
 order_date = '20250405' ) 
( customer_name = `Sue Reid`       product_name = `Product 2` 
order_date = '20260201' ) 
( customer_name = `Max Mustermann` product_name = `Product 1` 
order_date = '20250405' ) 
( customer_name = `John Developer` product_name = `Product 3` 
order_date = '20260301' ) 
( customer_name = `Wanda Payne`    product_name = `Product 1` 
order_date = '20260118' ) 
( customer_name = `Victor Tucker`  product_name = `Product 4` 
order_date = '20260214' ) 
( customer_name = `Sue Reid`       product_name = `Product 2` 
order_date = '20260111' ) ). 
 
DELETE DUPLICATES FROM itab_orders.
```

## Addition 1

`... USING KEY keyname`

### Description

The addition `USING KEY` can be used to specify a table key in [`keyname`](abenkeyname.md) with which the processing is executed. The specified table key affects the order in which the table lines are accessed, and the evaluation of the remaining conditions.

If the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) is specified, the processing behaves in the same way as if no key were explicitly specified. If a [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md) is specified, the order in which the lines are accessed is as follows:

- **Specification of a [sorted key](../../abap-glossary/abensorted_key_glosry.md)**

  The lines are processed by ascending line number in the [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md)

- **Specification of a [hash key](../../abap-glossary/abenhash_key_glosry.md)**

  The lines are processed in the order in which they were inserted into the table.

### Hint

Unlike the processing of a hashed table when a primary key is used, a preceding sort using the statement `SORT` does not affect the processing order when a secondary hash key is specified.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The statement `DELETE` deletes all multiple adjacent numbers from the internal table `itab`. The table then contains a maximum of ten lines.

``` abap
DATA itab TYPE TABLE OF i WITH EMPTY KEY 
               WITH NON-UNIQUE SORTED KEY skey COMPONENTS table_line. 
 
FINAL(t) = CONV i( cl_demo_date_time=>get_utc_time( ) ). 
FINAL(rnd) = cl_abap_random_int=>create( seed = t 
                                        min  = 1 
                                        max  = 10 ). 
 
itab = VALUE #( FOR i = 1 UNTIL i > 100 ( rnd->get_next( ) ) ). 
 
DELETE ADJACENT DUPLICATES FROM itab USING KEY skey.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The addition `USING KEY` is specified and the primary key is used, which is based on the component `customer_name`.

``` abap
TYPES: BEGIN OF ts_orders, 
             customer_name TYPE string, 
             product_name  TYPE string, 
             order_date    TYPE d, 
       END OF ts_orders. 
 
TYPES tt_orders TYPE STANDARD TABLE OF ts_orders WITH KEY primary_key 
COMPONENTS customer_name. 
 
DATA itab_orders TYPE tt_orders. 
 
itab_orders = VALUE #( 
( customer_name = `Max Mustermann` product_name = `Product 1` 
order_date = '20250405' ) 
( customer_name = `Sue Reid`       product_name = `Product 2` 
order_date = '20260201' ) 
( customer_name = `Max Mustermann` product_name = `Product 1` 
order_date = '20250405' ) 
( customer_name = `John Developer` product_name = `Product 3` 
order_date = '20260301' ) 
( customer_name = `Wanda Payne`    product_name = `Product 1` 
order_date = '20260118' ) 
( customer_name = `Victor Tucker`  product_name = `Product 4` 
order_date = '20260214' ) 
( customer_name = `Sue Reid`       product_name = `Product 2` 
order_date = '20260111' ) ). 
 
DELETE DUPLICATES FROM itab_orders USING KEY primary_key.
```

## Addition 2

`... COMPARING {comp1 comp2 ...}|{ALL FIELDS}`

### Description

If the addition `COMPARING` is specified, the groups are determined either by the content of the specified components `comp1 comp2 ...` or the content of all components `ALL FIELDS`. The specification of individual components `comp` is made as described in the section [Specification of Components](abenitab_components.md). Access to class attributes is possible using the object component selector.

### Hint

Specifying the [pseudo component](../../abap-glossary/abenpseudo_component_glosry.md) `table_line` has the same effect as specifying `ALL FIELDS`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of specific data from two tables in the `ITF` framework. After the multiple adjacent numbers are deleted, it is expected that both tables contain the same number of lines. The table declared inline, `dokhl_tab`, has an empty primary key, which means that the component `object` is specified explicitly using `COMPARING`.

``` abap
SELECT object 
       FROM dokil 
       WHERE id = 'SD' AND 
             object LIKE 'AB%' AND 
             langu = @sy-langu AND 
             typ   = 'E' 
       ORDER BY object 
       INTO TABLE @FINAL(dokil_tab). 
 
SELECT object 
       FROM dokhl 
       WHERE id = 'SD' AND 
             object LIKE 'AB%' AND 
             langu = @sy-langu AND 
             typ   = 'E' 
       ORDER BY object, dokversion DESCENDING 
       INTO TABLE @DATA(dokhl_tab). 
 
DELETE ADJACENT DUPLICATES FROM dokhl_tab COMPARING object. 
 
ASSERT lines( dokhl_tab ) = lines( dokil_tab ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The addition `COMPARING` is specified. The duplicates are identified based on the components `customer_name` and `order_date`. Although the `customer_name` `Sue Reid` appears twice even with the same `product_name`, it will not be identified as a duplicate. The reason is that the respective orders have a different `order_date`, which was explicitly specified as a component using `COMPARING`.

``` abap
TYPES: BEGIN OF ts_orders, 
             customer_name TYPE string, 
             product_name  TYPE string, 
             order_date    TYPE d, 
       END OF ts_orders. 
 
TYPES tt_orders TYPE STANDARD TABLE OF ts_orders WITH EMPTY KEY. 
 
DATA itab_orders TYPE tt_orders. 
 
itab_orders = VALUE #( 
( customer_name = `Max Mustermann` product_name = `Product 1` 
order_date = '20250405' ) 
( customer_name = `Sue Reid`       product_name = `Product 2` 
order_date = '20260201' ) 
( customer_name = `Max Mustermann` product_name = `Product 1` 
order_date = '20250405' ) 
( customer_name = `John Developer` product_name = `Product 3` 
order_date = '20260301' ) 
( customer_name = `Wanda Payne`    product_name = `Product 1` 
order_date = '20260118' ) 
( customer_name = `Victor Tucker`  product_name = `Product 4` 
order_date = '20260214' ) 
( customer_name = `Sue Reid`       product_name = `Product 2` 
order_date = '20260111' ) ). 
 
DELETE DUPLICATES FROM itab_orders USING KEY primary_key 
COMPARING customer_name order_date.
```
