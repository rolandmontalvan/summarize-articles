import tkinter
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')

url = 'http://www.sciencedirect.com/science/article/pii/S0040162515002942'

article = Article(url)
article.download()
article.parse()
article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')


