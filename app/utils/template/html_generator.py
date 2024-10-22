import os
from pathlib import Path

def generate_html(data, file_name="output.html"):
    """
    Generate an HTML file from the provided data.

    :param data: Dictionary containing the data to be included in the HTML.
    :param file_name: Name of the HTML file to create.
    """
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

    for key, value in data.items():
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

    # Make sure the directory exists
    output_dir = Path(__file__).resolve().parent.parent.parent / 'static' / 'html'
    os.makedirs(output_dir, exist_ok=True)

    output_file_path = output_dir / file_name
    with open(output_file_path, 'w') as file:
        file.write(html_content)

    print(f"HTML file generated at: {output_file_path}")
