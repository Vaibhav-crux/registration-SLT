import random
import string
from datetime import datetime
import pytz

def generate_sales_order_no():
    """Generates a unique sales order number based on the current date and a random 4-digit number."""
    timezone = pytz.timezone("Asia/Kolkata")
    date_part = datetime.now(timezone).strftime("%Y-%m-%d")
    random_number = ''.join(random.choices(string.digits, k=4))
    return f"STARLABS-{date_part}-PROJECT-{random_number}"

def generate_transaction_id(vehicle_no):
    """Generates a unique transaction ID based on the vehicle number and a random 8-digit string."""
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return f"{vehicle_no}{random_string}"
