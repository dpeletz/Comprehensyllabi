'''
    File name: pdf_extraction.py
    Authors: David Peletz and Jack Freier
    Date created: 12/01/2018
    Date last modified: 12/01/2018
    Python Version: 3.5
'''

import PyPDF2
import csv
import pandas as pd
import re
import spacy
from nltk import sent_tokenize
from nltk.corpus import stopwords

nlp = spacy.load('en')

pdf_file_reader = PyPDF2.PdfFileReader

file_path = "/Users/davidmpeletz/Desktop/islam.pdf"

input1 = pdf_file_reader(file_path)

def get_all_content(input_pdf):
    if input_pdf.getNumPages() > 0:

        text_content = []
        str_content = ""
        stop_words = set(stopwords.words('english'))

        for i in range(input_pdf.getNumPages()):
            sentences = sent_tokenize(input_pdf.getPage(i).extractText())
            str_content += "".join(sentences)
            line_list = input_pdf.getPage(i).extractText().split('\n')
            words = re.split(r'\W+', input_pdf.getPage(i).extractText())
            new_str_content = [w for w in words if not w in stop_words]
            text_content.extend(words)
            doc = nlp(str_content)
        #             print(str_content)

        return str_content

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

    f_index = grading_df.head(1).index[0]
    l_index = grading_df.tail(1).index[0]

    num_categories = len(grading_df)
    percentages = []
    descriptions = []

    string = ""
    for i in range(f_index, l_index + 2):
        string += line_df['line'][i]

    values = string.split('%', num_categories)

    for j in range(num_categories):
        percent_value = values[j][-2:] + "%"
        if j != num_categories - 1:
            description = values[j + 1][:-3]
        else:
            description = values[j + 1]

        percentages.append(percent_value)
        descriptions.append(description)

        # return_df = pd.DataFrame()
        # return_df['Percentage'] = percentages
        # return_df['Assignment'] = descriptions

    return [descriptions, percentages]


def get_email(input_df):
    email_frame = input_df.loc[input_df['has_email'] == 1]
    index = (email_frame.head(1).index[0])

    for i in (email_frame['line'][index].split()):
        email_match = re.findall(r'[\w\.-]+@[\w\.-]+', i)
        if len(email_match) > 0:
            return email_match[0]


return_bow = get_all_content(input1)

line_df = pd.DataFrame()
line_df['line'] = return_bow.split('\n')

line_df['has_useful_info'] = line_df['line'].apply(contains_useful_info)
line_df['has_email'] = line_df['line'].apply(contains_email)
line_df['has_grading_info'] = line_df['line'].apply(contains_grading_info)
line_df['has_date'] = line_df['line'].apply(contains_important_date)
line_df['has_office_hours'] = line_df['line'].apply(contains_office_hours)


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
    return return_df.to_csv('Summary')


print(format_return_df(line_df))

