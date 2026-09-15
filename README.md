# day3

Step 1 - Create virtual environment
1. create virtual environment
> python -m venv .venv

2. make sure the .venv folder was created, then activate virtual environment
source .venv/bin/activate

Step 2 - Install Dependencies / Python Librares

1. Create a requirements.txt file
2. Add 
> openai
> streamlit
> python-dotenv 
> chromadb
> pypdf
to requirements.txt file
3. Install dependencies by referring to requirements.txt file by run
> pip install -r requirements.txt

Step 3 - Create a .env file to store out secrets (including (OpenAI API Key))
1. Create a touch .env file
>touch .env
2. Ensure .env file is grayed out (git ignored) - if not, edit .gitignored to include .env
3. Add secrets to .env .OPENAI_API_KEY = ""
4. Password = ""

Step 4 - ADD PAGES FOLDER (to use pages in streamlit)
>mkdir pages

Step 5 - CREATE ENTRYPOINT FILES
1. Create a python file = call1 it whatever you'd like -home.py by convention 
> touch home.py
2. run streamlit, referring to the python file I created
> streamlit run home.py

CREATE CODE IN YOUR PYTHON FILE Import streamlit Import streamlit as st
Import openai from openai import OpenAI
Import python-dotenv from dotenv import load_dotenv

##REMEMBER TO SYNC WITH GITHUB REPOSITORY

Open source control on the left hand side of the screen
Click the plus sign (+)
Add a commit message in the message bar (update)
Click "commit"
Click "sync changes"
IMPORTANT to check github repositories that its already synced