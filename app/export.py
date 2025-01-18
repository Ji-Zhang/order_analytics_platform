import csv

def export_to_csv(colnames, query_result, output_file='output.csv'):
    """Export query result to a CSV file."""
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([col[0] for col in colnames])  # write header
        writer.writerows(query_result)  # write rows of data
    print(f"Results exported to {output_file}")