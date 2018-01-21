# HDFS Introduction

HDFS - Hadoop Distributed File System

- Distributed File System
- Designed for commodity hardware
- Highly Fault-tolerant
- Provides high throughput
- Optimized for large data sets

## Assumptions/Goals

### Hardware Failure

It is assumed that some components will fail in a given time.  Therefore, detection of faults and quick, automatic recovery from them is a core architectural goal of HDFS.

### Streaming Data access

HDFS is designed more for batch processing rather than interactive use by users.  
The emphasis is on high-throughput of data access rather than low latency of data access.

### Large data sets

HDFS is tuned to support large files. It should provide high aggregate data bandwidth and scale to hundreds of nodes in a single cluster.

### Simple Coherency model

HDFS applications need a write-once-read-many access model for files.  
A file once created, written, and closed need not be changed. This assumption allows high throughput data access.

### Moving Computation is cheaper than moving data

Since, the usual data set is huge, It is much more efficient to perform computations near the data it operates on. HDFS provides interfaces for applications to move themselves closer to where the data is located.

### Portability across heterogenous hardware and software platforms

This facilitates widespread adoption of HDFS as a platform of choice for a large set of applications.

## Architecture

- Master/Slave Architecture
- Read AOSA link.

## Reading List

1. [GFS Paper](https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf)
1. [HDFS Architecture Guide](http://hadoop.apache.org/docs/r2.6.0/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html)
1. [HDFS User Guide](http://hadoop.apache.org/docs/r2.6.0/hadoop-project-dist/hadoop-hdfs/HdfsUserGuide.html)
1. [AOSA HDFS](http://www.aosabook.org/en/hdfs.html)