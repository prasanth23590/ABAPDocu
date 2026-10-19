---
title: "Built-In Functions, Overview"
source_file: abenbuilt_in_functions_overview.html
section: "ABAP Programming Language > ABAP - Built-In Types, Data Objects, Functions, and Constructors > Built-In Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Built-In Functions, Overview

The following tables summarize the built-in functions by purpose. Built-in functions are generally [processing functions](../../abap-glossary/abenprocess_function_glosry.md) or [description functions](../../abap-glossary/abendescription_function_glosry.md).

- A processing function performs general processing and returns a return value according to its purpose.

- A description function determines a property of an [argument](../../abap-glossary/abenargument_glosry.md) and usually returns this property as a numeric value.

These include the logical functions, which either evaluate a logical expression as Boolean functions or return a truth value as a predicate function.

## Logical Functions

| **Function**                                                                                                                                      | **Meaning**                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| [`boolc`](../abap-program-flow-logic/abenboole_functions.md), [`boolx`](../abap-program-flow-logic/abenboole_functions.md), [`xsdbool`](../abap-program-flow-logic/abenboole_functions.md)                                   | Boolean functions                      |
| [`contains`](../abap-program-flow-logic/abencontains_functions.md), [`contains_any_of`](../abap-program-flow-logic/abencontains_functions.md), [`contains_any_not_of`](../abap-program-flow-logic/abencontains_functions.md) | Predicate functions for strings        |
| [`matches`](../abap-program-flow-logic/abenmatches_functions.md)                                                                                                           | Predicate function for strings         |
| [`line_exists`](../abap-program-flow-logic/abenline_exists_function.md)                                                                                                    | Predicate function for internal tables |

[***-\>* More about**](../abap-program-flow-logic/abenlogic_functions.md)

## Numeric Functions

| **Function**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **Meaning**                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| [`abs`](../abap-processing-internal-data/abennumerical_functions.md), [`ceil`](../abap-processing-internal-data/abennumerical_functions.md), [`floor`](../abap-processing-internal-data/abennumerical_functions.md), [`frac`](../abap-processing-internal-data/abennumerical_functions.md), [`sign`](../abap-processing-internal-data/abennumerical_functions.md), [`trunc`](../abap-processing-internal-data/abennumerical_functions.md)                                                                                                                                                                                                                                                                                                                                                     | General numeric functions        |
| [`ipow`](../abap-processing-internal-data/abenpower_function.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Integer power function           |
| [`nmax`](../abap-processing-internal-data/abennmax_nmin_functions.md), [`nmin`](../abap-processing-internal-data/abennmax_nmin_functions.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Numeric extremum functions       |
| [`acos`](../abap-processing-internal-data/abenfloating_point_functions.md), [`asin`](../abap-processing-internal-data/abenfloating_point_functions.md), [`atan`](../abap-processing-internal-data/abenfloating_point_functions.md), [`cos`](../abap-processing-internal-data/abenfloating_point_functions.md), [`sin`](../abap-processing-internal-data/abenfloating_point_functions.md), [`tan`](../abap-processing-internal-data/abenfloating_point_functions.md), [`cosh`](../abap-processing-internal-data/abenfloating_point_functions.md), [`sinh`](../abap-processing-internal-data/abenfloating_point_functions.md), [`tanh`](../abap-processing-internal-data/abenfloating_point_functions.md), [`exp`](../abap-processing-internal-data/abenfloating_point_functions.md), [`log`](../abap-processing-internal-data/abenfloating_point_functions.md), [`log10`](../abap-processing-internal-data/abenfloating_point_functions.md), [`sqrt`](../abap-processing-internal-data/abenfloating_point_functions.md) | Floating point functions         |
| [`round`](../abap-processing-internal-data/abendec_floating_point_functions.md), [`rescale`](../abap-processing-internal-data/abendec_floating_point_functions.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Rounding functions               |
| [`gamma`](../abap-processing-internal-data/abengamma_functions.md), [`log_gamma`](../abap-processing-internal-data/abengamma_functions.md), [`gamma_lower`](../abap-processing-internal-data/abenlower_gamma_functions.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Gamma functions                  |
| [`factorial`](../abap-processing-internal-data/abenfactorial_functions.md), [`binomial`](../abap-processing-internal-data/abenbinomial_functions.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Factorial and binomial functions |
| [`erf`](../abap-processing-internal-data/abenerror_functions.md), [`erfc`](../abap-processing-internal-data/abenerror_functions.md), [`erf_inv`](../abap-processing-internal-data/abenerror_functions.md), [`erfc_inv`](../abap-processing-internal-data/abenerror_functions.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                | Error functions                  |

[***-\>* More about**](../abap-processing-internal-data/abenmathematical_functions.md)

## Character String Functions

| **Function**                                                                                                                                                                                                                                         | **Meaning**                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| [`charlen`](../abap-processing-internal-data/abenlength_functions.md), [`dbmaxlen`](../abap-processing-internal-data/abenlength_functions.md), [`numofchar`](../abap-processing-internal-data/abenlength_functions.md), [`strlen`](../abap-processing-internal-data/abenlength_functions.md)                                                                                     | Length functions                        |
| [`char_off`](../abap-processing-internal-data/abenlength_functions_args.md)                                                                                                                                                                                                         | Length function                         |
| [`cmax`](../abap-processing-internal-data/abencmax_cmin_functions.md), [`cmin`](../abap-processing-internal-data/abencmax_cmin_functions.md)                                                                                                                                                                       | Character-like extremum value functions |
| [`count`](../abap-processing-internal-data/abencount_functions.md), [`count_any_of`](../abap-processing-internal-data/abencount_functions.md), [`count_any_not_of`](../abap-processing-internal-data/abencount_functions.md)                                                                                                                      | Search functions                        |
| [`distance`](../abap-processing-internal-data/abendistance_functions.md)                                                                                                                                                                                                            | Similarity function                     |
| [`condense`](../abap-processing-internal-data/abencondense_functions.md)                                                                                                                                                                                                            | Condense function                       |
| [`concat_lines_of`](../abap-processing-internal-data/abenconcatenation_functions.md)                                                                                                                                                                                                | Concatenation function                  |
| [`escape`](../abap-processing-internal-data/abenescape_functions.md)                                                                                                                                                                                                                | Escape symbol function                  |
| [`find`](../abap-processing-internal-data/abensearch_functions.md), [`find_end`](../abap-processing-internal-data/abensearch_functions.md), [`find_any_of`](../abap-processing-internal-data/abensearch_functions.md), [`find_any_not_of`](../abap-processing-internal-data/abensearch_functions.md)                                                                             | Search functions                        |
| [`insert`](../abap-processing-internal-data/abeninsert_functions.md)                                                                                                                                                                                                                | Insert function                         |
| [`match`](../abap-processing-internal-data/abenmatch_functions.md)                                                                                                                                                                                                                  | Substring function                      |
| [`repeat`](../abap-processing-internal-data/abenrepeat_functions.md)                                                                                                                                                                                                                | Repeat function                         |
| [`replace`](../abap-processing-internal-data/abenreplace_functions.md)                                                                                                                                                                                                              | Replace function                        |
| [`reverse`](../abap-processing-internal-data/abenreverse_functions.md)                                                                                                                                                                                                              | Reverse function                        |
| [`segment`](../abap-processing-internal-data/abensegment_functions.md)                                                                                                                                                                                                              | Segment function                        |
| [`shift_left`](../abap-processing-internal-data/abenshift_functions.md), [`shift_right`](../abap-processing-internal-data/abenshift_functions.md)                                                                                                                                                                  | Shift functions                         |
| [`substring`](../abap-processing-internal-data/abensubstring_functions.md), [`substring_after`](../abap-processing-internal-data/abensubstring_functions.md), [`substring_from`](../abap-processing-internal-data/abensubstring_functions.md), [`substring_before`](../abap-processing-internal-data/abensubstring_functions.md), [`substring_to`](../abap-processing-internal-data/abensubstring_functions.md) | Substring functions                     |
| [`to_upper`](../abap-processing-internal-data/abencase_functions.md), [`to_lower`](../abap-processing-internal-data/abencase_functions.md), [`to_mixed`](../abap-processing-internal-data/abencase_functions.md), [`from_mixed`](../abap-processing-internal-data/abencase_functions.md)                                                                                         | Case functions                          |
| [`translate`](../abap-processing-internal-data/abentranslate_functions.md)                                                                                                                                                                                                          | Translation function                    |

[***-\>* More about**](../abap-processing-internal-data/abenstring_functions.md)

## Byte Chain Functions

| **Function**                                       | **Meaning**     |
|----------------------------------------------------|-----------------|
| [`xstrlen`](../abap-processing-internal-data/abendescriptive_functions_binary.md) | Length function |
| [`bit-set`](../abap-processing-internal-data/abenbit_functions.md)                | Bit function    |

[***-\>* More about**](../abap-processing-internal-data/abenbinary_functions.md)

## Time Stamp Functions

| **Function**                                  | **Meaning**                         |
|-----------------------------------------------|-------------------------------------|
| [`utclong_current`](../abap-processing-internal-data/abenutclong_current.md) | Current UTC time stamp              |
| [`utclong_add`](../abap-processing-internal-data/abenutclong_add.md)         | Addition function for time stamps   |
| [`utclong_diff`](../abap-processing-internal-data/abenutclong_diff.md)       | Difference function for time stamps |

[***-\>* More about**](../abap-processing-internal-data/abentimestamp_functions.md)

## Functions for Internal Tables

| **Function**                                    | **Meaning**    |
|-------------------------------------------------|----------------|
| [`lines`](../abap-processing-internal-data/abendescriptive_functions_table.md) | Row function   |
| [`line_index`](../abap-processing-internal-data/abenline_index_function.md)    | Index function |

[***-\>* More about**](../abap-processing-internal-data/abenitab_functions.md)
