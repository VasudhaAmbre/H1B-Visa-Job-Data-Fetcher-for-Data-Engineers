# H1B-Visa-Job-Data-Fetcher-for-Data-Engineers
This Python script is designed to fetch H1B visa job data specific to data engineers from the MyVisaJobs website using web scraping techniques. The fetched data is then organized and saved into an Excel file, making it convenient for analysis and reference.

# H1B Visa Job Data Fetcher for Data Engineers

This Python script fetches H1B visa job data for data engineers from the MyVisaJobs website and saves it into an Excel file. It is designed to be used in a Jupyter Notebook environment.

## Features

- Fetches data from multiple pages of the website using web scraping techniques.
- Saves the fetched data into an Excel file, separating text content and hyperlinks.

## Requirements

- Python 3.x
- Jupyter Notebook
- Required Python packages (requests, BeautifulSoup, pandas)

## Installation

1. Clone the repository:
git clone https://github.com/your-username/h1b-visa-job-data-engineer.git

2. Navigate to the repository directory:
cd H1B-Visa-Job-Data-Fetcher-for-Data-Engineers

3. Install required packages:
pip install <package_name>


## Usage

1. Open Jupyter Notebook:

2. Open the `fetch_h1b_data.ipynb` notebook in Jupyter.

3. Run the cells in the notebook to execute the script.

4. Check the generated Excel file (`data_engineer_h1b_visa_jobs_combined.xlsx`) in the notebook's directory for the fetched data.

## Script Explanation

### 1. `fetch_data_from_url(url, table_class='tbl')`
- Function to fetch data from a given URL.
- Parameters:
  - `url`: The URL from which to fetch data.
  - `table_class`: The class name of the table containing data (default is `'tbl'`).
- Returns:
  - A list of lists, where each inner list represents a row of data.

### 2. `fetch_all_data(base_url, table_class='tbl', max_pages=None)`
- Function to fetch data from all pages starting from the base URL.
- Parameters:
  - `base_url`: The base URL pattern, without the page number.
  - `table_class`: The class name of the table containing data (default is `'tbl'`).
  - `max_pages`: Maximum number of pages to fetch (default is `None`).
- Returns:
  - A combined list of fetched data rows.

### 3. `save_data_to_excel(data, column_names, filename)`
- Function to save the provided data to an Excel file.
- Parameters:
  - `data`: The data to save, where each inner list represents a row of data.
  - `column_names`: A list of column names for the Excel file.
  - `filename`: The filename (including path) to save the Excel file.

### 4. Example Usage in Jupyter Notebook
- Initialize the base URL and table class.
- Fetch data using `fetch_all_data`.
- Specify column names.
- Save data to Excel using `save_data_to_excel`.




