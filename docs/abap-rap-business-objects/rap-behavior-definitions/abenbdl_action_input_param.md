---
title: "RAP - InputParameter"
source_file: abenbdl_action_input_param.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - RAP BO Operation, Additions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - InputParameter

## Syntax Forms

**Flat Parameter**

``` abap
... parameter { ParameterEntity | $self };
```

**Deep Parameter**

``` abap
... [deep [table]] parameter AbstractBDEF;
```

### Alternative

[1. `... parameter { ParameterEntity | $self };`](abenbdl_action_input_param.md#alternative-1)

[2. `... [deep [table]] parameter AbstractBDEF;`](abenbdl_action_input_param.html#alternative-2)

## Overview

### Description

Defines an [input parameter](../../abap-glossary/abeninput_parameter_glosry.md) for an [action](abenbdl_action.md) or [function](abenbdl_function.md). The input parameter can be flat or deep.

## More Information

Development guide for the ABAP RESTful Application Programming Model, topic [Action Definition](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/14ddc6b2442b4b97842af9158a1c9c44?version=sap_cross_product_abap).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF based on the CDS root view entity `DEMO_CDS_ACTION_INPUT_PARAM`. The business object describes a purchase order item. The BDEF defines one action, `deductDiscount`. This action has an input parameter for the discount percentage and it calculates the price of an item minus the discount. It is implemented in the behavior pool `BP_DEMO_CDS_ACTION_INPUT_PARAM`.

``` abap
managed implementation in class bp_demo_cds_action_input_param unique;
strict(2);

define behavior for DEMO_CDS_ACTION_INPUT_PARAM alias PurchaseItem
persistent table demo_purch_doc_i
lock master
authorization master (none)
{
  create;
  update;
  delete;

  action deductDiscount parameter DEMO_CDS_ABSTRACT_DISCOUNT result [1] $self;

  field(readonly:update) PurchaseDocument, PurchaseDocumentItem;

  mapping for DEMO_PURCH_DOC_I corresponding;
}
```

The class `CL_DEMO_CDS_ACTION_REDUCE` accesses the business object using [EML](../../abap-glossary/abeneml_glosry.md) and carries out the following operations:

- It asks the user to specify the discount in percent.

- It creates two instances of a purchase order item, identified by the key `PurchaseDocumentItem`, and assigns a price `Price` to each.

- It executes the action `deductDiscount`.

- Using the ABAP SQL `SELECT` statement, the content of the underlying database table is displayed.

Result: the price is reduced by the specified discount - here, the discount was specified as 10 percent. ![figure](images_abdoc_action_discount.png)

### Executable Example

The example above is explained in detail in the executable example [RAP BDL - action with input parameter](abenbdl_action2_abexa.md).

## Alternative 1

`parameter { ParameterEntity | $self }`

### Description

- The input parameter entity `ParameterEntity` can be a [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md) or a classic [DDIC type](../../abap-glossary/abenddic_type_glosry.md)

- `$self` can be specified if the input parameter entity is the same abstract entity the action or function is assigned to.

- Input parameters with `$self` are only allowed on static actions or functions. When specified for instance actions or functions, there is no syntax check warning, and a [runtime error](../../abap-glossary/abenruntime_error_glosry.md) occurs instead when a [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) accesses the action or function in question.

### Hints

- If [BDEF strict mode](abenbdl_strict.md) is enabled, `$self` is not allowed as input parameter.

- If a CDS abstract entity is specified as input parameter, the annotation [`EndUserText.label`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_f1_element_annotation.md) can be used to define a label that is displayed on the user interface in an OData scenario.

## Alternative 2

`[deep [table]] parameter AbstractBDEF`

### Description

The input parameter `AbstractBDEF` must be a [RAP abstract BDEF](abenbdl_abstract.md) [`with hierarchy`](abenbdl_bdef_abstract_header.md). The [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) for an abstract BDEF is a hierarchy that contains all entity fields plus a component for every [CDS composition](../../abap-glossary/abencds_composition_glosry.md).

The following syntax options are available:

- `deep parameter AbstractBDEF`: The input parameter is interpreted as a structure.

- `deep table parameter AbstractBDEF`: The input parameter is interpreted a table.

### Hint

An abstract BDEF can also be used as input parameter only with the keyword `parameter`. In this case, it is interpreted as flat parameter. It represents the same derived type as a single CDS abstract entity and does not offer any additional value.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows an abstract BDEF with three nodes that is constructed as hierarchy.

``` abap
abstract;
strict(2);
with hierarchy;

define behavior for DEMO_CDS_ABSTRACT_ROOT alias Root
{
  field ( suppress ) Dummy;

  deep mapping for DEMO_CDS_ABSTRACT_STRUC
  {
    char10 = char_10;
    Integer4 = integer_4;
    sub _itemStructure = struktur;
    sub _itemTable = tabelle;
  }

  association _itemTable;
  association _itemStructure;
}

define behavior for DEMO_CDS_ABSTRACT_ITEMSTRUCT alias ItemStructure
{
  field ( suppress ) Dummy, ToRoot;

  deep mapping for DEMO_ABSTRACT_ITEMSTRUCT
  {
    Char10 = char_10;
    Integer4 = integer_4;
  }

  association _parent;
}

define behavior for DEMO_CDS_ABSTRACT_ITEMTABLE alias ItemTable
{
  field ( suppress ) Dummy, ToRoot;

  deep mapping for DEMO_ABSTRACT_ITEMTABLE corresponding
  {
    Char10 = char_10;
    Integer4 = integer_4;
  }

  association _parent;
}
```

The managed BDEF `DEMO_CDS_DEEP_PARAMETER` uses the abstract BDEF as action parameter in three actions.

``` abap
managed implementation in class bp_demo_cds_deep_parameter unique;
strict(2);

define behavior for DEMO_CDS_DEEP_PARAMETER
persistent table DEMO_BO_DEEP
lock master
authorization master ( none )
{
  create;
  update;
  delete;

    mapping for demo_bo_deep
    {
    RootBO = root;
    }

  field (readonly:update) RootBO;

// mapping: none
  action a2_from_flat              parameter DEMO_CDS_ABSTRACT_ROOT;

// mapping: structure
  action a2_from_deep       deep  parameter DEMO_CDS_ABSTRACT_ROOT;

 // mapping: table
  action a2_from_deep_table deep table
                                  parameter DEMO_CDS_ABSTRACT_ROOT;

//deep selective output parameter
  action a2_deep_result deep result selective [1]
    DEMO_CDS_ABSTRACT_ROOT;
}
```

The abstract BDEF is used as flat parameter, as structure, or as table, depending on the keywords used.

- Usage as flat parameter in action `a2_from_flat`

  ![figure](images_abdoc_abstract_flat.jpg)

- Usage as structure in action `a2_from_deep`

  ![figure](images_abdoc_abstract_structure.jpg)

- Usage as table in action `a2_from_deep_table`

  ![figure](images_abdoc_abstract_table.jpg)
