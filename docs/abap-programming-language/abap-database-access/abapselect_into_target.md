---
title: "SELECT, INTO target"
source_file: abapselect_into_target.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, INTO, APPENDING"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, INTO target

## Syntax

``` abap
... {     @dobj       } 
  | {     @DATA(dobj)|@FINAL(dobj) } 
  | { NEW @dref       } 
  | { NEW @DATA(dref)|@FINAL(dref) } ...  
```

### Alternative

[1. `... @dobj`](abapselect_into_target.md#alternative-1)

[2. `... @DATA(dobj)|@FINAL(dobj)`](abapselect_into_target.md#alternative-2)

[3. `... NEW @dref`](abapselect_into_target.md#alternative-3)

[4. `... NEW @DATA(dref)|@FINAL(dref)`](abapselect_into_target.md#alternative-4)

## Overview

### Description

Specifies a target area of the [`INTO`](abapinto_clause.md) clause of an ABAP SQL query. The possible target areas of the [`INTO`](abapinto_clause.md) clause are as follows:

- Elementary data objects `elem1`, `elem2`, ... in a comma-separated list.

- Individual work areas `wa`.

- Internal tables `itab` after `TABLE`.

Each target area can be specified as follows:

- If the addition `NEW` is not used, `dobj` specifies the data object directly to which the data from the result set is written. The target area is one of the following:

  - A previously declared [host variable](../../abap-glossary/abenhost_variable_glosry.md) `@dobj`

  - A [host variable](../../abap-glossary/abenhost_variable_glosry.md) `dobj` declared [inline](../../abap-glossary/abeninline_declaration_glosry.md) using `@DATA`

The addition `NEW` is used to create an [anonymous data object](../../abap-glossary/abenanonymous_data_object_glosry.md) to which data from the result set is written and to which a [data reference variable](../../abap-glossary/abendata_reference_variable_glosry.md) `dref` points. The data reference variable is one of the following:

- A previously declared [host variable](../../abap-glossary/abenhost_variable_glosry.md) `@dref`

- A [host variable](../../abap-glossary/abenhost_variable_glosry.md) `dref` declared [inline](../../abap-glossary/abeninline_declaration_glosry.md) using `@DATA`

All alternatives can occur combined in a comma-separated list for elementary data objects as target areas. One of these alternatives must be selected when a single work area or an internal table is specified.

### Hints

- In the case of the variant `NEW @DATA(dref)|@FINAL(dref)`, the [`SELECT` list](abapselect_list.md), the [`FROM` clause](abapfrom_clause.md), and any [indicators](abapselect_indicators.md) can be specified dynamically. This is the only way of combining a dynamically defined result set with inline declarations.

## Alternative 1

`... @dobj`

### Description

Specifies a previously declared [host variable](abenabap_sql_host_variables.md) `@dobj` as a target area of the [`INTO`](abapinto_clause.md) clause. The data in the result set is written directly to the host variable `dobj`. Depending on the operand position, the host variable can be one of the following:

- In the comma-separated list `elem1`, `elem2`, ..., an [elementary data object](../../abap-glossary/abenelementary_data_object_glosry.md) that matches the type of the associated column of the result set or in other words: The type of the associated column of the result set can be converted to the data type of the data object.

- As a single work area `wa`, a data object that meets the [prerequisites](abenabap_sql_wa.md).

- As an internal table, any table category whose row structure meets the [prerequisites](abenabap_sql_wa.md).

Writes to the host variable are made as described in the [`INTO`](abapinto_clause.md) clause.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of different existing host variables as target areas of `SELECT` statements.

``` abap
DATA: 
  carrid   TYPE scarr-carrid, 
  carrname TYPE scarr-carrname, 
  url      TYPE scarr-url, 
  carrier  TYPE scarr, 
  carriers TYPE SORTED TABLE OF scarr WITH UNIQUE KEY carrid. 
 
SELECT SINGLE carrid, carrname, url 
       FROM scarr 
       WHERE carrid = 'UA' 
       INTO (@carrid, @carrname, @url). 
 
SELECT SINGLE * 
       FROM scarr 
       WHERE carrid = 'LH' 
       INTO @carrier. 
 
SELECT * 
       FROM scarr 
       INTO TABLE @carriers.
```

## Alternative 2

`... @DATA(dobj)|@FINAL(dobj)`

### Description

Specifies a [host variable](abenabap_sql_host_variables.md) `@dobj` declared inline as the target area of the [`INTO`](abapinto_clause.md) clause. The data in the result set is written directly to the host variable `dobj`. The inline declaration is made with one of the [declaration operators](../../abap-glossary/abendeclaration_operator_glosry.md) [`DATA`](../abap-declarations/abendata_inline.md) or [`FINAL`](../abap-declarations/abenfinal_inline.md), which must be prefixed with the escape character `@` here. Depending on the operand position, the host variable is declared as follows:

- In the comma-separated list `elem1`, `elem2`, ..., an elementary variable is declared. The data type of the variables is constructed as follows from the associated column of the result set:

  - The ABAP type to which the dictionary type of a [column](abenabap_sql_columns.md) of a data source is [assigned](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is used for this column.

  - The ABAP type to which the result type of an [SQL expression](abapsql_expr.md) is [assigned](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is used for this expression.

  - The ABAP type of a [host variable](abenabap_sql_host_variables.md) is used directly for this variable specified as a single SQL expression.

- Work area and internal table:

  - For `INTO @DATA(wa)` or `INTO @FINAL(wa)`, a flat data object `wa` is declared as a single work area.

  - For `INTO TABLE @DATA(itab)` or `INTO TABLE @FINAL(itab)`, a [standard table](../../abap-glossary/abenstandard_table_glosry.md) `itab` with an [empty table key](../abap-data-types-and-data-objects/abenitab_empty_key.md) is declared as an internal table.

    The data type of `wa` or the row type of the internal table is constructed as follows in accordance with the structure of the result set defined after `SELECT` and the number of data sources specified after [`FROM`](abapfrom_clause.md):

  - If the result set in the [`SELECT` list](abapselect_list.md) is defined using a single specified column [`col_spec`](abapselect_clause_col_spec.md) for which no name can be identified, the data type of `wa` or the row type of `itab` is its elementary type.

  - If the result set in the [`SELECT` list](abapselect_list.md) is defined using a single specified column [`col_spec`](abapselect_clause_col_spec.md) for which no name can be identified, the data type of `wa` or the row type of `itab` is a structure with a component, with its elementary type.

  - If the result set in the [`SELECT` list](abapselect_list.md) is defined using a single `data_source~*` or a list of multiple specified columns [`col_spec`](abapselect_clause_col_spec.md), the data type of `wa` or the row type of `itab` is a structure with elementary components. The data types of the components are the elementary types of the columns in the result set in the order defined there.

  - If `data_source~*` is specified in the [`SELECT` list](abapselect_list.md) together with other elements, the data type of `wa` or the row type of `itab` is a nested structure. For each data source [`data_source`](abapselect_data_source.md) specified in this way, a substructure is generated with the name or alias name of the table or view. The data types of the components of the substructures are the elementary types of the data source in the order defined there. If the data source is a [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md) declared using [`WITH`](abapwith.md), the first character `+` of its name is ignored for the name of the substructure.

  - If the result set in the [`SELECT` list](abapselect_list.md) is defined using `*`, the data type depends on the number of [data sources](abapselect_data_source.md) specified after [`FROM`](abapfrom_clause.md):

    In reads from a single [data source](abapselect_data_source.md) `data_source`, the data type of `wa` or the row type of `itab` is the same as in a definition of the result set using a single `data_source~*` (see above), that is, a structure with elementary components. In reads from multiple [data sources](abapselect_data_source.md) `data_source1`, `data_source2`, ... using a [join](abapselect_join.md), the data type of `wa` or the row type of `itab` is the same as in a definition of the result set using `data_source1~*, data_source2~*, ...`. (see above), that is, a structure with a substructure for each data source.

  - The names of the elementary components of a structure match the names of the associated columns from the [result set](abapselect_list.md). Any alias names defined there are respected.

  - As with an elementary data object in a comma-separated list, the elementary data type of an elementary data object or of an elementary component of a structure is constructed from the type of the associated column of the result set (see above).

  - If the addition [`INDICATORS`](abapselect_indicators.md) is used, a substructure called `null_ind` is added at the end of the structure or row structure declared inline. For each column in the result set, this substructure contains an identically named component of type `x` and length 1 in the same order. If preceding components of the structure declared inline are substructures, the substructure `null_ind` is also structured accordingly.

The prerequisites for an inline declaration are as follows:

- The result set can be specified dynamically only when combined with the addition `NEW`. If the addition `NEW` is not specified, the structure of the result set must be known statically. The [`SELECT` list](abapselect_list.md) and any [indicators](abapselect_indicators.md) must be specified statically.

- The result set defined in the [`SELECT` list](abapselect_list.md) cannot have multiple columns with the same name. This can be bypassed using alias names.

- In a [result set](abapselect_list.md) with multiple rows or if the addition [`INDICATORS`](abapselect_indicators.md) is specified, every [SQL expression](abapsql_expr.md) and every [aggregate expression](abapselect_aggregate.md) must have an alias name.

- Alias names of the [`SELECT` list](abapselect_list.md) must comply with the [naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md) for internal program names. More specifically, they cannot contain a minus sign `-`.

- The addition [`CORRESPONDING FIELDS OF`](abapinto_clause.md) cannot be used.

### Hints

- Column specifications for which no name can be identified are SQL expressions and aggregate expressions without alias name.

- When an inline declaration `@DATA(itab)` or `@FINAL(itab)` is specified after `APPENDING TABLE`, this addition usually works like `INTO TABLE` and is therefore pointless in this combination.

- When accessing a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) with a [CDS enumerated element](../../abap-glossary/abencds_enum_element_glosry.md), an [enumerated variable](../../abap-glossary/abenenumerated_variable_glosry.md) is generated in ABAP.

- Currently, only standard tables with an empty key and without secondary keys can be declared inline as internal tables in the `INTO` clause of a `SELECT` statement.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of individual columns of a result set into different target areas declared inline. `carrname`, `carrid`, and `url` are elementary data objects. `wa` is a structure with elementary components. `itab` is a standard table with the corresponding row type.

``` abap
SELECT SINGLE 
       FROM scarr 
       FIELDS carrname, 
              carrid, 
              url 
       WHERE carrid = 'LH' 
       INTO (@FINAL(carrname),@FINAL(carrid),@FINAL(url)). 
 
SELECT SINGLE 
       FROM scarr 
       FIELDS carrname, 
              carrid, 
              url 
       WHERE carrid = 'LH' 
       INTO @FINAL(wa). 
 
SELECT FROM scarr 
       FIELDS carrname, 
              carrid, 
              url 
       INTO TABLE @FINAL(itab). 
 
ASSERT wa-carrname = carrname. 
ASSERT wa-carrid   = carrid. 
ASSERT wa-url      = url. 
 
cl_demo_output=>new( 
  )->write( wa 
  )->write( itab )->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of all columns of a result set into an inner join in an internal table whose row type is declared as a nested structure with the same structure as the result set. The first component of the nested structure is called `SCARR` and includes all columns of this DDIC database table. The second component of the nested structure is called `SPFLI` and includes all columns of this DDIC database table. The content of the columns `MANDT` and `CARRID` in both tables is redundant. For the output, the internal table with a nested row type is converted to an output table without substructures.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
 
TYPES BEGIN OF output_wa. 
INCLUDE TYPE scarr AS scarr RENAMING WITH SUFFIX _scarr. 
INCLUDE TYPE spfli AS spfli RENAMING WITH SUFFIX _spfli. 
TYPES END OF output_wa. 
TYPES output TYPE SORTED TABLE OF output_wa 
             WITH NON-UNIQUE KEY carrid_scarr connid_spfli. 
 
SELECT * 
       FROM scarr 
         INNER JOIN spfli ON scarr~carrid = spfli~carrid 
       INTO TABLE @FINAL(itab). 
 
out->write( CONV output( itab ) ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example demonstrates how enumerated variables result from an inline declaration. The data source of the following `SELECT` statement is a CDS view entity. The elements `weekday` and `EnumConstant` are enumerated elements and have the data type `ENUM`. The variable `result` of the table declared inline also has the data type `enum`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
*fill database table 
DELETE FROM demo_ddic_types. 
INSERT demo_ddic_types FROM TABLE @( VALUE #( 
 ( id = 'A' int1 = 1 ) 
 ( id = 'B' int1 = 6 ) 
) ). 
 
*SELECT from cds view entity 
SELECT * 
FROM demo_cds_enum_2 
INTO TABLE @DATA(result). 
 
*display result 
out->write( result ). 
 
out->display( ).
```

Screenshot of the `result` variable in the debugger: ![figure](images_enum_inline.jpg)

### Executable Example

[Inline Declarations](abenselect_inline_decl_abexa.md)

## Alternative 3

`... NEW @dref`

### Description

The addition `NEW` creates an [anonymous data object](../../abap-glossary/abenanonymous_data_object_glosry.md) as the target area of the [`INTO` clause](abapinto_clause.md). `dref` expects a previously declared [data reference variable](../../abap-glossary/abendata_reference_variable_glosry.md) that points to the data object after the object is created. The data of the result set is written to the new anonymous data object. The data reference variable `dref` can be typed completely or generically.

- If the data reference variable `dref` is typed completely, its [static type](../../abap-glossary/abenstatic_type_glosry.md) must follow the same rules as for a directly specified data object `@dobj`:

  - In a comma-separated list `(..., dref, ...)`, it must be an elementary data type to which the type of the associated column of the result set can be converted.

  - In a single work area `wa`, the type must meet the [prerequisites](abenabap_sql_wa.md) for work areas.

  - In an internal table, it must be a table type with any table category whose row structure meets the [prerequisites](abenabap_sql_wa.md).

    The anonymous data object is created with the type of the data reference variable. The [static type](../../abap-glossary/abenstatic_type_glosry.md) of the data reference variable matches the [dynamic type](../../abap-glossary/abendynamic_type_glosry.md). Writes to the anonymous data object are made as described in the [`INTO`](abapinto_clause.md) clause.

- If the data reference variable `dref` is typed generically with [`data`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md), the data type of the anonymous data object or the [dynamic type](../../abap-glossary/abendynamic_type_glosry.md) of `dref` is constructed depending on the operand position in exactly the same way as the data type of `dobj` in the inline declaration `@DATA|FINAL(dobj)` described above. This means the following:

  - In a comma-separated list `(..., dref, ...)`, an elementary data object is created whose type is determined by the type of the associated column of the result set.

  - For a single work area in `INTO NEW @dref`, a flat data object is created. The type of the new data object is constructed in the same way as in an inline declaration using `@DATA|FINAL(dobj)`.

  - For `INTO TABLE NEW @dref`, a [standard table](../../abap-glossary/abenstandard_table_glosry.md) with an [empty table key](../abap-data-types-and-data-objects/abenitab_empty_key.md) is created as an internal table. The row type of the internal table is constructed in the same way as in an inline declaration using `@DATA|FINAL(dobj)`.

    The anonymous data object is created with this type. The [static type](../../abap-glossary/abenstatic_type_glosry.md) of the data reference variable is more general than the [dynamic type](../../abap-glossary/abendynamic_type_glosry.md). Writes to the anonymous data object are made as described in the [`INTO`](abapinto_clause.md) clause. The columns of the result set defined in the `SELECT` list must have unique names.

Unlike in inline declarations with `@DATA|FINAL(dobj)`, the type of the anonymous data object can also be created at runtime. This means that the addition `NEW` can also be specified in the following cases:

- If the structure of the result set cannot be known statically due to the use of dynamic tokens.

If possible, the type check takes place as part of the syntax check and otherwise at runtime. If an error is not detected until runtime, an exception of the class `CX_SY_DYNAMIC_OSQL_SEMANTICS` is raised.

The following restrictions apply:

- The addition `NEW` can only be specified after [`INTO`](abapinto_clause.md) and not after [`APPENDING`](abapinto_clause.md).

### Hints

- The addition `NEW` works in a similar way as creating an anonymous data object with the [instance operator](../../abap-glossary/abeninstance_operator_glosry.md) [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) directly in front of the ABAP SQL statement and using the dereferenced reference variable as a target area. The addition `NEW` has the advantage that the data type of the anonymous data object is constructed in a suitable way and this works especially for dynamic tokens as well.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of a generically typed and a completely typed data reference variable after `NEW`. The anonymous data objects created here both have the same type and the same content. The third `SELECT` statement writes to an anonymous data object created previously using the instance operator `NEW` demonstrating roughly how the `NEW` addition works.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES scarr_tab TYPE STANDARD TABLE OF scarr WITH EMPTY KEY. 
 
DATA dref_data TYPE REF TO data. 
SELECT FROM scarr 
       FIELDS * 
       INTO TABLE NEW @dref_data. 
 
DATA dref_scarr_tab TYPE REF TO scarr_tab. 
SELECT FROM scarr 
       FIELDS * 
       INTO TABLE NEW @dref_scarr_tab. 
 
ASSERT dref_data->* = dref_scarr_tab->*. 
 
out->write( dref_data->* ). 
 
dref_scarr_tab = NEW #( ). 
SELECT FROM scarr 
       FIELDS * 
       INTO TABLE @dref_scarr_tab->*. 
ASSERT dref_data->* = dref_scarr_tab->*. 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In this example, three anonymous data objects of the type `string` are created. The columns of the result set are converted to `string`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: 
  dref1 TYPE REF TO string, 
  dref2 TYPE REF TO string, 
  dref3 TYPE REF TO string. 
 
SELECT SINGLE carrid, carrname, url 
       FROM scarr 
       WHERE carrid = 'UA' 
       INTO (NEW @dref1, NEW @dref2, NEW @dref3). 
 
out->write( |{ dref1->* }, { dref2->* }, { dref3->* }| ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example compares an `INTO` clause with an inline declaration of the target area (see above) with an `INTO` clause with the addition `NEW`. In both cases, the same data type is constructed, namely an internal table with a nested row structure. As long as individual components are not accessed, the exact data type does not need to be known in the program.

``` abap
SELECT * 
       FROM scarr 
         INNER JOIN spfli ON scarr~carrid = spfli~carrid 
       INTO TABLE @FINAL(itab). 
 
DATA dref TYPE REF TO data. 
SELECT * 
     FROM scarr 
       INNER JOIN spfli ON scarr~carrid = spfli~carrid 
     INTO TABLE NEW @dref. 
 
ASSERT dref->* =  itab.
```

## Alternative 4

`... NEW @DATA(dref)|@FINAL(dref)`

### Description

The addition `NEW` in front of an inline declaration with the [declaration operators](../../abap-glossary/abendeclaration_operator_glosry.md) [`@DATA`](../abap-declarations/abendata_inline.md) or [`@FINAL`](../abap-declarations/abenfinal_inline.md) works like the previous variant, however the data reference variable `dref` that points to the new anonymous data object is declared inline. The [static type](../../abap-glossary/abenstatic_type_glosry.md) of the data reference variable `dref` is defined as follows:

- If the data type of the new anonymous data object is known statically, `dref` is also typed with this type.

- If the data type of the new anonymous data object cannot be known until runtime, `dref` is typed with the generic type [`data`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md).

The columns of the result set defined in the `SELECT` list must have unique names.

### Hints

- The addition `NEW` can also be used to make an inline declaration together with dynamic tokens. The data reference variable that points to the target area created as an anonymous data object is declared, however, instead of the direct target area.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of an anonymous data object as target area together with an inline declaration of the data reference variable. After `SELECT` with static tokens, the data reference variable `dref_scarr` has the static type of an internal table with the row type `SCARR` from the ABAP Dictionary. This is demonstrated using RTTI methods.

``` abap
SELECT * 
       FROM scarr 
       INTO TABLE NEW @FINAL(dref_scarr). 
 
cl_demo_output=>new( 
 
  )->write( |dref_scarr: { 
            CAST cl_abap_tabledescr( 
            CAST cl_abap_refdescr( 
               cl_abap_typedescr=>describe_by_data( dref_scarr ) 
               )->get_referenced_type( 
               ) )->get_table_line_type( 
               )->absolute_name } | 
  )->display( dref_scarr->* ).
```

## Executable Examples

- [Create Structure as Target Area](abenselect_into_new_wa_abexa.md)

- [Create Internal Table as Target Area](abenselect_into_new_table_abexa.md)
