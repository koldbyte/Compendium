# DataFrames API

A DataFrame is equivalent to a relational table in Spark SQL

## Actions

### collect()

Returns an array that contains all of Rows in this DataFrame.

Running collect requires moving all the data into the application's driver process, and doing so on a very large dataset can crash the driver process with OutOfMemoryError.

### count()

Returns the number of rows in the DataFrame.

### describe(cols: String*)

Computes statistics for numeric columns, including count, mean, stddev, min, and max.

### first()

Returns the first row. Alias for head().

### head(n : Int)

Returns the first row

### show(numrows = 20, truncate = true)

Displays the DataFrame in a tabular form.

### take(n : Int)

Returns the first n rows in the DataFrame

## Basic DataFrame function

### as[U](implicit arg0: Encoder): Dataset[U]

Converts this DataFrame to a strongly-typed Dataset containing objects of the specified type, U.

### cache()

Persist this DataFrame with the default storage level (MEMORY_AND_DISK).

### columns()

Returns all column names as an array

### explain(extended: Boolean)

Prints the plans (logical and physical) to the console for debugging purposes.

### persist(newLevel: StorageLevel = MEMORY_AND_DISk)

Persist this DataFrame with the given storage level.

### printSchema()

Prints the schema to the console in a nice tree format

### registerTempTable(tableName: String)

Registers this DataFrame as a temporary table using the given name.

### schema

Returns the schema of this DataFrame.

### toDF(colNames: String*)

Returns a new DataFrame with columns renamed

### unpersist(blocking: Boolean)

Mark the DataFrame as non-persistent, and remove all blocks for it from memory and disk.

## Language Integrated Queries

### agg

* agg(expr: Column, exprs: Column*)

```scala
// df.agg(...) is a shorthand for df.groupBy().agg(...)
df.agg(max($"age"), avg($"salary"))
df.groupBy().agg(max($"age"), avg($"salary"))
```

### alias

* alias(alias: String)

Returns a new DataFrame with an alias set. Same as `as`.

### apply, col

* apply(colName: String)
* col(colName: String)

Selects column based on the column name and return it as a Column.

### cube

* cube(col1: String, cols: String*)

Create a multi-dimensional cube for the current DataFrame using the specified columns, so we can run aggregation on them. See GroupedData for all the available aggregate functions.

```scala
// Compute the average for all numeric columns cubed by department and group.
df.cube("department", "group").avg()
```

### distinct

* distinct()

Returns a new DataFrame that contains only the unique rows from this DataFrame. This is an alias for    `dropDuplicates`.

### drop

* drop(colName: String)

Returns a new DataFrame with a column dropped. This is a no-op if the DataFrame doesn't have a column with an equivalent expression.

### except

* except(other: DataFrame)

Returns a new DataFrame containing rows in this frame but not in another frame. This is equivalent to EXCEPT in SQL.

### explode

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

### filter

### groupBy

### intersect

### join

### limit

### na

### orderBy

### repartition

### rollup

### select

### sort

### sortWithinPartitions

### where

### withColumn

### withColumnRenamed

## Output Operations

### write

## RDD operations

### coalesce

* coalesce(numPartitions: Int)

Returns a new DataFrame that has exactly numPartitions partitions. Similar to coalesce defined on an RDD, this operation results in a narrow dependency, e.g. if you go from 1000 partitions to 100 partitions, there will not be a shuffle, instead each of the 100 new partitions will claim 10 of the current partitions.

### flatMap

* flatMap[R](f: (Row) ⇒ TraversableOnce[R])(implicit arg0: ClassTag[R])

Returns a new RDD by first applying a function to all rows of this DataFrame, and then flattening the results.

### foreach

* foreach(f: (Row) ⇒ Unit)

Applies a function f to all rows.

### foreachPartition

* foreachPartition(f: (Iterator[Row])

Applies a function f to each partition of this DataFrame.

### rdd

Represents the content of the DataFrame as an RDD of Rows.

### map

Returns a new RDD by applying a function to all rows of this DataFrame.

### mapPartitions

Returns a new RDD by applying a function to each partition of this DataFrame

### toJSON

Returns the content of the DataFrame as a RDD of JSON strings.