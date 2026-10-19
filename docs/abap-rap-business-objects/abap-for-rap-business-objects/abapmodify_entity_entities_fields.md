---
title: "MODIFY ENTITY, ENTITIES, field_spec"
source_file: abapmodify_entity_entities_fields.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > MODIFY ENTITY, ENTITIES > MODIFY ENTITY, ENTITIES, operations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MODIFY ENTITY, ENTITIES, field_spec

## Syntax

``` abap
...  { FROM fields_tab } 
   | { AUTO FILL CID WITH fields_tab } 
   | { [AUTO FILL CID] FIELDS ( comp1 comp2 ... ) WITH fields_tab } 
   | { [AUTO FILL CID] SET FIELDS WITH fields_tab } ...  
```

[`fields_tab`](abapeml_fields_tab.md) · [`fields_tab`](abapeml_fields_tab.md) · [`fields_tab`](abapeml_fields_tab.md) · [`fields_tab`](abapeml_fields_tab.md)

### Variant

[1. `... FROM fields_tab`](abapmodify_entity_entities_fields.md#variant-1)

[2. `... AUTO FILL CID WITH fields_tab`](abapmodify_entity_entities_fields.md#variant-2)

[3. `... [AUTO FILL CID] FIELDS ( comp1 comp2 ... ) WITH fields_tab`](abapmodify_entity_entities_fields.md#variant-3)

[4. `... [AUTO FILL CID] SET FIELDS WITH fields_tab`](abapmodify_entity_entities_fields.md#variant-4)

### Addition

[`... AUTO FILL CID`](abapmodify_entity_entities_fields.md#addition)

## Overview

### Description

Field specification expressions define input parameters for modify operations on entity instances.

The `FIELDS (...) WITH` and `SET FIELDS WITH` variants can be used for operations that use the `CREATE`, `CREATE BY` and `UPDATE` ABAP EML statements. The `FROM` variant is the only option for `DELETE` and `EXECUTE` in most cases. The variants with `AUTO FILL CID` can be used for the operations `CREATE` and `CREATE BY`.

The parameters that are respected for modify operations must be specified in an internal table ([`fields_tab`](abapeml_fields_tab.md)). It is essential that the internal table is typed with the required [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md). Depending on the operation and the variant, the parameters of the internal table comprise [special components](abapderived_types_comp.md).

The following table provides an overview of the operations, which field specification expressions are possible for the operations, and which type and components of the required internal table are relevant. Depending on the context, the components listed in the **Components** column might cover more than mentioned. For example, the draft indicator `%is_draft` is available in case of [draft](../rap-behavior-definitions/abenbdl_with_draft.md) scenarios only. `%pid` is only available in [`late numbering`](../rap-behavior-definitions/abenbdl_late_numbering.md) scenarios.

<table>
<thead>
<tr class="header">
<th><strong>Operation</strong></th>
<th><strong>Field Specification Expression</strong></th>
<th><strong>Type of Internal Table <code class="ph codeph">fields_tab</code></strong></th>
<th><strong>Components of Internal Table</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">CREATE</code></td>
<td><p><code class="ph codeph">FROM</code></p>
<p><code class="ph codeph">AUTO FILL CID WITH</code></p>
<p><code class="ph codeph">FIELDS (...) WITH</code></p>
<p><code class="ph codeph">SET FIELDS WITH</code></p></td>
<td><code class="ph codeph">TABLE FOR CREATE bdef</code></td>
<td><p><code class="ph codeph">%cid</code></p>
<p><code class="ph codeph">%control</code></p>
<p><code class="ph codeph">%data</code></p>
<p><code class="ph codeph">%key</code></p>
<p><strong>Note:</strong> In case of <code class="ph codeph">FROM</code> and <code class="ph codeph">AUTO FILL CID WITH</code>, <code class="ph codeph">%control</code> must be filled explicitly.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">CREATE BY _assoc</code></td>
<td><p><code class="ph codeph">FROM</code></p>
<p><code class="ph codeph">AUTO FILL CID WITH</code></p>
<p><code class="ph codeph">FIELDS (...) WITH</code></p>
<p><code class="ph codeph">SET FIELDS WITH</code></p></td>
<td><code class="ph codeph">TABLE FOR CREATE bdef\_assoc</code></td>
<td><p><code class="ph codeph">%cid_ref</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%target</code></p>
<p><code class="ph codeph">%tky</code></p>
<p><strong>Note:</strong> In case of <code class="ph codeph">FROM</code> and <code class="ph codeph">AUTO FILL CID WITH</code>, <code class="ph codeph">%control</code> must be filled explicitly within <code class="ph codeph">%target</code>.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">UPDATE</code></td>
<td><p><code class="ph codeph">FROM</code></p>
<p><code class="ph codeph">FIELDS (...) WITH</code></p>
<p><code class="ph codeph">SET FIELDS WITH</code></p></td>
<td><code class="ph codeph">TABLE FOR UPDATE bdef</code></td>
<td><p><code class="ph codeph">%cid_ref</code></p>
<p><code class="ph codeph">%control</code></p>
<p><code class="ph codeph">%data</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p>
<p><strong>Note:</strong> In case of <code class="ph codeph">FROM</code>, <code class="ph codeph">%control</code> must be filled explicitly.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">DELETE</code></td>
<td><code class="ph codeph">FROM</code></td>
<td><code class="ph codeph">TABLE FOR DELETE bdef</code></td>
<td><p><code class="ph codeph">%cid_ref</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">EXECUTE</code></td>
<td><code class="ph codeph">FROM</code></td>
<td><code class="ph codeph">TABLE FOR ACTION IMPORT bdef~action</code></td>
<td><p><code class="ph codeph">%cid_ref</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%param</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p></td>
</tr>
</tbody>
</table>

`bdef` is the root entity name, `_assoc` the name of the association defined in the underlying CDS view of the root entity, and `action` the name of an action specified in the BDEF. See the details on the components in the documentation for [Components of BDEF Derived Types](abapderived_types_comp.md).

### Hints

- In case of operations for which `%cid_ref` can be specified in the internal table, the mandatory specification of the keys in the internal table can be omitted if a clear reference to the instance that is to be modified is given using `%cid_ref`.

- In case of create and create-by-association operations, `%cid` should be specified even if the [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) is not interested in `%cid`.

- The additions `FIELDS ( ... ) WITH` and `SET FIELDS WITH` are only possible for modify operations executing actions (using `EXECUTE`) if the action is defined with [`deep [table] parameter`](../rap-behavior-definitions/abenbdl_action_input_param.md) and without a [`selective`](../rap-behavior-definitions/abenbdl_action_output_para.md) parameter in the BDEF.

## Variant 1

`... FROM fields_tab`

### Description

The modify operation respects input parameters specified in an internal table ([`fields_tab`](abapeml_fields_tab.md)). It can be used for all operations (`CREATE`, `CREATE BY`, `UPDATE`, `DELETE`, `EXECUTE`) and it is the only option for `DELETE` and `EXECUTE`. The [`%control`](abapderived_types_comp.md) structure must be filled explicitly in the internal table `fields_tab` for `CREATE`, `CREATE BY` and `UPDATE`.

**Note:**

- `fields_tab` is in a read position. `%control` is set explicitly.

- Due to the explicit filling of the `%control` structure, more lines of code are necessary compared with the variants `FIELDS (...) WITH` and `SET FIELDS WITH`.

- A syntax check on static read-only fields is not possible with this variant (in contrast to `FIELDS (...) WITH`).

- Fields can be set to initial values.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_MODIFY_OPRTNS` demonstrates the keyword `FROM` within a `MODIFY` statement.

``` abap
MODIFY ENTITY demo_managed_root 
      CREATE FROM VALUE #( 
        ( %cid = 'cid1' 
          key_field = 1 
          %control-key_field = if_abap_behv=>mk-on 
          data_field1_root = 'aaa' 
          %control-data_field1_root = if_abap_behv=>mk-on 
          data_field2_root = 'bbb' 
          %control-data_field2_root = if_abap_behv=>mk-on ) 
        ( %cid = 'cid2' 
          key_field = 2 
          %control-key_field = if_abap_behv=>mk-on 
          data_field1_root = 'ccc' 
          %control-data_field1_root = if_abap_behv=>mk-on 
          data_field2_root = 'ddd' 
          %control-data_field2_root = if_abap_behv=>mk-on ) 
        ( %cid = 'cid3' 
          key_field = 3 
          %control-key_field = if_abap_behv=>mk-on 
          data_field1_root = 'eee' 
          %control-data_field1_root = if_abap_behv=>mk-on 
          data_field2_root = 'fff' 
          %control-data_field2_root = if_abap_behv=>mk-on ) 
        ( %cid = 'cid4' 
          key_field = 4 
          %control-key_field = if_abap_behv=>mk-on 
          data_field1_root = 'ggg' 
          %control-data_field1_root = if_abap_behv=>mk-on 
          data_field2_root = 'hhh' 
          %control-data_field2_root = if_abap_behv=>mk-on ) 
         ) 
      CREATE BY \_child FROM  VALUE #( 
        ( %cid_ref = 'cid1' 
          %target = VALUE #( 
                ( %cid = 'cid5' 
                  data_field1_child = 'zzz' 
                  %control-data_field1_child = if_abap_behv=>mk-on 
                  data_field2_child = 'yyy' 
                  %control-data_field2_child = if_abap_behv=>mk-on ) 
                 ) ) 
        ( %cid_ref = 'cid2' 
          %target = VALUE #( 
               ( %cid = 'cid6' 
                 data_field1_child = 'xxx' 
                 %control-data_field1_child = if_abap_behv=>mk-on 
                 data_field2_child = 'www' 
                 %control-data_field2_child = if_abap_behv=>mk-on ) 
               ) ) 
        ) 
      UPDATE FROM VALUE #( 
        ( %cid_ref = 'cid3' 
          data_field1_root = 'iii' 
          %control-data_field1_root = if_abap_behv=>mk-on 
          data_field2_root = 'jjj' 
          %control-data_field2_root = if_abap_behv=>mk-on ) 
         ) 
      DELETE FROM VALUE #( ( %cid_ref = 'cid4' ) ) 
        FAILED  FINAL(failed) 
        REPORTED FINAL(reported).
```

## Variant 2

`... AUTO FILL CID WITH fields_tab`

### Description

It is basically the variant `... FROM fields_tab` using the addition `AUTO FILL CID`. In this case, the keyword `WITH` must be used before `fields_tab` instead of `FROM`. The [`%control`](abapderived_types_comp.md) structure must be filled explicitly in the internal table `fields_tab`. The variant can be used for `CREATE` and `CREATE BY`. See the details on `AUTO FILL CID` further down.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_AUTO_FILL_CID` demonstrates the use of `AUTO FILL CID WITH` with a create operation as part of an ABAP EML `MODIFY` statement.

``` abap
MODIFY ENTITY demo_managed_root_4 
 CREATE AUTO FILL CID WITH VALUE #( 
    ( key_field = 3 
      %control-key_field = if_abap_behv=>mk-on 
      field1 = 'create_5' 
      %control-field1 = if_abap_behv=>mk-on 
      field2 = 'create_6' 
      %control-field2 = if_abap_behv=>mk-on 
      field3 = 5 
      %control-field3 = if_abap_behv=>mk-on 
      field4 = 6 
      %control-field4 = if_abap_behv=>mk-on ) 
    ( key_field = 4 
      %control-key_field = if_abap_behv=>mk-on 
      field1 = 'create_7' 
      %control-field1 = if_abap_behv=>mk-on 
      field2 = 'create_8' 
      %control-field2 = if_abap_behv=>mk-on 
      field3 = 7 
      %control-field3 = if_abap_behv=>mk-on 
      field4 = 8 
      %control-field4 = if_abap_behv=>mk-on ) 
    ) 
    MAPPED FINAL(mapped_auto_cid_root).
```

## Variant 3

`... FIELDS ( comp1 comp2 ... ) WITH fields_tab`

### Description

Using this variant, you specify the fields that should be respected by a [RAP BO operation](../../abap-glossary/abenrap_bo_operation_glosry.md) in a field list in parentheses after the keyword `FIELDS`. For example, you specify the fields of [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) that should be updated. The input parameters are specified in an internal table ([`fields_tab`](abapeml_fields_tab.md)). The fields (`comp1`, `comp2`, etc.) can be any of the entity's fields. At least one field must be specified in the field list. The fields are not separated by a comma. The order of the fields provided in this list is irrelevant.

The variant is a convenience variant and a shortcut for `FROM`. It cannot be used for `DELETE` and `EXECUTE`. `%control` is filled implicitly in `fields_tab`. If a field is specified within the brackets of `FIELDS (...) WITH`, it is set to the hexadecimal value *01* in the `%control` structure. Otherwise, it is set to the hexadecimal value *00*.

**Note:**

- `fields_tab` is both a read and write position since `%control` is set implicitly.

- A syntax check on static read-only fields is possible with this variant when specifying the fields within the parentheses of `FIELDS (...) WITH`.

- Fields can be set to initial values.

- If the key is not specified within the parentheses, the initial value for the key is used for the operation (even if a concrete value for the key is specified in the BDEF derived type). The initial value for the key is also used if the key is specified within the parentheses but a concrete value is not specified in the BDEF derived type.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code demonstrates the implicit setting of the `%control` structure component values using `FIELDS (...) WITH` within `MODIFY` statements.

First, an internal table typed with a [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) is created and filled. This table is used to create a [RAP BO instance](../../abap-glossary/abenrap_bo_instance_glosry.md) in the context of a [RAP create operation](../../abap-glossary/abenrap_create_operation_glosry.md). All data fields are specified within the parentheses of the `FIELDS (...) WITH` addition as part of an ABAP EML `MODIFY` statement. As a next step, the internal table is filled with other values followed by another ABAP EML `MODIFY` statement. Here, the fields specified within the parentheses of `FIELDS (...) WITH` purposely do not include all fields.

The outcome shows the effect of the field specification and the implicit setting of the `%control` structure. Before the ABAP EML modify request, all hexadecimal values of the input table are *00*. For the first ABAP EML modify request in which all fields are specified, all values in the `%control` structure are set to *01*. For the second ABAP EML modify request, only those components in the `%control` structure are set to the hexadecimal value *01* that are specified within the parentheses of the `FIELDS (...) WITH` addition. Consequently, despite specifying values in the input table, these fields have their initial value in the created instance.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DELETE FROM demo_tab_root_3. 
 
DATA input TYPE TABLE FOR CREATE demo_managed_root_4. 
input = VALUE #( ( key_field = 1 field1 = 'a' field2 = 'a' field3 = 1 
                   field4 = 1 ) ). 
 
out->write( input ). 
 
MODIFY ENTITY demo_managed_root_4 
  CREATE FIELDS ( key_field field1 field2 field3 field4 ) WITH input. 
 
out->write( input ). 
 
input = VALUE #( ( key_field = 2 field1 = 'b' field2 = 'b' field3 = 2 
                   field4 = 2 ) ). 
 
MODIFY ENTITY demo_managed_root_4 
  CREATE FIELDS ( key_field field1 field4 ) WITH input. 
 
out->write( input ). 
 
COMMIT ENTITIES. 
 
SELECT * FROM demo_tab_root_3 INTO TABLE @FINAL(itab). 
out->write( itab ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_MODIFY_OPRTNS` demonstrates the keywords `FIELDS (...) WITH` within a `MODIFY` statement.

``` abap
MODIFY ENTITY demo_managed_root 
      CREATE FIELDS ( key_field data_field1_root 
                      data_field2_root ) 
        WITH VALUE #( 
        ( %cid = 'cid7' 
          key_field = 5 
          data_field1_root = 'kkk' 
          data_field2_root = 'lll'  ) 
        ( %cid = 'cid8' 
          key_field = 6 
          data_field1_root = 'mmm' 
          data_field2_root = 'nnn'  ) 
        ) 
      CREATE BY \_child FIELDS ( data_field1_child 
                                 data_field2_child ) 
        WITH VALUE #( 
        ( %cid_ref = 'cid8' 
          %target = VALUE #( ( %cid = 'cid9' 
                               data_field1_child = 'vvv' 
                               data_field2_child = 'uuu' ) 
                           ) ) 
        ) 
      UPDATE FIELDS ( data_field1_root 
                      data_field2_root ) 
        WITH VALUE #( 
       ( %cid_ref = 'cid7' 
         data_field1_root = 'ooo' 
         data_field2_root = 'ppp' ) 
         ) 
        FAILED   FINAL(failed) 
        REPORTED FINAL(reported).
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

## Variant 4

`... [AUTO FILL CID] SET FIELDS WITH fields_tab`

### Description

It is a convenience variant and shortcut for `FROM`. The modify operation respects input parameters specified in an internal table ([`fields_tab`](abapeml_fields_tab.md)).

**Using this variant is not recommended** for the following reasons:

- The variant is very slow if the input is very large. Hence, using it leads to a syntax warning that can be removed by the pragma `##SETFIELDS_OK`. Note that the syntax warning does not come up if the internal table following `SET FIELDS WITH` is specified using a [constructor expression](../../abap-glossary/abenconstructor_expression_glosry.md) with the [`VALUE`](../../abap-programming-language/abap-creating-objects-and-values/abenconstructor_expression_value.md).

- A syntax check on static read-only fields is not possible with this variant (in contrast to `FIELDS (...) WITH`).

- Fields **cannot** be set to initial values.

The variant cannot be used for `DELETE` and `EXECUTE`. `%control` is filled implicitly in `fields_tab`. If a field is specified in `fields_tab`, it is set to the hexadecimal value *01* in the `%control` structure. Otherwise, it is set to the hexadecimal value *00*.

**Note:**

- `fields_tab` is both a read and write position since `%control` is set implicitly.

- A syntax check on static read-only fields is not possible with this variant (in contrast to `FIELDS (...) WITH`).

- Fields **cannot** be set to initial values.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_MODIFY_OPRTNS` demonstrates the keywords `SET FIELDS WITH` within an ABAP EML `MODIFY` statement.

``` abap
MODIFY ENTITY demo_managed_root 
      CREATE SET FIELDS ##SETFIELDS_OK 
      WITH VALUE #( 
        ( %cid = 'cid10' 
          key_field = 7 
          data_field1_root = 'qqq' 
          data_field2_root = 'rrr'  ) 
        ( %cid = 'cid11' 
          key_field = 8 
          data_field1_root = 'sss' 
          data_field2_root = 'ttt'  ) 
        ) 
      CREATE BY \_child SET FIELDS WITH VALUE #( 
        ( %cid_ref = 'cid10' 
          %target = VALUE #( ( %cid = 'cid12' 
                               data_field1_child = 'ttt' 
                               data_field2_child = 'sss' ) 
                           ) ) 
        ( %cid_ref = 'cid11' 
          %target = VALUE #( ( %cid = 'cid13' 
                               data_field1_child = 'rrr' 
                               data_field2_child = 'qqq' ) 
                           ) ) 
        ) 
      UPDATE SET FIELDS WITH VALUE #( 
        ( %cid_ref = 'cid11' 
          data_field1_root = 'uuu' 
          data_field2_root = 'vvv' ) 
         ) 
        FAILED   FINAL(failed) 
        REPORTED FINAL(reported).
```

## Addition

`... AUTO FILL CID ...`

### Description

The addition `AUTO FILL CID` can be specified to automatically fill [`%cid`](abapderived_types_comp.md) in the following contexts:

- Create operations (`MODIFY ... CREATE AUTO FILL CID ...`)

- Create-by-association operations (`MODIFY ... CREATE BY \assoc AUTO FILL CID ...`)

- [Factory actions](../rap-behavior-definitions/abenbdl_action.md) (`MODIFY ... EXECUTE action AUTO FILL CID ...`)

- [Repeatable actions](../../abap-glossary/abenrap_repeatable_action_glosry.md)

Specifying `%cid` should be done even if the [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) is not interested. Especially in the context of [`early numbering`](../rap-behavior-definitions/abenbdl_early_numb.md) and [`late numbering`](../rap-behavior-definitions/abenbdl_late_numbering.md) scenarios, `%cid` must be specified to avoid issues.

If the addition is specified and `%cid` is initial, `%cid` gets automatically filled with dummy values that have the prefix `%ABAP_EML_CID__`. This prefix is followed by numbers, for example, `%ABAP_EML_CID__1`, `%ABAP_EML_CID__2`, and so on. If the addition is specified and `%cid` is specified manually, too, only the manually specified value for `%cid` is valid.

If `%cid_ref` is to be used, `%cid` must be specified manually since `%cid_ref` cannot refer to an automatically created value.

If `AUTO FILL CID` is used, `%cid` must not be filled with a value prefixed by `%ABAP_EML_CID__` in capital letters. Otherwise, the runtime error `BEHAVIOR_RESERVED_PREFIX` occurs.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code (see more examples here: `CL_DEMO_RAP_EML_AUTO_FILL_CID`) demonstrates the use of `AUTO FILL CID` and `FIELDS ( ... ) WITH` with a create-by-association operation as part of an ABAP EML `MODIFY` statement.

``` abap
MODIFY ENTITY demo_managed_root_4 
     CREATE BY \_child AUTO FILL CID 
     FIELDS ( key_field_child field1 field2 field3 field4 ) 
     WITH VALUE #( 
        ( key_field = 3 
          %target = VALUE #( 
           ( key_field_child = 3 
             field1 = 'cba_5' 
             field2 = 'cba_6' 
             field3 = 5 
             field4 = 6 ) 
           ) ) 
         ( key_field = 4 
           %target = VALUE #( 
           ( key_field_child = 4 
             field1 = 'cba_7' 
             field2 = 'cba_8' 
             field3 = 7 
             field4 = 8 ) 
            ) ) ) 
          MAPPED FINAL(mapped_auto_cid_child).
```

### Executable Example

- The example [`MODIFY`: Field Specification Expressions](abeneml_modify_op_fields_abexa.md) demonstrates the variants of field selection when setting up internal tables for different modify statements and hence the manipulation of a simple managed RAP BO.

- The class `CL_DEMO_RAP_EML_AUTO_FILL_CID` demonstrates create and create-by-association operations with manually specified `%cid` components and automatically created ones using `AUTO FILL CID`. The output shows the [`MAPPED` responses](abapeml_response.md) of the operations as well as the instances that are persisted to the database following [`COMMIT ENTITIES`](abapcommit_entities.md) statements.

- For more examples on `MODIFY` operations in general, see [Examples for ABAP EML `MODIFY`](abapeml_modify_examples_abexas.md).
