# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:36:25 2024

@author: spark
"""
'''
bunch of text files. Within these text files, there is a date. 
I want my code to check the text files and the date inside them, and create a new folder and only include the text files within a June-Aug 2024. The date in the txt file is in this format 14-May-2024 

The date appears AFTER this part in every text-file (including the spaces and tabs.:  
Corrected Transcript 
 
 
1-877-FACTSET   www.callstreet.com 
Total Pages: 10 
Copyright © 2001-2024 FactSet CallStreet, LLC
'''

import os
import re
from datetime import datetime
import shutil

def extract_date(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Look for the date after the specified text
        match = re.search(r'Copyright © 2001-2024 FactSet CallStreet, LLC\s+(\d{2}-[A-Za-z]{3}-\d{4})', content)
        if match:
            return match.group(1)
    return None

def is_date_in_range(date_str):
    date = datetime.strptime(date_str, '%d-%b-%Y')
    start_date = datetime(2024, 6, 1)
    end_date = datetime(2024, 8, 31)
    return start_date <= date <= end_date

def process_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(source_folder, filename)
            date_str = extract_date(file_path)
            if date_str and is_date_in_range(date_str):
                shutil.copy2(file_path, destination_folder)
                print(f"Copied {filename} to {destination_folder}")


# Usage
source_folder = r'C:\Users\spark\OneDrive\Desktop\QMSS Classes\Sem 1\NLP\final proj\texts'
destination_folder = r'C:\Users\spark\OneDrive\Desktop\QMSS Classes\Sem 1\NLP\final proj\June-Aug-2024'

process_files(source_folder, destination_folder)




#Now, I only want 10 random companies. Each transcript has a number in the brackets representing a company.
#filter for any 10 numbers
import os
import re
import shutil

def extract_company_number(filename):
    match = re.search(r'Transcripts And Slides \((\d+)\)', filename)
    if match:
        return int(match.group(1))
    return None

def filter_companies(source_folder, destination_folder, company_numbers):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        if filename.endswith('.txt'):
            company_number = extract_company_number(filename)
            if company_number in company_numbers:
                source_path = os.path.join(source_folder, filename)
                dest_path = os.path.join(destination_folder, filename)
                shutil.copy2(source_path, dest_path)
                print(f"Copied {filename} to {destination_folder}")

# Usage
source_folder = r'C:\Users\spark\OneDrive\Desktop\QMSS Classes\Sem 1\NLP\final proj\June-Aug-2024'
destination_folder =  r'C:\Users\spark\OneDrive\Desktop\QMSS Classes\Sem 1\NLP\final proj\filtered_companies_10'

# List of company numbers you want to filter
company_numbers = ['21', '44', '45', '51', '53', '59', '61', '66', '71', '73']  

filter_companies(source_folder, destination_folder, company_numbers)


