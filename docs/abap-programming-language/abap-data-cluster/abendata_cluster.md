---
title: "ABAP - Data Cluster"
source_file: abendata_cluster.html
section: "ABAP Programming Language"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP - Data Cluster

A data cluster is a group of [data objects](../../abap-glossary/abendata_object_glosry.md) grouped together for the purpose of storage in a [memory medium](abapexport_data_cluster_medium.md) that can only be accessed using ABAP statements.

- The data objects are written to the memory medium by the statement [`EXPORT`](abapexport_data_cluster.md).

- The data objects are extracted again by the statement [`IMPORT`](abapimport_data_cluster.md).

- The statement `DELETE` can be used to delete any memory medium.
