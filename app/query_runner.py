from app.db import run_query

def get_query_result(query):
    """Run a query and get results."""
    try:
        result = run_query(query)
        return result
    except Exception as e:
        raise Exception(f"Error executing query: {e}")