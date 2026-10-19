---
title: "ABAP Unit"
source_file: abenabap_unit.html
section: "ABAP Programming Language > ABAP - Program Maintenance > Testing and Checking Programs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Unit

ABAP Unit is a test framework for [unit tests](../../abap-glossary/abenunit_test_glosry.md). ABAP Unit can be used to:

- run single tests or mass tests

- evaluate test results

Single tests can be started directly in the tool for the corresponding program. More comprehensive test runs are executed by using the ABAP Test Cockpit.

In ABAP programs, unit tests are performed as [test methods](../../abap-glossary/abentest_method_glosry.md) in local [test classes](../../abap-glossary/abentest_class_glosry.md). They are not part of the production code of a program, but are transported in the same way. Test methods of this type are executed and evaluated using the ABAP Unit Framework. The test methods generally call the units of the production code to be tested and then check the results using methods of the class `CL_ABAP_UNIT_ASSERT`. Test classes and test methods are defined using the following language elements. Special [test includes](../../abap-glossary/abentest_include_glosry.md) are used to define test classes in class pools and function pools.

- [`CLASS ... DEFINITION FOR TESTING`](abapclass_for_testing.md)

- [`METHODS ... FOR TESTING`](abapmethods_testing.md)

If test classes implement interfaces, not all interface methods generally need to be implemented there. The error message or warning that otherwise occurs can be hidden in test classes by using an addition of the statement `INTERFACES`.

- [`INTERFACES ... PARTIALLY IMPLEMENTED`](abapinterfaces_partially.md)

If production code contains parts that are not suitable for unit tests, sections of code can be flagged as [test seams](abentest_seams.md). [Injections](../../abap-glossary/abeninjection_glosry.md) can be defined in methods of test classes. Injections replace the test seams with test-friendly code when a unit test is executed.

In order to test repository objects that do not support test classes themselves in [ADT](../../abap-glossary/abenadt_glosry.md), the special [ABAP Doc comment](../../abap-glossary/abenabap_doc_comment_glosry.md) [`"! @testing ...`](abentest_relations.md) can be used to define a [test relation](../../abap-glossary/abentest_relation_glosry.md) that links a test class or a test method with such a repository object.

## Hints

- All components required for tests in the context of ABAP Unit should be defined exclusively in test classes. This ensures that they are not generated in production systems and cannot be addressed by production code. In addition to test classes with test methods, this also includes test doubles and other helper classes that do not contain test methods.

- The [ABAP Test Double Framework](https://help.sap.com/docs/ABAP_PLATFORM_NEW/c238d694b825421f940829321ffa326a/804c251e9c19426cadd1395978d3f17b) based on class `CL_ABAP_TESTDOUBLE` simplifies and standardizes the creation and configuration of test doubles.

- For more information, see the documentation [ABAP Unit](https://help.sap.com/docs/ABAP_PLATFORM_NEW/ba879a6e2ea04d9bb94c7ccd7cdac446/491cfd8926bc14cde10000000a42189b) in SAP Help Portal.
