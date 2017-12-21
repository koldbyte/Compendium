# Flume

Ingest real-time and near-real time streaming data into HDFS using Flume

[Link to User Guide](https://flume.apache.org/FlumeUserGuide.html)

## General

3 components need to be defined:

1. source
1. sink
1. channel

## Source

A non exhaustive list of sources with minimal additional required properties.

### avro

Listens on Avro port and receives events from external Avro client streams.
Additional properties:

    myAgent.sources.mySource.type = avro
    myAgent.sources.mySource.bind = 0.0.0.0
    myAgent.sources.mySource.port = 4141

### thrift

Listens on Thrift port and receives events from external Thrift client streams.
Additional properties:

    myAgent.sources.mySource.type = thrift
    myAgent.sources.mySource.bind = 0.0.0.0
    myAgent.sources.mySource.port = 4141

### exec

Exec source runs a given Unix command
Additional properties:

    myAgent.sources.mySource.type = exec
    myAgent.sources.mySource.command = tail -F /var/log/secure

### spooldir

This source lets you ingest data by placing files to be ingested into a “spooling” directory on disk.
Additional properties:

    myAgent.sources.mySource.type = spooldir
    myAgent.sources.mySource.spoolDir = /var/log/apache/flumeSpool

### syslog

Reads syslog data and generate Flume events.
Additional properties:

    myAgent.sources.mySource.type = syslogtcp #or syslogudp
    myAgent.sources.mySource.port = 5140
    myAgent.sources.mySource.host = localhost

### http

A source which accepts Flume Events by HTTP POST and GET.
Additional properties:

    myAgent.sources.mySource.type = http
    myAgent.sources.mySource.port = 5140

### netcat

A netcat-like source that listens on a given port and turns each line of text into an event. Acts like nc -k -l [host] [port].
Additional properties:

    myAgent.sources.mySource.type = netcat
    myAgent.sources.mySource.bind = 0.0.0.0
    myAgent.sources.mySource.port = 6666

## Sink

A non exhaustive list of sinks with minimal additional required properties.

### hdfs

This sink writes events into the HDFS. Consult the documentation !
Additional properties:

    myAgent.sinks.mySink.type = hdfs
    myAgent.sinks.mySink.hdfs.path = /flume/events/%y-%m-%d/%H%M/%S

### logger

Logs event at INFO level.
Additional properties:

    myAgent.sinks.mySink.type = logger

### avro

Flume events sent to this sink are turned into Avro events and sent to the configured hostname / port pair.
Additional properties:

    myAgent.sinks.mySink.type = avro
    myAgent.sinks.mySink.hostname = 10.10.10.10
    myAgent.sinks.mySink.port = 4545

### irc

The IRC sink takes messages from attached channel and relays those to configured IRC destinations.
Additional properties:

    myAgent.sinks.mySink.type = irc
    myAgent.sinks.mySink.hostname = irc.yourdomain.com
    myAgent.sinks.mySink.nick = flume
    myAgent.sinks.mySink.chan = #flume

### null

Discards all events it receives from the channel. 
Additional properties:

    myAgent.sinks.mySink.type = null

### hBaseSink

This sink writes data to HBase. Consult the documentation !
Additional properties:

    myAgent.sinks.mySink.type = hbase
    myAgent.sinks.mySink.table = foo_table
    myAgent.sinks.mySink.columnFamily = bar_cf

## Channel

A non exhaustive list of channels with minimal additional required properties.

### Memory

The events are stored in an in-memory queue with configurable max size. It’s ideal for flows that need higher throughput and are prepared to lose the staged data in the event of a agent failures.
Additional properties:

    myAgent.channels.myChannel.type = memory

### JDBC

The events are stored in a persistent storage that’s backed by a database.
Additional properties:

    myAgent.channels.myChannel.type = jdbc

### File

The events are stored in on the local disc in files.
Additional properties:

    myAgent.channels.myChannel.type = file

## 1. Ingest real-time and near-real time streaming data

### Configuration

    myAgent.sources = mySource
    myAgent.channels = myChannel
    myAgent.sinks = mySink

    myAgent.sources.mySource.type = spooldir
    myAgent.sources.mySource.spoolDir = /var/data/incoming
    myAgent.sources.mySource.channels = myChannel

    myAgent.channels.myChannel.type = memory

    myAgent.sinks.mySink.type = hdfs
    myAgent.sinks.mySink.hdfs.path = hdfs:///data/logs
    myAgent.sinks.mySink.hdfs.fileType = DataStream
    myAgent.sinks.mySink.channel = myChannel

Save this in a file. For example: myAgent.conf

### Start the agent

    $ flume-ng agent \
        --conf /etc/flume-ng/conf \
        --conf-file ./myAgent.conf \
        --name myAgent \
        -Dflume.root.logger=INFO,console