---
title: "TEST-SEAM"
source_file: abaptest-seam.html
section: "ABAP Programming Language > ABAP - Program Maintenance > Testing and Checking Programs > ABAP Unit > Test Seams"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TEST-SEAM

## Syntax

``` abap
TEST-SEAM seam.   
  [statement_block]   
END-TEST-SEAM.  
```

## Description

The statement `TEST-SEAM` introduces a [test seam](../../abap-glossary/abentest_seam_glosry.md) called `seam`, which is closed by `END-TEST-SEAM`. A [test class](../../abap-glossary/abentest_class_glosry.md) of the current program can use the statement [`TEST-INJECTION`](abaptest-injection.md) to replace the statement block `statement_block` with an [injection](../../abap-glossary/abeninjection_glosry.md) defined there. If no injection is performed for the test seam, the original code is executed.

Test seams have the following properties:

- Multiple test seams can be defined in a single [compilation unit](../../abap-glossary/abencompilation_unit_glosry.md), but each must have a unique name.

- The general [naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md) apply to the name `seam`.

- Test seams cannot be nested, which means that a test seam cannot contain further test seams.

- A test seam cannot extend beyond the limits of a [statement block](../../abap-glossary/abenstatement_block_glosry.md) but can contain closed [control structures](../../abap-glossary/abencontrol_structure_glosry.md).

- A test seam can include data declarations. These declarations are not replaced when an injection is performed and remain visible in their context.

- Test seams can be defined in the [global declaration part](../../abap-glossary/abenglobal_declaration_sect_glosry.md) of a program but not in the [declaration part](../../abap-glossary/abendeclaration_part_glosry.md) of a class.

- A test seam can be empty, that is, it does not contain any statements. An injection is inserted instead.

- Test seams cannot be defined in test classes.

## Hints

- The [injections](../../abap-glossary/abeninjection_glosry.md) for a test seam must be defined in the same [compilation unit](../../abap-glossary/abencompilation_unit_glosry.md).

- [Injections](../../abap-glossary/abeninjection_glosry.md) can only be created in test classes that are defined in a [test include](../../abap-glossary/abentest_include_glosry.md) of the current program. Test includes are currently only possible in [class pools](../../abap-glossary/abenclass_pool_glosry.md) and [function pools](../../abap-glossary/abenfunction_pool_glosry.md). This means that test seams are only feasible in class pools and function pools.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Here, the class `CL_DEMO_TEST_SEAMS` is an example of production code. The method `CHANGE_PRICE` multiplies the price of a flight in the database table `SFLIGHT` by a factor and, if successful, returns the modified price. If a database access fails, a specific invalid value is returned instead of the price.

Test seams are defined for both database accesses. This makes it possible to run a unit test without accessing actual data. See the example for [`TEST-INJECTION`](abaptest-injection.md).

``` abap
METHOD change_price. 
  DATA wa TYPE sflight. 
  TEST-SEAM selection. 
    SELECT SINGLE * 
           FROM sflight 
           WHERE carrid = @carrid AND 
                 connid = @connid AND 
                 fldate = @fldate 
           INTO @wa. 
    subrc = sy-subrc. 
  END-TEST-SEAM. 
  IF subrc <> 0. 
    new_price = -1. 
    RETURN. 
  ENDIF. 
  wa-price = wa-price * factor / 100. 
  TEST-SEAM modification. 
    MODIFY sflight FROM @wa. 
    subrc = sy-subrc. 
  END-TEST-SEAM. 
  IF subrc = 0. 
    new_price = wa-price. 
  ELSE. 
    new_price = -2. 
  ENDIF. 
ENDMETHOD.
```
