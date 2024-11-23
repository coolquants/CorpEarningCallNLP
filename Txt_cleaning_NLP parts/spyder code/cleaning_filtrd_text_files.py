# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:53:03 2024

@author: spark
"""

import os
import re
import os
import re

def extract_transcript(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Find the start of the relevant content
    start_marker = "MANAGEMENT DISCUSSION SECTION" 
    start_index = content.find(start_marker)
    
    if start_index == -1:
        return None  # Relevant content not found
    
    # Extract content from the start marker to the end of the file
    relevant_content = content[start_index:]
    
    # Remove speaker labels and question/answer markers
    cleaned_content = re.sub(r'^.*Analyst, .*\n', '', relevant_content, flags=re.MULTILINE)
    cleaned_content = re.sub(r'^.*[A-Z][a-z]+ [A-Z][a-z]+.*\n', '', cleaned_content, flags=re.MULTILINE)
    cleaned_content = re.sub(r'^Q\s*', '', cleaned_content, flags=re.MULTILINE)
    cleaned_content = re.sub(r'^A\s*', '', cleaned_content, flags=re.MULTILINE)
    cleaned_content = re.sub(r'^\s*\d+\s*$\n', '', cleaned_content, flags=re.MULTILINE) #removing the numbers that keep appearing in a whole line 
    
    # Remove repeated periods and other unwanted elements
    cleaned_content = re.sub(r'\.{3,}', '', cleaned_content)
    cleaned_content = re.sub(r'1-877-FACTSET\s+www\.callstreet\.com.*\n', '', cleaned_content)
    cleaned_content = re.sub(r'Copyright © 2001-2024 FactSet CallStreet, LLC.*\n', '', cleaned_content)
    cleaned_content = re.sub(r'MANAGEMENT DISCUSSION SECTION ', '', cleaned_content)
    cleaned_content = re.sub(r'UESTION AND ANSWER SECTION ', '', cleaned_content)
    cleaned_content = re.sub(r'\d{2}-[A-Za-z]{3}-\d{4}', '', cleaned_content) #Removing dates
    
    # Remove any remaining empty lines
    cleaned_content = re.sub(r'\n+', '\n', cleaned_content).strip()
    # Remove the disclaimer section if present
    disclaimer_start = cleaned_content.rfind("Disclaimer")
    if disclaimer_start != -1:
        cleaned_content = cleaned_content[:disclaimer_start].strip()
    
    
    return cleaned_content

def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"cleaned_{filename}")
            
            transcript = extract_transcript(input_path)
            if transcript:
                with open(output_path, 'w', encoding='utf-8') as file:
                    file.write(transcript)
                print(f"Processed: {filename}")
            else:
                print(f"Skipped: {filename} (No relevant content found)")
    
  

def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            transcript = extract_transcript(input_path)
            if transcript:
                with open(output_path, 'w', encoding='utf-8') as file:
                    file.write(transcript)
                print(f"Processed: {filename}")
            else:
                print(f"Skipped: {filename} (No relevant content found)")

# Usage
input_folder = r'C:\Users\spark\OneDrive\Desktop\QMSS Classes\Sem 1\NLP\final proj\filtered_companies_10'
output_folder = r'C:\Users\spark\OneDrive\Desktop\QMSS Classes\Sem 1\NLP\final proj\final_cleaned_transcripts'
process_folder(input_folder, output_folder)
