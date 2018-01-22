# Writing Sinks

## Parquet

### Parquet without compression

```scala
val pandaFriends = sqlContext.sql("SELECT name FROM people WHERE favouriteAnimal = \"panda\"")
pandaFriends.saveAsParquetFile("hdfs://...")
```

### Parquet in Compressed Format

Method 1:

```scala
sqlContext.setConf("spark.sql.parquet.compression.codec", "snappy") // Acceptable values include: uncompressed, snappy, gzip, lzo
df.write.parquet(hdfsLocation)
```

Method 2: **(Not supported in 1.6)**

```scala
//This can be one of the known case-insensitive shorten names(none, snappy, gzip, and lzo). This will override spark.sql.parquet.compression.codec.
df.write.option("compression", "snappy").parquet(hdfsLocation)
```

## Avro

### Avro without compression

```scala
import com.databricks.spark.avro._
df.write.avro(hdfsLocation)
```

### Avro in Compressed format

```scala
import com.databricks.spark.avro._
sqlContext.setConf("spark.sql.avro.compression.codec","snappy") //supported codec values are uncompressed, snappy, and deflate
//Specify the level to use with deflate compression in spark.sql.avro.deflate.level.
df.write.avro(hdfsLocation)
```

```scala
import com.databricks.spark.avro._

val sqlContext = new SQLContext(sc)

// configuration to use deflate compression
sqlContext.setConf("spark.sql.avro.compression.codec", "deflate")
sqlContext.setConf("spark.sql.avro.deflate.level", "5")

val df = sqlContext.read.avro("input dir")

// writes out compressed Avro records
df.write.avro("output dir")
```

## Text File

### Text File From dataframe (no compression)

Saves the content of the DataFrame in a text file at the specified path. The DataFrame must have only one column that is of string type. Each row becomes a new line in the output file. For example:

```scala
df.write.text(hdfsLocation)
```

### Text File from dataframe (with compression) **(Not supported in 1.6)**

```scala
//Default is "null"
df.write.option("compression", "snappy") //This can be one of the known case-insensitive shorten names (none, bzip2, gzip, lz4, snappy and deflate).
.text(hdfsLocation)
```

### Text File From RDD (no compression)

```scala
rdd.saveAsTextFile(hdfsLocation)
```

### Text File from RDD (with compression)

```scala
rdd.saveAsTextFile(hdfsLocation, classOf[org.apache.hadoop.io.compress.GzipCodec])
```

Generally Available codecs are:

* `org.apache.hadoop.io.compress.GzipCodec`
* `org.apache.hadoop.io.compress.BZip2Codec`
* `com.hadoop.compression.lzo.LzopCodec`
* `org.apache.hadoop.io.compress.SnappyCodec`
* `org.apache.hadoop.io.compress.DeflateCodec`
* `org.apache.hadoop.io.compress.Lz4Codec`

## Sequence File

```scala
rdd.saveAsObjectFile(hdfsLocation)
```

## JSON File

### JSON without compression

```scala
df.write.json(hdfsLocation)
```

```scala
df.toJSON.saveAsTextFile(hdfsLocation)
```

### JSON File in Compressed format

Method 1:

```scala
df.toJSON.saveAsTextFile(hdfsLocation, classOf[org.apache.hadoop.io.compress.GzipCodec])
```

Method 2: **(Not supported in 1.6)**

```scala
// This can be one of the known case-insensitive shorten names (none, bzip2, gzip, lz4, snappy and deflate).
df.write.option("compression", "snappy") //default null
    .json(hdfsLocation)
```