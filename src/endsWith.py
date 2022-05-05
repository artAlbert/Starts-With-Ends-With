from email.policy import default
from urllib import response
from flask import Flask
from flask import request

import os
import psycopg2
import json

app = Flask(__name__)

def connect_to_database_and_execute(SQL, data):

    # Establish connection with the database
    conn = psycopg2.connect(host='localhost',
                            database='endsWith',
                            user="postgres",
                            password="adminAdmin123!")
    
    # Execute query
    cur = conn.cursor()
    cur.execute(SQL, data)

    # Fetch results (Stored as a list of tuples)
    searchResults = cur.fetchall()

    # Close connections
    cur.close()
    conn.close()

    return searchResults


# Match words which begin and end with the same letter.
@app.route("/starts-and-ends-with")
def startsAndEndsWith():

    # Get the starts-with and ends-with character
    letter = request.args.get('letter', default = 'a', type = str)
    
    # Build query
    SQL = "SELECT word, meaning FROM oedict WHERE word ~ (%s);"
    data = ("^" + letter.upper() + ".*" + letter + "$", )

    # Get database results
    queryData = connect_to_database_and_execute(SQL, data)

    # Build response
    responseDict = {
        "count": 0,
        "words": []
    }
    wordCounter = 0
    wordList = responseDict["words"]
    for tuple in queryData:
        wordPairing = {
            "word" : str(tuple[0]).lower(),
            "meaning" : tuple[1]
        }
        wordCounter += 1
        wordList.append(wordPairing)    
    responseDict["count"] = wordCounter

    # JSON-ify
    responseJson = json.dumps(responseDict, indent = 4)

    return responseJson


# Match words which begin with one letter and end with another.
@app.route("/starts-with-ends-with")
def startsWithendsWith():

    # Get the starting and the ending characters
    first = request.args.get('first', default = 'a', type = str)
    last = request.args.get('last', default = 'a', type = str)

    # Build query
    SQL = "SELECT word, meaning FROM oedict WHERE word ~ (%s);"
    data = ("^" + first.upper() + ".*" + last + "$", )

    # Get database results
    queryData = connect_to_database_and_execute(SQL, data)

    # Build response
    responseDict = {
        "count": 0,
        "words": []
    }
    wordCounter = 0
    wordList = responseDict["words"]
    for tuple in queryData:
        wordPairing = {
            "word" : str(tuple[0]).lower(),
            "meaning" : tuple[1]
        }
        wordCounter += 1
        wordList.append(wordPairing)
    responseDict["count"] = wordCounter

    # JSON-ify
    responseJson = json.dumps(responseDict, indent = 4)
    
    return responseJson
    

if __name__=='__main__':
    app.run()
