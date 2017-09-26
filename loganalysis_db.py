# Database code for the Log Analysis Project.
#

import psycopg2
import bleach

DBNAME = "news"


def get_top_three_articles():
    """Return top three viewed articles """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(
        "select a.title, count(l.id) as num from articles "
        "a inner join log l on a.slug = "
        "substring(l.path from '/article/#\"%#\"' for '#') "
        "group by a.title order by num desc limit 3")
    posts = c.fetchall()
    db.close()
    return posts


def get_top_authors():
    """Rank authors based on the total views of his/her articles"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(
        "select c.name, sum(b.num) as total from "
        "(select a.slug, a.author, a.title,  count(l.id) "
        "as num from articles a inner join log l on a.slug = "
        "substring(l.path from '/article/#\"%#\"' for '#') "
        "group by a.slug, a.author, a.title order by num desc) as b "
        "inner join authors c on b.author = c.id "
        "group by c.name order by total desc")
    posts = c.fetchall()
    db.close()
    return posts


def get_high_http_error_date():
    """Return the dates when bad requests consists
        more than 1% of the total request"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(
        "select * from (select t.bad_req, t.total_req, "
        "t.bad_req::float/t.total_req::float*100 as error, t.date "
        "from (select count(status) FILTER (WHERE status not like '2%') "
        "as bad_req, count(status) as total_req, "
        "CAST(time AS DATE) as date "
        "from log group by CAST(time AS DATE)) as t) as innertable "
        "where innertable.error > 1")
    posts = c.fetchall()
    db.close()
    return posts
