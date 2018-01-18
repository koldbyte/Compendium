# Writing Sinks

## Parquet

```scala
val pandaFriends = hiveCtx.sql("SELECT name FROM people WHERE favouriteAnimal = \"panda\"")
pandaFriends.saveAsParquetFile("hdfs://...")
```

## Parquet in Compressed Format

```scala
sqlContext.setConf("spark.sql.parquet.compression.codec", "snappy") // Acceptable values include: uncompressed, snappy, gzip, lzo
df.write.parquet(hdfsLocation)
```

## Avro

```scala
import com.databricks.spark.avro._
df.write.avro(hdfsLocation)
```

## Avro in Compressed format

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

```scala
df.write.json(hdfsLocation)
```

```scala
df.toJSON.saveAsTextFile(hdfsLocation)
```

## JSON File Compressed

```scala
df.toJSON.saveAsTextFile(hdfsLocation, classOf[org.apache.hadoop.io.compress.GzipCodec])
```