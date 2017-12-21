# Parquet
`
val pandaFriends = hiveCtx.sql("SELECT name FROM people WHERE favouriteAnimal = \"panda\"")
pandaFriends.saveAsParquetFile("hdfs://...")
`