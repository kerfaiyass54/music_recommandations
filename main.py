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

