---
title: "CORRESPONDING, Type Mapping for ABAP EML"
source_file: abapeml_corresponding.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > Other RAP-Related ABAP Language Elements and Topics > Type Mapping for RAP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CORRESPONDING, Type Mapping for ABAP EML

## Syntax

``` abap
    { [ non_der_type = | ... ] CORRESPONDING {dtype|#}( [ ... ] in_der_type MAPPING FROM ENTITY ) } 
  | { [ out_der_type = | ... ] CORRESPONDING {dtype|#}( [ ... ] non_der_type MAPPING TO ENTITY ) } 
  | { [ non_der_type = | ... ] CORRESPONDING {dtype|#}( [ ... ] in_der_type [ ... ] USING CONTROL [ ... ] ) } 
  | { [ non_der_type = | ... ] CORRESPONDING {dtype|#}( [ ... ] in_der_type MAPPING FROM ENTITY USING CONTROL ) } 
  | { [ in_der_type = | ... ] CORRESPONDING {dtype|#}( [ ... ] non_der_type [ ... ] CHANGING CONTROL [ ... ] ) } ...  
```

### Variant

[1. `[ non_der_type = | ... ] CORRESPONDING {dtype|#}( [ ... ] in_der_type MAPPING FROM ENTITY ) ...`](abapeml_corresponding.md#variant-1)

[2. `[ out_der_type = | ... ] CORRESPONDING {dtype|#}( [ ... ] non_der_type MAPPING TO ENTITY ) ...`](abapeml_corresponding.md#variant-2)

[3. `[ non_der_type = | ... ] CORRESPONDING {dtype|#}( [ ... ] in_der_type [ ... ] USING CONTROL [ ... ] ) ...`](abapeml_corresponding.md#variant-3)

[4. `[ non_der_type = | ... ] CORRESPONDING {dtype|#}( [ ... ] in_der_type MAPPING FROM ENTITY USING CONTROL ) ...`](abapeml_corresponding.md#variant-4)

[5. `[ in_der_type = | ... ] CORRESPONDING {dtype|#}( [ ... ] non_der_type [ ... ] CHANGING CONTROL [ ... ] ) ...`](abapeml_corresponding.md#variant-5)

## Overview

### Description

The variants of the [`CORRESPONDING`](../../abap-programming-language/abap-processing-internal-data/abenconstructor_expr_corresponding.md) operator are used to create structures or internal tables with type mapping in ABAP within the context of RAP. The type mapping functionality is aimed at applications that have, on the one hand, [RAP BOs](../../abap-glossary/abenrap_bo_glosry.md) based on CDS entities and, on the other hand, have further types that are typically legacy types and implement the behavior of the RAP BOs or parts of it. This is particularly relevant for the implementation type [`unmanaged`](../rap-behavior-definitions/abenbdl_impl_type.md) that integrates existing functionality into RAP. However, it can also be relevant for [`managed`](../rap-behavior-definitions/abenbdl_impl_type.md), for example, when using code for determinations or validations that already exist but are based on legacy, non-RAP types, i.e., types that are not derived from the BDEF.

RAP requires [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) for the communication of [RAP BO providers](../../abap-glossary/abenrap_bo_provider_glosry.md) and [RAP BO consumers](../../abap-glossary/abenrap_bo_consumer_glosry.md). When including non-BDEF-derived types, the variants of the `CORRESPONDING` operator are responsible for matching them to the [input](../../abap-glossary/abenrap_input_der_type_glosry.md) (for example, `TYPE TABLE FOR UPDATE`) and [output](../../abap-glossary/abenrap_output_der_type_glosry.md) (for example, `TYPE TABLE FOR READ RESULT`) of BDEF derived types. A type mapping is needed if the types include field names that differ from the RAP BO or if the control information ([`%control`](abapderived_types_comp.md)) is available in non-BDEF-derived types. By using the variants of the `CORRESPONDING` operator, maintenance is simplified and errors are reduced because many individual specifications with `CORRESPONDING` can be avoided. Some of the variants require a mapping to be specified in the BDEF. For more information, see the RAP BDL documentation on [`Mapping`](../rap-behavior-definitions/abenbdl_type_mapping.md).

Notes on the syntax:

- `non_der_type`: Type that is not derived from the BDEF.

- `dtype`/`#`: Find more information [here](../../abap-programming-language/abap-processing-internal-data/abenconstructor_expr_corresponding.md).

- `out_der_type`: [RAP output derived type](../../abap-glossary/abenrap_output_der_type_glosry.md), for example, a data object typed with [`TYPE TABLE FOR READ RESULT`](abaptype_table_for.md) or [`TYPE STRUCTURE FOR READ RESULT`](abaptype_structure_for.md).

- `in_der_type`: [RAP input derived type](../../abap-glossary/abenrap_input_der_type_glosry.md), for example, a data object typed with `TYPE TABLE FOR UPDATE` or `TYPE STRUCTURE FOR UPDATE`.

- The placeholders (`...`) within the pair of parentheses that follows `CORRESPONDING` and `dtype`/`#` represent possible additions that are described [here](../../abap-programming-language/abap-processing-internal-data/abenconstructor_expr_corresponding.md).

## Variant 1

`[ non_der_type = | ... ] CORRESPONDING {dtype|#}( [ ... ] in_der_type MAPPING FROM ENTITY ) ...`

### Description

Used for the mapping of a [RAP input derived type](../../abap-glossary/abenrap_input_der_type_glosry.md) (`in_der_type`) to a non-BDEF derived type (`non_der_type`). As a prerequisite, the [`mapping`](../rap-behavior-definitions/abenbdl_type_mapping.md) for the non-BDEF derived type must be specified in the BDEF.

Possible additions in dedicated positions (`[ ... ]`) within the pair of parentheses:

- Internal table types: None. Use only with `MAPPING FROM ENTITY`.

- Structured types: `BASE`, `APPENDING`

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following code demonstrates the assignment of an input derived type to a non-BDEF derived type using the addition `MAPPING FROM ENTITY`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: ent_in_tab   TYPE TABLE FOR UPDATE demo_managed_root_map, 
      ty2_tab      TYPE STANDARD TABLE OF demo_struc2. 
 
ent_in_tab = VALUE #( ( key_field = 1 field1 = 'aaa' field2 = 'bbb' 
                        field3 = 1 field4 = 2 ) ). 
 
ty2_tab = CORRESPONDING #( ent_in_tab MAPPING FROM ENTITY ). 
 
out->write( ent_in_tab ). 
out->write( ty2_tab ). 
 
out->display( ).
```

## Variant 2

`[ out_der_type = | ... ] CORRESPONDING {dtype|#}( [ ... ] non_der_type MAPPING TO ENTITY ) ...`

### Description

Used for the mapping of a non-BDEF derived type (`non_der_type`) to a [RAP output derived type](../../abap-glossary/abenrap_output_der_type_glosry.md) (`out_der_type`). As a prerequisite, the [`mapping`](../rap-behavior-definitions/abenbdl_type_mapping.md) for the non-BDEF derived type must be specified in the BDEF.

Possible additions in dedicated positions (`[ ... ]`) within the pair of parentheses:

- Internal table types: None. Use only with `MAPPING FROM ENTITY`.

- Structured types: `BASE`, `APPENDING`

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following code demonstrates the assignment of a non-BDEF derived type to an output derived type using the addition `MAPPING TO ENTITY`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: ent_out_tab  TYPE TABLE FOR READ RESULT demo_managed_root_map, 
      ty3_tab      TYPE STANDARD TABLE OF demo_struc3. 
 
ty3_tab = VALUE #( ( z_key_field = 2 z_field1 = 'ccc' 
                     z_field2 = 'ddd' z_field3 = 3 z_field4 = 4 ) ). 
 
ent_out_tab = CORRESPONDING #( ty3_tab MAPPING TO ENTITY ). 
 
out->write( ty3_tab ). 
out->write( ent_out_tab ). 
 
out->display( ).
```

## Variant 3

`[ non_der_type = | ... ] CORRESPONDING {dtype|#}( [ ... ] in_der_type [ ... ] USING CONTROL [ ... ] ) ...`

### Description

Type mapping variant that respects the `%control` component of BDEF derived types. `in_der_type` must be a BDEF derived type that includes the `%control` component. Only those fields for which the corresponding `%control` field have been marked as enabled are respected by the mapping, i. e. if a specific `%control` field is marked as disabled (e. g. the field is initial) in `in_der_type`, the mapping is not applied to it on the non-BDEF-derived type `non_der_type`. There is no [`mapping`](../rap-behavior-definitions/abenbdl_type_mapping.md) required for the non-BDEF derived type in the BDEF.

Possible additions in dedicated positions (`[ ... ]`) within the pair of parentheses:

- Internal table types: `BASE`, `APPENDING`, `EXACT`, `MAPPING`, `DISCARDING DUPLICATES`, `EXCEPT`

- Structured types: `BASE`, `APPENDING`, `EXACT`, `MAPPING`, `EXCEPT`

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following code demonstrates the assignment of an input derived type to a non-BDEF derived type using the addition `USING CONTROL`. The `%control` component of a particular field is not selected, hence, this field is not assigned.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: ent_in_tab   TYPE TABLE FOR UPDATE demo_managed_root_map, 
      ty1_tab      TYPE STANDARD TABLE OF demo_struc1. 
 
ent_in_tab = VALUE #( 
  ( key_field = 4 field1 = 'ggg' field2 = 'hhh' field3 = 7 field4 = 8 
    %control = VALUE #( key_field = if_abap_behv=>mk-on 
                        field1    = if_abap_behv=>mk-off 
                        field2    = if_abap_behv=>mk-on 
                        field3    = if_abap_behv=>mk-on 
                        field4    = if_abap_behv=>mk-on ) ) ). 
 
ty1_tab = CORRESPONDING #( ent_in_tab USING CONTROL ). 
 
out->write( ent_in_tab ). 
out->write( ty1_tab ). 
 
out->display( ).
```

## Variant 4

`[ non_der_type = | ... ] CORRESPONDING {dtype|#}( [ ... ] in_der_type MAPPING FROM ENTITY USING CONTROL ) ...`

### Description

Type mapping variant that takes the `%control` component of BDEF derived types into consideration. `in_der_type` must be a BDEF derived type that includes the `%control` component. Only those fields for which the corresponding `%control` field have been marked as enabled are considered for the mapping, i. e. if a specific `%control` field is marked as disabled (e. g. the field is initial) in `in_der_type`, the mapping is not applied to it on the non-BDEF-derived type `non_der_type`. The variant is used if the components of the non-BDEF derived type have different field names than the ones from the BDEF-derived type. Thus, a [`mapping`](../rap-behavior-definitions/abenbdl_type_mapping.md) is required for the non-BDEF derived type in the BDEF with the notation `control`.

Possible additions in dedicated positions (`[ ... ]`) within the pair of parentheses:

- Internal table types: None. Use only with `MAPPING FROM ENTITY`.

- Structured types: `BASE`, `APPENDING`

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following code demonstrates the assignment of an input derived type to a non-BDEF derived type using the addition `MAPPING FROM ENTITY USING CONTROL`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: ent_in_tab   TYPE TABLE FOR UPDATE demo_managed_root_map, 
      ty2_tab      TYPE STANDARD TABLE OF demo_struc2. 
 
ent_in_tab = VALUE #( 
( key_field = 5 field1 = 'iii' field2 = 'jjj' field3 = 9 field4 = 10 
  %control = VALUE #( key_field = if_abap_behv=>mk-on 
                      field1    = if_abap_behv=>mk-on 
                      field2    = if_abap_behv=>mk-off 
                      field3    = if_abap_behv=>mk-on 
                      field4    = if_abap_behv=>mk-on ) ) ). 
 
ty2_tab = CORRESPONDING #( ent_in_tab MAPPING FROM 
                                      ENTITY USING CONTROL ). 
 
out->write( ent_in_tab ). 
out->write( ty2_tab ). 
 
out->display( ).
```

## Variant 5

`[ in_der_type = | ... ] CORRESPONDING {dtype|#}( [ ... ] non_der_type [ ... ] CHANGING CONTROL [ ... ] ) ...`

### Description

Type mapping variant that fills the `%control` structure of a BDEF-derived type based on a non-BDEF-derived type that does not include control information, i. e. if a field of `non_der_type` is left initial, the statement leaves the corresponding `%control` component of the field initial (`00`). Vice versa, if a field of `non_der_type` is provided with a value, the statement sets the corresponding `%control` component of `in_der_type` as enabled (`01`).

There is no [`mapping`](../rap-behavior-definitions/abenbdl_type_mapping.md) required for non-BDEF derived types in the BDEF. If non-BDEF derived types have different field names and a mapping from non-BDEF-derived types to input BDEF-derived types is required, a [`mapping`](../rap-behavior-definitions/abenbdl_type_mapping.md) in the BDEF must be defined (with the notation `control`) and a second `CORRESPONDING` statement with the addition `MAPPING TO ENTITY` must precede the statement with `CHANGING CONTROL`. In doing so, the first `CORRESPONDING` statement with the addition `MAPPING TO ENTITY` is responsible for mapping the field names and the second statement with `CHANGING CONTROL` is responsible filling the `%control` structure. This mapping variant is only possible for input derived types since all of them include `%control` structures.

Possible additions in dedicated positions (`[ ... ]`) within the pair of parentheses:

- Internal table types: `BASE`, `APPENDING`, `EXACT`, `MAPPING`, `DISCARDING DUPLICATES`, `EXCEPT`

- Structured types: `BASE`, `APPENDING`, `EXACT`, `MAPPING`, `EXCEPT`

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following code demonstrates the assignment of a non-BDEF derived type to an input derived type using the addition `CHANGING CONTROL`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: ent_in_tab   TYPE TABLE FOR UPDATE demo_managed_root_map, 
      ty1_tab      TYPE STANDARD TABLE OF demo_struc1. 
 
ty1_tab = VALUE #( ( key_field = 6 
                     "field1 not specified 
                     field2 = 'kkk' 
                     field3 = 11 
                     field4 = 12 ) ). 
 
ent_in_tab = CORRESPONDING #( ty1_tab CHANGING CONTROL ). 
 
out->write( ty1_tab ). 
out->write( ent_in_tab ). 
 
out->display( ).
```

### Executable Example

The example [ABAP EML - `CORRESPONDING`, Type Mapping](abeneml_type_mapping_abexa.md) demonstrates the different variants with a simple managed RAP BO.
