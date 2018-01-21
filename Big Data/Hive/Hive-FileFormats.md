# File formats support in Hive

## AVRO

> [Wiki Page for AvroSerde](https://cwiki.apache.org/confluence/display/Hive/AvroSerDe)
> AvroSerde is available since Hive v0.9.1.

### Creating a Avro backed table

* From existing schema (.avsc)

```sql
CREATE TABLE kst
  PARTITIONED BY (ds string)
  ROW FORMAT SERDE
  'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
  STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
  OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
  TBLPROPERTIES (
    'avro.schema.url'='http://schema_provider/kst.avsc');
```

* Storing as a new schema

```sql
CREATE TABLE as_avro (
    string1 string
    PARTITIONED BY (ds string)
STORED AS AVRO;
-- Add data from any type of table as long as schema is compatible
INSERT OVERWRITE TABLE as_avro SELECT * FROM normal_table;
```

* Generating Avro Schema from existing avro file
> After inserting records into an avro backed table, download a small portion of the data onto local drive.
Run `avro-tools getschema filename`. This will print out the schema. Use indirection or copy paste to save it as a .avsc file.

## Parquet files

* Creating a new table stored as parquet

```sql
CREATE TABLE parquet_test (
 id int,
 str string,
 mp MAP<STRING,STRING>,
 lst ARRAY<STRING>,
 strct STRUCT<A:STRING,B:STRING>)
PARTITIONED BY (part string)
STORED AS PARQUET;
```

* ParquetSerde
> `parquet.hive.serde.ParquetHiveSerDe`

## Compressing

You can import text files compressed with Gzip or Bzip2 directly into a table stored as TextFile. The compression will be detected automatically and the file will be decompressed on-the-fly during query execution.Ex-

```sql
CREATE TABLE raw (line STRING)
   ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n';

LOAD DATA LOCAL INPATH '/tmp/weblogs/20090603-access.log.gz' INTO TABLE raw;
```

Note: GZ is non-splittable format. Convert it or use a splittable format for better performance.

## [SerDes available in Hive](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-RowFormats&SerDe)

* [Avro](https://cwiki.apache.org/confluence/display/Hive/AvroSerDe) (Hive 0.9.1 and later)
    `org.apache.hadoop.hive.serde2.avro.AvroSerDe`
* [ORC](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+ORC) (Hive 0.11 and later)
* [RegEx](https://cwiki.apache.org/confluence/display/Hive/GettingStarted#GettingStarted-ApacheWeblogData)
    `org.apache.hadoop.hive.serde2.RegexSerDe`
* [Thrift](http://thrift.apache.org/)
* [Parquet](https://cwiki.apache.org/confluence/display/Hive/Parquet) (Hive 0.13 and later)
    `parquet.hive.serde.ParquetHiveSerDe`
* [CSV](https://cwiki.apache.org/confluence/display/Hive/CSV+Serde) (Hive 0.14 and later)
    `org.apache.hadoop.hive.serde2.OpenCSVSerde`
* JsonSerDe (Hive 0.12 and later in hcatalog-core)
    `org.apache.hive.hcatalog.data.JsonSerDe`
    > Requires `ADD JAR /usr/lib/hive-hcatalog/share/hcatalog/hive-hcatalog-core.jar;` on some distributions.