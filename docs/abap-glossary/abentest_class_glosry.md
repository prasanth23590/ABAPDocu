---
title: "test class"
source_file: abentest_class_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# test class

[ABAP Language](../abap-programming-language/abenabala_glossary.md)

## Definition

A test class in a narrower sense is a special local or global [class](abenclass_glosry.md) in which tests for [ABAP Unit](abenabap_unit_glosry.md) are implemented in the form of test methods. [Test methods](abentest_method_glosry.md) can be implemented in a test class. A test class groups together related tests that use the same [fixture](abenfixture_glosry.md). Test classes are defined using the [`FOR TESTING`](../abap-programming-language/abap-program-maintenance/abapclass_for_testing.md) addition of the [`CLASS`](../abap-programming-language/abap-declarations/abapclass_definition.md) statement. Test classes can only be used as part of [test runs](abentest_run_glosry.md) and, by default, are not generated in production systems. Test doubles and other auxiliary classes required for testing should also be defined with [`FOR TESTING`](../abap-programming-language/abap-program-maintenance/abapclass_for_testing.md) but do not contain any test methods and are not test classes in a narrower sense.
