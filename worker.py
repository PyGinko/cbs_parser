import json

with open("errors_temp.json", "r", encoding="utf-8") as file:
    error_data = json.load(file)

for error_code, details in error_data.items():
    details["mitigation"] = details["description"]
    details["description"] = details["message"]
    details["message"] = ""

with open("updated_erros_temp.json", "w", encoding="utf-8") as file:
    json.dump(error_data, file, indent=4, ensure_ascii=False)

print("ok")
