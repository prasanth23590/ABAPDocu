---
title: "CREATE DATA, TYPE, LIKE"
source_file: abapcreate_data_existing.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > CREATE DATA"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CREATE DATA, TYPE, LIKE

## Syntax

``` abap
CREATE DATA dref { {TYPE [LINE OF] {type|(name)}}
                 | {LIKE [LINE OF] dobj}
                 | {LIKE struct-{comp_name|(comp_name)}}}.
```

## Description

The type of the created data object is defined by a type or data object specification.

- For type, any data type can be specified from the ABAP Dictionary, particularly the DDIC structure of a DDIC database table,V5_out( a DDIC view,) a CDS type or a public data type of a global class, or any data type of the same program already defined using TYPES and that is either more specific than or identical to the static type of dref. Alternatively, a character-like data object name, which is not case-sensitive, can be specified in parentheses that contains the name of the existing data type when the statement is executed. The name in name can also be an absolute type name. If a standard table type with a generic primary table key is specified after TYPE, a new bound table type with standard key is created and used.

- A data object that is visible at this point can be specified for dobj. The generated data object inherits the current data type. If dobj is specified as a formal parameter or field symbol, it can be completely or partially generic. When the statement CREATE DATA is executed, a data object must be bound to a generically typed field symbol or parameter and its type is used. In the case of a completely typed field symbol or parameter, the declared type is used and no data object must be bound.

- Structure components can be referred to using the structure followed by the component selector and the component name comp_name. The component name can also be specified dynamically within parentheses.

The optional addition LINE OF can be used if type or the name in name is a table type, or if dobj is an internal table. As a result, the generated data object inherits the properties of the line type of the internal table.

## Hints

- The data objects which can be referred to using LIKE include the public attributes of global classes.

- If an anonymous data object is created with an enumerated type, the same rules apply to this object as to every other data object of this type.

- If a data type type is used, the instance operator NEW acts like the statement CREATE DATA dref TYPE type and can be used in general expression positions. The dynamic specification of name is not possible here.

## Example

Creation of an anonymous data object of type SCARR.

``` abap
FINAL(out) = cl_demo_output=>new( ).

DATA dref TYPE REF TO data.

CREATE DATA dref TYPE scarr.

SELECT SINGLE *
       FROM scarr
       WHERE carrid = 'LH'
       INTO @dref->*.

ASSIGN dref->*-('CARRID')   TO FIELD-SYMBOL(<fs1>).
ASSIGN dref->*-('CARRNAME') TO FIELD-SYMBOL(<fs2>).

out->write( |{ <fs1> }, { <fs2> }| ).

out->display( ).
```

## Example

The following example uses the LIKE addition and specifies a component name to refer to statically and dynamically.

``` abap
DATA: BEGIN OF struct,
        num TYPE i,
        str Type string,
      END OF struct.

DATA dref TYPE REF TO data.

CREATE DATA dref LIKE struct-num.
CREATE DATA dref LIKE struct-num.

CREATE DATA dref LIKE struct-('NUM').
DATA comp_name TYPE string VALUE `STR`.
CREATE DATA dref LIKE struct-(comp_name).
```

## Executable Example

[Creating Structured Data Objects](abencreate_structured_data_abexa.md)
