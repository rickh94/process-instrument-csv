import csv
import sys

from typing import List


def clean(data: List[dict]):
    cleaned_data = [
        {
            "Number": item["number"],
            "Size": item["size"],
            "Location": item["location"],
            "Assigned To": item["assignedTo"],
            "Maintenance Notes": item["maintenanceNotes"],
            "Condition Notes": item["conditionNotes"],
            "Condition": item["condition"],
            "Quality": item["quality"],
            "History": item["history"],
        }
        for item in data
        if item["gifted"] == "true"
    ]
    return cleaned_data


def read_file(filename):
    with open(filename, "r") as fp:
        reader = csv.DictReader(fp)
        data = [item for item in reader]
    return data


def main():
    filename = sys.argv[1]
    data = read_file(filename)
    cleaned_data = clean(data)
    with open(filename, "w") as fp:
        writer = csv.DictWriter(fp, fieldnames=cleaned_data[0])
        writer.writeheader()
        writer.writerows(cleaned_data)


if __name__ == "__main__":
    main()
