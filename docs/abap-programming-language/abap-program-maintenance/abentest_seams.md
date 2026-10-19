---
title: "Test Seams"
source_file: abentest_seams.html
section: "ABAP Programming Language > ABAP - Program Maintenance > Testing and Checking Programs > ABAP Unit"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Test Seams

Test seams are language constructs designed especially for [unit tests](../../abap-glossary/abenunit_test_glosry.md) and are implemented using the following statements:

- [`TEST-SEAM` - `END-TEST-SEAM`](abaptest-seam.md)

  Defines a test seam as a replaceable area in the production code of a program.

- [`TEST-INJECTION` - `END-TEST-INJECTION`](abaptest-injection.md)

  Replaces the executable statements of a test seam with the statements of an injection in a [test class](../../abap-glossary/abentest_class_glosry.md) of the same program.

Test seams have the following properties:

- Test seams do not affect the use of programs in production. No injection takes place, rather the original code is executed.

- A program can contain multiple test seams.

- Multiple injections can be defined for a single test seam.

- Injections can only be created in test classes that are defined in a [test include](../../abap-glossary/abentest_include_glosry.md). Test seams can be used in all executable units of a master program that includes a test include.

- Unit tests can make injections while [test methods](../../abap-glossary/abentest_method_glosry.md) or the `setup` method are being executed.

- If injections are repeated in the same test seam, the last injection is performed as an active injection.

## Hints

- Test seams are a simple way of replacing or expanding source code in the production parts of a program for test purposes. If, for example, the behavior of certain statements prevents tests from running, the unit test can replace them with suitable alternatives. Typical scenarios are:

  - Authorization checks

  - Reading persistent data

  - Modifying persistent data

  - Creating test doubles
