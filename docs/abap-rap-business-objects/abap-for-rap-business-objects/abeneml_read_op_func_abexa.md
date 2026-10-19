---
title: "ABAP EML - READ, Operation Executing Functions"
source_file: abeneml_read_op_func_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > READ ENTITY, ENTITIES > Examples for ABAP EML READ"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - READ, Operation Executing Functions

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how a `READ` statement can be used to access a managed RAP BO and execute a function. In this case, a selected set of fields is read from a RAP BO entity by executing a function.

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

For the above RAP behavior definition, one [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_SPFLI_FLIGHTS`. This global class implements the local handler class `LHC_DEMO_SPFLI_FLIGHTS`. The actual implementation takes place in the `BP_DEMO_SPFLI_FLIGHTS=========CCIMP`. In the example, the `FunctionResultEntity` method comprises an ABAP EML read operation reading the values of a selected set of fields from the entity `DEMO_SPFLI_FLIGHTS` according to specific keys that are specified in the internal table following the `... EXECUTE FunctionResultEntity FROM ...` statement in the report.

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
CLASS cl_demo_rap_eml_read_op_func DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_rap_eml_read_op_func IMPLEMENTATION. 
  METHOD main. 
 
    "Read operation executing a function 
    READ ENTITIES OF demo_spfli_flights 
     ENTITY demo_spfli_flights 
      EXECUTE FunctionResultEntity 
      FROM VALUE #( ( %tky-Carrid = 'AA' 
                      %tky-Connid = 17 ) 
                    ( %tky-Carrid = 'AZ' 
                      %tky-Connid = 555 ) 
                       ) 
     RESULT FINAL(result) 
     FAILED FINAL(failed) 
     REPORTED FINAL(reported). 
 
    out->next_section( 
      'Result of READ operation executing a function:' 
      )->write( result ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

- The `READ` statement executes the function `FunctionResultEntity` for those entity instances whose keys are specified in the internal table following the `... EXECUTE FunctionResultEntity FROM ...` statement.

- The outcome of the function execution is stored in the table `result`. In this case, the function `FunctionResultEntity` first reads a selected set of fields from [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md). Then, a calculation is carried out if a selected field has a certain value (the distance of a flight connection is converted to kilometers if the distance is stored as miles). The read result is then passed to the `result` table.

- To display the result of the read operation, an internal table is set up and filled with the values returned by the read operation.
