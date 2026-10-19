---
title: "%pid"
source_file: abapderived_types_pid.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > BDEF Derived Types > Components of BDEF Derived Types > Components Related to Keys and RAP BO Instance Identification"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# %pid

## Use

`%pid` is a component of [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) and of type `ABP_BEHV_PID`. It is used as a preliminary ID for [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) and only available if [late numbering](../rap-behavior-definitions/abenbdl_late_numbering.md) is defined in the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md). In the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md), `%pid` is transformed to the final key values.

Regarding `%pid` in the ...

- [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md):

  - `%pid` is assigned as a temporary identifier for [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) in the [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) for [create operations](abapmodify_entity_entities_op.md).

  - In these methods, [`%cid`](abapderived_types_cid.md) must be mapped to `%pid` in the [RAP response parameter](../../abap-glossary/abenrap_response_param_glosry.md) `mapped`.

- [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md):

  - To assign the final key values to the instances, the method [`adjust_numbers`](abensaver_adjust_numbers.md) is called before the actual saving happens with the [`save`](abensaver_method_save.md) method. The `adjust_numbers` method transforms `%pid` into the final key values.

Regarding the RAP BO instance identification in late numbering scenarios:

- In contrast to `%pid`, `%cid` and [`%cid_ref`](abapderived_types_cid_ref.md) are only available on a short-term basis for the current ABAP EML request within the RAP interaction phase. They are no longer available in the RAP save sequence whereas `%pid` is indeed available there as the unique identifier for an instance. `%pid` is then transformed into the final keys in the RAP saver method `adjust_numbers`. Hence, `%pid` serves as a long-term and stable ID until the final key creation which can happen at a later point in time after the instance has been created. For example, in case of a [draft](../rap-behavior-definitions/abenbdl_with_draft.md) scenario, the final key value creation can be days or weeks after the creation of an instance.

- Apart from using `%cid` or `%cid_ref`, the instance identification from a RAP consumer's point of view can also be done using `%pid` or, as it is recommended, the [component group](../../abap-glossary/abencomponent_group_glosry.md) [`%tky`](abapderived_types_tky.md) which includes `%pid` and more (for example, [`%key`](abapderived_types_key.md) if `%key` is to be used for containing the preliminary key instead of `%pid`).

**Where used**

- `%pid` occurs in late numbering scenarios only. It is not available in static actions and functions, `TYPE TABLE FOR KEY OF` or `TYPE STRUCTURE FOR KEY OF`. In case of create operations, `%cid` must be mapped to a created `%pid`. Both must be inserted in the [`mapped`](abaptype_response_for.md) response parameter.

- A RAP BO instance must always be identifiable uniquely by its transactional key (`%tky`) for internal processing during the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md). However, in case of late numbering scenarios, instances are identified using preliminary keys in the interaction phase and the early phase of the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md) before the [`save`](abensaver_method_save.md) method is called. The final key value assignment only takes place in the [`adjust_numbers`](abensaver_adjust_numbers.md) method. Therefore, the transactional key `%tky` also includes the preliminary ID `%pid` in late numbering scenarios to ensure the uniqueness also during more than one ABAP session, for example, in draft scenarios. Apart from `%pid`, `%tky` also includes `%key`. Depending on your use case, `%key` can also be used as a preliminary identifier by filling the key values with values that are only temporarily valid and transformed into the final keys not until the `adjust_numbers` method. That means you can either use `%pid` or `%key` as preliminary identifiers and leave the other one initial, or you use both of them in combination for uniquely identifying RAP BO instances. In any case, the component group `%tky` must in total uniquely identify the instance.

## Hints

- If `late numbering` is specified in the [RAP BO root entity](../../abap-glossary/abenrap_bo_root_entity_glosry.md), then `late numbering` is inherited by the composition tree. Consequently, `%pid` components must also be reflected in the hierarchy of RAP BO instances and non-composition associations before finally setting the keys.

- `%pid` is contained in the component groups `%tky` and [`%pky`](abapderived_types_pky.md) (while `%pky` itself is a component of `%tky`).

## More Information

[Using Keys and Identifying RAP BO Instances in a Nutshell](abapderived_types_keys_identifiers.md)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code section is taken from here: `BP_DEMO_UMANAGED_ROOT_LATE_NUMCCIMP`. The global class of the [behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is `BP_DEMO_UMANAGED_ROOT_LATE_NUM`. The code example demonstrates the component `%pid` in the context of a `create` method that is responsible for creating `%pid` and mapping it to [`%cid`](abapderived_types_cid.md) in an unmanaged scenario. See the executable program for this example in the topic [Using `%pid`](abenderived_types_pid_abexa.md).

``` abap
METHOD create. 
 
  LOOP AT entities ASSIGNING FIELD-SYMBOL(<entity>). 
    "Create %pid. 
    DATA(system_uuid) = cl_uuid_factory=>create_system_uuid( ). 
    TRY. 
        DATA(uuid_x16) = system_uuid->create_uuid_x16( ). 
        system_uuid->convert_uuid_x16( EXPORTING 
                                         uuid = uuid_x16 
                                       IMPORTING 
                                         uuid_c22 = DATA(uuid_c22) 
                                         uuid_c26 = DATA(uuid_c26) 
                                         uuid_c32 = DATA(uuid_c32) ). 
      CATCH cx_uuid_error. 
        APPEND VALUE #( %cid = <entity>-%cid ) 
                      TO failed-demo_umanaged_root_late_num. 
    ENDTRY. 
 
    "Insert values into unmanaged transactional buffer 
    APPEND VALUE #( 
    cid                = <entity>-%cid 
    pid                = uuid_x16 
    instance-key_field = <entity>-key_field 
    instance-field1    = COND #( WHEN <entity>-%control-field1 
                                   NE if_abap_behv=>mk-off 
                                 THEN <entity>-field1 ) 
    instance-field2    = COND #( WHEN <entity>-%control-field2 
                                   NE if_abap_behv=>mk-off 
                                 THEN <entity>-field2 ) 
    instance-field3    = COND #( WHEN <entity>-%control-field3 
                                   NE if_abap_behv=>mk-off 
                                 THEN <entity>-field3 ) 
    instance-field4    = COND #( WHEN <entity>-%control-field4 
                                   NE if_abap_behv=>mk-off 
                                 THEN <entity>-field4 ) 
    changed            = abap_true 
    deleted            = abap_false ) TO lcl_buffer=>root_buffer. 
 
    "Insert mapping information 
    APPEND VALUE #( %pid = uuid_x16 
                    %cid = <entity>-%cid 
                    %key = <entity>-%key ) 
                    TO mapped-demo_umanaged_root_late_num. 
 
  ENDLOOP. 
ENDMETHOD.
```

## Executable Examples

- The example [Using `%pid`](abenderived_types_pid_abexa.md) demonstrates the use of `%pid` with an unmanaged RAP BO in a late numbering scenario.

- The example [Using `%pre` / `%tmp`](abenderived_types_pre_tmp_abexa.md) also touches upon the use of `%pid`.
