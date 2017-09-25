"""
Execute select statements in postgres and store it's output as CSV files.
"""

import csv
import psycopg2

# Example connection, this has to be changed!
conn = psycopg2.connect("dbname=quast user=meet")

SELECT_STATEMENTS = [
    # Example statements
    # Populate this list with all the select statements whose output has to be
    # stored as CSV.
    "select * from answers where qid in (select qid from questions where author='meetmangukiya')",
    "select * from questions where author in (select followed_by from followers where following_to='meetmangukiya')",
    "select * from answers where author not in (select following_to from followers where followed_by='meetmangukiya');",
    "select * from answers where upvotes > all(select upvotes from questions);",
    "select * from answers where downvotes < some(select downvotes from questions);",
    "select * from questions where qid=1 and exists(select * from question_comments where qid=1);",
    "select * from questions where qid=1 and not exists(select * from question_comments where qid=2);",
    "select * from questions where qid in (select qid from question_comments);",
    "select * from questions where qid not in (select qid from question_comments);",
    "select * from questions where qid not in (select qid from answers);"
]

with conn.cursor() as curs:
    for i, statement in enumerate(SELECT_STATEMENTS):
        curs.execute(statement)
        data = curs.fetchall()
        with open("statement" + str(i) + ".csv", 'w') as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(list(row))
