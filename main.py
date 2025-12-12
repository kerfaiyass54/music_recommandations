
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from wordcloud import WordCloud
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

df = pd.read_csv("./spotify_millsongdata.csv")


print("\nNumber of data in this CSV: ", df.shape)

print("\nFirst 5 data rows: ", df.head())

print("\nInformation about the dataset: ", df.info())

print("\nNumber of null entries: ", df.isnull().sum())

top_artists = df['artist'].value_counts().head(10)
print("\nTop 10 artists: ", top_artists)


df = df.sample(10000)
df = df.drop('link', axis=1).reset_index(drop=True)


all_lyrics = " ".join(df['text'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_lyrics)


plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Most Common Words in Lyrics")
plt.show()





