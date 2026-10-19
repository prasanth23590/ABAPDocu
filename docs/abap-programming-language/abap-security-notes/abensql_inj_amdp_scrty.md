---
title: "SQL Injections Using AMDP"
source_file: abensql_inj_amdp_scrty.html
section: "ABAP Programming Language > ABAP Security Notes > Security Risks Caused by Input from Outside > SQL Injections"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SQL Injections Using AMDP

When [AMDP](../../abap-glossary/abenamdp_glosry.md) is used, database procedures are created and called that are currently usually implemented in [SQLScript](../../abap-glossary/abensql_script_glosry.md) for the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md). The implementation of the database procedures in AMDP methods is managed by ABAP, but their content and security is not ABAP's responsibility. Risks are incurred whenever a database procedure contains dynamic parts or whenever it calls further database procedures whose functions are unknown in ABAP and cannot be checked there.

There are currently no test tools available for checking the security of the implementation of a AMDP methods. Developers of AMDP methods are themselves responsible for their security, with dual control (Code Inspections) being a useful principle here. This is partly why the use of dynamic programming techniques is strongly [discouraged](../abap-database-access/abenamdp.md). In cases where AMDP methods do contain dynamic parts that could produce SQL injections when combined with input from outside, they must be flagged accordingly to allow the caller to implement any checks needed.

Implementations of [AMDP methods](../../abap-glossary/abenamdp_method_glosry.md) are not currently supported by ABAP test tools, which means the caller of a method is responsible for ensuring that only non-malicious content is passed to it. If the implementation of an AMDP method contains dynamic parts into which formal parameters are injected, no input from outside can be passed to these parameters that is not checked or escaped appropriately, to avoid SQL injections.

## Hint

The statements about AMDP made here apply in principle to all places in which implementations made in other programming languages are called from ABAP.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

An AMDP method is implemented as follows:

``` abap
CLASS cl_dyn_amdp IMPLEMENTATION. 
  METHOD increase_seatsocc BY DATABASE PROCEDURE FOR HDB 
                           LANGUAGE SQLSCRIPT. 
    EXEC 'UPDATE sflight SET seatsocc = seatsocc + ' || :seats; 
  ENDMETHOD. 
ENDCLASS.
```

This method uses the SQLScript statement `EXEC` in the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) to execute an SQL statement specified as a character string into which the input parameter `seats` is merged. A method like this should be classified as a potential risk, since the input parameter is not checked. If possible, an input check should be implemented in SQLScript directly before the statement `EXEC` is executed.

If the method is delivered without an appropriate check and the caller wants to pass value entered outside to it, the validity of the value must be checked first. In the case in question, only integers can be passed, which can be verified using the method `CHECK_INT_VALUE` of the class `CL_ABAP_DYN_PRG` in calls from ABAP. If not, input such as `2, seatsmax = seatsmax + 10` would be possible, which would change the column `SEATSMAX` and not just the column `SEATSOCC`.

``` abap
DATA seats TYPE string. 
cl_demo_input=>request( CHANGING field = seats ). 
TRY. 
    NEW cl_dyn_amdp( )->increase_seatsocc( 
      seats = |{ cl_abap_dyn_prg=>check_int_value( seats ) }| ). 
  CATCH cx_abap_not_an_integer INTO DATA(exc). 
    cl_demo_output=>display( exc->get_text( ) ). 
ENDTRY.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

An AMDP method is implemented as follows:

``` abap
CLASS cl_dyn_amdp IMPLEMENTATION. 
  METHOD get_flights BY DATABASE PROCEDURE FOR HDB 
                        LANGUAGE SQLSCRIPT 
                        USING spfli. 
    flights = SELECT * FROM SPFLI WHERE mandt = :mandt; 
    flights = APPLY_FILTER(:flights, :filter); 
  ENDMETHOD. 
ENDCLASS.
```

This method uses the SQLScript statement `APPLY_FILTER` in the [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md), which sets a dynamic condition on a result set. This statement can also produce SQL injections when combined with input from outside if the input is not validated appropriately. As used in ABAP, methods of the class `CL_ABAP_DYN_PRG` can validate this input..

``` abap
DATA column TYPE string. 
cl_demo_input=>add_field( CHANGING field = column ). 
DATA value TYPE string. 
cl_demo_input=>request( CHANGING field = value ). 
TRY. 
    DATA(filter) = cl_abap_dyn_prg=>check_column_name( column ) && 
                   ` = ` && 
                   cl_abap_dyn_prg=>quote( value ). 
    NEW cl_dyn_amdp( )->get_flights( EXPORTING mandt = sy-mandt 
                                              filter = filter 
                                   IMPORTING flights = DATA(result) ). 
  CATCH cx_abap_invalid_name cx_amdp_execution_failed INTO DATA(exc). 
    cl_demo_output=>display( exc->get_text( ) ). 
ENDTRY.
```
