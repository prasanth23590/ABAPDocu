---
title: "ST - tt:loop, Internal Tables"
source_file: abenst_tt_loop.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Serialization and Deserialization > ST - Transformation of ABAP Values"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:loop, Internal Tables

## Syntax

``` abap
<tt:loop [ref="node"] [name="alias"]> 
  ... 
</tt:loop>  
```

## Description

Internal tables are serialized and deserialized within a loop defined by `tt:loop` that sets the [current node](abenst_tt_ref.md) to the current table line.

The optional attribute `ref` can be used to define the current node for the statement. If `ref` is not specified, the current node of the surrounding element is used implicitly. The ABAP data object that is bound to the current node must be an internal table.

The `name` attribute can be used to define an `alias` for the current node within the loop. In the `tt:loop` loop, the current node can then be addressed with `$alias`. When nested loops are used, the alias allows access to the current nodes of outer loops. If only one loop is used and in the outermost loop, `$alias` is equivalent to `$ref` when entering the loop.

**Serialization**

In serializations, a loop is run for the entire internal table. If the internal table is blank, processing continues after the element. In each loop pass, the current node of a data node is set further and the current ABAP table line is bound to the data node. The content of element `tt:loop`, which can contain any template elements, is processed for each data node.

**Deserialization**

In deserializations, the ABAP table is initialized and the content of element `tt:loop` is also executed in a loop. The XML data continues to be processed until a position is reached that cannot be processed with the content of the element. A new line is created in the bound ABAP table for each loop pass and is in turn bound to the current node. The XML values that are deserialized in the current loop pass are passed on to the current table line.

## Hints

- If it must be possible to deserialize a transformation, it must be possible to properly terminate loop executions, especially in the case of nested `tt:loop` loops. This is the case if the content of a `tt:loop` element can be compared with the sections to be deserialized. If the XML elements in a loop are not sufficient, the entire loop body can be enclosed with a literal XML element, for example, which defines a hierarchy level that can be evaluated during deserialization.

- In a Simple Transformation, a data node can either be handled exclusively as an internal table or not at all. This is especially true when splitting a template into different transformation directions.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the following symmetrical Simple Transformation `DEMO_ST_LOOP`, the internal table that is bound to the `ROOT` data roots and its table-like component `values` are serialized and deserialized in two nested `tt:loop` loops. For demonstration purposes, an alias called `line` is defined in the outermost loop and is addressed in the loop using `$line`. Since `$line` is not addressed in the inner loop, the definition of the alias name would not be necessary here.

``` abap
<?sap.transform simple?> 
<tt:transform 
  xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="ROOT"/> 
  <tt:template> 
    <tab1> 
      <tt:loop ref=".ROOT" name="line"> 
        <key> 
          <tt:value ref="$line.key" /> 
        </key> 
        <tab2> 
          <tt:loop ref="$line.values"> 
            <value> 
              <tt:value /> 
            </value> 
          </tt:loop> 
        </tab2> 
      </tt:loop> 
    </tab1> 
  </tt:template> 
</tt:transform>
```

The following ABAP program can call the transformation:

``` abap
TYPES: BEGIN OF line, 
         key    TYPE i, 
         values TYPE TABLE OF i WITH EMPTY KEY, 
       END OF line. 
 
DATA itab TYPE TABLE OF line WITH EMPTY KEY. 
DATA result LIKE itab. 
 
itab = 
  VALUE #( FOR j = 2 UNTIL j > 4 
           ( key    = j 
             values = VALUE #( ( j ** 2 ) 
                               ( j ** 3 ) 
                               ( j ** 4 ) ) ) ). 
 
CALL TRANSFORMATION demo_st_loop 
  SOURCE root = itab 
  RESULT XML DATA(xml_xstring). 
 
cl_abap_browser=>show_xml( EXPORTING xml_xstring = xml_xstring ). 
 
CALL TRANSFORMATION demo_st_loop 
  SOURCE XML xml_xstring 
  RESULT root = result.
```

The result of the serialization is the following:

``` abap
<tab1> 
  <key>2</key> 
  <tab2> 
    <value>4</value> 
    <value>8</value> 
    <value>16</value> 
  </tab2> 
  <key>3</key> 
  <tab2> 
    <value>9</value> 
    <value>27</value> 
    <value>81</value> 
  </tab2> 
  <key>4</key> 
  <tab2> 
    <value>16</value> 
    <value>64</value> 
    <value>256</value> 
  </tab2> 
</tab1>
```

The transformation is [symmetrical](abenst_symmetry.md). After deserialization, `result` has the same content as `itab`.
