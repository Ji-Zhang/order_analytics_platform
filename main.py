import argparse
import sys
import os
from app.query_runner import get_query_result

def read_query_from_file(file_path):
    """Reads the SQL query from a file."""
    if not os.path.isfile(file_path):
        print(f"Error: The file {file_path} does not exist.")
        sys.exit(1)
    
    with open(file_path, 'r') as file:
        query = file.read().strip()
    
    return query

def main():
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description="SQL Query Runner CLI")
    
    # Add the query argument
    parser.add_argument('query', help="SQL query to run or path to SQL script file")
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Check if the query is a file path or a direct SQL query
    query = args.query
    if os.path.isfile(query):  # If the input is a file, read the query from the file
        print(f"Reading SQL query from file: {query}")
        query = read_query_from_file(query)
    else:
        print(f"Using provided SQL query: {query}")

    # Run the query
    print(f"Running query: {query}")
    try:
        query_result = get_query_result(query)
        if query_result:
            print(f"Query executed successfully.")
        else:
            print("No data returned.")
    except Exception as e:
        print(f"Error while running query: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()