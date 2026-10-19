---
title: "RAP Calculator: Managed, Draft-Enabled RAP BO with Late Numbering"
source_file: abensheet_rap_calc_dr_ln_m_abexa.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > Other RAP-Related ABAP Language Elements and Topics > RAP Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP Calculator: Managed, Draft-Enabled RAP BO with Late Numbering

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example represents a calculator using RAP concepts, i. e. using ABAP EML in the context of a [managed](../../abap-glossary/abenmanaged_rap_bo_glosry.md) and [draft-enabled](../../abap-glossary/abendraft_rap_bo_glosry.md) RAP business object with [RAP late numbering](../../abap-glossary/abenrap_late_numbering_glosry.md) to carry out simple calculations. Here, a [RAP BO instance](../../abap-glossary/abenrap_bo_instance_glosry.md) consists of a calculation ID (which is the key that is finally set not until the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md)), two operands (having integer values), the arithmetic operator and the result plus other draft-related fields.

**Data model**

The CDS data model consists of the root entity `DEMO_CS_RAP_DRAFT_M`:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED

@ObjectModel.semanticKey: ['id']
@UI: { headerInfo: { title: { value: 'id' },
       typeName: 'Calculation', typeNamePlural: 'Calculations' } }
define root view entity DEMO_CS_RAP_DRAFT_M
  as select from demo_cs_tab_calc
  {
        //FACET SECTION
        @UI.facet: [

        // Header Facet (Object Page):

        { id:              'HeaderFacet',
          purpose:         #HEADER,
          type:            #FIELDGROUP_REFERENCE,
          //label:           'Calculation ID',
          targetQualifier: 'Fieldgroup:HeaderItems',
          position:        10 },

        // Body Facets (Object Page)

        { id:       'Calculation',
          type:     #IDENTIFICATION_REFERENCE,
          label:    'Calculation',
          position: 10 }

        ]

         // Element List
    @EndUserText.label: 'Calculation ID'
    @UI: { lineItem: [ { importance: #HIGH, position: 10, 
                         label: 'Calculation ID' },
                     { type: #FOR_ACTION, dataAction: 'delete_all', 
                       label: 'Delete All Persisted Calculations' } ],
           fieldGroup: [ { qualifier: 'Fieldgroup:HeaderItems', 
                           position: 10 } ] }
    key id,
        @UI: { lineItem:       [ { importance: #HIGH, position: 20, 
                                   label: '1st Operand' } ],
               identification: [ { position: 20, 
                                   label: '1st Operand' } ],
               fieldGroup:     [ { qualifier: 'CaluclationItems', 
                                   position: 10 } ] }
        num1,
        @UI: { lineItem:       [ { importance: #HIGH, position: 30, 
                                   label: 'Operator' } ],
               identification: [ { position: 30, label: 'Operator' } ],
               fieldGroup:     [ { qualifier: 'CaluclationItems', 
                                   position: 20 } ] }
        arithm_op,
        @UI: { lineItem:       [ { importance: #HIGH, position: 40, 
                                   label: '2nd Operand' } ],
               identification: [ { position: 40, 
                                   label: '2nd Operand' } ],
               fieldGroup:     [ { qualifier: 'CaluclationItems', 
                                   position: 30 } ] }
        num2,
        @UI: { lineItem:       [ { importance: #HIGH, position: 50, 
                                   label: 'Result' } ],
               identification: [ { position: 50, label: 'Result' } ],
               fieldGroup:     [ { qualifier: 'CaluclationItems', 
                                   position: 40 } ] }
        calc_result,
        @UI: { hidden: true }
        @Semantics.systemDateTime.lastChangedAt: true
        crea_date_time,
        @EndUserText.label: 'Last Changed At'
        @UI: { fieldGroup:     [ { qualifier: 'Fieldgroup:HeaderItems', 
                                   position: 20 } ] }
        @Semantics.systemDateTime.localInstanceLastChangedAt: true
        lchg_date_time
  }
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_CS_RAP_DRAFT_M` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_cs_rap_draft_m unique;
strict ( 2 );
with draft;

define behavior for DEMO_CS_RAP_DRAFT_M alias calc
persistent table demo_cs_tab_calc
draft table demo_cs_drafttab
lock master
total etag crea_date_time
etag master lchg_date_time
authorization master ( none )
late numbering
{
  create;
  update;
  delete;
  field ( readonly ) id, calc_result, crea_date_time, lchg_date_time;
  field ( mandatory ) num1, num2, arithm_op;
  static action delete_all;
  internal action calculation;
  validation validate on save { create; field num1, arithm_op, num2; }
  determination det_modify on modify { field num1, num2, arithm_op; }
  draft action Resume;
  draft action Edit;
  draft action Activate optimized;
  draft action Discard;
  draft determine action Prepare
  {
    validation validate;
  }
}
```

**Behavior implementation**

For the above RAP behavior definition, one [ABP](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_CS_RAP_DRAFT_M`. The actual behavior implementation takes place in local classes that are defined and implemented in the `BP_DEMO_CS_RAP_DRAFT_M========CCIMP` of the behavior pool. See comments in the code for more information on the implementation.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_cs_rap_draft_ln_m DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      activate_tab  TYPE TABLE FOR ACTION IMPORT 
                      demo_cs_rap_draft_m~activate, 
      activate_tab2 TYPE TABLE FOR ACTION IMPORT 
                      demo_cs_rap_draft_m~activate, 
      activate_tab3 TYPE TABLE FOR ACTION IMPORT 
                      demo_cs_rap_draft_m~activate, 
      edit_tab      TYPE TABLE FOR ACTION IMPORT 
                      demo_cs_rap_draft_m~edit, 
      read_tab      TYPE TABLE FOR READ IMPORT demo_cs_rap_draft_m, 
      f             TYPE RESPONSE FOR FAILED demo_cs_rap_draft_m, 
      r             TYPE RESPONSE FOR REPORTED demo_cs_rap_draft_m, 
      m             TYPE RESPONSE FOR MAPPED demo_cs_rap_draft_m. 
    METHODS: 
      initialize_dbtabs. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cs_rap_draft_ln_m IMPLEMENTATION. 
  METHOD main. 
 
    out->begin_section( `RAP Demo: RAP Calculator Using Managed, ` && 
                      `Draft-Enabled RAP BO (Late Numbering)` ). 
 
    out->line( 
      )->next_section( `1) Creating Instances and ` && 
                       `Saving to the database` ). 
 
    "Creating instances; draft indicator %is_draft is enabled 
    MODIFY ENTITY demo_cs_rap_draft_m 
     CREATE AUTO FILL CID 
     FIELDS ( num1 arithm_op num2 ) 
     WITH VALUE #( 
        ( %is_draft = if_abap_behv=>mk-on 
          num1 = 1 arithm_op = '+' num2 = 2 ) 
        ( %is_draft = if_abap_behv=>mk-on 
          num1 = 2 arithm_op = '*' num2 = 4 ) 
        ( %is_draft = if_abap_behv=>mk-on 
          num1 = 3 arithm_op = '-' num2 = 5 ) 
        ( %is_draft = if_abap_behv=>mk-on 
          num1 = 1 arithm_op = '/' num2 = 4 ) 
        ( %is_draft = if_abap_behv=>mk-on 
          num1 = 2 arithm_op = 'P' num2 = 5 ) ) 
        FAILED f 
        REPORTED r 
        MAPPED m. 
 
    "Displaying responses only if FAILED and REPORTED 
    "response parameters are not initial 
    IF f IS NOT INITIAL OR r IS NOT INITIAL. 
      out->write_html( `<b>Responses after MODIFY operation</b>` ). 
 
      IF m IS NOT INITIAL. 
        out->write( m ). 
      ENDIF. 
 
      IF f IS NOT INITIAL. 
        out->write( f ). 
      ENDIF. 
 
      IF r IS NOT INITIAL. 
        out->write( r ). 
      ENDIF. 
 
    ENDIF. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    "Retrieving draft table entries 
    SELECT id, num1, arithm_op, num2, calc_result, crea_date_time, 
           lchg_date_time, draftentitycreationdatetime, 
           draftentitylastchangedatetime 
     FROM demo_cs_drafttab 
     ORDER BY id 
     INTO TABLE @DATA(draft_parent_before_act). 
 
    "Retrieving database table entries 
    SELECT id, num1, arithm_op, num2, calc_result, crea_date_time, 
           lchg_date_time 
     FROM demo_cs_tab_calc 
     ORDER BY id 
     INTO TABLE @DATA(db_tab_root_before_act). 
 
    "Filling the derived type for the ACTIVATE method by 
    "getting %pid values 
    LOOP AT m-calc 
      ASSIGNING FIELD-SYMBOL(<fs>). 
      APPEND VALUE #( %pid = <fs>-%pid ) 
                             TO activate_tab. 
 
    ENDLOOP. 
 
    MODIFY ENTITY demo_cs_rap_draft_m 
      EXECUTE activate AUTO FILL CID WITH activate_tab 
      MAPPED m 
      FAILED f 
      REPORTED r. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    "Retrieving draft table entries 
    SELECT id, num1, arithm_op, num2, calc_result, crea_date_time, 
           lchg_date_time, draftentitycreationdatetime, 
           draftentitylastchangedatetime 
     FROM demo_cs_drafttab 
     ORDER BY id 
     INTO TABLE @DATA(draft_parent_afer_act). 
 
    "Retrieving database table entries 
    SELECT id, num1, arithm_op, num2, calc_result, crea_date_time, 
           lchg_date_time 
     FROM demo_cs_tab_calc 
     ORDER BY id 
     INTO TABLE @DATA(db_tab_root_after_act). 
 
    "Displaying entries 
    out->write_html( `<b>a) Draft and database tables before ` && 
                   `ACTIVATE action</b>` 
      )->write( data = draft_parent_before_act exclude = `client` 
                name = 'Draft table before activation' 
      )->write( data = db_tab_root_before_act exclude = `client` 
                name = 'Database table before activation' ). 
 
    out->write_html( `<b>b) Draft and database tables after ` && 
                   `ACTIVATE action</b>` 
      )->write( data = draft_parent_afer_act exclude = `client` 
                name = 'Draft table after activation' 
      )->write( data = db_tab_root_after_act exclude = `client` 
                name = 'Database table after activation' 
      ). 
 
********************************************************************** 
 
    out->line( 
          )->next_section( `2) Creating Invalid Instances` ). 
 
 
    "Purposely creating invalid instances; 
    "draft indicator %is_draft is enabled 
    MODIFY ENTITY demo_cs_rap_draft_m 
     CREATE AUTO FILL CID 
     FIELDS ( num1 arithm_op num2 ) 
     WITH VALUE #( 
        ( %is_draft = if_abap_behv=>mk-on 
          num1 = 1 arithm_op = 'a' num2 = 1 )  "wrong operator 
        ( %is_draft = if_abap_behv=>mk-on 
          num1 = 1 arithm_op = '/' num2 = 0 ) "0 division 
        ( %is_draft = if_abap_behv=>mk-on 
          num1 = 2 arithm_op = 'P' num2 = 12345 ) ) "arithmetic overflow 
        FAILED f 
        REPORTED r 
        MAPPED m. 
 
    "Displaying responses only if FAILED and REPORTED 
    "response parameters are not initial. 
    IF f IS NOT INITIAL OR r IS NOT INITIAL. 
      out->write_html( `<b>Responses after MODIFY operation</b>` ). 
 
      IF m IS NOT INITIAL. 
        out->write( m ). 
      ENDIF. 
 
      IF f IS NOT INITIAL. 
        out->write( f ). 
      ENDIF. 
 
      IF r IS NOT INITIAL. 
        out->write( r ). 
      ENDIF. 
 
    ENDIF. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    "Retrieving draft table entries 
    SELECT id, num1, arithm_op, num2, calc_result, crea_date_time, 
           lchg_date_time, draftentitycreationdatetime, 
           draftentitylastchangedatetime 
     FROM demo_cs_drafttab 
     ORDER BY id 
     INTO TABLE @draft_parent_before_act. 
 
    "Retrieving database table entries 
    SELECT id, num1, arithm_op, num2, calc_result, crea_date_time, 
           lchg_date_time 
     FROM demo_cs_tab_calc 
     ORDER BY id 
     INTO TABLE @db_tab_root_before_act. 
 
    "Filling the derived type for the ACTIVATE method by 
    "getting %pid values; here, another table is filled for later use 
    LOOP AT m-calc 
      ASSIGNING FIELD-SYMBOL(<fs2>). 
 
      APPEND VALUE #( %pid = <fs2>-%pid ) 
                             TO activate_tab2. 
 
      APPEND VALUE #( %pid = <fs2>-%pid ) 
                             TO activate_tab3. 
    ENDLOOP. 
 
    MODIFY ENTITY demo_cs_rap_draft_m 
      EXECUTE activate AUTO FILL CID WITH activate_tab2 
      MAPPED m 
      FAILED f 
      REPORTED r. 
 
    "Displaying responses only if FAILED and REPORTED 
    "response parameters are not initial. 
    IF f IS NOT INITIAL OR r IS NOT INITIAL. 
      out->write_html( `<b>Responses after MODIFY operation</b>` ). 
 
      IF m IS NOT INITIAL. 
        out->write( m ). 
      ENDIF. 
 
      IF f IS NOT INITIAL. 
        out->write( f ). 
      ENDIF. 
 
      IF r IS NOT INITIAL. 
        out->write( r ). 
      ENDIF. 
 
    ENDIF. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    "Retrieving draft table entries 
    SELECT id, num1, arithm_op, num2, calc_result, crea_date_time, 
           lchg_date_time, draftentitycreationdatetime, 
           draftentitylastchangedatetime 
     FROM demo_cs_drafttab 
     ORDER BY id 
     INTO TABLE @draft_parent_afer_act. 
 
    "Retrieving database table entries 
    SELECT id, num1, arithm_op, num2, calc_result, crea_date_time, 
           lchg_date_time 
     FROM demo_cs_tab_calc 
     ORDER BY id 
     INTO TABLE @db_tab_root_after_act. 
 
    "Displaying entries 
    out->write_html( `<b>a) Draft and database tables before ` && 
                   `ACTIVATE action</b>` 
      )->write( data = draft_parent_before_act exclude = `client` 
                name = 'Draft table before activation' 
      )->write( data = db_tab_root_before_act exclude = `client` 
                name = 'Database table before activation' ). 
 
    out->write_html( `<b>b) Draft and database tables after ` && 
                   `ACTIVATE action</b>` 
      )->write( data = draft_parent_afer_act exclude = `client` 
                name = 'Draft table after activation' 
      )->write( data = db_tab_root_after_act exclude = `client` 
                name = 'Database table after activation' 
      ). 
 
 
********************************************************************** 
 
    out->line( 
    )->next_section( `3) Correcting and Updating Invalid Instances` ). 
 
    "Preparing the derived type for the read operation to 
    "retrieve the field values; the draft indicator is enabled 
    LOOP AT activate_tab3 ASSIGNING FIELD-SYMBOL(<fs3>). 
 
      APPEND VALUE #( %pky = <fs3>-%pky 
                      %is_draft = if_abap_behv=>mk-on 
                      %control-id = if_abap_behv=>mk-on 
                      %control-num1 = if_abap_behv=>mk-on 
                      %control-arithm_op = if_abap_behv=>mk-on 
                      %control-num2 = if_abap_behv=>mk-on 
                      %control-calc_result = if_abap_behv=>mk-on 
                      %control-crea_date_time = if_abap_behv=>mk-on 
                      %control-lchg_date_time = if_abap_behv=>mk-on 
                    ) TO read_tab. 
    ENDLOOP. 
 
    "Retrieving the entries of the invalid instances 
    READ ENTITY demo_cs_rap_draft_m 
      ALL FIELDS WITH read_tab 
      RESULT FINAL(result). 
 
    "Correcting and updating the invalid instances 
    MODIFY ENTITY demo_cs_rap_draft_m 
      UPDATE FROM VALUE #( 
        FOR wa IN result ( 
            %pid = wa-%pid 
            %is_draft = if_abap_behv=>mk-on 
            num2 = SWITCH #( wa-calc_result 
              WHEN `Division by 0` THEN 2 
              WHEN `Overflow error` THEN 3 ) 
            arithm_op = SWITCH #( wa-calc_result 
              WHEN `Wrong operator` THEN '+' ) 
            %control-num2 = SWITCH #( wa-calc_result 
              WHEN `Division by 0` THEN if_abap_behv=>mk-on 
              WHEN `Overflow error` THEN if_abap_behv=>mk-on 
              ELSE if_abap_behv=>mk-off ) 
            %control-arithm_op = SWITCH #( wa-calc_result 
              WHEN `Wrong operator` THEN if_abap_behv=>mk-on 
              ELSE if_abap_behv=>mk-off ) ) ) 
        FAILED f 
        REPORTED r 
        MAPPED m. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    MODIFY ENTITY demo_cs_rap_draft_m 
      EXECUTE activate AUTO FILL CID WITH activate_tab3 
      MAPPED m 
      FAILED f 
      REPORTED r. 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    "Retrieving draft table entries 
    SELECT id, num1, arithm_op, num2, calc_result, crea_date_time, 
           lchg_date_time, draftentitycreationdatetime, 
           draftentitylastchangedatetime 
     FROM demo_cs_drafttab 
     ORDER BY id 
     INTO TABLE @draft_parent_afer_act. 
 
    "Retrieving database table entries 
    SELECT id, num1, arithm_op, num2, calc_result, crea_date_time, 
           lchg_date_time 
     FROM demo_cs_tab_calc 
     ORDER BY id 
     INTO TABLE @db_tab_root_after_act. 
 
    "Displaying entries 
    out->write_html( `<b>Draft and database tables after ` && 
                   `ACTIVATE action</b>` 
      )->write( data = draft_parent_afer_act exclude = `client` 
                name = 'Draft table after activation' 
      )->write( data = db_tab_root_after_act exclude = `client` 
                name = 'Database table after activation' 
      ). 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_cs_tab_calc.                       "#EC CI_NOWHERE 
    DELETE FROM demo_cs_drafttab.                       "#EC CI_NOWHERE 
 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor(  ). 
    initialize_dbtabs( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**RAP Calculator within a class**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class.

The class that acts as [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) here demonstrates the following:

- Creating instances and saving to the database

  First, five instances are created using an ABAP EML `MODIFY` statement, i. e. five calculations are triggered. All of them use a different arithmetic operator. They all return a valid result. To show the effect of the statement, the entries of the draft table and the database table are retrieved and displayed. At this stage, the entries are not yet available in the database table. Then, the `activate` action is executed so that the entries in the draft table are persisted to the database table. The table entries are retrieved again showing that the draft table has no entries. All instances have been persisted to the database.

- Creating invalid entries

  Three instances are created using an ABAP EML `MODIFY` statement, i. e. three calculations are carried out. All of them fail either by using a wrong operator or because of a division by 0 or an arithmetic overflow issue. Consequently, the `FAILED` and `REPORTED` response parameters are filled with these instances. In the same way as above, the table entries are retrieved and displayed before and after executing the `activate` method. Here, the invalid entries are not persisted to the database.

- Correcting and updating invalid entries

  The three invalid entries are updated so that the calculation is successful and a valid result is returned. Finally, the now valid instances are saved to the database table.

**RAP Calculator using an SAP Fiori Elements app**

You can test the RAP Calculator using the preview version of an SAP Fiori Elements app as follows:

1.  In [ADT](../../abap-glossary/abenadt_glosry.md), search for and open the service binding `DEMO_RAP_CALC_DR_SB`. It is contained in the same package as the class mentioned above.

2.  Make sure that the `Local Service Endpoint` in the `Service Version Details` section is published.

3.  Select the entity set `DEMO_CS_RAP_DRAFT_M` and choose *Preview*.

4.  An app is opened in a browser. If you are prompted, provide the system credentials to log on. The app and the managed, draft-enabled RAP BO can be explored. The late numbering aspects comes into the picture when you, for example, create a new instance, i. e. create a new calculation, and you keep a draft version of it instead of saving it to the database. The calculation ID which represents the key of the instance has an initial value. The final key is only set when you save the instance to the database.

See comments in the code for more information.
