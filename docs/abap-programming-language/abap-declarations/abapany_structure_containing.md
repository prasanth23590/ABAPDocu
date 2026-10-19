---
title: "TYPES, ANY STRUCTURE CONTAINING"
source_file: abapany_structure_containing.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Data Types > TYPES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPES, ANY STRUCTURE CONTAINING

## Syntax

``` abap
... TYPE ANY STRUCTURE CONTAINING component_list.  
```

## Description

Used to create partially generic structured types. These types impose constraints by predefining a set of components (`component_list`) following the `CONTAINING` addition. The component list (`component_list`), which is not separated by commas, can include one or more components.

The syntax can be used for creating local types with `TYPES` statements, not for directly typing field symbols and formal parameters, unlike when using the fully generic types `ANY STRUCTURE` without the `CONTAINING` addition. They must be typed with the locally declared types.

The components of `component_list` can have both generic and non-generic types. These syntax options are supported for typing:

- `TYPE non_generic_type`

- `TYPE REF TO ...`

- `TYPE LINE OF ...`

- `TYPE generic_type` (all [generic ABAP types](../../abap-glossary/abengeneric_abap_type_glosry.md) such as `ANY`, `ANY STRUCTURE`, `ANY TABLE`, `c`, and so on, except for `TABLE`)

To assign non-generic structures to partially generic structures, the order of the defined components in the partially generic structures is irrelevant. However, the components of the non-generic structure must match the components of the generic structured type. The component names must be identical, and their types must be compatible. Additionally, the non-generic structure can include more components than those available in the partially generic type. Two partially generic structured types are compatible if their constraints in the component list do not contradict each other in terms of component names and types.

The compatibility rule for identical names and compatible types also applies to substructures of partially generic structures and partially generic structured line types of internal tables.

[Strict compatibility checks](../../abap-dictionary-ddic/ddic-built-in-data-types/abapmapping_ddic_abap.md) are enforced for components with elementary types, especially regarding dictionary types.

Generic structured types can be used for defining [formal parameters](../../abap-glossary/abenformal_parameter_glosry.md) and field symbols. The following criteria apply to typing formal parameters with generic structured types:

- Any optional parameter requires the specification of a default value.

- Importing and changing parameters can be specified with fully generic structured types when they are mandatory or defined as default by specifying a default structure.

- Exporting parameters cannot be defined with generic structured types since their passing is inherently optional.

- Returning parameters cannot be defined with generic structured types because the formal parameter must be completely typed.

- In the case of AMDP database procedures, parameters cannot be defined with generic structured types.

## Hints

- Concrete data objects cannot be declared with generic structured types because there is no implicit type completion. This differs from other generic ABAP types, such as the generic type `c`, which automatically completes to type `c LENGTH 1`.

- Casting generic types to character-like types (such as type `c`) is not supported because the compiler handles generic structures as deep structures.

- In ABAP SQL, generic structures are not allowed as target areas.

- Generic structures cannot be used for table parameters or as global interfaces for function modules.

- Regarding include structures, there is no special handling for component aliases.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example demonstrates the creation of local types that are partially generic structured types. These types are used to define field symbols. The example highlights the following aspects:

- Assignments succeed when there are no conflicts with component names and their types.

- Assignments succeed even if the order of the component list differs.

- Assignments succeed when the component lists match, and the assigned structure can include additional components.

- Strict compatibility checks are enforced for elementary dictionary types.

- Component aliases with include structures

``` abap
"Non-generic structured types 
TYPES: BEGIN OF ts_1, 
         comp1 TYPE i, 
         comp2 TYPE i, 
       END OF ts_1, 
       BEGIN OF ts_2, 
         comp2 TYPE i, 
         comp1 TYPE i, 
       END OF ts_2, 
       BEGIN OF ts_3, 
         comp1 TYPE i, 
         comp2 TYPE i, 
         comp3 TYPE i, 
         comp4 TYPE i, 
         comp5 TYPE i, 
       END OF ts_3, 
       BEGIN OF ts_4, 
         comp1 TYPE i, 
         comp2 TYPE int8, 
       END OF ts_4. 
 
DATA: struc_1 TYPE ts_1, 
      struc_2 TYPE ts_2, 
      struc_3 TYPE ts_3, 
      struc_4 TYPE ts_4. 
 
"Locally declared partially generic structured types 
TYPES: ts_gen_1 TYPE ANY STRUCTURE CONTAINING comp1 TYPE i 
                                              comp2 TYPE i, 
       ts_gen_2 TYPE ANY STRUCTURE CONTAINING comp2 TYPE i 
                                              comp3 TYPE i. 
 
FIELD-SYMBOLS <gs_1> TYPE ts_gen_1. 
FIELD-SYMBOLS <gs_2> TYPE ts_gen_2. 
 
"Identical component list with compatible types 
ASSIGN struc_1 TO <gs_1>. 
 
"Component list matches, but different order 
ASSIGN struc_2 TO <gs_1>. 
 
"Component list of partially generic structure matches, 
"assigned structure contains additional components 
ASSIGN struc_3 TO <gs_1>. 
 
"Component names match, but there is a type incompatibility; 
"no assignment possible 
"ASSIGN struc_4 TO <gs_1>. 
 
"Not matching component list; no assignment possible 
"ASSIGN struc_1 TO <gs_2>. 
 
"Not matching component list; no assignment possible 
"ASSIGN struc_2 TO <gs_2>. 
 
"Component list of partially generic structure matches, 
"assigned structure contains additional components 
ASSIGN struc_3 TO <gs_2>. 
 
"Not matching component list; no assignment possible 
"ASSIGN struc_4 TO <gs_2>. 
 
"Strict checks regarding elementary dictionary types 
TYPES: BEGIN OF ts_time, 
         time TYPE t, 
       END OF ts_time. 
DATA struc_time TYPE ts_time. 
 
TYPES ts_gen_tims TYPE ANY STRUCTURE 
  CONTAINING time TYPE demo_ddic_types-tims. 
FIELD-SYMBOLS <gs_tims> TYPE ts_gen_tims. 
 
ASSIGN struc_time TO <gs_tims>. 
 
TYPES ts_gen_timn TYPE ANY STRUCTURE 
  CONTAINING time TYPE demo_ddic_types-timn. 
FIELD-SYMBOLS <gs_timn> TYPE ts_gen_timn. 
 
"No assignment possible due to type incompatibility 
"ASSIGN struc_time TO <gs_timn>. 
 
"Example with include structure 
TYPES: BEGIN OF ts_5, 
         comp1 TYPE i, 
       END OF ts_5, 
       BEGIN OF ts_6. 
         INCLUDE TYPE ts_5 AS substruct. 
TYPES: comp2 TYPE i, 
         comp3 TYPE i, 
       END OF ts_6. 
 
DATA struct TYPE ts_6. 
 
"comp1 can be accessed both by comp1 and substruct-comp1 
struct-comp1 = 1. 
struct-substruct-comp1 = 1. 
struct-comp2 = 2. 
struct-comp3 = 3. 
 
TYPES t_gts_5 TYPE ANY STRUCTURE CONTAINING substruct TYPE ts_5 
                                            comp2 TYPE i. 
 
FIELD-SYMBOLS <fts_5> TYPE t_gts_5. 
ASSIGN struct TO <fts_5>. 
 
"The structure is also compatible with the following generic 
"structured type, as there is no special handling for component 
"aliases, and it meets the constraints set by the generic structure, 
"even though comp1 in the example is essentially specified twice. 
TYPES t_gts_6 TYPE ANY STRUCTURE CONTAINING substruct TYPE ts_5 
                                            comp1 TYPE i. 
 
FIELD-SYMBOLS <fts_6> TYPE t_gts_6. 
ASSIGN struct TO <fts_6>.
```

## Executable Example

The example [Partially Generic Structures](abengeneric_structures_abexa.md) explores different contexts for using partially generic structures.
