---
title: "CDS DDL - parameter"
source_file: abencds_f1_param.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Common DDL Elements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - parameter

## Syntax

``` abap
... [@parameter_annot1] 
    [@parameter_annot2] 
    ... 
    pname : typing 
    [@<parameter_annot1] 
    [@<parameter_annot2] 
    ...  
```

[`@parameter_annot1`](abencds_f1_parameter_annotations.md) · [`@parameter_annot2`](abencds_f1_parameter_annotations.md) · [`typing`](abencds_typing.md) · [`@<parameter_annot1`](abencds_f1_parameter_annotations.md) · [`@<parameter_annot2`](abencds_f1_parameter_annotations.md)

### Addition

[`... @parameter_annot | ... @<parameter_annot`](abencds_f1_param.md#addition)

## Overview

### Description

Defines a `CDS parameter` called `pname` in one of the following:

- [Parameter list](abencds_parameter_list_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md)

- [Parameter list](abencds_parameter_list_apv.md) of a [CDS analytical projection view](../../abap-glossary/abencds_analytical_pv_glosry.md)

- [Parameter list](abencds_f1_func_parameter_list.md) of a [CDS table function](../../abap-glossary/abencds_table_function_glosry.md)

- [Parameter list](abencds_f1_hiera_parameter_list.md) of a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md)

- [Parameter list](abencds_f1_custom_parameter_list.md) of a [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md)

- [Parameter list](abencds_f1_entity_parameter_list.md) of an [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md)

- [Parameter list](../abap-cds-obsolete-language-elements/abencds_parameter_list_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md)

The name `pname` must comply with the naming rules for [names](../abap-cds-syntax/abencds_general_syntax_rules.md). Furthermore, `pname` cannot contain any slash (/) characters and cannot be a reserved name in ABAP Dictionary. The name `pname` must be unique and be located in the namespace of the elements and exposed CDS associations of the current CDS entity. In table functions, the reserved name `connection` cannot be used. All reserved names that cannot be used are specified in the DDIC database table `TRESE`. The evaluation of names is not case-sensitive. Blanks in the comma-separated parameter list are ignored and can be omitted.

Each parameter must be typed with an elementary data type. All data types listed in topic [`Typing`](abencds_typing.md) are allowed, except for `abap.accp`, `abap.geom_ewkb`, `abap.rawstring`, and `abap.string`. In CDS view entities and CDS table functions, parameters can also have data type `abap.string`.

A [CDS persistent entity](../../abap-glossary/abencds_sql_entity_glosry.md) for which CDS parameters are defined as input parameters can be used as

- data source or in a path expression of a different [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) or [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md)

- A [data source](../../abap-programming-language/abap-database-access/abapselect_data_source.md) of a [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) statement from ABAP SQL in ABAP

In these cases, each input parameter must be assigned a suitable actual parameter whose value is then used in the operand positions in which the parameter is specified. The actual parameters are assigned using a parenthesized comma-separated list as follows:

[`... cds_entity( pname1 : act1, pname2 : act2, ...) ...`](abencds_select_parameters_v2.md),

This list must be specified directly after the name of the view when using an entity with parameters (both within the CDS DDL in ABAP CDS and in ABAP SQL). In ABAP SQL, an equal sign (`=`) is used instead of a colon (`:`).

### Hint

It is not currently possible to define optional input parameters or replacement parameters for input parameters. The annotation [`@Environment.systemField`](abencds_f1_parameter_annotations.md) can be used, however, to make ABAP SQL pass ABAP system fields to an input parameter implicitly.

## Addition

`... @parameter_annot | ... @<parameter_annot`

### Description

Specifies annotations for the parameter. The annotations can be specified before the parameter using [`@parameter_annot`](abencds_f1_parameter_annotations.md) or after the parameter using [`<@parameter_annot`](abencds_f1_parameter_annotations.md). The latter is possible only for [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md), and [CDS hierarchies](../../abap-glossary/abencds_hierarchy_glosry.md) but not for [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md), [CDS custom entities](../../abap-glossary/abencds_custom_entity_glosry.md), and [CDS abstract entities](../../abap-glossary/abencds_abstract_entity_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example shows a CDS view entity with one CDS parameter called `P_MyParameter`.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'SDDL: Interface (BO) View for BuPa'
define root view entity DEMO_SALES_CDS_SO_PARAM_VE
  with parameters
    P_MyParameter : abap.char( 5 )
  as select from
    demo_sales_bupa as bupa
    {
      key id,
          given_name,
          middle_name,
          family_name,
          $parameters.P_MyParameter as my_parameter
    }
```
