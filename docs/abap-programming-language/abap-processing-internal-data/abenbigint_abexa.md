---
title: "CL_ABAP_BIGINT, Key Encryption"
source_file: abenbigint_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > System Classes for Numbers > System Class CL_ABAP_BIGINT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CL_ABAP_BIGINT, Key Encryption

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example uses methods of the system class `CL_ABAP_BIGINT` to encrypt a text by generating public and private keys using the RSA algorithm.

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
CLASS cl_demo_bigint_rsa DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    TYPES: BEGIN OF ty_key, 
             exponent TYPE REF TO cl_abap_bigint, 
             modulus  TYPE REF TO cl_abap_bigint, 
             bits     TYPE i, 
           END OF ty_key, 
           BEGIN OF ty_print_key, 
             exponent TYPE string, 
             modulus  TYPE string, 
             bits     TYPE i, 
           END OF ty_print_key. 
    METHODS create_random_bigint 
      IMPORTING min_bits      TYPE i 
      RETURNING VALUE(bigint) TYPE REF TO cl_abap_bigint. 
    METHODS next_prime CHANGING bigint TYPE REF TO cl_abap_bigint. 
    METHODS encrypt IMPORTING message          TYPE string 
                              public_key       TYPE ty_key 
                    RETURNING VALUE(encrypted) 
                                TYPE REF TO cl_abap_bigint. 
    METHODS decrypt IMPORTING encrypted 
                                TYPE REF TO cl_abap_bigint 
                              private_key      TYPE ty_key 
                    RETURNING VALUE(decrypted) TYPE string. 
    METHODS create_bigint_from_xstring 
      IMPORTING xstring TYPE xstring 
      RETURNING VALUE(bigint) TYPE REF TO cl_abap_bigint. 
    METHODS create_xstring_from_bigint 
      IMPORTING bigint TYPE REF TO cl_abap_bigint 
      RETURNING VALUE(xstring) TYPE xstring. 
    METHODS make_key_printable IMPORTING key 
                                           TYPE ty_key 
                               RETURNING VALUE(printable_key) 
                                           TYPE ty_print_key. 
    METHODS generate_key IMPORTING bits 
                                     TYPE i 
                         EXPORTING public_key 
                                     TYPE ty_key 
                                   private_key TYPE ty_key. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_bigint_rsa IMPLEMENTATION. 
  METHOD main. 
 
    DATA p_bits TYPE i VALUE 128. 
    DATA: public_key     TYPE ty_key, 
          private_key    TYPE ty_key, 
          secret_message TYPE string VALUE `Hello ABAP` ##NO_TEXT. 
 
    cl_demo_input=>new( 
      )->add_field( CHANGING field = p_bits 
      )->request( ). 
 
    DATA(rsa) = NEW cl_demo_bigint_rsa( ). 
 
    rsa->generate_key( EXPORTING bits = p_bits 
                       IMPORTING public_key = public_key 
                                 private_key = private_key ). 
 
    IF private_key-bits <> p_bits. 
      out->write( `Number of bits was set to: ` && private_key-bits ) 
      ##NO_TEXT. 
    ENDIF. 
 
    out->write( 'PUBLIC KEY' ). 
    out->write( rsa->make_key_printable( public_key ) ). 
    out->write( 'PRIVATE KEY' ). 
    out->write( rsa->make_key_printable( private_key ) ). 
    out->write( 'SECRET_MESSAGE' ). 
    out->write( secret_message ). 
 
    DATA(encrypted) = rsa->encrypt( message = secret_message 
                                    public_key = public_key ). 
 
    out->write( 'ENCRYPTED' ). 
    out->write( encrypted->to_string( ) ). 
 
    DATA(decrypted) = rsa->decrypt( encrypted = encrypted 
                                    private_key = private_key ). 
 
    out->write( 'DECRYPTED' ). 
    out->write( decrypted ). 
 
    IF secret_message <> decrypted. 
      out->write( 'Need more bits for correct decryption' ) 
      ##NO_TEXT. 
    ENDIF. 
  ENDMETHOD. 
  METHOD create_bigint_from_xstring. 
    bigint = REDUCE #( INIT x = cl_abap_bigint=>factory_from_int4( ) 
                       FOR i = 0 UNTIL i >= xstrlen( xstring ) 
                       LET byte = xstring+i(1) IN 
                       NEXT x = x->mul_by_two_power( 8 )->add_int4( 
                         CONV #( byte ) ) ). 
  ENDMETHOD. 
  METHOD create_random_bigint. 
    DATA random TYPE xstring. 
    CALL FUNCTION 'GENERATE_SEC_RANDOM' 
      EXPORTING 
        length         = ceil( min_bits / 8 ) 
      IMPORTING 
        random         = random 
      EXCEPTIONS 
        invalid_length = 1 
        no_memory      = 2 
        internal_error = 3 
        OTHERS         = 4. 
    IF sy-subrc <> 0. 
      out->write( 'Could not generate random number' ). 
    ENDIF. 
    bigint = create_bigint_from_xstring( random ). 
  ENDMETHOD. 
  METHOD create_xstring_from_bigint. 
    TYPES lty_x TYPE x LENGTH 1. 
    DATA(cloned) = bigint->clone( ). 
    xstring = ``. 
 
    WHILE NOT cloned->is_zero( ). 
      DATA(byte) = CONV lty_x( cloned->mod_int4( 256 ) ). 
      xstring = byte && xstring. 
      cloned->div_by_two_power( 8 ). 
    ENDWHILE. 
  ENDMETHOD. 
  METHOD decrypt. 
    DATA(decrypted_number) = encrypted->clone( )->pow_mod( 
      io_exponent = private_key-exponent io_modulus = 
      private_key-modulus ). 
    DATA(xstring) = create_xstring_from_bigint( decrypted_number ). 
    decrypted = cl_abap_conv_codepage=>create_in( codepage = `1100` 
      )->convert( xstring ). 
  ENDMETHOD. 
  METHOD encrypt. 
    DATA xstring TYPE xstring. 
    encrypted = create_bigint_from_xstring( 
      cl_abap_conv_codepage=>create_out( codepage = `1100` 
      )->convert( message ) ). 
    encrypted->pow_mod( io_exponent = public_key-exponent io_modulus = 
      public_key-modulus ). 
  ENDMETHOD. 
  METHOD generate_key. 
    DATA p TYPE REF TO cl_abap_bigint. 
    DATA p_minus_1 TYPE REF TO cl_abap_bigint. 
    DATA q TYPE REF TO cl_abap_bigint. 
    DATA q_minus_1 TYPE REF TO cl_abap_bigint. 
    DATA n TYPE REF TO cl_abap_bigint. " modulus 
    DATA lambda TYPE REF TO cl_abap_bigint. " totient l(n) 
    DATA e TYPE REF TO cl_abap_bigint. " public exponent e 
    DATA d TYPE REF TO cl_abap_bigint. " private exponent d 
 
    " for simplicity we take always a bit number divisible by 8 
    DATA(min_bits) = ceil( bits / 2 ). 
 
    IF min_bits MOD 8 <> 0. 
      min_bits += ( 8 - ( min_bits MOD 8 ) ). 
    ENDIF. 
 
    " get two large prime numbers, p and q: 
    " minimum is 8 bits for simplicity 
    p = create_random_bigint( min_bits ). 
 
    next_prime( CHANGING bigint = p ). 
 
    p_minus_1 = p->clone( )->sub_int4( 1 ). 
 
    q = create_random_bigint( min_bits ). 
    next_prime( CHANGING bigint = q ). 
 
    IF p->compare( q ) = cl_abap_bigint=>equal. " very unlikely!! 
      q->add_int4( 2 ). 
      next_prime( CHANGING bigint = q ). 
    ENDIF. 
 
    ASSERT q->compare( p ) <> cl_abap_bigint=>equal. 
 
    q_minus_1 = q->clone( )->sub_int4( 1 ). 
 
    " compute modulus = p * q 
    n = p->clone( )->mul( q ). 
 
    " compute totient = lcm( (p - 1) * (q - 1) ) 
    lambda = p_minus_1->clone( )->mul( q_minus_1 )->div( 
      p_minus_1->clone( )->gcd( q_minus_1 ) )-quotient. 
 
    " create fixed exponent; is public anyways 
    e = cl_abap_bigint=>factory_from_int4( 65537 ). " best guess! 
 
    " assure gcd( lambda, e ) = 1 
    WHILE lambda->clone( )->gcd( e )->compare_int4( 1 ) <> 
      cl_abap_bigint=>equal. 
      e->add_int4( 2 ). " very unlikely!! 
      next_prime( CHANGING bigint = e ). 
    ENDWHILE. 
 
    " compute d * e = 1 mod lambda 
    d = e->clone( )->mod_inverse( lambda ). 
 
    ASSERT d->clone( )->mul( e )->mod( lambda )->compare_int4( 1 ) = 
      cl_abap_bigint=>equal. 
 
    public_key = VALUE #( modulus = n exponent = 
      e bits = n->get_number_of_bits( ) ). 
    private_key = VALUE #( modulus = n exponent = 
      d bits = n->get_number_of_bits( ) ). 
  ENDMETHOD. 
  METHOD make_key_printable. 
    printable_key = VALUE #( exponent = key-exponent->to_string( ) 
      modulus = key-modulus->to_string( ) bits = key-bits ). 
  ENDMETHOD. 
  METHOD next_prime. 
    IF bigint->mod_int4( 2 ) = 0. 
      bigint->add_int4( 1 ). 
    ENDIF. 
    WHILE bigint->is_prime( iv_iterations = 5 ) = 
      cl_abap_bigint=>no_prime. 
      bigint->add_int4( 2 ). 
    ENDWHILE. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Public and private RSA key pairs are generated using methods of the system class `CL_ABAP_BIGINT`. These key pairs are used to encrypt a text. The key pairs, as well as the encrypted and decrypted text, are generated as screen output.
