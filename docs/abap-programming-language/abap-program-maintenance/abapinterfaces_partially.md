---
title: "INTERFACES, PARTIALLY IMPLEMENTED"
source_file: abapinterfaces_partially.html
section: "ABAP Programming Language > ABAP - Program Maintenance > Testing and Checking Programs > ABAP Unit"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INTERFACES, PARTIALLY IMPLEMENTED

## Syntax

``` abap
INTERFACES intf   
  PARTIALLY IMPLEMENTED   
  ...  
```

[`INTERFACES`](../abap-declarations/abapinterfaces_class.md)

## Description

The addition `PARTIALLY IMPLEMENTED` for statement [`INTERFACES`](../abap-declarations/abapinterfaces_class.md) for implementing interfaces in classes can only be used in [test classes](../../abap-glossary/abentest_class_glosry.md). This addition prevents the syntax check error/warning from occurring if not all concrete non-optional interface methods are implemented in the test class. The addition must be specified before the additions that list the attributes or methods.

If an interface method that is not implemented is called during a test, an exception from the class `CX_SY_DYN_CALL_ILLEGAL_METHOD` is raised.

## Hint

The addition is particularly useful when classes that are used as test doubles implement interfaces and not all the methods of these implements are called by the code to be tested. Without this addition, it would be necessary to implement all unnecessary methods without values and assign them the `needed` pragma. This is because implementing methods without values produces a warning from the extended program check.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The class `CL_HTTP_EXT_SERVICE_DEMO` is an example of production code. This class demonstrates the function of a simple `HTTP` service. If the service is used normally, the method `IF_HTTP_EXTENSION~HANDLE_REQUEST` from ICF is called. ICF-independent tests can be run for the class: In its `CL_HTTP_EXT_SERVICE_DEMO======CCAU` local classes are declared as test doubles for the classes of ICF that implement the following interfaces:

``` abap
CLASS mock_server DEFINITION FOR TESTING FINAL. 
  PUBLIC SECTION. 
    INTERFACES if_http_server PARTIALLY IMPLEMENTED. 
ENDCLASS. 
 
CLASS mock_server IMPLEMENTATION. 
ENDCLASS. 
 
CLASS mock_request DEFINITION FOR TESTING FINAL. 
  PUBLIC SECTION. 
    INTERFACES if_http_request PARTIALLY IMPLEMENTED. 
ENDCLASS. 
 
CLASS mock_request IMPLEMENTATION. 
  METHOD if_http_request~get_form_field. 
    value = SWITCH spfli-carrid( name WHEN 'carrid' THEN 'LH' 
                                      ELSE space ) ##no_text. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS mock_response DEFINITION FOR TESTING FINAL. 
  PUBLIC SECTION. 
    INTERFACES if_http_response PARTIALLY IMPLEMENTED. 
    DATA output TYPE string. 
ENDCLASS. 
 
CLASS mock_response IMPLEMENTATION. 
  METHOD if_http_response~set_cdata. 
    me->output = data. 
  ENDMETHOD. 
ENDCLASS.
```

Only the interface methods required for the execution of tests are implemented. The interfaces have numerous other methods. These methods must not be implemented when empty due to the addition `PARTIALLY IMPLEMENTED`.

The actual test class looks as follows:

``` abap
CLASS test_http_service DEFINITION FOR TESTING 
                        DURATION SHORT 
                        RISK LEVEL HARMLESS 
                        FINAL. 
  PRIVATE SECTION. 
    DATA mock_request  TYPE REF TO mock_request. 
    DATA mock_response TYPE REF TO mock_response. 
    DATA mock_server   TYPE REF TO mock_server. 
    DATA handler  TYPE REF TO cl_http_ext_service_demo. 
    METHODS test_service FOR TESTING. 
ENDCLASS. 
 
CLASS test_http_service IMPLEMENTATION. 
  METHOD test_service. 
    CREATE OBJECT mock_request. 
    CREATE OBJECT mock_response. 
    CREATE OBJECT mock_server. 
    CREATE OBJECT handler. 
    mock_server->if_http_server~request  = mock_request. 
    mock_server->if_http_server~response = mock_response. 
    handler->if_http_extension~handle_request( mock_server ). 
    IF mock_response->output NS `<meta name="Output" content="Data">`. 
      cl_abap_unit_assert=>fail( msg = `Wrong output data` ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```

In the test method, ICF is simulated by directly creating objects of the test doubles. The `REQUEST` test double simulates the form field. The `RESPONSE` test double contains the result that is checked after the method `HANDLER` is called for testing.
