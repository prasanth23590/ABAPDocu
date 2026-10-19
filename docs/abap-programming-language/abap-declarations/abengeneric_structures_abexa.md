---
title: "Partially Generic Structures"
source_file: abengeneric_structures_abexa.html
section: "ABAP Programming Language > ABAP - Declarations > Typing > typing Addition > typing Addition, generic_type > ANY STRUCTURE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Partially Generic Structures

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example class explores working with partially generic structures that include both field symbols and formal parameters.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_generic_structures DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
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
           END OF ts_4, 
           gen_struc   TYPE ANY STRUCTURE 
                       CONTAINING %cid_ref TYPE abp_behv_cid 
                                  %is_draft TYPE abp_behv_flag 
                                  %control TYPE ANY STRUCTURE, 
           request_tab TYPE INDEX TABLE OF gen_struc 
            WITH FURTHER SECONDARY KEYS, 
           cid_ref_tab TYPE SORTED TABLE OF abp_behv_cid 
            WITH UNIQUE KEY table_line, 
           update_root TYPE TABLE FOR UPDATE demo_managed_draft_root. 
    DATA: struc_1 TYPE ts_1, 
          struc_2 TYPE ts_2, 
          struc_3 TYPE ts_3, 
          struc_4 TYPE ts_4, 
          update  TYPE update_root. 
    METHODS: assignments IMPORTING out TYPE REF TO if_demo_output, 
      move IMPORTING out TYPE REF TO if_demo_output, 
      assignments_ddic_types IMPORTING out TYPE REF TO if_demo_output, 
      include_structures IMPORTING out TYPE REF TO if_demo_output, 
      itabs_generic_struc_type IMPORTING out TYPE REF TO if_demo_output, 
      static_implementation IMPORTING out TYPE REF TO if_demo_output 
                                      request_static TYPE update_root 
                            EXPORTING cid_ref_tab TYPE cid_ref_tab 
                            RETURNING VALUE(result) TYPE REF TO data, 
      dynamic_implementation IMPORTING out TYPE REF TO if_demo_output 
                                       request_dynamic TYPE ANY TABLE 
                                   VALUE(dyn_where_clause) TYPE string 
                             EXPORTING cid_ref_tab TYPE cid_ref_tab 
                             RETURNING VALUE(result) TYPE REF TO data, 
      generic_implementation IMPORTING out TYPE REF TO if_demo_output 
                                       request_generic TYPE request_tab 
                             EXPORTING cid_ref_tab TYPE cid_ref_tab 
                             RETURNING VALUE(result) TYPE REF TO data, 
      populate_structures. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_generic_structures IMPLEMENTATION. 
  METHOD main. 
 
    out->write( `*********** assignments ***********` ). 
    assignments( out ). 
    out->write( `*********** assignments_ddic_types ***********` ). 
    assignments_ddic_types( out ). 
    out->write( `*********** move ***********` ). 
    move( out ). 
    out->write( `*********** include_structures ***********` ). 
    include_structures( out ). 
    out->write( `*********** itabs_generic_struc_type ***********` ). 
    itabs_generic_struc_type( out ). 
    out->write( `*********** static_implementation ***********` ). 
    static_implementation( out = out request_static = update ). 
    out->write( `*********** dynamic_implementation ***********` ). 
    dynamic_implementation( out = out request_dynamic = update 
    dyn_where_clause = `%is_draft = if_abap_behv=>mk-off ` && 
                       `and %control is not initial` ). 
    out->write( `*********** generic_implementation ***********` ). 
    generic_implementation( out = out request_generic = update ). 
 
  ENDMETHOD. 
  METHOD assignments_ddic_types. 
 
 
    TYPES: BEGIN OF ts_time, 
             time TYPE t, 
           END OF ts_time. 
    DATA(struc_time) = VALUE ts_time( time = CONV t( '123456' ) ). 
 
    TYPES ts_gen_tims TYPE ANY STRUCTURE 
      CONTAINING time TYPE demo_ddic_types-tims. 
    FIELD-SYMBOLS <gs_tims> TYPE ts_gen_tims. 
 
    ASSIGN struc_time TO <gs_tims>. 
 
    out->write( <gs_tims> ). 
 
    TYPES ts_gen_timn TYPE ANY STRUCTURE 
      CONTAINING time TYPE demo_ddic_types-timn. 
    FIELD-SYMBOLS <gs_timn> TYPE ts_gen_timn. 
 
    "No assignment possible due to type incompatibility 
    "ASSIGN struc_time TO <gs_timn>. 
 
  ENDMETHOD. 
  METHOD assignments. 
 
    populate_structures( ). 
 
    TYPES: ts_gen_1 TYPE ANY STRUCTURE CONTAINING comp1 TYPE i 
                                                  comp2 TYPE i, 
           ts_gen_2 TYPE ANY STRUCTURE CONTAINING comp2 TYPE i 
                                                  comp3 TYPE i. 
 
    FIELD-SYMBOLS <gs_1> TYPE ts_gen_1. 
    FIELD-SYMBOLS <gs_2> TYPE ts_gen_2. 
 
    "Identical component list with compatible types 
    ASSIGN struc_1 TO <gs_1>. 
 
    out->write( <gs_1> ). 
 
    "Component list matches, but different order 
    ASSIGN struc_2 TO <gs_1>. 
 
    out->write( <gs_1> ). 
 
    "Component list of partially generic structure matches, 
    "assigned structure contains additional components 
    ASSIGN struc_3 TO <gs_1>. 
 
    out->write( <gs_1> ). 
 
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
 
    out->write( <gs_2> ). 
 
    "Not matching component list; no assignment possible 
    "ASSIGN struc_4 TO <gs_2>. 
 
  ENDMETHOD. 
  METHOD move. 
 
    populate_structures( ). 
 
    out->write( struc_2 ). 
 
    "Position-based movement 
    struc_2 = struc_1. 
    ASSERT struc_2-comp1 <> 3. 
    ASSERT struc_2-comp2 <> 4. 
 
    out->write( struc_2 ). 
 
    FIELD-SYMBOLS <s1> TYPE data. 
    FIELD-SYMBOLS <s2> TYPE data. 
    ASSIGN struc_1 TO <s1>. 
    ASSIGN struc_2 TO <s2>. 
 
    out->write( <s1> ). 
    out->write( <s2> ). 
 
    <s2> = <s1>. 
 
    out->write( <s1> ). 
    out->write( <s2> ). 
 
    TYPES ts_gen TYPE ANY STRUCTURE CONTAINING comp1 TYPE i. 
    FIELD-SYMBOLS <s4> TYPE ts_gen. 
    ASSIGN struc_1 TO <s4>. 
 
    out->write( <s4> ). 
 
    struc_2 = <s4>. 
 
    out->write( struc_2 ). 
 
    "Corresponding move 
    populate_structures( ). 
 
    ASSIGN struc_1 TO <s4>. 
 
    MOVE-CORRESPONDING <s4> TO struc_2. 
 
    out->write( struc_2 ). 
 
    populate_structures( ). 
 
    ASSIGN struc_1 TO <s4>. 
 
    struc_2 = CORRESPONDING #( <s4> ). 
 
    out->write( struc_2 ). 
  ENDMETHOD. 
  METHOD populate_structures. 
    struc_1 = VALUE #( comp1 = 1 comp2 = 2 ). 
    struc_2 = VALUE #( comp2 = 3 comp1 = 4 ). 
    struc_3 = VALUE #( comp1 = 5 comp2 = 6 comp3 = 7 
                       comp4 = 8 comp5 = 9 ). 
    struc_4 = VALUE #( comp1 = 10 comp2 = 11 ). 
  ENDMETHOD. 
  METHOD include_structures. 
 
    TYPES: BEGIN OF s1, 
             comp1 TYPE i, 
           END OF s1, 
           BEGIN OF s2. 
             INCLUDE TYPE s1 AS substruc. 
    TYPES: comp2 TYPE i, 
             comp3 TYPE i, 
           END OF s2. 
 
    TYPES t_gs1 TYPE ANY STRUCTURE CONTAINING substruc TYPE s1 
                                              comp2 TYPE i. 
 
    DATA(struct_1) = VALUE s2( substruc-comp1 = 1 comp2 = 2 
                               comp3 = 3 ). 
 
    FIELD-SYMBOLS <fs1> TYPE t_gs1. 
 
    ASSIGN struct_1 TO <fs1>. 
 
    out->write( <fs1> ). 
 
    TYPES: BEGIN OF s3. 
             INCLUDE TYPE s1 AS substruc RENAMING WITH SUFFIX _sub. 
    TYPES:   comp2 TYPE i, 
             comp3 TYPE i, 
           END OF s3. 
 
    DATA(struct_2) = VALUE s3( substruc-comp1 = 4 comp2 = 5 
                               comp3 = 6 ). 
 
    "Not compatible due to renaming with suffix 
    "ASSIGN struct_3 TO <fs1>. 
 
    TYPES t_gs2 TYPE ANY STRUCTURE CONTAINING comp2 TYPE i 
                                              comp1_sub TYPE i. 
 
    FIELD-SYMBOLS <fs2> TYPE t_gs2. 
 
    ASSIGN struct_2 TO <fs2>. 
 
    out->write( <fs2> ). 
 
    TYPES t_gs3 TYPE ANY STRUCTURE CONTAINING comp2 TYPE i 
                                              substruc TYPE s1. 
 
    FIELD-SYMBOLS <fs3> TYPE t_gs2. 
 
    ASSIGN struct_2 TO <fs3>. 
 
    out->write( <fs3> ). 
  ENDMETHOD. 
  METHOD itabs_generic_struc_type. 
 
    TYPES: BEGIN OF ts_5, 
             comp_a TYPE i, 
             comp_b TYPE c LENGTH 10, 
             comp_c TYPE decfloat34, 
             comp_d TYPE string, 
           END OF ts_5, 
           tab_type1 TYPE TABLE OF ts_5 WITH EMPTY KEY. 
 
    TYPES: c10         TYPE c LENGTH 10, 
           t_gs4 TYPE ANY STRUCTURE CONTAINING comp_b TYPE c10 
                                               comp_c TYPE decfloat34 
                                               comp_a TYPE i, 
           tab_type_gs TYPE TABLE OF t_gs4 WITH EMPTY KEY. 
 
    FIELD-SYMBOLS <tgs> TYPE tab_type_gs. 
 
    DATA(itab1) = VALUE tab_type1( 
    ( comp_a = 1 comp_b = 'a' 
      comp_c = CONV decfloat34( '1.1' ) comp_d = `hello` ) 
    ( comp_a = 2 comp_b = 'b' 
      comp_c = CONV decfloat34( '2.2' ) comp_d = `world` ) 
    ( comp_a = 3 comp_b = 'c' 
      comp_c = CONV decfloat34( '3.3' ) comp_d = `ABAP` ) ). 
 
    ASSIGN itab1 TO <tgs>. 
 
    out->write( <tgs> ). 
 
    TYPES: BEGIN OF ts_6, 
             comp_a TYPE i, 
             comp_b TYPE c LENGTH 10, 
           END OF ts_6, 
           tab_type2 TYPE TABLE OF ts_6 WITH EMPTY KEY. 
 
    DATA(itab2) = VALUE tab_type2( ( comp_a = 4 comp_b = 'd' ) 
                                   ( comp_a = 5 comp_b = 'e' ) ). 
 
    <tgs> = CORRESPONDING #( BASE ( <tgs> ) itab2 ). 
 
    out->write( <tgs> ). 
 
    struc_1 = VALUE #( comp1 = 6 comp2 = 7 ). 
    DATA itab3 LIKE TABLE OF struc_1 WITH EMPTY KEY. 
    APPEND struc_1 TO itab3. 
 
    <tgs> = CORRESPONDING #( BASE ( <tgs> ) 
      itab3 MAPPING comp_a = comp1 comp_b = comp2 ). 
 
    out->write( <tgs> ). 
 
    LOOP AT <tgs> ASSIGNING FIELD-SYMBOL(<wa>). 
      <wa>-comp_b = to_upper( <wa>-comp_b ). 
      ASSIGN <wa>-('comp_d') TO FIELD-SYMBOL(<comp>). 
      <comp> = to_upper( <comp> ). 
    ENDLOOP. 
 
    SORT <tgs> BY comp_a DESCENDING. 
 
    out->write( <tgs> ). 
 
    READ TABLE <tgs> ASSIGNING FIELD-SYMBOL(<line>) 
      WITH KEY comp_b = 'C'. 
 
    IF <line> IS ASSIGNED. 
      out->write( <line> ). 
    ENDIF. 
 
    DATA(ref) = REF #( <tgs>[ 5 ] OPTIONAL ). 
 
    out->write( ref->* ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
 
    update = VALUE #( 
      ( %cid_ref = `cid1` %control-field1 = if_abap_behv=>mk-on ) 
      ( %cid_ref = `cid2` %control-field1 = if_abap_behv=>mk-on ) 
      ( %cid_ref = `cid3` %control-field1 = if_abap_behv=>mk-on 
        %is_draft = if_abap_behv=>mk-on ) 
      ( %cid_ref = `cid4` %control-field1 = if_abap_behv=>mk-on 
        %is_draft = if_abap_behv=>mk-on ) 
      ( %cid_ref = `cid5` ) 
      ( %cid_ref = `cid6` ) ). 
  ENDMETHOD. 
  METHOD dynamic_implementation. 
 
    CREATE DATA result LIKE request_dynamic. 
 
    dyn_where_clause = 
      cl_abap_dyn_prg=>escape_quotes( dyn_where_clause ). 
 
    LOOP AT request_dynamic ASSIGNING FIELD-SYMBOL(<instance>) 
      WHERE (dyn_where_clause). 
 
      INSERT <instance> INTO TABLE result->*. 
      INSERT <instance>-('%cid_ref') INTO TABLE cid_ref_tab. 
 
    ENDLOOP. 
 
    out->write( result->* ). 
    out->write( cid_ref_tab ). 
  ENDMETHOD. 
  METHOD generic_implementation. 
    CREATE DATA result LIKE request_generic. 
 
    LOOP AT request_generic ASSIGNING FIELD-SYMBOL(<instance>) 
      WHERE %is_draft = if_abap_behv=>mk-off 
      AND %control IS NOT INITIAL. 
 
      INSERT <instance> INTO TABLE result->*. 
      INSERT <instance>-%cid_ref INTO TABLE cid_ref_tab. 
 
    ENDLOOP. 
 
    out->write( result->* ). 
    out->write( cid_ref_tab ). 
  ENDMETHOD. 
  METHOD static_implementation. 
 
    CREATE DATA result LIKE request_static. 
 
    LOOP AT request_static ASSIGNING FIELD-SYMBOL(<instance>) 
      USING KEY id 
      WHERE %is_draft = if_abap_behv=>mk-off 
      AND %control IS NOT INITIAL. 
 
      INSERT <instance> INTO TABLE result->*. 
      INSERT <instance>-%cid_ref INTO TABLE cid_ref_tab. 
 
    ENDLOOP. 
 
    out->write( result->* ). 
    out->write( cid_ref_tab ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The following example contexts are included:

- Assigning non-generic structures to field symbols typed with partially generic structured types using `ASSIGN statements`, highlighting component definitions.

- Structure assignments that emphasize position-based and name-based movements.

- Structure assignments that emphasize the enforcing of strict checks regarding elementary dictionary types.

- Non-generic structures with include structures assigned to partially generic structures.

- Internal tables with a line type of partially generic structured type.

- Three approaches to implement an algorithm: static, dynamic, and generic implementation. In three example methods, content from an internal table typed with a BDEF derived type should be extracted, returning only instances where the draft indicator is disabled and the `%control` structure is not initial. Additionally, `%cid_ref` values are returned. The static implementation is valid only for one specific type, while the dynamic implementation applies to all concrete types that meet the required dynamic criteria. The generic method establishes necessary criteria for the expected structures while ensuring type compliance.
