---
title: "CLASS, FOR BEHAVIOR OF"
source_file: abapclass_for_behavior_of.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS, FOR BEHAVIOR OF

## Syntax

``` abap
CLASS bp_bdef DEFINITION 
            PUBLIC [ABSTRACT] [FINAL] 
            FOR BEHAVIOR OF bdef ... 
 ... 
ENDCLASS.  
```

[`CLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`DEFINITION`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`PUBLIC [ABSTRACT] [FINAL]`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`ENDCLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md)

## Description

The addition `FOR BEHAVIOR OF` to the definition of a [global class](../../abap-glossary/abenglobal_class_glosry.md) defines an [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) for the [RAP behavior definition (BDEF)](../../abap-glossary/abencds_behavior_definition_glosry.md) specified in `bdef`. The name of the global class (`bp_bdef`) of an ABAP behavior pool usually starts with the prefix `BP_`. The global class is implicitly [`ABSTRACT`](../../abap-programming-language/abap-declarations/abapclass_options.md) and [`FINAL`](../../abap-programming-language/abap-declarations/abapclass_options.md); hence, `ABSTRACT` and `FINAL` can but need not be specified. In the [visibility sections](../../abap-glossary/abenvisibility_section_glosry.md), [static methods](../../abap-glossary/abenstatic_method_glosry.md) as well as statements with [`CLASS-DATA`](../../abap-programming-language/abap-declarations/abapclass-data.md), [`CONSTANTS`](../../abap-programming-language/abap-declarations/abapconstants.md) and [`TYPES`](../../abap-programming-language/abap-declarations/abaptypes.md) can be used.

If a BDEF defines operations with user-defined logic, such as [nonstandard operations](../rap-behavior-definitions/abenbdl_nonstandard.md), [determinations](../rap-behavior-definitions/abenbdl_determinations.md) or [validations](../rap-behavior-definitions/abenbdl_validations.md), an implementation of those operations is required in one or more behavior pools. Any number of behavior pools can be assigned to a BDEF allowing applications a structuring into multiple units (see the topic [RAP BDL - implementation grouping](../rap-behavior-definitions/abenbdl_grouping.md)).

The actual implementation of the transactional behavior of RAP BOs happens in the [CCIMP include](../../abap-glossary/abenccimp_glosry.md) of a behavior pool. There, two types of special [local classes](../../abap-glossary/abenlocal_class_glosry.md) can be defined: one or more [handler classes](abenabp_handler_class.md) to implement the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md) and a [saver class](abenabp_saver_class.md) to implement the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md) of the business object behavior.

## Hints

- See more syntax options for the [global declaration part](../../abap-glossary/abenglobal_declaration_sect_glosry.md) [here](../../abap-programming-language/abap-declarations/abapclass_definition.md).

- Currently, global classes of behavior pools cannot be instantiated or inherited.

- The addition `FOR BEHAVIOR OF` is also relevant for [ABAP auxiliary classes](../../abap-glossary/abenabp_aux_class_glosry.md).

## More Information

When implementing RAP operations, ensure that you comply with [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). Follow the implementation guidelines in the development guide for the ABAP RESTful Application Programming Model, section [RAP Business Object Contract](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

You can find a selected set of guidelines in [here](abaprap_impl_rules.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from the global class `BP_DEMO_MANAGED_ADDITIONAL_SAV` shows a class definition.

``` abap
 CLASS bp_demo_managed_additional_sav DEFINITION PUBLIC 
   ABSTRACT FINAL FOR BEHAVIOR OF demo_managed_additional_save. 
   PUBLIC SECTION. 
    CLASS-DATA: var_req_c TYPE REQUEST 
                    FOR CHANGE demo_managed_additional_save, 
                var_req_d TYPE REQUEST 
                    FOR DELETE demo_managed_additional_save, 
                var_tab_c TYPE TABLE 
                    FOR CHANGE demo_managed_additional_save, 
                var_struc_c TYPE STRUCTURE 
                    FOR CHANGE demo_managed_additional_save. 
  ... 
ENDCLASS. 
 
CLASS bp_demo_managed_additional_sav IMPLEMENTATION. 
  ... 
ENDCLASS.
```
