---
title: "CREATE DATA"
source_file: abapcreate_data.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CREATE DATA

## Syntax Forms

**[Defining the Data Type Implicitly](abapcreate_data_implicit.md)**

``` abap
1. CREATE DATA dref.
```

**[Defining the Data Type Using Built-in ABAP Types](abapcreate_data_built_in.md)**

``` abap
2. CREATE DATA dref 
                   TYPE {abap_type|(name)} 
                        [LENGTH len] [DECIMALS dec].
```

**[Defining the Data Type Using an Existing Type](abapcreate_data_existing.md)**

``` abap
3. CREATE DATA dref 
                   { {TYPE [LINE OF] {type|(name)}} 
                   | {LIKE [LINE OF] dobj} }.
```

**[Creating Reference Variables](abapcreate_data_reference.md)**

``` abap
5. CREATE DATA dref 
                   TYPE REF TO {type|(name)}.
```

**[Creating Internal Tables](abapcreate_data_itab.md)**

``` abap
6. CREATE DATA dref 
                   { {TYPE [STANDARD]|SORTED|HASHED TABLE 
                      OF [REF TO] {type|(name)}} 
                   | {LIKE [STANDARD]|SORTED|HASHED TABLE OF dobj} } 
                   [ {WITH [UNIQUE|NON-UNIQUE] 
                           {KEY {comp1 comp2 ...}|(keytab)}|{DEFAULT KEY}} 
                   | {WITH EMPTY KEY} ] 
                   [INITIAL SIZE n]. 
```

**[Create Data Object with BDEF Derived Types](../../abap-rap-business-objects/abap-for-rap-business-objects/abapderived_types_declaration.md)**

``` abap
7. CREATE DATA dref TYPE (der_type).
```

[`der_type`](../../abap-rap-business-objects/abap-for-rap-business-objects/abapderived_types_declaration.md)

## Description

The statement `CREATE DATA` creates an [anonymous data object](../../abap-glossary/abenanonymous_data_object_glosry.md) and assigns the reference to the data object to the reference variable `dref`.

By default, the data object is created in the [internal session](../../abap-glossary/abeninternal_session_glosry.md) ([heap](../../abap-glossary/abenheap_glosry.md)) of the current program and is preserved there for as long as it is required. If no [data references](../../abap-glossary/abendata_reference_glosry.md) and no [field symbols](../../abap-glossary/abenfield_symbol_glosry.md) point to the data object or to a part of the data object, it is deleted by the [Garbage Collector](../../abap-glossary/abengarbage_collector_glosry.md).

The reference variable `dref` must be declared as a data reference variable. The content of a data object created using `CREATE DATA` can only be accessed using dereferenced data variables or field symbols (see [Data Objects in Operand Positions](../abap-operands/abenoperands_data_objects.md)).

The data type of the created data object can be defined using the addition `TYPE` and a type specification or using the addition `LIKE` and a data object specification.

According to the rules in the section [Assignments Between Data Reference Variables](../abap-processing-internal-data/abenconversion_references_data.md), the static type of the data reference variable must be more general than the data type of the created data object, or be identical to it.

If a catchable exception is raised when the object is created, the object is not created and the `dref` data reference variable keeps its previous state.

## Hints

- Unlike the statement [`DATA`](../abap-declarations/abapdata.md), `CREATE DATA` creates the data object at the time of execution. Data objects declared using `DATA` are created when the associated program unit is loaded.

- The statement `CREATE DATA` creates a [heap reference](../../abap-glossary/abenheap_reference_glosry.md). All references that point to the anonymous data object or its parts are also heap references and keep the data object alive. The same applies to field symbols.

- When a data type is used, the [instance operator](../../abap-glossary/abeninstance_operator_glosry.md) [`NEW`](abenconstructor_expression_new.md) acts like the statement `CREATE DATA dref TYPE type` and can be used in [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md).

- Unlike [`CREATE OBJECT`](abapcreate_object.md), the return code `sy-subrc` is not set for `CREATE DATA`.

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_CREATE_DATA_ERROR`

- *Cause:* Illegal value for the addition `DECIMALS`.

  *Runtime error:* `CREATE_DATA_ILLEGAL_DECIMALS`

- *Cause:* Illegal value for the addition `INITIAL SIZE`.

  *Runtime error:* `CREATE_DATA_ILLEGAL_INIT_SIZE`

- *Cause:* Illegal value for the addition `LENGTH`.

  *Runtime error:* `CREATE_DATA_ILLEGAL_LENGTH`

- *Cause:* The addition `LENGTH` was used for a type other than `c`, `n`, `x`, or `p`.

  *Runtime error:* `CREATE_DATA_LEN_NOT_ALLOWED`

- *Cause:* The type specified dynamically in the addition `TYPE` is not typed in full.

  *Runtime error:* `CREATE_DATA_NOT_ALLOWED_TYPE`

- *Cause:* The type specified dynamically in the addition `TYPE` is not known.

  *Runtime error:* `CREATE_DATA_UNKNOWN_TYPE`
