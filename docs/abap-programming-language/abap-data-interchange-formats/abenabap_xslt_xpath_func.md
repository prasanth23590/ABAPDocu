---
title: "XSL - User-defined XPath Functions"
source_file: abenabap_xslt_xpath_func.html
section: "ABAP Programming Language > ABAP - Data Interchange Formats > ABAP and XML > XML - Transformations > XSL Transformations > XSL - User-Defined Transformations > XSL - Instructions > XSL - SAP Instructions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# XSL - User-defined XPath Functions

User-defined XPath functions can be specified in XSLT programs using the instruction `sap:function`.

``` abap
<sap:function name="prefix:fName"> 
   <sap:argument    name = "arg1"/> 
   <sap:argument    name = "arg2"/> 
      ... 
   <sap:result      define = " 
                            <!-- function definition --> 
                            "/> 
</sap:function>
```

- All function arguments are declared using the sub-instruction `sap:argument`. They are specified only by their names.

- The result of the function is defined as an XPath expression for the `define` attribute within the sub-instruction `sap:result`. The function body can contain calls to previously defined functions.

## Hint

Multiple functions can be called with the same name, if they have different arguments.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

You can define a function for calculating the factorial as follows.

``` abap
<sap:function name ="p:fact"> 
   <sap:argument      name ="n"/> 
   <sap:result        define ="sapxsl:if($n &lt;= 0, 
                                        0, 
                                        sapxsl:if($n=1, 
                                                  1, 
                                                  $n*p:fact($n-1)))"/> 
</sap:function>
```
