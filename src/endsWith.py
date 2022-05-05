from email.policy import default
from flask import Flask
from flask import request

import os
import psycopg2

app = Flask(__name__)

def connect_to_database():
    conn = psycopg2.connect(host='localhost',
                            database='endsWith',
                            user="postgres",
                            password="adminAdmin123!")
    return conn

# Match words which begin and end with the same letter.
@app.route("/starts-and-ends-with")
def startsAndEndsWith():
    # Get the starts-with and ends-with character.
    letter = request.args.get('letter', default = 'a', type = str)
    
    # Connect to postgresql database
    conn = connect_to_database()
    cur = conn.cursor()

    # Query
    SQL = "SELECT word, meaning FROM oedict WHERE word ~ (%s) LIMIT 10;"
    data = ("^" + letter.upper() + ".*" + letter + "$", )
    cur.execute(SQL, data)

    # Save output.
    matches = str(cur.fetchall())

    # Close connections.
    cur.close()
    conn.close()
    return matches

# Match words which begin with one letter and end with another
@app.route("/starts-with-ends-with")
def startsWithendsWith():
    # Get the starting and the ending characters.
    first = request.args.get('first', default = 'a', type = str)
    last = request.args.get('last', default = 'a', type = str)

    # Connect to postgresql database
    conn = connect_to_database()
    cur = conn.cursor()

    # Query
    SQL = "SELECT word, meaning FROM oedict WHERE word ~ (%s) LIMIT 10;"
    data = ("^" + first.upper() + ".*" + last + "$", )
    cur.execute(SQL, data)

    # Save output.
    matches = str(cur.fetchall())

    # Close connections.
    cur.close()
    conn.close()
    return matches

if __name__=='__main__':
    app.run()
