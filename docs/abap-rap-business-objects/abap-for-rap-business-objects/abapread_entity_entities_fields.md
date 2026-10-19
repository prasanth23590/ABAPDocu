---
title: "READ ENTITY, ENTITIES, field_spec"
source_file: abapread_entity_entities_fields.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > READ ENTITY, ENTITIES > READ ENTITY, ENTITIES, operations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# READ ENTITY, ENTITIES, field_spec

## Syntax

``` abap
...  { FROM fields_tab } 
   | { FIELDS ( comp1 comp2 ... ) WITH fields_tab } 
   | { ALL FIELDS WITH fields_tab } ...  
```

[`fields_tab`](abapeml_fields_tab.md) · [`fields_tab`](abapeml_fields_tab.md) · [`fields_tab`](abapeml_fields_tab.md)

### Variant

[1. `... FROM fields_tab ...`](abapread_entity_entities_fields.md#variant-1)

[2. `... FIELDS ( comp1 comp2 ... ) WITH fields_tab ...`](abapread_entity_entities_fields.md#variant-2)

[3. `... ALL FIELDS WITH fields_tab ...`](abapread_entity_entities_fields.md#variant-3)

## Overview

### Description

The field specification expressions are used to specify input parameters on whose basis read operations can be performed for on [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md). All variants can be used for direct [read](../../abap-glossary/abenrap_read_operation_glosry.md) and [read-by-association operations](../../abap-glossary/abenrap_rba_operation_glosry.md). The variant `FROM` is the only option for read operations executing functions (using the keyword `EXECUTE`) in most cases.

The parameters that are taken into account for read operations must be specified in an internal table ([`fields_tab`](abapeml_fields_tab.md)). It is essential that the internal table is typed with the required [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md). Depending on the operation and the variant, the parameters of the internal table comprise [special components](abapderived_types_comp.md).

The following table provides an overview on the operations, which field specification expressions are possible for the operations, and which type and components of the required internal table are relevant:

<table>
<thead>
<tr class="header">
<th><strong>Operation</strong></th>
<th><strong>Field Specification Expression</strong></th>
<th><strong>Type of Internal Table<code class="ph codeph">fields_tab</code></strong></th>
<th><strong>Components of Internal Table</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Direct read operation (for example, <code class="ph codeph">READ ENTITY bdef FROM</code>)</td>
<td><p><code class="ph codeph">FROM</code></p>
<p><code class="ph codeph">FIELDS (...) WITH</code></p>
<p><code class="ph codeph">ALL FIELDS WITH</code></p></td>
<td><code class="ph codeph">TYPE TABLE FOR READ IMPORT bdef</code></td>
<td><p><code class="ph codeph">%control</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p></td>
</tr>
<tr class="even">
<td>Read-by-association operation (<code class="ph codeph">... BY \_assoc ...</code>)</td>
<td><p><code class="ph codeph">FROM</code></p>
<p><code class="ph codeph">FIELDS (...) WITH</code></p>
<p><code class="ph codeph">ALL FIELDS WITH</code></p></td>
<td><code class="ph codeph">TYPE TABLE FOR READ IMPORT bdef\_assoc</code></td>
<td><p><code class="ph codeph">%control</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p></td>
</tr>
<tr class="odd">
<td>Read operation executing a function (using the keyword <code class="ph codeph">EXECUTE</code>)</td>
<td><code class="ph codeph">FROM</code></td>
<td><code class="ph codeph">TYPE TABLE FOR FUNCTION IMPORT bdef~function</code></td>
<td><p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p></td>
</tr>
</tbody>
</table>

`bdef` is the root entity name, `_assoc` the name of the association defined in the underlying CDS view of the root entity, and `function` the name of a function specified in the BDEF. See the details on the components in the documentation for [Components of BDEF Derived Types](abapderived_types_comp.md).

### Hints

- The read statement must be completed by specifying a [result](abapeml_result.md) after `fields_tab`. Optionally, [`response_param`](abapeml_response.md) can also be specified after `fields_tab`.

- Depending on the context, the components listed in the **Components** column of the overview table might cover more than mentioned there. For example, the draft indicator `%is_draft` is available in case of drafts only. `%pid` is only available in late numbering scenarios.

- In the internal table (`fields_tab`), all key fields must be specified, otherwise the read operation fails. In read-by-association operations, all key fields of an associated entity are returned by default.

- The additions `FIELDS ( ... ) WITH` and [`SET FIELDS WITH`](abapmodify_entity_entities_fields.md) are only possible for read operations executing functions (using `EXECUTE`) if the function is defined with [`deep [table] parameter`](../rap-behavior-definitions/abenbdl_action_input_param.md) and without a [`selective`](../rap-behavior-definitions/abenbdl_action_output_para.md) parameter in the BDEF.

## Variant 1

`... FROM fields_tab ...`

### Description

The read operation considers input parameters specified in an internal table ([`fields_tab`](abapeml_fields_tab.md)). It can be used for all operations.

The [`%control`](abapderived_types_comp.md) structure must be filled explicitly in `fields_tab`.

In [managed](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md) scenarios, setting the[`%control`](abapderived_types_control.md) flags for key fields, such as in the context of the `FROM` addition in ABAP EML `READ` statements, is optional. The returned instances include the key values.

### Hint

`fields_tab` is in a read position. `%control` is set explicitly.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_READ_OP_FIELDS` shows the use of `FROM` with a `READ` operation. The `%control` structure shows that some fields are requested, some are not.

``` abap
READ ENTITY demo_spfli_flights 
    FROM VALUE #( 
        ( %key-Carrid = 'AZ' 
          %key-Connid = 790 
          %control = VALUE #( Airpfrom  = if_abap_behv=>mk-on 
                              Airpto    = if_abap_behv=>mk-on 
                              Cityfrom  = if_abap_behv=>mk-on 
                              Cityto    = if_abap_behv=>mk-on 
                              Countryfr = if_abap_behv=>mk-on 
                              Countryto = if_abap_behv=>mk-on 
                              Deptime   = if_abap_behv=>mk-off 
                              Arrtime   = if_abap_behv=>mk-off 
                              Distance  = if_abap_behv=>mk-off 
                              Fltime    = if_abap_behv=>mk-on 
                            ) ) ) 
      RESULT FINAL(read_from) 
      FAILED FINAL(failed_from).
```

## Variant 2

`... FIELDS ( comp1 comp2 ... ) WITH fields_tab ...`

### Description

Fields to be returned by the read operation are specified in a field list in brackets after the keyword `FIELDS`. The input parameters for the read operation are specified in an internal table ([`fields_tab`](abapeml_fields_tab.md)). The fields (`comp1`, `comp2`, etc.) can be any of the entity's fields. Key fields can but need not be explicitly specified since they are read and returned by default even if not specified. At least one field must be specified in the field list. The fields are not separated by a comma. The order of the fields is irrelevant. However, the order of the columns, for example, of the read result table corresponds to the order in the database table.

The variant is a convenience variant and shortcut for `FROM`. `%control` is filled implicitly in `fields_tab`. The advantage of using the variant is that it provides static compiler checks and code completion. For example, static field attributes such as `readonly` and `mandatory` are respected.

### Hint

`fields_tab` is both a read and write position since `%control` is set implicitly.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_READ_OP_FIELDS` shows the use of `FIELDS ... WITH` with a read-by-association operation.

``` abap
READ ENTITY demo_spfli_flights 
    BY \_Flights 
    FIELDS ( Carrid Connid Currency Price Planetype ) 
     WITH VALUE #( ( %key-Carrid = 'AA' 
                     %key-Connid = 26 ) ) 
     RESULT FINAL(rba_fields_with) 
     FAILED FINAL(failed_rba_fields_with).
```

The `FIELDS ( ... ) WITH` addition supports the setting of `%control` regarding components in [`deep` input parameters](../rap-behavior-definitions/abenbdl_action_input_param.md) in the context of deep [action](../../abap-glossary/abenrap_action_glosry.md) and [function](../../abap-glossary/abenrap_function_glosry.md) parameters. In this context, setting values of the `%control` structure is only possible if the [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) for a [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md) is defined with [`with hierarchy;`](../rap-behavior-definitions/abenbdl_bdef_abstract_header.md) and the behavior for one or more of the nodes of the [CDS composition tree](../../abap-glossary/abencds_composition_tree_glosry.md) is defined with [`define behavior for ... with control`](../rap-behavior-definitions/abenbdl_define_beh_abstract.md).

With the following syntax options, the setting of `%control` values (in [`%param`](abapderived_types_param.md)) can be more detailed out for components of associated entities, for example, if only subcomponents of associated abstract entities are to be flagged and not the whole abstract entity itself:

- An additional pair of parentheses following an associated abstract entity `_ent` containing components (e. g. `comp1`) denotes that `_ent` is not flagged itself but the subcomponents specified: `... FIELDS ( ... _ent ( comp1 comp2 ... ) ... ) WITH ...`

- `+` before the additional pair of parentheses following an associated abstract entity `_ent` containing components (e. g. `comp1`) denotes that the specified subcomponents are flagged and the abstract entity `_ent` itself, too: `... FIELDS ( ... _ent +( comp1 comp2 ... ) ... ) WITH ...`

In the following code snippets, `a` represents a field of the parent abstract entity, `_ent` represents an associated abstract entity. `b` represents a subcomponent contained in `_ent`. The example demonstrates the effect on the `%control` structures contained in `%param`:

``` abap
... FIELDS ( a _ent ) WITH ... 
"%param-%control-a: flagged 
"%param-%control-_ent: flagged 
"%param-_ent-%control-b: not flagged 
 
... FIELDS ( a _ent ( b ) ) WITH ... 
"%param-%control-a: flagged 
"%param-%control-_ent: not flagged 
"%param-_ent-%control-b: flagged 
 
... FIELDS ( a _ent +( b ) ) WITH ... 
"%param-%control-a: flagged 
"%param-%control-_ent: flagged 
"%param-_ent-%control-b: flagged
```

See the class `CL_DEMO_RAP_EML_DEEP_PARA_FLDS` that visualizes these syntax options using an action.

## Variant 3

`... ALL FIELDS WITH fields_tab ...`

### Description

All fields of an instance are read according to input parameters for the read operation specified in an internal table ([`fields_tab`](abapeml_fields_tab.md)).

The variant is a convenience variant and shortcut for `FROM`. It cannot be used for `EXECUTE`. `%control` is filled implicitly in `fields_tab`.

### Hint

`fields_tab` is both a read and write position since `%control` is set implicitly.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_READ_OP_FIELDS` shows the use of `ALL FIELDS WITH` with a `READ` operation.

``` abap
READ ENTITY demo_spfli_flights 
    BY \_Flights 
    ALL FIELDS WITH VALUE #( ( %key-Carrid = 'DL' 
                               %key-Connid = 1699 ) ) 
     RESULT FINAL(rba_all_fields_with) 
     FAILED FINAL(failed_rba_all_fields_with).
```

### Executable Example

- The example [`READ`: Field Specification Expressions](abeneml_read_op_fields_abexa.md) demonstrates several different variants of field specification expressions with a simple managed RAP BO.

- For more examples on `READ` operations in general, see [Examples for ABAP EML `READ`](abapeml_read_examples_abexas.md).
