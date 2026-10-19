---
title: "ABAP EML - READ, Variants"
source_file: abeneml_read_alternatives_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > READ ENTITY, ENTITIES > Examples for ABAP EML READ"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - READ, Variants

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the variants of the ABAP EML `READ` statement to read data from a simple managed [RAP BO](../../abap-glossary/abenrap_bo_glosry.md):

- `READ ENTITY bdef`

- `READ ENTITIES OF bdef`

- `READ ENTITIES OPERATIONS dynop`

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

For the above RAP behavior definition, one [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_SPFLI_FLIGHTS`. This global class implements the local handler class `LHC_DEMO_SPFLI_FLIGHTS`. The actual implementation takes place in the `BP_DEMO_SPFLI_FLIGHTS=========CCIMP`. The details of the behavior implementation are not relevant for this example since no custom operations are used here.

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
CLASS cl_demo_rap_eml_read DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_read IMPLEMENTATION. 
  METHOD main. 
 
    "READ ENTITY bdef 
    READ ENTITY demo_spfli_flights 
    ALL FIELDS WITH VALUE #( ( %key-Carrid = 'AA' 
                               %key-Connid = 17 ) ) 
     RESULT FINAL(read_entity) 
     FAILED FINAL(read_failed). 
 
    out->next_section( 'READ ENTITY bdef' ). 
 
    IF read_failed-demo_spfli_flights IS NOT INITIAL. 
      out->write( 'Read failed' ). 
    ELSE. 
      out->write( read_entity ). 
    ENDIF. 
 
********************************************************************** 
 
    "READ ENTITY bdef (read-by-association operation) 
    READ ENTITY demo_spfli_flights 
      BY \_Flights 
      ALL FIELDS WITH VALUE #( ( %key-Carrid = 'LH' 
                                 %key-Connid = 400 ) ) 
      RESULT FINAL(rba) 
      FAILED FINAL(rba_failed). 
 
    out->next_section( 
    'READ ENTITY bdef (read-by-association operation)' ). 
 
    SELECT * FROM @rba AS flight_tab 
      INTO TABLE @FINAL(read_entity_by_assoc) UP TO 3 ROWS. 
 
    IF rba_failed-demo_spfli_flights IS NOT INITIAL. 
      out->write( 'Read failed' ). 
    ELSE. 
      out->write( read_entity_by_assoc ). 
    ENDIF. 
 
********************************************************************** 
 
    "Get a flight date. 
    SELECT fldate FROM sflight AS flight_tab 
    WHERE carrid = 'LH' AND connid = 402 
    INTO TABLE @FINAL(fldate_tab). 
 
    "READ ENTITIES OF bdef 
    READ ENTITIES OF demo_spfli_flights 
      ENTITY demo_spfli_flights 
        ALL FIELDS WITH VALUE #( ( %key-Carrid = 'LH' 
                                   %key-connid = 401 ) ) 
        RESULT FINAL(read_entities_of) 
      ENTITY sflight 
        "All key fields must be specified. 
        ALL FIELDS WITH 
           VALUE #( ( %key-carrid = 'LH' 
                      %key-connid = 402 
                      fldate = VALUE #( fldate_tab[ 1 ] OPTIONAL ) ) ) 
        RESULT FINAL(read_entities_child) 
      ENTITY demo_spfli_flights 
        BY \_Flights 
        ALL FIELDS WITH 
            VALUE #( ( %key-Carrid = 'AA' 
                       %key-connid = 17 ) ) 
        RESULT FINAL(rba2) 
        FAILED FINAL(read_entities_failed). 
 
    SELECT * FROM @rba2 AS flight_tab2 
       INTO TABLE @FINAL(read_entities_by_assoc) UP TO 3 ROWS. 
 
    out->next_section( 'READ ENTITIES OF bdef' ). 
 
    IF read_entities_failed-demo_spfli_flights IS NOT INITIAL. 
      out->write( 'Read failed' ). 
    ELSE. 
      out->write( read_entities_of 
        )->write( read_entities_child 
        )->write( read_entities_by_assoc 
        ). 
    ENDIF. 
 
********************************************************************** 
 
    "READ ENTITIES OPERATIONS op_tab 
    DATA: 
      op_tab          TYPE abp_behv_retrievals_tab, 
      read_dyn        TYPE TABLE FOR READ IMPORT demo_spfli_flights, 
      read_dyn_result TYPE TABLE FOR READ RESULT demo_spfli_flights, 
      rba_dyn         TYPE TABLE FOR READ IMPORT 
                          demo_spfli_flights\_Flights, 
      rba_dyn_result  TYPE TABLE FOR READ RESULT 
                          demo_spfli_flights\_Flights, 
      rba_dyn_link    TYPE TABLE FOR READ LINK 
                          demo_spfli_flights\_Flights. 
 
    read_dyn = VALUE #( 
      ( %key-Carrid = 'DL' 
        %key-connid = 106 
        %control = VALUE #( 
           Airpfrom  = if_abap_behv=>mk-on 
           Airpto    = if_abap_behv=>mk-on 
           Arrtime   = if_abap_behv=>mk-on 
           Cityfrom  = if_abap_behv=>mk-on 
           Cityto    = if_abap_behv=>mk-on 
           Countryfr = if_abap_behv=>mk-on 
           Countryto = if_abap_behv=>mk-on 
           Deptime   = if_abap_behv=>mk-on 
           Fltime    = if_abap_behv=>mk-on 
           Distance  = if_abap_behv=>mk-on 
           Distid    = if_abap_behv=>mk-on 
           Fltype    = if_abap_behv=>mk-on 
           Period    = if_abap_behv=>mk-on 
                          ) 
                          ) ). 
 
    rba_dyn = VALUE #( 
     ( %key-Carrid = 'AZ' 
       %key-connid = 555 
       %control = VALUE #( Fldate     = if_abap_behv=>mk-on 
                           Price      = if_abap_behv=>mk-on 
                           Currency   = if_abap_behv=>mk-on 
                           Planetype  = if_abap_behv=>mk-on 
                           Seatsmax   = if_abap_behv=>mk-on 
                           Seatsocc   = if_abap_behv=>mk-on 
                          ) ) ). 
 
    op_tab = VALUE #( 
       ( op = if_abap_behv=>op-r-read "op = 'R' also possible 
         entity_name = 'DEMO_SPFLI_FLIGHTS' 
         instances   = REF #( read_dyn ) 
         results = REF #( read_dyn_result ) ) 
       ( op = if_abap_behv=>op-r-read_ba "op = 'N' also possible 
         entity_name = 'DEMO_SPFLI_FLIGHTS' 
         sub_name = '_FLIGHTS' 
         full = abap_true 
         instances   = REF #( rba_dyn ) 
         results = REF #( rba_dyn_result ) 
         links = REF #( rba_dyn_link ) ) 
                  ). 
 
    READ ENTITIES OPERATIONS op_tab FAILED FINAL(failed_dyn). 
 
    SELECT * FROM @rba_dyn_result AS flight_tab3 
      INTO TABLE @FINAL(read_by_assoc_dyn) UP TO 3 ROWS. 
 
    out->next_section( 'READ ENTITIES OPERATIONS op_tab' ). 
 
    IF failed_dyn IS NOT INITIAL. 
      out->write( 'Read failed' ). 
    ELSE. 
      out->write( read_dyn_result 
      )->write( read_by_assoc_dyn 
      )->write( rba_dyn_link ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

- `READ ENTITY bdef`

  Two read operations are executed with the statement `READ ENTITY` for single entities. The one for the root entity, the other for the child entity using a read-by-association operation. The mandatory results of the read operations are stored in an internal table which is declared inline. In doing so, the internal table gets the required [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md). The RAP query engine reads the data from the respective database tables into a managed [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md) in which the read operations take place using the `ALL FIELDS WITH` addition.

- `READ ENTITIES OF bdef`

  Multiple operations are executed on multiple RAP BO entities. In this case, read operations on the root entity, the child entity directly (mentioning the alias name defined in the BDEF) as well as a read-by-association operation (here, it is the association to the child entity) are covered.

- `READ ENTITIES OPERATIONS dynop`

  The example demonstrates a dynamic read operation on the root entity and a dynamic read-by-association operation on the child entity. For that purpose, an internal table with type `ABP_BEHV_RETRIEVALS_TAB` must be defined. This table includes specific parameters that must be filled, among others, references to other internal tables holding components according to which the dynamic read operation should be carried out.
