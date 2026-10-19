---
title: "CDS DDL - DEFINE HIERARCHY"
source_file: abencds_f1_define_hierarchy.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Hierarchies"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE HIERARCHY

## Syntax

``` abap
[@entity_annot1] 
[@entity_annot2] 
... 
[@hierarchy_annot1] 
[@hierarchy_annot2] 
... 
[DEFINE] HIERARCHY hierarchy 
         [parameter_list] 
         AS PARENT CHILD HIERARCHY( 
           SOURCE cds_entity 
           CHILD TO PARENT ASSOCIATION _hierarchy_assoc 
           [PERIOD FROM field1 TO field2 VALID FROM from TO to] 
           [DIRECTORY _directory_assoc FILTER BY cds_cond] 
           [START WHERE cds_cond] 
           SIBLINGS ORDER BY field1 [ASCENDING|DESCENDING][, 
                             field2 [ASCENDING|DESCENDING], ...] 
           [DEPTH depth] 
           [NODETYPE node_type] 
           [LOAD BULK|INCREMENTAL|load_option] 
           [MULTIPLE PARENTS {NOT ALLOWED}|{LEAVES ONLY}|ALLOWED] 
           [ORPHANS IGNORE|ERROR|ROOT] 
           [CYCLES ERROR|BREAKUP] 
           [GENERATE SPANTREE] 
           [CACHE ON|OFF|FORCE]) 
     { element_list }  
```

[`@entity_annot1`](abencds_f1_entity_annotations.md) · [`@entity_annot2`](abencds_f1_entity_annotations.md) · [`@hierarchy_annot1`](abencds_f1_hierarchy_annotations.md) · [`@hierarchy_annot2`](abencds_f1_hierarchy_annotations.md) · [`parameter_list`](abencds_f1_hiera_parameter_list.md) · [`element_list`](abencds_f1_hiera_element_list.md)

### Addition

[1. `... SOURCE cds_entity`](abencds_f1_define_hierarchy.md#addition-1)

[2. `... CHILD TO PARENT ASSOCIATION _hierarchy_assoc`](abencds_f1_define_hierarchy.md#addition-2)

[3. `... PERIOD FROM field1 TO field2 VALID FROM from TO to`](abencds_f1_define_hierarchy.md#addition-3)

[4. `... DIRECTORY _directory_assoc FILTER BY cds_cond`](abencds_f1_define_hierarchy.md#addition-4)

[5. `... START WHERE cds_cond`](abencds_f1_define_hierarchy.md#addition-5)

[6. `... SIBLINGS ORDER BY field1 [ASCENDING|DESCENDING], ...`](abencds_f1_define_hierarchy.md#addition-6)

[7. `... DEPTH depth`](abencds_f1_define_hierarchy.md#addition-7)

[8. `... NODETYPE node_type`](abencds_f1_define_hierarchy.md#addition-8)

[9. `... LOAD BULK|INCREMENTAL|load_option`](abencds_f1_define_hierarchy.md#addition-9)

[10. `... MULTIPLE PARENTS {NOT ALLOWED}|{LEAVES ONLY}|ALLOWED`](abencds_f1_define_hierarchy.md#addition-10)

[11. `... ORPHANS IGNORE|ERROR|ROOT`](abencds_f1_define_hierarchy.md#addition-11)

[12. `... CYCLES ERROR|BREAKUP`](abencds_f1_define_hierarchy.md#addition-12)

[13. `... GENERATE SPANTREE`](abencds_f1_define_hierarchy.md#addition-13)

[14. `... CACHE ON|OFF|FORCE`](abencds_f1_define_hierarchy.md#addition-14)

## Overview

### Description

Defines a [CDS entity](../../abap-glossary/abencds_entity_glosry.md) `hierarchy` as a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md) in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md). A CDS hierarchy has a tabular result set whose rows construct [parent-child relationships](../../abap-glossary/abenpcr_glosry.md). When a CDS hierarchy is accessed as the data source of a [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) query, it is handled like an [ABAP SQL hierarchy](../../abap-glossary/abensql_hierarchy_glosry.md) ([parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md)) in which additional [hierarchy columns](../../abap-glossary/abenhierarchy_column_glosry.md) can be selected.

- [`@entity_annot`](abencds_f1_entity_annotations.md) and [`@hierarchy_annot`](abencds_f1_hierarchy_annotations.md) can be used to specify optional [annotations](../../abap-glossary/abencds_annotation_glosry.md) for the CDS hierarchy.

- [`parameter_list`](abencds_f1_hiera_parameter_list.md) is used to declare a list of optional input parameters for the CDS hierarchy.

- [`element_list`](abencds_f1_hiera_element_list.md) is used to declare the elements of the CDS hierarchy.

The additions in parentheses after `AS PARENT CHILD HIERARCHY` define the way the hierarchy is created:

- `SOURCE` must be followed by a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), a [CDS table entity](../../abap-glossary/abencds_table_entity_glosry.md), or a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) `cds_entity` as the source of the hierarchy.

- `CHILD TO PARENT ASSOCIATION` must be followed by a [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md) `_hierarchy_assoc` exposed by the source `cds_entity`. The hierarchy association must be a [self-association](../../abap-glossary/abenself_association_glosry.md) where the [association source](../../abap-glossary/abenassociation_source_glosry.md) and [association target](../../abap-glossary/abenassociation_target_glosry.md) must be the source `cds_view`. The `ON` condition of the hierarchy association defines the [parent-child relationships](../../abap-glossary/abenpcr_glosry.md) between the [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md).

- `START WHERE` can be followed by a start condition that defines [root nodes](../../abap-glossary/abenroot_node_glosry.md) for the [root node set](../../abap-glossary/abenroot_node_set_glosry.md) of the hierarchy. The hierarchy consists of the root nodes of the root node set and their [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md).

  In semantic key scenarios, i.e. when the column that contains the parent node has a numeric data type, the `START WHERE` condition can be left out. In this case, an implicit `START WHERE` condition is generated, so that the root node set consists of all rows where the column that contains the [parent node](../../abap-glossary/abenparent_node_glosry.md) (as defined by the hierarchy association) is initial. In UUID scenarios, the condition where to start is not implicitly set and must be specified explicitly. Otherwise, a syntax check error occurs.

All other additions define further properties of the hierarchy. The rows of the tabular result set of the CDS hierarchy are the [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md) of the new hierarchy but without its [hierarchy columns](../../abap-glossary/abenhierarchy_column_glosry.md).

The name of a CDS hierarchy is in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP.

### Hints

- The syntax and functions of a CDS hierarchy overlap to a large extent with the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](../../abap-programming-language/abap-database-access/abenselect_hierarchy_gen_assoc.md) for a [parent-child-based hierarchy](../../abap-glossary/abenpc_based_hiera_glosry.md) in ABAP SQL

- Unlike in ABAP SQL, however, ABAP CDS cannot access the additional [hierarchy columns](../../abap-glossary/abenhierarchy_column_glosry.md) of a CDS hierarchy. Instead, the associated [hierarchy attributes](../../abap-glossary/abenhierarchy_attribute_glosry.md) must be entered in the [element list](abencds_f1_hiera_element_list.md) of the CDS hierarchy if required.

- On [SAP HANA databases](../../abap-glossary/abenhana_database_glosry.md), the result sets of CDS hierarchies plus the hierarchy generator `HIERARCHY` are created by using the SAP HANA hierarchy generator function `HIERARCHY` and similar. More information can be found in the [HANA SQL documentation](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/b4b0eec1968f41a099c828a4a6c8ca0f).

- Since hierarchies generated from the `START WHERE` condition are buffered on the database, it is advisable to use fixed values for the root nodes of large hierarchies of data that do not change often. To evaluate subnodes of such hierarchies, the [hierarchy navigators](../../abap-glossary/abenhierarchy_navigator_glosry.md) of ABAP SQL can then be used. The usage of arbitrary parameters for specifying the root nodes especially should be restricted to small hierarchies or for demonstration purposes only.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Defines a simple CDS hierarchy. The class `CL_DEMO_HIERARCHY_TREE` accesses the CDS hierarchy and compares this with accesses to similar hierarchies in ABAP SQL.

``` abap
define hierarchy DEMO_CDS_SIMPLE_TREE
  with parameters
    p_id : abap.int4
  as parent child hierarchy(
    source
      DEMO_CDS_SIMPLE_TREE_SOURCE
      child to parent association _tree
      start where
        id = :p_id
      siblings order by
        id ascending
    )
    {
      id,
      parent,
      name
    }
```

## Addition 1

`... SOURCE cds_entity`

### Description

The mandatory addition `SOURCE` specifies a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), a [CDS table entity](../../abap-glossary/abencds_table_entity_glosry.md), or a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) as the [hierarchy source](../../abap-glossary/abenhierarchy_source_glosry.md) of the CDS hierarchy. This source must [expose](abencds_select_list_association_v2.md) the [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md) specified after `CHILD TO PARENT ASSOCIATION` in its `SELECT` list.

### Hint

A CDS hierarchy cannot be the source of another CDS hierarchy.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The CDS hierarchy of the previous example uses the following CDS view entity as a source:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_SIMPLE_TREE_SOURCE
  as select from demo_simple_tree
  association to exact one DEMO_CDS_SIMPLE_TREE_SOURCE as _tree 
    on $projection.parent = _tree.id
{
      _tree,
  key id,
      parent_id as parent,
      name
}
```

## Addition 2

`... CHILD TO PARENT ASSOCIATION _hierarchy_assoc`

### Description

The mandatory addition `CHILD TO PARENT ASSOCIATION` specifies the [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md) whose `ON` condition selects the [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md) of the [root node set](../../abap-glossary/abenroot_node_set_glosry.md). The hierarchy association must be exposed by the CDS entity specified after `SOURCE`.

The hierarchy association defines the parent-child relationship between the [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md). The following conditions apply here:

- The CDS association must be a [self-association](../../abap-glossary/abenself_association_glosry.md).

- Only equality comparisons with the operator `=` and combined using `AND` can occur in the `ON` condition of the CDS association.

- In each comparison in the `ON` condition, one field of the [association source](../../abap-glossary/abenassociation_source_glosry.md) must be compared with a field (prefixed with `_hierarchy_assoc`) of the [association target](../../abap-glossary/abenassociation_target_glosry.md).

- The [association source](../../abap-glossary/abenassociation_source_glosry.md) of the CDS association cannot contain any fields that have the same name as a [hierarchy attribute](abencds_hierarchy_attributes.md). An alternative element name must be defined for these fields.

Each row of the result set of the source `hierarchy_source` that meets the `ON` condition for an existing hierarchy node is included recursively in the hierarchy as its [child node](../../abap-glossary/abenchild_node_glosry.md) (if this is possible).

### Hint

The optional additions define further conditions specifying whether a row can be included as a hierarchy node or not.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The CDS view entity of the previous example exposes its association `_tree`. This CDS association meets all requirements of a hierarchy association and can be used as one.

## Addition 3

`... PERIOD FROM field1 TO field2 VALID FROM from TO to`

### Description

The optional addition `PERIOD` defines the hierarchy as a [temporal SQL hierarchy](../../abap-glossary/abentemporal_hierarchy_glosry.md) in which the hierarchy nodes are limited by an adjustment of time intervals.

- `field1` and `field2` are used to specify the fields of the source `cds_entity` that define the lower and upper limits of a [period](../../abap-glossary/abenperiod_glosry.md) in the hierarchy data. `field1` and `field2` must be different fields of the same data type. This can be:

  - The built-in type [`DATS`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DATN`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`UTCL`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md), [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 15 and 7 decimal places, or [`DEC`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) with length 21 and 7 decimal places.

  - A data type that is defined by one of the [DDIC data elements](../../abap-glossary/abendata_element_glosry.md) `TIMESTAMP` or `TIMESTAMPL`.

- `from` and `to` define the lower and upper limit of a time interval that acts as a condition for the periods of the [root node set](../../abap-glossary/abenroot_node_set_glosry.md). The data type of `from` and `to` must match the data type of `field1` and `field2`. The following can be specified:

  - Parameters from the [parameter list](abencds_f1_hiera_parameter_list.md) of the hierarchy. Here, only the syntax [`$parameters.pname`](abencds_parameter_v2.md) is possible.

  - [Literals](abencds_literal_v2.md) whose value matches the requested data type. [Typed date literals](abencds_typed_literal_v2.md) are recommended.

A temporal SQL hierarchy is created as follows:

- Only [root nodes](../../abap-glossary/abenroot_node_glosry.md) of the [root node set](../../abap-glossary/abenroot_node_set_glosry.md) in which the period defined using `field1` and `field2` has a non empty intersection with the time interval defined by `from` and `to` are taken into account. This intersection forms the [validity interval](../../abap-glossary/abenvalidity_interval_glosry.md) of the root node.

- Only [child nodes](../../abap-glossary/abenchild_node_glosry.md) in which the period defined by `field1` and `field2` has a non empty intersection with the validity interval of the [parent node](../../abap-glossary/abenparent_node_glosry.md) are generated. This intersection forms the [validity interval](../../abap-glossary/abenvalidity_interval_glosry.md) of the child node.

For temporal SQL hierarchies, there are additional [hierarchy attributes](abencds_hierarchy_attributes.md) `VALID_FROM` and `VALID_UNTIL` that contain the interval limits of the [validity interval](../../abap-glossary/abenvalidity_interval_glosry.md) of each hierarchy node.

The addition `PERIOD` must not be used with `GENERATE SPANTREE`.

### Hints

- The validity interval of a descendant node is always a subset of a validity interval of all ancestor nodes. Validity intervals can only remain the same or become narrower from hierarchy level to hierarchy level, they can never get wider.

- For a descendant node to belong to a temporal SQL hierarchy, it is not sufficient for its period to overlap with the time interval defined by `from` and `to`. Only the validity interval of the parent node is decisive. A path of a regular hierarchy is truncated in a temporal SQL hierarchy at the position in which there is no intersection between the period and the preceding validity interval.

- The [association source](../../abap-glossary/abenassociation_source_glosry.md) of the current [hierarchy association](../../abap-glossary/abenhierarchy_association_glosry.md) must not have any fields called `VALID_FROM` or `VALID_UNTIL`. An alternative element name must be defined for these fields.

- The value of `to` can also be less than the value of `from`. However, a validity interval is formed where necessary. In contrast, if the value of the lower interval limit of the period is greater than the value of the upper interval limit, the validity interval is empty.

- Additions such as `MULTIPLE PARENTS` or `CYCLES` affect the temporal SQL hierarchy. Nodes that would raise an exception in a regular hierarchy can be hidden in a temporal SQL hierarchy.

- On an [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md), the associated hierarchy generator function [`HIERARCHY_TEMPORAL`](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/2969da89b87f4abd85fd0b5f9f5bc395) is used to create a temporal SQL hierarchy.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS hierarchies create two [temporal SQL hierarchies](../../abap-glossary/abentemporal_hierarchy_glosry.md). Here, date fields and time stamp fields are both used once as [periods](../../abap-glossary/abenperiod_glosry.md). The class `CL_DEMO_HIERARCHY_TEMPORAL` accesses the CDS hierarchies and compares the results with the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](../../abap-programming-language/abap-database-access/abenselect_hierarchy_generator.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) used in a similar way. When executed, `CL_DEMO_HIERARCHY_TEMPORAL` demonstrates how the addition `PERIOD` works.

``` abap
define hierarchy DEMO_CDS_PARENT_CHILD_DATE_PRD
  with parameters
    p_date_from : dats,
    p_date_to   : dats
  as parent child hierarchy(
    source DEMO_CDS_PARENT_CHILD_SRC_PRD
    child to parent association _relat
    period from date_from to date_to
      valid from $parameters.p_date_from 
              to $parameters.p_date_to
    start where
      id = 'A'
    siblings order by
      id
  )
{
  id,
  parent,
  $node.valid_from  as h_valid_from,
  $node.valid_until as h_valid_until }

```abap
define hierarchy DEMO_CDS_PARENT_CHILD_TS_PRD
  with parameters
    p_ts_from : timestamp,
    p_ts_to   : timestamp
  as parent child hierarchy(
    source DEMO_CDS_PARENT_CHILD_SRC_PRD
    child to parent association _relat
    period from ts_from to ts_to
      valid from $parameters.p_ts_from 
              to $parameters.p_ts_to
    start where
      id = 'A'
    siblings order by
      id
  )
{
  id,
  parent,
  $node.valid_from  as h_valid_from,
  $node.valid_until as h_valid_until }
```

## Addition 4

`... DIRECTORY _directory_assoc FILTER BY cds_cond`

### Description

The optional addition `DIRECTORY` defines a filter condition `cds_cond` for the rows of the source of the hierarchy specified after `SOURCE`. The hierarchy is generated only from those rows in the source that meet the filter condition. For `cds_cond`, `AND` comparisons for equality using `=` can be specified as follows:

- The operator on the left side of a comparison must be an element of the current hierarchy whose name occurs as an operand in the CDS view specified after `SOURCE` as follows:

  - On the left side of an `ON` condition of a CDS association `_directory_assoc`.

  - On the left side of an `ON` condition of the hierarchy association `_hierarchy_assoc`.

- The operator on the right side of the comparison can be a [typed literal](abencds_typed_literal_v2.md) or a type-compliant parameter from the [parameter list](abencds_f1_hiera_parameter_list.md) of the hierarchy.

The same [rules](abencds_cond_expr_types_v2.md) apply to the comparable types as to CDS views.

### Hints

- A filter condition removes all hierarchy nodes and their descendant nodes from the result set that do not match the condition `cds_cond`.

- The content of the [association target](../../abap-glossary/abenassociation_target_glosry.md) of the CDS association `_directory_assoc` is ignored when the filter condition is evaluated.

- The restriction of the operands on the left side of a comparison to the operands of a CDS association of the source is mainly intended for analytical data models that are evaluated by an analytical runtime. The analytical runtime reads data from the [association target](../../abap-glossary/abenassociation_target_glosry.md) of this CDS association and passes it to input parameters of the hierarchy that evaluates them in the filter condition.

## More Information

For more information about hierarchy directories, see [*Hierarchy Directories*](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/eac380b170594d86910e92829f4c8d3d?version=sap_cross_product_abap) in the ABAP Data Models guide on SAP Help Portal.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS view entity defines a self association `_pcr`, which itself defines a parent-child relationship, and a CDS association `_dir` of a DDIC database table `DEMO_HIERA_DIR`:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_PARENT_CHILD_SRC_DIR
  as select from
    demo_parchld_dir
    association to many DEMO_CDS_PARENT_CHILD_SRC_DIR as _pcr on
      $projection.parent = _pcr.id and
      $projection.dir_entry =  _pcr.id
    association to one demo_hiera_dir                as _dir   on
      $projection.dir_entry = _dir.dir_entry 
    {
      _pcr,
      _dir,
      id,
      parent_id as parent,
      dir_entry
    }
```

The following CDS hierarchy uses the operand `dir_entry` from the left side of the `ON` condition from the CDS view in the filter condition after `DIRECTORY _dir FILTER BY`:

``` abap
define hierarchy DEMO_CDS_PARENT_CHILD_DIR  
  with parameters
    p_id1 : abap.char(2),
    p_id2 : abap.char(2),
    p_dir : abap.char(2)
      as parent child hierarchy(
    source
      DEMO_CDS_PARENT_CHILD_SRC_DIR 
      child to parent association _pcr
      directory _dir filter by dir_entry = :p_dir 
      start where
        id = :p_id1 or id = :p_id2 
      siblings order by
        parent
      multiple parents allowed
    )
    {
      id,
      parent,
      dir_entry
    }
```

When the class `CL_DEMO_HIERARCHY_PRNTCHLD_DIR` is executed, various parameters can be passed and the filter condition is demonstrated.

## Addition 5

`... START WHERE cds_cond`

### Description

The optional addition `START WHERE` specifies the start condition for creating the hierarchy. `START WHERE` can be followed by a logical expression `cds_cond` that selects rows from the source `cds_entity`. The same operators can be specified for [`cds_cond`](abencds_conditional_expression_v2.md) as in a [`WHERE`](abencds_where_clause_v2.md) clause of a CDS view entity and the same rules apply. The operands on the left side can be elements of the CDS entity specified after `SOURCE`. The operands on the right side can be literals, parameters from the [parameter list](abencds_f1_hiera_parameter_list.md) of the hierarchy, and [session variables](../../abap-glossary/abensession_variable_glosry.md). When specifying literals, parameters, and session variables, the same applies as when defining CDS views.

In semantic key scenarios, i.e. when the column that contains the parent node has a numeric data type, the `START WHERE` condition can be left out. In this case, an implicit `START WHERE` condition is generated, so that the root node set consists of all rows where the column that contains the [parent node](../../abap-glossary/abenparent_node_glosry.md) (as defined by the hierarchy association) is initial.

In UUID scenarios, the condition where to start is not implicitly set and must be specified explicitly. Otherwise, a syntax check error occurs.

The selected rows are inserted in the hierarchy as a [root node set](../../abap-glossary/abenroot_node_set_glosry.md). For each [root node](../../abap-glossary/abenroot_node_glosry.md) in the root node set, the [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md) are selected that meet the `ON` condition of the hierarchy association and, if possible, inserted in the hierarchy.

### Hints

- It is advisable to always specify the start condition explicitly, since this makes the definition clearer. Furthermore, the root node set defined by the implicit start condition is not always suitable and also cannot be modified using parameters.

- The start condition should select a feasible set of root nodes. If no rows in the result set of the source `cds_entity` meet the condition, the hierarchy is empty. If all rows meet the condition, the descendant nodes of every row are selected and inserted.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS hierarchy uses an interval boundary with `BETWEEN` as a start condition. The class `CL_DEMO_HIERARCHY_START_WHERE` accesses the CDS hierarchy and compares the result with the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](../../abap-programming-language/abap-database-access/abenselect_hierarchy_generator.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) used in a similar way. When executed, this class demonstrates how this addition works.

``` abap
define hierarchy DEMO_CDS_PARENT_CHILD_STRTWHR 
  with parameters
    p_from : abap.char(2),
    p_to   : abap.char(2)
  as parent child hierarchy(
    source
      DEMO_CDS_PARENT_CHILD_SOURCE
      child to parent association _relat
      start where
        id between :p_from and :p_to
      siblings order by
        id
      multiple parents allowed
      cycles breakup
    )
    {
      id,
      parent
    }
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS hierarchy does not have a `START WHERE` condition:

``` abap
define hierarchy DEMO_CDS_HIERA_NO_START_WHERE
  as parent child hierarchy(
    source DEMO_CDS_SIMPLE_TREE_SOURCE
    child to parent association _tree
    siblings order by
      id ascending
  )
{
  id,
  parent,
  name
}
```

It is implicitly handled like the following CDS hierarchy:

``` abap
define hierarchy DEMO_CDS_HIERA_START_WHERE
  as parent child hierarchy(
    source DEMO_CDS_SIMPLE_TREE_SOURCE
    child to parent association _tree
    start where
      parent is initial
    siblings order by
      id ascending
  )
{
  id,
  parent,
  name
}
```

An implicit `START WHERE` condition is added that depends on the parent column, which again depends on the hierarchy association. The class `CL_DEMO_CDS_HIERA_START_WHERE` shows that both CDS hierarchies select the same data.

## Addition 6

`... SIBLINGS ORDER BY field1 [ASCENDING|DESCENDING], ...`

### Description

The mandatory addition `SIBLINGS ORDER BY` sorts [sibling nodes](../../abap-glossary/abensibling_node_glosry.md) in the hierarchy. Fields `field1`, `field2`, ... of the source `cds_entity` can be specified in a comma-separated list after the addition `SIBLINGS ORDER BY` to specify the order of the sibling nodes.

The addition `ASCENDING` or `DESCENDING` can be specified for each field to specify an ascending or descending order (ascending is the default).

The fields specified after `SIBLINGS ORDER BY` cannot be of the [type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) `LCHR`, `LRAW`, `STRING`, `RAWSTRING`, or `GEOM_EWKB`.

### Hint

The addition `SIBLINGS ORDER BY` is mandatory in the case of CDS hierarchies, since this sort cannot be performed at a later time. For example, the result of a [hierarchy navigator](../../abap-glossary/abenhierarchy_navigator_glosry.md) in ABAP SQL may depend on how the hierarchy specified as a source is sorted. A [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) specified as a source can be sorted directly here, but this is no longer possible in the case of predefined CDS hierarchies.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS hierarchy sorts siblings in descending order by the field `id`. The class `CL_DEMO_HRRCHY_SIBLINGS_ORDER` accesses the CDS hierarchy and compares the result with the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](../../abap-programming-language/abap-database-access/abenselect_hierarchy_generator.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) used in a similar way. When executed, this class demonstrates how this addition works.

``` abap
define hierarchy DEMO_CDS_SIMPLE_TREE_SIBL_ORD
  with parameters
    p_id : abap.int4
  as parent child hierarchy(
    source
      DEMO_CDS_SIMPLE_TREE_SOURCE
      child to parent association _tree
      start where
        id = :p_id
      siblings order by
        id descending
    )
    {
      id,
      parent,
      name
    }
```

## Addition 7

`... DEPTH depth`

### Description

The optional addition `depth` limits the number of [hierarchy levels](../../abap-glossary/abenhierarchy_level_glosry.md) used to create [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md). `depth` can be a typed literal or a parameter from the [parameter list](abencds_f1_hiera_parameter_list.md) of the hierarchy that has an integer type.

The value in `depth` has the following meaning:

- For `depth` values greater then 0, the number of hierarchy edges are traversed that is specified in `depth`, starting from a [root node](../../abap-glossary/abenroot_node_glosry.md).

- If the value of `depth` is 0, only the [root nodes](../../abap-glossary/abenroot_node_glosry.md) are inserted in the hierarchy.

- For `depth` values less than 0, no [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md) are created.

The addition `DEPTH` can be used only if the addition `ORPHANS` is not specified or is specified as `ORPHANS IGNORE`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS hierarchy uses an input parameter `p_depth` to restrict the hierarchy levels. The class `CL_DEMO_HIERARCHY_DEPTH` accesses the CDS hierarchy and compares the result with the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](../../abap-programming-language/abap-database-access/abenselect_hierarchy_generator.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) used in a similar way. When executed, this class demonstrates how this addition works.

``` abap
define hierarchy DEMO_CDS_SIMPLE_TREE_DEPTH
  with parameters
    p_depth : abap.int4
  as parent child hierarchy(
    source
      DEMO_CDS_SIMPLE_TREE_SOURCE
      child to parent association _tree
      start where
        id = 1
      siblings order by
        id ascending
      depth :p_depth
    )
    {
      name,
      $node.hierarchy_level as hiera_level
    }
```

## Addition 8

`... NODETYPE node_type`

### Description

The optional addition `NODETYPE` identifies an element of the CDS hierarchy that can be used to determine the type of the hierarchy node. The values of this [element](abencds_f1_hiera_element.md) must be element names, which must also be contained in the [element list](abencds_f1_hiera_element_list.md) of the CDS hierarchy. Using the foreign key association or text association, which is assigned (via dedicated annotations) to the respective element, the attributes and the text for the respective hierarchy node can be determined. The element `node_type` specified with `NODETYPE` is saved in the metadata of the CDS hierarchy and can be read by consumers using the method `GET_NODETYPE_FIELD` of interface `IF_DD_CDS_READ_API_HIER_C2P`.

### Hint

A framework that analyzes `NODETYPE` is currently the [ABAP Analytical Engine](../../abap-glossary/abenabap_ae_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following CDS [tree hierarchy](../../abap-glossary/abentree_hierarchy_glosry.md), the element `name` is defined as a node type. If a hierarchy node in the element `name` has the value `Apple`, it should be a [leaf node](../../abap-glossary/abenleaf_node_glosry.md) without any [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md).

``` abap
define hierarchy DEMO_CDS_SIMPLE_TREE_NODETYPE
  as parent child hierarchy(
    source
      DEMO_CDS_SIMPLE_TREE_SOURCE
      child to parent association _tree
      start where
        id = 1
      siblings order by
        id ascending
      nodetype name
    )
    {
      id,
      parent,
      name
    }
```

The class `CL_DEMO_HRRCHY_TREE_NODETYPE` accesses the CDS hierarchy and when executed returns any hierarchy nodes that violate the rule. For that, the node type of the CDS hierarchy is evaluated by the following code sequence:

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TRY. 
    FINAL(nodetype) = 
      CAST if_dd_cds_read_api_hier_c2p( 
        cl_dd_sobject_factory=>create_entity( 
          'DEMO_CDS_SIMPLE_TREE_NODETYPE' ) 
            )->get_nodetype_field( )-fieldname. 
  CATCH cx_dd_sobject_get cx_dd_cds_read_api INTO FINAL(exc). 
    out->write( exc->get_text( ) ). 
ENDTRY. 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following CDS [tree hierarchy](../../abap-glossary/abentree_hierarchy_glosry.md), the element `NodeType` is defined as a node type. When selecting data from the CDS hierarchy for a view that can be used by the ABAP Analytical Engine, the element `NodeType` might return two different values. One is `CostCenter` and the other is `HierarchyNode`. When `NodeType` = `CostCenter`, then the elements `ControllingArea` and `CostCenter` must be filled, and with the foreign key association `_CostCenter`, the text and additional attributes can be derived. When `NodeType` = `HierarchyNode`, then the text association `_Text` is used to get the text for that node.

``` abap
define hierarchy DEMO_COSTCENTERHIER 
  with parameters 
    p_controllingArea : fis_kokrs, 
    P_hierarchy : fis_hryid_cctr 
  as parent child hierarchy( 
    source 
      DEMO_COSTCENTERHIERARCHYNODE 
    child to parent association 
      _parent 
    directory 
      _Hierarchy 
        filter by 
          ControllingArea        = $parameters.p_controllingArea 
         and CostCenterHierarchy = $parameters.P_hierarchy 
    start where 
      ParentNode is initial 
    siblings order by 
      HierarchyNodeSequence 
    nodetype 
      NodeType 
  ) 
{ 
      @ObjectModel.foreignKey.association: '_ControllingArea' 
      ControllingArea, 
      CostCenterHierarchy, 
      @ObjectModel.text.association: '_Text' 
      HierarchyNode, 
      ParentNode, 
      @ObjectModel.foreignKey.association: '_CostCenter' 
      CostCenter, 
      HierarchyNodeSequence, 
      NodeType, 
 
      _Text, 
      _CostCenter, 
      _Hierarchy, 
      _ControllingArea 
}
```

## Addition 9

`... LOAD BULK|INCREMENTAL|load_option`

### Description

The addition `LOAD` specifies the load policy for the generated hierarchy. It can be used for performance optimization.

The addition works as follows:

- `BULK`

  This is the default setting. The complete source table of the hierarchy is loaded.

- `INCREMENTAL`

  Only the rows of the source table that can be reached from the root nodes ([root node set](../../abap-glossary/abenroot_node_set_glosry.md)) are loaded.

- `load_option`

  For `load_option` a parameter from the [parameter list](abencds_f1_hiera_parameter_list.md) of the hierarchy can specified using the syntax [`$parameters.pname`](abencds_parameter_v2.md). The parameter must have the data type `CHAR` or `SSTRING` and a length of at least 11. Valid values of the parameter are *BULK* or *INCREMENTAL* in uppercase and have the same effect as the respective keywords. Invalid values lead to an exception from the database.

### Hints

- The performance optimization with `LOAD INCREMENTAL` depends on the data source. If the source table is very large and the hierarchy reads relatively few rows, there is a positive effect. If, by contrast, the source table has only few rows and they are all part of the hierarchy, `LOAD INCREMENTAL` might even take longer than `LOAD BULK`.

- Do not use `LOAD INCREMENTAL` with [global temporary tables](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_gtt.md) as data source, because it does not have any positive effect then (if anything, it slows down the performance).

- The valid values for `load_option` are the names of [enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md) with the [enumerated type](../../abap-glossary/abenenumerated_type_glosry.md) `LOAD_OPTION` from the class `SQL_HIERARCHY`. When accessing a CDS hierarchy with a parameter for `load_option` in ABAP SQL, the character representation of these enumerated constants can be passed.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS hierarchy uses the addition `LOAD` with a parameter `p_load`:

``` abap
define hierarchy DEMO_CDS_GUID_HIERA_BULK_INCR
  with parameters
    p_id   : abap.raw(16),
    p_load : abap.char(11)
  as parent child hierarchy(
    source DEMO_CDS_GUID_HIERA_SOURCE
    child to parent association _relat
    start where
      id = :p_id
    siblings order by
      id
    load $parameters.p_load
  )
{
  id,
  parent,
  field
}
```

The following `SELECT` statement is taken from the class `CL_DEMO_CDS_HIERA_BLK_INCRMNT`:

``` abap
DATA start_node TYPE demo_guid_hiera-id. 
 
SELECT FROM demo_cds_guid_hiera_bulk_incr( 
              p_id   = @start_node, 
              p_load = @( CONV #( 
                sql_hierarchy=>c_load_option-incremental ) ) ) 
       FIELDS id, 
              parent, 
              field 
       ORDER BY id 
       INTO TABLE @FINAL(inc_result).
```

By converting the enumerated constant `sql_hierarchy=>c_load_option-incremental` into a character string, the value *INCREMENTAL* is passed to the parameter `p_load`. The program works in the same way as described for the [executable example](../../abap-programming-language/abap-database-access/abenselect_hierarchy_abexa.md) for the hierarchy generator of ABAP SQL.

## Addition 10

`... MULTIPLE PARENTS {NOT ALLOWED}|{LEAVES ONLY}|ALLOWED`

### Description

The optional addition `MULTIPLE PARENTS` specifies whether the hierarchy can have [child nodes](../../abap-glossary/abenchild_node_glosry.md) with multiple [parent nodes](../../abap-glossary/abenparent_node_glosry.md):

- `NOT ALLOWED`

  This is the default setting (a child node can have exactly one parent node only).

- `LEAVES ONLY`

  Only [leaf nodes](../../abap-glossary/abenleaf_node_glosry.md) can have multiple parent nodes.

- `ALLOWED`

  All hierarchy nodes can have multiple parent nodes.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS hierarchy allows multiple parent nodes for leaf nodes. The class `CL_DEMO_HIERARCHY_MULTI_PRNTS` accesses the CDS hierarchy and compares the result with the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](../../abap-programming-language/abap-database-access/abenselect_hierarchy_generator.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) used in a similar way. When executed, this class demonstrates how this addition works.

``` abap
define hierarchy DEMO_CDS_PARENT_CHILD_MULTIPAR
  as parent child hierarchy(
    source
      DEMO_CDS_PARENT_CHILD_SOURCE
      child to parent association _relat
      start where
           id = 'A'
      siblings order by
        id
      multiple parents leaves
    )
    {
      id,
      parent,
      $node.hierarchy_level    as hiera_level
    }
```

## Addition 11

`... ORPHANS IGNORE|ERROR|ROOT`

### Description

The optional addition `ORPHANS` defines the way [orphan nodes](../../abap-glossary/abenorphan_node_glosry.md) are handled. The following categories of orphan nodes exist:

- Hierarchy nodes that could have parent nodes (as specified by the parent-child relationship) but the parent nodes are not in the hierarchy (known as true orphans).

- Hierarchy nodes that cannot be reached from the root node set using hierarchy edges.

- Hierarchy nodes that are part of a [node cycle](../../abap-glossary/abennode_cycle_glosry.md) and cannot be reached from the root node set using hierarchy nodes (known as island orphans).

The additions work as follows:

- `IGNORE`

  This is the default setting (any orphan nodes are not inserted in the hierarchy).

- `ERROR`

  Any orphan nodes detected raise an exception.

- `ROOT`

  Orphan nodes are inserted in the hierarchy as follows:

  - True orphans are included in the root node set as root nodes and flagged as orphan nodes in the [hierarchy attribute](abencds_hierarchy_attributes.md) `HIERARCHY_IS_ORPHAN`.

  - [Descendant nodes](../../abap-glossary/abendescendant_node_glosry.md) of true orphans are handled like descendant nodes of parent nodes from the root node set, but are also flagged as orphan nodes in the [hierarchy attribute](abencds_hierarchy_attributes.md) `HIERARCHY_IS_ORPHAN`.

  - For the hierarchy nodes of island orphans, a parent node in the root node set is generated for the child node where the cycle occurs. In the generated root node, all columns of the source `hierarchy_source` contain the null value. In the [hierarchy attributes](abencds_hierarchy_attributes.md), the additional root node is flagged as an orphan node and `PARENT_ID` also contains the null value.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS hierarchy transforms orphan nodes into root nodes. The class `CL_DEMO_HIERARCHY_ORPHANS` accesses the CDS hierarchy and compares the result with the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](../../abap-programming-language/abap-database-access/abenselect_hierarchy_generator.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) used in a similar way. When executed, this class demonstrates how this addition works.

``` abap
define hierarchy DEMO_CDS_PARENT_CHILD_ORPHANS
  as parent child hierarchy(
    source
      DEMO_CDS_PARENT_CHILD_SOURCE
      child to parent association _relat
      start where
        id = 'A'
      siblings order by
        id
      multiple parents allowed
      orphans root
      cycles breakup
    )
    {
      id,
      parent,
      $node.node_id               as hiera_node_id,
      $node.parent_id             as hiera_parent_id,
      $node.hierarchy_is_orphan   as hiera_is_orphan,
      $node.hierarchy_is_cycle    as hiera_is_cycle,
      $node.hierarchy_rank        as hiera_rank,
      $node.hierarchy_parent_rank as hiera_parent_rank,
      $node.hierarchy_level       as hiera_level
    }
```

## Addition 12

`... CYCLES ERROR|BREAKUP`

### Description

The addition `CYCLES` defines how [node cycles](../../abap-glossary/abennode_cycle_glosry.md) are defined. The additions work as follows:

- `ERROR`

  This is the default setting (an exception is raised when a node cycle is detected).

- `BREAKUP`

  The traversal of [descendant nodes](../../abap-glossary/abendescendant_node_glosry.md) is broken at the child node where the node cycle occurs and the [hierarchy attribute](../../abap-programming-language/abap-database-access/abenddddl_hierarchy.md) `HIERARCHY_IS_CYCLE` is set to the value 1.

If the addition `BREAKUP` is specified, `MULTIPLE PARENTS ALLOWED` must also be specified.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS hierarchy breaks node cycles using `CYCLES BREAKUP`. The class `CL_DEMO_HIERARCHY_CYCLES` accesses the CDS hierarchy and compares the result with the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](../../abap-programming-language/abap-database-access/abenselect_hierarchy_generator.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) used in a similar way. When executed, this class demonstrates how this addition works.

``` abap
define hierarchy DEMO_CDS_PARENT_CHILD_CYCLES
  as parent child hierarchy(
    source
      DEMO_CDS_PARENT_CHILD_SOURCE
      child to parent association _relat
      start where
           id = 'A'
        or id = 'X'
        or id = 'Y'
        or id = 'Z'
      siblings order by
        id
      multiple parents allowed
      cycles breakup
    )
    {
      id,
      parent,
      $node.hierarchy_is_cycle as hiera_is_cycle,
      $node.hierarchy_level    as hiera_level
    }
```

## Addition 13

`... GENERATE SPANTREE`

### Description

If the addition `GENERATE SPANTREE` is specified, only those child nodes without multiple parent nodes are inserted in the hierarchy, starting from every root node. If, due to its parent-child relationships, a child node were to have multiple parent nodes after its root node, exactly one of the potential paths from the root node to this child node is selected and the child node is created for this path only.

- If the paths have different lengths, the shortest is selected.

- If the paths all have the same length, the first path found is selected.

If the addition `GENERATE SPANTREE` is specified, the additions `MULTIPLE PARENTS`, `ORPHANS`, and `CYCLES` cannot be specified and other defaults apply in parts:

- `MULTIPLE PARENTS` is used implicitly with `ALLOWED`.

- `CYCLES` is used implicitly with `BREAKUP`.

### Hints

- If the parent-child relationships for the current data do not produce [tree hierarchies](../../abap-glossary/abentree_hierarchy_glosry.md), the addition `GENERATE SPANTREE` is ignored.

- Even if one path (from many paths) to a child node is selected, this does not mean that all others are rejected. In this case, only the edges leading to the child node are missing.

- The addition `GENERATE SPANTREE` can be used to detect whether at least one path leads from a root node to a child node without the result set needing to contain all paths.

- The addition `GENERATE SPANTREE` is used in an [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md) to access the hierarchy generator function [`HIERARCHY_SPANTREE`](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/2969da89b87f4abd85fd0b5f9f5bc395) there.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS hierarchy uses the addition `GENERATE SPANTREE`. The class `CL_DEMO_HIERARCHY_SPANTREE` accesses the CDS hierarchy and compares the result with the [hierarchy generator](../../abap-glossary/abenhierarchy_generator_glosry.md) [`HIERARCHY`](../../abap-programming-language/abap-database-access/abenselect_hierarchy_generator.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) used in a similar way. When executed, this class demonstrates how this addition works.

``` abap
define hierarchy DEMO_CDS_PARENT_CHILD_SPANTREE
  as parent child hierarchy(
    source
      DEMO_CDS_PARENT_CHILD_SOURCE
      child to parent association _relat
      start where
           id = 'A'
        or id = 'K'
        or id = 'X'
        or id = 'Y'
      siblings order by
        id
      generate spantree  
      ) 
    {
      id,
      parent
    }
```

## Addition 14

`... CACHE ON|OFF|FORCE`

### Description

The optional addition `CACHE` defines the caching policy for the generated hierarchy result. It can be used for performance optimization. The addition works as follows:

- `ON`

  The generated hierarchy is cached by the database if the system assesses the source to be reliably deterministic. This is the default behavior.

- `OFF`

  The generated hierarchy is not cached by the database.

- `FORCE`

  The generated hierarchy is cached by the database even if the source cannot be assessed to be reliably deterministic.
