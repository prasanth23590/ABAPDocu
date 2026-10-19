---
title: "CDS DDL - DEFINE TYPE ENUM"
source_file: abencds_define_enum_type.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Type Definitions > CDS DDL - DEFINE TYPE > ABAP CDS - Enumerated Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE TYPE ENUM

## Syntax

``` abap
[@type_annot1] 
[@type_annot2] 
... 
  DEFINE TYPE EnumType : BaseType ENUM 
  { 
    [@enum_annot1] 
     EnumConstant1 = EnumValue1 | INITIAL; 
    [@enum_annot2] 
     EnumConstant2 = EnumValue2 | INITIAL; 
    [...] 
  } 
| DEFINE TYPE EnumTypeStack : EnumTypeBase[;]  
```

[`@type_annot1`](abencds_enum_type_anno.md) · [`@type_annot2`](abencds_enum_type_anno.md)

## Description

Defines a [CDS enumerated type](../../abap-glossary/abencds_enum_type_glosry.md) `EnumType`. An enumerated type defines a set of [enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md) `EnumConstant1`, `EnumConstant2`, ... and each constant is assigned an [enumerated value](../../abap-glossary/abenenumerated_value_glosry.md) `Enum1Value1`, `Enum1Value2`, .... [CDS enumerated elements](../../abap-glossary/abencds_enum_element_glosry.md) and [enumerated variables](../../abap-glossary/abenenumerated_variable_glosry.md) in ABAP that are typed with a CDS enumerated type may take only one of the enumerated values. The enumerated constants and enumerated values define the set of allowed values of an enumerated type.

The statement for defining an enumerated type is `DEFINE TYPE ... ENUM`. A list of enumerated constants and enumerated values is defined in curly brackets. If an enumerated type `EnumTypeStack` is typed using another enumerated type `EnumTypeBase`, the enumerated constants are inherited automatically and the addition `ENUM` can be left out.

The name `EnumType` of a CDS enumerated type is defined after the `DEFINE TYPE` statement. It is in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP. The general rules for CDS object names described in topic [ABAP CDS - General Syntax Rules](../abap-cds-syntax/abencds_general_syntax_rules.md) apply. The name of the CDS enumerated type must be the same as the name of the source code.

The [base type](../../abap-glossary/abenbase_type_glosry.md) `BaseType` determines the technical storage type of the enumerated constants and the CDS enumerated elements. The following can be specified as base type:

<table>
<thead>
<tr class="header">
<th><strong><code class="ph codeph">BaseType</code></strong></th>
<th><strong>Dictionary Type</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><code class="ph codeph">abap.int1</code></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">INT1</code></a></td>
</tr>
<tr class="even">
<td><code class="ph codeph">abap.int2</code></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">INT2</code></a></td>
</tr>
<tr class="odd">
<td><code class="ph codeph">abap.int4</code></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">INT4</code></a></td>
</tr>
<tr class="even">
<td><p><code class="ph codeph">abap.char( len )</code>.</p>
<p><code class="ph codeph">len</code> can be 1 to 8.</p></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">CHAR</code></a> with length <code class="ph codeph">len</code>.</td>
</tr>
<tr class="odd">
<td><p><code class="ph codeph">abap.numc( len )</code>.</p>
<p><code class="ph codeph">len</code> can be 1 to 8.</p></td>
<td><a href="abenddic_builtin_types.html"><code class="ph codeph">NUMC</code></a> with length <code class="ph codeph">len</code>.</td>
</tr>
</tbody>
</table>

The base type has the following effect:

- The enumerated values must comply with the base type and be within the value range of the base type.

- The base type describes how each enumeration value of the value set is stored internally. It is part of the compatibility checks during cast expressions and in comparisons with CDS enumerated elements.

- The base type is the technical storage type of a CDS enumerated type itself.

**Note:** The base type is the technical storage type of [CDS enumerated elements](../../abap-glossary/abencds_enum_element_glosry.md). However, in the code element information or in the debugger, the data type of CDS enumerated elements is displayed as `ENUM`.

**Components**

- Header annotations [`@type_annot1`](abencds_enum_type_anno.md), [`@type_annot2`](abencds_enum_type_anno.md), ... can be specified in front of the statement `DEFINE TYPE`. All header annotations are optional, and an enumerated type can also be created without any header annotations.

- Annotations for enumerated constants `enum_annot1`, `enum_annot2`, ... can optionally be specified in front of the enumerated constants to add semantic information. The following annotations are available for enumerated constants:

  - [`EndUserText.heading`](abencds_enum_type_anno.md)

  - [`EndUserText.label`](abencds_enum_type_anno.md)

- Enumerated constants `EnumConstant1`, `EnumConstant2`, ... contain the enumerated values `EnumValue1`, `EnumValue2`, ... The data type of each constant is the enumerated type `ENUM`. Each name `EnumConstant1`, `EnumConstant2`, must follow the [naming rules](../abap-cds-syntax/abencds_general_syntax_rules.md). Most importantly, it can have up to 30 characters and each name must be unique within the enumerated type.

- Enumerated values `EnumValue1`, `EnumValue2`, ... assign type-compliant values to the enumerated constants. Each enumerated value must be unique within the enumerated type. The order of the specified values is not important. The enumerated values are specified as [untyped literals](../../abap-glossary/abenuntyped_literal_glosry.md), and their content must be compatible with the base type of the CDS enumerated type in question.

- The addition `INITIAL` must be specified for exactly one constant. It generates the initial value of the base type.

## Hints

- An enumerated type is always an elementary data type. Likewise, the associated type description class `CL_ABAP_ENUMDESCR` is a subclass of `CL_ABAP_ELEMDESCR`.

- The enumerated values are specified as untyped literals. Internally, they are handled as typed literals of the base type, so the data type of the base type is used as a prefix.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Definition of an enumerated type `DEMO_CDS_ENUM_WEEKDAY`. The base type is `abap.int1` and the enumerated values of the enumerated constants `MON`, `TUE`, ... are 0 to 6.

``` abap
@EndUserText.label: 'Days of the week' 
define type DEMO_CDS_ENUM_WEEKDAY : abap.int1 enum 
{  
  @EndUserText.label: 'Monday' 
  MON = initial; 
  @EndUserText.label: 'Tuesday' 
  TUE =       1; 
  @EndUserText.label: 'Wednesday' 
  WED =       2; 
  @EndUserText.label: 'Thursday' 
  THU =       3; 
  @EndUserText.label: 'Friday' 
  FRI =       4; 
  @EndUserText.label: 'Saturday' 
  SAT =       5; 
  @EndUserText.label: 'Sunday' 
  SUN =       6; 
} 
 
 
```

The enumerated type can be used for declaring an enumerated variable `wd` in an ABAP program. By doing so, an [enumerated structure](../../abap-glossary/abenenumerated_structure_glosry.md) named `demo_cds_enum_weekday` is implicitly declared in the current context and can be used there. `wd` initially contains the content of the initial enumerated constant `demo_cds_enum_weekday-mon`. Note that the components of the structure are ordered alphabetically and not according to their definition.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA wd TYPE demo_cds_enum_weekday. 
 
ASSERT wd = demo_cds_enum_weekday-mon. 
 
out->write( demo_cds_enum_weekday ). 
 
out->display( ).
```

The class `CL_DEMO_CDS_ENUM_TYPE` uses the type description class `CL_ABAP_ENUMDESCR` to return properties of the CDS enumerated type `DEMO_CDS_ENUM_WEEKDAY`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES my_type TYPE demo_cds_enum_weekday. 
DATA  my_data TYPE my_type. 
 
FINAL(descr) = cl_abap_enumdescr=>describe_by_data( my_data ). 
 
out->next_section( 'CL_ABAP_ENUMDESCR' ). 
 
FINAL(enum_descr) = CAST cl_abap_enumdescr( 
cl_abap_typedescr=>describe_by_data( my_data ) ). 
 
out->write_data( enum_descr->kind 
      )->write_data( enum_descr->type_kind 
      )->write_data( enum_descr->base_type_kind 
      )->write_data( enum_descr->members ). 
 
out->display( ).
```

The CDS view entity `DEMO_CDS_ENUM_2` defines two CDS enumerated elements in its `SELECT` list:

- The field `weekday` casts the field `INT1` to the CDS enumerated type `DEMO_CDS_ENUM_WEEKDAY`.

- The field `EnumConstant` defines an enumerated constant as element in the `SELECT` list.

``` abap
@EndUserText.label: 'Cast to enum'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_ENUM_2
  as select from demo_ddic_types
{
  key id,
      int1,
      cast(int1 as DEMO_CDS_ENUM_WEEKDAY) as weekday,
      DEMO_CDS_ENUM_CHAR.#first_value     as EnumConstant
}
```

The following code snippets demonstrates access to the CDS view entity using ABAP SQL. It first inserts data into the database table `DEMO_DDIC_TYPES` and then it selects all elements from the CDS view entity. The columns `weekday` and `enumconstant` of the inline declared table `result` both have an enumerated type.

**Note:** If the field `INT1` contains a value that is not contained in the list of enumerated values of the CDS enumerated type `DEMO_CDS_ENUM_WEEKDAY`, a runtime error occurs.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
*fill database table 
DELETE FROM demo_ddic_types. 
INSERT demo_ddic_types FROM TABLE @( VALUE #( 
 ( id = 'A' int1 = 1 ) 
 ( id = 'B' int1 = 6 ) 
*( id = 'C' int1 = 7 ) -> runtime error. 7 is not an allowed value. 
) ). 
 
*SELECT from cds view entity 
SELECT * 
FROM demo_cds_enum_2 
INTO TABLE @DATA(result). 
 
*display result 
out->write( result ). 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS enumerated type `DEMO_CDS_ENUM_STACK` has the CDS enumerated type `DEMO_CDS_ENUM_WEEKDAY` as base type. It inherits the definition and the annotations of the referenced base type.

``` abap
@EndUserText.label: 'CDS enum typed with another enum' 
define type DEMO_CDS_ENUM_STACK: DEMO_CDS_ENUM_WEEKDAY
```

The following CDS view entity `DEMO_CDS_ENUM_TYPE_USAGE_1` uses an enumerated constant of the enumerated type as element of the `SELECT` list.

``` abap
@EndUserText.label: 'CDS view entity, enumerated types'

define view entity DEMO_CDS_ENUM_TYPE_USAGE_1
  as select from demo_expressions
{
  key id                       as Id,
  num1 as integer1,
      DEMO_CDS_ENUM_STACK.#FRI as friday
}
```

The following screenshot shows the code element information. The element typed with the enumerated type has the data type `enum(3)`. ![figure](images_enum.jpg)

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS enumerated type `DEMO_CDS_ENUM_BOOLEAN` demonstrates how a generally available Boolean data type might look like.

``` abap
@EndUserText.label: 'Boolean' 
define type DEMO_CDS_ENUM_BOOLEAN : abap.char(1) enum 
{ 
  @EndUserText.label: 'false' 
  FALSE = initial; 
  @EndUserText.label: 'true' 
  TRUE  = 'X'; 
}
```

The following code snippet shows its use in an ABAP program:

``` abap
DATA gui_flag TYPE demo_cds_enum_boolean. 
 
IF cl_demo_sap_gui=>check( ). 
  gui_flag = demo_cds_enum_boolean-true. 
ELSE. 
  gui_flag = demo_cds_enum_boolean-false. 
ENDIF.
```
