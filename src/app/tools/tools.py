from langchain_core.tools import tool


@tool
def get_customer(customer_id: str) -> str:
    """Get customer information."""
    return "Customer information"
