# Predicate Push Down
Predicate push-down allows Spark SQL to move some parts of our query “down” to
the engine we are querying. If we wanted to read only certain records in Spark, the
standard way to handle this would be to read in the entire dataset and then execute a
filter on it. However, in Spark SQL, if the underlying data store supports retrieving
only subsets of the key range, or another restriction, Spark SQL is able to push the
restrictions in our query down to the data store, resulting in potentially much less
data being read.

#
https://stackoverflow.com/questions/37301226/difference-between-dataset-api-and-dataframe-api

https://spark.apache.org/docs/1.6.0/api/scala/index.html#org.apache.spark.sql.DataFrame

