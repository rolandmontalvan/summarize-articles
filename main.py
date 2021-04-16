import tkinter
import nltk
from textblob import TextBlob
from newspaper import Article
from googletrans import Translator

translator = Translator()
nltk.download('punkt')

url = 'https://www.sciencedirect.com/science/article/pii/S108480452030237X'

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

#print(f'{article.html}')


print(f'Title: {article.title}')
print(f'Título: {title.text}')
print(f'Key Words: {article.keywords}')
print(f'\nAuthors: {article.authors}')
print(f'\nPublication Date: {article.publish_date}')
print(f'\nSummary: {article.summary}')
print(f'\nResumo: {summary.text}')
print(f'\nText: {article.text}')
print(f'\nTexto: {text.text}')


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