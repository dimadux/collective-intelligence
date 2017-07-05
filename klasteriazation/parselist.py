import feedparser
import re
import pandas as pd

links = []
with open("feedlist.txt","r") as file:
    links = file.readlines()
links = [s.strip() for s in links]

def getwordscount(url):
    wordict = {}
    html = feedparser.parse(url)

    for entry in html.entries:
        if "summary" in entry: summary = entry.summary
        else: summary = entry.description

        words = getwords(summary)
        for word in words:
            wordict.setdefault(word,0)
            wordict[word]+=1
    return url,wordict

def getwords(html):
    txt = re.compile(r'<[^>]+>').sub("",html)
    words = re.compile(r'[^A-Z^a-z]+').split(txt)
    return [word.lower() for word in words if word !='']

def getall(links,file_name):
    apcount = {}
    wordcounts = {}
    for link in links:
        title,wordcount = getwordscount(link)
        wordcounts[title] = wordcount
        for word,count in wordcount.items( ):
            apcount.setdefault(word,0)
            if count>1:
                apcount[word]+=1
    wordlist=[]
    for w,bc in apcount.items( ):
        frac=float(bc)/len(links)
        if frac>0.1 and frac<0.5 and len(w)>2: wordlist.append(w)
    for keys,value in wordcounts.items():
        for i in set(value.keys()).difference(set(wordlist)):
            del wordcounts[keys][i]
    data = pd.DataFrame.from_dict(wordcounts)
    data.to_csv(file_name, sep='\t', encoding='utf-8', na_rep="0")
getall(links,"blogs.csv")
