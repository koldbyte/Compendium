# Hive CLI

## Available Hive CLI

1. $HIVE_HOME/bin/hive (soon to be deprecated)
1. Beeline (Hiveserver2 based on SQLLine)

## /bin/hive

### Important parameters

* `-h <hostname>`
* `-p <port>`
* `-e <quoted-query-string>`
* `-f <filename>`
* `-S` - for silent
* `-v` - for verbose

### Examples

1. Running a query from the command line (-e)
> `$HIVE_HOME/bin/hive -e 'select a.col from tabl1 a'`

1. Dumping data out of a query into a file (-S)
> `$HIVE_HOME/bin/hive -S -e 'select a.col from tabl1 a' > a.txt`

1. Running a script file non-interactively
> `$HIVE_HOME/bin/hive -f /home/my/hive-script.sql`
> `$HIVE_HOME/bin/hive -f hdfs://<namenode>:<port>/directory/hive-script.sql`

1. Run with logging configuration
> `$HIVE_HOME/bin/hive --hiveconf hive.root.logger=INFO,console`

### Interactive Shell Commands

1. `quit`, `exit`
1. for configuration -> `reset`, `set key=value`, `set`, `set -v`
1. `add FILE[S] filepath filepath*`
1. `add JAR[S] filepath filepath*`
1. `add ARCHIVE[S] filepath filepath*`
1. `list FILE[S]`
1. `list JAR[S]`
1. `list ARCHIVE[S]`
1. `!<command>` - to run shell command
1. `dfs <command>` - run command on dfs
1. `source filepath` - run query from file

## Beeline CLI

### Important Parameters

* `-u <jdbc-database-url>`
* `-n <username>`
* `-p password`
* `-w <password-file>`
* `-e <query-to-run>`
* `-f <script-file>`
* `--delimiter=;` - (default is ';')
* `--silent=true`

### Interactive Shell commands

1. Connect to the hive server : `!connect jdbc:hive2://localhost:10000 scott tiger`
1. `!<SQLLine commands>`
1. `!delimiter`
1. `!quit`

### Connection URL Format

`jdbc:hive2://<host1>:<port1>,<host2>:<port2>/dbName;initFile=<file>;sess_var_list?hive_conf_list#hive_var_list`
