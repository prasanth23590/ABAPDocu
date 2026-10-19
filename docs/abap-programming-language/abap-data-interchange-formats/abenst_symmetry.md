---
title: "ST - Symmetry of Serialization and Deserialization"
source_file: abenst_symmetry.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - Symmetry of Serialization and Deserialization

The language constructs of Simple Transformations support the formulation of reversible transformations, that is, of programs that provide the original values in the execution order serialization - deserialization (or vice versa). However, it is also possible to write programs that cannot be reversed.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The simple example `DEMO_ST_SYMMETRY` illustrates a non-symmetrical transformation. Since the [`tt.value`](abenst_tt_value_elementary.md) statements are not enclosed in separate elements, the serialized values of `ROOT1` and `ROOT2` are grouped in *X*.

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT1"/> 
  <tt:root name="ROOT2"/> 
  <tt:template> 
    <X> 
      <tt:value ref="ROOT1"/> 
      <tt:value ref="ROOT2"/> 
    </X> 
  </tt:template> 
</tt:transform>
```

The following ABAP program can call the transformation:

``` abap
DATA xml_string TYPE string. 
DATA field1 TYPE string VALUE 'Hello'. 
DATA field2 TYPE string VALUE ' World!'. 
 
DATA result1 LIKE field1. 
DATA result2 LIKE field2. 
 
CALL TRANSFORMATION demo_st_symmetry 
  SOURCE root1 = field1 
         root2 = field2 
  RESULT XML xml_string. 
 
CALL TRANSFORMATION demo_st_symmetry 
  SOURCE XML xml_string 
  RESULT root1 = result1 
         root2 = result2.
```

The result of the serialization is:

`<X>Hello World!</X>`

Accordingly, the result of the deserialization to `result1` is `"Hello World!"`, while `result2` retains its initial value, which is different from the original content of `field1` and `field2`.

For a symmetrical transformation, the `tt:value` statements each have to appear in separate elements, or they must be separated by a unique text (which cannot appear in the first value).
