---
title: "ST - tt:serialize, tt:deserialize, Transformation Direction"
source_file: abenst_tt_serialize_deserialize.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Flow Control"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:serialize, tt:deserialize, Transformation Direction

## Syntax

``` abap
<tt:serialize> 
  ... 
</tt:serialize> 
 
<tt:deserialize> 
  ... 
</tt:deserialize>  
```

## Description

These ST statements can be used to limit parts of templates for execution in serializations or deserializations:

All template elements specified within the `tt:serialize` element are only respected in serializations. All the template elements specified within the `tt:deserialize` element are only respected in deserializations.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following Simple Transformation `DEMO_ST_SERIALIZE_DESERIALIZE` serializes a structure and deserializes to an internal table:

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT1"/> 
  <tt:root name="ROOT2"/> 
  <tt:template> 
    <X> 
      <tt:serialize> 
        <Y> 
          <tt:value ref=".ROOT1.COL1"/> 
        </Y> 
        <Y> 
          <tt:value ref=".ROOT1.COL2"/> 
        </Y> 
        <Y> 
          <tt:value ref=".ROOT1.COL3"/> 
        </Y> 
      </tt:serialize> 
      <tt:deserialize> 
        <tt:loop ref=".ROOT2"> 
          <Y> 
            <tt:value/> 
          </Y> 
        </tt:loop> 
      </tt:deserialize> 
    </X> 
  </tt:template> 
</tt:transform>
```

The following ABAP program can call the transformation:

``` abap
DATA xml_string TYPE string. 
 
DATA: BEGIN OF struc, 
        col1 TYPE i VALUE 1, 
        col2 TYPE i VALUE 2, 
        col3 TYPE i VALUE 3, 
      END OF struc. 
 
DATA itab TYPE TABLE OF i. 
 
CALL TRANSFORMATION demo_st_serialize_deserialize 
  SOURCE root1 = struc 
  RESULT XML xml_string. 
 
CALL TRANSFORMATION demo_st_serialize_deserialize 
  SOURCE XML xml_string 
  RESULT root2 = itab.
```

After deserialization, the internal table contains three lines with the values of the structure components.
