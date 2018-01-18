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
