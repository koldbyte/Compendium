

# SQL Tuning
## `spark.sql.codegen`
> Default: false
When true, Spark SQL will compile each query to Java bytecode on the fly. This can improve performance for large queries, but codegen can slow down very short queries

## `spark.sql.inMemoryColumnarStorage.compressed`
> Default: false
Compress the in-memory columnar storage automatically.

## `spark.sql.inMemoryColumnarStorage.batchSize`
> Default: 1000
The batch size for columnar caching. Larger values may cause out-of-memory problems

## `spark.sql.parquet.compression.codec`
> Default: snappy
Which compression codec to use. Possible options include uncompressed, snappy, gzip, and lzo.