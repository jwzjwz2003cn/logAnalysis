# Database code for the Log Analysis Project.
#

import psycopg2
import bleach

DBNAME = "news"

def execute_queries(queryString):
    try:    
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(queryString)
        posts = c.fetchall()
        db.close()
        return posts
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def get_top_three_articles():
    """Return top three viewed articles """
    queryString = """
        SELECT a.title, count(l.id) AS num 
        FROM articles a
        INNER JOIN log l ON '/article/' || a.slug = l.path 
        GROUP BY a.title 
        ORDER BY num desc limit 3
        """
    posts = execute_queries(queryString)
    return posts


def get_top_authors():
    """Rank authors based on the total views of his/her articles"""
    queryString = """
        SELECT c.name, sum(b.num) AS total 
        FROM 
        (SELECT a.slug, a.author, a.title,  count(l.id) 
        AS num FROM articles a INNER JOIN log l ON 
        '/article/' || a.slug = l.path 
        GROUP BY a.slug, a.author, a.title ORDER BY num DESC) AS b 
        INNER JOIN authors c ON b.author = c.id 
        GROUP BY c.name ORDER BY total DESC
        """
    posts = execute_queries(queryString)
    return posts


def get_high_http_error_date():
    """Return the dates when bad requests consists
        more than 1% of the total request"""
    queryString = """
        SELECT * 
        FROM 
        (SELECT t.bad_req, t.total_req, 
        t.bad_req::FLOAT/t.total_req::FLOAT*100 AS error, t.date 
        FROM 
        (SELECT COUNT(status) FILTER (WHERE status NOT LIKE '2%') 
        AS bad_req, count(status) AS total_req, 
        CAST(time AS DATE) as date 
        FROM log 
        GROUP by CAST(time AS DATE)) AS t) AS innertable 
        WHERE innertable.error > 1
        """
    posts = execute_queries(queryString)
    return posts
