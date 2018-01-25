# Functions available in Dataframe

## Aggregate Functions

* approxCountDistinct
* avg
* collect_list
* collect_set
* count
* countDistinct
* max
* mean
* min
* stddev
* sum
* sumDistinct
* variance

## Collection functions

* array_contains
* explode
* get_json_object
* json_tuple
* sort_array
* size

## Date/Time Functions

* add_months
  * add_months(startDate: Column, numMonths: Int): Column

Returns the date that is numMonths after startDate.

* date_add
  * date_add(start: Column, days: Int): Column

Returns the date that is days days after start

* date_sub
  * date_sub(start: Column, days: Int): Column

Returns the date that is days days before start

* from_unixtime
  * from_unixtime(ut: Column, f: String): Column

Converts the number of seconds from unix epoch (1970-01-01 00:00:00 UTC) to a string representing the timestamp of that moment in the current system time zone in the given format.

* from_utc_timestamp
  * from_utc_timestamp(ts: Column, tz: String): Column

Assumes given timestamp is UTC and converts to given timezone.

* to_utc_timestamp
  * to_utc_timestamp(ts: Column, tz: String): Column

Assumes given timestamp is in given timezone and converts to UTC.

* unix_timestamp
  * unix_timestamp(s: Column, p: String): Column

Convert time string with given pattern (SimpleDateFormat) to Unix time stamp (in seconds), return null if fail. Default pattern is yyyy-MM-dd HH:mm:ss

Note: Date and time format Specifiers

* last_day
* next_day

* current_date
* current_timestamp
* dayofmonth
* dayofyear
* hour
* minute
* month
* quarter
* second
* weekofyear
* year

## Math Functions

* sin
* cos
* tan

* asin
* acos
* atan

* toRadians
* toDegrees

* round
* ceil
* floor
* log

* factorial
* pow

* hex

* cbrt
* sqrt

## Misc. Functions

* crc32
* md5
* sha1
* sha2

## Non-aggregate Functions

* abs
* greatest
* isnan
* isnull
* lit
* rand
* struct
* when

## Sorting

* asc
* desc

## String functions

* ascii
* concat
* format_number
  * format_number(x: Column, d: Int): Column

Formats numeric column x to a format like '#,###,###.##', rounded to d decimal places, and returns the result as a string column.

If d is 0, the result has no decimal point or fractional part. If d < 0, the result will be null.

* format_string
  * format_string(format: String, arguments: Column*): Column

Formats the arguments in printf-style and returns the result as a string column.

* length
* locate
* lpad
* ltrim
* repeat
* reverse
* rtrim
* rpad
* split
* trim
* upper

## Window Functions

* dense_rank

Window function: returns the rank of rows within a window partition, without any gaps.

* lag
  * lag(e: Column, offset: Int, defaultValue: Any): Column

Window function: returns the value that is offset rows before the current row, and defaultValue if there is less than offset rows before the current row. For example, an offset of one will return the previous row at any given point in the window partition.

* lead
  * lead(e: Column, offset: Int, defaultValue: Any): Column

Window function: returns the value that is offset rows after the current row, and defaultValue if there is less than offset rows after the current row. For example, an offset of one will return the next row at any given point in the window partition.

* ntile
  * ntile(n: Int): Column

Window function: returns the ntile group id (from 1 to n inclusive) in an ordered window partition. Fow example, if n is 4, the first quarter of the rows will get value 1, the second quarter will get 2, the third quarter will get 3, and the last quarter will get 4.

* percent_rank

Window function: returns the relative rank (i.e. percentile) of rows within a window partition.

* rank

Window function: returns the rank of rows within a window partition.

* row_number

Window function: returns a sequential number starting at 1 within a window partition.
