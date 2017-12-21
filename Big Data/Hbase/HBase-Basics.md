# HBase Basics

## Limitations with HDFS

* Updates not allowed
* not optimized for Random access

## Features of HBase

* Distributed
* Versioned
* Column-oriented
* Dynamic Columns
* Does not occupy space for Sparse data
* Fixed queries (Predicate is well defined)
* Quick lookup (optimized)
* Indexed file format (Hfile)
* Provides random, real-time read/write access to HDFS

## Goal of HBase

> to host very large tables

* billions of rows multiplied by millions of columns
* on commodity hardware clusters

|   |RDBMS|HBase|
|---|---|---|
|Data layout|Row or column oriented|Column Familiy oriented|
|Transactions|Yes|Single row only|
|Query Language|SQL|GET/PUT/SCAN|
|Security|Authentication/Authorization|Access control

## Terms

* One table may have multiple Regions
  * Region - Horizontal Division of a table
* One Region may have multiple Stores
  * Stores - for a column family stored in Hfile format
* Namespace - (similar to database) (default two - System & User)

## Factors in designing schema

* Choosing your column family (ideally should be limited to maximum 3)
* Deciding which column goes to which column family
* Choosing your row key
* Deciding on Composite key

## Roles/Responsibilities of HMaster

* Performing DDL Operations
* Coordinating Region Servers failure
* Load balancing of Regions

## Roles/Responsibilities of Region Servers

* Hosting Region stores
* Caching of Block
* hosts WAL (Write ahead Log)
* Replay WAL on Failure
* Splitting of Regions

## HBase Block vs HDFS Block

## CoProcessors

[Guide to Coprocessor](https://blogs.apache.org/hbase/entry/coprocessor_introduction)

### Characteristics

* Arbitrary code can run at each table in table server
* High-level call interface for clients
  * Calls are addressed to rows or ranges of rows and the coprocessor client library resolves them to actual locations;
  * Calls across multiple rows are automatically split into multiple parallelized RPC
* Provides a very flexible model for building distributed services
* Automatic scaling, load balancing, request routing for applications

### Types

* Endpoint (similar to Procedure)
* Observers (similar to Trigger)

## Research

* [Google Colossus - Next gen GFS](http://highscalability.com/blog/2010/9/11/googles-colossus-makes-search-real-time-by-dumping-mapreduce.htm)
* [Link](https://hortonworks.com/blog/apache-hbase-region-splitting-and-merging/)
* Tall Table vs Wide Table
* [Row Key Design](http://hbase.apache.org/0.94/book/rowkey.design.html)