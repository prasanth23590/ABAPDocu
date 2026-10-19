---
title: "CLASS, FOR TESTING"
source_file: abapclass_for_testing.html
section: "ABAP Programming Language > ABAP - Program Maintenance > Testing and Checking Programs > ABAP Unit"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS, FOR TESTING

## Syntax

``` abap
CLASS class DEFINITION FOR TESTING [RISK LEVEL {CRITICAL|DANGEROUS|HARMLESS}] 
                                   [DURATION {SHORT|MEDIUM|LONG}].  
```

[`CLASS class DEFINITION`](../abap-declarations/abapclass_definition.md)

### Addition

[1. `... RISK LEVEL {CRITICAL|DANGEROUS|HARMLESS}`](abapclass_for_testing.md#addition-1)

[2. `... DURATION {SHORT|MEDIUM|LONG}`](abapclass_for_testing.md#addition-2)

## Overview

### Description

The `FOR TESTING` addition defines a class to be used in [ABAP Unit](../../abap-glossary/abenabap_unit_glosry.md). A class with the `FOR TESTING` addition can have different purposes:

- [Test class](../../abap-glossary/abentest_class_glosry.md) in a narrower sense. A test class contains [test methods](../../abap-glossary/abentest_method_glosry.md) that are called by the ABAP Unit framework during a [test run](../../abap-glossary/abentest_run_glosry.md).

- Represent a test double for use as dependent-on component in unit tests. For more information, see [Managing Dependencies with ABAP Unit](https://help.sap.com/docs/ABAP_PLATFORM_NEW/c238d694b825421f940829321ffa326a/04a2d0fc9cd940db8aedf3fa29e5f07e).

- Provide helper functions (test infrastructure) for writing ABAP unit tests.

A test class and its components cannot be addressed in the production code of the program; therefore, only in other test classes. In particular, a subclass of a test class must be a test class itself and be declared using the `FOR TESTING` addition. The only exception to this rule is that test classes can be specified as [friends](../../abap-glossary/abenfriend_glosry.md) in the definition of production classes to make it possible to test private components.

A local test class can contain special private methods that implement the [fixture](../../abap-glossary/abenfixture_glosry.md) for the tests of the class. These methods have the following predefined names:

- An [instance method](../../abap-glossary/abeninstance_method_glosry.md) `setup`, which is executed before each individual test that is before each execution of a test method of a class.

- An instance method `teardown`, which is executed after each individual test that is after each execution of a test method of the class.

- A [static method](../../abap-glossary/abenstatic_method_glosry.md) `class_setup`, which is executed once before all tests of the class.

- A static method `class_teardown`, which is executed once after all tests of the class.

The source code of a test class is not part of the production code of its program and is not generated in production systems. The code of such a class is not counted in code coverage measurements.

### Hints

- Local test classes of class pools and function pools should only be created in the [test includes](../../abap-glossary/abentest_include_glosry.md) designed for them. In other programs, these tests should located at the end of the program.

- In addition to the test methods and special methods for the fixture, a test class can also contain other components. These components can be used in a user's own test class only or in other test classes, depending on the visibility. In this way, help methods can be defined for tests.

- All components required for tests in the context of ABAP Unit should be defined exclusively in test classes. This ensures that they cannot be generated in production systems and cannot be addressed by production code. In addition to test classes with test methods, this also includes test doubles and other helper classes that do not contain test methods.

- Test classes can inherit from any other classes, especially global classes. This allows general global tests to be implemented that can be used in local test classes.

- Global test classes (in a narrower sense) always have to define the code under test by means of a [test relation](../../abap-glossary/abentest_relation_glosry.md).

- In test classes, the addition [`PARTIALLY IMPLEMENTED`](abapinterfaces_partially.md) of the statement `INTERFACES` can be specified, which allows interfaces to be implemented only partially. This is particularly useful in test doubles.

- The addition `FOR TESTING` in a local class created in the area for *local types* of the class pool of a global test class. The addition is not needed in auxiliary classes for the global test class, since its property *test class* affects the entire class pool with regard to its generation. In rare cases in which a global test class is to be tested itself, local test classes can be created as recommended for other global classes in the area *local test classes*.

- The methods of the [fixture](../../abap-glossary/abenfixture_glosry.md) are not test methods and the addition [`FOR TESTING`](abapmethods_testing.md) cannot be specified for their declaration.

- Global test classes can also contain [AMDP method](../../abap-glossary/abenamdp_method_glosry.md) as test methods. In this case, they must include the corresponding tag interface [`IF_AMDP_MARKER_...`](../abap-database-access/abenamdp_classes.md) for [AMDP classes](../../abap-glossary/abenamdp_class_glosry.md).

## Addition 1

`... RISK LEVEL {CRITICAL|DANGEROUS|HARMLESS}`

## Addition 2

`... DURATION {SHORT|MEDIUM|LONG}`

### Description

These additions assign test properties to a test class.

- `RISK LEVEL` defines the risk level for a test.

- `DURATION` specifies the expected execution time.

During test execution, the test properties are checked against values that are maintained by administration.

- The meaning of the risk levels is as follows:

  - `CRITICAL` - a test changes system settings or customizing data (default)

  - `DANGEROUS` - a test changes persistent data

  - `HARMLESS` - a test does not change system settings or persistent data

    Tests whose risk level is higher than specified by administration are not executed.

- The meaning of the expected execution time is as follows:

  - `SHORT` - an imperceptible execution time of some few seconds is expected.

  - `MEDIUM` - a noticeable execution time of around a minute is expected.

  - `LONG` - a very noticeable execution time of more than one minute is expected.

    For each of these expected execution times, upper limits are specified by administration. These limits are usually greater than the expected execution times in order to include processes, for example compilations, that are not part of the test itself. If a test exceeds the upper limit associated with the expected time, the system behavior depends on the execution mode of the test and whether the ABAP Unit runtime monitoring is switched on or off.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

See the class `CL_DEMO_ABAP_UNIT`.

- The global class itself represents the production part of the source code. A method `get_sum` adds the values of the fields of a row of a DDIC database table and assigns the result to the private attribute `sum`.

- The class `test_demo` in the `CCAU` include is a test class for the global class.

  - In the method `setup`, an object of the global class is created and the DDIC database table is prepared with test data. Therefore, the addition `DANGEROUS` is specified for `RISK LEVEL`.

  - The method `test_sum` calls `get_sum` and compares the private attribute `sum` with the expected value. For this reason, `test_demo` must be a local friend of the global class.

  - In the method `teardown`, the test data is removed from the DDIC database table again.

    The test method is called when the unit test of `CL_DEMO_ABAP_UNIT` is executed and should not report an error.
