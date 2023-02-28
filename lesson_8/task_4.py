import json
import csv

with open("taks3.json", "r") as file_json, open("task4.csv", "w") as file_csv:
    file_j = json.load(file_json)
    csv_wr = csv.DictWriter(file_csv, delimiter="-",
                            fieldnames=["id", "name", "age", "phone"])
    csv_wr.writeheader()
    for k, v in file_j.items():
        csv_wr.writerow({
            'id': k,
            'name': v[0],
            'age': v[1],
            "phone": input("enter phone number: ")
        })
