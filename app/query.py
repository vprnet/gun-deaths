#!/usr/bin/python
from sheet import get_google_sheet

def get_entries():
    sheet = get_google_sheet()
    entry_list = []

    for entry in sheet:
        entry['Name'] = entry['Legal Name']
        entry['Sex'] = str.lower(entry['Sex'])
        entry['Date'] = entry['Date of Death']
        entry['Manner'] = str.lower(entry['Manner of Death'])

        if entry['If described, type of firearm']:
            entry['Specified'] = str.lower(entry['If described, type of firearm'])
        else:
            entry['Specified'] = "firearm"

        entry_list.append(entry)

    return entry_list


# PARSE FOR--
# legal name
# date of death
# time of death
# age
# marital status
# education
# us army?
# occupation
# race
# relationship of informant to decedent
# manner of death
# type of firearm


# STILL NEED--
# a way to deal with dates of death where only a month is given?
# a better way to deal with entries where the firearm isn't specified
