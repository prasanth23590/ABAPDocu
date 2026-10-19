---
title: "Random Numbers"
source_file: abenrandom_number_class.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > System Classes for Numbers"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Random Numbers

The class `CL_ABAP_RANDOM` calls the pseudo random number generator *Mersenne Twister* for different numeric types.

For the one-dimensional case, the following special classes generate random numbers for the different numeric types:

- `CL_ABAP_RANDOM_INT` for type `i`

- `CL_ABAP_RANDOM_INT8` for type `int8`

- `CL_ABAP_RANDOM_FLOAT` for type `f`

- `CL_ABAP_RANDOM_PACKED` for type `p`

- `CL_ABAP_RANDOM_PACKED_DEC1` to `CL_ABAP_RANDOM_PACKED_DEC14` for type `p` with 1 to 14 decimal places.

- `CL_ABAP_RANDOM_DECFLOAT16` for type `decfloat16`

- `CL_ABAP_RANDOM_DECFLOAT34` for type `decfloat34`

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Creation of a pseudo random number of the type `i` between 1 and 100, initialized by the UTC time.

``` abap
FINAL(time) = cl_demo_date_time=>get_utc_time( ). 
FINAL(r) = cl_abap_random_int=>create( seed = CONV i( time ) 
                                       min  = 1 
                                       max  = 100 ).
```
