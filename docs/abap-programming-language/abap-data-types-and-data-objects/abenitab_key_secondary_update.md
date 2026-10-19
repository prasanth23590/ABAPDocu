---
title: "itab - Updating Secondary Table Keys"
source_file: abenitab_key_secondary_update.html
section: "ABAP Programming Language > ABAP - Data Types and Data Objects > Data Objects > Internal Tables > itab - Table Key > itab - Secondary Table Key"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Updating Secondary Table Keys

For all statements that change the content and structure of an internal table, the internal administration of the secondary keys is updated automatically as follows:

- For all operations that insert lines into tables or delete lines from tables, the secondary key administration for unique keys is updated immediately, that is, a unique secondary key is up-to-date immediately after the operation ([direct update](../../abap-glossary/abendirect_update_glosry.md)). Non-unique secondary table keys are not updated immediately and only when the secondary key is next used explicitly using `USING KEY` or `WITH KEY ... COMPONENTS` ([lazy update](../../abap-glossary/abenlazy_update_glosry.md)). If an update violates secondary key uniqueness, a [catchable exception or runtime error occurs](abenitab_key_duplicates.md).

  Inserting operations include table statements such as [`INSERT`](../abap-processing-internal-data/abapinsert_itab.md) and [`APPEND`](../abap-processing-internal-data/abapappend.md) and block operations in which the entire body of the table is filled at once, like for statements between internal tables, passing parameters to procedures, filling internal tables with `SELECT`, importing with [`IMPORT`](../abap-data-cluster/abapimport_data_cluster.md), and so on. The operation for deleting table lines is the table statement [`DELETE`](../abap-processing-internal-data/abapdelete_itab.md).

- For operations that change the components of secondary table keys in existing lines, the secondary key administration is either updated directly or only at a specified synchronization time.

  - If [`MODIFY`](../abap-processing-internal-data/abapmodify_itab.md) is used to modify individual lines, any unique secondary keys are updated directly ([direct update](../../abap-glossary/abendirect_update_glosry.md)). If the modification produces duplicate entries, an uncatchable exception is raised.

  - If field symbols or data references that point to table lines are used to modify individual lines, any unique secondary keys are updated the next time the internal table is accessed ([delayed update](../../abap-glossary/abendelayed_update_glosry.md)). The uniqueness check also only takes place at the time of synchronization. An internal table can therefore be in an inconsistent state with respect to the secondary key following a modification to existing lines using field symbols or data references. The corresponding [exception](abenitab_key_duplicates.md) is only raised when the table is next used.

    In both cases, a non-unique key not updated until the secondary table key is next used explicitly ([lazy update](../../abap-glossary/abenlazy_update_glosry.md)).

The methods `FLUSH_ITAB_KEY` and `FLUSH_ITAB_KEYS` of the class `CL_ABAP_ITAB_UTILITIES` can be used to update individual secondary keys or all secondary keys of an internal table explicitly in exceptional circumstances. These methods can be used for analysis and test purposes. It might also make sense to use them after making changes if the next access does not take place immediately afterwards to handle possible exceptions there and then.

## Executable Example

The example for Deletion Using Table Keys demonstrates the runtimes that are required to create the secondary key and when they occur.
