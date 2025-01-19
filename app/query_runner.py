from db import run_query

def get_query_result(query):
    """
    Run a sql query and get results.
    
    Args:
        query (str): The SQL query to be executed.

    Example:
        result = get_query_result("SELECT * FROM orders")
    """
    try:
        result = run_query(query)
        return result
    except Exception as e:
        raise Exception(f"Error executing query: {e}")