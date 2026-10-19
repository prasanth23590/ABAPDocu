---
title: "itab - STEP Examples"
source_file: abenloop_step_examples_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, Basic Form > LOOP AT itab, cond"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - STEP Examples

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates different usages of the addition `STEP`.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_step_examples DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    TYPES: 
      BEGIN OF customer_purchase, 
        cust_id    TYPE c LENGTH 8, 
        cust_name  TYPE string, 
        item_id    TYPE c LENGTH 9, 
        purch_date TYPE datn, 
        proc_date  TYPE datn, 
      END OF customer_purchase, 
      customer_purchases TYPE STANDARD TABLE OF customer_purchase 
        WITH EMPTY KEY. 
    METHODS: 
      constructor, 
      purchase_order, 
      quarterly_order, 
      discount, 
      tombola. 
 
  PRIVATE SECTION. 
    CONSTANTS co_example_customer TYPE c LENGTH 8 VALUE '00000001'. 
    DATA m_customer_purchases 
      TYPE customer_purchases. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_step_examples IMPLEMENTATION. 
  METHOD main. 
 
    me->purchase_order( ). 
    me->quarterly_order( ). 
    me->discount( ). 
    me->tombola( ). 
 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    m_customer_purchases = VALUE customer_purchases( 
            ( cust_id = '00000001' cust_name = `Customer A` 
              item_id = '781029348' purch_date = `20211108` 
              proc_date = `20211109` ) 
            ( cust_id = '00000001' cust_name = `Customer A` 
              item_id = '781028275' purch_date = `20211117` 
              proc_date = `20211118` ) 
            ( cust_id = '00000001' cust_name = `Customer A` 
              item_id = '781029350' purch_date = `20211203` 
              proc_date = `20211206` ) 
            ( cust_id = '00000002' cust_name = `Customer B` 
              item_id = '781029348' purch_date = `20211207` 
              proc_date = `20211208` ) 
            ( cust_id = '00000003' cust_name = `Customer C` 
              item_id = '781029353' purch_date = `20211215` 
              proc_date = `20211216` ) 
            ( cust_id = '00000004' cust_name = `Customer D` 
              item_id = '781029321' purch_date = `20211215` 
              proc_date = `20211216` ) 
            ( cust_id = '00000005' cust_name = `Customer E` 
              item_id = '781029342' purch_date = `20211216` 
              proc_date = `20211217` ) ). 
  ENDMETHOD. 
  METHOD discount. 
    TYPES: 
      BEGIN OF order, 
        tabix      TYPE sy-tabix, 
        item_id    TYPE c LENGTH 9, 
        purch_date TYPE datn, 
        proc_date  TYPE datn, 
      END OF order, 
      orders TYPE TABLE OF order WITH EMPTY KEY, 
 
      BEGIN OF discount_candidate, 
        tabix      TYPE sy-tabix, 
        item_id    TYPE c LENGTH 9, 
        purch_date TYPE datn, 
        proc_date  TYPE datn, 
      END OF discount_candidate, 
      discount_candidates TYPE TABLE OF discount_candidate 
        WITH EMPTY KEY. 
 
    DATA(orders) = VALUE orders( FOR <fs> IN m_customer_purchases 
      INDEX INTO idx STEP -1 WHERE ( cust_id = co_example_customer ) 
                                 ( tabix = idx item_id = <fs>-item_id 
                                   purch_date = <fs>-purch_date 
                                   proc_date = <fs>-proc_date ) ). 
 
    DELETE orders WHERE purch_date <= `20211001` 
      OR purch_date >= `20211231`. 
 
    FINAL(discounts) = VALUE discount_candidates( 
                            ( LINES OF orders FROM 3 STEP 3 ) ). 
 
    FINAL(is_discount_granted) = xsdbool( discounts IS NOT INITIAL ). 
 
    out->write( 
      |Discount of { m_customer_purchases[ cust_id = 
        co_example_customer ]-cust_name } ({ co_example_customer 
        }) granted: { is_discount_granted }| ). 
  ENDMETHOD. 
  METHOD purchase_order. 
    TYPES: 
      BEGIN OF order, 
        tabix      TYPE sy-tabix, 
        item_id    TYPE c LENGTH 9, 
        purch_date TYPE datn, 
        proc_date  TYPE datn, 
      END OF order. 
 
    DATA orders TYPE TABLE OF order. 
 
    LOOP AT m_customer_purchases REFERENCE INTO FINAL(customer_purchase) 
      STEP -1 WHERE cust_id = co_example_customer. 
      orders = VALUE #( BASE orders 
          ( tabix = sy-tabix item_id = customer_purchase->item_id 
            purch_date = customer_purchase->purch_date 
            proc_date = customer_purchase->proc_date ) ). 
    ENDLOOP. 
 
    out->write( |Orders of { m_customer_purchases[ cust_id = 
      co_example_customer ]-cust_name } ({ co_example_customer })| ). 
    out->write( orders ). 
  ENDMETHOD. 
  METHOD quarterly_order. 
    TYPES: 
      BEGIN OF order, 
        tabix      TYPE sy-tabix, 
        item_id    TYPE c LENGTH 9, 
        purch_date TYPE datn, 
        proc_date  TYPE datn, 
      END OF order, 
      orders TYPE TABLE OF order WITH EMPTY KEY, 
 
      BEGIN OF quarter, 
        quarter_start TYPE datn, 
        quarter_end   TYPE datn, 
      END OF quarter, 
      quarters TYPE TABLE OF quarter WITH EMPTY KEY. 
 
    DATA quarter_name TYPE string. 
 
    FINAL(quarters) = VALUE quarters( ( quarter_start = `20211001` 
                                       quarter_end = `20211231` ) ). 
 
    FINAL(quarter) = REF #( quarters[ lines( quarters ) ] ). 
 
    FINAL(q_start) = quarter->quarter_start. 
    FINAL(q_end) = quarter->quarter_end. 
 
    FINAL(orders) = VALUE orders( FOR <fs> IN m_customer_purchases 
      INDEX INTO idx STEP -1 WHERE ( purch_date >= q_start 
                                     AND purch_date <= q_end ) 
                                  ( tabix = idx item_id = <fs>-item_id 
                                    purch_date = <fs>-purch_date 
                                    proc_date = <fs>-proc_date ) ). 
 
    FINAL(quarter_start_month) = substring( val = q_start 
                                           off = 4 len = 2 ). 
 
    CASE quarter_start_month. 
      WHEN `01`. 
        quarter_name = `Quarter 1`. 
      WHEN `04`. 
        quarter_name = `Quarter 2`. 
      WHEN `07`. 
        quarter_name = `Quarter 3`. 
      WHEN `10`. 
        quarter_name = `Quarter 4`. 
    ENDCASE. 
 
    FINAL(quarter_year) = substring( val = q_start len = 4 ). 
 
    out->write( 
     |Orders of all customers in { quarter_name } { quarter_year }:| ). 
    IF orders IS NOT INITIAL. 
      out->write( orders ). 
    ELSE. 
      out->write( |No orders found.| ). 
    ENDIF. 
  ENDMETHOD. 
  METHOD tombola. 
    TYPES: 
      BEGIN OF customer_benefit, 
        cust_id          TYPE c LENGTH 8, 
        discount_granted TYPE abap_boolean, 
        tombola_won      TYPE abap_boolean, 
      END OF customer_benefit, 
      customer_benefits TYPE STANDARD TABLE OF customer_benefit 
        WITH EMPTY KEY. 
 
    DATA(customer_benefit) = VALUE customer_benefits( ). 
    DATA(win_candidates) = VALUE customer_benefits( ). 
 
    FINAL(customers_with_discounts) = VALUE customer_benefits( 
                                    ( cust_id = co_example_customer 
                                      discount_granted = abap_true ) ). 
 
    LOOP AT m_customer_purchases REFERENCE INTO FINAL(tombola) STEP 2 
         GROUP BY ( cust_id = tombola->cust_id ) 
           REFERENCE INTO FINAL(customer). 
      IF NOT line_exists( customers_with_discounts[ cust_id = 
                                                 customer->cust_id ] ). 
        INSERT VALUE #( cust_id     = customer->cust_id 
                        tombola_won = abap_true ) 
                      INTO TABLE win_candidates. 
      ENDIF. 
    ENDLOOP. 
 
    INSERT LINES OF customers_with_discounts 
      INTO TABLE customer_benefit. 
    INSERT LINES OF win_candidates STEP 2 INTO TABLE customer_benefit. 
 
    out->write( customer_benefit ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The table `customer_purchases` stores customer data and purchased item data. There are four methods which show the use of `STEP` in different contexts.

- Method `purchase_order`

  Looping across the lines of the internal table `customer_purchases` with `LOOP` and with `STEP -1`, indicating a backward loop, to get all purchase orders of a specific customer from the newest to the oldest date.

- Method `quarterly_order`

  Looping across the lines of the internal table `customer_purchases` with `FOR` and `STEP -1`, indicating a backward loop, within a specific time period from the newest to the oldest date.

- Method `discount`

  Looping across the lines of the internal table `customer_purchases` with `FOR` and `STEP -1` as for method `quarterly_order`. Inserting lines of the internal table `orders` when constructing the internal table `discount_candidates` with the additions `FROM 3` and `STEP 3` to get every third line starting from the third line.

- Method `tombola`

  Looping across the lines of the internal table `customer_purchases` with `STEP 2` to get every second line and grouping the lines with the group key `cust_id`. Inserting the lines of the internal table `win_candidates` into the internal table `customer_benefit` with `STEP 2` to get every second table line.
