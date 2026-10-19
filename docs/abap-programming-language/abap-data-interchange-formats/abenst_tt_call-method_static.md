---
title: "ST - tt:call-method, Calling Static Methods"
source_file: abenst_tt_call-method_static.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > Simple Transformations (ST) > ST - Access to ABAP Objects from ST"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ST - tt:call-method, Calling Static Methods

## Syntax

``` abap
<tt:call-method class="class" [s-|d-]name="meth" 
                              [writer = "writer_para"] 
                              [reader = "reader_para"] 
  [<tt:with-parameter [s-|d-]name="para1" 
                      [ref="node1"|val="val1"|var="var1"] /> 
   <tt:with-parameter [s-|d-]name="para2" 
                      [ref="node2"|val="val2"|var="var2"] /> 
   ...] 
</tt:call-method>  
```

## Description

Using this variant of the statement `tt:call-method`, it is possible to call a static method of a global ABAP Objects class in an ST program as follows: `class` can be used to specify a class from the class library and `meth` can be used to specify a visible method of this class. This is not case-sensitive. The method is called for both serializations and deserializations when `name` is specified and it is called for serializations only when `s-name` is specified and for deserializations only when `d-name` is specified.

The interface parameters `para1`, `para2`, ... of the called method can or must be bound to actual parameters using the ST statement `tt:with-parameter`. The attribute `name` specifies the name of a formal parameter. An actual parameter is bound to this attribute only in serializations if `s-name` is specified and only in deserializations if `d-name` is specified. In certain cases, this allows a single method to be used for both directions. As actual parameters, `ref` can be used to specify data roots, `var` to specify variables or parameters, and `val` to specify [values](abenst_abap_representation.md). Depending on the type of formal parameter, the values of the specified actual parameters are either passed in the call or copied when the called method ends.

When binding actual parameters, read-only access to data roots is possible only in serializations, which is why they can only be passed to input parameters of the method. Conversely, in deserializations, only writes can be performed on data roots, which is why they can be used only by output parameters or return values.

The type of an actual parameter must match the typing of the interface parameter. The type of a data root, which can itself be typed in the statement [`tt:root`](abenst_tt_root.md), is determined by the type of the bound ABAP data object. Parameters and variables do not have a static type, unless the addition `ref-type` of the statements [`tt:parameter`](abenst_tt_parameter.md) or [`tt:variable`](abenst_tt_variable.md) defines them as reference variables. Data reference variables defined in this way can be bound to interface parameters of the same type.

When a method is called, control is passed from the ST processor to the ABAP processor of the ABAP runtime framework. There are no restrictions on which statements can be executed in the method. If `ENDMETHOD` or `RETURN` is used to end a method correctly, control is passed to the ST processor again and the ST program resumes after `tt:call-method`. Otherwise, control does not return to the ST program:

- If a statement such as `LEAVE PROGRAM`, `SUBMIT` without the addition `AND RETURN`, or `LEAVE TO TRANSACTION` is used to exit the method, the program responds as if the method were called from an ABAP program, that is, the current [internal session](../../abap-glossary/abeninternal_session_glosry.md) is deleted, together with the ST program.

- If the method is terminated by a class-based exception so that the exception is propagated from the method, the statement [`CALL TRANSFORMATION`](abapcall_transformation.md) is terminated with the catchable exception `CX_ST_CALL_METHOD_ERROR`. The `EXCEPTION_NAME` attribute of the exception object then contains the name of the original exception.

- Non-class-based exceptions cannot be handled. A method terminated using a non-class-based exception always causes a runtime error.

If ABAP data objects are modified in the called method, and these data objects are bound to data roots of the calling ST program, these modifications take effect immediately in the ST program. The following restriction applies: If a method is called within a [`tt:loop`](abenst_tt_loop.md) loop, serialization within the method (and within further nested `tt:loop` loops) only allows read-only access to the current internal table or its components. Deserialization within the method does not allow any access. Otherwise, a runtime error occurs.

The optional attributes `writer` and `reader` can be used to specify the input parameters `writer_para` or `reader_para` of the called method that must be typed with the reference types `IF_SXML_WRITER` or `IF_SXML_READER`. If `s-name` is specified, only `writer` can be specified. If `d-name` is specified, only `reader` can be specified. If `name` is specified, both attributes can be specified. `writer` is used for serialization and `reader` is used for deserialization. These attributes can be used to pass a reference to the [XML writer](../../abap-glossary/abenxml_writer_glosry.md) or the [XML reader](../../abap-glossary/abenxml_reader_glosry.md), created by `CALL TRANSFORMATION`, to the called method. In this method, the relevant interface can be used to access the reader or writer.

## Hint

If variables or parameters are bound to the interface parameters of called methods, it should be noted that these variables or parameters can be serialized or deserialized only if they contain elementary values.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following transformation exists as `DEMO_ST_WITH_METHOD_CALL` in AS ABAP. In a serialization in a `tt:loop` loop, it uses the data root `SCARR_TAB` to call the static method `GET_FLIGHTS` of the global class `CL_DEMO_CALL_FROM_ST`. This passes the component `carrid` of the internal table `scarr_tab` to the input parameter of the method.

``` abap
<?sap.transform simple?> 
<tt:transform xmlns:tt="http://www.sap.com/transformation-templates"> 
  <tt:root name="SCARR_TAB"/> 
  <tt:root name="SPFLI_TAB"/> 
  <tt:variable name="carrid"/> 
  <tt:template> 
    <FlightList> 
      <tt:loop ref=".SCARR_TAB"> 
        <Flights> 
          <tt:attribute name="Carrier" value-ref="CARRNAME"/> 
          <tt:assign ref="carrid" to-var="carrid"/> 
          <tt:call-method class="CL_DEMO_CALL_FROM_ST" 
                          s-name="GET_FLIGHTS"> 
            <tt:with-parameter name="CARRID" var="carrid"/> 
          </tt:call-method> 
          <tt:loop ref=".SPFLI_TAB"> 
            <Connection> 
              <tt:attribute name="ID" value-ref="CONNID"/> 
              <From> 
                <tt:value ref="CITYFROM"/> 
              </From> 
              <To> 
                <tt:value ref="CITYTO"/> 
              </To> 
            </Connection> 
          </tt:loop> 
        </Flights> 
      </tt:loop> 
    </FlightList> 
  </tt:template> 
</tt:transform>
```

The Simple Transformation can be called in the method `MAIN` of the same class `CL_DEMO_CALL_FROM_ST`. The internal tables `scarr_tab` and `spfli_tab` are both static attributes of the class. `scarr_tab` is filled and passed to the transformation data root with the same name, whereas `spfli_tab` remains empty and is filled differently in each loop pass in the method `GET_SPFLI` called from the Simple Transformation in accordance with the parameter `carrid`.

The method `MAIN` produces the following result:

``` abap
<FlightList> 
  <Flights Carrier="American Airlines"> 
    <Connection ID="0017"> 
      <From>NEW YORK</From> 
      <To>SAN FRANCISCO</To> 
    </Connection> 
    <Connection ID="0064"> 
      <From>SAN FRANCISCO</From> 
      <To>NEW YORK</To> 
    </Connection> 
    <Connection ID="0555"> 
      <From>ROME</From> 
      <To>FRANKFURT</To> 
    </Connection> 
    ... 
  </Flights> 
  <Flights Carrier="Air Berlin"> 
    ... 
  </Flights> 
</FlightList>
```

The class uses the binding of the attribute `spfli_tab` to the Simple Transformation and write access to this attribute in the called method to enable write access to data nodes during serialization within the ST program. In this way, it bypasses the restriction that a data node cannot be written during serialization within the ST program itself.
