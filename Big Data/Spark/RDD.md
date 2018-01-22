# RDD API

Resilient Distributed Dataset (RDD)
Represents an immutable, partitioned collection of elements that can be operated on in parallel.

Internally, each RDD is characterized by five main properties:

* A list of partitions
* A function for computing each split
* A list of dependencies on other RDDs
* Optionally, a Partitioner for key-value RDDs (e.g. to say that the RDD is hash-partitioned)
* Optionally, a list of preferred locations to compute each split on (e.g. block locations for an HDFS file)

## Types of RDD

* Simple RDD
* DoubleRDD
* Pair RDD
* CoGroupedRDD
* OrderedRDDFunctions
* ShuffledRDD
* UnionRDD
* SequenceFileRDD
* JdbcRDD
* HadoopRDD
* NewHadoopRDD

## RDD Functions

### Common

* `++(other: RDD[T])` , `union(other: RDD[T])`

Return the union of this RDD and another one. Any identical elements will appear multiple times (use .distinct() to eliminate them).

* `aggregate[U](zeroValue: U)(seqOp: (U, T) ⇒ U, combOp: (U, U) ⇒ U)(implicit arg0: ClassTag[U])`

Aggregate the elements of each partition, and then the results for all the partitions, using given combine functions and a neutral "zero value". Both of these functions are allowed to modify and return their first argument instead of creating a new U to avoid memory allocation.

* `cartesian[U](other: RDD[U])(implicit arg0: ClassTag[U])`

Return the Cartesian product of this RDD and another one, that is, the RDD of all pairs of elements (a, b) where a is in this and b is in other.

* `coalesce(numPartitions: Int, shuffle: Boolean = false)(implicit ord: Ordering[T] = null)`

Return a new RDD that is reduced into numPartitions partitions.

* `count`

Return the number of elements in the RDD.

* `countByValue(scala.math.Ordering<T> ord)`

Return the count of each unique value in this RDD as a local map of (value, count) pairs.

* `distinct`

Return a new RDD containing the distinct elements in this RDD.

* `filter`

Return a new RDD containing only the elements that satisfy a predicate.

* `first`

Return the first element in this RDD.

* `flatMap`

Return a new RDD by first applying a function to all elements of this RDD, and then flattening the results.

* `fold(T zeroValue, scala.Function2<T,T,T> op)`

Aggregate the elements of each partition, and then the results for all the partitions, using a given associative and commutative function and a neutral "zero value".

* `foreach`

Applies a function f to all elements of this RDD.

* `getNumPartitions`

Returns the number of partitions of this RDD.

* `groupBy`

Return an RDD of grouped items.

* `intesection(RDD<T> other)`

Return the intersection of this RDD and another one.

* `keyBy(scala.Function1<T,K> f)`

Creates tuples of the elements in this RDD by applying f. Returns `<K> RDD<scala.Tuple2<K,T>>`

* `map(scala.Function1<T,U> f)`

Return a new RDD by applying a function to all elements of this RDD.

* `mapPartitions(scala.Function1<scala.collection.Iterator<T>,scala.collection.Iterator<U>> f, boolean preservesPartitioning)`

Return a new RDD by applying a function to each partition of this RDD.

* `max(scala.math.Ordering<T> ord)`

Returns the max of this RDD as defined by the implicit Ordering[T].

* `min(scala.math.Ordering<T> ord)`

Returns the min of this RDD as defined by the implicit Ordering[T].

* `persist`

Persist this RDD with the default storage level (`MEMORY_ONLY`).

* `pipe(java.lang.String command)`

Return an RDD created by piping elements to a forked external process.

* reduce

Reduces the elements of this RDD using the specified commutative and associative binary operator.

* repartition

Return a new RDD that has exactly numPartitions partitions.
repartition is same as calling coalesce with shuffle = true

* saveAsTextFile

Save this RDD as a compressed text file, using string representations of elements.

* sortBy

Return this RDD sorted by the given key function.

* subtract

Return an RDD with the elements from this that are not in other.

* take

Take the first num elements of the RDD.

* toDebugString

A description of this RDD and its recursive dependencies for debugging.

* treeAggregate

Aggregates the elements of this RDD in a multi-level tree pattern.

* treeReduce

Reduces the elements of this RDD in a multi-level tree pattern.

* zip

Zips this RDD with another one, returning key-value pairs with the first element in each RDD, second element in each RDD, etc.

* zipWithIndex

Zips this RDD with its element indices.

* zipWithUniqueId

Zips this RDD with generated unique Long ids.

* `collect`

Return an array that contains all of the elements in this RDD.

* `cache()`

Persist this RDD with the default storage level (MEMORY_ONLY).

* `checkpoint()`