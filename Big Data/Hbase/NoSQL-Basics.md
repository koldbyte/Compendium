# NoSQL Basics

## Problems with RDBMS

* Rigid Schema
* No Horizontal Scalability
* No support for specialized processing like Graph Processing
* Limit on amount of Data it can process
* Not capable for Handling "internet" scale (without tuning upto a scale)
* Limit on scaling of columns (millions of column)
* Occupy space for Sparse data (ie. nulls)
* Impedence Mismatch Problem

## Advantages of NoSQL

* Low cost
* Runs on commodity hardware
* Mostly opensource
* Flexible Schema
* Horizontally Scalable

## Limitations of NoSQL

* Transactions support is limited
* Relatively less mature than RDBMS
* Limited support for SQL
* ACID compliance is missing from most of the databases
* Mostly have Specialized purpose eg. Graph processing
* Sparse data is gracefully handled (for eg. in hbase)

## Types of NoSQL DBs

* Document Store
  * Very useful for Dynamic schemas
  * Geospatial search (in MongoDB)
  * Ex - MongoDB
* Key/Value Store
  * Mostly used as Cache
  * Ex - Redis
* Graph Store
  * For graph based processing
  * Ex - Neo4j
* Search (sometimes included as NoSQL DB)
  * Ex - Solr, ElasticSearch
* Column Oriented Store
  * Provides column family as value
  * Ex - Cassandra, Hbase

## Research

* Impedence mismatch problem [Link](https://en.wikipedia.org/wiki/Object-relational_impedance_mismatch)
* Polyglot Persistence [Martin Fowler](https://www.martinfowler.com/bliki/PolyglotPersistence.html)
* CAP Theorem in Plain English [Link](http://ksat.me/a-plain-english-introduction-to-cap-theorem/)
* PACELC [Link](https://en.wikipedia.org/wiki/PACELC_theorem)