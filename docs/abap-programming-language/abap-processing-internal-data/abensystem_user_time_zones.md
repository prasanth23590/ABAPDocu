---
title: "System Time Zone and User Time Zone"
source_file: abensystem_user_time_zones.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Date and Time Processing > Date, Time, Time Stamp, and Time Zones"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# System Time Zone and User Time Zone

Two [time zones](../../abap-glossary/abentime_zone_glosry.md) are preconfigured in AS ABAP, the [system time zone](../../abap-glossary/abensystem_time_zone_glosry.md) and the [user time zone](../../abap-glossary/abenuser_time_zone_glosry.md).

- The system time zone is the client-specific time zone of the [system time](../../abap-glossary/abensystem_time_glosry.md) and the [system date](../../abap-glossary/abensystem_date_glosry.md) and cannot be changed while the system is running.

- The user time zone is a client-specific time zone that can be defined for the [user time](../../abap-glossary/abenuser_time_glosry.md) and [user date](../../abap-glossary/abenuser_date_glosry.md) of each individual user in the [user master record](../../abap-glossary/abenuser_master_record_glosry.md).

If no user time zone is defined in the user master record, or the specified time zone is invalid or inactive, the default value from a system table is used.

The system time zone and user time zone are relevant for:

- [System Time and System Date](abensystem_user_time_zones.md#system-time-and-system-date)

- [User Time and User Date](abensystem_user_time_zones.md#user-time-and-user-date)

## Hints

- The system time zone and the user time zone of an AS ABAP can be retrieved with [time zone functions in ABAP CDS](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_timezone_functions_v2.md) and [time zone functions in ABAP SQL](../abap-database-access/abensql_timezone_func.md).

- The system time zone should not be used any more. Instead, UTC should be used for internal times and dates.

- The [XCO time library](https://help.sap.com/docs/ABAP_PLATFORM_NEW/65de2977205c403bbc107264b8eccf4b/6213705cecd84757bf1badc19836a3ee) provides methods for working with times, dates and time zones.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Determination of the user time zone using an attribute of the XCO time library. Usage of that time zone to create local dates and times from a current UTC time stamp and using methods of the XCO time library.

``` abap
FINAL(zonlo) = xco_cp_time=>time_zone->user. 
 
CONVERT UTCLONG utclong_current( ) 
        INTO DATE FINAL(datlo) 
             TIME FINAL(timlo) 
        TIME ZONE zonlo->value. 
 
FINAL(moment) = xco_cp=>sy->moment( zonlo ). 
FINAL(date_time) = 
  moment->as( xco_cp_time=>format->abap )->value. 
FINAL(date) = 
  moment->date->as( xco_cp_time=>format->abap )->value. 
FINAL(time) = 
  moment->time->as( xco_cp_time=>format->abap )->value. 
 
ASSERT date = date_time(8). 
ASSERT time = date_time+8. 
 
ASSERT date = datlo. 
ASSERT time = timlo.
```

## System Time and System Date

The system time and the system date are the local time and local date of an AS ABAP in the system time zone. They are produced by regular synchronizations of the clock of the [ABAP runtime server](../../abap-glossary/abenabap_runtime_frmwk_glosry.md) and the clock of the database server. During synchronization, the ABAP runtime framework clock is set to the database server clock. Since this happens on all [AS instances](../../abap-glossary/abenas_instance_glosry.md) of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md), the ABAP runtime framework clock of an AS instance is synchronized with the clocks of all other AS instances and with the database system clock, and therefore shows the system time and system date of the entire AS ABAP.

The character-like system fields `sy-uzeit` and `sy-datum` are provided with the system time and system date at certain times.

### Hints

- System time and system date should not be used any more. Instead, UTC time and UTC date should be used, that can be retrieved from an [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md).

- The methods `TO_SYSTEM_TIMESTAMP` and `FROM_SYSTEM_TIMESTAMP` of class `CL_ABAP_UTCLONG` convert a [system date](../../abap-glossary/abensystem_date_glosry.md) and a [system time](../../abap-glossary/abensystem_time_glosry.md) in the [system time zone](../../abap-glossary/abensystem_time_zone_glosry.md) to an UTC time stamp and vice versa.

## Caution

Despite their names, the methods `GET_SYSTEM_TIME` and `GET_SYSTEM_DATE` of the C1-contract released class `CL_ABAP_CONTEXT_INFO` do not return the system time and the system date. They return the current UTC time and UTC date instead.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of an UTC time stamp from the system date and system time.

``` abap
CONVERT DATE cl_demo_date_time=>get_system_date( ) 
        TIME cl_demo_date_time=>get_system_time( ) 
        INTO UTCLONG FINAL(ts) 
        TIME ZONE cl_demo_date_time=>get_system_time_zone( ). 
 
cl_demo_output=>display( |{ ts TIMESTAMP = ISO }| ).
```

## User Time and User Date

The user time and the user date are the local time and local date of the current user, which are calculated from the system time and the user time zone.

### Hint

To determine the local time and local date from a [UTC time stamp](../../abap-glossary/abenutc_timestamp_glosry.md) created using [`GET TIME STAMP`](abapget_time-stamp.md), the user time zone can be passed to the statement [`CONVERT TIME STAMP`](abapconvert_time-stamp.md). An initial value for the time zone is implicitly set to *UTC* and not to the system time zone in `CONVERT TIME STAMP`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Determination of a local date and a local time from an UTC time stamp.

``` abap
FINAL(tz) = cl_demo_date_time=>get_user_time_zone( ). 
 
CONVERT UTCLONG utclong_current( ) 
        INTO DATE FINAL(date) 
             TIME FINAL(time) 
        TIME ZONE tz. 
 
cl_demo_output=>display( |{ date }, { time } ({ tz })| ).
```
