## Log Analysis Project Overview
This log anaylsis program will connect to a PostgreSQL database called 'news', and will list out the most viewed articles, most viewed authors and the dates when more than 1% of the user requests resulted in error. 

###'news' DB tables
          List of relations
| Schema  | Name     | Type  | Owner   | 
|:------ :|:--------:|:-----:|:-------:| 
| public  | articles | table | vagrant |
| public  | authors  | table | vagrant |
| public  | log      | table | vagrant |


###Table "public.articles"

| Column |           Type           |                       Modifiers                       |
|:------:|:------------------------:|:-----------------------------------------------------:|
| author | integer                  | not null                                              |
| title  | text                     | not null                                              |
| slug   | text                     | not null                                              |
| lead   | text                     |                                                       |
| body   | text                     |                                                       |
| time   | timestamp with time zone | default now()                                         |
| id     | integer                  | not null default nextval('articles_id_seq'::regclass) |
Indexes:
    "articles_pkey" PRIMARY KEY, btree (id)
    "articles_slug_key" UNIQUE CONSTRAINT, btree (slug)
Foreign-key constraints:
    "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)

###Table "public.authors"

| Column |  Type   |                      Modifiers                        |
|:------:|:-------:|:-----------------------------------------------------:|
| name   | text    | not null                                              |
| bio    | text    |                                                       |
| id     | integer | not null default nextval('authors_id_seq'::regclass)  |
Indexes:
    "authors_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "articles" CONSTRAINT "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)

###Table "public.log"
| Column |           Type           |                    Modifiers                      |
|:------:|:------------------------:|:-------------------------------------------------:|
| path   | text                     |                                                   |
| ip     | inet                     |                                                   |
| method | text                     |                                                   |
| status | text                     |                                                   |
| time   | timestamp with time zone | default now()                                     |
| id     | integer                  | not null default nextval('log_id_seq'::regclass)  |
Indexes:
    "log_pkey" PRIMARY KEY, btree (id)


## Prerequesites
1. Python 2.7 or above version
2. PostgreSQL with 'news' database preloaded
3. python components
⋅⋅* psycopg2 
⋅⋅* bleach components

## Usage
1. Download the newsdata.sql file from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
2. Initialize the news database
```
$  psql -d news -f newsdata.sql
```
3. Run the log analysis tool.
```
$ python loganalysis.py
```