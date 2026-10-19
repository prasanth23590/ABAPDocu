---
title: "CDS DDL - CDS Enumerated Type, Use"
source_file: abencds_enum_abexa.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Type Definitions > CDS DDL - DEFINE TYPE > ABAP CDS - Enumerated Types > CDS DDL - DEFINE TYPE ENUM"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS Enumerated Type, Use

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the use of [CDS enumerated types](../../abap-glossary/abencds_enum_type_glosry.md).

The following CDS enumerated type `DEMO_CDS_ENUM_WEEKDAY` has the base type `abap.int1`, the names of the enumerated constants are abbreviations for the days of the week and the enumerated values are 0 to 6.

``` abap
@EndUserText.label: 'Days of the week' 
define type DEMO_CDS_ENUM_WEEKDAY : abap.int1 enum 
{  
  @EndUserText.label: 'Monday' 
  MON = initial; 
  @EndUserText.label: 'Tuesday' 
  TUE =       1; 
  @EndUserText.label: 'Wednesday' 
  WED =       2; 
  @EndUserText.label: 'Thursday' 
  THU =       3; 
  @EndUserText.label: 'Friday' 
  FRI =       4; 
  @EndUserText.label: 'Saturday' 
  SAT =       5; 
  @EndUserText.label: 'Sunday' 
  SUN =       6; 
} 
 
 
```

The CDS table function `DEMO_CDS_TF_ENUM_WEEKDAY` selects from the database table `SFLIGHT`.

**CDS table function**

``` abap
@ClientHandling.type: #CLIENT_DEPENDENT
@ClientHandling.algorithm: #SESSION_VARIABLE
@EndUserText.label: 'CDS table function, enum demo'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define table function DEMO_CDS_TF_ENUM_WEEKDAY
returns
{
  key mandt      : s_mandt;
  key carrid     : s_carr_id;
  key connid     : s_conn_id;
  key fldate     : s_date;
      weekday    : int2;

}
implemented by method
  CL_DEMO_CDS_TF_ENUM=>WEEKDAY;
```

**AMDP function implementation**

The AMDP function implementation uses the SAP HANA SQL function `WEEKDAY` to calculate the integer representation of the day of the week for a given flight date.

``` abap
METHOD weekday 
         BY DATABASE FUNCTION FOR HDB 
         LANGUAGE SQLSCRIPT 
         OPTIONS READ-ONLY 
         USING DEMO_CDS_SFLIGHT_VE. 
 
  RETURN 
 
select 
mandt, 
carrid, 
connid, 
fldate, 
weekday( fldate ) as weekday 
from DEMO_CDS_SFLIGHT_VE; 
ENDMETHOD.
```

**CDS view entity**

The CDS view entity `DEMO_CDS_ENUM_1` selects from the table function `DEMO_CDS_TF_ENUM_WEEKDAY`. It casts the field `weekday` to the enumerated type `DEMO_CDS_ENUM_WEEKDAY`.

``` abap
@EndUserText.label: 'Select from table function'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_ENUM_1
  as select from DEMO_CDS_TF_ENUM_WEEKDAY
{
  key carrid,
  key connid,
  key fldate,
      cast( weekday as DEMO_CDS_ENUM_WEEKDAY ) as weekday
}
```

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Class that uses RTTI to evaluate a CDS 
"! enumerated type</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_cds_enum_1 DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cds_enum_1 IMPLEMENTATION. 
  METHOD main. 
 
    SELECT FROM demo_cds_enum_1 
           FIELDS * 
           INTO TABLE @DATA(result).                    "#EC CI_NOWHERE 
    out->write( result ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The class selects from the CDS view entity `DEMO_CDS_ENUM_1` that casts the integer representation of weekdays to a CDS enumerated type. As a consequence, the column `weekday` contains the names of the enumerated constants as values.
