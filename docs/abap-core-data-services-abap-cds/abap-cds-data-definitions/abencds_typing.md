---
title: "CDS DDL - typing"
source_file: abencds_typing.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Common DDL Elements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - typing

## Syntax

``` abap
... dtype | data_element | cds_type  ...  
```

## Description

Types elements or parameters of [CDS entities](../../abap-glossary/abencds_entity_glosry.md) and [aspects](abencds_aspects.md) in [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md). The following is typed:

- Elements of CDS entities:

  - Elements of the element list [`element_list`](abencds_table_entity_element_list.md) in a [CDS table entity](../../abap-glossary/abencds_table_entity_glosry.md).

  - Elements of the element list [`element_list`](abencds_f1_return_list.md) in a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md).

  - Elements of the element list [`element_list`](abencds_ee_elem_list.md) in a [CDS external entity](../../abap-glossary/abencds_external_entity_glosry.md).

  - Elements of the element list [`element_list`](abencds_f1_custom_element_list.md) in a [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md).

  - Elements of the element list [`element_list`](abencds_f1_absent_element_list.md) of a [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md).

  - Elements of the element list [`element_list`](abencds_f1_absent_element_list.md) of a [CDS aspect](abencds_aspects.md).

  - [Typed literals](abencds_typed_literal_v2.md) in a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) or a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md).

  - [CDS virtual elements](../../abap-glossary/abencds_virtual_element_glosry.md) in a [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md).

- Input parameters of CDS entities

  - Input parameters of the parameter list [`parameter_list`](abencds_parameter_list_v2.md) in a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md)

  - Input parameters of the parameter list [`parameter_list`](abencds_parameter_list_apv.md) in a [CDS analytical projection view](../../abap-glossary/abencds_analytical_pv_glosry.md)

  - Input parameters of the parameter list [`parameter_list`](abencds_f1_func_parameter_list.md) in a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md).

  - Input parameters of the parameter list [`parameter_list`](abencds_f1_hiera_parameter_list.md) in a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md).

  - Input parameters of the parameter list [`parameter_list`](abencds_f1_entity_parameter_list.md) in an [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md).

  - Input parameters of the parameter list [`parameter_list`](abencds_f1_entity_parameter_list.md) in an [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md).

  - Input parameters of the parameter list [`parameter_list`](../abap-cds-obsolete-language-elements/abencds_parameter_list_v1.md) in a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md)

Typing can be specified as follows:

- Using a built-in data type from ABAP Dictionary. The addition `PRESERVING TYPE` cannot be specified in this case. All available data types are listed in the topic [ABAP CDS - Built-In Data Types](../abap-cds-data-types/abencds_overview_builtin_types.md).

- Using the name of a [CDS user-defined type](../../abap-glossary/abencds_user_defined_type_glosry.md) `cds_type`.

- Using the name of a [DDIC data element](../../abap-glossary/abendata_element_glosry.md) `data_element`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity has two input parameters. `p_date` is typed with the CDS simple type `DEMO_BT_DATE` and `p_num` is typed with the built-in data type `DEC` with a specified length and number of decimal places.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_PARAMETER_TYPE_VE
  with parameters
    p_date :DEMO_BT_DATE,
    p_num  :abap.dec( 10, 3 )
  as select from demo_expressions
{
  key id,
      $parameters.p_date       as col_date,
      $parameters.p_num + dec3 as col_num
};
```

The class `CL_DEMO_CDS_PARAMETER_TYPE` accesses the view using the following `SELECT` statement:

``` abap
SELECT id, col_date, col_num 
       FROM demo_cds_parameter_type_ve( p_date = @sy-datlo, 
                                        p_num  = '1.234' ) 
       INTO TABLE @DATA(result).
```
