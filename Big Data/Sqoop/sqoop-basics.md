# Sqoop

## Introduction

Sqoop is a tool designed to transfer data between Hadoop and relational databases or mainframes. You can use Sqoop to import data from a relational database management system (RDBMS) such as MySQL or Oracle or a mainframe into the Hadoop Distributed File System (HDFS), transform the data in Hadoop MapReduce, and then export the data back into an RDBMS.

Sqoop automates most of this process, relying on the database to describe the schema for the data to be imported. Sqoop uses MapReduce to import and export the data, which provides parallel operation as well as fault tolerance.

[Link to User Guide](https://sqoop.apache.org/docs/1.4.6/SqoopUserGuide.html)

## Sqoop Tools

Sqoop is a collection of related tools. To use Sqoop, you specify the tool you want to use and the arguments that control the tool.

### General Syntax

* `sqoop tool-name [tool-arguments]`

### Help

* `sqoop help`
* `sqoop help COMMAND`

### MySQL Connection

```bash
sqoop list-tables \
    --connect jdbc:mysql://dbhost:3306/dbname \
    --username dbuser \
    --password passwd
```

### Import data from MySQL DB

#### Import All Tables

```bash
sqoop import-all-tables \
    --connect jdbc:mysql://dbhost/dbname \
    --username dbuser --password passwd
```

Stored by default as comma-­delimited files

#### Import a Specific Table

```bash
sqoop import \
    --table tablename \
    --target-dir /foo/bar \
    --connect jdbc:mysql://dbhost/dbname \
    --username dbuser --password passwd
```

target-dir specifies a different base directory. Default is user home.

#### Useful Parameters

##### Incremental lastmodified

Import only new and modified record based on a timestamp in a specified column.

```bash
--incremental lastmodified \
--check-column last_modification_column_name \
--last-value '2017-12-11 11:11:00'
```

##### Incremental append

Import only new records based on the value of the last record in a specified column

```bash
--incremental append \
--check-column id \
--last-value 1234
```

##### Import only specified columns from table

```bash
--columns "id,number,prefix"
```

##### Where Clause

```bash
--where "prefix='+91'"
```

### Export Data

```bash
sqoop export \
    --table tablename \
    --export-dir /hdfs/data/location \
    --connect jdbc:mysql://dbhost/dbname \
    --username dbuser --password passwd
```

#### Useful Params

##### Update mode

MySQL will try to insert new row and if the insertion fails with duplicate unique key error it will update appropriate row instead.

```bash
--update-mode allowinsert
```

### Change the delimiter and file format of data during import

[Guide to file formats](https://sqoop.apache.org/docs/1.4.6/SqoopUserGuide.html#_file_formats)

#### Delimiter

```bash
--fields-terminated-by "\t"
--enclosed-by "\""
--escaped-by "\\"
--lines-terminated-by "\n"
```

#### File Formats

##### Imports data to Avro data files

```bash
--as-avrodatafile
```

##### Imports data to Parquet files

```bash
--as-parquetfile
```

##### Imports data to SequenceFiles

```bash
--as-sequencefile
```

##### Imports data as plain text (default)

```bash
--as-textfile
```

### Sqoop Jobs

#### Create a sqoop job

```bash
sqoop job \
    --create import_job \
    -- import \
    --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
    --username retail_dba \
    --password cloudera \
    --table departments \
    --target-dir /user/cloudera/departments
```

#### Sqoop Job commands

* will list all the existing sqoop jobs

```bash
sqoop job --list
```

* will show the job details and definition

```bash
sqoop job --show
```

* To run the job

```bash
sqoop job --exec
```

### Sqoop Merge

```bash
 sqoop merge \
 --merge-key department_id \
 --new-data /user/cloudera/sqoop_merge/departments_delta \
 --onto /user/cloudera/sqoop_merge/departments \
 --target-dir /user/cloudera/sqoop_merge/staging \
 --class-name departments.java \
 --jar-file /tmp/sqoop-cloudera/compile/e11d28e872acd71c103d33fbf81ec5c7/departments.jar
```

* now remove the old dir ‘/user/cloudera/sqoop_merge/departments’
  * `hdfs dfs -rm -R /user/cloudera/sqoop_merge/departments`
* rename dir ‘/user/cloudera/sqoop_merge/staging’ to ‘/user/cloudera/sqoop_merge/departments’
  * `hdfs dfs -mv /user/cloudera/sqoop_merge/staging /user/cloudera/sqoop_merge/departments`