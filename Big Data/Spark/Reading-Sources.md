# Parquet
```python
val rows = hiveCtx.parquetFile(parquetFile)
val names = rows.map(lambda row: row.name)

//Register as temp table
rows.registerTempTable("rows")
```


# JSON
```scala
val input = hiveCtx.jsonFile(inputFile)
input.printSchema()
```

Note: Access nested elements using '.' (dot) for each level of nesting.
      Access array elements using '[]' (Square brackets).

# RDDs to Dataframe
```python
happyPeopleRDD = sc.parallelize([Row(name="holden", favouriteBeverage="coffee")])
happyPeopleSchemaRDD = hiveCtx.inferSchema(happyPeopleRDD)
happyPeopleSchemaRDD.registerTempTable("happy_people")
```

```scala
case class HappyPerson(handle: String, favouriteBeverage: String)
...
// Create a person and turn it into a Schema RDD
val happyPeopleRDD = sc.parallelize(List(HappyPerson("holden", "coffee")))
// Note: there is an implicit conversion
// that is equivalent to sqlCtx.createSchemaRDD(happyPeopleRDD)
happyPeopleRDD.registerTempTable("happy_people")
```