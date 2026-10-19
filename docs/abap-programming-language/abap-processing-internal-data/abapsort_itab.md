---
title: "SORT itab"
source_file: abapsort_itab.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SORT itab

## Syntax

``` abap
SORT itab [STABLE] 
          { { [ASCENDING|DESCENDING] 
              [AS TEXT] 
              [BY {comp1 [ASCENDING|DESCENDING] [AS TEXT]} 
                  {comp2 [ASCENDING|DESCENDING] [AS TEXT]} 
                  ... ] } 
          | { [BY (otab)] } 
          | { [BY expr] } }.  
```

[`comp1`](abenitab_components.md) · [`comp2`](abenitab_components.md)

### Addition

[1. `... STABLE`](abapsort_itab.md#addition-1)

[2. `... ASCENDING|DESCENDING`](abapsort_itab.md#addition-2)

[3. `... AS TEXT`](abapsort_itab.md#addition-3)

[4. `... BY compi [ASCENDING|DESCENDING] [AS TEXT]`](abapsort_itab.md#addition-4)

[5. `... BY (otab)`](abapsort_itab.md#addition-5)

[6. `... BY expr`](abapsort_itab.md#addition-6)

## Overview

### Description

This statement sorts an internal table `itab` according to the content of its components. Here, size comparisons are performed by default using the general [comparison rules](../abap-program-flow-logic/abenlogexp_rules.md), that is:

- Numeric and byte-like components are sorted by their values.

- Character-like components are sorted by default by their binary representation ([code page](../../abap-glossary/abencodepage_glosry.md)). Textual sorting of character-like components can be performed using the addition `AS TEXT`.

- The sizes of other component types are compared using the corresponding rules for [reference variables](../abap-program-flow-logic/abenlogexp_rules_operands_ref.md), [structures](../abap-program-flow-logic/abenlogexp_rules_operands_struc.md), and [internal tables](../abap-program-flow-logic/abenlogexp_rules_operands_itab.md).

If no explicit sort key is specified using the addition `BY`, the internal table `itab` is sorted by the [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md). The priority of the sort depends on the order in which the [key fields](../abap-declarations/abaptypes_keydef.md) are specified in the table definition. In [standard keys](../../abap-glossary/abenstandard_key_glosry.md), the sort is prioritized according to the order of the key fields in the line type of the table. If the primary table key of a standard table is [empty](../abap-data-types-and-data-objects/abenitab_empty_key.md), no sort takes place. If this is known statically, the syntax check produces a warning.

Sorting is unstable by default, which means that the relative order of lines that do not differ in sort keys is not preserved when they are sorted. The order can be different depending on the platform or when sorted multiple times. The addition `STABLE` can be used for stable sorting.

`itab` expects a [standard table](../../abap-glossary/abenstandard_table_glosry.md) or a [hashed table](../../abap-glossary/abenhashed_table_glosry.md).

- In standard tables, the [primary table index](../../abap-glossary/abenprimary_table_index_glosry.md) is applied in accordance with the sort order

- In hashed tables, the internal order is modified. This internal order was defined either by inserting lines into the internal table or by a previous sort using the statement `SORT`.

In both table categories, `SORT` specifies the order in which a subsequent [`LOOP`](abaploop_at_itab.md) runs without the addition `USING KEY`.

Sorted tables cannot be sorted using `SORT` and applying the statement `SORT` to [sorted tables](../../abap-glossary/abensorted_table_glosry.md) is forbidden by the syntax. If it is not determined until runtime that a sorted table is to be sorted, an uncatchable exception is raised if this action could modify the existing sorting. The latter occurs in the following cases:

- if the addition `BY` is used to specify a different sort key as the initial part of the table key.

- if the addition `DESCENDING` is used.

- if the addition `AS TEXT` is used.

- if an attribute of an object is specified as a component in the addition `BY`.

Otherwise, the statement `SORT` is ignored for sorted tables.

### Hints

- It is best to specify an explicit sort key behind `BY`, if possible. An implicit sort behind the [primary table key](../../abap-glossary/abentable_key_glosry.md), which can itself, in standard tables, be defined implicitly as a [standard key](../../abap-glossary/abenstandard_key_glosry.md), makes a program difficult to understand and possibly unpredictable.

- When using the primary table key, it should be noted that this key can be the [standard key](../../abap-glossary/abenstandard_key_glosry.md), which can also have unexpected consequences:

  - If the line type is structured, the table is sorted by all character-like and byte-like components.

  - The standard key of a standard table can be [empty](../abap-data-types-and-data-objects/abenitab_empty_key.md).

- Secondary table keys cannot be specified as sort keys.

- Sorting using `SORT` does not affect the assignment of lines to a [secondary table index](../../abap-glossary/abensecondary_table_index_glosry.md).

- It is possible to sort columns with [reference types](../../abap-glossary/abenreference_type_glosry.md) but doing this is questionable. Here, it is important to note that no comparison rule is defined for non-initial invalid references. An internal table can only be sorted by valid or initial references. A non-initial, invalid reference leads to a runtime error if it is involved in sorting.

- The addition [`GROUP BY`](abaploop_at_itab_group_by.md) of the statement [`LOOP AT itab`](abaploop_at_itab.md) or of a [`FOR` expression](abenfor_groups_of.md) also has the additions `ASCENDING` and `DESCENDING` for sorting groups. These can be used as an extension to the statement `SORT` if its sort criteria are not sufficient.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Simplest form of the statement `SORT` for internal tables. The hashed table `carriers` is sorted by its primary key, that is by the column `carrid`.

``` abap
DATA carriers TYPE HASHED TABLE OF scarr 
              WITH UNIQUE KEY carrid. 
 
SELECT * 
       FROM scarr 
       INTO TABLE @carriers. 
 
SORT carriers.
```

## Executable Examples

- [Sorting Internal Tables](abensort_stable_abexa.md)

- [Sorting Internal Tables with Secondary Keys](abensort_itab_sec_key_abexa.md)

## Addition 1

`... STABLE`

### Description

`STABLE` is used to achieve stable sorting, which means that the relative order of lines that do not differ in the sort key remains unchanged in the sort. If the addition `STABLE` is not specified, the order is not stable:

- The order can depend on the platform.

- Multiple sorting of a table using the same sort key can produce a different order each time the table is sorted.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Stable sorting of the internal table `flights` by columns `cityfrom` `cityto`, whereby the order within this sorting with respect to `carrid` and `connid` is preserved.

``` abap
SELECT carrid, connid, cityfrom, cityto 
       FROM spfli 
       ORDER BY carrid, connid 
       INTO TABLE @DATA(flights). 
 
SORT flights STABLE BY cityfrom cityto.
```

## Addition 2

`... ASCENDING|DESCENDING`

### Description

The addition `ASCENDING` or `DESCENDING` can be used to specify the sort direction explicitly as ascending or descending. If neither of the additions is specified, the table is sorted in ascending order. This sort direction can be overwritten after the addition `BY` for components listed individually here.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The internal table `itab` is sorted by its primary key in descending order, that is, by its lines. Next, [`LOOP AT GROUP BY`](abaploop_at_itab_group_by.md) can be used for grouping and determine the number of lines per group.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA itab TYPE TABLE OF i WITH NON-UNIQUE KEY table_line. 
 
FINAL(t) = cl_demo_date_time=>get_utc_time( ). 
FINAL(rnd) = cl_abap_random_int=>create( seed = CONV i( t ) 
                                        min  = 1 
                                        max  = 10 ). 
 
itab = VALUE #( FOR i = 1 UNTIL i > 100 ( rnd->get_next( ) ) ). 
 
SORT itab DESCENDING. 
 
LOOP AT itab ASSIGNING FIELD-SYMBOL(<fs>) 
             GROUP BY ( key = <fs> size = GROUP SIZE ) 
             ASSIGNING FIELD-SYMBOL(<key>). 
  out->write( |{ <key>-key WIDTH = 4 
              }{ <key>-size }| ). 
ENDLOOP. 
 
out->display( ).
```

## Addition 3

`... AS TEXT`

### Description

The addition `AS TEXT` specifies that [text-like](../../abap-glossary/abentextlike_data_type_glosry.md) components are sorted in accordance with the [locale](../../abap-glossary/abenlocale_glosry.md) of the current [text environment](../../abap-glossary/abentext_environment_glosry.md). If `AS TEXT` is not specified, text-like components are sorted according to the encoding in the code page of the current text environment. This can be overwritten after the addition `BY` for the components listed individually here. The text environment is set when an [internal session](../../abap-glossary/abeninternal_session_glosry.md) is opened or by using the statement `SET LOCALE`.

### Hints

- The result of a sorting without the addition `AS TEXT` depends on the operating system of the [host computer](../../abap-glossary/abenhost_computer_glosry.md) of the current [AS instance](../../abap-glossary/abenas_instance_glosry.md). Although the sequence of individual letters that belong to the activated language remains the same across different operating systems, there are differences in terms of the characters that do not belong to the alphabet of the activated language. Even if only the letters from the alphabet of the activated language are used, some slight differences occur when sorting complete words. Furthermore, the order of uppercase and lowercase letters is specific to the operating system.

- The use of the addition `AS TEXT` usually makes the statement [`CONVERT TEXT`](abapconvert_text.md) superfluous in the context of internal tables.

- A sort without the addition `AS TEXT` is considerably faster than a sort with this addition. If it is certain that both sorts produce the same order, the addition `AS TEXT` is not necessary. The latter can be the case if, for example, text-like components contain characters from the [ASCII](../../abap-glossary/abenascii_glosry.md) character set only and only lowercase or uppercase letters.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Sorting of a [hashed table](../../abap-glossary/abenhashed_table_glosry.md) `text_tab` by the order in the code page and in accordance with the locale of the current [text environment](../abap-language-environment/abentext_environment.md). If a western European text environment is configured, the sorts produce the orders `Miller`, `Moller`, `Muller`, `M&#x00F6;ller` and `Miller`, `Moller`, `M&#x00F6;ller`, `Muller` respectively (see also the executable example for `SET LOCALE`).

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS meth. 
  PRIVATE SECTION. 
    CLASS-DATA text_tab TYPE HASHED TABLE OF string 
               WITH UNIQUE KEY table_line. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD meth. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    text_tab = VALUE #( 
      ( `Muller` ) 
      ( `M&#x00F6;ller` ) 
      ( `Moller` ) 
      ( `Miller` ) ). 
    SORT text_tab. 
    out->write_data( text_tab ). 
    SORT text_tab AS TEXT. 
    out->write_data( text_tab ). 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    demo=>meth( ). 
  ENDMETHOD. 
ENDCLASS.
```

### Executable Example

[Sorting Internal Tables Alphabetically](abensort_text_abexa.md)

## Addition 4

`... BY compi [ASCENDING|DESCENDING] [AS TEXT]`

### Description

The addition `BY compi` does not sort the table by the [primary table key](../abap-declarations/abaptypes_keydef.md), but by the components `comp1 comp2...` specified after it. The components are specified as described under [Specifying Components](abenitab_components.md). If all components are specified using `name` variables and these contain only blanks, no sort takes place. The priority of the sort depends on the order in which the components `comp1 comp2 ...` are specified from left to right. The specified components can also be duplicated or overlapping. The specified components can have any data type. The relevant [comparison rules](../abap-program-flow-logic/abenlogexp_rules.md) apply to the evaluation.

If neither of the additions `ASCENDING` or `DESCENDING` are specified after `compi`, the sort direction specified by addition 2 is used. If one of the additions `ASCENDING` or `DESCENDING` is specified, it overwrites the default for this component.

If the addition `AS TEXT` is not specified after a text-like component `compi`, the default specified by addition 3 is used. If the addition `AS TEXT` is specified after a text-like component, it overwrites the default for this component. In non-text-like components, `AS TEXT` cannot be specified, unless a structured component is specified. In structured components, `AS TEXT` only affects text-like components.

### Hints

- If the line type of the internal table is not known statically, the components can only be specified dynamically and not directly.

- Instead of individual dynamic components, an internal table can be specified directly as `otab` or as the result of an expression `expr` as a dynamic sort key (see additions 5 and 6). Using a table like this has the advantage that any exceptions are catchable. When specifying the table, the number of components of the sort key is also dynamic. In contrast, when individual dynamic components are used, a character-like data object must be specified for any required component, which is ignored if it only contains blank characters.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Sorting of the internal table `itab` in ascending order by column `col1` and in descending order by column `col2`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF line, 
    col1 TYPE c LENGTH 1, 
    col2 TYPE i, 
  END OF line. 
 
DATA itab TYPE STANDARD TABLE OF line WITH EMPTY KEY. 
 
itab = VALUE #( ( col1 = 'A' col2 = 6 ) 
                ( col1 = 'B' col2 = 4 ) 
                ( col1 = 'B' col2 = 7 ) 
                ( col1 = 'C' col2 = 1 ) 
                ( col1 = 'C' col2 = 3 ) 
                ( col1 = 'B' col2 = 9 ) 
                ( col1 = 'A' col2 = 2 ) 
                ( col1 = 'A' col2 = 5 ) 
                ( col1 = 'C' col2 = 8 ) ). 
 
SORT itab BY col1 ASCENDING col2 DESCENDING. 
 
out->write( itab ). 
 
out->display( ).
```

## Addition 5

`... BY (otab)`

### Description

The addition `BY (otab)` does not sort the table by the [primary table key](../abap-declarations/abaptypes_keydef.md), but by the component specified dynamically in the internal table `otab`. Each line of the table `otab` defines a component of the sort key. The priority of the sort is based on the order of the lines in `otab`. If the table `otab` is initial, the table is not sorted.

For `otab`, a standard table of the table type `ABAP_SORTORDER_TAB` from the ABAP Dictionary must be specified. The line type of this table is the dictionary structure `ABAP_SORTORDER` with the following components:

- `NAME` of the type [`SSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md)

  for specifying a component of the sort key. The component is specified in the form *comp_name\[+off(len)\]*, where *comp_name* must be the name of a component in `itab` in uppercase letters. The component name may contain [offsets and lengths](../abap-operands/abenoffset_length.md), structure component selectors, and component selectors for assigning structured data objects and attributes in classes or objects.

- `DESCENDING` of the type `CHAR` with length 1

  for specifying the sort direction for the current component. If `DESCENDING` is initial, the sort is performed in ascending order. If `DESCENDING` has the value *X*, the table is sorted in descending order.

- `ASTEXT` of the type `CHAR` with length 1

  for the text sorting of the current component. If `ASTEXT` has the value *X*, the sort is performed as with the addition `AS TEXT`. This is only possible for character-like components. If `ASTEXT` is initial, character-like components are sorted in accordance with their binary representation.

If a column of `otab` has invalid content, that is, if `NAME` contains the name of a component that does not exist or an incorrect offset/length or if `DESCENDING` and `ASTEXT` do not contain *X* or the initial value, a catchable exception of the class `CX_SY_DYN_TABLE_ILL_COMP_VAL` is raised.

### Hints

- The addition `BY (otab)` cannot be combined with `BY compi`.

- When using the addition `BY (otab)`, it is not possible to use `DESCENDING` or `AS TEXT` to specify a descending sort direction or textual sorting for all components.

- If a single parenthesized data object `(dobj)` is specified after the addition `BY`, its data type decides whether its content is used to specify a [single dynamic component](abenitab_components.md) or multiple components. In either case, no sort takes place if `dobj` is initial.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of a database table into a dynamic internal table dynamically and sorting its content dynamically. The name of the database table and the names of the columns by which the table sorted can be entered.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA dbtab TYPE c LENGTH 30 VALUE 'spfli'. 
cl_demo_input=>add_field( CHANGING field = dbtab ). 
DATA columns TYPE string VALUE `cityfrom, cityto`. 
cl_demo_input=>request( CHANGING field = columns ). 
dbtab = condense( to_upper( dbtab ) ). 
 
DATA dref  TYPE REF TO data. 
 
TRY. 
    CREATE DATA dref TYPE STANDARD TABLE OF (dbtab). 
  CATCH cx_sy_create_data_error. 
    out->write( 'Wrong data type!' ). 
ENDTRY. 
 
TRY. 
    SELECT * 
           FROM (dbtab) 
           INTO TABLE @dref->*. 
  CATCH cx_sy_dynamic_osql_semantics. 
    out->write( 'Wrong database table!' ). 
ENDTRY. 
 
SPLIT columns AT `,` INTO TABLE FINAL(column_tab). 
FINAL(order) = VALUE abap_sortorder_tab( 
                FOR wa IN column_tab 
               ( name = condense( to_upper( wa ) ) ) ). 
 
TRY. 
    SORT dref->* BY (order). 
  CATCH cx_sy_dyn_table_ill_comp_val. 
    out->write(  'Wrong column name!' ). 
ENDTRY. 
 
out->write( dref->* ). 
 
out->display( ).
```

## Addition 6

`... BY expr`

### Description

The addition `BY expr` can be used to specify an expression or a functional method call `expr` whose result is an internal table with the same type and content as in the preceding addition `BY (otab)`. `expr` is a [general expression position](../../abap-glossary/abengeneral_expr_position_glosry.md). The behavior is the same as when specifying a parenthesized internal table directly.

### Hint

Parentheses cannot be placed around `expr`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The above example for specifying `BY (otab)` can be written shorter as shown below. Instead of specifying the unnecessary internal table `order`, it is possible to directly specify the tabular value constructed using the value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) of the required content.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA dbtab TYPE c LENGTH 30 VALUE 'spfli'. 
cl_demo_input=>add_field( CHANGING field = dbtab ). 
DATA columns TYPE string VALUE `cityfrom, cityto`. 
cl_demo_input=>request( CHANGING field = columns ). 
dbtab = condense( to_upper( dbtab ) ). 
 
DATA dref  TYPE REF TO data. 
 
TRY. 
    CREATE DATA dref TYPE STANDARD TABLE OF (dbtab). 
  CATCH cx_sy_create_data_error. 
    out->write( 'Wrong data type!' ). 
ENDTRY. 
 
TRY. 
    SELECT * 
           FROM (dbtab) 
           INTO TABLE @dref->*. 
  CATCH cx_sy_dynamic_osql_semantics. 
    out->write( 'Wrong database table!' ). 
ENDTRY. 
 
SPLIT columns AT `,` INTO TABLE DATA(column_tab). 
TRY. 
    SORT dref->* BY VALUE #( FOR wa IN column_tab 
                     ( name = condense( to_upper( wa ) ) ) ). 
  CATCH cx_sy_dyn_table_ill_comp_val. 
    out->write(  'Wrong column name!' ). 
ENDTRY. 
 
out->write( dref->* ). 
 
out->display( ).
```

### Executable Example

[Sorting Internal Tables Dynamically](abensort_itab_exp_abexa.md).

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_DYN_TABLE_ILL_LINE_TYPE`

- *Cause:* The table `otab` has an invalid line type.

  *Runtime error:* `DYN_TABLE_ILL_LINE_TYPE`

`CX_SY_DYN_TABLE_ILL_COMP_VAL`

- *Cause:* A column of the table `otab` contains an invalid value.

  *Runtime error:* `DYN_TABLE_ILL_COMP_VAL`
