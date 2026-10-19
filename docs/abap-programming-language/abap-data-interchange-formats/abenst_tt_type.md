---
title: "ST - tt:type, tt:front, tt:node, Type Definitions"
source_file: abenst_tt_type.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Structure of ST Programs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:type, tt:front, tt:node, Type Definitions

## Syntax

``` abap
<tt:type name="..." [[line-]type="..." [length="..."] [decimals="..."]] 
  [extensible="..."]> 
  [<tt:front> 
     <tt:node name="..." [[line-]type="..." [...]] 
       [extensible="..."]> 
       [...] 
     </tt:node> 
     ... 
   </tt:front>] 
  [<tt:node name="..." [[line-]type="..." [...]] 
     [extensible="..."]> 
     [...] 
   </tt:node> 
  ...] 
</tt:type>  
```

## Description

The [data roots](abenst_tt_root.md) used in an ST program can optionally be assigned type specifications. As a rule, types from the repository (ABAP Dictionary, types of global classes) are used, although separate type definitions can also be made in the ST program. An ST program outside of a template can contain one or more definitions of types with statement `tt:type`. The attribute `name` is used to declare a symbolic name that can be used to type data roots and in other type definitions.

Elementary, structured, and tabular types can all be defined, which can be partially or completely generic. Moreover, references to globally defined data types of the repository and to types of the same ST program defined using `tt:type` are possible. Reference types cannot be defined as standalone types, but they can be created by using references to reference types from the ABAP repository.

**Namespaces**

The following XML namespaces in [asXML format](abenabap_xslt_asxml.md) must be used to specify types from the repository and from the same ST program:

- `http://www.sap.com/abapxml/types/dictionary` describes ABAP Dictionary.

- `http://www.sap.com/abapxml/types/type-pool/name` describes the type pool `name`.

- `http://www.sap.com/abapxml/types/class-pool/class` describes the global class `class`.

- `http://www.sap.com/abapxml/types/defined/name` describes the type that is defined in the current ST program using `tt:type`.

The type name that is specified in `[line-]type` then must have the form `p:NAME`, where the namespace prefix `p` must be bound to one of these URIs and `NAME` is the name of the actual type in uppercase letters. `p` therefore specifies where the type is defined.

**Definition of Elementary Types**

For the definition of elementary types, the elementary ABAP types `C`, `D`, `F`, `I`, `N`, `P`, `STRING`, `T`, `X` or `XSTRING` (uppercase) are specified for the attribute value `type` after `tt:type` or `tt:node`.

For types `C`, `N`, `P`, and `X`, the length can also be specified in the attribute `length`, and for type `P` the number of decimal places can be specified in attribute `decimals`. If `decimals` is specified without `length`, `decimals` is ignored. If `length` or `decimals` are not specified, the length and decimal places are generic.

`C` without a length specification corresponds to the generic ABAP type `csequence`, that is, it includes `c` with any length and `string`. Similarly, `xsequence` applies to `X`.

The name of an elementary type from the repository or the ST program can also be specified for the value of attribute `type`.

**Definition of Structured Types**

The statement `tt:node` is used as an element of `tt:type` to define structured types. Here the name of a component is determined by the value of the attribute `name` and its type is determined using the value of the attribute `[line-]type`. A statement `tt:node`, which is an element of a different statement `tt:node`, defines a substructure. An element `tt:type` or `tt:node` that contains subelements `tt:node` must not specify any types except using `[line-]type="?"`. In this case, `line-type="?"` is used to define a tabular type with a structured line type.

The type `[line-]type` can be specified after `tt:node` and can be used to structure the types of a component as elementary types (see above), as table-like (see below), or as using a reference to a structured type of the repository or the ST program itself.

The type of a component can be partly or completely generic. In addition, a structured type is generic by default in terms of the number and order of its components. This means that a data root that is typed with a structured type can be bound to an ABAP structure that contains the specified components in a different order and/or additional components.

To define the number and order of the components of the initial part of a structured type or of the entire structured type without gaps, the corresponding component definitions `tt:node` can be specified as subelements of the statement `tt:front`. The statement `tt:type` or `tt:node` may have exactly one `tt:front` statement as the first subelement.

To restrict the number of components in a structure to the components that are defined in the ST program, the `extensible` attribute of the statements `tt:type` or `tt:node` can be used. The following values can be specified for the attribute:

- `on`: The value *on* indicates that the current element may have direct subelements that are not explicitly specified.

- `deep`: The value *deep* states that the current element and its subelements can be enhanced and is the standard setting.

- `off`: The value *off* deactivates extensibility for the current element but not its subelements. In other words, direct subelements cannot be added to the element but its (specified) subelements can be.

- `deep-off`: The value *deep-off* deactivates extensibility for the current element and its subelements.

These settings can be overwritten locally in individual subelements.

**Definition of Tabular Types**

The attribute `line-type` of the elements `tt:type` and `tt:node` is used to define of tabular types. `line-type` defines the type or the component as a table with the line type that is specified as the value of the attribute.

Elementary types (see above) or any repository or ST program types can be specified as the line type. A structured line type can also be declared by specifying *?* as the value of `line-type`. If the current element then contains `tt:node` statements as subelements, these define the components of the line type.

The line type of a tabular type can be partly or completely generic. The latter is defined by specifying the type `line-type="?"` without defining components using `tt:node`.

**Definition of Reference Types**

There is currently no `ref-type` addition available in `tt:types` for the definition of reference types. Standalone reference types can be created only by using a reference to a reference type in the ABAP repository. [`tt:parameter`](abenst_tt_parameter.md) and [`tt:variable`](abenst_tt_variable.md), however, do have a `ref-type` addition.

**Definition of Generic Types**

All types whose properties have not been completely defined are generic in terms of the missing properties.

- A type is completely generic if the attribute `type` is either not specified at all, or is specified with the value *?*. Specifying `type="?"` is the same as not specifying anything. However, it should always be specified for reasons of readability. `line-type="?"` is also required to define a tabular type directly with a structured line type.

- An elementary type `N` or `P` is partly generic if the length or decimal places are not specified for `P`.

- Individual components can be generic in structured types and the number of components is also generic.

- Tabular types can be partly or completely generic in terms of the line type.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The type `T1` that is defined in transformation `DEMO_ST_NODE_TYPE` below is a structure that contains at least component `C`, which is an internal table whose line type contains at least the components `C1` (with dictionary type `DDT1`) and `C2` (with defined type `T2`). Structure type `T2` contains component `D` whose subcomponent `D1` is an internal table with any line type.

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates" 
  xmlns:ddic="http://www.sap.com/abapxml/types/dictionary" 
  xmlns:def="http://www.sap.com/abapxml/types/defined" > 
  <tt:type name="T1"> 
    <tt:node name="C" line-type="?"> 
      <tt:node name="C1" type="ddic:DDT1"/> 
       <tt:node name="C2" line-type="def:T2"/> 
    </tt:node> 
  </tt:type> 
  <tt:type name="T2"> 
    <tt:node name="D"> 
      <tt:node name="D1" line-type="?"/> 
    </tt:node> 
  </tt:type> 
</tt:transform>
```
