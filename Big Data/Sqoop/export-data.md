# Exporting data through Sqoop

The export tool exports a set of files from HDFS back to an RDBMS. The target table must already exist in the database. The input files are read and parsed into a set of records according to the user-specified delimiters.

The default operation is to transform these into a set of INSERT statements that inject the records into the database.

## Basic Syntax

`sqoop export (generic-args) (export-args)`

## Common Arguments

* `--connect <jdbc-url>`
* `--driver <class-name>`
* `--username <username>`
* `--password <password>`
* `-P` Read password from Console
* `--verbose`

## Required Arguments

* `--table <table-name>` the table to populate in the database
* `--export-dir <dir>`  the directory in HDFS that contains the source data

## Export control arguments

* `--direct`  use direct export fast path (using `mysqlimport` for mysql)
* `-m <n>`, `--num-mappers <n>` Use `n` map tasks to export in parallel. Default is 4.
* `--input-null-string <null-string>` The string to be interpreted as null for string columns. Default is `null`.
* `--input-null-non-string <null-string>`  The string to be interpreted as null for non-string columns. Default is `null` and empty content is always treated as null value.
* `--batch` Use batch mode for underlying statement execution

## Staging Mode

`--staging-table`
specify a staging table via the --staging-table option which acts as an auxiliary table that is used to stage exported data. The staged data is finally moved to the destination table in a single transaction.

Used when avoiding job failure due to insert collisions or duplicated data.

Staging table must be created prior to running and is structurally similar to the target table.

## Inserts vs Updates

By default, Sqoop transforms each record into Insert statements. This mode is primarily intended for exporting records to a new, empty table intended to receive these results.

If you specify the --update-key argument, Sqoop will instead modify an existing dataset in the database.
The row a statement modifies is determined by the column name(s) specified with `--update-key`. In effect, this means that an update-based export will not insert new rows into the database.

Depending on the target database, you may also specify the `--update-mode` argument with `allowinsert` mode if you want to update rows if they exist in the database already or insert rows if they do not exist yet.

* `--update-key <col-name>`
* `--update-mode <mode>` Legal values for mode include `updateonly` (default) and `allowinsert`

## Input Parsing Arguments

* `--input-enclosed-by <char>` Sets a required field encloser
* `--input-escaped-by <char>` Sets the input escape character
* `--input-fields-terminated-by <char>` Sets the input field separator
* `--input-lines-terminated-by <char>` Sets the input end-of-line character
* `--input-optionally-enclosed-by <char>` Sets a field enclosing charcter

## Output formatting Arguments

* `--enclosed-by <char>` Sets a required field enclosing character
* `--escaped-by <char>` Sets the escape character
* `--fields-terminated-by <char>` Sets the field separator character
* `--lines-terminated-by <char>` Sets the end-of-line character
* `--mysql-delimiters` Uses MySQL’s default delimiter set: fields: `,` lines: `\n` escaped-by: `\`  optionally-enclosed-by: `'`
* `--optionally-enclosed-by <char>` Sets a field enclosing character

## Examples

### Export to a table

```bash
sqoop export \
    --connect jdbc:mysql://db.example.com/foo \
    --table bar  \
    --export-dir /results/bar_data
```