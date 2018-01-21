# Hive DML

> [Wiki Page](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DML)

## Loading files into tables

```sql
LOAD DATA [LOCAL] INPATH 'filepath' [OVERWRITE] INTO TABLE tablename [PARTITION (partcol1=val1, partcol2=val2 ...)]
```

Notes:

* filepath can be relative, absolute or full URI with schema but cannot contain subdirectories
* If the table is partitioned, then one must specify a specific partition of the table by specifying values for all of the partitioning columns.
* LOCAL will make the load command to look for filepath in the local file system
* OVERWRITE means the contents of the target table (or partition) will be deleted and replaced by the files referred to by filepath

## Inserting data into Hive Tables from queries

```sql
INSERT [OVERWRITE] TABLE tablename1 [PARTITION (partcol1=val1, partcol2=val2 ...) [IF NOT EXISTS]] select_statement1 FROM from_statement;
```

```sql
# Multiple Inserts
FROM from_statement
INSERT [OVERWRITE] TABLE tablename1 [PARTITION (partcol1=val1, partcol2=val2 ...) [IF NOT EXISTS]] select_statement1
[INSERT [OVERWRITE] TABLE tablename2 [PARTITION ... [IF NOT EXISTS]] select_statement2]
...
```

```sql
# Hive extension (dynamic partition inserts):
INSERT [OVERWRITE] TABLE tablename PARTITION (partcol1[=val1], partcol2[=val2] ...) select_statement FROM from_statement;
```

## Writing data into the filesystem from queries

```sql
INSERT OVERWRITE [LOCAL] DIRECTORY directory1
  [ROW FORMAT row_format] [STORED AS file_format] (Note: Only available starting with Hive 0.11.0)
  SELECT ... FROM ...
```

Row format is defined as below:

```sql
DELIMITED [FIELDS TERMINATED BY char [ESCAPED BY char]]
[COLLECTION ITEMS TERMINATED BY char]
[MAP KEYS TERMINATED BY char]
[LINES TERMINATED BY char]
[NULL DEFINED AS char] (Note: Only available starting with Hive 0.13)
```

```sql
FROM from_statement
INSERT OVERWRITE [LOCAL] DIRECTORY directory1 select_statement1
[INSERT OVERWRITE [LOCAL] DIRECTORY directory2 select_statement2] ...
```

## Inserting values into tables from SQL

```sql
INSERT INTO TABLE tablename [PARTITION (partcol1[=val1], partcol2[=val2] ...)] VALUES values_row [, values_row ...]
```

## Update

```sql
UPDATE tablename SET column = value [, column = value ...] [WHERE expression]
```

Note:

* Only rows that match the WHERE clause will be updated.
* Partitioning columns cannot be updated.
* Bucketing columns cannot be updated.

## Delete

```sql
DELETE FROM tablename [WHERE expression]
```

## Merge

```sql
MERGE INTO <target table> AS T USING <source expression/table> AS S
ON <boolean expression1>
WHEN MATCHED [AND <boolean expression2>] THEN UPDATE SET <set clause list>
WHEN MATCHED [AND <boolean expression3>] THEN DELETE
WHEN NOT MATCHED [AND <boolean expression4>] THEN INSERT VALUES<value list>
```