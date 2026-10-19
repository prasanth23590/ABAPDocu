---
title: "ST - tt:read-write, Read or Write Variables"
source_file: abenst_tt_read_write.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Reading and Writing Variables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:read-write, Read or Write Variables

## Syntax

``` abap
<tt:read-write var="variable" [type="type" [length="len"] 
                                           [decimals="dec"]] 
                              [map="..."] 
                              [minLength|maxLength="len"] 
                              [xsd-type...] />  
```

## Description

The `tt:read-write` statement is a short form of the following two statements:

``` abap
<tt:read var="variable" [type="type" [length="len"] 
                                     [decimals="dec"]] 
                        [map="..."] 
                        [minLength|maxLength="len"] 
                        [xsd-type...] />
```

``` abap
<tt:write var="variable" [map="..."] 
                         [minLength|maxLength="len"] 
                         [xsd-type...] />
```

Specifying `tt:read-write` has the same effect as the statements [`tt:read`](abenst_tt_read.md) and [`tt:write`](abenst_tt_write.md) listed one directly after the other.

The attribute `type` and the attributes `length` and `decimals` specified using this attribute are respected by `tt:read` only. As with `tt:read`, the attribute `length` can only be specified together with `type`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Serialization and deserialization using a variable. In serializations, the variable `VARI` is assigned the value of the data object bound to `ROOT` and is written to XML using `read-write`. In deserializations, the value of the variable is read from XML and assigned to the data object bound to `ROOT`. The following example can be found as `DEMO_ST_READ_WRITE`.

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:variable name="VARI"/> 
  <tt:template> 
    <tt:assign ref="ROOT" to-var="VARI"/> 
    <X> 
      <tt:read-write var="VARI" type="STRING" 
                                minLength="10"/> 
    </X> 
    <tt:assign to-ref="ROOT" var="VARI"/> 
  </tt:template> 
</tt:transform>
```

The following ABAP program can call the transformation:

``` abap
DATA  str TYPE string. 
DATA xstr TYPE xstring. 
 
CALL TRANSFORMATION demo_st_read_write 
     SOURCE root = `abcde` 
     RESULT XML xstr. 
 
cl_abap_browser=>show_xml( xml_xstring = xstr ). 
 
CALL TRANSFORMATION demo_st_read_write 
     SOURCE XML xstr 
     RESULT root = str.
```

The result of the serialization is:

`<X>abcde </X>`

The transformation is not [symmetrical](abenst_symmetry.md) due to [`minLength`](abenst_length.md). After deserialization, the string `str` has at least 10 places.
