import os
from pathlib import Path
from datetime import datetime
from app.utils.random_string_generator import generate_sales_order_no, generate_transaction_id

def generate_html(data, file_name="output.html"):
    fields_to_include = {
        "SALES ORDER NO.": data.get("SALES ORDER NO."),
        "TRANSACTION ID": data.get("TRANSACTION ID"),
        "USER ID": data.get("User id", "VAIBHAV"),  # Default User ID
        "DATE": data.get("Create date"),  # Current Date
        "TIME": data.get("Create Time"),  # Current Time
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
        <title>Sales Order Receipt</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
                padding-top: 20px;
                margin: 40px;
                width: 600px;
                text-align: center;
                border: 1px solid black;
            }

            .header {
                width: 100%;
                border-bottom: 2px solid;
            }

            .address {
                font-size: 0.9em;
                color: #555;
            }

            table {
                width: 100%;
            }

            h2 {
                letter-spacing: 12px;
                font-weight: lighter;
            }

            .footer {
                display: flex;
                justify-content: center;
                text-align: left;
            }

            .footer-container {
                width: 200px;
                padding: 40px;
            }

            .footer-divider {
                border-right: 1.5px dashed;
                margin: 20px;
            }
        </style>
    </head>

    <body>
        <div class="header">
            <div style="font-size: xx-large;">*</div>
            <h1>STARLABS TECHNOLOGIES</h1>
            <h2>PRIVATE LIMITED</h2>
            <div class="address">
                <p>NORTHERN COAL FIELDS LIMITED</p>
                <p>BONA PROJECT</p>
                <p>SONBHADRA, UP - 231220</p>
                <p> PH-03261234567</p>
            </div>
        </div>
        <div>**************************************************************</div>

        <table>
        """
    for key, value in fields_to_include.items():
        html_content += f"""
            <tr>
                <td style="padding: 20px; margin-left: 20px; text-align: left;">{key}</td>
                <td>:</td>
                <td style="padding: 20px; margin-left: 20px; text-align: left;">{value}</td>
            </tr>
        """

    html_content +="""
            <tr>
                <td style="padding: 20px; margin-left: 20px; text-align: left;">TRANSACTION ID</td>
                <td>:</td>
                <td style="padding: 20px; margin-left: 20px; text-align: left;">U54656S116DA355Q61A3S8</td>
            </tr>
        </table>

        <div>**************************************************************</div>
        """
    user_id=data.get('User id', 'VAIBHAV')
    html_content+= f"""
        <div class="footer">
            <div class="footer-container">
                FOR STARLABS : <br><br>
                THIS RECEIPT IS GENERATED BY STARLABS BOOM BARRIER SYSTEM
            </div>
            <div class="footer-divider"></div>
            <div class="footer-container">
                FOR NCL BINA PROJECT: <br><br>

                USER ID : {user_id}<br>
                EMP ID : E90264531
            </div>
        </div>

        <div class="divider"></div>

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