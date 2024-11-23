# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 20:14:36 2024

@author: spark
"""

import os
import re
import pandas as pd
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def extract_file_number(filename):
    match = re.search(r'Transcripts And Slides \((\d+)\)', filename)
    return match.group(1) if match else None

def process_files(input_folder):
    all_sentences = []
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_folder, filename)
            file_number = extract_file_number(filename)
            
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                sentences = sent_tokenize(content)
                
                for sentence in sentences:
                    all_sentences.append({
                        'sentence': sentence.strip(),
                        'file_number': file_number,
                        'file_name': filename
                    })
    
    return pd.DataFrame(all_sentences)

# Usage
input_folder = r'C:\Users\spark\OneDrive\Desktop\QMSS Classes\Sem 1\NLP\final proj\final_cleaned_transcripts'
df = process_files(input_folder)

# Display the first few rows of the DataFrame
print(df.head())

# Save the DataFrame to a CSV file (optional)
df.to_csv('sentences_output.csv', index=False)