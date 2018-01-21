# Delimiters and File formats arguments

## Delimiters

### Import

* --enclosed-by <char> 	Sets a required field enclosing character
* --escaped-by <char> 	Sets the escape character
* --fields-terminated-by <char> 	Sets the field separator character
* --lines-terminated-by <char> 	Sets the end-of-line character
* --mysql-delimiters 	Uses MySQL’s default delimiter set: fields: , lines: \n escaped-by: \ * optionally-enclosed-by: '
* --optionally-enclosed-by <char> 	Sets a field enclosing character 

### Export

* --input-enclosed-by <char> 	Sets a required field encloser
* --input-escaped-by <char> 	Sets the input escape character
* --input-fields-terminated-by <char> 	Sets the input field separator
* --input-lines-terminated-by <char> 	Sets the input end-of-line character
* --input-optionally-enclosed-by <char> 	Sets a field enclosing character 

## File formats

* --as-avrodatafile 	Imports data to Avro Data Files
* --as-sequencefile 	Imports data to SequenceFiles
* --as-textfile 	Imports data as plain text (default)
* --as-parquetfile 	Imports data to Parquet Files