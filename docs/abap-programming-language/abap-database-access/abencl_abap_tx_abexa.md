---
title: "CL_ABAP_TX and API Classifications"
source_file: abencl_abap_tx_abexa.html
section: "ABAP Programming Language > ABAP - Database Access > Data Consistency > SAP LUW > Controlled SAP LUW"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CL_ABAP_TX and API Classifications

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the explicit setting of transactional phases using the `MODIFY` and `SAVE` methods of the class `CL_ABAP_TX`. It includes multiple showcase implementations after setting the transactional phase. In some cases, the implementations deliberately violate the transactional contract to demonstrate what is allowed and what not. Furthermore, the implementations include method calls. The methods are tagged with `IF_ABAP_TX*`.

**Note:** The example can only be executed if the checkpoint group `CC_STMT` is not active. If they are active, the demo execution is not possible choosing the *Execute* button in the system-internal ABAP Keyword Documentation as dynpro processing is involved triggering a runtime error.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for CL_ABAP_TX</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_cl_abap_tx DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    DATA input TYPE i. 
 
  PRIVATE SECTION. 
    METHODS get_html RETURNING VALUE(html) TYPE string. 
    DATA current_phase TYPE cl_abap_behv_aux=>t_phase. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cl_abap_tx IMPLEMENTATION. 
  METHOD main. 
 
    cl_demo_input=>new( 
       )->add_text( get_html( ) 
       )->add_field( EXPORTING 
                       text  = `Number` 
                     CHANGING 
                       field = input 
       )->request( ). 
 
    IF input >= 7. 
      DATA(oref) = NEW cl_demo_classified_apis(  ). 
    ENDIF. 
 
    CASE input. 
 
      WHEN 1. 
 
        cl_abap_tx=>modify( ). 
 
        current_phase = cl_abap_behv_aux=>get_current_phase( ). 
 
        MODIFY ENTITY demo_managed_root 
         CREATE AUTO FILL CID 
         FIELDS ( key_field data_field1_root data_field2_root ) 
         WITH VALUE #( 
            ( key_field = 1 
              data_field1_root = `abc` 
              data_field2_root = `def` ) ) 
         MAPPED DATA(m) 
         FAILED DATA(f) 
         REPORTED DATA(r). 
 
        out->write( `RAP create operation in MODIFY phase` ). 
        out->write( |Current phase: { current_phase }| ). 
 
      WHEN 2. 
 
        cl_abap_tx=>modify( ). 
 
        current_phase = cl_abap_behv_aux=>get_current_phase( ). 
 
        DELETE FROM demo_tab_root.                      "#EC CI_NOWHERE 
 
        out->write( `Database modification operation in MODIFY ` && 
        `phase` ). 
        out->write( |Current phase: { current_phase }| ). 
 
      WHEN 4. 
 
        cl_abap_tx=>save( ). 
 
        current_phase = cl_abap_behv_aux=>get_current_phase( ). 
 
        DELETE FROM demo_tab_root.                      "#EC CI_NOWHERE 
 
        out->write( `Database modification operation in SAVE ` && 
        `phase` ). 
        out->write( |Current phase: { current_phase }| ). 
 
      WHEN 5. 
 
        cl_abap_tx=>save( ). 
 
        current_phase = cl_abap_behv_aux=>get_current_phase( ). 
 
        COMMIT ENTITIES. 
 
        IF sy-subrc <> 0. 
          out->write_doc( `An issue occurred in the RAP ` && 
                          `save sequence.` ). 
        ENDIF. 
 
        out->write( `Commit in (late) SAVE phase` ). 
        out->write( |Current phase: { current_phase }| ). 
 
      WHEN 6. 
 
        cl_abap_tx=>save( ). 
 
        current_phase = cl_abap_behv_aux=>get_current_phase( ). 
 
        MODIFY ENTITY demo_managed_root 
         CREATE AUTO FILL CID 
         FIELDS ( key_field data_field1_root data_field2_root ) 
         WITH VALUE #( 
            ( key_field = 1 
              data_field1_root = `abc` 
              data_field2_root = `def` ) ) 
         MAPPED m 
         FAILED f 
         REPORTED r. 
 
        out->write( `RAP create operation in SAVE phase` ). 
        out->write( |Current phase: { current_phase }| ). 
 
*************** Classified APIs ************************************** 
 
        "if_abap_tx_complete 
      WHEN 7. 
 
        cl_abap_tx=>modify( ). 
 
        current_phase = cl_abap_behv_aux=>get_current_phase( ). 
 
        oref->meth_complete( ). 
 
        out->write( `Calling API classified with ` && 
        `IF_ABAP_TX_COMPLETE in MODIFY phase` ). 
        out->write( |Current phase: { current_phase }| ). 
 
      WHEN 8. 
 
        cl_abap_tx=>save( ). 
 
        current_phase = cl_abap_behv_aux=>get_current_phase( ). 
 
        oref->meth_complete( ). 
 
        out->write( `Calling API classified with ` && 
        `IF_ABAP_TX_COMPLETE in SAVE phase` ). 
        out->write( |Current phase: { current_phase }| ). 
 
      WHEN 9. 
 
        oref->meth_complete( ). 
 
        current_phase = cl_abap_behv_aux=>get_current_phase( ). 
 
        out->write( `Calling API classified with ` && 
        `IF_ABAP_TX_COMPLETE (no transactional context set)` ). 
        out->write( |Current phase: { current_phase }| ). 
 
        "if_abap_tx_read 
      WHEN 10. 
 
        cl_abap_tx=>modify( ). 
 
        current_phase = cl_abap_behv_aux=>get_current_phase( ). 
 
        oref->meth_read( ). 
 
        out->write( `Calling API classified with ` && 
        `IF_ABAP_TX_READ in MODIFY phase` ). 
        out->write( |Current phase: { current_phase }| ). 
 
      WHEN 11. 
 
        cl_abap_tx=>save( ). 
 
        current_phase = cl_abap_behv_aux=>get_current_phase( ). 
 
        oref->meth_read( ). 
 
        out->write( `Calling API classified with ` && 
        `IF_ABAP_TX_READ in SAVE phase` ). 
        out->write( |Current phase: { current_phase }| ). 
 
        "if_abap_tx_modify 
      WHEN 12. 
 
        cl_abap_tx=>modify( ). 
 
        current_phase = cl_abap_behv_aux=>get_current_phase( ). 
 
        oref->meth_modify( ). 
 
        out->write( `Calling API classified with ` && 
        `IF_ABAP_TX_MODIFY in MODIFY phase` ). 
        out->write( |Current phase: { current_phase }| ). 
 
      WHEN 13. 
 
        cl_abap_tx=>save( ). 
 
        current_phase = cl_abap_behv_aux=>get_current_phase( ). 
 
        oref->meth_modify( ). 
 
        out->write( `Calling API classified with ` && 
        `IF_ABAP_TX_MODIFY in SAVE phase` ). 
        out->write( |Current phase: { current_phase }| ). 
 
        "if_abap_tx_save 
      WHEN 14. 
 
        cl_abap_tx=>modify( ). 
 
        current_phase = cl_abap_behv_aux=>get_current_phase( ). 
 
        oref->meth_save( ). 
 
        out->write( `Calling API classified with ` && 
        `IF_ABAP_TX_SAVE in MODIFY phase` ). 
        out->write( |Current phase: { current_phase }| ). 
 
      WHEN 15. 
 
        cl_abap_tx=>save( ). 
 
        current_phase = cl_abap_behv_aux=>get_current_phase( ). 
 
        oref->meth_save( ). 
 
        out->write( `Calling API classified with ` && 
        `IF_ABAP_TX_SAVE in SAVE phase` ). 
        out->write( |Current phase: { current_phase }| ). 
 
        "if_abap_tx_functional 
      WHEN 16. 
 
        cl_abap_tx=>modify( ). 
 
        current_phase = cl_abap_behv_aux=>get_current_phase( ). 
 
        oref->meth_functional( ). 
 
        out->write( `Calling API classified with ` && 
        `IF_ABAP_TX_FUNCTIONAL in MODIFY phase` ). 
        out->write( |Current phase: { current_phase }| ). 
 
      WHEN 17. 
 
        cl_abap_tx=>save( ). 
 
        current_phase = cl_abap_behv_aux=>get_current_phase( ). 
 
        oref->meth_functional( ). 
 
        out->write( `Calling API classified with ` && 
        `IF_ABAP_TX_FUNCTIONAL in SAVE phase` ). 
        out->write( |Current phase: { current_phase }| ). 
 
        "if_abap_tx_surface 
      WHEN 18. 
 
        cl_abap_tx=>modify( ). 
 
        current_phase = cl_abap_behv_aux=>get_current_phase( ). 
 
        oref->meth_surface( ). 
 
        out->write( `Calling API classified with ` && 
        `IF_ABAP_TX_SURFACE in MODIFY phase` ). 
        out->write( |Current phase: { current_phase }| ). 
 
      WHEN 19. 
 
        cl_abap_tx=>save( ). 
 
        current_phase = cl_abap_behv_aux=>get_current_phase( ). 
 
        oref->meth_surface( ). 
 
        out->write( `Calling API classified with ` && 
        `IF_ABAP_TX_SURFACE in SAVE phase` ). 
        out->write( |Current phase: { current_phase }| ). 
 
      WHEN OTHERS. 
        out->write( `Enter one of the prededfined numbers.` ). 
    ENDCASE. 
 
  ENDMETHOD. 
  METHOD get_html. 
    html = 
    `<p>For testing the ` && 
    `effect of setting the transactional ` && 
    `phase explicitly using the methods MODIFY and SAVE  ` && 
    `of the class CL_ABAP_TX, ` && 
    `enter one of the following numbers (note that "Violation" ` && 
    `can mean a runtime error):</p>` && 
    `<table>` && 
    `<tbody style="font-size: 11px";>` && 
    `<tr><th>Number</th>` && 
    `<th>Phase</th>` && 
    `<th>What is executed</th>` && 
    `<th>Expected Result</th></tr>` && 
    `<tr><td>1</td><td>MODIFY</td><td>RAP create operation` && 
    `</td><td>Ok</td></tr>` && 
    `<tr><td>2</td><td>MODIFY</td><td>ABAP SQL ` && 
    `database modification</td><td>Violation</td></tr>` && 
    `<tr><td>4</td><td>SAVE</td><td>ABAP SQL database ` && 
    `modification</td><td>Ok</td></tr>` && 
    `<tr><td>5</td><td>SAVE</td><td>Commit</td>` && 
    `<td>Violation</td></tr>` && 
    `<tr><td>6</td><td>SAVE</td><td>RAP create operation` && 
    `</td><td>Violation</td></tr>` && 
    `<tr><td>7</td><td>MODIFY</td><td>Calling API tagged with ` && 
    `IF_ABAP_TX_COMPLETE</td>` && 
    `<td>Violation</tr>` && 
    `<tr><td>8</td><td>SAVE</td><td>Calling API tagged with ` && 
    `IF_ABAP_TX_COMPLETE</td><td>Violation</tr>` && 
    `<tr><td>9</td><td>No phase set</td><td>Calling API ` && 
    `tagged with IF_ABAP_TX_COMPLETE` && 
    `</td><td>Ok</tr>` && 
    `<tr><td>10</td><td>MODIFY</td><td>Calling API tagged with ` && 
    `IF_ABAP_TX_READ</td><td>Ok</tr>` && 
    `<tr><td>11</td><td>SAVE</td><td>Calling API tagged with ` && 
    `IF_ABAP_TX_READ</td><td>Ok</tr>` && 
    `<tr><td>12</td><td>MODIFY</td><td>Calling API tagged with ` && 
    `IF_ABAP_TX_MODIFY</td><td>Ok</tr>` && 
    `<tr><td>13</td><td>SAVE</td><td>Calling API tagged with ` && 
    `IF_ABAP_TX_MODIFY</td><td>Violation</tr>` && 
    `<tr><td>14</td><td>MODIFY</td><td>Calling API tagged with ` && 
    `IF_ABAP_TX_SAVE</td><td>Violation</tr>` && 
    `<tr><td>15</td><td>SAVE</td><td>Calling API tagged with ` && 
    `IF_ABAP_TX_SAVE</td><td>Ok</tr>` && 
    `<tr><td>16</td><td>MODIFY</td><td>Calling API tagged with ` && 
    `IF_ABAP_TX_FUNCTIONAL</td><td>Ok</tr>` && 
    `<tr><td>17</td><td>SAVE</td><td>Calling API tagged with ` && 
    `IF_ABAP_TX_FUNCTIONAL</td><td>Ok</tr>` && 
    `<tr><td>18</td><td>MODIFY</td><td>Calling API tagged with ` && 
    `IF_ABAP_TX_SURFACE</td><td>Violation</tr>` && 
    `<tr><td>19</td><td>SAVE</td><td>Calling API tagged with ` && 
    `IF_ABAP_TX_SURFACE</td><td>Violation</tr>` && 
    `</tbody>` && 
    `</table>`. 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The example is executed based on an input parameter. For the details, see the code and the descriptions in the popup that is displayed when running the example.
