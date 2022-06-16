from distutils.command.build import build
from email.policy import default
from urllib import response
from flask import Flask
from flask import request

import os
import psycopg2
import json

app = Flask(__name__)

def connect_to_database():
    """Establishes a connection with the database

    Args: 
        none

    Returns:
        conn (object): connection to the PostgreSQL database instance 
    """

    conn = psycopg2.connect(host='HOST',
                            database='DATABASE',
                            user="USER",
                            password="PASSWORD",
                            port="PORT")
    
    return conn


def execute_query(conn, SQL, data):
    """Executes a database query and fetch the results

    Args:
        conn (object): connection to the PostgreSQL database instance 
        SQL (str): the query string with argument parameters
        data (tuple): variables to match the parameters in the SQL query string
    
    Returns:
        searchResults (List[(tuples)]): results from the database query
    """
    # Execute query
    cur = conn.cursor()
    cur.execute(SQL, data)

    # Fetch results (Stored as a list of tuples)
    searchResults = cur.fetchall()

    # Close connections
    cur.close()
    conn.close()

    return searchResults


def build_response(searchResults):
    """Creates the JSON response from the query results
    
    Builds a dictionary structure from the database results where the 'count' key is
    the number of matches, and the 'words' key is a list of dictionaries containing the
    database rows (unique id, letter, word, meaning). The dictionary is serialized into 
    JSON and returned.

    Example:
        {
            'count': 2,
            'words': [
                {
                    'word_id' : '1',
                    'letter': 'p',
                    'word': 'potato',
                    'meaning': "vegetable"
                },
                {
                    'word_id': '2',
                    'letter' : 't',
                    'word': 'tomato',
                    'meaning': "fruit"
                }
            ]
        }

    Args:
        searchResults (List[(tuples)]): results from a database query

    Returns:
        responseJson (dict): serialized dictionary containing the query data
    """
    responseDict = {
        "count": 0,
        "words": []
    }

    wordList = responseDict["words"]

    for tuple in searchResults:
        wordPairing = {
            # .lower() is called because the words stored in the database are capitalized.
            "word_id": tuple[0],
            "letter": tuple[1],
            "word" : str(tuple[2]).lower(),
            "meaning" : tuple[3]
        }
        wordList.append(wordPairing)  

    wordListSize = len(wordList)
    responseDict["count"] = wordListSize

    # JSON-ify
    responseJson = json.dumps(responseDict, indent = 4)

    return responseJson


@app.route("/starts-and-ends-with")
def startsAndEndsWith():
    """Match words which begin and end with the same letter.

    Args:
        None

    Returns:
        responseJson (dict): serialized dictionary containing words that start
        and end with the same letter, and their meanings.
    """

    # Get the starts-with and ends-with character
    letter = request.args.get('letter', default = 'a', type = str)

    # Check input
    if len(letter) > 1:
        # Return error without executing a search in database
        return ("""{ "errors": [{"code":211, "message":"Incorrect input length"}]}""")
    
    # Build query
    SQL = "SELECT * FROM word_dict WHERE word ~ (%s);"

    data = ("^" + letter.upper() + ".*" + letter.lower() + "$", )

    # Connect to database
    conn = connect_to_database()

    # Execute query
    searchResults = execute_query(conn, SQL, data)

    # Build response
    responseJson = build_response(searchResults)

    return responseJson


# Match words which begin with one letter and end with another.
@app.route("/starts-with-ends-with")
def startsWithEndsWith():
    """Match words which begin with the given 'first' letter , and end 
    with the given 'last' letter.

    Args:
        None

    Returns:
        responseJson (dict): serialized dictionary containing words that start
        with letter 'first' and end with letter 'last', and their meanings.
    """

    # Get the starting and the ending characters
    first = request.args.get('first', default = 'a', type = str)
    last = request.args.get('last', default = 'a', type = str)

    # Check input
    if len(first) or len(last) > 1:
        # Return error without executing a search in database
        return ("""{ "errors": [{"code":211, "message":"Incorrect input length"}]}""")

    # Build query
    SQL = "SELECT * FROM word_dict WHERE word ~ (%s);"
    data = ("^" + first.upper() + ".*" + last + "$", )

    # Connect to database
    conn = connect_to_database()

    # Execute query
    searchResults = execute_query(conn, SQL, data)

    # Build response
    responseJson = build_response(searchResults)

    return responseJson
    

if __name__=='__main__':
    app.run()
