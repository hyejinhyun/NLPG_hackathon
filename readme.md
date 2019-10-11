Online Newspaper Summarization Web Service using Textrank Algorithm
============
> NLPG / 문효진, 백지희, 유현선, 정성원, 현혜진

# 1. 프로젝트 소개

최근 온라인 기사들의 조회수 경쟁으로 인해 내용과 관련성이 떨어지는 자극적인 제목의 기사들이 늘어나고 있다. 이에 따라 사용자들이 기사를 통해 원하는 정보를 찾는 것에 어려움을 느끼고 있다. 해당 프로젝트에서는 자연어 처리 분야 중 하나인 text summarization 기술을 이용해 온라인 기사를 요약해 사용자들에게 실제로 기사가 담고 있는 내용을 노출시킴으로써 원하는 정보를 담고 있는 기사를 선택할 수 있도록 돕는다.

# 2. 구현

## 2.1 사용 언어 및 플랫폼

python, html, php, bitnami(apache, mysql)

## 2.2 textrank 알고리즘

>text summarization은 extractive summarization과 abstractive summarization으로 나뉘며 textrank 알고리즘은 대표적인 extractive summarization 알고리즘이다.

```python
#textrank 구현 코드 중 일부
class TextRank(object):
    def __init__(self, text):
        self.sent_tokenize = SentenceTokenizer()
    
        self.sentences = self.sent_tokenize.text2sentences(text)

        self.nouns = self.sent_tokenize.get_nouns(self.sentences)

        self.graph_matrix = GraphMatrix()
        self.sent_graph = self.graph_matrix.build_sent_graph(self.nouns)

        self.rank = Rank()
        self.sent_rank_idx = self.rank.get_ranks(self.sent_graph)
        self.sorted_sent_rank_idx = sorted(self.sent_rank_idx, key=lambda k: self.sent_rank_idx[k], reverse=True)


    def summarize(self, sent_num=3):
        summary = []
        num = len(self.sentences)
        if(num>=50):
            sent_num = 5
        index=[]
        for idx in self.sorted_sent_rank_idx[:sent_num]:
            index.append(idx)

        index.sort()
        for idx in index:
            summary.append(self.sentences[idx])

        return summary
```

크롤링한 기사 본문을 문장 단위로 나눠 tfidf 알고리즘을 이용해 중요도를 계산한다. 계산된 중요도를 기준으로 가장 중요도가 높은 n개의 문장을 return 한다

# 3. References

크롤링:

<https://twpower.github.io/84-how-to-use-beautiful-soup>

<https://excelsior-cjh.tistory.com/m/92>

데이터베이스:

<https://www.fun-coding.org/mysql_basic6.html>

textrank:

<https://github.com/ExcelsiorCJH/Projects>