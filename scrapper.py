from bs4 import BeautifulSoup
import json

html_file = "windows_errors.html"  # Replace with your actual HTML file


def extract_errors_from_html(html_file):
    errors = {}

    with open(html_file, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Find all <tbody> elements in the HTML file
    tables = soup.find_all("tbody")

    for table in tables:
        rows = table.find_all("tr")  # Find all rows in the table

        for row in rows:
            columns = row.find_all("td")  # Extract <td> elements

            if len(columns) >= 3:  # Ensure it has enough columns
                error_code = columns[0].text.strip()
                error_message = columns[1].text.strip()
                error_description = columns[2].text.strip()

                errors[error_code] = {
                    "message": error_message,
                    "description": error_description
                }

    return errors


# Extract and save to JSON
error_data = extract_errors_from_html(html_file)

with open("windows_error_codes.json", "w", encoding="utf-8") as json_file:
    json.dump(error_data, json_file, indent=4, ensure_ascii=False)

print(f"Extracted {len(error_data)} error codes successfully!")
