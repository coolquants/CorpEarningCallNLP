# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:22:31 2024

@author: spark
"""

'''
Direct from zip folder: Combined extracting txt file paths from zip and sentiment analysis of each file
import zipfile
import csv
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the NLTK sentiment analysis model
nltk.download('vader_lexicon', quiet=True)

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores

def process_zip_files(zip_path, output_csv):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Filename', 'Positive', 'Negative', 'Neutral', 'Compound'])
            
            for file_info in zip_ref.infolist():
                if file_info.filename.endswith('.txt'):
                    with zip_ref.open(file_info.filename) as file:
                        content = file.read().decode('utf-8')
                        sentiment = analyze_sentiment(content)
                        
                        csv_writer.writerow([
                            file_info.filename,
                            sentiment['pos'],
                            sentiment['neg'],
                            sentiment['neu'],
                            sentiment['compound']
                        ])

    print(f"Sentiment analysis results have been saved to '{output_csv}'")


zip_path = "C:/Users/spark/OneDrive/Desktop/QMSS Classes/Sem 1/NLP/final proj/wetransfer_pdf_extraction_with_txt_paths-csv_2024-11-11_2058.zip"
output_csv = 'sentiment_results.csv'   

process_zip_files(zip_path, output_csv)
'''

''' from csv with each txt file_path:'''
import csv

import pandas as pd

def clean_tokenize(str_in):
    import pandas as pd
    import re
    # Preprocess input string
    str_in = re.sub("[^A-Za-z']+", " ", str_in)
    str_in = str_in.lower()
    word_set = set(str_in.split())
    return word_set

# Download necessary NLTK data#
#nltk.download('punkt')
#nltk.download('vader_lexicon')

def word_fun(df_in, col_in):
    import collections
    all_dictionary = dict()
    the_topics = set(df_in["label"]) #the_data["label"].unique()
    for x in the_topics:
        tmp = df_in[df_in["label"] == x]
        tmp = tmp[col_in].str.cat(sep=" ")
        all_dictionary[x] = dict(collections.Counter(tmp.split()))
    return all_dictionary

def rem_sw(str_in):
    from nltk.corpus import stopwords
    sw = stopwords.words('english')
    tmp = [word for word in str_in.split() if word not in sw]
    tmp = ' '.join(tmp)
    return tmp

def xform_fun(df_in, m_in, n_in, sw_in, path_in):
    import pandas as pd
    if sw_in == "tf":
        from sklearn.feature_extraction.text import CountVectorizer 
        cv = CountVectorizer(ngram_range=(m_in, n_in))
    else:
        from sklearn.feature_extraction.text import TfidfVectorizer
        cv = TfidfVectorizer(ngram_range=(m_in, n_in), use_idf=False)
    x_f_data_t = pd.DataFrame(
        cv.fit_transform(df_in).toarray()) #be careful
    write_pickle(cv, path_in, sw_in)
    x_f_data_t.columns = cv.get_feature_names_out()
    return x_f_data_t

def clean_txt(var_in):
    import re
    tmp_t = re.sub("[^A-Za-z']+", " ", var_in
                   ).strip().lower()
    return tmp_t

def read_file(file_path):
    import os
    import pandas as pd
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

def file_crawler(path_in):
    import re
    import os
    import pandas as pd
    my_pd_t = pd.DataFrame()
    
    # Debug: Check if path exists
    if not os.path.exists(path_in):
        print(f"Path does not exist: {path_in}")
        return my_pd_t
    
    for root, dirs, files in os.walk(path_in):
        # Debug: Print current directory
        print(f"Checking directory: {root}")
        
        for name in files:
            # Debug: Print file name
            
            
            if name.endswith('.txt'):  # Only process .txt files
                try:
                    file_path = os.path.join(root, name)
                    txt_t = read_file(file_path)
                    
                    if len(txt_t) > 0:
                        the_lab = re.search(r'_([A-Z]+) -', name).group(1)
                        tmp_pd = pd.DataFrame(
                            {"body": [txt_t], "label": [the_lab]})
                        my_pd_t = pd.concat(
                            [my_pd_t, tmp_pd], ignore_index=True)
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}")
    
    return my_pd_t

def read_pickle(path_in, name_in):
    import pickle
    the_data_t = pickle.load(open(path_in + name_in + ".pk", "rb"))
    return the_data_t

def write_pickle(obj_in, path_store, name_in):
    import pickle
    pickle.dump(obj_in, open(path_store + name_in + ".pk", "wb"))

import zipfile
import csv
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

#Sentiment

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores

def process_zip_files(zip_path, output_csv):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Filename', 'Positive', 'Negative', 'Neutral', 'Compound'])
            
            for file_info in zip_ref.infolist():
                if file_info.filename.endswith('.txt'):
                    with zip_ref.open(file_info.filename) as file:
                        content = file.read().decode('utf-8')
                        sentiment = analyze_sentiment(content)
                        
                        csv_writer.writerow([
                            file_info.filename,
                            sentiment['pos'],
                            sentiment['neg'],
                            sentiment['neu'],
                            sentiment['compound']
                        ])

    print(f"Sentiment analysis results have been saved to '{output_csv}'")

