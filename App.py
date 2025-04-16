from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import sqlite3
import pandas as pd
import google.generativeai as genai

# Configure Google Generative AI Key
genai.configure(api_key=(st.secrets.get("GOOGLE_API_KEY",os.getenv("GOOGLE_API_KEY"))))

# Function To Load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash-8b-exp-0924')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function To retrieve query from the database and capture column names
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    try:
        cur.execute(sql)
        # Get column names from the cursor description
        columns = [desc[0] for desc in cur.description] if cur.description else []
        rows = cur.fetchall()
    except Exception as e:
        st.error(f"An error occurred: {e}")
        columns = []
        rows = []
    finally:
        conn.commit()
        conn.close()
    return columns, rows

# Define Your Prompt (updated for EMPLOYEES table)
prompt = ["""
You are an expert in converting English questions to SQL query!
The SQL database has the name EMPLOYEES and has the following columns - employee_id, first_name, last_name, age, gender, department, salary, location.
For example,
Example 1 - How many employees are there?, the SQL command will be: SELECT COUNT(*) FROM EMPLOYEES;
Example 2 - Show all the employees in the Engineering department?, the SQL command will be: SELECT * FROM EMPLOYEES WHERE department='Engineering';
Make sure the SQL code is plain without any extra markdown formatting.
"""]

# Enhanced Streamlit Interface
st.set_page_config(page_title="NeuraQuery: Query Employee Database", layout="wide")
st.title("NeuraQuery")
st.markdown("""
Welcome to the **NeuraQuery**!
This app uses our sample Employee database. You can ask questions in plain English, and our system will convert them into SQL queries and execute them against the database.
**Database Details:**
- **Table Name:** EMPLOYEES
- **Columns:** employee_id, first_name, last_name, age, gender, department, salary, location
""")

# Sidebar instructions for better user understanding
st.sidebar.header("How It Works")
st.sidebar.markdown("""
1. **Enter a Question:** Write your question about the Employee database.  
2. **Generate SQL Query:** Our integrated Gemini model will convert your question into a SQL query.  
3. **View Results:** The SQL query and its results will be displayed below.

*Example questions:*
- "How many employees are in the database?"
- "List all employees in the IT department."
""")

# User input area for SQL question
question = st.text_input("Enter your question about the Employee Database:")

submit = st.button("Ask the question")

# Process the question when the submit button is clicked
if submit:
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        # Generate SQL Query from the user's question
        response_sql = get_gemini_response(question, prompt)
        st.write("#### Generated SQL Query:")
        st.code(response_sql, language='sql')

        # Execute the query and display the results
        columns, rows = read_sql_query(response_sql, "employees.db")
        st.write("#### Query Result:")

        if rows and columns:
            df = pd.DataFrame(rows, columns=columns)
            st.table(df)
            
            # Provide a download button for CSV export
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download results as CSV",
                data=csv,
                file_name='query_results.csv',
                mime='text/csv',
            )
        else:
            st.info("No data was returned for the given query.")
