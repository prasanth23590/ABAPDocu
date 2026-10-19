---
title: "bit_exp - Bit Operators"
source_file: abenbit_operators.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Byte Chain Processing > Bit Expressions (bit_exp)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# bit_exp - Bit Operators

Bit operators work with the individual bits of the operands. The [calculation length](../../abap-glossary/abencalculation_length_glosry.md) is determined by the operands involved. Combining two operands with `BIT-AND`, `BIT-OR`, and `BIT-XOR` produces a result of this length in which each bit is set according to the table from the bits of the corresponding positions in the operands. `BIT-NOT` changes the bits of the operands to its right as shown in the table.

| `x` | `y` | `BIT-NOT x` | `x BIT-AND y` | `x BIT-XOR y` | `x BIT-OR y` |
|-----|-----|-------------|---------------|---------------|--------------|
| 0   | 0   | 1           | 0             | 0             | 0            |
| 0   | 1   | 1           | 0             | 1             | 1            |
| 1   | 0   | 0           | 0             | 1             | 1            |
| 1   | 1   | 0           | 1             | 0             | 1            |

The order of the columns in the table reflects the priority of the bit operators. The operator `BIT-NOT` has the highest, and `BIT-OR` the lowest priority. Within one [level of parentheses](abenbit_brackets.md), the results of operators with higher priority are formed before the results with operators of a lower priority. For adjacent operators of the same priority, the evaluation is performed from left to right, except for the operator `BIT-NOT`, which is executed from right to left.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of various bit operators.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES output TYPE TABLE OF xstring WITH EMPTY KEY. 
DATA hex1 TYPE xstring VALUE '0011'. 
DATA hex2 TYPE xstring VALUE '0101'. 
out->write( VALUE output( 
  ( hex1 BIT-AND hex2 ) 
  ( hex1 BIT-OR hex2  ) 
  ( hex1 BIT-XOR hex2 ) ) ). 
 
out->display( ).
```

The displayed result is:

``` abap
0001 
0111 
0110
```
