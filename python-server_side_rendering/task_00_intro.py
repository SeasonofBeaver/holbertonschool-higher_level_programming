#!/usr/bin/python3
import re
import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        raise TypeError(f"Invalid input: template should be \
                        a string, got {type(template).__name__}")
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict)
                                                  for attendee in attendees):
        raise TypeError(f"Invalid input: attendees should be \
                        a list, got {type(attendees).__name__}")
    if not template.strip():
        raise ValueError("Template is empty, no output files generated.")
    if not attendees:
        raise ValueError("No data provided, no output files generated.")

    for index, attendee in enumerate(attendees, start=1):
        message = template
        
        for key, value in attendee.items():
            if value is None:
                value = "N/A"
            message = message.replace(f'{{{key}}}', str(value))

        message = re.sub(r'{[^{}]+}', "N/A", message)

        output_filename = f"output_{index}.txt"
        if os.path.exists(output_filename):
            print(f"File {output_filename} already exists. Skipping write.")
            continue

        with open(output_filename, "w") as output_file:
            output_file.write(message)
