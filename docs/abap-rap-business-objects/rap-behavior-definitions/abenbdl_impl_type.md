---
title: "RAP - Implementation Type"
source_file: abenbdl_impl_type.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - BehaviorDefinitionHeader"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Implementation Type

## Syntax

``` abap
{ managed 
| unmanaged 
| abstract 
| projection } 
| interface ...  
```

## Description

RAP BDL offers the following statements for different [implementation types](../../abap-glossary/abencds_bdef_impl_type_glosry.md):

- `managed`

  The [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md) and the [standard BO operations](abenbdl_standard_operations.md) are handled by the managed RAP BO provider. Recommended for development scenarios in which all essential parts are developed from scratch, without a large amount of existing code (also known as *greenfield* development) with standard implementation. See also: [managed RAP business object](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- `unmanaged`

  The [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md) and the [standard BO operations](abenbdl_standard_operations.md) must be implemented in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). Recommended for development scenarios in which business logic already exists and is intended to be reused (also known as *brownfield* development). See also: [unmanaged RAP business object](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- `projection`

  A [RAP projection behavior definition](../../abap-glossary/abencds_proj_bdef_glosry.md) is based on a managed or unmanaged RAP BO and represents a direct projection of its base behavior definition. It exposes a subset of the base behavior definition's operations and characteristics. In a business application, a projection BDEF provides the means to define service-specific behavior for a BO projection. See also: [RAP BDL - projection behavior definitions](abenbdl_projection_bo.md).

- `abstract`

  A [RAP abstract behavior definition](../../abap-glossary/abencds_abstract_bdef_glosry.md) mainly serves as typing mechanism for deep action or function parameters. Only a limited range of syntax elements is available, such as associations and type mapping. It is not possible to define any transactional behavior in an abstract behavior definition. See also: [RAP abstract behavior definition](abenbdl_abstract.md)

- `interface`

  Defines the behavior of a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md), which serves as interface for stable consumption and is typically released as [released API](../../abap-glossary/abenreleased_api_glosry.md). See also: [RAP Interface Behavior Definition](abenbdl_rap_bo_interface.md).

## Hint

The syntax `implementation {managed|unmanaged|projection|abstract}` is obsolete and should not be used. The keyword `implementation` should be left out. If [BDEF strict mode](abenbdl_strict.md) is enabled, the keyword `implementation` must not be used.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF based on the CDS root view entity `DEMO_RAP_FOREIGN_ENTITY`. The implementation type `managed` is specified in the [RAP behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md).

``` abap
managed implementation in class bp_demo_rap_foreign_entity unique;
strict ( 2 );
//enables MAP_MESSAGES:
foreign entity DEMO_SALES_CDS_SO_1;

define behavior for DEMO_RAP_FOREIGN_ENTITY alias RootEntity
persistent table demo_dbtab_root
lock master
authorization master ( none )
{
  create;
  update;
  delete;

  field ( readonly : update ) key_field;
}
```
