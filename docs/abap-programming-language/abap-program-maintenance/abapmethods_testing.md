---
title: "METHODS, FOR TESTING"
source_file: abapmethods_testing.html
section: "ABAP Programming Language > ABAP - Program Maintenance > Testing and Checking Programs > ABAP Unit"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# METHODS, FOR TESTING

## Syntax

``` abap
METHODS meth [ABSTRACT|FINAL] 
             [AMDP OPTIONS [READ-ONLY] 
               [client_handling]] 
  FOR TESTING 
  [RAISING exc1|RESUMABLE(exc1) exc2|RESUMABLE(exc2) ...].  
```

[`METHODS`](../abap-declarations/abapmethods.md) · [`ABSTRACT|FINAL`](../abap-declarations/abapmethods_abstract_final.md) · [`AMDP OPTIONS [READ-ONLY]`](../abap-database-access/abapmethods_amdp_options.md) · [`client_handling`](../abap-database-access/abapmethods_amdp_options_client.md)

## Description

This statement is only possible in a [test class](../../abap-glossary/abentest_class_glosry.md). It declares a [test method](../../abap-glossary/abentest_method_glosry.md) that is called as a single test during a [test run](../../abap-glossary/abentest_run_glosry.md). A test can be programmed in the method implementation. To check the test assumptions, static methods from the class `CL_ABAP_UNIT_ASSERT` are used, such as:

- `ASSERT_EQUALS`

- `ASSERT_BOUND`

- `ASSERT_NOT_BOUND`

- `ASSERT_INITIAL`

- `ASSERT_NOT_INITIAL`

- `ASSERT_SUBRC`

- `FAIL`

The data is evaluated using the [ABAP Unit](../../abap-glossary/abenabap_unit_glosry.md) Framework.

The same applies to the additions `ABSTRACT`, `FINAL`, and `RAISING` as to the [general instance methods](../abap-declarations/abapmethods_general.md). Furthermore, the addition [`AMDP OPTIONS`](../abap-database-access/abapmethods_amdp_options.md) can be specified for test methods, since these methods can also be implemented as [AMDP methods](../../abap-glossary/abenamdp_method_glosry.md).

Test methods are usually used to call units of production code and to check the result. Production code units that are called from a test method must be exited [regularly](../abap-calling-and-exiting-program-units/abenend_processing_blocks.md) or by a dedicated statement like [`RETURN`](../abap-calling-and-exiting-program-units/abapreturn.md). The statements `LEAVE PROGRAM` `LEAVE TO TRANSACTION` and `SUBMIT` without `AND RETURN` that exit the complete program are not allowed in production code called during a unit test.

## Hints

- Test methods should be private or protected if the methods are inherited. Since test classes implicitly offer friendship to the test driver in the runtime framework, the driver can call them. Test methods only need to be public in rare cases where a test executes tests from other test classes.

- When a test method is executed, the same applies to [resumable exceptions](../../abap-glossary/abenresumable_exception_glosry.md) as to all other methods. If processing can be resumed successfully, the interrupted test can be resumed.

- The special methods `setup`, `teardown`, `class_setup`, and `class_teardown` of the [fixture](../../abap-glossary/abenfixture_glosry.md) are not test methods and the addition `FOR TESTING` cannot be used for this methods.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of a test class `mytest` with a test method `mytest` that checks the value of the `text` attribute after the method `set_text_to_x` of the class `myclass` has been called. In this example, the ABAP Unit test reports an error since the value *X* is expected instead of *U*.

``` abap
* Production classes 
 
CLASS myclass DEFINITION. 
  PUBLIC SECTION. 
    CLASS-DATA text TYPE string. 
    CLASS-METHODS set_text_to_x. 
ENDCLASS. 
 
CLASS myclass IMPLEMENTATION. 
  METHOD set_text_to_x. 
    text = 'U'. 
  ENDMETHOD. 
ENDCLASS. 
 
* Test classes 
 
CLASS mytest DEFINITION FOR TESTING RISK LEVEL HARMLESS. 
  PRIVATE SECTION. 
    METHODS mytest FOR TESTING. 
ENDCLASS. 
 
CLASS mytest IMPLEMENTATION. 
  METHOD mytest. 
    myclass=>set_text_to_x( ). 
    cl_abap_unit_assert=>assert_equals( act = myclass=>text 
                                        exp = 'X' ). 
  ENDMETHOD. 
ENDCLASS.
```
