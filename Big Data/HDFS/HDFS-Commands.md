# Overview
The HDFS fs-shell supports various shell-like commands to interact with the Hadoop Distributed File System (HDFS) as well as other file systems that Hadoop supports, such as Local FS, HFTP FS, S3 FS, and others. The FS shell is invoked by:
> `bin/hadoop fs <args>`

# Common commands
1. **appendToFile**
> Append single src, or multiple srcs from local file system to the destination file system. Also reads input from stdin and appends to destination file system.

1. **cat**
> Copies source paths to stdout

1. **copyFromLocal**
1. **copyToLocal**
1. **count**
1. **cp**
1. **get**
1. **getmerge**
1. **ls**
1. **mkdir**
1. **moveFromLocal**
1. **moveToLocal**
1. **mv**
1. **put**
1. **rm**
1. **tail**
1. **test**

# Other commands
1. **chgrp**
1. **chmod**
1. **chown**
1. **du**
1. **expunge**
1. **getfacl**
1. **getfattr**
1. **setfacl**
1. **setfattr**
1. **setrep**
1. **stat**
1. **touchz**
1. **text**

# Reading List
1. [FS Shell Commands][http://hadoop.apache.org/docs/r2.6.0/hadoop-project-dist/hadoop-common/FileSystemShell.html]
1. [Hadoop Commands][http://hadoop.apache.org/docs/r2.6.0/hadoop-project-dist/hadoop-hdfs/HDFSCommands.html]