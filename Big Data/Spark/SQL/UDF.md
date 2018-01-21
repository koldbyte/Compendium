# UDFs

## Creating a UDF for Spark SQL

```python
# Make a UDF to tell us how long some text is
hiveCtx.registerFunction("strLenPython", lambda x: len(x), IntegerType())
lengthSchemaRDD = hiveCtx.sql("SELECT strLenPython('text') FROM tweets LIMIT 10")
```

```scala
registerFunction("strLenScala", (_: String).length)
val tweetLength = hiveCtx.sql("SELECT strLenScala('tweet') FROM tweets LIMIT 10")
```

## Using Hive UDFs in Spark SQL

Note: Make sure jars for the UDF is included with the application. For JDBC servers, use `--jars` command line flag.

```python
# Simply use a HiveContext and register a function
hiveCtx.sql("CREATE TEMPORARY FUNCTION name AS class.function")
```