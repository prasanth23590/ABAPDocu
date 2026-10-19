---
title: "CL_ABAP_CORRESPONDING, Assignment of Values"
source_file: abencl_abap_corresponding_3.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > CL_ABAP_CORRESPONDING, System Class"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CL_ABAP_CORRESPONDING, Assignment of Values

The method `CREATE_WITH_VALUE` of the system class `CL_ABAP_CORRESPONDING` has essentially the same function as the method [`CREATE`](abencl_abap_corresponding_1.md). Additionally, the values of any data objects can be assigned to the components of the target structure or target table.

The factory method `CREATE_WITH_VALUE` creates a mapping object:

``` abap
`DATA(mapper) = 
  cl_abap_corresponding=>create_with_value( source                = struct|itab 
                                            destination           = struct|itab 
                                            mapping               = mapping_tab 
                                            discarding_duplicates = flag ).`
```

For the parameters `source` and `destination`, the same applies as to the method [`CREATE`](abencl_abap_corresponding_1.md). An internal table of the type `CL_ABAP_CORRESPONDING=>MAPPING_TABLE_VALUE` that contains the mapping rule, must be passed to the parameter `mapping`. This mapping table has the same components, with the same meaning as a mapping table of type [`CL_ABAP_CORRESPONDING=>MAPPING_TABLE`](abencl_abap_corresponding_1.md) with an additional column and further values for the column `KIND`:

- `VALUE`

  In this column, a reference to a suitable data object can be specified, whose value is assigned to the component of the target structure that is specified in `DSTNAME`.

- `KIND`

  The additional values for the mapping type are:

  - `CL_ABAP_CORRESPONDING=>MAPPING_VALUE` (16), the value specified in `VALUE` is always assigned. The column `SRCNAME` must be initial

  - `CL_ABAP_CORRESPONDING=>MAPPING_DEFAULT_VALUE` (32), the value specified in `VALUE` is only assigned if the component specified in the column `SRCNAME` is initial. The component name in `SRCNAME` must exist in the source structure.

A mapping object created with `CREATE_WITH_VALUE` is used like a mapping object created with [`CREATE`](abencl_abap_corresponding_1.md) with the method `EXECUTE`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The component `b2` is given the value *xxx* and the component `b3` is given the value *yyy*. The components `b1` and `b4` are given the values of the assigned components `a1` and `a4` of the source structure.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: 
  BEGIN OF struct1, 
    a1 TYPE string VALUE 'a1', 
    a2 TYPE string VALUE 'a2', 
    a3 TYPE string VALUE '  ', 
    a4 TYPE string VALUE 'a4', 
  END OF struct1, 
  BEGIN OF struct2, 
    b1 TYPE string VALUE 'b1', 
    b2 TYPE string VALUE 'b2', 
    b3 TYPE string VALUE 'b3', 
    b4 TYPE string VALUE 'b4', 
  END OF struct2. 
 
FINAL(mapper) = 
  cl_abap_corresponding=>create_with_value( 
    source            = struct1 
    destination       = struct2 
    mapping           = VALUE 
      cl_abap_corresponding=>mapping_table_value( 
        ( level = 0 kind = 1  srcname = 'a1' dstname = 'b1' ) 
        ( level = 0 kind = 16                dstname = 'b2' 
                                             value = REF #( `xxx` ) ) 
        ( level = 0 kind = 32 srcname = 'a3' dstname = 'b3' 
                                             value = REF #( `yyy` ) ) 
        ( level = 0 kind = 32 srcname = 'a4' dstname = 'b4' 
                                             value = REF #( `zzz` ) ) 
         ) ). 
 
mapper->execute( EXPORTING source      = struct1 
                 CHANGING  destination = struct2 ). 
 
out->write( struct2 ). 
 
out->display( ).
```
