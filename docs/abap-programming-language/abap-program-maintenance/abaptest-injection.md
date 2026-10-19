---
title: "TEST-INJECTION"
source_file: abaptest-injection.html
section: "ABAP Programming Language > ABAP - Program Maintenance > Testing and Checking Programs > ABAP Unit > Test Seams"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TEST-INJECTION

## Syntax

``` abap
TEST-INJECTION seam.   
  [statement_block]   
END-TEST-INJECTION.  
```

## Description

The statement `TEST-INJECTION` introduces an [injection](../../abap-glossary/abeninjection_glosry.md) for a [test seam](../../abap-glossary/abentest_seam_glosry.md) `seam`, which is closed using `END-TEST-INJECTION`. The test seam `seam` must be defined in the production code of the current program using the statement [`TEST-SEAM`](abaptest-seam.md). When a unit test is performed, the statement block `statement_block` of the injection replaces the statement block of the test seam `seam` in production code.

An injection can only be defined in the methods of test classes created in a [test include](../../abap-glossary/abentest_include_glosry.md). Injections have the following properties:

- Injections can be made only while a test method or the `setup` method is being executed.

- Injections cannot be nested, which means that an injection cannot contain further injections.

- An injection cannot extend beyond the limits of a [statement block](../../abap-glossary/abenstatement_block_glosry.md) but can contain closed [control structures](../../abap-glossary/abencontrol_structure_glosry.md).

- An injection can include local data declarations using the statement [`DATA`](../abap-declarations/abapdata.md). These variables are visible below their declaration in the current injection and all following injections of the current test class. The data objects declared in an injection are not visible outside of injections, that is, neither in other parts of the test class nor in production code. Injections that access data objects declared in a different injection can only be assigned to test seams defined in the production source code below the test seam, that is, the test seam assigned to the declaring injection.

- An injection can be empty, that is, it is does not contain any statements. The code of the specified test seam is removed when the injection is executed.

- Injections can access all types and objects that are visible in the location of the specified test seam.

- In an injection, it is not possible to access types and objects of the test method, in which the injection is defined. These types and objects are visible in the position of the statement `TEST-INJECTION`, but not in the injection.

The test seam remains replaced by the injection until a new injection is encoutered for the test seam. This means that a test seam can be replaced more than once during a unit test and by different injections. All replacements are canceled at the end of an individual test or test method.

## Hints

- When the test runs, any data objects declared in injections are preserved in their context, even if the declaring injection is replaced by a different injection in its test seam.

- Apart from `DATA`, no declarative statements are possible in injections.

- The injections for a test seam must be defined in the same [compilation unit](../../abap-glossary/abencompilation_unit_glosry.md).

- Test includes can currently only be created for class pools and function groups, which means that injections can only be created there as well.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The `CL_DEMO_TEST_SEAMS============CCAU` of the class `CL_DEMO_TEST_SEAMS` is an example of a test class with injections:

The test method tests the method `CHANGE_PRICE` (see the example for [`TEST-SEAM`](abaptest-seam.md)). Before the test method is executed, the injection replaces the injection in the `setup` method of the test seam `selection`. When the test method is executed,

- the statements of the test seam `modification` are removed when replaced by an empty injection and the successful closing of the method is checked,

- the statements of the test seam `modification` are replaced in such a way that an unsuccessful modification of the table content is simulated, and the associated return code checked,

- the statements of the test seam `selection` are replaced in such a way that an unsuccessful selection of the table content is simulated, and the associated return code checked.

``` abap
CLASS test_demo_test_seam DEFINITION FOR TESTING 
                          RISK LEVEL HARMLESS 
                          DURATION SHORT 
                          FINAL. 
  PRIVATE SECTION. 
    METHODS: setup, 
      test_change_price FOR TESTING, 
      invoke_and_assert IMPORTING exp TYPE i. 
ENDCLASS. 
 
CLASS test_demo_test_seam IMPLEMENTATION. 
  METHOD setup. 
    TEST-INJECTION selection. 
      wa-price = 100. 
    END-TEST-INJECTION. 
  ENDMETHOD. 
  METHOD test_change_price. 
    TEST-INJECTION modification. 
    END-TEST-INJECTION. 
    invoke_and_assert( 90 ). 
    TEST-INJECTION modification. 
      subrc = 4. 
    END-TEST-INJECTION. 
    invoke_and_assert( -2 ). 
    TEST-INJECTION selection. 
      subrc = 4. 
    END-TEST-INJECTION. 
    TEST-INJECTION modification. 
    END-TEST-INJECTION. 
    invoke_and_assert( -1 ). 
  ENDMETHOD. 
  METHOD invoke_and_assert. 
    NEW cl_demo_test_seams( )->change_price( 
      EXPORTING 
         carrid = '   ' 
         connid = '0000' 
         fldate = '00000000' 
         factor = 90 
       IMPORTING new_price = DATA(new_price) ). 
    cl_abap_unit_assert=>assert_equals( 
     EXPORTING 
       exp = exp 
       act = new_price  ). 
  ENDMETHOD. 
ENDCLASS.
```
