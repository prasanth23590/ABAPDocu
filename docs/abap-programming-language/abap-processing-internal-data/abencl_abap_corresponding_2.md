---
title: "CL_ABAP_CORRESPONDING, Lookup Table"
source_file: abencl_abap_corresponding_2.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > CL_ABAP_CORRESPONDING, System Class"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CL_ABAP_CORRESPONDING, Lookup Table

The methods `CREATE_USING` and `EXECUTE_USING` of the system class `CL_ABAP_CORRESPONDING` can be used to assign components between internal tables with a dynamically specified mapping rule. The source table acts as a lookup table.

The factory method `CREATE_USING` is used to create a mapping object:

``` abap
`DATA(mapper) = cl_abap_corresponding=>create_using( destination = itab 
                                                    using       = lookup_tab 
                                                    mapping     = mapping_tab ).`
```

Internal tables `itab` and `lookup_table` of the table types to which the assignment is to be made must be passed to the parameters `destination` and `using`. An internal table of the type `CL_ABAP_CORRESPONDING=>MAPPING_TABLE` that contains the mapping rule, must be passed to the parameter `mapping`. The mapping table has the same components as in the methods for [simple assignments](abencl_abap_corresponding_1.md) with the following special semantics:

- `KIND`

  Mapping type. Additional possible values are:

  - `CL_ABAP_CORRESPONDING=>USING_KEY` (4), the table key of the lookup table used for the evaluation is specified in the component `SRCNAME` in this line. The table must contain such a line.

  - `CL_ABAP_CORRESPONDING=>MAPPING_USING_COMPONENT` (5), the name of a column of the lookup table in `SRCNAME` is linked with the name of a column of the target table in `DSTNAME` in a line like this. All key fields of the table key used must be covered by a line like this.

    The mapping types for [simple assignments](abencl_abap_corresponding_1.md) can also be used and have the same semantics as described here.

The method `EXECUTE_USING` of a mapping object can be used to perform any number of assignments between tables `lookup_src` and `dst` whose data type matches the source type or target type `lookup_tab` or `itab` specified when the object was created:

``` abap
` mapper->execute_using( EXPORTING using       = lookup_src 
                       CHANGING  destination = dst ).`
```

For each line in `dst`, a line is searched for in the lookup table `lookup_src` that matches this line in accordance with the relationship defined using the mapping type `CL_ABAP_CORRESPONDING=>MAPPING_USING_COMPONENT` in the mapping table. If the key is not unique, the first line found is used. If no line like this is found, the line from `dst` remains unchanged. If a line like this is found in `lookup_src`, it is assigned to the line from `dst` in accordance with the rules of [`MOVE-CORRESPONDING` for structures](abapmove-corresponding.md) using the addition `EXPANDING NESTED TABLES`, with the following exception. The components used for the search are not assigned by default. The lines in the mapping table with mapping types for [simple assignments](abencl_abap_corresponding_1.md) can be used to override the default assignment of identically named components and the default exclusion of the components used for the search. It is not possible to specify the same table for `dst` and `lookup_src`, otherwise the runtime error `CORRESPONDING_SELF` occurs.

## Hints

- The methods `CREATE_USING` and `EXECUTE_USING` of the system class `CL_ABAP_CORRESPONDING` implement an assignment similar to the statement

  dst = [`CORRESPONDING`](abencorresponding_constr_using.md) \#( dst FROM lookup_tab KEY key_name ... ). However, the columns used for comparison between the target table and lookup table and the [mapping rule](abencorresponding_constr_mapping.md) are specified dynamically as the content of a special internal table.

- In the mapping table, the columns of the target table `dst` are part of the column `DSTNAME`, regardless of the mapping type, and the columns of the lookup table are part of the column `SRCNAME`. In the [`CORRESPONDING`](abencorresponding_constr_using.md) operator, however, the arrangement of the operands after `USING` is different from the arrangement after `MAPPING`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example shows the implementation of the example of component operator [`CORRESPONDING` with lookup table](abencorresponding_constr_using.md) to class `CL_ABAP_CORRESPONDING`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF line, 
    value   TYPE i, 
    comment TYPE string, 
  END OF line, 
  itab1 TYPE STANDARD TABLE OF line WITH EMPTY KEY, 
  itab2 TYPE HASHED TABLE OF line WITH UNIQUE KEY value. 
 
DATA(itab1) = VALUE itab1( FOR i = 1 UNTIL i >= 10 ( value = i ) ). 
FINAL(itab2) = VALUE itab2( ( value = 2 comment = `...` ) 
                           ( value = 3 comment = `...` ) 
                           ( value = 5 comment = `...` ) 
                           ( value = 8 comment = `...` ) ). 
 
FINAL(mapping_tab) = VALUE cl_abap_corresponding=>mapping_table( 
  ( level = 0 kind = 4 srcname = 'PRIMARY_KEY' ) 
  ( level = 0 kind = 5 srcname = 'VALUE' dstname = 'VALUE' ) ). 
 
cl_abap_corresponding=>create_using( 
     destination       = itab1 
     using             = itab2 
     mapping           = mapping_tab 
     )->execute_using( EXPORTING using       = itab2 
                       CHANGING  destination = itab1 ). 
 
out->write( itab1 ). 
 
out->display( ).
```

## Executable Example

[`CL_ABAP_CORRESPONDING` with Lookup Table](abencl_abap_corr_lookup_abexa.md)
