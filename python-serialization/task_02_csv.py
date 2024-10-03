#!/usr/bin/python3
"""Defines a function to convert csv to json."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts a CSV file into JSON format."""
    try:
        with open(csv_filename) as csvf:
            csvReader = csv.DictReader(csvf)
            data = list(csvReader)

        with open('data.json', 'w') as f:
            json.dump(data, f)
        return True

    except FileNotFoundError:
        return False
