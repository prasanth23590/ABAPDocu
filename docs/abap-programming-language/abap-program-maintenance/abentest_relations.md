---
title: "Test Relations"
source_file: abentest_relations.html
section: "ABAP Programming Language > ABAP - Program Maintenance > Testing and Checking Programs > ABAP Unit"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Test Relations

## Syntax

``` abap
"! @testing [kind:]name  
```

## Description

This special [ABAP Doc comment](../../abap-glossary/abenabap_doc_comment_glosry.md) can be used in front of the declaration of a [test class](../../abap-glossary/abentest_class_glosry.md) or a [test method](../../abap-glossary/abentest_method_glosry.md) to define a [test relation](../../abap-glossary/abentest_relation_glosry.md) that links the test class or test method with the repository object specified after `@testing`.

- `name` is used to specify the name of a repository object and is not case-sensitive.

- `kind` must be used to specify the type of some repository objects and must be omitted for others. The following can be used for `kind`:

  - `FUNC` for [function modules](../../abap-glossary/abenfunction_module_glosry.md) in function pools

  - `FUGR` for [function pools](../../abap-glossary/abenfunction_pool_glosry.md)

  - `XSLT` for [XSLT programs](../../abap-glossary/abenxslt_program_glosry.md) and [Simple Transformations](../../abap-glossary/abensimple_transformation_glosry.md)

  - `BDEF` for [RAP behavior definitions](../../abap-glossary/abencds_behavior_definition_glosry.md)

    `kind` cannot and must not be specified for other repository objects such as global classes and [CDS entities](../../abap-glossary/abencds_entity_glosry.md). They are addressed by their names alone.

Defining a test relation between a test class or test method and a repository object has the effect that the test can be displayed and executed for this object in [ADT](../../abap-glossary/abenadt_glosry.md).

## Hints

- Test relations are to be understood more as an annotation in an ABAP program than as ABAP Doc comment.

- Test relations are used to link repository objects with external [unit tests](../../abap-glossary/abenunit_test_glosry.md). This is especially useful for repository objects that do not support test classes themselves.

- The current program of the test class or test method cannot be specified.

- Multiple test relations can be specified for a single test class or test method.

- For more information, see [Writing ABAP Unit with Test Relations](https://help.sap.com/docs/ABAP_PLATFORM_NEW/c238d694b825421f940829321ffa326a/12104d8c73224af78f5a04885809b30e).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Defining test relations between a test class and its test methods and various repository objects.

``` abap
"! @testing cl_demo1 
"! @testing cl_demo2 
CLASS test_demo_cds_association DEFINITION FOR TESTING. 
  PRIVATE SECTION. 
    METHODS: 
      test_class1 FOR TESTING, 
      test_class2 FOR TESTING, 
      "! @testing demo_cds_view 
      test_cds_view FOR TESTING, 
      "! @testing XSLT:demo_trafo 
      test_transformation FOR TESTING. 
ENDCLASS. 
 
CLASS test_demo_cds_association IMPLEMENTATION. 
  METHOD test_cds_view. 
    ... 
  ENDMETHOD. 
  METHOD test_class1. 
    ... 
  ENDMETHOD. 
  METHOD test_class2. 
    ... 
  ENDMETHOD. 
  METHOD test_transformation. 
    ... 
  ENDMETHOD. 
ENDCLASS.
```
