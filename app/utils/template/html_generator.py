import os
from pathlib import Path
from datetime import datetime
from app.utils.random_string_generator import generate_sales_order_no, generate_transaction_id

def generate_html(data,alloted, file_name="output.html"):
    if alloted:
        fields_to_include = {
            # "SALES ORDER NO.": data.get("SALES ORDER NO."),
            # "TRANSACTION ID": data.get("TRANSACTION ID"),
            "USER ID": data.get("User id", "VAIBHAV"),  # Default User ID
            "DATE": data.get("Create date"),  # Current Date
            "TIME": data.get("Create Time"),  # Current Time
            "BARRIER GATE": data.get("BARRIER GATE"),
            "SALES TYPE": data.get("SALES TYPE"),
            "RFID EPC": data.get("RFID EPC", ""),
            "VEHICLE NO.": data.get("VEHICLE NO.", ""),
            "VEHICLE TYPE": data.get("VEHICLE TYPE", ""),
            # "PAYMENT MODE": data.get("PAYMENT MODE", ""),  # Correct key access
            # "STATUS": data.get("STATUS", ""),  # Correct key access
            # "TOTAL": str(data.get("TOTAL", ""))  # Correct key access
        }
    else:
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
            html,
            body {
                margin: 0;
                padding: 0;
                height: 100%;
                display: flex;
                justify-content: center;
            }

            body {
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
                height: 480px;
                width: 400px;
                margin-top: 10px;
                text-align: center;
                border: 1px solid black;
            }

            .header {
                height: 60px;
                width: 100%;
                padding-top: 5px;
                border-bottom: 2px solid;
            }

            table {
                width: 100%;
                font-size: small;
            }

            .footer {
                display: flex;
                justify-content: center;
                text-align: left;
                font-size: x-small;
            }

            .footer-container {
                width: 180px;
                padding: 5px;
            }

            .footer-divider {
                border-right: 1.5px dashed;
                margin: 5px;
            }

            .type {
                font-family: 'Courier New', Courier, monospace;
            }

            .star-divider {
                font-size: small;
            }

            .vehicle-reg{
                font-size: base;
            }
        </style>
    </head>

    <body>
        <div class="header">
            STARLABS
            <div class="type">
                SPECIALIZED TEAM FOR<br>
                ALTERNATIVE RESEARCH LABS
            </div>
        </div>
        <div class="star-divider">***************************************************</div>
        """
    if alloted:
        html_content += """
        <div class="vehicle-reg">
            Vehicle registered successfully
        </div>
        """

    html_content += """
        <table>
    """
    for key, value in fields_to_include.items():
        html_content += f"""
            <tr>
                <td style="padding-left: 20px; padding-bottom: 5px; margin-left: 20px; text-align: left;">{key}</td>
                <td>:</td>
                <td style="padding-left: 20px; padding-bottom: 5px; margin-left: 20px; text-align: left;">{value}</td>
            </tr>
        """

    html_content +="""
        </table>

        <div class="star-divider">***************************************************</div>
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