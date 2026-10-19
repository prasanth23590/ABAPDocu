---
title: "IMPORT, conversion_options"
source_file: abapimport_conversion.html
section: "ABAP Programming Language > ABAP - Data Cluster > IMPORT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# IMPORT, conversion_options

## Syntax

``` abap
... { { { {[ACCEPTING PADDING] [ACCEPTING TRUNCATION]}   
        | [IGNORING STRUCTURE BOUNDARIES] }   
        [IGNORING CONVERSION ERRORS [REPLACEMENT CHARACTER rc]] }   
    | [IN CHAR-TO-HEX MODE] }   
    [CODE PAGE INTO cp]   
    [ENDIAN INTO endian].  
```

### Addition

[1. `... ACCEPTING PADDING`](abapimport_conversion.md#addition-1)

[2. `... ACCEPTING TRUNCATION`](abapimport_conversion.md#addition-2)

[3. `... IGNORING STRUCTURE BOUNDARIES`](abapimport_conversion.md#addition-3)

[4. `... IGNORING CONVERSION ERRORS [REPLACEMENT CHARACTER rc]`](abapimport_conversion.md#addition-4)

[5. `... IN CHAR-TO-HEX MODE`](abapimport_conversion.md#addition-5)

[6. `... CODE PAGE INTO cp`](abapimport_conversion.md#addition-6)

[7. `... ENDIAN INTO endian`](abapimport_conversion.md#addition-7)

## Overview

### Description

These additions allow the reading of data stored in [data clusters](../../abap-glossary/abendata_cluster_glosry.md) into non-type-compliant data objects and define associated conversion rules. The following table shows which of the additions may be used during imports from the various buffers. The column headers are abbreviations for the following storage locations: [`DATA BUFFER`](abapimport_medium.md) (`B`), [`MEMORY`](abapimport_medium.md) (`M`), [`SHARED MEMORY`](abapimport_medium.md) (`SM`), [`SHARED BUFFER`](abapimport_medium.md) (`SB`), [`DATABASE`](abapimport_medium.md) (`DB`), and [`INTERNAL TABLE`](abapimport_medium.md) (`IT`).

| **Conversion Addition**         | **`B`** | **`M`** | **` IT`** | **`DB`** | **`SM`** | **`SB`** |
|---------------------------------|---------|---------|-----------|----------|----------|----------|
| `ACCEPTING PADDING`             | \+      | \+      | \+        | \+       | \+       | \+       |
| `ACCEPTING TRUNCATION`          | \+      | \+      | \+        | \+       | \+       | \+       |
| `IGNORING STRUCTURE BOUNDARIES` | \+      | \+      | \+        | \+       | \+       | \+       |
| `IGNORING CONVERSION ERRORS`    | \+      | \-      | \+        | \+       | \-       | \-       |
| `REPLACEMENT CHARACTER rc`      | \+      | \-      | \+        | \+       | \-       | \-       |
| `IN CHAR-TO-HEX MODE`           | \+      | \-      | \+        | \+       | \-       | \-       |
| `CODE PAGE INTO cp`             | \+      | \-      | \+        | \+       | \-       | \-       |
| `ENDIAN INTO endian`            | \+      | \-      | \+        | \+       | \-       | \-       |

## Addition 1

`... ACCEPTING PADDING`

### Description

This addition extends the rules from [`parameter_list`](abapimport_parameterlist.md) for different data types of source field and target field `dobj` in the data clusters:

- In addition to data objects of the type `c`, the target field can be longer than the source field for data objects of the type `n`, `p`, or `x`.

- Source fields of the type

  - `b` can be read into target fields of the types `s`, `i`, and `int8`

  - `s` can be read into target fields of the type `i` and `int8` (but negative numbers are handled incorrectly)

  - `i` can be read into target fields of the type `int8`

- Source fields of the type `c` can be exported to target fields of the type `string` and source fields of the type `x` can be exported to target fields of the type `xstring`.

- The rules above also apply if the component involved is the last component of a source structure or target structure that is otherwise set up in the same way.

- In a target structure, substructures can also have more components than the substructures of the source structure if the structure is otherwise set up in the same way. The surplus components are provided with type-dependent [initial values](../../abap-glossary/abeninitial_value_glosry.md).

### Hint

The rule that substructures in a target structure can have more components than the source structure can cause problems in relation to structures defined in the ABAP Dictionary. This is the case if the structure there is marked as extendable. Therefore, this situation raises a warning from the extended program check.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Without the addition `ACCEPTING PADDING`, the structure `f1` in the byte string could not be imported into the structure `f2` since a substructure of `f2` contains a surplus component.

``` abap
DATA buffer TYPE xstring. 
 
DATA: BEGIN OF f1, 
        col1 TYPE string, 
        BEGIN OF sub, 
          col2 TYPE decfloat16, 
        END OF sub, 
        col3 TYPE i, 
      END OF f1. 
 
DATA: BEGIN OF f2, 
        col1 TYPE string, 
        BEGIN OF sub, 
          col2 TYPE decfloat16, 
          col3 TYPE xstring, 
        END OF sub, 
        col4 TYPE i, 
      END OF f2. 
 
EXPORT para = f1 TO DATA BUFFER buffer. 
 
... 
 
IMPORT para = f2 FROM DATA BUFFER buffer ACCEPTING PADDING.
```

## Addition 2

`... ACCEPTING TRUNCATION`

### Description

This addition expands the rules from [`parameter_list`](abapimport_parameterlist.md) for different data types of source field in the data cluster and target field `dobj` in the data cluster. This means that, in the case of structures that otherwise have the same type, if the source structure at the highest level has more components than the target structure in the data cluster, the surplus components are cut off. A substructure of the source structure must not have more components than the corresponding substructure in the target structure.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Without the addition `ACCEPTING TRUNCATION`, the structure `f1` in the byte string could not be imported into the structure `f2` since `f2` contains fewer components.

``` abap
DATA buffer TYPE xstring. 
 
DATA: BEGIN OF f1, 
        col1 TYPE string, 
        BEGIN OF sub, 
          col2 TYPE decfloat34, 
        END OF sub, 
        col3 TYPE i, 
        col4 TYPE xstring, 
      END OF f1. 
 
DATA: BEGIN OF f2, 
        col1 TYPE string, 
        BEGIN OF sub, 
          col2 TYPE decfloat34, 
        END OF sub, 
        col3 TYPE i, 
      END OF f2. 
 
EXPORT para = f1 TO DATA BUFFER buffer. 
 
... 
 
IMPORT para = f2 FROM DATA BUFFER buffer ACCEPTING TRUNCATION.
```

## Addition 3

`... IGNORING STRUCTURE BOUNDARIES`

### Description

This addition expands the rules from [`parameter_list`](abapimport_parameterlist.md) for different data types of source field in the data cluster and target field `dobj` in the data cluster. In structures, this produces an insignificantly different setup, with the differences resulting from substructures or from various applied components of other structures with the statement [`INCLUDE`](../abap-declarations/abapinclude_type.md). The components of source and target structure are all considered on one level, regardless of the setup inherited from substructures or from components applied using `INCLUDE`. Any [alignment gaps](../../abap-glossary/abenalignment_gap_glosry.md) that have resulted from substructures are irrelevant.

The addition `IGNORING STRUCTURE BOUNDARIES`, however, restricts the rules from [`parameter_list`](abapimport_parameterlist.md) in such a way that once the substructures or inherited components in the target structure are resolved, a last component of type `c` cannot have a different length and the target structure cannot have any additional components. The addition cannot be used together with the additions `ACCEPTING PADDING` and `ACCEPTING TRUNCATION`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Without the addition `IGNORING STRUCTURE BOUNDARIES`, the structure `f1` in the byte string could not be imported into the structure `f2` since `f1` and `f2` are set up differently from substructures.

``` abap
DATA buffer TYPE xstring. 
 
DATA: BEGIN OF incl_struc, 
        cola TYPE string, 
        colb TYPE i, 
      END OF incl_struc. 
 
DATA: BEGIN OF f1. 
        INCLUDE STRUCTURE incl_struc. 
DATA:   col1 TYPE string, 
        BEGIN OF sub, 
          col2 TYPE decfloat16, 
          col3 TYPE decfloat34, 
        END OF sub, 
        col4 TYPE i, 
      END OF f1. 
 
DATA: BEGIN OF f2, 
        cola TYPE string, 
        colb TYPE i, 
        col1 TYPE string, 
        BEGIN OF sub, 
          col2 TYPE decfloat16, 
        END OF sub, 
        col3 TYPE decfloat34, 
        col4 TYPE i, 
      END OF f2. 
 
EXPORT para = f1 TO DATA BUFFER buffer. 
 
... 
 
IMPORT para = f2 FROM DATA BUFFER buffer 
                 IGNORING STRUCTURE BOUNDARIES.
```

## Addition 4

`... IGNORING CONVERSION ERRORS [REPLACEMENT CHARACTER rc]`

### Description

This addition suppresses an exception of the class `CX_SY_CONVERSION_CODEPAGE`, which is raised when a conversion to another [code page](../../abap-glossary/abencodepage_glosry.md) is carried out during the import, and a character does not exist in the target code page.

If the addition `REPLACEMENT CHARACTER` is specified, each non-convertible character is replaced during the conversion by the character in `rc`. `rc` expects a character-like data object containing a single character. If the addition is not specified, the character *\#* is used as a replacement character.

The addition `IGNORING CONVERSION ERRORS` also suppresses the exception if the number of bytes of an imported character-like component increases during a conversion to another code page, and therefore does no longer fit into the target object. If the addition is specified, surplus characters are cut off on the right. If the addition is not specified, only superfluous blanks are cut off on the right without raising an exception.

## Addition 5

`... IN CHAR-TO-HEX MODE`

### Description

This addition specifies that data that is stored in the data cluster under the data type `c` is assigned to target fields of the type `x`. The content of the source fields is not converted to the code page of the target system and are left unconverted and passed to the target fields instead. A single source field or a structure component of the type `c` can be assigned to a single target field or to a structure component of the type `x`, which has the same length in bytes. The addition is ignored by target fields of the type `c`.

This addition cannot be used together with the previous conversion additions.

### Hint

A program using this addition cannot be transported between systems where character representations require different numbers of bytes. This addition is designed only for temporary programs, enabling them to import byte strings that were stored incorrectly in fields of the type `c` and to store them again in a type-compliant way.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

See under Addition `ENDIAN INTO`.

## Addition 6

`... CODE PAGE INTO cp`

### Description

This addition assigns the ID of the code page of the exported data to the data object `cp`. This object must have a character-like data type. The ID of the code page is the content of the column `CPCODEPAGE` of the database table `TCP00`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

See under Addition `ENDIAN INTO`.

## Addition 7

`... ENDIAN INTO endian`

### Description

This addition assigns the ID of the byte order of the exported data to the data object `ENDIAN`, which must have the data type `abap_endian` from the [type pool](../../abap-glossary/abentype_pool_glosry.md) ABAP. The ID for big endian is *B* and *L* for little endian.

### Hint

The byte order can be used to process data objects imported using `CHAR-TO-HEX MODE`, since code pages in which a character takes up more than one byte can be dependent on the byte order.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The target field `f2-col2` contains, after the import, the unconverted, binary content of `f1-col2`. The code page and the byte order in which the data is stored is in `cp` and `en`. Normally, the data in such a case is exported and imported in different programs. This example only works in a system in which a character is displayed using two bytes, since `f2-col2` is double the length of `f1-col2`.

``` abap
DATA buffer TYPE xstring. 
 
DATA: BEGIN OF f1, 
        col1 TYPE c LENGTH 10 VALUE '1234567890', 
        col2 TYPE c LENGTH 10 VALUE '1234567890', 
      END OF f1. 
 
DATA: BEGIN OF f2, 
        col1 TYPE c LENGTH 10, 
        col2 TYPE x LENGTH 20, 
      END OF f2. 
 
DATA: cp TYPE string, 
      en TYPE abap_endian. 
 
EXPORT para = f1 TO DATA BUFFER buffer. 
 
... 
 
IMPORT para = f2 FROM DATA BUFFER buffer 
                 IN CHAR-TO-HEX MODE 
                 CODE PAGE INTO cp 
                 ENDIAN INTO en.
```
