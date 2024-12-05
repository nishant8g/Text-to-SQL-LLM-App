Gemini App to Retrieve SQL Data

🚀 What the Project Does
This app allows users to:
* Ask natural language questions about a students' database and retrieve answers.
* Automatically converts the question into an SQL query using Google Gemini AI.
* Executes the query on an SQLite database and displays the results.
  
The students' database contains the following columns:

NAME
CLASS
SECTION
MARKS
Example questions:

"How many records are present?" → SQL: SELECT COUNT(*) FROM students;
"Tell me all the students studying in class 10." → SQL: SELECT * FROM students WHERE CLASS='10';
"What is the average marks of students in class 10?"

🌟 Why the Project is Useful
Time-Saving: Converts natural language questions to SQL queries instantly.
AI-Powered: Uses advanced AI to interpret user intent and generate precise SQL queries.
Educational Tool: Great for learning SQL or understanding data interactions in a database.
Dynamic Querying: Adapts to any question structure, making querying databases user-friendly.
