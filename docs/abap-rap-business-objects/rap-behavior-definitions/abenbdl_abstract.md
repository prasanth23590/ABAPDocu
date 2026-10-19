---
title: "RAP - Abstract Behavior Definitions"
source_file: abenbdl_abstract.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Abstract Behavior Definitions

[RAP abstract behavior definitions](../../abap-glossary/abencds_abstract_bdef_glosry.md) are created using the behavior definition language [RAP BDL](../../abap-glossary/abencds_ddl_glosry.md) in [BDL source code](../../abap-glossary/abenbdl_source_code_glosry.md).

A [RAP abstract behavior definition](../../abap-glossary/abencds_abstract_bdef_glosry.md) mainly serves as typing mechanism for deep [action](../../abap-glossary/abenrap_action_glosry.md) or [function](../../abap-glossary/abenrap_function_glosry.md) parameters. Only a limited range of syntax elements is available, such as associations and type mapping. It is not possible to define any transactional behavior in an abstract behavior definition.

**Related Information**

- How to use an abstract BDEF as [input parameter](../../abap-glossary/abeninput_parameter_glosry.md) for a [RAP action](abenbdl_action.md) or a [RAP function](abenbdl_function.md) in a managed or unmanaged RAP BO is described in topic [`RAP BDL - InputParameter`](abenbdl_action_input_param.md).

- How to use an abstract BDEF as [output parameter](../../abap-glossary/abenoutput_parameter_glosry.md) for a RAP action or a RAP function in a managed or unmanaged RAP BO is described in topic [`RAP BDL - OutputParameter`](abenbdl_action_output_para.md).

- Abstract behavior definitions can be classified with the [C0 contract](../../abap-glossary/abenc0_contract_glosry.md) for extensibility.

## Example

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
