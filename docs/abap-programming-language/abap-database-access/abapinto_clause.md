---
title: "SELECT, INTO, APPENDING"
source_file: abapinto_clause.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, INTO, APPENDING

## Syntax

``` abap
... { INTO 
        (elem1, elem2,  ...) } 
  | { INTO 
        [CORRESPONDING FIELDS OF] wa [indicators] } 
  | { INTO|APPENDING 
        [CORRESPONDING FIELDS OF] TABLE itab [indicators] 
                                             [PACKAGE SIZE n] } 
    [ extended_result ] 
    [ creating ] ... .  
```

[`elem1`](abapselect_into_target.md) · [`elem2`](abapselect_into_target.md) · [`wa`](abapselect_into_target.md) · [`indicators`](abapselect_indicators.md) · [`itab`](abapselect_into_target.md) · [`indicators`](abapselect_indicators.md) · [`extended_result`](abapselect_extended_result.md) · [`creating`](abapselect_creating.md)

### Alternative

[1. `... INTO (elem1, elem2, ...)`](abapinto_clause.md#alternative-1)

[2. `... INTO [CORRESPONDING FIELDS OF] wa ...`](abapinto_clause.md#alternative-2)

[3. `... INTO|APPENDING [CORRESPONDING FIELDS OF] TABLE itab ...`](abapinto_clause.md#alternative-3)

## Overview

### Description

The additions `INTO` or `APPENDING` construct the `INTO` clause of a [`SELECT`](abapselect.md), [`WITH`](abapwith.md), or `FETCH` statement. They define which ABAP data objects are assigned the data of the result set of a query and how this assignment is made. The following options are available:

- An assignment to a parenthesized comma-separated list of individual elementary data objects [`elem1`](abapselect_into_target.md), [`elem2`](abapselect_into_target.md), .... specified after `INTO`.

- An assignment to a single work area [`wa`](abapselect_into_target.md) specified after `INTO`.

- An assignment to an internal table [`itab`](abapselect_into_target.md) specified after `INTO` or `APPENDING`.

The data objects [`elem1`](abapselect_into_target.md), [`elem2`](abapselect_into_target.md), ...., [`wa`](abapselect_into_target.md), and [`itab`](abapselect_into_target.md) can be specified as existing [host variables](abenabap_sql_host_variables.md) or declared inline using [`@DATA`](abapselect_into_target.md) or [`@FINAL`](abapselect_into_target.md). An addition [`NEW`](abapselect_into_target.md) makes it possible to create target areas implicitly as [anonymous data objects](../../abap-glossary/abenanonymous_data_object_glosry.md).

The additions have the following meaning:

- In writes to work areas `wa` and internal tables `itab`, `CORRESPONDING FIELDS OF` can be used to assign columns of the result set to identically named components of structured target areas.

- In writes to internal tables, `PACKAGE SIZE` can be used to split lines of the result set into packages.

- [`indicators`](abapselect_indicators.md) can be used to specify indicators. Currently, a [null indicator](../../abap-glossary/abennull_indicator_glosry.md) can be specified with information about whether a column of the result set contains the null value.

- [`extended_result`](abapselect_extended_result.md) can be used to provide an extended result in a result object.

- It may be necessary to use [`creating`](abapselect_creating.md) to define whether an [LOB](../../abap-glossary/abenlob_glosry.md) of the result set linked with an [LOB handle](../../abap-glossary/abenlob_handle_glosry.md) is a [data stream](../../abap-glossary/abendata_stream_glosry.md) or a [locator](../../abap-glossary/abenlocator_glosry.md).

These additions can all be used together with the following exceptions:

- The addition `CORRESPONDING FIELDS OF` cannot be used together with inline declarations [`@DATA`](abapselect_into_target.md) or [`@FINAL`](abapselect_into_target.md) for `wa` or `itab`.

- The addition `APPENDING` cannot be specified together with [`NEW`](abapselect_into_target.md).

If the target area is specified using field symbols or reference variables, and a `SELECT` loop is closed using [`ENDSELECT`](abapendselect.md), the data object referenced by a field symbol or reference variable is identified exactly once when the loop is entered. This data object is used as a target area in each loop pass. Any modifications to the assignment of a field symbol or reference variable within the loop are ignored.

The `INTO` clause must be the final clause of a [main query](../../abap-glossary/abenmainquery_glosry.md) and the additions [`UP TO`](abapselect_up_to_offset.md), [`OFFSET`](abapselect_up_to_offset.md), and [`abap_options`](abapselect_options.md) must be placed after the `INTO` clause.

**Note:** The `INTO` clause does not affect the result set defined by other clauses. Any optimizations do not change the scope of the specified result set.

### Hints

- The addition [`NEW`](abapselect_into_target.md) or other methods for creating [anonymous data objects](../../abap-glossary/abenanonymous_data_object_glosry.md) can be used to create suitable data objects for dynamically specified [`FROM` clauses](abapfrom_clause.md) or [`SELECT` lists](abapselect_list.md).

- Whether data should better be read into an internal table or a work area depends on the type of further processing: If data is required only once in a program, it should be imported into a work area, row by row, using a `SELECT` loop. Reading data into an internal table requires more memory space without compensating this disadvantage with a considerably higher reading speed. If, on the other hand, data is required many times in a program, it should be read into an internal table. The disadvantage of the increased memory requirement is more than compensated for here by the advantage of a once-only selection.

- If data is to be imported into an internal table, it is better to import it once into an internal table than to read it, row by row, into a work area and insert its content in the internal table.

- The `INTO` clause and its rules are not affected by the implicit [client handling](abenabap_sql_client_handling.md) of ABAP SQL. In particular, the client column of a target structure can be filled with other values than the client ID, for example when assigning individually specified columns of a [select list](abapselect_list.md).

- Reference variables for LOB handles or LOB handle structures cannot currently be specified after the statement `FETCH`.

## Alternative 1

`... INTO (elem1, elem2, ... )`

### Description

Specifies a parenthesized and comma-separated list of elementary data objects [`elem1`](abapselect_into_target.md), [`elem2`](abapselect_into_target.md), ... as target areas of the `INTO` clause. This specification is only possible if the columns of the result set are defined using one or more explicitly specified columns [`col_spec`](abapselect_clause_col_spec.md) in the [`SELECT` list](abapselect_list.md). Each of the data objects [`elem1`](abapselect_into_target.md), [`elem2`](abapselect_into_target.md), ... can be specified as existing [host variables](abenabap_sql_host_variables.md) or declared inline using [`@DATA`](abapselect_into_target.md) or [`@FINAL`](abapselect_into_target.md). The addition [`NEW`](abapselect_into_target.md) allows the creation of anonymous data objects.

The comma-separated list must have the same number of elements as columns in the result set. The content of the columns in the result set is assigned to the data objects specified in the list from left to right in accordance with the order specified after `SELECT`. [Assignment rules](abenselect_into_conversion.md) apply to the individual assignments. If an [LOB](../../abap-glossary/abenlob_glosry.md) is assigned to a reference variable for [LOB handles](../../abap-glossary/abenlob_handle_glosry.md), an [LOB handle is created](abenselect_into_lob_handles.md). If an [offset/length is specified](../abap-operands/abenoffset_length.md) to access a data object, `+off` must not be omitted. If the result set is empty, the data objects remain unchanged. If a catchable exception is raised when the data objects are written to, their content is undefined when the exception is handled.

If the result set consists of one row, the columns of this row are assigned to the data objects. If the result set has multiple rows, the statements [`SELECT`](abapselect.md) and [`WITH`](abapwith.md) are used to open a `SELECT` loop that itself must be closed using [`ENDSELECT`](abapendselect.md) or [`ENDWITH`](abapendwith.md). A `SELECT` loop assigns the columns of the result set to the data objects row by row and evaluates them. If used in the statement `FETCH`, the columns of the row are extracted at the current cursor position.

### Hints

- If the result set is defined in the [`SELECT` list](abapselect_list.md) by specifying `*` or `data_source~*`, it is not possible to specify a comma-separated list of data objects.

- Generally, whitespace characters are ignored within the parentheses and the comma-separated list can span multiple program lines. But if the opening bracket is followed by a whitespace, there also must be a whitespace in front of the closing bracket.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of the three columns of a result set to three elementary data objects. The first data object `carrid` is a previously declared host variable. The second data object `carrname` is a host variable declared inline. The third data object is an anonymous data object created using [`NEW`](abapselect_into_target.md) and to which a data reference variable `dref` declared inline points.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA carrid TYPE scarr-carrid. 
 
SELECT carrid, carrname, url 
       FROM scarr 
       ORDER BY carrid 
       INTO (@carrid, 
             @FINAL(carrname), 
             NEW @FINAL(dref)). 
  out->write( |{ carrid 
            }, { carrname 
            }, { dref->* } | ). 
ENDSELECT. 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of the four columns of a result set into four individually specified components of a structure. Unlike when writing to a work area using `CORRESPONDING FIELDS` (see below), the runtime framework does not compare names here.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: 
  BEGIN OF wa, 
    cityfrom TYPE spfli-cityfrom, 
    cityto   TYPE spfli-cityto, 
    carrid   TYPE spfli-carrid, 
    connid   TYPE spfli-connid, 
  END OF wa. 
 
SELECT SINGLE 
       FROM spfli 
       FIELDS carrid, connid, cityfrom, cityto 
       WHERE carrid = 'LH' AND connid = '400' 
       INTO (@wa-carrid, 
             @wa-connid, 
             @wa-cityfrom, 
             @wa-cityto). 
 
out->write( wa ). 
 
out->display( ).
```

## Alternative 2

`... INTO [CORRESPONDING FIELDS OF] wa`

### Description

Specifies a single work area [`wa`](abapselect_into_target.md) as a target area of the `INTO` clause. This can be specified for all result sets. The data object [`wa`](abapselect_into_target.md) can be specified as an existing [host variable](abenabap_sql_host_variables.md) or declared inline using [`@DATA`](abapselect_into_target.md) or [`@FINAL`](abapselect_into_target.md). The addition [`NEW`](abapselect_into_target.md) allows the creation of an anonymous data object.

If the result set consists of a single row, this row is assigned to the work area `wa`. If the result set has multiple rows, the statements [`SELECT`](abapselect.md) and [`WITH`](abapwith.md) are used to open a `SELECT` loop that itself must be closed using [`ENDSELECT`](abapendselect.md) or [`ENDWITH`](abapendwith.md). A `SELECT` loop assigns the result set to the work area `wa` row by row and evaluates it. After `ENDSELECT` or `ENDWITH`, the work area `wa` contains the row that was assigned last. If used in the `FETCH` statement, a row is extracted at the current cursor position. If the result is empty, the work area remains unchanged. If a catchable exception is raised when the work area is filled, its content is undefined when the exception is handled.

If the optional addition `CORRESPONDING FIELDS OF` is specified, `wa` must be a [structure](../../abap-glossary/abenstructure_glosry.md). This addition specifies that only the content of columns that have identically named components in `wa` is assigned to them. If the addition `CORRESPONDING FIELDS OF` is not specified, `wa` must meet the prerequisites described under [Work Areas in Statements](abenabap_sql_wa.md). The rows of the result set are assigned as follows, based on the definition of the result set in the [`SELECT` list](abapselect_list.md):

- **Definition of the result set using `*` without the addition `CORRESPONDING FIELDS OF`** in the `INTO` clause:

  If all columns of the data sources are read using `*`, `CORRESPONDING FIELDS` is not specified and the `SELECT` statement is not the main query of a [`WITH`](abapwith.md) statement, `SELECT` behaves as follows:

  - A work area without [LOB handle components](../../abap-glossary/abenlob_handle_component_glosry.md) is assigned the row of the result set, left-aligned and unconverted and in accordance with the structure of the result set. Unaffected parts of `wa` retain their previous content. To be able to access the components of the result set according to type after the assignment, the work area `wa` must be structured like the result set.

  - When an [LOB handle structure](../../abap-glossary/abenlob_handle_structure_glosry.md) is specified, it must be constructed exactly like the structure of the [data source](abapselect_data_source.md), in accordance with the [prerequisites](abenabap_sql_wa.md). The content of the columns of the result set that are not assigned to any [LOB handle components](../../abap-glossary/abenlob_handle_component_glosry.md) are directly assigned to the corresponding components of the work area. One [LOB handle](abenselect_into_lob_handles.md) is created for each LOB handle component.

- **All Other Combinations**

  If the result set consists of a single column specified explicitly after `SELECT` or a single [SQL expression](../../abap-glossary/abensql_expression_glosry.md) or a single [aggregate expression](../../abap-glossary/abenaggregate_expression_glosry.md), `wa` can be an elementary data object or a structure. If the result set consists of multiple columns, it must be a structure and the following rules apply:

  - If the addition `CORRESPONDING FIELDS` is not specified, `wa` must contain enough components and the content of the columns are assigned to the components of `wa` from left to right in the order specified after `SELECT`. The content of surplus components of `wa` is not changed.

  - If the addition `CORRESPONDING FIELDS` is specified, only those content of columns for which there are identically named components in `wa` are assigned to them. The alias names defined using [`AS`](abapselect_list.md) are respected. Columns and aggregate expressions that appear multiple times can only be assigned using alias names, if `CORRESPONDING FIELDS` is specified. If `wa` contains substructures, these are resolved by the addition `CORRESPONDING FIELDS` and the full names linked using the structure component selector are considered. If a column name occurs multiple times and no alias name was assigned, the last column listed is assigned.

[Assignment rules](abenselect_into_conversion.md) apply to the individual assignments. If an [LOB](../../abap-glossary/abenlob_glosry.md) of a reference variable for [LOB handles](../../abap-glossary/abenlob_handle_glosry.md) is assigned, an [LOB handle is created](abenselect_into_lob_handles.md). If an [offset/length is specified](../abap-operands/abenoffset_length.md) to access a substring of `wa`, `+off` must not be omitted.

If `CORRESPONDING FIELDS` is used, the columns of the result set defined in the [`SELECT` list](abapselect_list.md) must match the components of the target area on a certain level. Among other things, there must be at least one name match or there must be an identically named component in the target area for each explicitly specified column.

If `CORRESPONDING FIELDS` is used, an optimization takes place that removes columns that are not needed for the complete query from the result set: If one or more names match all the columns for which there are no name match and that are not required by other clauses of the ABAP SQL statement are not included in the result set. This is also true for `*` in the [`SELECT` list](abapselect_list.md). If there are no name matches, none of the columns are removed from the result set.

**Note:** The addition `CORRESPONDING FIELDS` does not violate the rule that an `INTO` clause does not affect the result set defined by other clauses.

### Hints

- The second point of the enumeration above, [All Other Combinations](abapinto_clause.md), also includes [`data_source~*`](abapselect_list.md) when specified in the [`SELECT` list](abapselect_list.md). In this case, `wa` must be a structure. This is particularly valid when only one data source [`data_source~*`](abapselect_data_source.md) is specified. Therefore, if a single `data_source~*` is specified, other rules apply than in the case where `*` is specified, even if the same result sets are defined both times.

- The addition `CORRESPONDING FIELDS` ignores names that were only defined using the addition `AS name` of the statement [`INCLUDE`](../abap-declarations/abapinclude_type.md) or when integrating the structures in the ABAP Dictionary. Any components renamed using the addition `RENAMING WITH SUFFIX` of the statement `INCLUDE` or renamed similarly in the ABAP Dictionary are, however, not ignored.

- If the addition `CORRESPONDING FIELDS` is used, fields with matching names (if known statically) are assigned when the program is generated or are otherwise assigned once when the `SELECT` statement is executed.

- If individual columns are read and the structure of the result set is known statically, it is recommended that a list of data objects or inline declarations is used instead of using the addition `CORRESPONDING FIELDS`.

- If the addition `INTO CORRESPONDING` is used and all the required information exists statically, the fields are assigned when the program is generated. Otherwise, the fields are assigned once when the `SELECT` statement is executed, which causes a slight increase in the required runtime.

- The fact, that the addition `INTO CORRESPONDING` does not affect the result set defined by other clauses, can be demonstrated by using it together with [`DISTINCT`](abapselect_clause.md), [`FOR ALL ENTRIES`](abenwhere_all_entries.md) or any other construct that requires the selection of specific columns. Then the optimization of the result set does not remove columns required by these constructs and their values are taken into account. This is shown by class `CL_DEMO_SELECT_DISTINCT_CORRES`. The additions `DISTINCT` and `FOR ALL ENTRIES` remove duplicate values as defined by the explicitly given `SELECT` list and not by the columns that match the names of the target area.

- The variants with the addition `INTO CORRESPONDING FIELDS` run the risk of having target areas with more components than are actually filled. This should only be the case if the components that are not filled are then filled in the program. Otherwise appropriately sized work areas should be used to avoid a large amount of memory being filled by initial values, especially in internal tables.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of all columns of a row of a result set into structured work areas. In the first `SELECT` statement, `wa` is a previously declared host variable. In the second `SELECT` statement, `wa_inl` is a host variable declared inline. In the third `SELECT` statement, the work area is created as an anonymous data object using [`NEW`](abapselect_into_target.md). This object is pointed to using a data reference variable `dref` declared inline.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA wa TYPE scarr. 
SELECT SINGLE * 
       FROM scarr 
       WHERE carrid = 'LH' 
       INTO @wa. 
 
SELECT SINGLE * 
       FROM scarr 
       WHERE carrid = 'LH' 
       INTO @FINAL(wa_inl). 
ASSERT wa_inl = wa. 
 
SELECT SINGLE * 
       FROM scarr 
       WHERE carrid = 'LH' 
       INTO NEW @FINAL(dref). 
ASSERT dref->* = wa. 
 
out->write( dref->* ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of the four columns of a result set into four respective components of the same name in a work area in a different order.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: 
  BEGIN OF wa, 
    cityfrom TYPE spfli-cityfrom, 
    cityto   TYPE spfli-cityto, 
    carrid   TYPE spfli-carrid, 
    connid   TYPE spfli-connid, 
  END OF wa. 
 
SELECT SINGLE 
       FROM spfli 
       FIELDS carrid, connid, cityfrom, cityto 
       WHERE carrid = 'LH' AND connid = '400' 
       INTO CORRESPONDING FIELDS OF @wa. 
 
out->write( wa ). 
 
out->display( ).
```

## Alternative 3

`... INTO|APPENDING [CORRESPONDING FIELDS OF] TABLE itab`

### Addition

[`... PACKAGE SIZE n`](abapinto_clause.md#addition)

### Description

Specifies an internal table [`itab`](abapselect_into_target.md) as a target area of the `INTO` clause. This can be specified for all result sets. The data object [`itab`](abapselect_into_target.md) can be specified as an existing [host variable](abenabap_sql_host_variables.md) or declared inline using [`@DATA`](abapselect_into_target.md) or [`@FINAL`](abapselect_into_target.md). The addition [`NEW`](abapselect_into_target.md) makes it possible to create an anonymous data object.

An internal table can only be specified after `INTO TABLE` or after `APPENDING TABLE` if the result set has multiple rows. The internal table can have any [table category](../../abap-glossary/abentable_category_glosry.md). Its row type must meet the same [prerequisites](abenabap_sql_wa.md) as a work area `wa`.

The result set with multiple rows is inserted into the internal table `itab` row-by-row in accordance with the rules of [`INSERT`](../abap-processing-internal-data/abapinsert_itab.md). A sorting process is executed in the case of a [sorted table](../../abap-glossary/abensorted_table_glosry.md).

- If `INTO` is used, the internal table is initialized before the rows are inserted.

- Preceding rows are preserved if `APPENDING` is used. `APPENDING` cannot be used together with the addition [`NEW`](abapselect_into_target.md).

If there is a conflict with an existing unique table key, an uncatchable exception is raised like in the case of the statement [`INSERT LINES OF`](../abap-processing-internal-data/abapinsert_itab_linespec.md).

Before any assignment of a row of the result set, an initial row of the internal table `itab` is created and the row of the result set is assigned to this row. When assigning a row of the result set to a row of the internal table with or without `CORRESPONDING FIELDS`, the same rules apply as when assigning to an individual work area `wa` (see above) with the exception that when inserting into internal tables, [LOB handles](../../abap-glossary/abenlob_handle_glosry.md) can be [created](abenselect_into_lob_handles.md) as [locators](../../abap-glossary/abenlocator_glosry.md) but not as [reader streams](../../abap-glossary/abenreader_stream_glosry.md).

If the addition `PACKAGE SIZE` is not specified, all rows of the result set are inserted into the internal table `itab` and the statements `ENDSELECT` or `ENDWITH` statement must not be specified after `SELECT` or `WITH`.

If the result set is empty, the internal table is initialized when `INTO` is used, and remains unchanged when `APPENDING` is used. If a catchable exception is raised when the internal table is filled, its content is undefined when the exception is handled.

### Hints

- When specifying an internal table with a unique [primary](../../abap-glossary/abenprimary_table_key_glosry.md) or [secondary table key](../../abap-glossary/abensecondary_table_key_glosry.md), an uncatchable exception is raised if an attempt is made to create a duplicate entry.

- If the internal table contains more columns than required when using the addition `CORRESPONDING FIELDS`, generally too much memory is being used by initial fields and a warning is raised by the syntax check. In cases where the columns are needed, for example, when they are filled with derived values by the program, a [pragma](../abap-syntax-elements-of-an-abap-program/abenpragma.md) can be used to bypass the warning.

- The maximum number of [data streams](../../abap-glossary/abendata_stream_glosry.md) that can be assigned to an ABAP SQL statement is limited to 16. This means that reader streams should not be created when importing internal tables.

- It is not recommended that a data object `itab` is declared inline with `@FINAL`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of all columns of all rows of a result set into structured internal tables. In the first `SELECT` statement, `itab` is a previously declared host variable. In the second `SELECT` statement, `itab_inl` is a host variable declared inline. In the third `SELECT` statement, the internal table is created as an anonymous data object using [`NEW`](abapselect_into_target.md). This object is pointed to using a data reference variable `dref` declared inline.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA itab TYPE STANDARD TABLE OF scarr 
          WITH EMPTY KEY. 
SELECT * 
       FROM scarr 
       ORDER BY carrid 
       INTO TABLE @itab. 
 
SELECT * 
       FROM scarr 
       ORDER BY carrid 
       INTO TABLE @FINAL(itab_inl). 
ASSERT itab_inl = itab. 
 
SELECT * 
       FROM scarr 
       ORDER BY carrid 
       INTO TABLE NEW @FINAL(dref). 
ASSERT dref->* = itab. 
 
out->write( dref->* ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of the four columns of a result set into four respective components of the same name in an internal table in a different order.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF wa, 
    cityfrom TYPE spfli-cityfrom, 
    cityto   TYPE spfli-cityto, 
    carrid   TYPE spfli-carrid, 
    connid   TYPE spfli-connid, 
  END OF wa. 
 
DATA itab TYPE SORTED TABLE OF wa WITH UNIQUE KEY table_line. 
 
SELECT FROM spfli 
       FIELDS carrid, connid, cityfrom, cityto 
       INTO CORRESPONDING FIELDS OF TABLE @itab. 
 
out->write( itab ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example for `APPENDING TABLE` creates the same internal table as the example for [`UNION`](abapunion.md).

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT FROM scarr 
       FIELDS carrname, 
              CAST( '-' AS CHAR( 4  ) ) AS connid, 
              CAST( '-' AS CHAR( 20 ) ) AS cityfrom, 
              CAST( '-' AS CHAR( 20 ) ) AS cityto 
       WHERE carrid = 'LH' 
       INTO TABLE @DATA(result). 
 
SELECT FROM spfli 
       FIELDS '-' AS carrname, 
             connid, 
             cityfrom, 
             cityto 
          WHERE carrid = 'LH' 
          APPENDING TABLE @result. 
 
SORT result BY carrname DESCENDING connid cityfrom cityto. 
 
out->write( result ). 
 
out->display( ).
```

## Addition

`... PACKAGE SIZE n`

### Description

If the addition `PACKAGE SIZE` is specified after `INTO|APPENDING TABLE`, the rows of the result set are inserted into the internal table `itab` in packages of `n` rows. In the case of the statements [`SELECT`](abapselect.md) and [`WITH`](abapwith.md), a `SELECT` loop is opened that itself must be closed using [`ENDSELECT`](abapendselect.md) or [`ENDWITH`](abapendwith.md). `n` expects a [host variable](abenabap_sql_host_variables.md), a [host expression](abenabap_sql_host_expressions.md), or a [literal](abenabap_sql_literals.md) of type `i` that contains the number of rows. If `n` is an untyped literal or a host variable, its content must match the data type `i` in accordance with the rules for a [lossless assignment](../../abap-glossary/abenlossless_assignment_glosry.md). `n` must have the type `b`, `s`, `i`, or `int8`. If the value of `n` is less than 0, an exception is raised that cannot be handled. If `n` is equal to 0, all rows of the result set are inserted into the internal table `itab`. If used in the statement `FETCH`, `n` rows are extracted from the current cursor position.

If `INTO` is used, the internal table is initialized before each insertion and, in the `SELECT` loop, it only contains the rows of the current package. If `APPENDING` is used, a further package is added to the existing rows of the internal table for each `SELECT` loop or for each extraction using `FETCH`.

After `ENDSELECT` or `ENDWITH`, the content of `itab` is not defined if `INTO` is used. That is, the table can either contain the rows of the last package or it can be initial. If `APPENDING` is used, the content of `itab` retains the state of the last loop pass.

### Hints

- The addition `PACKAGE SIZE` can be used after `INTO` to limit the amount of data read at once. Otherwise, a runtime error can occur when reading a data set that is too large into an internal table so that its [maximum size](../abap-data-types-and-data-objects/abenmemory_consumption_2.md) is exceeded. `PACKAGE SIZE` cannot prevent this runtime error after `APPENDING`.

- If the addition `PACKAGE SIZE` is specified with the addition [`FOR ALL ENTRIES`](abenwhere_all_entries.md), all selected rows are read into an internal system table initially and the packages are only created when they are passed from the system table to the actual target table. The addition `FOR ALL ENTRIES` thereby negates the effect of `PACKAGE SIZE` in preventing memory overflow.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading and output of the columns of the DDIC database table `SPFLI` in packages of 10 rows.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
SELECT carrid, connid, cityfrom, cityto 
       FROM spfli 
       ORDER BY carrid, connid, cityfrom, cityto 
       INTO  TABLE @FINAL(result) PACKAGE SIZE 10. 
  out->next_section( |Package { sy-dbcnt / 10 }| 
    )->write( result ). 
ENDSELECT. 
out->display( ).
```
