**AI Agent Dashboard - Google Sheets Integration**
This is a project creating a dashboard application with the ability to upload a CSV file or connect to a Google Sheet, querying data using a template, and doing web searches and extracting the information back through large language models (LLMs). The extracted information can be saved back to the Google Sheet or downloaded as a CSV file.
Project Description
This application utilizes the following technologies:
**Streamlit**: Constructing the web-based user interface.
**Google Sheets API**: Connect and interact with Google Sheets.
Transformers (Hugging Face): To query and retrieve using pre-trained language models.
Pandas: Data manipulation and analysis.
GSpread: Connect and use Google Sheets in Python.
Features
**CSV Upload**: Users upload a CSV file, then it is made available for interaction.h
Google Sheets Integration: one can input a link to a Google Sheet and import the information contained in it.
Dynamic Query Generation: for a user-specified template of the prompt with placeholders for data, queries are dynamically generated.
Web Search Simulation: one can perform a web search for each entity in the dataset and show results.
LLM Information Extraction : Retrieves email addresses and other relevant information extracted from web search results using large language models.
Data export functionality to export extracted data in CSV format or to replace Google Sheet with results
Requirements
Before running the project, you will need: 
Python (>= 3.7)
Streamlit
Pandas
GSpread
Transformers (Hugging Face)
Installation of dependencies
You can install the required Python libraries using the following command: 

pip install streamlit pandas gspread google-auth transformers
Google Sheets API Configuration
Go to the Google Developers Console .
Create a new project and enable the Google Sheets API and Google Drive API.
Create service account credentials and download the credentials.json file.
 Put the credentials.json file in the same directory as your python script.
How To Run the Project Locally
Clone the Repository: Clone the repository into your local machine if you haven't already.
git clone <repository_url>
Navigate to the Project Directory: Open your terminal or Anaconda prompt and navigate to the project folder.
cd <project_directory>
Run the Streamlit App: Run the following command to start the Streamlit app on your local machine:
streamlit run filename.py
Interact with the Dashboard: Once the app is running, open your browser and navigate to http://localhost:8501 to use the dashboard. You can:

Upload a CSV file or provide a Google Sheets URL.
Select a column and then do dynamic queries.
Do some web searches, extracting the information
Download the results as a CSV file or update the Google Sheet
File Structure
project-directory/
│
├── credentials.json           # Google API credentials
├── filename.py                # Main Python script for the dashboard
└── requirements.txt             # list of dependencie
├── README.md                    # Project documentation
Notes: 
credentials.json should be in the same directory as the python script of this integration Google Sheets to actually work.
The web search feature is simulated, not an actual web search.
Licence
This project is licensed under the MIT License.

Loom Video link : https://www.loom.com/share/a9b8c32bf2d14d0f8f614c837b4174e4?sid=a8e15dad-705a-443b-a795-313dee1fbb7c
