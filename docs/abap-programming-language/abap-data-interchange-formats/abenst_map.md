---
title: "ST - map, Mapping List"
source_file: abenst_map.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Transformation of ABAP Values > ST - tt:value, Elementary Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - map, Mapping List

## Syntax

``` abap
... map="..., val(a1, a2, ...) > xml(x), ..." ...   
... map="..., xml(x1, x2, ...) > val(a), ..." ...   
... map="..., val(a) = xml(x), ..." ...   
... map="..., xml(x) = val(a), ..." ...  
```

## Description

The attribute `map` can be used to specify a list of mapping rules for [`tt:value`](abenst_tt_value_elementary.md), [`tt:write`](abenst_tt_write.md), and [`tt:read`](abenst_tt_read.md). This is done to map a list of explicitly specified values to exactly one value when serializing or deserializing. A mapping list consists of a single mapping rule or a comma-separated list of multiple mapping rules. The following mapping rules are possible:

- `val(a1, a2, ...) > xml(x)`

  This mapping rule is evaluated in serializations. If the value of the current data node matches one of the specified values `a1`, `a2`, ... it is transformed to the value `x`.

- `xml(x1, x2, ...) > val(a)`

  This mapping rule is evaluated in deserializations. If the value of the current node matches one of the specified values `x1`, `x2`, ... it is transformed to the ABAP value `a`.

- `val(a) = xml(x)` and `xml(x) = val(a)`

  These mapping rules both mean the same thing and are evaluated in both serializations and deserializations. If the value of the current node corresponds to the specified value `a`, it is converted into value `x`, and vice versa.

The values `a`, `a1`, `a2`, ... must be specified in accordance with the [representation of ABAP values](abenst_abap_representation.md). The XML values `x`, `x1`, `x2`, ... must be enclosed in quotation marks.

## Hint

If mapping rules with more than one argument are used, the transformation is usually no longer [symmetrical](abenst_symmetry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Serialization of ABAP data using a mapping list with the transformation `DEMO_ST_MAPPING_LIST`:

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT1"/> 
  <tt:root name="ROOT2"/> 
  <tt:template> 
    <X0> 
      <X1> 
        <tt:value  ref="ROOT1" 
            map="val(C('Woman'), C('Man')) > xml('Person')" /> 
      </X1> 
      <X2> 
        <tt:value  ref="ROOT2" 
            map="val(C('Woman'), C('Man')) > xml('Person')" /> 
      </X2> 
    </X0> 
  </tt:template> 
</tt:transform>
```

The transformation is not [symmetrical](abenst_symmetry.md). In the following ABAP program, `field1` and `field2` contain the value *Person* after deserialization.

``` abap
DATA xml_string TYPE string. 
 
DATA(o) = cl_demo_output=>new( ). 
 
DATA field1 TYPE string VALUE 'Woman'. 
DATA field2 TYPE string VALUE 'Man'. 
 
o->write( field1 
)->write( field2 ). 
 
CALL TRANSFORMATION demo_st_mapping_list 
  SOURCE root1 = field1 
         root2 = field2 
  RESULT XML xml_string. 
 
o->write( xml_string ). 
 
CALL TRANSFORMATION demo_st_mapping_list 
  SOURCE XML xml_string 
  RESULT root1 = field1 
         root2 = field2. 
 
o->write( field1 
)->write( field2 
)->display( ).
```
