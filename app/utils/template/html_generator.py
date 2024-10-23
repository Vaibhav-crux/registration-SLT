import os
from pathlib import Path
from datetime import datetime
from app.utils.random_string_generator import generate_sales_order_no, generate_transaction_id

def generate_html(data, file_name="output.html"):
    fields_to_include = {
        "SALES ORDER NO.": data.get("SALES ORDER NO."),
        "TRANSACTION ID": data.get("TRANSACTION ID"),
        "User id": data.get("User id", "VAIBHAV"),  # Default User ID
        "Create date": data.get("Create date"),  # Current Date
        "Create Time": data.get("Create Time"),  # Current Time
        "BARRIER GATE": data.get("BARRIER GATE"),
        "SALES TYPE": data.get("SALES TYPE"),
        "RFID EPC": data.get("RFID EPC", ""),
        "VEHICLE NO.": data.get("VEHICLE NO.", ""),
        "VEHICLE TYPE": data.get("VEHICLE TYPE", ""),
        "PAYMENT MODE": data.get("PAYMENT MODE", ""),  # Correct key access
        "STATUS": data.get("STATUS", ""),  # Correct key access
        "TOTAL": str(data.get("TOTAL", ""))  # Correct key access
    }

    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>RFID Details</title>
        <style>
            body { font-family: Arial, sans-serif; }
            table { border-collapse: collapse; width: 100%; }
            th, td { border: 1px solid black; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h1>RFID Details</h1>
        <table>
            <tr>
                <th>Field</th>
                <th>Value</th>
            </tr>
    """

    for key, value in fields_to_include.items():
        html_content += f"""
            <tr>
                <td>{key}</td>
                <td>{value}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    output_dir = Path(__file__).resolve().parent.parent.parent / 'static' / 'html'
    os.makedirs(output_dir, exist_ok=True)

    output_file_path = output_dir / file_name
    with open(output_file_path, 'w') as file:
        file.write(html_content)

    print(f"HTML file generated at: {output_file_path}")
    return output_file_path
