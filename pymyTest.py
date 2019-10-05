'''
크롤링 > db 삽입
'''
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
  ///string입력 --> string 반환 여기서 크롤링 할 필요 없음.///
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


#크롤링 & 자연어 처리 끝난 데이터 db에 삽입하기
#full content 말고 자연어 처리된 데이터를 디비에 넣는 걸로 소스 수정 필요
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
