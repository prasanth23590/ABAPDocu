---
title: "System Class for Probability Distribution"
source_file: abenprobability_dist_class.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > System Classes for Numbers"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# System Class for Probability Distribution

The following system classes are available for probability distribution:

- `CL_ABAP_PROB_DISTRIBUTION`: Defines probability distributions in ABAP for probabilities of a floating point data type.

- `CL_ABAP_PROB_DISTRIBUTION_DF34`: Defines probability distributions in ABAP for probabilities of the built-in data type `decfloat34`.

Both classes allow the generation of random numbers and calculation of quantile, probabilities, and other aspects. The following distributions are included: normal, log-normal, gamma, exponential, and uniform ` INT4`/`INT8` distributions. Discrete and continuous distributions are supported.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example generates 10 random numbers in the value range 1 - 50.

``` abap
DATA(random_nums) = cl_abap_random=>create( 
  seed = cl_abap_random=>seed( ) ). 
DATA rt TYPE if_abap_prob_types=>int_range. 
rt = VALUE #( ( sign = 'I' option = 'BT' low = 1 high = 50 ) ). 
DATA(distribution) = 
  cl_abap_prob_distribution=>get_uniform_int_distribution( range = rt ). 
DATA(int_tab) = distribution->next_random_numbers( count = 10 
                                                   rng = random_nums ).
```
