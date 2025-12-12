import zipile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import IfidVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from wordcloud import WordCloud
import re
import ntlk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

df = pd.read_csv("./spotify_millsongdata.csv")


print("Number of data in this CSV: " + df.shape)

print("First 5 data rows: " + df.head())

print("Information about the dataset: /n" + df.info())

print("Number of null entries: " + df.isnull.sum())






