# DataFrames API

A DataFrame is equivalent to a relational table in Spark SQL

## Actions

### **collect()**

Returns an array that contains all of Rows in this DataFrame.

Running collect requires moving all the data into the application's driver process, and doing so on a very large dataset can crash the driver process with OutOfMemoryError.

### **count()**

Returns the number of rows in the DataFrame.

### __describe(cols: String*)__

Computes statistics for numeric columns, including count, mean, stddev, min, and max.

### **first()**

Returns the first row. Alias for head().

### **head(n : Int)**

Returns the first row

### **show(numrows = 20, truncate = true)**

Displays the DataFrame in a tabular form.

### **take(n : Int)**

Returns the first n rows in the DataFrame

## Basic DataFrame function

### **as[U](implicit arg0: Encoder): Dataset[U]**

Converts this DataFrame to a strongly-typed Dataset containing objects of the specified type, U.

### **cache()**

Persist this DataFrame with the default storage level (MEMORY_AND_DISK).

### **columns()**

Returns all column names as an array

### **explain(extended: Boolean)**

Prints the plans (logical and physical) to the console for debugging purposes.

### **persist(newLevel: StorageLevel = MEMORY_AND_DISk)**

Persist this DataFrame with the given storage level.

### **printSchema()**

Prints the schema to the console in a nice tree format

### **registerTempTable(tableName: String)**

Registers this DataFrame as a temporary table using the given name.

### **schema**

Returns the schema of this DataFrame.

### __toDF(colNames: String*)__

Returns a new DataFrame with columns renamed

### **unpersist(blocking: Boolean)**

Mark the DataFrame as non-persistent, and remove all blocks for it from memory and disk.

## Language Integrated Queries

### **agg**

* agg(expr: Column, exprs: Column*)

```scala
// df.agg(...) is a shorthand for df.groupBy().agg(...)
df.agg(max($"age"), avg($"salary"))
df.groupBy().agg(max($"age"), avg($"salary"))
```

### **alias**

* alias(alias: String)

Returns a new DataFrame with an alias set. Same as `as`.

### **apply**, **col**

* apply(colName: String)
* col(colName: String)

Selects column based on the column name and return it as a Column.

Note: In Scala, `$"col-name"` returns Column using implicits.

### **cube**

* cube(col1: String, cols: String*)5

Create a multi-dimensional cube for the current DataFrame using the specified columns, so we can run aggregation on them.

```scala
// Compute the average for all numeric columns cubed by department and group.
df.cube("department", "group").avg()
```

See [Mastering Spark SQL Gitbook](https://jaceklaskowski.gitbooks.io/mastering-spark-sql/spark-sql-multi-dimensional-aggregation.html#cube) for examples.

### **distinct**

* distinct()

Returns a new DataFrame that contains only the unique rows from this DataFrame. This is an alias for    `dropDuplicates`.

### **drop**

* drop(colName: String)

Returns a new DataFrame with a column dropped. This is a no-op if the DataFrame doesn't have a column with an equivalent expression.

### **except**

* except(other: DataFrame)

Returns a new DataFrame containing rows in this frame but not in another frame. This is equivalent to EXCEPT in SQL.

### **explode**

* explode[A, B](inputColumn: String, outputColumn: String)(f: (A) ⇒ TraversableOnce[B])(implicit arg0: scala.reflect.api.JavaUniverse.TypeTag[B])

```scala
df.explode("words", "word"){words: String => words.split(" ")}
```

* explode[A <: Product](input: Column*)(f: (Row) ⇒ TraversableOnce[A])(implicit arg0: scala.reflect.api.JavaUniverse.TypeTag[A])

Returns a new DataFrame where a single column has been expanded to zero or more rows by the provided function. This is similar to a LATERAL VIEW in HiveQL. All columns of the input row are implicitly joined with each value that is output by the function.

```scala
case class Book(title: String, words: String)
val df: RDD[Book]

case class Word(word: String)
val allWords = df.explode('words) {
  case Row(words: String) => words.split(" ").map(Word(_))
}

val bookCountPerWord = allWords.groupBy("word").agg(countDistinct("title"))
```

### **filter**

* filter(conditionExpr: String)

`df.filter("age > 10")`

### **groupBy**

Groups the DataFrame using the specified columns, so we can run aggregation on them.

* groupBy(col1: String, cols: String*)

`df.groupBy("age", "salary")`

* groupBy(cols: Column*)

`df.groupBy($"age", $"salary")`

### **intersect**

Returns a new DataFrame containing rows only in both this frame and another frame.

### **join**

Inner join with another DataFrame, using the given join expression.

* join(right: DataFrame, joinExprs: Column, joinType: String)

Join types : inner, outer, left_outer, right_outer, leftsemi

```scala
// Scala:
import org.apache.spark.sql.functions._
df1.join(df2, $"df1Key" === $"df2Key", "outer")
```

* join(right: DataFrame, joinExprs: Column)

```scala
// The following two are equivalent:
df1.join(df2, $"df1Key" === $"df2Key")
df1.join(df2).where($"df1Key" === $"df2Key")
```

### **limit**

Returns a new DataFrame by taking the first n rows.

### **na**

Returns a DataFrameNaFunctions for working with missing data.

`df.na.drop()`

Other functions available: fill, replace

### **orderBy**

Returns a new DataFrame sorted by the given expressions.

* orderBy(sortExprs: Column*)

`df.orderBy($"age")`

* orderBy(sortCol: String, sortCols: String*)

`df.orderBy("age")`

### **repartition**

Returns a new DataFrame partitioned by the given partitioning expressions. The resulting DataFrame is hash partitioned. Same as "DISTRIBUTE BY" in HiveQL.

* repartition(partitionExprs: Column*)
* repartition(numPartitions: Int, partitionExprs: Column*)
* repartition(numPartitions: Int)

### **rollup**

Create a multi-dimensional rollup for the current DataFrame using the specified columns, so we can run aggregation on them.

```scala
// Compute the average for all numeric columns rolluped by department and group.
df.rollup("department", "group").avg()

// Compute the max age and average salary, rolluped by department and gender.
df.rollup($"department", $"gender").agg(Map(
  "salary" -> "avg",
  "age" -> "max"
))
```

See [Mastering Spark SQL Gitbook](https://jaceklaskowski.gitbooks.io/mastering-spark-sql/spark-sql-multi-dimensional-aggregation.html#rollup) for examples.

### **select**

Selects a set of columns.

* select(col: String, cols: String*)

`df.select("age", "salary")`

* select(cols: Column*)

`df.select($"age", $"salary")`

### **sort**

Returns a new DataFrame sorted by the given expressions. For example:

`df.sort($"col1", $"col2".desc)`

### **sortWithinPartitions**

Returns a new DataFrame with each partition sorted by the given expressions.

### **where**

Filters rows using the given SQL expression.

```scala
peopleDf.where("age > 15")
peopleDf.where($"age" > 15)
peopleDf.filter($"age" > 15)
```

### **withColumn**

* withColumn(colName: String, col: Column)

Returns a new DataFrame by adding a column or replacing the existing column that has the same name.

### **withColumnRenamed**

* withColumnRenamed(existingName: String, newName: String)

Returns a new DataFrame with a column renamed. This is a no-op if schema doesn't contain existingName.

## Output Operations

### write

Interface for saving the content of the DataFrame out into external storage.

## RDD operations

### **coalesce**

* coalesce(numPartitions: Int)

Returns a new DataFrame that has exactly numPartitions partitions. Similar to coalesce defined on an RDD, this operation results in a narrow dependency, e.g. if you go from 1000 partitions to 100 partitions, there will not be a shuffle, instead each of the 100 new partitions will claim 10 of the current partitions.

### **flatMap**

* flatMap[R](f: (Row) ⇒ TraversableOnce[R])(implicit arg0: ClassTag[R])

Returns a new RDD by first applying a function to all rows of this DataFrame, and then flattening the results.

### **foreach**

* foreach(f: (Row) ⇒ Unit)

Applies a function f to all rows.

### **foreachPartition**

* foreachPartition(f: (Iterator[Row])

Applies a function f to each partition of this DataFrame.

### **rdd**

Represents the content of the DataFrame as an RDD of Rows.

### **map**

* map[R](f: (Row) ⇒ R)(implicit arg0: ClassTag[R]): RDD[R]

Returns a new RDD by applying a function to all rows of this DataFrame.

### **mapPartitions**

* mapPartitions[R](f: (Iterator[Row]) ⇒ Iterator[R])(implicit arg0: ClassTag[R]): RDD[R]

Returns a new RDD by applying a function to each partition of this DataFrame

### **toJSON**

Returns the content of the DataFrame as a RDD of JSON strings.