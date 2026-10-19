---
title: "CL_ABAP_CORRESPONDING, Simple Assignment"
source_file: abencl_abap_corresponding_1.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > CL_ABAP_CORRESPONDING, System Class"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CL_ABAP_CORRESPONDING, Simple Assignment

The methods `CREATE` and `EXECUTE` of the system class `CL_ABAP_CORRESPONDING` can be used to assign components between structures or between internal tables with a dynamically specified mapping rule.

The factory method `CREATE` is used to create a mapping object:

``` abap
`DATA(mapper) = cl_abap_corresponding=>create( source  = struct|itab 
                                              destination           = struct|itab 
                                              mapping               = mapping_tab 
                                              discarding_duplicates = flag ).`
```

Structures `struct` or internal tables `itab` of data types for which the assignment is to be executed must be passed to the parameters `source` and `destination`. An internal table of the type `CL_ABAP_CORRESPONDING=>MAPPING_TABLE`, which contains the mapping rule, must be passed to the parameter `mapping`. If an initial mapping table is passed, only the identically named components are assigned. The mapping table has the following components:

- `LEVEL`

  Level of the components in the structure or line structure. The value 0 represents the top level.

- `KIND`

  Mapping type. The possible values are:

  - `CL_ABAP_CORRESPONDING=>MAPPING_COMPONENT` (1) The components specified in this line are mapped to each other.

  - `CL_ABAP_CORRESPONDING=>MAPPING_EXCEPT_COMPONENT` (2) The component of the source structure specified in this line is excluded from the mapping of identically named components.

  - `CL_ABAP_CORRESPONDING=>MAPPING_EXCEPT_ALL` (3) All components of the current source structure are excluded from the mapping of identically name components.

  - `CL_ABAP_CORRESPONDING=>MAPPING_DISCARDING_DUPLICATES` (9) In a source table, duplicate rows are ignored as when using [`DISCARDING DUPLICATES`](abencorresponding_constr_dupl.md) in a mapping rule of the component operator. The target table must have a unique table key.

- `SRCNAME`

  Component of the source structure.

- `DSTNAME`

  Component of the target structure.

The lines of the internal table must be constructed so that they result in a mapping rule in the correct order. Components of the source structure for which no mapping is defined and that were not excluded are assigned identically named components of the target structure.

The method `EXECUTE` of a mapping object can be used to perform any number of assignments between structures or internal tables `src` and `dst` whose data type matches the source type or target type specified when the object was created:

``` abap
`mapper->execute( EXPORTING source        = src 
                           keeping_lines = flag 
                 CHANGING  destination = dst ).`
```

The assignment is performed component by component

- between the components specified in the mapping rule

- between the remaining identically named components at the same level if they were not excluded in the mapping rule.

In assignments between structures, components of the target structure to which no components of the source structure are assigned keep their previous value, like the statement [`MOVE-CORRESPONDING`](abapmove-corresponding.md) and like the operator [`CORRESPONDING`](abencorresponding_constr_arg_type.md) with the addition `BASE`. Nested internal tables are always resolved, as if the addition `EXPANDING NESTED TABLES` is specified in `MOVE-CORRESPONDING` or the addition `DEEP` for the operator `CORRESPONDING`. In assignments between internal tables, the target table is always initialized first. The additions `KEEPING TARGET LINES` in `MOVE-CORRESPONDING` or `BASE` in `CORRESPONDING` are reflected in the optional parameter `KEEPING_LINES` which represents a flag. If it is not flagged, internal table lines are not retained.

If the value *X* was passed to the parameter `DISCARDING_DUPLICATES` of the method `CREATE`, duplicate rows are handled in tabular component assignments in the same way as when using the addition [`DISCARDING DUPLICATES`](abencorresponding_constr_dupl.md) in the basic form of the component operator. Here, the target table must have a unique table key.

The source and the target may be the same. However, it should be noted that, unlike in the operator [`CORRESPONDING`](abencorresponding_constr_arg_type.md) for reflexive assignments. the target object is used directly like in the statement [`MOVE-CORRESPONDING`](abapmove-corresponding.md) and no temporary interim result is created.

The passing of incorrect parameters to the methods of the class `CL_ABAP_CORRESPONDING` raises exceptions of the class `CX_CORR_DYN_ERROR`.

## Hints

- Using the `CREATE` method comes with performance costs. Hence, `CL_ABAP_CORRESPONDING` should be used if the created instance is reused within the code.

- The methods `CREATE` and `EXECUTE` of the system class `CL_ABAP_CORRESPONDING` implement an assignment similar to the statement

  dst = [`CORRESPONDING`](abencorresponding_constr_arg_type.md) \#( BASE ( dst ) struct\|itab [`MAPPING ... EXCEPT ...`](abencorresponding_constr_mapping.md) ). Here, the [mapping rule](abencorresponding_constr_mapping.md) is specified dynamically, however, as the content of a special internal table.

- The same restrictions apply as to the operator [`CORRESPONDING`](abencorresponding_constr_arg_type.md). Components can only be mapped to each other if they are on the same level. Components of a substructure cannot be assigned to the components at higher levels and vice versa.

- The class `CL_ABAP_CORRESPONDING` always resolves tabular components, which corresponds to the behavior of the operator [`CORRESPONDING`](abencorresponding_constr_arg_type.md) if a mapping rule is specified. In this case, the addition `DEEP` is also set implicitly.

- To achieve the same results for standalone components in assignments between structures as in the operator [`CORRESPONDING`](abencorresponding_constr_arg_type.md) without the addition `BASE`, an initial structure can be assigned to the parameter `destination`.

- The [pseudo component](../../abap-glossary/abenpseudo_component_glosry.md) `table_line` cannot be addressed in the mapping table.

- In reflexive assignments between components of the same object, as in [`MOVE-CORRESPONDING`](abapmove-corresponding.md), it should be noted that the processing order is not defined and that a call of the method `EXECUTE` cannot be used to swap the content of two components.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of the class `CL_ABAP_CORRESPONDING` for assignments of components to a simple structure. The mapping rule specifies that the components `a3` are assigned to `b1` and `a1` to `b3`. The component `a2` is ignored since there are no identically named components in the target structure and `b2` keeps its value. `a4` and `a5` in the target structure also keep their values, even though the source structure contains identically named components, since the value of `CL_ABAP_CORRESPONDING=>MAPPING_EXCEPT_ALL` is specified for the mapping type for all non-specified components. The executable [example for simple structures](abencl_abap_corr_dyn_abexa.md) enables interactive input of the component names that are mapped to each other.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: 
  BEGIN OF struct1, 
    a1 TYPE string VALUE 'a1', 
    a2 TYPE string VALUE 'a2', 
    a3 TYPE string VALUE 'a3', 
    a4 TYPE string VALUE 'a4', 
    a5 TYPE string VALUE 'a5', 
  END OF struct1, 
  BEGIN OF struct2, 
    b1 TYPE string VALUE 'b1', 
    b2 TYPE string VALUE 'b2', 
    b3 TYPE string VALUE 'b3', 
    a4 TYPE string VALUE 'b4', 
    a5 TYPE string VALUE 'b5', 
  END OF struct2. 
 
FINAL(mapper) = 
  cl_abap_corresponding=>create( 
    source            = struct1 
    destination       = struct2 
    mapping           = VALUE cl_abap_corresponding=>mapping_table( 
      ( level = 0 kind = 1 srcname = 'a1' dstname = 'b3' ) 
      ( level = 0 kind = 1 srcname = 'a3' dstname = 'b1' ) 
      ( level = 0 kind = 3 ) ) ). 
 
mapper->execute( EXPORTING source      = struct1 
                 CHANGING  destination = struct2 ). 
 
out->write( struct2 ). 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example demonstrates the use of the `KEEPING_LINES` parameter. An assignment is done for structures containing an internal table as component. The first call of the `EXECUTE` method does not include the `KEEPING_LINES` parameter, i. e. it is not flagged by default. In the second call of the `EXECUTE` method, the parameter is flagged, i. e. existing table lines are retained.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: BEGIN OF line1, 
         col1 TYPE c LENGTH 1, 
         col2 TYPE c LENGTH 1, 
       END OF line1, 
       BEGIN OF line2, 
         col1 TYPE c LENGTH 1, 
         col2 TYPE c LENGTH 1, 
         col3 TYPE c LENGTH 1, 
       END OF line2. 
 
DATA: 
  BEGIN OF struc_a, 
    comp   TYPE c LENGTH 1, 
    itab_a TYPE TABLE OF line1 WITH EMPTY KEY, 
  END OF struc_a, 
 
  BEGIN OF struc_b, 
    comp   TYPE c LENGTH 1, 
    itab_b TYPE TABLE OF line2 WITH EMPTY KEY, 
  END OF struc_b. 
 
struc_a = VALUE #( comp   = 'A' 
                   itab_a = VALUE #( ( col1 = 'a' col2 = 'b' ) 
                                     ( col1 = 'c' col2 = 'd' ) ) ). 
struc_b = VALUE #( comp = 'B' 
                   itab_b = VALUE #( 
                     ( col1 = 'Z' col2 = 'Y' col3 = 'X' ) 
                     ( col1 = 'W' col2 = 'V' col3 = 'U' )  ) ). 
 
DATA(struc_c) = struc_b. 
 
FINAL(mapper) = 
  cl_abap_corresponding=>create( 
    source            = struc_a 
    destination       = struc_b 
    mapping           = VALUE cl_abap_corresponding=>mapping_table( 
      ( level = 0 kind = 1 srcname = 'itab_a' dstname = 'itab_b' ) ) ). 
 
mapper->execute( EXPORTING source      = struc_a 
                 CHANGING  destination = struc_b ). 
 
out->write( struc_b ). 
 
FINAL(mapper2) = 
  cl_abap_corresponding=>create( 
    source            = struc_a 
    destination       = struc_c 
    mapping           = VALUE cl_abap_corresponding=>mapping_table( 
      ( level = 0 kind = 1 srcname = 'itab_a' dstname = 'itab_b' ) ) ). 
 
mapper2->execute( EXPORTING source        = struc_a 
                            keeping_lines = abap_true 
                  CHANGING  destination = struc_c ). 
 
out->write( struc_c ). 
 
out->display( ).
```

## Executable Examples

- [`CL_ABAP_CORRESPONDING` for Simple Structures](abencl_abap_corr_dyn_abexa.md)

- [`CL_ABAP_CORRESPONDING` for Nested Structures](abencl_abap_corr_struc_abexa.md)

- [`CL_ABAP_CORRESPONDING` for Internal Tables](abencl_abap_corr_itab_abexa.md)

- [`CL_ABAP_CORRESPONDING` for Tabular Components](abencl_abap_corr_deep_abexa.md)
