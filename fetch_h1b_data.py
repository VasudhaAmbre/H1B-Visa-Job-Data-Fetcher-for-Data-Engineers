import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_data_from_url(url, table_class='tbl'):
    """
    Fetch data from a given URL and return a list of rows.
    Each row is a list of column values.
    
    Parameters:
    - url (str): The URL from which to fetch data.
    - table_class (str): The class name of the table containing data.
    
    Returns:
    - list: A list of lists, where each inner list represents a row of data.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad response status
        
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'class': table_class})  # Adjust based on specific website
        
        if not table:
            print(f"No table found on {url}")
            return []
        
        rows = table.find_all('tr')[1:]  # Skip the header row
        data = [
            [col.text.strip() for col in row.find_all('td')]
            for row in rows
        ]
        
        print(f"Data extracted from {url}: {len(data)} rows")
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []

def fetch_all_data(base_url, table_class='tbl', max_pages=None):
    """
    Fetch data from all pages starting from the base URL and return a combined list of rows.
    Stop fetching when no more data is found on a page or maximum pages limit reached.
    
    Parameters:
    - base_url (str): The base URL pattern, without the page number.
    - table_class (str): The class name of the table containing data.
    - max_pages (int or None): Maximum number of pages to fetch. None means fetch until no more data is found.
    
    Returns:
    - list: A combined list of fetched data rows.
    """
    all_data = []
    page_num = 1
    previous_data = None
    
    while True:
        url = f"{base_url}-{page_num}/" if page_num > 1 else base_url
        
        data = fetch_data_from_url(url, table_class)
        
        if not data or len(data) == 0:
            print(f"No more data found on {url}. Stopping.")
            break
        
        all_data.extend(data)
        
        if previous_data and data == previous_data:
            print(f"No new data found on {url}. Stopping.")
            break
        
        previous_data = data
        
        if max_pages and page_num >= max_pages:
            print(f"Reached maximum pages limit ({max_pages}). Stopping.")
            break
        
        page_num += 1
    
    return all_data

def save_data_to_excel(data, column_names, filename):
    """
    Save the provided data to an Excel file with the specified filename.
    
    Parameters:
    - data (list): The data to save, where each inner list represents a row of data.
    - column_names (list): A list of column names for the Excel file.
    - filename (str): The filename (including path) to save the Excel file.
    """
    if not data:
        print("No data to save. Exiting.")
        return
    
    # Remove rows where all values are NaN or empty
    df = pd.DataFrame(data, columns=column_names)
    df.dropna(how='all', inplace=True)
    
    # Remove rows where all values are empty strings
    df.replace('', pd.NA, inplace=True)
    df.dropna(how='all', inplace=True)
    
    df.to_excel(filename, index=False)
    print(f"Data has been successfully saved to {filename}")

def main():
    base_url = 'https://www.myvisajobs.com/reports/h1b/job-title/data-engineer'
    table_class = 'tbl'  # Adjust based on the class name of the table
    
    data = fetch_all_data(base_url, table_class)
    
    # Assuming column names are known or fetched dynamically
    column_names = ["Rank", "H1B Visa Sponsor", "Number of LCA", "Average Salary"]
    
    save_data_to_excel(data, column_names, 'data_engineer_h1b_visa_jobs_combined.xlsx')

if __name__ == "__main__":
    main()
