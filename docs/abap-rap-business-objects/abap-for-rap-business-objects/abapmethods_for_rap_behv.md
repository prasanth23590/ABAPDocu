---
title: "METHODS, FOR, RAP Handler Methods"
source_file: abapmethods_for_rap_behv.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Handler Classes and Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# METHODS, FOR, RAP Handler Methods

## Syntax

**Handler method definitions:**

``` abap
METHODS meth [FINAL] 
   FOR { DETERMINE ON { SAVE | MODIFY }   ... [IMPORTING  ] ... FOR ... } 
     | { GLOBAL AUTHORIZATION    ...  [IMPORTING  ] ... FOR ... } 
     | { GLOBAL FEATURES   ... [IMPORTING  ] ... FOR ... } 
     | { [INSTANCE] AUTHORIZATION   ... [IMPORTING  ] ... FOR ... } 
     | { [INSTANCE] FEATURES   ... [IMPORTING  ] ... FOR ... } 
     | { LOCK   ... [IMPORTING  ] ... FOR ... } 
     | { MODIFY   ... [IMPORTING  ] ... FOR ... } 
     | { NUMBERING   ... [IMPORTING  ] ... FOR ... } 
     | { PRECHECK   ... [IMPORTING  ] ... FOR ...  } 
     | { READ   ... [IMPORTING  ] ... FOR ... } 
     | { VALIDATE ON SAVE   ... [IMPORTING  ] ... FOR ... } 

[CHANGING   { [failed   TYPE data  ] [reported   TYPE data  ] [mapped   TYPE data  ] }].  
```

**Handler method implementations:**

``` abap
METHOD meth. 
   ... 
ENDMETHOD.  
```

[`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`FINAL`](../../abap-programming-language/abap-declarations/abapmethods_abstract_final.md) · [`DETERMINE ON { SAVE | MODIFY } `](abaphandler_meth_det.md) · [`IMPORTING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`GLOBAL AUTHORIZATION `](abaphandler_meth_global_auth.md) · [`IMPORTING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`GLOBAL FEATURES `](abaphandler_meth_global_features.md) · [`IMPORTING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`[INSTANCE] AUTHORIZATION `](abaphandler_meth_auth.md) · [`IMPORTING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`[INSTANCE] FEATURES `](abaphandler_meth_features.md) · [`IMPORTING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`LOCK `](abaphandler_meth_lock.md) · [`IMPORTING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`MODIFY `](abaphandler_meth_modify.md) · [`IMPORTING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`NUMBERING `](abaphandler_meth_numbering.md) · [`IMPORTING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`PRECHECK `](abaphandler_meth_precheck.md) · [`IMPORTING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`READ `](abaphandler_meth_read.md) · [`IMPORTING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`VALIDATE ON SAVE `](abaphandler_meth_validate.md) · [`IMPORTING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`CHANGING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`failed `](abaptype_response_for.md) · [`data `](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) · [`reported `](abaptype_response_for.md) · [`data `](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) · [`mapped `](abaptype_response_for.md) · [`data `](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) · [`METHOD`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`ENDMETHOD`](../../abap-programming-language/abap-declarations/abapmethods.md)

## Description

[Handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) must be defined and implemented in a [handler class](../../abap-glossary/abenabp_handler_class_glosry.md) of an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). The method name (`meth`) can be freely chosen except for the predefined [draft actions](../rap-behavior-definitions/abenbdl_draft_action.md) (whose implementation is only relevant if they are specified with `with additional implementation` in the BDEF), the method names in the context of [`augment`](../rap-behavior-definitions/abenbdl_augment_projection.md) operations, and the method names in the context of [RAP default values functions](abaprap_handler_default_val_func.md). The `METHODS` statements of handler methods in behavior pools contain RAP-specific ABAP words like `FOR MODIFY`, `FOR CREATE` or `FOR READ` as well as optional or mandatory ABAP words like `REQUEST` and `RESULT` that are followed by parameters typed with [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md).

The following list provides an overview on parameters of handler methods:

- Nearly all parameters are typed with [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) that have [RAP components](abapderived_types_comp.md). The parameters' names can be chosen freely.

- Each handler method must have at least one importing parameter. The addition [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) is optional since it is used implicitly.

- All handler methods have changing parameters. The changing parameters for retrieving mapping information (`mapped`) or information on failures (`failed`) and error messages (`reported`) have predefined names and are used implicitly. The addition [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) and the explicit specification of those changing parameters is optional. The availability of the `mapped`, `failed` and `reported` parameters depends on the handler method used. When used explicitly, for example, for the method `... FOR MODIFY ... FOR CREATE ...`, the syntax can be as follows:

  `METHODS create FOR MODIFY IMPORTING entities FOR CREATE bdef CHANGING failed TYPE DATA mapped TYPE DATA reported TYPE DATA.` For the explicit declaration of the changing parameters, the generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) is used. At runtime, the typed parameters, e. g. `failed`, implicitly has the BDEF derived type [`TYPE RESPONSE FOR`](abaptype_response_for.md).

- In many cases, parameters can be passed by reference (see [`REFERENCE`](../../abap-programming-language/abap-declarations/abapmethods_parameters.md)), however, they cannot be passed by value ([`VALUE`](../../abap-programming-language/abap-declarations/abapmethods_parameters.md)). Hence, the importing parameters cannot be changed in the methods.

At least one of the three methods with the predefined names `MODIFY`, `READ` and `LOCK` must be implemented in each handler class. Apart from that, helper methods can be implemented.

## Hints

- It is recommended that the `CHANGING` parameters `failed`, `reported` and `mapped` are filled with returned information, for example, if an instance cannot be read. The components of each of the `CHANGING` parameters can vary depending on how it is typed with a BDEF derived type. Here is an example on how a `CHANGING` parameter can be filled within the method implementation:

  `LOOP AT import_params ASSIGNING FIELD-SYMBOL(<fs>). ... APPEND VALUE #( %key = <fs>-%key %fail = if_abap_behv=>cause-not_found ... ) TO failed-bdef. APPEND VALUE #( %msg = new_message_with_text( severity = if_abap_behv_message=>severity-error text = 'Issue occurred.' %key = <fs>-%key ... ) TO reported-bdef. ENDLOOP.`

- In some cases, the F2 help of the [ADT](../../abap-glossary/abenadt_glosry.md) shows further `CHANGING` parameters for RAP handler methods apart from `failed`, `reported` and `mapped`. `RESULT` is a RAP-specific ABAP word that must be explicitly specified. Hence, the `CHANGING` parameter `result` cannot be specified using the ABAP word `CHANGING`:

  `METHODS read FOR READ IMPORTING keys FOR READ bdef RESULT result.` Similarly, the `IMPORTING` parameter `requested_field` must be specified in combination with the ABAP word `REQUEST` in the handler method definition.

- The handler method `FOR MODIFY` can handle multiple entities and operations within one processing step. However, it might be useful to split the handler method implementation into separate methods in the interest of readability and keeping the complexity on a lower level. In doing so, multiple RAP handler classes within one ABP or multiple ABPs can be defined. The following handler method definition demonstrates a handler method `FOR MODIFY` that includes multiple operations:

  `... METHODS modify_meth FOR MODIFY IMPORTING create_imp_param FOR CREATE bdef update_imp_param FOR UPDATE bdef delete_imp_param FOR DELETE bdef action_imp_param FOR ACTION bdef~action cba_imp_param FOR CREATE bdef\_assoc. ...`

- Exceptions cannot be raised in handler methods, hence, the addition [`RAISING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) cannot be used.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following code snippet shows several handler method definitions. The method `create` includes an explicit specification of the `CHANGING` keyword and the parameters for the information retrieval.

``` abap
... 
    METHODS create FOR MODIFY 
    IMPORTING entities FOR CREATE demo_bdef 
    CHANGING failed TYPE DATA mapped TYPE DATA reported TYPE DATA. 
 
    METHODS cba_child FOR MODIFY 
    IMPORTING entities_cba FOR CREATE demo_bdef\_assoc. 
 
    METHODS update FOR MODIFY 
    IMPORTING entities FOR UPDATE demo_bdef. 
 
    METHODS delete FOR MODIFY 
    IMPORTING keys FOR DELETE demo_bdef. 
 
    METHODS read FOR READ 
    IMPORTING keys FOR READ demo_bdef RESULT result. 
 
    METHODS rba_child FOR READ 
    IMPORTING keys_rba FOR READ demo_bdef\_child 
    FULL result_requested RESULT result LINK association_links. 
...
```

## Executable Examples

- The example [Example for RAP Handler Methods](abenrap_handler_methods_abexa.md) demonstrates RAP handler methods within a RAP handler class using a simple unmanaged RAP BO that is draft-enabled.

- The example [ABAP EML - `MODIFY AUGMENTING ENTITY`](abeneml_modify_augmenting_abexa.md) demonstrates the three handler methods `augment_create`, `augment_update` and `augment_cba_assoc` (`assoc` refers to the name of the association) with a RAP projection business object.
