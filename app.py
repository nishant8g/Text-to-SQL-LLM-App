from dotenv import load_dotenv
load_dotenv()#load all the environment variable

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

#configure our api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load google geini model and provide sql query as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text


#function to retruieve query to sql database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows
##define your prompt
prompt=[
    """
    you are an expert to converting english questions to sql query!
    The sql database has the students and has the following columns- NAME,CLASS,
    SECTION,MARKS\n\nfor example,\nExample 1- How many entries of records are present?,
    the sql command will be something like this SELECT COUNT(*) from students;
    \n example 2-Tell me all the students studying in 10 class?,
    the sql command will be something like this SELECT * from students WHERE CLASS='10';
    \n example 3-What is the average marks of students studying in 10 class?
    alse the sql code shouls not have ``` in beginning or end and sql word in the output```


    """
]


##streamlit app

st.set_page_config(page_title="I can retrieve any SQL querry")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("input: ",key="input")
submit=st.button('Ask The Question')

#if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("the Response is")
    for row in data:
        print(row)
        st.header(row)


