AI Agent Dashboard - Google Sheets
This project develops a dashboard application that reads in a CSV upload file or connects to a Google Sheet, does a query from a template, web search, and uses LLMs to extricate interesting information. It could save this information back into the Google Sheet or export it as a CSV.

**Project Overview**
The application makes use of these technologies

Streamlit: Used to create the web interface.
Google Sheets API: Used to interact and connect with the Google Sheets.
Transformers (Hugging Face): Employed in querying and extracting information by making use of pre-trained language models.
Pandas: Used for data manipulation and analysis.
GSpread: Used to connect with, read, and write from Google Sheets from Python.
Features
CSV Upload: Users can upload a CSV file, which is then made available for further interaction.
Google Sheets Import: The user can add a link to a Google Sheet and import data from it.
Dynamic Query Generation: It will dynamically generate queries based on a prompt template provided by the user with placeholders for data
Web Search Simulation: Users can simulate web searches over every entity in the dataset and analyze results they receive.
LLData Extractor: Fetch emails, and other useful data from web search results using large language models.
Export Data: The fetched data can be exported in CSV format or the result can be inserted directly into the Google Sheet.
Requirements
You'll need the following before running the project.
Python (>= 3.7)
Streamlit
Pandas
GSpread
Transformers (Hugging Face)
Install Dependencies
Use the following command to install the needed Python libraries.
pip install streamlit pandas gspread google-auth transformers
Google Sheets API Settings
Go to the Google Developers Console.
Create a new project, enable Google Sheets API and Google Drive API
Create service account credentials and download credentials.json
Put your credentials.json in the same directory as your python script
How To Run the Project Locally
Clone the Repository: Clone the repository into your local machine if you haven't already:
git clone <repository_url>
Enter Project Directory: Use the terminal or Anaconda prompt to go into your project folder directory
cd <project_directory>
Run Streamlit App locally :Below command runs Streamlit app in local run mode:
streamlit run filename.py
Interact with Dashboard: Once the app launches, open up a web browser and access the dashboard via http://localhost:8501. You can:
Upload a CSV file or insert a Google Sheets URL.
Choose one column, make dynamic SQL queries
Perform web search for above and print/extract information
Download as CSV or else update Google Sheet with result.
File Structure
project-directory/
│
├── credentials.json           # Google API credentials
├── filename.py                # Main Python script for the dashboard
└── requirements.txt           # Dependencies list
└── README.md                  # Project documentation
Notes
Assure that credentials.json is located in the same directory as your python script to enable google sheet functionality.
Web search is a simulated feature and doesn't really does web search
License
This project is licensed under the MIT License.

Loom Video: https://www.loom.com/share/a9b8c32bf2d14d0f8f614c837b4174e4?sid=7a1eb736-19c4-46be-a149-b8b93de5a093 
