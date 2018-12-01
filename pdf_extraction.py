'''
    File name: pdf_extraction.py
    Authors: David Peletz and Jack Freier
    Date created: 12/01/2018
    Date last modified: 12/01/2018
    Python Version: 3.5
'''

import PyPDF2
import pandas as pd
import re
import spacy
from nltk import sent_tokenize

nlp = spacy.load('en')

pdf_file_reader = PyPDF2.PdfFileReader

file_path = "/Users/davidmpeletz/Documents/Github/Comprehensyllabi/sample_syllabus.pdf"

pdf_input = pdf_file_reader(file_path)

def get_all_content(input_pdf):
    if input_pdf.getNumPages() > 0:

        pdf_as_string = ""

        for i in range(input_pdf.getNumPages()):
            lines = sent_tokenize(input_pdf.getPage(i).extractText())
            pdf_as_string += "".join(lines)

        return pdf_as_string

    else:
        raise Exception("The syllabus PDF must contain at least 1 page.")

def contains_office_hours(line):
    doc = nlp(line)

    for token in doc:

        if token.pos_ == 'NUM' and ':' in line:
            if 'MWF' in line:
                return 1

def contains_grading_info(line):
    line = str(line).lower()
    doc = nlp(line)

    for ent in doc.ents:
        if (ent.label_ == 'PERCENT'):
            return 1

    return 0

def contains_email(line):
    line = str(line).lower()
    email_match = re.findall(r'[\w\.-]+@[\w\.-]+', line)

    if len(email_match) > 0:
        return 1

    return 0

def contains_useful_info(line):
    useful_info = ["quiz", "test", "exam", "final", "assessment", "due",
                   "office hours", "room", "homework", "problem set", "essay",
                   "paper", "reflection", "analysis", "project", "presentation",
                   "percent", "%", "evaluation", "assessment", "grading",
                   "grade", "policy", "report", "debate"]

    line = str(line).lower()

    for i in useful_info:
        if i in line:
            return 1

    return 0

def contains_important_date(line):
    line = str(line).lower()
    doc = nlp(line)

    for ent in doc.ents:

        if ('DATE' in ent.label_ or
            'CARDINAL' in ent.label_ or
            'TIME' in ent.label_):
            return 1

    return 0

def get_grading_policy(input_df):
    grading_df = input_df.loc[input_df['has_grading_info'] == 1]

    first = grading_df.head(1).index[0]
    last = grading_df.tail(1).index[0]

    num_categories = len(grading_df)
    percentages = []
    assignments = []

    section_string = ""
    for i in range(first, last + 2):
        section_string += input_df['line'][i]

    percentage_list = section_string.split('%', num_categories)

    for j in range(num_categories):
        percent_value = percentage_list[j][-2:] + "%"

        if j != num_categories - 1:
            description = percentage_list[j + 1][:-3]

        else:
            description = percentage_list[j + 1]

        percentages.append(percent_value)
        assignments.append(description)

    return [assignments, percentages]

def get_email(input_df):

    email_df = input_df.loc[input_df['has_email'] == 1]
    first = (email_df.head(1).index[0])

    for i in (email_df['line'][first].split()):

        email_match = re.findall(r'[\w\.-]+@[\w\.-]+', i)

        if len(email_match) > 0:
            return email_match[0]

def get_office_hours(input_df):
    office_hour_df = input_df.loc[input_df['has_office_hours'] == 1]
    index = office_hour_df.head(1).index[0]
    office_hour_df['has_office_hours'][index + 1] = 1
    string = ""

    for j in range(index, index + 2):
        string += input_df['line'][j]

    split_string = string.split(', ')[1]

    return split_string

def format_return_df(input_df) :
    office_hours = get_office_hours(input_df)
    email = get_email(input_df)
    return_df = pd.DataFrame(columns=('Assignment', 'Percentage', 'Email', 'Office Hours'))
    return_df['Assignment'] = get_grading_policy(input_df)[0]
    return_df['Percentage'] = get_grading_policy(input_df)[1]
    return_df['Office Hours'][0] = office_hours
    return_df['Email'][0] = email
    return_df.reset_index()
    return return_df.to_csv('syllabus_summary.csv', index=False)

def get_useful_information(input_pdf):

    return_df = pd.DataFrame()
    return_df['line'] = get_all_content(input_pdf).split('\n')
    return_df['has_useful_info'] = return_df['line'].apply(contains_useful_info)
    return_df['has_email'] = return_df['line'].apply(contains_email)
    return_df['has_grading_info'] = return_df['line'].apply(contains_grading_info)
    return_df['has_date'] = return_df['line'].apply(contains_important_date)
    return_df['has_office_hours'] = return_df['line'].apply(contains_office_hours)

    return format_return_df(return_df)

get_useful_information(pdf_input)