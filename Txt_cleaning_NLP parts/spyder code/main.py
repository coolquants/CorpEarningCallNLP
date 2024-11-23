# # -*- coding: utf-8 -*-
# """
# Created on Wed Nov 20 17:58:23 2024

# @author: spark
# """

from clean_senti_fns import *

path_stored = "C:/Users/spark/OneDrive/Desktop/QMSS Classes/Sem 1/NLP/final proj/"

# path_in = "C:/Users/spark/OneDrive/Desktop/QMSS Classes/Sem 1/NLP/final proj/final_cleaned_transcripts"
# result = file_crawler(path_in)

# write_pickle(result, path_stored, 'texts_df')


''''''''''''''''''

# data= read_pickle(path_stored, 'texts_df')
# processed_strs = data['body'].apply(clean_tokenize)
# data['regex'] = data["body"].apply(clean_txt)
# data['body_sw'] = data["regex"].apply(rem_sw)
# write_pickle(data, path_stored, 'texts_body_sw')


''''''


#doing rest on colab
#count frequency of statements and remove high frequency ones because they're just repeated things in all txts: tfidf
# tfidf = xform_fun(data['body_sw'], 1, 1, 'tfidf', path_stored)
# tfidf.head(15)


# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# vader = SentimentIntensityAnalyzer()
# data['vader'] = data['body_sw'].apply(lambda x: vader.polarity_scores(x)['compound'])
    