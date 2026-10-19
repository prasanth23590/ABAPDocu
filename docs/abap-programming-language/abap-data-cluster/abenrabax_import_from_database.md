---
title: "Exceptions in IMPORT"
source_file: abenrabax_import_from_database.html
section: "ABAP Programming Language > ABAP - Data Cluster > IMPORT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Exceptions in IMPORT

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

## Catchable Exceptions

`CX_SY_COMPRESSION_ERROR`

- *Cause:* Error during compression or decompression.

  *Runtime error:* `IMPORT_DECOMPRESS_FAILED`

- *Cause:* Error when decompressing during `IMPORT`.

  *Runtime error:* `CONNE_IMPORT_WRONG_COMP_LENG`

`CX_SY_CONVERSION_CODEPAGE`

- *Cause:* Error in conversion.

  *Runtime error:* `CONNE_IMPORT_CONVERSION_ERROR`

`CX_SY_IMPORT_MISMATCH_ERROR`

- *Cause:* A component of a structured dataset has an incorrect decimal place.

  *Runtime error:* `CONNE_IMPORT_WRONG_COMP_DECS`

- *Cause:* A component of a structured dataset has an incorrect length.

  *Runtime error:* `CONNE_IMPORT_WRONG_COMP_LENG`

- *Cause:* A component of a structured type in the dataset has an incorrect type.

  *Runtime error:* `CONNE_IMPORT_WRONG_COMP_TYPE`

- *Cause:* A field in the dataset has incorrect decimal places.

  *Runtime error:* `CONNE_IMPORT_WRONG_FIELD_DECS`

- *Cause:* A field in the dataset has an incorrect length.

  *Runtime error:* `CONNE_IMPORT_WRONG_FIELD_LENG`

- *Cause:* A field in the dataset has an incorrect type.

  *Runtime error:* `CONNE_IMPORT_WRONG_FIELD_TYPE`

- *Cause:* Type conflict between simple and structured data types.

  *Runtime error:* `CONNE_IMPORT_WRONG_OBJECT_TYPE`

- *Cause:* Type conflict between structured objects

  *Runtime error:* `CONNE_IMPORT_WRONG_STRUCTURE`

- *Cause:* Source object and target object have incompatible types.

  *Runtime error:* `IMPORT_ALIGNMENT_MISMATCH`

- *Cause:* Dataset has a different length.

  *Runtime error:* `IMPORT_WRONG_END_POS`

`CX_SY_IMPORT_FORMAT_ERROR`

- *Cause:* Error in the data description of a stored data object.

  *Runtime error:* `IMPORT_FORMAT_ERROR`

- *Cause:* Error in the data description.

  *Runtime error:* `IMPORT_DESCR_ENDMARK_MISSING`

- *Cause:* The dataset was destroyed. The data is distributed among several table entries, and at least one table entry is missing.

  *Runtime error:* `IMPORT_UNEXPECTED_END_OF_DATA`

- *Cause:* Error in decompression.

  *Runtime error:* `IMPORT_DECOMPRESS_FAILED`

- *Cause:* Invalid or missing data cluster in `IMPORT FROM INTERNAL TABLE`

  *Runtime error:* `IMPORT_CONTAINER_MISSING`

- *Cause:* Empty internal table in `IMPORT FROM INTERNAL TABLE`

  *Runtime error:* `IMPORT_CONTAINER_MISSING`

- *Cause:* Empty data object in `IMPORT FROM DATA BUFFER`

  *Runtime error:* `IMPORT_CONTAINER_MISSING`

- *Cause:* The data cluster was destroyed.

  *Runtime error:* `IMPORT_OBJECT_DESTROYED`

- *Cause:* Invalid or missing data cluster in `IMPORT FROM DATA BUFFER`

  *Runtime error:* `CONNE_CONTAINER_TOO_SHORT`

- *Cause:* The dataset was destroyed.

  *Runtime error:* `CONNE_ILLEGAL_TRANSPORT_HEADER`

- *Cause:* An attempt was made to import a dataset originating from an AS ABAP of a higher release level. This action is not supported.

  *Runtime error:* `CONNE_ILLEGAL_TRANSPORT_VERS`

- *Cause:* Error in data description in `IMPORT`.

  *Runtime error:* `CONNE_IMPORT_ILL_DESCRIPTION`

- *Cause:* One of the properties saved for the cluster is invalid.

  *Runtime error:* `CONNE_COMPRESS_FLAG_INVALID`

  *Runtime error:* `CONNE_DESCRIPTION_FLAG_INVALID`

  *Runtime error:* `CONVERSION_CODEPAGE_UNKNOWN`

`CX_SY_EXPIMP_DB_SQL_ERROR`

- *Cause:* SQL error in import from the database.

  *Runtime error:* [`DBIF_...`](../abap-database-access/abenabap_sql_exceptions.md)
