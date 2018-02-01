# Sources of Data in Spark

## Parquet (Default in Spark SQL)

Fully qualified name : `org.apache.spark.sql.parquet`

```scala
val rows = sqlContext.parquetFile(parquetFile)
```

```scala
val df = sqlContext.read.load("examples/src/main/resources/users.parquet")
```

```scala
val df = sqlContext.sql("SELECT * FROM parquet.`examples/src/main/resources/users.parquet`")
```

```scala
val parquetFile = sqlContext.read.parquet("people.parquet")
```

## JSON

```scala
val input = sqlContext.jsonFile(inputFile)
input.printSchema()
```

```scala
val df = sqlContext.read.json(path)
val df2 = sqlContext.read.json(jsonRDD)
```

Note: Each line must contain a separate, self-contained valid JSON object. As a consequence, a regular multi-line JSON file will most often fail.

Note: Access nested elements using '.' (dot) for each level of nesting.
      Access array elements using '[]' (Square brackets).

## Avro

Run `spark-shell --packages com.databricks:spark-avro_2.11:4.0.0`

Note: Cloudera Quickstart Sandbox includes the avro package.

```scala
import com.databricks.spark.avro._
val df = sqlContext.read.avro(hdfsLocation)
```

### Using a custom Avro Schema

```scala
import org.apache.avro.Schema
val schema = new Schema.Parser().parse(new File("user.avsc"))

val df = sqlContext.read
  .format("com.databricks.spark.avro")
  .option("avroSchema", schema.toString)
  .load("src/test/resources/episodes.avro")

df.show()
```

## RDDs to Dataframe

```python
# Python
happyPeopleRDD = sc.parallelize([Row(name="holden", favouriteBeverage="coffee")])
happyPeopleSchemaRDD = hiveCtx.inferSchema(happyPeopleRDD)
happyPeopleSchemaRDD.registerTempTable("happy_people")
```

```scala
//Scala
// this is used to implicitly convert an RDD to a DataFrame.
import sqlContext.implicits._
case class HappyPerson(handle: String, favouriteBeverage: String)
...
// Create a person and turn it into a Schema RDD
val happyPeopleRDD = sc.parallelize(List(HappyPerson("holden", "coffee")))
// Note: there is an implicit conversion
// that is equivalent to sqlCtx.createSchemaRDD(happyPeopleRDD)
happyPeopleRDD.registerTempTable("happy_people")
```

```scala
val people = sc.textFile("examples/src/main/resources/people.txt")

// Import Row.
import org.apache.spark.sql.Row;

// Import Spark SQL data types
import org.apache.spark.sql.types.{StructType,StructField,StringType};

// The schema is encoded in a string
val schemaString = "name age"

// Generate the schema based on the string of schema
val schema =
  StructType(
    schemaString.split(" ").map(fieldName => StructField(fieldName, StringType, true)))

// Convert records of the RDD (people) to Rows.
//Method 1: Manually specifying each columns
val rowRDD = people.map(_.split(",")).map(p => Row(p(0), p(1).trim))

//Method 2: Using a helper method
val rowRDD = people.map(_.split(",")).map(p => Row.fromSeq(p))

// Apply the schema to the RDD.
val peopleDataFrame = sqlContext.createDataFrame(rowRDD, schema)

```

## Hive Tables

```scala
// sc is an existing SparkContext.
val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)

sqlContext.sql("CREATE TABLE IF NOT EXISTS src (key INT, value STRING)")
sqlContext.sql("LOAD DATA LOCAL INPATH 'examples/src/main/resources/kv1.txt' INTO TABLE src")

// Queries are expressed in HiveQL
sqlContext.sql("FROM src SELECT key, value").collect().foreach(println)
```

## JDBC

```scala
val jdbcDF = sqlContext.read.format("jdbc").options(
  Map("url" -> "jdbc:postgresql:dbserver",
  "dbtable" -> "schema.tablename")).load()
```

Other options include - `driver`, `fetchSize` etc.

Note: To get started you will need to include the JDBC driver for you particular database on the spark classpath. Example:
`SPARK_CLASSPATH=postgresql-9.3-1102-jdbc41.jar bin/spark-shell`

## SequenceFiles

```scala
import org.apache.hadoop.io._

val file=sc.sequenceFile[BytesWritable,String](hdfsLocation)
```

Note: For SequenceFiles, use SparkContext’s sequenceFile[K, V] method where K and V are the types of key and values in the file. These should be subclasses of Hadoop’s Writable interface, like IntWritable and Text. In addition, Spark allows you to specify native types for a few common Writables; for example, sequenceFile[Int, String] will automatically read IntWritables and Texts.

## Text files through Hadoop formats

```scala
import org.apache.hadoop.conf.Configuration
import org.apache.hadoop.mapreduce.Job
import org.apache.hadoop.io.{LongWritable, Text}
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat

val conf = new Configuration(sc.hadoopConfiguration)
conf.set("textinputformat.record.delimiter", "\n")
/*
public <K,V,F extends org.apache.hadoop.mapreduce.InputFormat<K,V>> RDD<scala.Tuple2<K,V>> newAPIHadoopFile(    java.lang.String path,
  java.lang.Class<F> fClass, //Class of the InputFormat
  java.lang.Class<K> kClass, //Class of the keys
  java.lang.Class<V> vClass, //Class of the values
  org.apache.hadoop.conf.Configuration conf
)
*/
val input = sc.newAPIHadoopFile("file_path", classOf[TextInputFormat], classOf[LongWritable], classOf[Text], conf)
val lines = input.map { case (_, text) => text.toString}
println(lines.collect)
```

## Range

* range(start: Long, end: Long, step: Long, numPartitions: Int)

* range(start: Long, end: Long)

## Collections

* createDataFrame(data: List[_], beanClass: Class[_])
* createDataFrame(rows: List[Row], schema: StructType)

## RDD

* createDataFrame(rdd: JavaRDD[_], beanClass: Class[_])
* createDataFrame(rdd: RDD[_], beanClass: Class[_])
* createDataFrame(rowRDD: JavaRDD[Row], schema: StructType)
* createDataFrame(rowRDD: RDD[Row], schema: StructType)
* createDataFrame[A <: Product](rdd: RDD[A])