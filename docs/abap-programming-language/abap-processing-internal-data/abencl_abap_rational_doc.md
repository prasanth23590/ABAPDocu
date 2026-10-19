---
title: "System Class CL_ABAP_RATIONAL"
source_file: abencl_abap_rational_doc.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > System Classes for Numbers"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# System Class CL_ABAP_RATIONAL

The documented system class `CL_ABAP_RATIONAL` contains methods for calculating with rational numbers without any precision loss. All basic operations, such as addition, multiplication, division, and subtraction, can be performed without any rounding errors.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of any rational numbers from string values using the method `FACTORY_FROM_STRING` of the class `CL_ABAP_RATIONAL`.

``` abap
DATA(lo_rational) = cl_abap_rational=>factory_from_string( 
  EXPORTING iv_value = 
`123451319241923741092743102751927431209374123461928374612983746129` & 
`3461293641239461293641237946192785619264124` ). 
 
 
" do some calculations 
"multiplication 
lo_rational->mul( cl_abap_rational=>factory_from_string( 
  `12345131924192374109274310275192743120937412346192837461298374612` & 
  `93461293641239461293641237946192785619264124` ) ). 
 
"division 
lo_rational->div( cl_abap_rational=>factory_from_string( 
`1234513192419237410927431027519274312093741234619283746129837461293` & 
`461293641239461293641237946192785619264124` ) ). 
 
"addition 
lo_rational->add( cl_abap_rational=>factory_from_string( 
  `12345131924192374109274310275192743120937412346192837461298374612` & 
  `93461293641239461293641237946192785619264124` ) ). 
 
"subtraction 
lo_rational->sub( cl_abap_rational=>factory_from_string( 
`1234513192419237410927431027519274312093741234619283746129837461293` & 
`461293641239461293641237946192785619264124` ) ).
```
