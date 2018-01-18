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

Simple RDD
DoubleRDD
Pair RDD
CoGroupedRDD
OrderedRDDFunctions
ShuffledRDD
UnionRDD
SequenceFileRDD
JdbcRDD
HadoopRDD
NewHadoopRDD

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

* countByValue

* distinct
* filter
* first
* flatMap
* fold
* foreach
* getNumPartitions
* groupBy
* intesection
* keyBy
* map
* mapPartition
* max
* min
* persist
* pipe
* reduce
* repartition

Return a new RDD that has exactly numPartitions partitions.
repartition is same as calling coalesce with shuffle = true

* saveAsTextFile
* sortBy
* subtract
* take
* toDebugString
* treeAggregate
* treeReduce
* zip
* zipWithIndex
* zipWithUniqueId
* 



* `collect`

Return an array that contains all of the elements in this RDD.

* `cache()`

Persist this RDD with the default storage level (MEMORY_ONLY).

* `checkpoint()`