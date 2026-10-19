---
title: "System Class for Time Stamp Fields"
source_file: abentimestamp_system_class.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Date and Time Processing > Time Stamps > Time Stamp Fields with Time Stamp Type"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# System Class for Time Stamp Fields

The Class Library contains the following system class for handling UTC time stamps in [time stamp fields](../../abap-glossary/abentimestamp_field_glosry.md):

- `CL_ABAP_UTCLONG`

This class provides the following methods:

- `DIFF` for calculating time differences.

- `READ` for reading an UTC time stamp from a string.

- `WRITE_ISO_FORMAT_WITH_OFFSET` for writing an UTC time stamp to a string in ISO-8601 format, where the time zone offset is expressed by a suffix.

- `READ_ISO_FORMAT` for reading an UTC time stamp from a string that contains a value in n ISO-8601 format, where the time zone offset can be expressed by a suffix.

- `TO_SYSTEM_TIMESTAMP` converts an UTC time stamp into [system date](../../abap-glossary/abensystem_date_glosry.md) and [system time](../../abap-glossary/abensystem_time_glosry.md) in the [system time zone](../../abap-glossary/abensystem_time_zone_glosry.md).

- `FROM_SYSTEM_TIMESTAMP` converts a [system date](../../abap-glossary/abensystem_date_glosry.md) and [system time](../../abap-glossary/abensystem_time_glosry.md) in the [system time zone](../../abap-glossary/abensystem_time_zone_glosry.md) into an UTC time stamp.

The attributes `MIN` and `MAX` contain the minimum and maximum values of the [time stamp type](../../abap-glossary/abentimestamp_type_glosry.md) `utclong`.

## Hint

An initial time stamp passed to the method `DIFF` is handled here like the smallest possible value of a time stamp.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Comparison of the method `DIFF` with the built-in function [`utclong_diff`](abenutclong_diff.md).

``` abap
FINAL(ts_low)  = utclong_current( ). 
FINAL(ts_high) = utclong_add( val     = ts_low 
                             seconds = 100000 ). 
 
FINAL(diff) = utclong_diff( high = ts_high 
                           low  = ts_low ). 
 
cl_abap_utclong=>diff( EXPORTING high     = ts_high 
                                 low      = ts_low 
                       IMPORTING days    = FINAL(days) 
                                 hours   = FINAL(hours) 
                                 minutes = FINAL(minutes) 
                                 seconds = FINAL(seconds) ). 
 
ASSERT diff = 100000. 
ASSERT diff = 86400 * days + 3600 * hours + 60 * minutes + seconds.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A current UTC time stamp is converted into an ISO-8601 format where the offset of the local time zone is shown as a suffix. Some decimals are cut. Then, the character representation is converted back into time stamp type `utclong` again.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(ts_utc) = utclong_current( ). 
out->write_data( ts_utc ). 
 
TRY. 
    FINAL(ts_iso) = 
    cl_abap_utclong=>write_iso_format_with_offset( 
      EXPORTING utclong   = ts_utc 
                decimals  = 4 
                timezone  = cl_demo_date_time=>get_user_time_zone( ) ). 
    out->write_data( ts_iso ). 
  CATCH cx_abap_utclong_invalid INTO FINAL(exc2). 
    out->display( exc2->get_text( ) ). 
    RETURN. 
ENDTRY. 
 
TRY. 
    cl_abap_utclong=>read_iso_format( 
      EXPORTING string   = ts_iso 
      IMPORTING value    = FINAL(ts_utc_from_iso) ). 
    out->write( ts_utc_from_iso ). 
  CATCH cx_abap_utclong_invalid INTO FINAL(exc1). 
    out->display( exc1->get_text( ) ). 
    RETURN. 
ENDTRY. 
 
out->display( ).
```

## Executable Example

Read Time Stamp from String
