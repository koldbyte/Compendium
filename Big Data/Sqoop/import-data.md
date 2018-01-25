# Sqoop Import

## Import all tables using sqoop-import

### Create import directory

`hadoop fs -mkdir /user/cloudera/sqoop_import`

### Import db

```bash
sqoop import-all-tables \
-m 4 \
--connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
--username=retail_dba \
--password=cloudera \
--warehouse-dir=/user/cloudera/sqoop_import
```

### Validate the import

`hadoop fs -ls -R /user/cloudera/sqoop_import`

## Import data using avro format – import-all-tables

### Create import directory

`hadoop fs -rm -R /user/cloudera/sqoop_import`

### Import db

```bash
sqoop import-all-tables \
-m 12 \
--connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
--username=retail_dba \
--password=cloudera \
--as-avrodatafile \
--warehouse-dir=/user/cloudera/sqoop_import
```

### Validate the import data and *.avsc schema files

`hadoop fs -ls -R /user/cloudera/sqoop_import`

## Import into hive default database – import-all-tables

### Make sure hive is running

### Import db

```bash
sqoop import-all-tables \
--num-mappers 1 \
--connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
--username=retail_dba \
--password=cloudera \
--hive-import \
--hive-overwrite \
--create-hive-table \
--compress \
--compression-codec org.apache.hadoop.io.compress.SnappyCodec \
--outdir java_files
```

## Import into hive existing database – import-all-tables

### Hive database

`hive -e "CREATE DATABASE IF NOT EXISTS retail_stage"`

### Import

```bash
sqoop import-all-tables \
--num-mappers 1 \
--connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
--username=retail_dba \
--password=cloudera \
--hive-import \
--hive-overwrite \
--create-hive-table \
--outdir java_files \
--hive-database retail_stage
```

### Validate

`hive -e "USE retail_stage; SHOW TABLES; SELECT * FROM departments;"`

## Import single table

### Directory should not exist

`hadoop fs -rm -R /user/cloudera/departments`

### Import db

```bash
sqoop import \
  --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username=retail_dba \
  --password=cloudera \
  --table departments \
  --as-textfile \
  --target-dir=/user/cloudera/sqoop_import/departments
```

### Notes

* `--as-textfile` (default): to store data in HDFS using text file format. Other valid formats are
* `--as-avrodatafile`: Imports data to Avro Data Files
* `--as-sequencefile`: Imports data to SequenceFiles
* `--as-textfile`: Imports data as plain text (default)
* `--as-parquetfile`: Imports data to Parquet Files (from 1.4.6)

* `--split-by` can be used to use multiple threads in case there is no primary key or unique key in the table from source database. If --split-by is not used we should pass --num-mappers 1
* `--query` can be used to pass custom query to import the data

* `--fields-terminated-by '|' \`
* `--lines-terminated-by '\n' \`

## Import into existing hive table

### Create table in hive

```sql
CREATE TABLE departments (
department_id INT,
department_name STRING
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '|'
STORED AS TEXTFILE;
SHOW TABLES;
```

### Import

```bash
sqoop import \
  --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username=retail_dba \
  --password=cloudera \
  --table departments \
  --fields-terminated-by '|' \
  --lines-terminated-by '\n' \
  --hive-home /user/hive/warehouse \
  --hive-import \
  --hive-overwrite \
  --hive-table departments \
  --outdir java_files
```

### Notes

Specify db either by
  > --hive-table dbname.departments
  > --hive-database dbname

### Sqoop Merge

--Merge process begins
`hadoop fs -mkdir /user/cloudera/sqoop_merge`

--Initial load

```bash
sqoop import \
  --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username=retail_dba \
  --password=cloudera \
  --table departments \
  --as-textfile \
  --target-dir=/user/cloudera/sqoop_merge/departments
```

--Validate

```bash
sqoop eval --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username retail_dba \
  --password cloudera \
  --query "select * from departments"
```

`hadoop fs -cat /user/cloudera/sqoop_merge/departments/part*`

--update

```bash
sqoop eval --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username retail_dba \
  --password cloudera \
  --query "update departments set department_name='Testing Merge' where department_id = 9000"
```

--Insert

```bash
sqoop eval --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username retail_dba \
  --password cloudera \
  --query "insert into departments values (10000, 'Inserting for merge')"
```

```bash
sqoop eval --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username retail_dba \
  --password cloudera \
  --query "select * from departments"
```

--New load

```bash
sqoop import \
  --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username=retail_dba \
  --password=cloudera \
  --table departments \
  --as-textfile \
  --target-dir=/user/cloudera/sqoop_merge/departments_delta \
  --where "department_id >= 9000"
```

`hadoop fs -cat /user/cloudera/sqoop_merge/departments_delta/part*`

--Merge

```bash
sqoop merge --merge-key department_id \
  --new-data /user/cloudera/sqoop_merge/departments_delta \
  --onto /user/cloudera/sqoop_merge/departments \
  --target-dir /user/cloudera/sqoop_merge/departments_stage \
  --class-name departments \
  --jar-file
```

`hadoop fs -cat /user/cloudera/sqoop_merge/departments_stage/part*`

--Delete old directory

`hadoop fs -rm -R /user/cloudera/sqoop_merge/departments`

--Move/rename stage directory to original directory

`hadoop fs -mv /user/cloudera/sqoop_merge/departments_stage /user/cloudera/sqoop_merge/departments`

--Validate that original directory have merged data

`hadoop fs -cat /user/cloudera/sqoop_merge/departments/part*`

--Merge process ends

## Import a table without primary key

give either ‘-m 1’ or ‘–split-by ‘

```bash
sqoop import \
  --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username retail_dba \
  --password cloudera \
  --table departments_nopk \
  --target-dir /user/cloudera/departments \
  -m 1
```

OR

```bash
sqoop import \
  --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username retail_dba \
  --password cloudera \
  --table departments_nopk \
  --target-dir /user/cloudera/departments \
  --split-by department_id
```

## Incremental

### Option 1 using where

```bash
sqoop import \
  --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username retail_dba \
  --password cloudera \
  --table departments \
  --append \
  --target-dir /user/cloudera/sqoop_import/departments/ \
  --where "department_id > 7"
```

* `–append` and `–where` works togeather in incremental loads. If `–append` not given then it will error out

### Option 2 using incremental-append

```bash
sqoop import \
  --connect "jdbc:mysql://quickstart.cloudera:3306/retail_db" \
  --username retail_dba \
  --password cloudera \
  --table departments \
  --append \
  --target-dir /user/cloudera/sqoop_import/departments/ \
  --check-column department_id \
  --incremental append \
  --last-value 7
```

* –append is req in this case as well
* –check-column : columns against which delta is evaluated
* –last-value: last values from where data has to be imported
* –incremental: append/lastmodified

* –incremental: append – Used when there are only inserts into the the sql table (NO UPDATES)
* –incremental: lastmodified – Used when there are inserts and updates to the SQL table. For this to use we should have date column in the table and –last-value should be the timestamp