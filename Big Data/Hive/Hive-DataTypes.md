# Data types supported in Hive (upto Hive 1.1.0)

## Numeric Types

* TINYINT
* SMALLINT
* INT
* BIGINT
* FLOAT
* DOUBLE
* DECIMAL

## Date/Time types

* TIMESTAMP (supported for avro only from Avro v1.8.0)
* DATE

## String Types

* STRING
* VARCHAR
* CHAR

## Misc

* BOOLEAN
* BINARY

## Complex Types

* ARRAY<data_type>
* MAP<primitive_type, data_type>
* STRUCT<col_name: dataype [COMMENT col_comment], ...>
* UNIONTYPE<data_type, data_type, ...>

## Literal Types

* Integral
  * TinyInt - Ex. 100**Y**
  * SmallInt - Ex. 100**S**
  * BIGINT - Ex. 100**L**
* String
  * Either single quotes or double quotes. C-style escaping within the string.

## Casting Types

Ex. `cast(timestamp as date)`