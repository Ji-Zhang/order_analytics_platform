import csv

def export_to_csv(colnames, query_result, output_file):
    """
    Export query result to a CSV file.
    
    Args:
        colnames (list): List of column names as tuples.
        query_result (list of tuples): Query result rows to write to the CSV file.
        output_file (str): Path to the output CSV file.
    """
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([col[0] for col in colnames])  # write header
        writer.writerows(query_result)  # write rows of data
    print(f"Results exported to {output_file}")