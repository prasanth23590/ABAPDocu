---
title: "CDS DDL - ANNOTATE, parameter_list"
source_file: abencds_f1_annotate_view_para_list.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - Specifying Annotations > ABAP CDS - Metadata Extensions > ABAP CDS - DDL for Metadata Extensions > CDS DDL - ANNOTATE ENTITY, VIEW"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - ANNOTATE, parameter_list

## Syntax

``` abap
... PARAMETERS 
      @parameter_annot1 
     [@parameter_annot2 
      ...] 
      pname1[, 
      @parameter_annot1 
     [@parameter_annot2 
      ...] 
      pname2, 
      ...]  
```

[`@parameter_annot1`](../abap-cds-data-definitions/abencds_f1_parameter_annotations.md) · [`@parameter_annot2`](../abap-cds-data-definitions/abencds_f1_parameter_annotations.md) · [`@parameter_annot1`](../abap-cds-data-definitions/abencds_f1_parameter_annotations.md) · [`@parameter_annot2`](../abap-cds-data-definitions/abencds_f1_parameter_annotations.md)

## Description

Specifies annotations for the following parameters:

- [Parameter list](../abap-cds-data-definitions/abencds_f1_entity_parameter_list.md) of an [CDS abstract entity](../../abap-glossary/abencds_abstract_entity_glosry.md)

- [Parameter list](../abap-cds-data-definitions/abencds_parameter_list_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md)

- [Parameter list](../abap-cds-obsolete-language-elements/abencds_parameter_list_v1.md) of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md)

The parameters in a [CDS metadata extension](../../abap-glossary/abencds_metadata_extension_glosry.md) introduced using [`ANNOTATE`](abencds_f1_annotate_view.md). A comma-separated list `pname1`, `pname2`, ... prefixed with annotations `@parameter_annot` can be specified after `PARAMETERS`. There must not be comma after the last element of the list.

Each parameter `pname` specified after `PARAMETERS` should appear in the parameter list of the entity extended using `ANNOTATE`. If not, the syntax check produces a warning. All parameters defined there can be used exactly once. Valid [SAP annotations](abencds_annotations_sap.md) `@parameter_annot` can be specified before these as [parameter annotations](../abap-cds-data-definitions/abencds_f1_parameter_annotations.md). It is not possible here to specify annotations after the name of a parameter `pname` with the syntax `@<parameter_annot`.

At least one parameter `pname` of the extended entity must be specified after `PARAMETERS`. At least one parameter annotation [`@parameter_annot`](../abap-cds-data-definitions/abencds_f1_parameter_annotations.md) must be specified before each parameter of the list. If this is not the case, `PARAMETERS` cannot be used.

## Hints

- A parameter must be specified directly with its name. It cannot be specified using the syntax `:pname` or `$parameters.pname`, which is used within the entity for its addressing (parameter passing in CDS view entities is described [here](../abap-cds-data-definitions/abencds_select_parameters_v2.md), parameter passing in CDS DDIC-based views (obsolete) is described [here](../abap-cds-obsolete-language-elements/abencds_select_parameters_v1.md)).

- The program `ABAP_DOCU_MDE_ANNOS` shows all annotations that can be specified in metadata extensions.
