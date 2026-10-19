---
title: "ABAP EML - READ, Field Specification Expressions"
source_file: abeneml_read_op_fields_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > READ ENTITY, ENTITIES > Examples for ABAP EML READ"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - READ, Field Specification Expressions

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates read operations using various variants of field specification expressions so as to read from a simple managed [RAP BO](../../abap-glossary/abenrap_bo_glosry.md).

The example covers read and read-by-association operations as well as a read operation executing a function. The following field specification alternatives are covered in the example:

- `FROM`

- `FIELDS (...) WITH`

- `ALL FIELDS WITH`

**Data model**

The CDS data model consists of the root entity `DEMO_SPFLI_FLIGHTS` and its child entity `DEMO_SFLIGHT`. The root entity represents flight schedule data and the child entity represents flight details.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@Metadata.allowExtensions: true
@EndUserText.label: 'spfli view'
define root view entity DEMO_SPFLI_FLIGHTS
  as select from spfli
  composition [0..*] of DEMO_SFLIGHT as _Flights
  {
    key spfli.carrid    as Carrid,
    key spfli.connid    as Connid,
        spfli.countryfr as Countryfr,
        spfli.cityfrom  as Cityfrom,
        spfli.airpfrom  as Airpfrom,
        spfli.countryto as Countryto,
        spfli.cityto    as Cityto,
        spfli.airpto    as Airpto,
        spfli.fltime    as Fltime,
        spfli.deptime   as Deptime,
        spfli.arrtime   as Arrtime,
        spfli.distance  as Distance,
        spfli.distid    as Distid,
        spfli.fltype    as Fltype,
        spfli.period    as Period,
        _Flights
  }
```

Child entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_SFLIGHT
  as select from sflight
  association to parent DEMO_SPFLI_FLIGHTS as _Spfli 
    on  $projection.Carrid = _Spfli.Carrid
    and $projection.Connid = _Spfli.Connid
  {
    key sflight.carrid     as Carrid,
    key sflight.connid     as Connid,
    key sflight.fldate     as Fldate,
        sflight.price      as Price,
        sflight.currency   as Currency,
        sflight.planetype  as Planetype,
        sflight.seatsmax   as Seatsmax,
        sflight.seatsocc   as Seatsocc,
        sflight.paymentsum as Paymentsum,
        sflight.seatsmax_b as SeatsmaxB,
        sflight.seatsocc_b as SeatsoccB,
        sflight.seatsmax_f as SeatsmaxF,
        sflight.seatsocc_f as SeatsoccF,
        _Spfli
  }
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_SPFLI_FLIGHTS` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_spfli_flights unique;
strict(2);

define behavior for DEMO_SPFLI_FLIGHTS
persistent table SPFLI
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  association _Flights { create; }
  function (authorization:none) FunctionResultEntity result [1] $self;
  field ( readonly ) carrid, connid;
}

define behavior for DEMO_SFLIGHT alias SFLIGHT
persistent table SFLIGHT
lock dependent by _spfli
authorization dependent by _spfli
{
  update;
  delete;
  field ( readonly ) carrid, connid, fldate;
  mapping for SFLIGHT corresponding
  {
  SeatsmaxB = seatsmax_b;
  SeatsmaxF = seatsmax_f;
  SeatsoccF = seatsocc_f;
  SeatsoccB = seatsocc_b;
  }
  association _spfli;
}
```

**Behavior implementation**

For the above RAP behavior definition, there is an [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) available. The global class of the behavior pool is `BP_DEMO_SPFLI_FLIGHTS`. This global class implements the local handler class `LHC_DEMO_SPFLI_FLIGHTS`. The actual implementation takes place in the `BP_DEMO_SPFLI_FLIGHTS=========CCIMP`. In managed scenarios, the implementation for standard operations is carried out by the managed RAP BO provider. Hence, only the function `FunctionResultEntity` which is executed in a read operation in the example is relevant here. See the example [`READ`: Operation Executing Functions](abeneml_read_op_func_abexa.md) that focuses on this very function execution for details.

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
CLASS cl_demo_rap_eml_read_op_fields DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_read_op_fields IMPLEMENTATION. 
  METHOD main. 
 
    "Read operation 
    "FROM 
    READ ENTITY demo_spfli_flights 
    FROM VALUE #( 
        ( %key-carrid = 'AA' 
          %key-connid = 17 
          %control = VALUE #( airpfrom  = if_abap_behv=>mk-on 
                              airpto    = if_abap_behv=>mk-on 
                              cityfrom  = if_abap_behv=>mk-on 
                              cityto    = if_abap_behv=>mk-on 
                              countryfr = if_abap_behv=>mk-on 
                              countryto = if_abap_behv=>mk-on 
                              deptime   = if_abap_behv=>mk-off 
                              arrtime   = if_abap_behv=>mk-off 
                              distance  = if_abap_behv=>mk-off 
                              fltime    = if_abap_behv=>mk-on 
                            ) ) ) 
      RESULT FINAL(read_from) 
      FAILED FINAL(failed_from). 
 
    out->next_section( `Read: FROM` ). 
    IF failed_from-demo_spfli_flights IS NOT INITIAL. 
      LOOP AT failed_from-demo_spfli_flights 
        ASSIGNING FIELD-SYMBOL(<failed_from>). 
        out->write( <failed_from>-%fail ). 
      ENDLOOP. 
    ELSE. 
      out->write( read_from ). 
    ENDIF. 
 
    "FIELDS (...) WITH 
    READ ENTITY demo_spfli_flights 
     FIELDS ( carrid connid airpfrom airpto 
              cityfrom cityto 
               ) 
       WITH VALUE #( ( %key-carrid = 'LH' 
                       %key-connid = 400 ) ) 
      RESULT FINAL(read_fields_with) 
      FAILED FINAL(failed_fields_with). 
 
    out->next_section( `Read: FIELDS (...) WITH` ). 
    IF failed_fields_with-demo_spfli_flights IS NOT INITIAL. 
      LOOP AT failed_fields_with-demo_spfli_flights 
        ASSIGNING FIELD-SYMBOL(<failed_fields_with>). 
        out->write( <failed_fields_with>-%fail ). 
      ENDLOOP. 
    ELSE. 
      out->write( read_fields_with ). 
    ENDIF. 
 
    "ALL FIELDS WITH 
    READ ENTITY demo_spfli_flights 
    ALL FIELDS WITH VALUE #( ( %key-carrid = 'LH' 
                               %key-connid = 401  ) ) 
     RESULT FINAL(read_all_fields_with) 
     FAILED FINAL(failed_all_fields_with). 
 
    out->next_section( `READ: ALL FIELDS WITH` ). 
    IF failed_all_fields_with-demo_spfli_flights IS NOT INITIAL. 
      LOOP AT failed_all_fields_with-demo_spfli_flights 
        ASSIGNING FIELD-SYMBOL(<failed_all_fields_with>). 
        out->write( <failed_all_fields_with>-%fail ). 
      ENDLOOP. 
    ELSE. 
      out->write( read_all_fields_with ). 
    ENDIF. 
 
    "Read-by-association operation 
    "FROM 
    READ ENTITY demo_spfli_flights 
    BY \_flights 
    FROM VALUE #( ( %key-carrid = 'AA' 
                    %key-connid = 17 
                    %control = VALUE #( seatsocc = if_abap_behv=>mk-on ) 
                  ) ) 
     RESULT FINAL(rba_from) 
     FAILED FINAL(failed_rba_from). 
 
    out->next_section( `Read by association: FROM` ). 
    IF failed_rba_from-demo_spfli_flights IS NOT INITIAL. 
      LOOP AT failed_rba_from-demo_spfli_flights 
        ASSIGNING FIELD-SYMBOL(<failed_rba_from>). 
        out->write( <failed_rba_from>-%fail ). 
      ENDLOOP. 
    ELSE. 
      SELECT * FROM @rba_from AS rba_from 
        INTO TABLE @FINAL(rba_from_selected) UP TO 3 ROWS. 
      out->write( rba_from_selected ). 
    ENDIF. 
 
    "FIELDS (...) WITH 
    READ ENTITY demo_spfli_flights 
    BY \_flights 
    FIELDS ( carrid connid currency price planetype ) 
     WITH VALUE #( ( %key-carrid = 'AA' 
                     %key-connid = 17 ) ) 
     RESULT FINAL(rba_fields_with) 
     FAILED FINAL(failed_rba_fields_with). 
 
    out->next_section( `Read by association: FIELDS (...) WITH` ). 
    IF failed_rba_fields_with-demo_spfli_flights IS NOT INITIAL. 
      LOOP AT failed_rba_fields_with-demo_spfli_flights 
        ASSIGNING FIELD-SYMBOL(<failed_rba_fields_with>). 
        out->write( <failed_rba_fields_with>-%fail ). 
      ENDLOOP. 
    ELSE. 
      SELECT * FROM @rba_fields_with AS rba_fields_with 
        INTO TABLE @FINAL(rba_fields_with_selected) UP TO 3 ROWS. 
      out->write( rba_fields_with_selected ). 
    ENDIF. 
 
    "ALL FIELDS WITH 
    READ ENTITY demo_spfli_flights 
    BY \_flights 
    ALL FIELDS WITH VALUE #( ( %key-carrid = 'LH' 
                               %key-connid = 401 ) ) 
     RESULT FINAL(rba_all_fields_with) 
     FAILED FINAL(failed_rba_all_fields_with). 
 
    out->next_section( `Read by association: ALL FIELDS WITH` ). 
    IF failed_rba_all_fields_with-demo_spfli_flights IS NOT INITIAL. 
      LOOP AT failed_rba_all_fields_with-demo_spfli_flights 
        ASSIGNING FIELD-SYMBOL(<failed_rba_all_fields_with>). 
        out->write( <failed_rba_all_fields_with>-%fail ). 
      ENDLOOP. 
    ELSE. 
      SELECT * FROM @rba_all_fields_with AS rba_all_fields_with 
        INTO TABLE @FINAL(rba_all_fields_with_selected) UP TO 3 ROWS. 
      out->write( rba_all_fields_with_selected ). 
    ENDIF. 
 
    "Read operation executing a function 
    "FROM 
    READ ENTITY demo_spfli_flights 
         EXECUTE functionresultentity 
         FROM VALUE #( ( %tky-carrid =  'AA' 
                         %tky-connid = 17 ) ) 
        RESULT FINAL(execute_from) 
        FAILED FINAL(failed_execute_from). 
 
    "Set up internal table to output 
    "the result of the function execution. 
    TYPES: BEGIN OF result_structure, 
             carrid   TYPE s_carr_id, 
             connid   TYPE s_conn_id, 
             cityfrom TYPE s_from_cit, 
             airpfrom TYPE s_fromairp, 
             cityto   TYPE s_to_city, 
             airpto   TYPE s_toairp, 
           END OF result_structure. 
 
    TYPES result_table_type TYPE TABLE OF result_structure. 
    DATA execute_from_result TYPE result_table_type. 
 
    LOOP AT execute_from   ASSIGNING FIELD-SYMBOL(<execute_from>). 
      APPEND VALUE #( carrid = <execute_from>-%param-carrid 
                      connid =  <execute_from>-%param-connid 
                      cityfrom =  <execute_from>-%param-cityfrom 
                      airpfrom =  <execute_from>-%param-airpfrom 
                      cityto  =  <execute_from>-%param-cityto 
                      airpto =  <execute_from>-%param-airpto 
                    ) TO execute_from_result. 
    ENDLOOP. 
 
    out->next_section( `Read operation executing a function` ). 
    IF failed_execute_from-demo_spfli_flights IS NOT INITIAL. 
      LOOP AT failed_execute_from-demo_spfli_flights 
        ASSIGNING FIELD-SYMBOL(<failed_execute_from>). 
        out->write( <failed_execute_from>-%fail ). 
      ENDLOOP. 
    ELSE. 
      out->write( execute_from_result ). 
    ENDIF. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

Using the short syntax form `READ ENTITY`, several separate read and read-by-association operations are carried out in the example showcasing the various variants of field specification that are possible to specify input parameters for the read operation in an internal table. In this case, the internal table is always created at an operand position using the [value operator](../../abap-programming-language/abap-creating-objects-and-values/abenconstructor_expression_value.md). The table gets the required [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) automatically. Depending on the operation and key words (`FROM`, for example), the internal tables require specific components.

The RAP query engine reads the data from the respective database tables into a managed [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md) in which the read operations take place using the respective additions. Each result of the individual read operations is output. For the sake of completeness, an example for the read operation executing a function is covered here as well. Refer to the separate example [`READ`: Operation Executing Functions](abeneml_read_op_func_abexa.md) for the details.
