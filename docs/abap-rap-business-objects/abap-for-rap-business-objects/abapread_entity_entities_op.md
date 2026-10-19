---
title: "READ ENTITY, ENTITIES, operations"
source_file: abapread_entity_entities_op.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > READ ENTITY, ENTITIES"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# READ ENTITY, ENTITIES, operations

## Syntax

``` abap
... [field_spec RESULT result_tab] 
    [BY \_assoc field_spec { {RESULT result_tab} | {LINK link_tab} } 
                           | {RESULT result_tab LINK link_tab} ] 
    [EXECUTE function field_spec [REQUEST request] RESULT result_tab ] ...  
```

[`field_spec`](abapread_entity_entities_fields.md) · [`RESULT result_tab`](abapeml_result.md) · [`field_spec`](abapread_entity_entities_fields.md) · [`RESULT result_tab`](abapeml_result.md) · [`RESULT result_tab`](abapeml_result.md) · [`field_spec`](abapread_entity_entities_fields.md) · [`RESULT result_tab`](abapeml_result.md)

### Variant

[1. `... field_spec RESULT result_tab ...`](abapread_entity_entities_op.md#variant-1)

[2. `... BY \_assoc field_spec RESULT result_tab LINK link ...`](abapread_entity_entities_op.md#variant-2)

[3. `... EXECUTE function field_spec [REQUEST request] RESULT result_tab ...`](abapread_entity_entities_op.md#variant-3)

## Overview

### Description

The ABAP EML `READ` statement includes three kinds of operations:

- [Read operations](../../abap-glossary/abenrap_read_operation_glosry.md): Read entities directly via key fields.

- [Read-by-association operations](../../abap-glossary/abenrap_rba_operation_glosry.md): Read [child entities](../../abap-glossary/abenchild_entity_glosry.md) via key fields of the [parent entity](../../abap-glossary/abenparent_entity_glosry.md). It is also possible to read parent entities via the child entities, however, only from within the implementation class.

- Execute functions: Carry out a user-defined read operation, for example, if parameters are required.

All read operations require an internal table ([`field_spec`](abapread_entity_entities_fields.md)) as input parameter to specify, for example, whether all fields or only a specific set of fields should be read from RAP BO entities. Read operations always have a result, which is stored in an internal table ([`result_tab`](abapeml_result.md)). Note that read-by-association operations must either have a read result or return the associated keys. They can also return both.

### Hints

- After the keyword `BY` for read-by-association operations, it is required to insert the backslash (`\`) before the associations are displayed via the code completion.

## More Information

See further information and rules for using ABAP EML statements in implementations of the [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) and [consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) in the Development guide for the ABAP RESTful Application Programming Model, section [RAP Business Object Contract](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

## Variant 1

`... field_spec RESULT result_tab ...`

### Description

Used to read directly from a RAP BO entity, either a [root](../../abap-glossary/abenroot_entity_glosry.md) or [child entity](../../abap-glossary/abenchild_entity_glosry.md), with input parameters specified in [`field_spec`](abapread_entity_entities_fields.md).

The keyword `RESULT` is the only additional mandatory keyword. The internal table `result_tab` is used to store the result of the read operation. It must be typed with a [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) that depends on the read operation variant. See more details in the documentation for [`RESULT result_tab`](abapeml_result.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_READ_OPRTNS` demonstrates a `READ` operation directly from a RAP BO entity.

``` abap
READ ENTITY demo_spfli_flights 
 FROM VALUE #( 
    ( %key-Carrid = 'AZ' %key-Connid = 790 
      %control = VALUE #( Airpfrom  = if_abap_behv=>mk-on 
                          Airpto    = if_abap_behv=>mk-on 
                          Cityfrom  = if_abap_behv=>mk-on 
                          Cityto    = if_abap_behv=>mk-on 
                          Countryfr = if_abap_behv=>mk-on 
                          Countryto = if_abap_behv=>mk-on 
                          Deptime   = if_abap_behv=>mk-on 
                          Arrtime   = if_abap_behv=>mk-on 
                          Distance  = if_abap_behv=>mk-on 
                          Fltime    = if_abap_behv=>mk-on 
                                        ) ) ) 
  RESULT FINAL(read_from) 
  FAILED FINAL(read_failed).
```

## Variant 2

`... BY \_assoc field_spec RESULT result_tab LINK link_tab ...`

### Addition

[`... LINK link_tab`](abapread_entity_entities_op.md#addition-1)

### Description

Used for read-by-association operations, that is, to read [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) of associated entities via the keys of the [parent entity](../../abap-glossary/abenparent_entity_glosry.md). This includes associated [child entities](../../abap-glossary/abenchild_entity_glosry.md) that are part of the composition tree but also cross-BO entities that are not part of it. It is also possible to read parent entities via the child entities, however, only from within the implementation class. `_assoc` is the name of the association as specified in the underlying CDS view. As a prerequisite, child entities to be read from must be defined in the same BDEF. For read access to a cross-BO entity, it is a prerequisite that behavior is defined for it in another BDEF.

[`field _spec`](abapread_entity_entities_fields.md) is an internal table specifying the input parameters for the read-by-association operation. The internal table [`RESULT result_tab`](abapeml_result.md) is used to store the result of the read operation. It must be typed with a [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) that depends on the read operation variant. The component [`%target`](abapderived_types_comp.md) must be filled in the in the internal table `field_spec`.

## Addition

`... LINK link_tab`

### Description

The statement provides an additional target variable (`link_tab`) after the `LINK` keyword. `link_tab` is an internal table containing keys of the source (i. e. the parent, or the child respectively if instances are read from the parent via the child) and keys of the target (associated entity) as nested structures. `link_tab` must be typed with the BDEF derived type [`TYPE TABLE FOR READ LINK`](abaptype_table_for.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_READ_OPRTNS` demonstrates a read-by-association operation.

``` abap
READ ENTITY demo_spfli_flights 
 BY \_Flights 
 ALL FIELDS WITH VALUE #( ( %key-Carrid = 'AA' 
                            %key-Connid = 26 ) ) 
 RESULT FINAL(rba_all_fields_with) 
 FAILED FINAL(read4_failed).
```

## Variant 3

`... EXECUTE function field_spec [REQUEST request] RESULT result_tab ...`

### Addition

[`... REQUEST request`](abapread_entity_entities_op.md#addition-3)

### Description

The keyword `EXECUTE` triggers the calling of a [RAP function](../../abap-glossary/abenrap_function_glosry.md) for a read-only operation. In both managed and unmanaged scenarios, the function must be user-implemented in a [behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md).

[`field _spec`](abapread_entity_entities_fields.md) is an internal table specifying the input parameters for the operation. The internal table `result_tab` is used to store the result of the read operation. It must be typed with a BDEF derived type that depends on the read operation variant. See more details in the documentation for [`RESULT result_tab`](abapeml_result.md).

### Hint

The consumption of [RAP key functions](../../abap-glossary/abenrap_key_function_glosry.md) using ABAP EML `READ` statements works like consuming static [RAP functions](../../abap-glossary/abenrap_function_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_READ_OP_FUNC` demonstrates a read operation executing a function.

``` abap
READ ENTITIES OF demo_spfli_flights 
 ENTITY demo_spfli_flights 
  EXECUTE FunctionResultEntity 
  FROM VALUE #( ( %tky-Carrid =  'AA' 
                  %tky-Connid = 17 ) ) 
 RESULT FINAL(result) 
 FAILED FINAL(failed) 
 REPORTED FINAL(reported).
```

## Addition

`... REQUEST request`

### Description

Used to specify whether the result should be returned completely or only parts of it (for example, only the keys) for the purpose of improving performance. `request` must be typed with the required [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md): `TYPE STRUCTURE FOR FUNCTION REQUEST`. The components of the structure are all key and data fields of the RAP BO entity. They are of type `ABP_BEHV_FLAG` and can be flagged whether to include the respective fields or not.

It is optional and can only be used for functions specified in the BDEF with the addition [`result selective`](../rap-behavior-definitions/abenbdl_action_output_para.md). In the context of [RAP key functions](../../abap-glossary/abenrap_key_function_glosry.md), the `REQUEST` addition can be specified even if there is no explicit specification in the BDEF regarding the result. In this case, the RAP key function is implicitly specified with `result selective [1] $self`.

### Executable Example

- The example [`READ`: Operations and Field Selection](abeneml_read_op_fields_abexa.md) demonstrates several different variants of field selection with a simple managed RAP BO.

- For more examples on `READ` operations in general, see [Examples for ABAP EML `READ`](abapeml_read_examples_abexas.md).
