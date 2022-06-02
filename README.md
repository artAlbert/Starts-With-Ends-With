# Starts With Ends With
Project Links: [React frontend](https://main.djf9hwudvwist.amplifyapp.com) || [Flask backend](https://flask-service.a1cqh1bc24r90.us-east-1.cs.amazonlightsail.com) ||

Built with React (hosted on AWS Amplify), Flask (hosted on Amazon Lightsail), and PostgreSQL (hosted on AWS RDS)

![FacebookTeaser2](https://user-images.githubusercontent.com/103860612/171473732-6398c073-db43-450e-b11d-d48cbfadc5bd.jpg)

**Starts With Ends With** is a web application inspired by clickbait intelligence tests. I saw a post like the one above and I got curious about all the words that start and end with 'M', so I created an application that iterates over 36600 English words [^1] and returns the results. 

## How It Works

The app currently has two modes: finding words that start and end with the same letter, and finding words that start and end with different letters. Both options take user input, make an API call to the backend, and return the words that match the search query along with their meanings and a count of the total matches found.

### Front-End

  The React app offers radio buttons to switch between the two modes, and text fields to accept user input (these fields are limited to one character). The radio button selector and the input fields are separate React components. The radio selector component (RadioSelection.js) passes the mode choice as a prop to the input field component (PostForm.js), which provides the necessary number of text fields and waits for input. The user enters which starting-and-ending-character words they'd like to search for, and the input field component passes this information along to a fetching component (FetchWords.js) which builds the API call to the backend with the user's input as variables and sends a GET request.
  
### Back-End

  The Flask app has two routes to match the two modes: `/starts-and-ends-with?letter={}` for the first mode, and `/starts-with-ends-with?first={}&last={}` for the second mode. When the front-end makes a call to either URL, the back-end builds an SQL query with a REGEX matching pattern using the supplied variable. Then it connects to the PostgreSQL AWS RDS database using Psycopg2 and executes the search. The database returns the matches as a list of tuples, with information like word_id (sequential key), letter, word, and meaning. The back-end takes this information and builds a JSON response which it returns for the React app to display. 


[^1]: The dataset I found containing both words and their meanings only has about 36,600 entries. Oxford's Advanced Learner's Dictionary contains about 60,000 words.
