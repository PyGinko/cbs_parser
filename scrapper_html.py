import requests
from bs4 import BeautifulSoup
import json

url = "https://learn.microsoft.com/en-us/troubleshoot/windows-client/setup-upgrade-and-drivers/windows-10-upgrade-resolution-procedures?context=%2Fwindows%2Fdeployment%2Fcontext%2Fcontext"  # Replace with the actual URL

def extract_errors_from_url(url):
    errors = {}

    # Fetch the webpage content
    response = requests.get(url)
    response.raise_for_status()  # Raise an error if request fails

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all <tbody> elements in the webpage
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
                    "description": error_description,
                    "mitigation": ""
                }

    return errors

# Extract and save to JSON
error_data = extract_errors_from_url(url)

with open("windows_error_codes.json", "w", encoding="utf-8") as json_file:
    json.dump(error_data, json_file, indent=4, ensure_ascii=False)

print(f"Extracted {len(error_data)} error codes successfully!")
