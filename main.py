import tkinter
import nltk
from textblob import TextBlob
from newspaper import Article
from googletrans import Translator

translator = Translator()
nltk.download('punkt')

url = 'https://www.sciencedirect.com/science/article/pii/S1084804516000928#f0005'

article = Article(url)
article.download()
article.parse()
article.nlp()

title = article.title
title =  translator.translate(title, dest='pt', src='auto')

summary = article.summary
summary = translator.translate(summary, dest='pt', src='auto')

text = article.text
text =  translator.translate(text, dest='pt', src='auto')




print(f'Title: {article.title}')
print(f'Título: {title.text}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')
print(f'Resumo: {summary.text}')
print(f'Text: {article.text}')
print(f'Texto: {text.text}')


"""

import googletrans

print(googletrans.LANGUAGES)

"""
"""
from googletrans import Translator
translator = Translator()

result = translator.translate('bom dia')

print(result.src)
print(result.dest)
print(result.origin)
print(result.text)
print(result.pronunciation) 

"""