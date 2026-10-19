---
title: "TYPE STRUCTURE FOR"
source_file: abaptype_structure_for.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# TYPE STRUCTURE FOR

## Syntax

``` abap
... STRUCTURE FOR { ACTION IMPORT bdef~action } 
                | { ACTION REQUEST bdef~action } 
                | { ACTION RESULT bdef~action } 
                | { [INSTANCE] AUTHORIZATION KEY bdef[~group] } 
                | { [INSTANCE] AUTHORIZATION REQUEST bdef[~group] } 
                | { [INSTANCE] AUTHORIZATION RESULT bdef[~group] } 
                | { CHANGE bdef } 
                | { CREATE bdef [\_assoc] } 
                | { DELETE bdef } 
                | { DETERMINATION bdef~det } 
                | { EVENT bdef~evt } 
                | { FAILED [EARLY | LATE] bdef } 
                | { [INSTANCE] FEATURES KEY bdef[~group] } 
                | { [INSTANCE] FEATURES REQUEST bdef[~group] } 
                | { [INSTANCE] FEATURES RESULT bdef[~group] } 
                | { FUNCTION IMPORT bdef~function } 
                | { FUNCTION REQUEST bdef~function } 
                | { FUNCTION RESULT bdef~function } 
                | { GLOBAL AUTHORIZATION REQUEST bdef[~group] } 
                | { GLOBAL AUTHORIZATION RESULT bdef[~group] } 
                | { GLOBAL FEATURES REQUEST bdef[~group] } 
                | { GLOBAL FEATURES RESULT bdef[~group] } 
                | { HIERARCHY bdef } 
                | { KEY OF bdef } 
                | { MAPPED [EARLY | LATE] bdef } 
                | { PERMISSIONS KEY bdef } 
                | { PERMISSIONS REQUEST bdef } 
                | { PERMISSIONS RESULT bdef } 
                | { READ CHANGES bdef } 
                | { READ IMPORT bdef [\_assoc] } 
                | { READ LINK bdef\_assoc } 
                | { READ RESULT bdef [\_assoc] } 
                | { REPORTED [EARLY | LATE] bdef } 
                | { UPDATE bdef } 
                | { VALIDATION bdef~valid } ...  
```

## Description

Special ABAP type for structures in the context of [RAP](../../abap-glossary/abenrap_glosry.md). The structures have [special components](abapderived_types_comp.md) tailored for RAP purposes. Those structures are used to enable the communication between a [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) and a [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md).

Structures typed with `TYPE STRUCTURE FOR` constitute a helper construct if structures are needed for internal tables in the RAP context. Apart from that, several structures serve distinct purposes. For example, in the context of [`GET PERMISSIONS`](abapget_permissions.md) statements, a structure of type `TYPE STRUCTURE FOR PERMISSIONS REQUEST` must be specified as `REQUEST` parameter to define which operations, fields or actions are respected for the retrieval of permission information.

With the use of `TYPE STRUCTURE FOR`, it is possible to get the line type of an internal table that is typed with the respective [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md). In doing so, a type declaration with `LINE OF` can be avoided.

Notes on the syntax:

- `bdef`: `bdef` means the full entity name of either a root or child entity, or an alias. An alias, however, only works within handler methods of a RAP BO provider. Aliases do not work for explicit declarations outside of implementation classes. The reference to a child entity can also be specified together with its root entity by writing the root entity name followed by `\\` and the child entity name: `root_entity\\child_entity`. If this syntax is used, the child's alias name must be specified if specified in the BDEF: `root_entity\\child_entity_alias`.

- `bdef\_assoc`: `_assoc` is the name of an association specified in the underlying CDS view of the RAP BO. The reference to the association is made using a backslash `\`.

- `bdef~action`: `action` is the name of an action specified in the BDEF. The reference to the action is made using a tilde (`~`).

- `bdef~function`: `function` is the name of a function specified in the BDEF. The reference to the function is made using a tilde (`~`).

- `bdef~group`: `group` is the name of a group specified in the BDEF. The reference to the group is made using a tilde (`~`).

- `bdef~det`: `det` is the name of a determination specified in the BDEF. The reference to the determination is made using a tilde (`~`).

- `bdef~valid`: `valid` is the name of a validation specified in the BDEF. The reference to the validation is made using a tilde (`~`).

- `bdef~evt`: `evt` is the name of a [RAP business event](../../abap-glossary/abenrap_entity_event_glosry.md) specified in the BDEF. The reference to the event is made using a tilde (`~`).

## Hints

- Certain BDEF derived types can only be specified and used within implementation classes and [ABP auxiliary classes](../../abap-glossary/abenabp_aux_class_glosry.md), not outside them. These types include the following: `FOR CHANGE`, `FOR DETERMINATION`, `FOR VALIDATION`, `FOR ... FEATURES`, ` FOR ... AUTHORIZATION`

- Internal tables typed with [`TYPE TABLE FOR`](abaptype_table_for.md) and structures typed with `TYPE STRUCTURE FOR` largely share the same set of variants, whereas there are more possible variants for the type `TYPE STRUCTURE FOR` in total.

- For details on the components (`%cid`, `%cid_ref`, etc.), see the topic [Components of BDEF Derived Types](abapderived_types_comp.md).

- The components listed in the **Components** column of the following tables might cover more components or fewer than mentioned there. It depends on the specification of the BDEF. For example, the draft indicator `%is_draft` is available in case of drafts only in multiple BDEF derived types. `%pid` is only available in BDEF derived types in [`late numbering`](../rap-behavior-definitions/abenbdl_late_numbering.md) scenarios.

**Overview 1**

The following table covers the variants including information on the BDEF prerequisites and the structures' components. The table includes only those variants that are exclusive for TYPE STRUCTURE FOR and not available for [`TYPE TABLE FOR`](abaptype_table_for.md).

<table>
<thead>
<tr class="header">
<th><strong><code class="ph codeph">TYPE STRUCTURE FOR ...</code></strong></th>
<th><strong>Purpose</strong></th>
<th><strong>Prerequisites</strong></th>
<th><a href="abapderived_types_comp.html">Possible Components</a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">ACTION REQUEST</code></td>
<td>Used to specify whether <a href="abenbdl_action.html">actions</a> should be executed based on request parameters, i. e. if the result of the action should be returned completely or only parts of it.</td>
<td>The notation <code class="ph codeph">result selective</code> must be specified for an action.</td>
<td>Key and data fields are typed with <code class="ph codeph">ABP_BEHV_FLAG</code>.</td>
</tr>
<tr class="even">
<td><p><code class="ph codeph">AUTHORIZATION REQUEST</code></p>
<p><code class="ph codeph">INSTANCE AUTHORIZATION REQUEST</code></p></td>
<td><p>Used to retrieve information on <a href="abenbdl_authorization.html">instance-based authorization</a> in the context of handler method implementations of ABAP EML <a href="abapget_permissions.html"><code class="ph codeph">GET PERMISSIONS</code></a> statements. Request parameters, that have been specified for <a href="abenrap_bo_instance_glosry.html">RAP BO instances</a> to define the conditions of the permission information retrieval, serve as import parameters for the corresponding handler methods. For example, the information retrieval for certain operations can be enabled or disabled.</p>
<p>A specification with <code class="ph codeph">AUTHORIZATION REQUEST</code> is the same as with <code class="ph codeph">INSTANCE AUTHORIZATION REQUEST</code>.</p></td>
<td>An authorization check must be specified in the BDEF using the property <code class="ph codeph">instance</code>. See the details in the RAP BDL documentation for <a href="abenbdl_authorization.html">authorization</a>.</td>
<td><p><strong>Note:</strong> The availability of the following components depends on the context and definition in the BDEF, that is, only a subset of the components below can be expected to be available.</p>
<p>Subcomponents of <code class="ph codeph">%action</code> and <code class="ph codeph">%assoc</code> typed with <code class="ph codeph">ABP_BEHV_FLAG</code></p>
<p><code class="ph codeph">%create</code>, <code class="ph codeph">%delete</code> and <code class="ph codeph">%update</code> typed with <code class="ph codeph">ABP_BEHV_FLAG</code></p></td>
</tr>
<tr class="odd">
<td><p><code class="ph codeph">FEATURES REQUEST</code></p>
<p><code class="ph codeph">INSTANCE FEATURES REQUEST</code></p></td>
<td><p>Used for retrieving <a href="abenbdl_actions_fc.html">instance feature control</a> information in the context of handler method implementations of ABAP EML <a href="abapget_permissions.html"><code class="ph codeph">GET PERMISSIONS</code></a> statements. Request parameters, that have been specified for RAP BO instances to define the conditions of the permission information retrieval, serve as import parameters for the corresponding handler methods. For example, the information retrieval for certain operations can be enabled or disabled.</p>
<p>A specification with <code class="ph codeph">FEATURES REQUEST</code> is the same as with <code class="ph codeph">INSTANCE FEATURES REQUEST</code>.</p></td>
<td>The property <code class="ph codeph">features: instance</code> must be specified in the BDEF.</td>
<td><p><strong>Note:</strong> The availability of the following components depends on the context and definitions in the BDEF, that is, only a subset of the below components can be expected to be available.</p>
<p>Subcomponents of <code class="ph codeph">%action</code> and <code class="ph codeph">%assoc</code> typed with <code class="ph codeph">ABP_BEHV_FLAG</code></p>
<p><code class="ph codeph">%create</code>, <code class="ph codeph">%delete</code> and <code class="ph codeph">%update</code> typed with <code class="ph codeph">ABP_BEHV_FLAG</code></p>
<p>Subcomponents of <code class="ph codeph">%field</code> typed with <code class="ph codeph">ABP_BEHV_FEATURE</code></p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">FUNCTION REQUEST</code></td>
<td>Used to specify whether <a href="abenbdl_function.html">functions</a> should be executed based on request parameters, i. e. if the result of the function should be returned completely or only parts of it.</td>
<td>The notation <code class="ph codeph">result selective</code> must be specified for a function.</td>
<td>Key and data fields typed with <code class="ph codeph">ABP_BEHV_FLAG</code>.</td>
</tr>
<tr class="odd">
<td><code class="ph codeph">GLOBAL FEATURES RESULT</code></td>
<td>Used for retrieving information on <a href="abenbdl_actions_fc.html">global feature control</a> in the context of handler method implementations of ABAP EML <a href="abapget_permissions.html"><code class="ph codeph">GET PERMISSIONS</code></a> statements. The result contains the outcome of the permission information retrieval for global features based on the request parameters.</td>
<td>The property <code class="ph codeph">features: global</code> must be specified in the BDEF.</td>
<td><p><strong>Note:</strong> The availability of the following components depends on the context and definition in the BDEF, that is, only a subset of the below components can be expected to be available.</p>
<p>Subcomponents of <code class="ph codeph">%action</code> and <code class="ph codeph">%assoc</code> typed with <code class="ph codeph">ABP_BEHV_FLAG</code></p>
<p><code class="ph codeph">%create</code>, <code class="ph codeph">%delete</code> and <code class="ph codeph">%update</code> typed with <code class="ph codeph">ABP_BEHV_FLAG</code></p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">GLOBAL AUTHORIZATION REQUEST</code></td>
<td>Used to retrieve information on <a href="abenbdl_authorization.html">global authorization</a> in the context of handler method implementations of ABAP EML <a href="abapget_permissions.html"><code class="ph codeph">GET PERMISSIONS</code></a> statements. Request parameters, that have been specified for RAP BO instances to define the conditions of the permission information retrieval, serve as import parameters for the corresponding handler methods. For example, the information retrieval for certain operations can be enabled or disabled.</td>
<td>An authorization check must be specified in the BDEF using the property <code class="ph codeph">global</code>. See the details in the RAP BDL documentation for <a href="abenbdl_authorization.html">authorization</a>.</td>
<td><p><strong>Note:</strong> The availability of the following components depends on the context and definition in the BDEF, that is, only a subset of the below components can be expected to be available.</p>
<p>Subcomponents of <code class="ph codeph">%action</code> typed with <code class="ph codeph">ABP_BEHV_FLAG</code></p>
<p><code class="ph codeph">%create</code>, <code class="ph codeph">%delete</code> and <code class="ph codeph">%update</code> typed with <code class="ph codeph">ABP_BEHV_FLAG</code></p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">GLOBAL AUTHORIZATION RESULT</code></td>
<td>Used to retrieve information on <a href="abenbdl_authorization.html">global authorization</a> in the context of handler method implementations of ABAP EML <a href="abapget_permissions.html"><code class="ph codeph">GET PERMISSIONS</code></a> statements. The result contains the outcome of the permission information retrieval for global authorization based on the request parameters.</td>
<td>An authorization check must be specified in the BDEF using the property <code class="ph codeph">global</code>. See the details in the RAP BDL documentation for <a href="abenbdl_authorization.html">authorization</a>.</td>
<td><p><strong>Note:</strong> The availability of the following components depends on the context and definition in the BDEF, that is, only a subset of the below components can be expected to be available.</p>
<p>Subcomponents of <code class="ph codeph">%action</code> and <code class="ph codeph">%assoc</code> typed with <code class="ph codeph">ABP_BEHV_FLAG</code></p>
<p><code class="ph codeph">%create</code>, <code class="ph codeph">%delete</code> and <code class="ph codeph">%update</code> typed with <code class="ph codeph">ABP_BEHV_FLAG</code></p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">GLOBAL FEATURES REQUEST</code></td>
<td>Used to retrieve information on <a href="abenbdl_actions_fc.html">global feature control</a> in the context of handler method implementations of ABAP EML <a href="abapget_permissions.html"><code class="ph codeph">GET PERMISSIONS</code></a> statements. Request parameters, that have been specified for RAP BO instances to define the conditions of the permission information retrieval, serve as import parameters for the corresponding handler methods. For example, the information retrieval for certain operations can be enabled or disabled.</td>
<td>The property <code class="ph codeph">features: global</code> must be specified in the BDEF.</td>
<td><p><strong>Note:</strong> The availability of the following components depends on the context and definition in the BDEF, that is, only a subset of the below components can be expected to be available.</p>
<p>Subcomponents of <code class="ph codeph">%action</code> and <code class="ph codeph">%assoc</code> typed with <code class="ph codeph">ABP_BEHV_FLAG</code></p>
<p><code class="ph codeph">%create</code>, <code class="ph codeph">%delete</code> and <code class="ph codeph">%update</code> typed with <code class="ph codeph">ABP_BEHV_FLAG</code></p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">PERMISSIONS REQUEST</code></td>
<td>Used to retrieve permission information in the context of ABAP EML <a href="abapget_permissions.html"><code class="ph codeph">GET PERMISSIONS</code></a> statements. Request parameters are specified for RAP BO instances to define the conditions of the permission information retrieval, for example, if information retrieval for certain operations is enabled or disabled.</td>
<td>Operations, actions, associations and fields must be specified in the BDEF so that the respective components are available in the structure. For details on the BDEF specifications, see the subtopics in <a href="abenbdl.html">RAP - BDL for Behavior Definitions</a>.</td>
<td><p><strong>Note:</strong> The availability of the following components depends on the context and definitions in the BDEF, that is, only a subset of the below components can be expected to be available.</p>
<p>Subcomponents of <code class="ph codeph">%action</code> and <code class="ph codeph">%assoc</code> typed with <code class="ph codeph">ABP_BEHV_FLAG</code></p>
<p><code class="ph codeph">%create</code>, <code class="ph codeph">%delete</code> and <code class="ph codeph">%update</code> typed with <code class="ph codeph">ABP_BEHV_FLAG</code></p>
<p>Subcomponents of <code class="ph codeph">%field</code> typed with <code class="ph codeph">ABP_BEHV_FEATURE</code></p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">PERMISSIONS RESULT</code></td>
<td>Used to retrieve permission information in the context of ABAP EML <a href="abapget_permissions.html"><code class="ph codeph">GET PERMISSIONS</code></a> statements. The result contains the outcome of the permission information retrieval for <a href="abenbdl_authorization.html">global and instance authorization</a>, <a href="abenbdl_actions_fc.html">global and instance feature control</a> and <a href="abenbdl_field_char.html">static feature control</a>.</td>
<td>Operations, actions, associations and fields must be specified in the BDEF so that the respective components are available in the structure. For details on the BDEF specifications, see the subtopics in <a href="abenbdl.html">RAP - BDL for Behavior Definitions</a>.</td>
<td><p><strong>Note:</strong> The availability of the following components depends on the context and definition in the BDEF, that is, only a subset of the below components can be expected to be available.</p>
<p>Internal table <code class="ph codeph">instances</code> holding the following components:</p>
<p>Key names directly (not <code class="ph codeph">%keys</code> etc.) retaining the full line type;</p>
<p>subcomponents of <code class="ph codeph">%action</code> and <code class="ph codeph">%assoc</code> typed with <code class="ph codeph">ABP_BEHV_FLAG</code>;</p>
<p><code class="ph codeph">%delete</code> and <code class="ph codeph">%update</code> typed with <code class="ph codeph">ABP_BEHV_FLAG</code>;</p>
<p>subcomponents of <code class="ph codeph">%field</code> typed with <code class="ph codeph">ABP_BEHV_FEATURE</code>; the permissions can also be addressed via the component group <code class="ph codeph">%perm</code></p>
<p>Structure <code class="ph codeph">global</code> holding the following components:</p>
<p>Subcomponents of <code class="ph codeph">%action</code> and <code class="ph codeph">%assoc</code> typed with <code class="ph codeph">ABP_BEHV_FLAG</code> ;</p>
<p><code class="ph codeph">%create</code>, <code class="ph codeph">%delete</code> and <code class="ph codeph">%update</code> typed with <code class="ph codeph">ABP_BEHV_FLAG</code>;</p>
<p>subcomponents of <code class="ph codeph">%field</code> typed with <code class="ph codeph">ABP_BEHV_FEATURE</code></p></td>
</tr>
</tbody>
</table>

**Overview 2**

The following table covers the variants that are available for both TYPE STRUCTURE FOR and [`TYPE TABLE FOR`](abaptype_table_for.md).

<table>
<thead>
<tr class="header">
<th><strong><code class="ph codeph">TYPE STRUCTURE FOR ...</code></strong></th>
<th><strong>Purpose</strong></th>
<th><strong>Prerequisites</strong></th>
<th><strong>Components</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">ACTION IMPORT</code></td>
<td>Used to store the import parameters for <a href="abenbdl_action.html">actions</a>.</td>
<td>The action is specified in the BDEF. See the details in the RAP BDL documentation for <a href="abenbdl_action.html">action</a>.</td>
<td><p><strong>Note:</strong> The availability of the following components depends on the context and defined action in the BDEF, that is, only a subset of the below components can be expected to be available. For example, <code class="ph codeph">%param</code> is only available if the action is defined with the notation <code class="ph codeph">PARAMETER</code>.</p>
<p><code class="ph codeph">%cid</code></p>
<p><code class="ph codeph">%cid_ref</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%param</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">ACTION RESULT</code></td>
<td>Used to store the result for <a href="abenbdl_action.html">actions</a>.</td>
<td>Only available if the action has a result parameter specified in the BDEF. See the details in the RAP BDL documentation for <a href="abenbdl_action.html">action</a>.</td>
<td><p><strong>Note:</strong> The availability of the following components depends on the context and defined action in the BDEF, that is, only a subset of the below components might be expected to be available depending on how the action is defined in the BDEF.</p>
<p><code class="ph codeph">%cid</code></p>
<p><code class="ph codeph">%cid_ref</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%param</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p></td>
</tr>
<tr class="odd">
<td><p><code class="ph codeph">AUTHORIZATION KEY</code></p>
<p><code class="ph codeph">INSTANCE AUTHORIZATION KEY</code></p></td>
<td><p>Used for retrieving <a href="abenbdl_authorization.html">instance authorization</a> information in the context of handler method implementations of ABAP EML <a href="abapget_permissions.html"><code class="ph codeph">GET PERMISSIONS</code></a> statements. The keys of RAP BO instances, that have been specified, serve as import parameters for the corresponding handler methods. The keys specify for which RAP BO instance authorization information is to be requested.</p>
<p>A specification with <code class="ph codeph">AUTHORIZATION KEY</code> is the same as with <code class="ph codeph">INSTANCE AUTHORIZATION KEY</code>.</p></td>
<td>An authorization check must be specified in the BDEF: <code class="ph codeph">authorization master</code> or <code class="ph codeph">authorization dependent</code>. See the details in the RAP BDL documentation for <a href="abenbdl_authorization.html">authorization</a>.</td>
<td><p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p></td>
</tr>
<tr class="even">
<td><p><code class="ph codeph">AUTHORIZATION RESULT</code></p>
<p><code class="ph codeph">INSTANCE AUTHORIZATION RESULT</code></p></td>
<td><p>Used for retrieving <a href="abenbdl_authorization.html">instance authorization</a> information in the context of handler method implementations of ABAP EML <a href="abapget_permissions.html"><code class="ph codeph">GET PERMISSIONS</code></a> statements. The result contains the outcome of the permission information retrieval for authorizations based on the keys and request parameters.</p>
<p>A specification with <code class="ph codeph">AUTHORIZATION RESULT</code> is the same as with <code class="ph codeph">INSTANCE AUTHORIZATION RESULT</code>.</p></td>
<td>An authorization check must be specified in the BDEF: <code class="ph codeph">authorization master</code> or <code class="ph codeph">authorization dependent</code>. See the details in the RAP BDL documentation for <a href="abenbdl_authorization.html">authorization</a>.</td>
<td><p><code class="ph codeph">%action</code></p>
<p><code class="ph codeph">%assoc</code></p>
<p><code class="ph codeph">%delete</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%op</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p>
<p><code class="ph codeph">%update</code></p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">CHANGE</code></td>
<td><p>Only used in the <code class="ph codeph">save_modified</code> method that is part of a local saver class of an ABP that inherits from the base saver class <code class="ph codeph">CL_ABAP_BEHAVIOR_SAVER</code>. It is only used in the context of managed implementations with additional save and unmanaged save.</p>
<p>Internal tables that are typed with <code class="ph codeph">TYPE TABLE FOR CHANGE</code> are available as nested tables of the <code class="ph codeph">create</code> and <code class="ph codeph">update</code> structures typed with <a href="abaptype_request_for.html"><code class="ph codeph">TYPE REQUEST FOR CHANGE</code></a> in the <code class="ph codeph">save_modified</code> method.</p></td>
<td>See the topic <a href="abenbdl_saving.html">RAP - <code class="ph codeph">SavingOptions</code></a> for the BDEF prerequisites on managed implementations with additional save and unmanaged save.</td>
<td><p><code class="ph codeph">%control</code></p>
<p><code class="ph codeph">%data</code></p>
<p><code class="ph codeph">%key</code></p>
<p><strong>Note:</strong> The access is not allowed outside of the implementation class.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">CREATE</code></td>
<td>Used for <a href="abapmodify_entity_entities_op.html"><code class="ph codeph">CREATE</code></a> or create-by-association (<a href="abapmodify_entity_entities_op.html"><code class="ph codeph">CREATE BY</code></a>) operations.</td>
<td><p><code class="ph codeph">CREATE bdef</code>: <code class="ph codeph">create</code> must be defined in the root view's part of the BDEF. See the details in the RAP BDL documentation for <a href="abenbdl_standard_operations.html">standard operations</a>.</p>
<p><code class="ph codeph">CREATE bdef\_assoc</code>: create-by-association operations are enabled by default for compositions even if not explicitly maintained. Yet, it is recommended that the <code class="ph codeph">create</code> operation for the respective association is included in the root view's or child view's part of the BDEF. A create-by-association operation cannot be carried out for a child entity if it is not explicitly maintained using the <code class="ph codeph">{ create; }</code> notation. For modifying external cross-BO associations that are not part of the composition, the <code class="ph codeph">{ create; }</code> notation must be explicitly maintained in the BDEF for the association. As a prerequisite, the behavior for the association <code class="ph codeph">_assoc</code> is maintained in another BDEF accordingly. See more details in the RAP BDL documentation for <a href="abenbdl_association.html">Operations for Associations</a>.</p></td>
<td><p><code class="ph codeph">CREATE bdef</code>:</p>
<p><code class="ph codeph">%cid</code></p>
<p><code class="ph codeph">%control</code></p>
<p><code class="ph codeph">%data</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">CREATE bdef\assoc</code>:</p>
<p><code class="ph codeph">%cid_ref</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%target</code></p>
<p><code class="ph codeph">%tky</code></p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">DELETE</code></td>
<td>Used for <a href="abapmodify_entity_entities_op.html"><code class="ph codeph">DELETE</code></a> operations.</td>
<td><code class="ph codeph">delete</code> must be defined in the root view's part of the BDEF. See the details in the RAP BDL documentation for <a href="abenbdl_standard_operations.html">Standard Operations</a>.</td>
<td><p><code class="ph codeph">%cid_ref</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">DETERMINATION</code></td>
<td>Used to specify the keys of RAP BO instances as input parameters in the context of determinations and their handler method implementations. The keys specify which RAP BO instances are to be respected for determinations.</td>
<td>The determination is specified in the BDEF. See the details in the RAP BDL documentation for <a href="abenbdl_determinations.html">Determinations</a>.</td>
<td><p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p>
<p><strong>Note:</strong> The access to determinations is not allowed outside of the implementation class.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">EVENT</code></td>
<td>Used with <a href="abapraise_entity_event.html"><code class="ph codeph">RAISE ENTITY EVENT</code></a> statements in the context of <a href="abenrap_entity_event_glosry.html">RAP entity events</a>.</td>
<td>The event <code class="ph codeph">evt</code> must be defined in a BDEF or <a href="abenrap_extension_glosry.html">BDEF extension</a> with or without parameters.</td>
<td><p><code class="ph codeph">%key</code></p>
<p>If the event is defined with parameters, <code class="ph codeph">%param</code> is available, too.</p></td>
</tr>
<tr class="even">
<td><p><code class="ph codeph">FAILED</code></p>
<p><code class="ph codeph">FAILED EARLY</code></p>
<p><code class="ph codeph">FAILED LATE</code></p></td>
<td><p>Used to specify <a href="abenrap_response_param_glosry.html">RAP response parameters</a>. In this case, it is used for information for identifying the data set for which an error occurred in a RAP operation.</p>
<p>The addition <code class="ph codeph">EARLY</code> or no addition is relevant in the context of the interaction phase. The addition <code class="ph codeph">LATE</code> is relevant in the context of the save phase.</p></td>
<td>In general, behavior must be defined for the entity in the BDEF.</td>
<td><p><strong>Note:</strong> The availability of the following components depends on the BDEF, that is, only a subset of the below components might be expected to be available.</p>
<p><code class="ph codeph">%action</code></p>
<p><code class="ph codeph">%assoc</code></p>
<p><code class="ph codeph">%cid</code></p>
<p><code class="ph codeph">%create</code></p>
<p><code class="ph codeph">%delete</code></p>
<p><code class="ph codeph">%fail</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%op</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p>
<p><code class="ph codeph">%update</code></p>
<p>In case of <code class="ph codeph">LATE</code>, the component <code class="ph codeph">%cid</code> is not available.</p></td>
</tr>
<tr class="odd">
<td><p><code class="ph codeph">FEATURES KEY</code></p>
<p><code class="ph codeph">INSTANCE FEATURES KEY</code></p></td>
<td><p>Used for retrieving <a href="abenbdl_actions_fc.html">instance feature control</a> information in the context of handler method implementations of ABAP EML <a href="abapget_permissions.html"><code class="ph codeph">GET PERMISSIONS</code></a> statements. The keys of RAP BO instances that have been specified serve as import parameters of the corresponding handler methods. The keys specify for which RAP BO instances feature control information is to be requested.</p>
<p>A specification with <code class="ph codeph">FEATURES KEY</code> is the same as with <code class="ph codeph">INSTANCE FEATURES KEY</code>.</p></td>
<td>The property <code class="ph codeph">features:instance</code> must be specified in the BDEF. See the subtopics in the RAP BDL documentation on the <a href="abenbdl_body.html">Entity Behavior Body</a> for those elements that can be specified with the property.</td>
<td><p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p></td>
</tr>
<tr class="even">
<td><p><code class="ph codeph">FEATURES RESULT</code></p>
<p><code class="ph codeph">INSTANCE FEATURES RESULT</code></p></td>
<td><p>Used for retrieving <a href="abenbdl_actions_fc.html">instance feature control</a> information in the context of handler method implementations of ABAP EML <a href="abapget_permissions.html"><code class="ph codeph">GET PERMISSIONS</code></a> statements. The result contains the outcome of the permission information retrieval for instance features based on the keys and request parameters.</p>
<p>A specification with <code class="ph codeph">FEATURES RESULT</code> is the same as with <code class="ph codeph">INSTANCE FEATURES RESULT</code>.</p></td>
<td>The property <code class="ph codeph">features:instance</code> must be specified in the BDEF. See the subtopics in the RAP BDL documentation on the <a href="abenbdl_body.html">entity behavior body</a> for those elements that can be specified with the property.</td>
<td><p><strong>Note:</strong> The availability of the following components depends on the BDEF, that is, only a subset of the below components might be expected to be available.</p>
<p><code class="ph codeph">%action</code></p>
<p><code class="ph codeph">%assoc</code></p>
<p><code class="ph codeph">%delete</code></p>
<p><code class="ph codeph">%features</code></p>
<p><code class="ph codeph">%field</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p>
<p><code class="ph codeph">%update</code></p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">FUNCTION IMPORT</code></td>
<td>Used to store the import parameters for <a href="abenbdl_function.html">functions</a>.</td>
<td>The function is specified in the BDEF. See the details in the RAP BDL documentation for <a href="abenbdl_function.html">Function</a>.</td>
<td><p><strong>Note</strong>: The availability of the following components depends on the context and defined function in the BDEF, that is, only a subset of the below components might be expected to be available.</p>
<p><code class="ph codeph">%cid</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%param</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">FUNCTION RESULT</code></td>
<td>Used to store the result for <a href="abenbdl_function.html">functions</a>.</td>
<td>Only available if the function has a result parameter specified in the BDEF. See the details in the RAP BDL documentation for <a href="abenbdl_function.html">function</a>.</td>
<td><p><strong>Note:</strong> The availability of the following components depends on the context and defined function in the BDEF, that is, only a subset of the below components might be expected to be available.</p>
<p><code class="ph codeph">%cid</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%param</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">HIERARCHY</code></td>
<td>Used for <a href="abenbdl_action_input_param.html"><code class="ph codeph">deep</code> input parameters</a> and <a href="abenbdl_action_output_para.html"><code class="ph codeph">deep</code> output parameters</a> in the context of deep <a href="abenrap_action_glosry.html">action</a> or <a href="abenrap_function_glosry.html">function</a> parameters. The type is only available for <a href="abencds_abstract_bdef_glosry.html">abstract BDEFs</a>.</td>
<td>Only available if behavior is defined for an abstract entity, i. e. the BDEF must be defined with <a href="abenbdl_bdef_abstract_header.html"><code class="ph codeph">with hierarchy;</code></a>. Furthermore, deep actions or functions must be defined in the non-abstract BDEFs with the additions <a href="abenbdl_action_input_param.html"><code class="ph codeph">deep parameter</code></a> (to interpret the input parameter as structure) or <a href="abenbdl_action_input_param.html"><code class="ph codeph">deep table parameter</code></a> (to interpret the input parameter as table).</td>
<td><p>The type comprises all entity fields plus, if available, a component for every <a href="abencds_composition_glosry.html">composition</a> that itself has subcomponents. All fields keep their original line type.</p>
<p>If the BDEF for the abstract entity includes behavior definitions for the compositions, the derived type contains further components: For a composition with cardinality &lt;= 1, this component is a structure; otherwise, the component is a table. If the behavior for an abstract entity is defined with the addition <a href="abenbdl_define_beh_abstract.html"><code class="ph codeph">with control</code></a>, the derived type also contains <a href="abapderived_types_comp.html"><code class="ph codeph">%control</code></a> as component. The components of <code class="ph codeph">%control</code> itself are comprised of all fields of the abstract entity and, as above and if available, structures or internal tables for compositions.</p>
<p>The subcomponents of the <a href="abapderived_types_param.html"><code class="ph codeph">%param</code></a> component in the context of deep action and function are typed with this BDEF derived type.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">KEY OF</code></td>
<td>Used, for example, to specify RAP BO instances that are to be locked in the context of the ABAP EML statement <a href="abapset_locks.html"><code class="ph codeph">SET LOCKS</code></a>. The nested tables of the structures that are typed with <a href="abaptype_request_for.html"><code class="ph codeph">TYPE REQUEST FOR DELETE</code></a> in the context of managed RAP BOs <a href="abenbdl_saving.html"><code class="ph codeph">with additional save</code></a> and <a href="abenbdl_saving.html"><code class="ph codeph">with unmanaged save</code></a> also use this type.</td>
<td>See the details in the RAP BDL documentation for <a href="abenbdl_locking.html">Locking</a> and <a href="abenbdl_saving.html"><code class="ph codeph">SavingOptions</code></a>.</td>
<td><p>The keys (not <code class="ph codeph">%key</code>).</p>
<p><strong>Note:</strong> <code class="ph codeph">%is_draft</code> and <code class="ph codeph">%pid</code> are not possible.</p></td>
</tr>
<tr class="odd">
<td><p><code class="ph codeph">MAPPED</code></p>
<p><code class="ph codeph">MAPPED EARLY</code></p>
<p><code class="ph codeph">MAPPED LATE</code></p></td>
<td><p>Used to specify <a href="abenrap_response_param_glosry.html">RAP response parameters</a>. In this case, it is used to provide mapping information on <a href="abenrap_bo_instance_glosry.html">RAP BO instances</a>, for example, which key values were created for given content IDs (<a href="abapderived_types_cid.html"><code class="ph codeph">%cid</code></a>).</p>
<p>The addition <code class="ph codeph">EARLY</code> or no addition is relevant in the context of the interaction phase. The addition <code class="ph codeph">LATE</code> is relevant in the context of the save phase. See more details in the documentation for <a href="abapeml_response.html"><code class="ph codeph">response_param</code></a>.</p></td>
<td>In general, behavior must be defined for the entity in the BDEF.</td>
<td><p>The availability of the following components depends on the context and defined function in the BDEF, that is, only a subset of the below components might be expected to be available.</p>
<p>Components of a table typed without an addition or with the addition <code class="ph codeph">EARLY</code>:</p>
<p><code class="ph codeph">%cid</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pid</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p>
<p>Components of a table typed with the addition <code class="ph codeph">LATE</code>:</p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pid</code></p>
<p><code class="ph codeph">%pre</code></p>
<p><code class="ph codeph">%tmp</code></p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">PERMISSIONS KEY</code></td>
<td>Used for specifying the keys of RAP BO instances in the context of ABAP EML <a href="abapget_permissions.html"><code class="ph codeph">GET PERMISSIONS</code></a> statements. The keys of RAP BO instances are specified to define for which RAP BO instances permission information is to be requested. The keys serve then as import parameters for the corresponding handler methods <a href="abapget_permissions.html"><code class="ph codeph">GET PERMISSIONS</code></a> statements.</td>
<td></td>
<td><p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">READ CHANGES</code></td>
<td>Used to type read results in ABAP EML <code class="ph codeph">READ</code> statements using the <a href="abapeml_read_with_changes.html"><code class="ph codeph">WITH CHANGES</code></a> addition.</td>
<td></td>
<td>Same as <code class="ph codeph">READ RESULT</code> including <a href="abapderived_types_chg.html"><code class="ph codeph">%chg</code></a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">READ IMPORT</code></td>
<td>Used to import RAP BO instances in <a href="abapread_entity_entities_op.html"><code class="ph codeph">READ</code></a> and read-by-association (<a href="abapread_entity_entities_op.html"><code class="ph codeph">READ BY</code></a>) operations.</td>
<td><p><code class="ph codeph">READ bdef</code>: Read operations are enabled by default for compositions and cannot be deactivated.</p>
<p><code class="ph codeph">READ bdef\_assoc</code>: Read-by-association operations are enabled by default for compositions even if not explicitly maintained. Yet, it is recommended <code class="ph codeph">association _assoc;</code> is used. Reading from cross-BO associations, which are not part of the composition tree, must be explicitly enabled in the BDEF using an <code class="ph codeph">association</code> notation.</p></td>
<td><p><code class="ph codeph">%control</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">READ LINK</code></td>
<td>Used to return the primary keys of root and associated entities within a composition tree in <a href="abapread_entity_entities_op.html"><code class="ph codeph">READ</code></a> and read-by-association (<a href="abapread_entity_entities_op.html"><code class="ph codeph">READ BY</code></a>) operations.</td>
<td><code class="ph codeph">READ bdef\_assoc</code>: Read-by-association operations are enabled by default for compositions even if not explicitly maintained. Yet, it is recommended that <code class="ph codeph">association _assoc;</code> s used. Reading from cross-BO associations, which are not part of the composition tree, must be explicitly enabled in the BDEF using an <code class="ph codeph">association</code> notation.</td>
<td>Structure <code class="ph codeph">source</code> containing <code class="ph codeph">%key</code>/<code class="ph codeph">%pky</code>/<code class="ph codeph">%tky</code> of the source entity, and structure <code class="ph codeph">target</code> containing <code class="ph codeph">%key</code>/<code class="ph codeph">%pky</code>/<code class="ph codeph">%tky</code> of the associated entity.</td>
</tr>
<tr class="even">
<td><code class="ph codeph">READ RESULT</code></td>
<td>Used to return successfully read RAP BO instances in <a href="abapread_entity_entities_op.html"><code class="ph codeph">READ</code></a> and read-by-association (<a href="abapread_entity_entities_op.html"><code class="ph codeph">READ BY</code></a>) operations.</td>
<td><p><code class="ph codeph">READ bdef</code>: Read operations are enabled by default for compositions and cannot be deactivated.</p>
<p><code class="ph codeph">READ bdef\_assoc</code>: Read-by-association operations are enabled by default for compositions even if not explicitly maintained. Yet, it is recommended that <code class="ph codeph">association _assoc;</code> is used. Reading from cross-BO associations that are not part of the composition tree must be explicitly enabled in the BDEF using an <code class="ph codeph">association</code> notation.</p></td>
<td><p><code class="ph codeph">%data</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p></td>
</tr>
<tr class="odd">
<td><p><code class="ph codeph">REPORTED</code></p>
<p><code class="ph codeph">REPORTED EARLY</code></p>
<p><code class="ph codeph">REPORTED LATE</code></p></td>
<td><p>Used to specify <a href="abenrap_response_param_glosry.html">RAP response parameters</a>. In this case, it is used to exchange messages, for example, error messages, for each entity defined in the BDEF and not related to a specific entity.</p>
<p>The addition <code class="ph codeph">EARLY</code> or no addition is relevant in the context of the interaction phase. The addition <code class="ph codeph">LATE</code> is relevant in the context of the save phase. See more details in the documentation for <a href="abapeml_response.html"><code class="ph codeph">response_param</code></a>.</p></td>
<td>In general, behavior must be defined for the entity in the BDEF.</td>
<td><p><code class="ph codeph">%action</code></p>
<p><code class="ph codeph">%cid</code></p>
<p><code class="ph codeph">%create</code></p>
<p><code class="ph codeph">%element</code></p>
<p><code class="ph codeph">%delete</code></p>
<p><code class="ph codeph">%global</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%msg</code></p>
<p><code class="ph codeph">%op</code></p>
<p><code class="ph codeph">%path</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%state_area</code></p>
<p><code class="ph codeph">%tky</code></p>
<p><code class="ph codeph">%update</code></p>
<p>In case of <code class="ph codeph">LATE</code>, the component <code class="ph codeph">%cid</code> is not available.</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">UPDATE</code></td>
<td>Used for <a href="abapmodify_entity_entities_op.html"><code class="ph codeph">UPDATE</code></a> operations.</td>
<td><code class="ph codeph">update</code> must be defined in the root view's part of the BDEF. See the details in the RAP BDL documentation for <a href="abenbdl_standard_operations.html">standard operations</a>.</td>
<td><p><code class="ph codeph">%cid_ref</code></p>
<p><code class="ph codeph">%control</code></p>
<p><code class="ph codeph">%data</code></p>
<p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">VALIDATION</code></td>
<td>Used to specify the keys of RAP BO instances as input parameters in the context of validations and their handler method implementations. The keys specify which RAP BO instances are to be considered for validations.</td>
<td>The validation is specified in the BDEF. See the details in the RAP BDL documentation for <a href="abenbdl_validations.html">Validations</a>.</td>
<td><p><code class="ph codeph">%key</code></p>
<p><code class="ph codeph">%pky</code></p>
<p><code class="ph codeph">%tky</code></p>
<p><strong>Note:</strong> The access to validations is not allowed outside of the implementation class.</p></td>
</tr>
</tbody>
</table>

## Executable Examples

- The example Display BDEF Derived Type Components allows you to explore the various BDEF derived type components and their availability in variables type with [`TYPE TABLE FOR ...`](abaptype_table_for.md) and `TYPE STRUCTURE FOR ...`. The program makes use of three different RAP scenarios: [RAP external numbering](../../abap-glossary/abenrap_ext_numbering_glosry.md), [`late numbering`](../rap-behavior-definitions/abenbdl_late_numbering.md) and [draft](../rap-behavior-definitions/abenbdl_with_draft.md).

- The type `TYPE STRUCTURE FOR CHANGE` is demonstrated in the following examples:

  - [ABAP EML - `TYPE REQUEST FOR` in a managed RAP BO with additional save](abenrap_additional_save_abexa.md): Uses a managed RAP BO whose BDEF is specified with `with additional save`.

  - [ABAP EML - `TYPE REQUEST FOR` in a managed RAP BO with unmanaged save](abenrap_managed_unm_save_abexa.md): Uses a simple managed RAP BO whose BDEF is specified with `with unmanaged save`.

- The type `TYPE STRUCTURE FOR HIERARCHY` is demonstrated in the example [Using `TYPE TABLE`/`TYPE STRUCTURE FOR HIERARCHY`](abenderived_type_hierarchy_abexa.md).
