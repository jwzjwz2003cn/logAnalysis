## Log Analysis Project Overview
This log anaylsis program will connect to a PostgreSQL database called 'news', and will list out the most viewed articles, most viewed authors and the dates when more than 1% of the user requests resulted in error. 

### 'news' DB tables

| Name     | Type  |
|:--------:|:-----:|
| articles | table |
| authors  | table |
| log      | table |


### Table "public.articles"

| Column |           Type           |
|:------:|:------------------------:|
| author | integer                  |
| title  | text                     |
| slug   | text                     |
| lead   | text                     |
| body   | text                     |
| time   | timestamp with time zone |
| id     | integer                  |

### Table "public.authors"

| Column |  Type   |
|:------:|:-------:|
| name   | text    |
| bio    | text    |
| id     | integer |

### Table "public.log"

| Column |           Type           |
|:------:|:------------------------:|
| path   | text                     |
| ip     | inet                     |
| method | text                     |
| status | text                     |
| time   | timestamp with time zone |
| id     | integer                  |


## Prerequesites
1. Python 2.7 or above version
2. PostgreSQL with 'news' database preloaded
3. python components
⋅⋅* psycopg2 
⋅⋅* bleach components

## Usage
1. Download the newsdata.sql file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
2. Initialize the 'news' database
```
$  psql -d news -f newsdata.sql
```
3. Run the log analysis tool.
```
$ python loganalysis.py
```