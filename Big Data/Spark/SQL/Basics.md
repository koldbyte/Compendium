# Spark SQL

The entry point into all functionality in Spark SQL is the SQLContext class, or one of its descendants. To create a basic SQLContext, all you need is a SparkContext.

```scala
val sc: SparkContext // An existing SparkContext.
val sqlContext = new org.apache.spark.sql.SQLContext(sc)

// this is used to implicitly convert an RDD to a DataFrame.
import sqlContext.implicits._
```

## Running SQL queries

The sql function on a SQLContext enables applications to run SQL queries programmatically and returns the result as a DataFrame.

```scala
val sqlContext = ... // An existing SQLContext
val df = sqlContext.sql("SELECT * FROM table")
```

## Read write Dataframes

```scala
val df = sqlContext.read.format("json").load("examples/src/main/resources/people.json")
df.select("name", "age").write.format("parquet").save("namesAndAges.parquet")
```

## Make Dataframe available as table

```scala
// Register this DataFrame as a table.
people.registerTempTable("people")
```

## Supported Hive Features

Spark SQL supports the vast majority of Hive features, such as:

* Hive query statements, including:
  * SELECT
  * GROUP BY
  * ORDER BY
  * CLUSTER BY
  * SORT BY
* All Hive operators, including:
  * Relational operators (=, ⇔, ==, <>, <, >, >=, <=, etc)
  * Arithmetic operators (+, -, *, /, %, etc)
  * Logical operators (AND, &&, OR, ||, etc)
  * Complex type constructors
  * Mathematical functions (sign, ln, cos, etc)
  * String functions (instr, length, printf, etc)
* User defined functions (UDF)
* User defined aggregation functions (UDAF)
* User defined serialization formats (SerDes)
* Window functions
* Joins
  * JOIN
  * {LEFT|RIGHT|FULL} OUTER JOIN
  * LEFT SEMI JOIN
  * CROSS JOIN
* Unions
* Sub-queries
  * SELECT col FROM ( SELECT a + b AS col from t1) t2
* Sampling
* Explain
* Partitioned tables including dynamic partition insertion
* View
* All Hive DDL Functions, including:
  * CREATE TABLE
  * CREATE TABLE AS SELECT
  * ALTER TABLE
* Most Hive Data types, including:
  * TINYINT
  * SMALLINT
  * INT
  * BIGINT
  * BOOLEAN
  * FLOAT
  * DOUBLE
  * STRING
  * BINARY
  * TIMESTAMP
  * DATE
  * ARRAY<>
  * MAP<>
  * STRUCT<>
