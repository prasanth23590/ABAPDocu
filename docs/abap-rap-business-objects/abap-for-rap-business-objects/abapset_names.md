---
title: "SET NAMES"
source_file: abapset_names.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > Other RAP-Related ABAP Language Elements and Topics > Type Mapping for RAP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SET NAMES

## Syntax

``` abap
SET NAMES fields FROM FLAGS src { MAPPING { TYPE p_type } 
                                        | { LIKE var } 
                                }.  
```

### Variant

[1. `... MAPPING TYPE p_type.`](abapset_names.md#variant-1)

[2. `... MAPPING LIKE var.`](abapset_names.md#variant-2)

## Overview

### Description

Used for the conversion of fields that have the [technical type](../../abap-glossary/abentechnical_type_prpt_glosry.md) [`x`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md) and field name lists in the context of RAP. The statement deals with [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) that include the components [`%control`](abapderived_types_comp.md) and [`%element`](abapderived_types_comp.md). The components of `%control` and `%element` have the technical type `x`.

The ABAP statement is targeted at applications that include, on the one hand, [RAP BOs](../../abap-glossary/abenrap_bo_glosry.md) that use BDEF derived types and, on the other hand, implementations of the [RAP BO behavior](../../abap-glossary/abenrap_bo_behavior_glosry.md) that use other data types. Mapping of field names is required if types are involved that have different field names than those in the underlying [CDS entities](../../abap-glossary/abencds_entity_glosry.md) of the RAP BO.

`fields` represents a [general expression](../../abap-glossary/abengeneral_expr_position_glosry.md). A variable in the position of `fields` must be a table containing one or more field names. It is of type `ABP_FIELD_NAME_TAB`, the line type is `ABP_FIELD_NAME`. `src` represents a [general expression](../../abap-glossary/abengeneral_expr_position_glosry.md). A variable in the position of `src` must be typed with a BDEF derived type that contains `%control` or `%element`.

As a result of the ABAP statement, the field name list `fields` contains those fields that have non-initial values in the `%control` or `%element` structure of `src`. The ABAP statement [`SET FLAGS`](abapset_flags.md) does the conversion the other way round.

The following short dumps result from an operation that cannot be executed at runtime using the `SET NAMES` statements:

- `TCHK_TYPE_LOAD`: Inappropriate type for field names.

- `BEHAVIOR_FLAGS_NAMES_ERROR`: Inappropriate type on the BDEF derived type side or a missing mapping, which is true for the variants of the statement.

## Variant 1

`... MAPPING TYPE p_type.`

### Description

Used in case type mapping is required for a structured [DDIC type](../../abap-glossary/abenddic_type_glosry.md), for example, a legacy type. As a prerequisite, the BDEF contains a mapping specification for the mapped type. See more information in the RAP BDL topic [`mapping for`](../rap-behavior-definitions/abenbdl_type_mapping.md).

## Variant 2

`... MAPPING LIKE var.`

### Description

Used in case type mapping is required for a structured [DDIC type](../../abap-glossary/abenddic_type_glosry.md), for example, a legacy type. This variant is relevant if the type is not available and is a variable of the required type instead. As a prerequisite, the BDEF contains a mapping specification for the mapped type. See more information in the RAP BDL topic [`mapping for`](../rap-behavior-definitions/abenbdl_type_mapping.md).

### Hint

`%element` contains the names of all associations of the RAP BO. However, type mapping cannot be defined for associations. Hence, if the ABAP statement is used with `mapping` and a BDEF derived typed with `%element`, information from `%element` that relates to associations is lost. In this case, only the mapped component name is available in `fields`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_SET_NAMES` shows the syntax of the `SET NAMES` variants.

``` abap
DATA: fields  TYPE abp_field_name_tab, 
      fields2 TYPE abp_field_name_tab, 
      fields3 TYPE abp_field_name_tab, 
      src     TYPE STRUCTURE FOR UPDATE demo_managed_root_map, 
      var     TYPE demo_struc. 
 
src-%control = VALUE #( key_field = if_abap_behv=>mk-on 
                        field1    = if_abap_behv=>mk-off 
                        field2    = if_abap_behv=>mk-on 
                        field3    = if_abap_behv=>mk-on 
                        field4    = if_abap_behv=>mk-on 
                      ). 
 
"First variant. 
SET NAMES fields FROM FLAGS src. 
 
"Second variant. 
SET NAMES fields2 FROM FLAGS src MAPPING TYPE demo_struc. 
 
"Third variant. 
SET NAMES fields3 FROM FLAGS src MAPPING LIKE var.
```

### Executable Example

The example [ABAP EML - Variants of `SET NAMES`](abeneml_set_names_abexa.md) demonstrates the three different variants with a simple managed RAP BO.
