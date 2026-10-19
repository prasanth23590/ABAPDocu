---
title: "CDS DDL - EXTEND VIEW ddic_based"
source_file: abencds_extend_view.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entity Extension"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - EXTEND VIEW ddic_based

## Syntax

``` abap
@AbapCatalog.sqlViewAppendName: 'CDS_APPEND_VIEW' 
[@extension_annot1] 
[@extension_annot2] 
... 
EXTEND VIEW ddic_based_view 
       WITH cds_view_extension 
            [association1 
             association2 ...] 
            { select_list_extension } 
            [GROUP BY field1, field2, ...  ] 
            [UNION [ALL] { ... }] [;]  
```

[`@AbapCatalog.sqlViewAppendName: 'CDS_APPEND_VIEW'`](abencds_f1_extend_view_annotations.md) · [`@extension_annot1`](abencds_f1_extend_view_annotations.md) · [`@extension_annot2`](abencds_f1_extend_view_annotations.md)

### Addition

[1. `... GROUP BY field1, field2, ...`](abencds_extend_view.md#addition-1)

[2. `... UNION [ALL] { ... }`](abencds_extend_view.md#addition-2)

## Overview

### Description

Extends an existing [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) `ddic_based_view` using a [CDS DDIC-based view extension](../../abap-glossary/abencds_view_extend_glosry.md) `cds_view_extension` in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md). An existing CDS DDIC-based view (obsolete) can have one or more CDS DDIC-based view extensions.

The extended CDS view `ddic_based_view` must be specified under the name of its [CDS entity](../../abap-glossary/abencds_entity_glosry.md). The name of the [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md) cannot be specified.

## Prerequisite

As a prerequisite for the extension of the CDS view with the statement `EXTEND VIEW`, the elements of the [annotation array](../../abap-glossary/abenannotation_array_glosry.md) [`AbapCatalog.viewEnhancementCategory[ ]`](../abap-cds-obsolete-language-elements/abencds_view_anno_v1.md) must be specified accordingly in its definition with [`DEFINE VIEW`](../abap-cds-obsolete-language-elements/abencds_define_view_v1.md):

- By default or if only the value `#PROJECTION_LIST` is specified, views without [aggregate expressions](../abap-cds-obsolete-language-elements/abencds_aggregate_functions_v1.md) in the `SELECT` list and without a [`UNION`](../abap-cds-obsolete-language-elements/abencds_union_v1.md) clause can be extended.

- In order to extend views that have [aggregate expressions](../abap-cds-obsolete-language-elements/abencds_aggregate_functions_v1.md) in the `SELECT` list, the annotation array must contain the value `#GROUP_BY` alongside `#PROJECTION_LIST`.

- In order to extend views that contain [`UNION`](../abap-cds-obsolete-language-elements/abencds_union_v1.md) clauses, the annotation array must contain the value `#UNION` alongside `#PROJECTION_LIST`.

- If the annotation array contains the value `#NONE`, the view cannot be extended.

**Components of a View Extension**

View extensions can make additions to the original view, but it cannot modify, overwrite, or delete elements from the original view. The following components are possible in a CDS view extension:

- The annotation [`AbapCatalog.sqlViewAppendName`](abencds_f1_extend_view_annotations.md) is mandatory. Further annotations [`extension_annot1`](abencds_f1_extend_view_annotations.md), [`extension_annot2`](abencds_f1_extend_view_annotations.md), ... can also be specified. This is optional.

- New associations `association1`, `association2` can be defined and exposed in the CDS view extension. The same rules apply that are described in topic [CDS DDL - DDIC-based view, `ASSOCIATION`](../abap-cds-obsolete-language-elements/abencds_simple_association_v1.md).

  **Note:** The definition of new [to-child associations](../../abap-glossary/abento_child_association_glosry.md) or [CDS to-parent associations](../../abap-glossary/abento_parent_association_glosry.md) in a view extension is not allowed.

- The elements of the extension list `select_list_extension` specified after `EXTEND VIEW` are added to the existing `SELECT` list. At least one element must be added. It is possible to access all fields of all data sources of the extended view in the extension list `select_list_extension`. The list can have all [elements](../abap-cds-obsolete-language-elements/abencds_select_list_entry_v1.md) of a [`SELECT` list](../abap-cds-obsolete-language-elements/abencds_select_list_v1.md), namely:

  - [field](abencds_field_v2.md) of a data source

  - [Input parameters](../abap-cds-obsolete-language-elements/abencds_parameter_v1.md) of the extended CDS view. It is not possible to specify new input parameters in a view extension.

  - It can expose a [CDS association](abencds_select_list_association_v2.md) of the extended view or a newly defined association

  - Using a [path expressions](../abap-cds-obsolete-language-elements/abencds_path_expression_v1.md), a field of an association target can be included. Path expressions are possible for associations of the extended view or for newly defined associations.

  - [literals, session variables, expressions and functions](../abap-cds-obsolete-language-elements/abencds_operands_and_expr_v1.md)

    **Note:** To add aggregate expressions to a view extension, special rules apply. See below.

- Aggregate expressions are possible in the `SELECT` list of a view extension only if the following conditions are met:

  - The original view must contain [aggregate expressions](../abap-cds-obsolete-language-elements/abencds_aggregate_functions_v1.md). If the original view does not contain any aggregate expressions, this is not possible.

  - The extended view must be annotated with `AbapCatalog.viewEnhancementCategory [#PROJECTION_LIST, #GROUP_BY]`

  - If non-aggregated elements are added to a CDS view with aggregate expressions, then the [`GROUP-BY`](../abap-cds-obsolete-language-elements/abencds_group_by_v1.md) clause must be extended using the addition `GROUP BY`

- If the original view contains [`UNION`](../abap-cds-obsolete-language-elements/abencds_union_v1.md), equivalent `UNION` additions must be used in the statement `EXTEND VIEW`. As a prerequisite, the extended view must be annotated with `AbapCatalog.viewEnhancementCategory [#PROJECTION_LIST, #UNION]`

  If an appended element already occurs in the existing `SELECT` list or if a different extension occurs, it must be given an alternative element name using `AS`.

## Restrictions

- CDS views with an explicit [name list](../abap-cds-obsolete-language-elements/abencds_name_list_v1.md) cannot currently be extended.

- CDS view extensions themselves cannot be extended.

- It is not possible to specify new input parameters in a view extension.

- No addition [`ROOT`](../abap-cds-obsolete-language-elements/abencds_define_root_view_v1.md) can be specified in the statement `EXTEND VIEW` to transform a regular view to a [root entity](../../abap-glossary/abenroot_entity_glosry.md).

- An appended field cannot be defined as a key field using `KEY`.

- The definition of new to-parent or to-child associations in a view extension is not allowed.

- For views that have an element of data type `LRAW` or `LCHR` in the `SELECT` list, no view extension is possible and the annotation ` AbapCatalog.viewEnhancementCategory[#NONE]` is enforced. The reason is that elements of data types `LRAW` or `LCHR` must always be in the last position of the `SELECT` list.

- The annotation [`ClientHandling.clientSafe`](../abap-cds-annotations/abencds_1549616294_anno.md) is not supported as a header annotation in view extensions.

**Naming**

Two repository objects are created for a CDS view extension that is defined using EXTEND VIEW. A name must be specified for each of the two objects:

- The actual name `cds_view_extension` of the CDS view extension is specified after the keywords `EXTEND VIEW`. This name follows the same rules as the name of an [DDIC append view](../../abap-glossary/abenddic_append_view_glosry.md), but can have up to 30 characters.

- The name `CDS_APPEND_VIEW` for an [append view](../../abap-glossary/abenddic_append_view_glosry.md) in ABAP Dictionary must be specified in quotation marks after the annotation [`@AbapCatalog.sqlViewAppendName`](abencds_f1_extend_view_annotations.md). This name is subject to the same rules as the name of a [DDIC database view](../../abap-glossary/abendatabase_view_glosry.md) in ABAP Dictionary, see topic DDIC - Naming Rules for DDIC Views. The new DDIC append view extends the [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md) of the extended CDS view. The name given to the DDIC append view can no longer be changed after the CDS view extension is transported into a follow-on system.

The name of the new DDIC append view and of the actual CDS view extension should be located in the customer namespace (or in the namespace of a partner or special development) to protect it against being overwritten by upgrades or new releases.

- Once the DDL source code of a CDS view extension has been transported, the actual name `cds_view_extension` and the name of the DDIC append view `CDS_APPEND_VIEW` can no longer be changed. The extended view `ddic_based_view` can also no longer be changed.

**Note:** The DDL source code of a CDS view extension does not need to have the same name as the CDS view extension entity, but it is advisable to use the name of the entity.

### Hints

- Currently it is not possible to define extension categories for CDS views. As a consequence, the following restrictions apply:

  - CDS views have the property `can be extended in any way` with respect to the [extension category of DDIC structures](../../abap-dictionary-ddic/ddic-data-types/abenddic_structures_enh_cat.md). The consequences of this must be respected when extending a CDS view.

  - The properties of a CDS view defined using [annotations](../abap-cds-obsolete-language-elements/abencds_view_anno_v1.md), such as switching on [table buffering](../../abap-glossary/abentable_buffering_glosry.md), cannot currently be modified using extensions.

- CDS view extensions specified with `EXTEND ENTITY` are recommended for CDS DDIC-based views (obsolete) only. However, for compatibility and migration reasons, it is also possible to extend [CDS projection views](../../abap-glossary/abencds_projection_view_glosry.md) or [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) with the statement `EXTEND VIEW`. However, view extends defined using `EXTEND VIEW` do not support the syntax elements specific to projection views and CDS view entities. Therefore, it is recommended that the statement [`EXTEND VIEW ENTITY`](abencds_extend_view_entity.md) is used for extensions of CDS projection views and CDS view entities instead.

- If, for some reason, a CDS projection view or a CDS view entity is extended with `EXTEND VIEW`, the [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md) is deleted (as CDS projection views and CDS view entities do not have any DDIC artefacts), and entity annotations referring to the CDS-managed DDIC view are ignored.

- CDS DDIC-based views (obsolete) are [obsolete](../abap-cds-obsolete-language-elements/abencds_ddic_entity.md). If new CDS views are required, CDS view entities should be used.

It is not allowed to use inner joins in view extensions, since it would affect the result cardinality of the extended view and would therefore represent a modification, which is not allowed. Inner joins, for example in the form of path expressions with a join attribute, lead to syntax check errors.

## Addition 1

`... GROUP BY field1, field2, ...`

### Description

This addition must be specified if elements not defined using aggregate expressions are added to a view with [aggregate expressions](../abap-cds-obsolete-language-elements/abencds_aggregate_functions_v1.md). These elements must be specified after `GROUP BY` add extend the [`GROUP-BY`](../abap-cds-obsolete-language-elements/abencds_group_by_v1.md) clause of the original view. With respect to the extended view, the extended `GROUP-BY` clause must follow the general rules for a `GROUP-BY` clause.

The addition cannot be specified if the definition of the original view does not contain any aggregate expressions in its `SELECT` list.

### Hint

Extensions of a view with aggregate expressions require it to contain the annotation array `viewEnhancementCategory[ ]` with the value `#GROUP_BY`.

## Addition 2

`... UNION [ALL] { ... }`

### Description

This addition must be specified when a view with [`UNION`](../abap-cds-obsolete-language-elements/abencds_union_v1.md) clauses is extended. A corresponding `UNION` addition must be specified for each `UNION` clause of the original view. The addition `ALL` must be specified each time it is specified in the associated `UNION` clause of the original view. The curly brackets can contain elements that extend the `SELECT` list of the associated `UNION` clause of the original view. As specified by the `SELECT` list extended using `select_list_extension`, the `UNION` clauses must be extended so that the rules for `UNION` clauses are not broken in the extended view.

The addition cannot be specified if the definition of the original view does not have a `UNION` clause.

### Hint

Extensions of a view with `UNION` clauses require it to contain the annotation array `viewEnhancementCategory[ ]` with the value `#UNION`.
