---
title: "CONVERT KEY"
source_file: abapconvert_key.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CONVERT KEY

## Syntax

``` abap
CONVERT KEY OF [bdef|(bdef)] 
  FROM [TEMPORARY] pre_key 
  TO final_key.  
```

## Description

Used to retrieve the final keys (`final_key`) from preliminary keys (`pre_key`) in the context of [RAP late numbering](../../abap-glossary/abenrap_late_numbering_glosry.md).

Outside of [RAP behavior implementations](../../abap-glossary/abenbehavior_implement_glosry.md), [transaction owners](../../abap-glossary/abentransaction_owner_glosry.md) can only specify `CONVERT KEY` statements between `COMMIT ENTITIES BEGIN ... COMMIT ENTITIES END.` statements.

Within behavior implementations, `CONVERT KEY` statements are specified without `COMMIT ENTITIES BEGIN... COMMIT ENTITIES END.` statements in [RAP saver methods](../../abap-glossary/abenabp_saver_method_glosry.md) when accessing other RAP BOs that specify late numbering to retrieve their final keys. Typically, use the `CONVERT KEY` statements in the `save` or `save_modified` methods. Use this statement in `adjust_numbers` only if the business objects' saving order in the save sequence is guaranteed. For example, in the implementation of `adjust_numbers` for BO *B*, you can specify `CONVERT KEY` for BO *A* if *B* follows *A* in the save sequence. Ensure *A* is identified as the predecessor of *B*, either by declaring a dependent BO or explicitly stating [`save after`](../rap-behavior-definitions/abenbdl_save_after.md) in the BDEF.

Details on the syntax elements:

<table>
<thead>
<tr class="header">
<th><strong>Syntax Elements</strong></th>
<th><strong>Details</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">CONVERT KEY OF bdef ...</code></td>
<td><p>Specifies the <a href="abenrap_bo_entity_glosry.html">RAP BO entity</a> <code class="ph codeph">bdef</code> for which the keys should be converted. The entity name can also be specified dynamically within a pair of parentheses. The entity name must be compatible with <code class="ph codeph">ABP_ENTITY_NAME</code>.</p>
<p>Unlike other EML statements, the <code class="ph codeph">CONVERT KEY OF</code> statement does not operate on mass data, i. e. internal tables, but on single values (<code class="ph codeph">pre_key</code>, <code class="ph codeph">final_key</code>).</p></td>
</tr>
<tr class="even">
<td><code class="ph codeph">... FROM [TEMPORARY] pre_key ...</code></td>
<td><p>Specifies the value of the preliminary key <code class="ph codeph">pre_key</code>. The type of <code class="ph codeph">pre_key</code> must be compatible with <a href="abapderived_types_pid.html"><code class="ph codeph">%pid</code></a> or <a href="abapderived_types_pre.html"><code class="ph codeph">%pre</code></a> in case of using the addition <code class="ph codeph">TEMPORARY</code>.</p>
<p>The optional addition <code class="ph codeph">TEMPORARY</code> is only relevant in late numbering scenarios in which <code class="ph codeph">%pre</code> is used to contain the preliminary keys during the <a href="abenrap_int_phase_glosry.html">RAP interaction phase</a> - instead of <a href="abapderived_types_pid.html"><code class="ph codeph">%pid</code></a>.</p>
<p>For more information on the use of <code class="ph codeph">%pid</code>, <code class="ph codeph">%pre</code> and <code class="ph codeph">%key</code> in the context of late numbering scenarios, see the topic <a href="abapderived_types_keys_identifiers.html">Using Keys and Identifying RAP BO Instances in a Nutshell</a>.</p></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">... TO final_key.</code></td>
<td><code class="ph codeph">final_key</code> specifies the final key value. The type of <code class="ph codeph">final_key</code> must be compatible with the primary key's type. You can use a structure of type <a href="abaptype_structure_for.html"><code class="ph codeph">TYPE STRUCTURE FOR KEY</code></a>, especially when specifying the entity dynamically.</td>
</tr>
</tbody>
</table>

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_EML_COMMIT_3` demonstrates the `COMMIT ENTITIES BEGIN ... END` variant and `CONVERT KEY OF`.

``` abap
DATA: mapped_early TYPE RESPONSE FOR MAPPED EARLY 
        demo_umanaged_root_late_num. 
 
COMMIT ENTITIES BEGIN. 
 
  LOOP AT mapped_early-demo_umanaged_root_late_num 
    ASSIGNING FIELD-SYMBOL(<mapped_early>). 
 
    CONVERT KEY OF demo_umanaged_root_late_num 
      FROM <mapped_early>-%pid 
      TO FINAL(lv_root_key). 
 
  ENDLOOP. 
 
COMMIT ENTITIES END.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section taken from `CL_DEMO_RAP_DRVD_TYPES_LATENU2` demonstrates the `COMMIT ENTITIES BEGIN ... END` variant and `CONVERT KEY OF` with the addition `TEMPORARY`.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    DATA: 
 
      mapped_early TYPE RESPONSE FOR MAPPED EARLY 
                   demo_umanaged_root_late_num3. 
 
    METHODS main. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
 
  METHOD main. 
    ... 
    COMMIT ENTITIES BEGIN RESPONSES FAILED DATA(failed_late) 
         REPORTED DATA(reported_late). 
    ... 
    LOOP AT mapped_early-demo_umanaged_root_late_num3 
      ASSIGNING FIELD-SYMBOL(<mapped_early>). 
 
      CONVERT KEY OF demo_umanaged_root_late_num3 
        FROM TEMPORARY VALUE #( %pid = <mapped_early>-%pid 
                                %tmp = <mapped_early>-%key ) 
        TO DATA(lv_final_key). 
    ENDLOOP. 
    ... 
    COMMIT ENTITIES END. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Executable Examples

- The example [`COMMIT ENTITIES BEGIN`, `END` with `CONVERT KEY OF`](abencommit_entities_beginend_abexa.md) demonstrates the use of this `COMMIT ENTITIES` statement including `CONVERT KEY OF`.

- The example [Using `%pre` / `%tmp`](abenderived_types_pre_tmp_abexa.md) demonstrates the use of `%pre` and `%tmp` with an [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) in a [`late numbering`](../rap-behavior-definitions/abenbdl_late_numbering.md) scenario. In this context, a `COMMIT ENTITIES` statement including `CONVERT KEY OF` with the addition `TEMPORARY` is used.
