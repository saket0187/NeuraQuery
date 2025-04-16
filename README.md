# NeuraQuery

NeuraQuery is an innovative Streamlit application that leverages Google's large language models (LLMs) to translate natural language queries into SQL commands. This enables users with limited SQL knowledge to interact with and retrieve data from an employee database seamlessly. NeuraQuery harnesses the power of NLP to bridge the gap between plain English questions and database querying, simplifying data exploration and analysis.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Overview

NeuraQuery is designed to convert user-friendly natural language questions into SQL queries using Google’s Generative AI models. By integrating state-of-the-art language models and a simple Streamlit interface, NeuraQuery allows users to retrieve relevant employee data quickly, view it in a formatted table, and even download results as CSV files.

---

## Features

- **Natural Language to SQL Conversion:**  
  Leverages Google's LLMs to transform plain English questions into SQL queries.
  
- **Dynamic Query Execution:**  
  Runs the generated SQL queries against an employee database (SQLite) to retrieve accurate data.
  
- **Formatted Results Display:**  
  Presents query results in a well-structured table with proper column headers.
  
- **CSV Download Option:**  
  Includes a download button to export query results as a CSV file for further analysis.
  
- **User-Friendly Interface:**  
  Built with Streamlit, ensuring an accessible and interactive experience for all users.
  
- **Configurable Environment:**  
  Uses environment variables to safely store and load configurations like API keys.

---

## Architecture

NeuraQuery consists of three primary components:

1. **User Interface (UI):**  
   Built with Streamlit, it provides an interactive platform where users can input questions, view generated SQL queries, see query results, and download data.

2. **Generative AI Module:**  
   Powered by Google’s LLMs, this module converts natural language questions into SQL queries using specific models such as `gemini-1.5-flash-8b-exp-0924`.

3. **Database Interaction Layer:**  
   Connects to an SQLite database, executes the generated SQL queries, and retrieves data from the EMPLOYEES table.

---

## Installation

### Prerequisites

- Python 3.7 or higher
- An active Google API key with access to the Generative AI models
- SQLite database with an EMPLOYEES table


