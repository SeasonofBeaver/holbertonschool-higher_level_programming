#!/usr/bin/python3
import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        raise TypeError(f"Invalid input: template should be a string, \
                        got {type(template).__name__}")

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict)
                                                  for attendee in attendees):
        raise TypeError(f"Invalid input: attendees should be a list of \
                        dictionaries, got {type(attendees).__name__}")

    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        try:
            message = template

            for key in ["name", "event_title", "event_date", "event_location"]:
                value = attendee.get(key, "N/A")
                message = message.replace(f'{{{key}}}', value
                                          if value is not None else "N/A")

            output_filename = f"output_{index}.txt"

            if os.path.exists(output_filename):
                print(f"File {output_filename} already exists. \
                      Skipping write.")
                continue

            with open(output_filename, "w") as output_file:
                output_file.write(message)

            print(f"File {output_filename} generated successfully.")

        except Exception as e:
            print(f"An error occurred while generating the invitation \
                  for {attendee.get('name', 'N/A')}: {e}")
