from newspaper import Article
from urllib.request import urlopen
import urllib.parse
from bs4 import BeautifulSoup
import re
import pymysql.cursors
 
def get_art_body(URL):
  a = Article(URL,language='ko')
  a.download()
  a.parse()
  return (a.title,a.text)

def get_articles_list():  
  with urllib.request.urlopen("https://www.hankyung.com/society/1002?hkonly=true") as response:
    html = response.read()
    soup = BeautifulSoup(html,'html.parser')
    art_link = soup.select('div.article > span > a')

  articles = []

'''
def text_rank(content):
  //////
  return summary
'''

  for (i,a) in enumerate(art_link):
    #articles[i][0]: 링크, articles[i][1]: 제목, articles[i][2]: 본문
    if i == 15:
      break
    l = a.get('href')
    (t,c) = get_art_body(l)
    #r = text_rank(c)
    articles.append([t,c,l])  #articles.append([t,c,l,r])
    

  return articles



import pymysql

# 접속
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='171217', db='test', charset='utf8')

atcList = get_articles_list()
try:
  for a in atcList:
    with conn.cursor() as cursor:
      sql = 'INSERT INTO news (title,content,link) VALUES (%s, %s, %s)'
      cursor.execute(sql, (a[0],a[1],a[2]))
    conn.commit()
    print(cursor.lastrowid)
    
finally:
    conn.close()
