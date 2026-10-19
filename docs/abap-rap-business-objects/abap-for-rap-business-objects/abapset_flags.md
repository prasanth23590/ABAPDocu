---
title: "SET FLAGS"
source_file: abapset_flags.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > Other RAP-Related ABAP Language Elements and Topics > Type Mapping for RAP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SET FLAGS

## Syntax

``` abap
SET FLAGS src FROM NAMES fields { MAPPING { TYPE p_type } 
                                        | { LIKE var } 
                                }.  
```

### Variant

[1. `... MAPPING TYPE p_type.`](abapset_flags.md#variant-1)

[2. `... MAPPING LIKE var.`](abapset_flags.md#variant-2)

## Overview

### Description

Used for the conversion of fields that have the [technical type](../../abap-glossary/abentechnical_type_prpt_glosry.md) [`x`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_byte.md) and field name lists in the context of RAP. The statement deals with [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) that include the components [`%control`](abapderived_types_comp.md) and [`%element`](abapderived_types_comp.md). The components of `%control` and `%element` have the technical type `x`.

The ABAP statement is targeted at applications that include, on the one hand, [RAP BOs](../../abap-glossary/abenrap_bo_glosry.md) that use BDEF derived types and, on the other hand, implementations of the [RAP BO behavior](../../abap-glossary/abenrap_bo_behavior_glosry.md) that use other data types. Mapping of field names is required if types are involved that have different field names than those in the underlying [CDS entities](../../abap-glossary/abencds_entity_glosry.md) of the RAP BO.

`src` represents a variable typed with a BDEF derived type that contains `%control` or `%element`. `fields` represents a [general expression](../../abap-glossary/abengeneral_expr_position_glosry.md). A variable in the position of `fields` must be a table containing one or more field names. It is of type `ABP_FIELD_NAME_TAB`, the line type is `ABP_FIELD_NAME`.

As a result of the ABAP statement, the field names contained in the table get identified as component names in the `%control` or `%element` structure and their value is set to `01`. If field names do not exist in `fields`, the value in the structures is set to `00`. The ABAP statement [`SET NAMES`](abapset_names.md) does the conversion the other way round.

The following short dumps result from an operation that cannot be executed at runtime using the `SET FLAGS` statements:

- `TCHK_TYPE_LOAD`: Inappropriate type for field names.

- `BEHAVIOR_FLAGS_NAMES_ERROR`: Inappropriate type on the BDEF derived type side or a missing mapping, which is true for the variants of the statement.

## Variant 1

`... MAPPING TYPE p_type.`

### Description

Used in case type mapping is required for a structured [DDIC type](../../abap-glossary/abenddic_type_glosry.md), for example, a legacy type. `fields` must contain the field names of the legacy type.

As a prerequisite, the BDEF contains a mapping specification for the mapped type. See more information in the RAP BDL topic [`mapping for`](../rap-behavior-definitions/abenbdl_type_mapping.md).

## Variant 2

`... MAPPING LIKE var.`

### Description

Used in case type mapping is required for a structured [DDIC type](../../abap-glossary/abenddic_type_glosry.md), for example, a legacy type. This variant is relevant if the type is not available and is a variable of the required type instead. `fields` must contain the field names of the legacy type.

As a prerequisite, the BDEF contains a mapping specification for the mapped type. See more information in the RAP BDL topic [`mapping for`](../rap-behavior-definitions/abenbdl_type_mapping.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_SET_NAMES` shows the syntax of the `SET NAMES` variants.

``` abap
DATA: fields  TYPE abp_field_name_tab, 
      fields2 TYPE abp_field_name_tab, 
      src     TYPE STRUCTURE FOR CREATE demo_managed_root_map, 
      var     TYPE demo_struc. 
 
fields = VALUE #( ( CONV #( 'KEY_FIELD' ) ) 
                  ( CONV #( 'FIELD1' ) ) 
                  ( CONV #( 'FIELD2' ) ) 
                  ( CONV #( 'FIELD3' ) ) 
                  ( CONV #( 'FIELD4' ) ) 
                ). 
 
fields2 = VALUE #( ( CONV #( 'B_KEY_FIELD' ) ) 
                   ( CONV #( 'B_FIELD1' ) ) 
                   ( CONV #( 'B_FIELD2' ) ) 
                   ( CONV #( 'B_FIELD3' ) ) 
                   ( CONV #( 'B_FIELD4' ) ) 
                 ). 
 
"First variant. 
SET FLAGS src FROM NAMES fields. 
 
"Second variant. 
SET FLAGS src FROM NAMES fields2 MAPPING TYPE demo_struc. 
 
"Third variant. 
SET FLAGS src FROM NAMES fields2 MAPPING LIKE var.
```

### Executable Example

The example [ABAP EML - Variants of `SET FLAGS`](abeneml_set_flags_abexa.md) demonstrates the three different variants with a simple managed RAP BO.
