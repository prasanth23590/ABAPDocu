---
title: "CREATE OBJECT, FOR TESTING"
source_file: abapcreate_object_for_testing.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Testing RAP Business Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CREATE OBJECT, FOR TESTING

## Syntax

``` abap
CREATE OBJECT ... FOR TESTING.  
```

## Description

RAP-specific variant of [`CREATE OBJECT`](../../abap-programming-language/abap-creating-objects-and-values/abapcreate_object.md).

For [unit tests](../../abap-glossary/abenunit_test_glosry.md) of an [ABAP behavior implementation](../../abap-glossary/abenbehavior_implement_glosry.md), an [object](../../abap-glossary/abenobject_glosry.md) of the corresponding [class](../../abap-glossary/abenabp_handler_class_glosry.md) needs to be created using a [reference variable](../../abap-glossary/abenreference_variable_glosry.md) declared beforehand. The `FOR TESTING` addition enables the instantiation of [RAP handler classes](../../abap-glossary/abenabp_handler_class_glosry.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [Test](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/1fa88de357464d98a08165cb5830c0ad?version=sap_cross_product_abap).

## Executable Example

The [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) `BP_DEMO_MANAGED_ROOT_2` contains a `BP_DEMO_MANAGED_ROOT_2========CCAU`. The variable `class_under_test` is defined in the private section of the class `ltc_managed` as follows:

``` abap
CLASS-DATA: class_under_test TYPE REF TO lhc_demo_managed_root2, 
...
```

The method `class_setup` includes a `CREATE OBJECT ... FOR TESTING.` statement:

CREATE OBJECT class_under_test FOR TESTING.

Find more details on the unit test implementation, the methods used in this test include, and so on, via the link to the development guide for the ABAP RESTful Application Programming Model provided above.

The `BP_DEMO_MANAGED_ROOT_2========CCIMP` contains the validation `validate_field`. This validation checks the value of a specific field. If the value is greater than specified in the validation implementation, a [RAP BO instance](../../abap-glossary/abenrap_bo_instance_glosry.md) cannot be saved. The test class contains a basic [unit test](../../abap-glossary/abenunit_test_glosry.md) which includes the method `validate_field`. The method is provided with mock data. In this case, the field value that is checked with the validation `validate_field` is set that the saving of an instance does not fail.

To show the unit test result, execute the unit test.

**Note:** To show a failed unit test, you can set the value of `data_field4_root` provided in the `validate_field` method implementation to a value greater than the specified threshold in the behavior pool or uncomment the definition and implementation of method `validate_field_fails`.
