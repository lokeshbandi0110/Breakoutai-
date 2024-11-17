import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from transformers import pipeline
import time

# Function to read data from the specified Google Sheet URL
def read_google_sheet(sheet_url, credentials):
    try:
        gc = gspread.authorize(credentials)
        sheet = gc.open_by_url(sheet_url)
        worksheet = sheet.get_worksheet(0)  # Access the first worksheet
        data = worksheet.get_all_records()
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        st.error(f"Error accessing the Google Sheet: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error

# Function to update Google Sheet with extracted information
def update_google_sheet(sheet_url, credentials, data):
    try:
        gc = gspread.authorize(credentials)
        sheet = gc.open_by_url(sheet_url)
        worksheet = sheet.get_worksheet(0)  # Access the first worksheet

        # Convert DataFrame to a list of lists
        data_list = [data.columns.tolist()] + data.values.tolist()
        worksheet.clear()  # Clear the existing content
        worksheet.update(data_list)  # Update the sheet with new data

        st.success("Google Sheet updated successfully!")
    except Exception as e:
        st.error(f"Error updating the Google Sheet: {e}")

# Main App Function
def main():
    st.title("AI Agent Dashboard")
    st.subheader("Upload CSV or Enter Google Sheet Link")

    # Upload CSV File
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    # Input for Google Sheet Link
    sheet_url = st.text_input("Enter Google Sheet URL (Leave empty if using CSV upload)", "")
    
    # Use credentials.json for Google Sheets API
    credentials_file = 'credentials.json'
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/drive.file"
    ]
    credentials = Credentials.from_service_account_file(credentials_file, scopes=scope)

    # Initialize an empty DataFrame
    data = pd.DataFrame()

    # Handling CSV File Upload
    if uploaded_file:
        try:
            data = pd.read_csv(uploaded_file, on_bad_lines='skip')
            st.success("CSV file successfully uploaded!")
            st.write("Preview of the uploaded CSV file:")
            st.dataframe(data.head())
        except Exception as e:
            st.error(f"Error reading the CSV file: {e}")

    elif sheet_url:
        try:
            data = read_google_sheet(sheet_url, credentials)
            if not data.empty:
                st.success("Google Sheet successfully connected!")
                st.write("Preview of the connected Google Sheet:")
                st.dataframe(data.head())
            else:
                st.warning("No data found in the Google Sheet.")
        except Exception as e:
            st.error(f"Error accessing the Google Sheet: {e}")

    # Display Column Selection if Data is Loaded
    if not data.empty:
        columns = data.columns.tolist()
        selected_column = st.selectbox("Select the Main Column (e.g., company names)", columns)
        st.write("Preview of the Selected Column Data:")
        st.dataframe(data[[selected_column]].head())

        # Define Query Template
        st.subheader("Define Your Query Prompt Template")
        prompt_template = st.text_input(
            "Enter your prompt template using {entity} as a placeholder",
            value="Get me the email address of {entity}"
        )

        # Generate Preview of Queries
        if prompt_template:
            st.write("Preview of Generated Queries:")
            preview_data = data[selected_column].head(5)
            generated_queries = [prompt_template.replace("{entity}", str(entity)) for entity in preview_data]
            for query in generated_queries:
                st.write(f"🔍 {query}")

        # Option to Download the Selected Data
        csv = data.to_csv(index=False)
        st.download_button("Download CSV", csv, "selected_data.csv", "text/csv")

        # Perform Web Search Button
        if st.button("Perform Web Search"):
            st.write("Performing web searches... This may take a while.")
            search_results = []
            for entity in data[selected_column]:
                search_query = prompt_template.replace("{entity}", str(entity))
                
                # Simulate web search results
                search_results.append({
                    "entity": entity,
                    "results": [f"Result for {search_query} - URL", "Snippet info from search"]
                })
                
            # Save results to session state and display table
            st.session_state.search_results = search_results
            result_df = pd.DataFrame(search_results)
            st.dataframe(result_df)
            st.success("Web search completed.")

        # Extract Information Using LLM
        if 'search_results' in st.session_state:
            if st.button("Extract Information Using LLM"):
                st.write("Processing search results with LLM... This may take a while.")
                with st.spinner('Extracting information...'):
                    # Initialize language models
                    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
                    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

                    extraction_results = []
                    batch_size = 3  # Process 3 results at a time to reduce time

                    # Process results in smaller batches to speed up
                    for i in range(0, len(st.session_state.search_results), batch_size):
                        batch = st.session_state.search_results[i:i+batch_size]
                        batch_results = []

                        for result in batch:
                            entity = result['entity']
                            combined_results = " ".join(result['results'])

                            try:
                                # Classify and Summarize
                                candidate_labels = ["email address", "contact information", "email"]
                                classification = classifier(combined_results, candidate_labels)
                                if classification['labels'][0] == "email address":
                                    output = summarizer(combined_results, max_length=150, min_length=10)
                                    extracted_info = output[0]['summary_text']
                                else:
                                    extracted_info = "No email address found."
                            except Exception as e:
                                extracted_info = f"Error: {e}"

                            batch_results.append({
                                "entity": entity,
                                "extracted_info": extracted_info
                            })

                        extraction_results.extend(batch_results)  # Combine results from each batch

                    result_df = pd.DataFrame(extraction_results)
                    st.success('Extraction completed!')
                    st.dataframe(result_df)

                    # Download CSV Button
                    extracted_csv = result_df.to_csv(index=False)
                    st.download_button("Download Extracted Data as CSV", extracted_csv, "extracted_data.csv", "text/csv")

                    # Update Google Sheet Option
                    if st.button("Update Google Sheet with Extracted Information"):
                        # Update Google Sheet
                        update_google_sheet(sheet_url, credentials, result_df)

                        # Now update the CSV file
                        csv_with_extracted_info = result_df.to_csv(index=False)
                        st.download_button("Download Updated CSV", csv_with_extracted_info, "updated_data.csv", "text/csv")

if __name__ == "__main__":
    main()
