import re
import pandas as pd
from bs4 import BeautifulSoup
import itertools
import requests
from collections import Counter
import time
import io
import pdfplumber


output = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    'style',
    'input'
]
stopwords = ['university','dit','hoe','0','om','ook','startskip','backskip','aheadstream','playmedia','fullscreen','captionsunmuteturn','onfullscreenmedia','captionsunmuteturn','captionsunmuteturn','selected1.25x1.5x1.75x2xturn','speed0.5x0.75x1x','playmedia','speedplayback','followers','co.','university','deze','zijn','edited','op','reply','ik','8','9','je','te','voor','1mo','2mo','3mo','4mo','5mo','6mo','7mo','8mo','9mo','10mo','11mo','12mo','-','9mo','4','5','3','6','7','10','11','12','13','14','bij','•','status','see','feed','2nd','1','read','min','first','follow','het','view','image','larger','3rd+','2','een','offline','de','…see','likes','van','en','comments','comment','like','ago','dennis','nguyen','share','send','post','months','get','ourselves', 'hers','us','there','you','for','that','as','between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']
ban_chars = ['|','/','&']

fulllist = []

with open('dennis.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')


with pdfplumber.open(r'Nguyen_FINAL NEW MANUSCRIPT.pdf') as pdf:
    first_page = pdf.pages[0]
    print(first_page.extract_text())
    
    pdf_full_content = []
    for page in pdf.pages:
        page_content = page.extract_text()
        pdf_full_content.append(page_content)
    





text = soup.find_all(text=True)

for a in soup.findAll('a', href = True):
    print ('Found url: ' + a['href'])

for t in text:
    if t.parent.name not in blacklist:
        output += t.replace("\n","").replace("\t","")
output = output.split(" ")

output = [x for x in output if not x=='' and not x[0] =='#' and x not in ban_chars] 
output = [x.lower() for x in output]
output = [word for word in output if word not in stopwords]
counts = Counter(output).most_common(500)
fulllist += output
df = pd.DataFrame(counts)
df.to_csv('data_linkedin.csv', mode='a', header=False)



print('--------------------------------')

# if __name__ == '__main__':
#     open_file('dennis.html')
#     print('--------------------------------')
    



