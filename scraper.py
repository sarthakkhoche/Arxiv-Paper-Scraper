import requests
from bs4 import BeautifulSoup
import sys

def get_data(url, i):
    r = requests.get(url)
    content = r.content
    soup = BeautifulSoup(content, "html.parser")
    paper_tags = soup.findAll('span', attrs={'class':'list-identifier'})

    for paper in paper_tags:
        i+=1
        paper_tag = paper.find('a', attrs={'title': 'Download PDF'})
        save_pdf("https://arxiv.org" + paper_tag['href'], "p_" + str(i)+ ".pdf")

def save_pdf(url, filename):
    response = requests.get(url, stream=True)
    if not response.ok:
        print(response)
        return

    paper_data = response.content
    filename = "./papers/"+filename
    with open(filename, 'wb') as handler:
        handler.write(paper_data)

dic = {'cv' : "https://arxiv.org/list/cs.CV/recent",
       'ml' : "https://arxiv.org/list/cs.LG/recent",
       'cry' : "https://arxiv.org/list/cs.CR/recent",
       'dsa' : "https://arxiv.org/list/cs.DS/recent",
       'ai' : "https://arxiv.org/list/cs.AI/recent",
       'db' : "https://arxiv.org/list/cs.DB/recent",
       'os' : "https://arxiv.org/list/cs.OS/recent",
       'pl' : "https://arxiv.org/list/cs.PL/recent",
       'sr' : "https://arxiv.org/list/cs.SD/recent"}

inp = input()
get_data(dic[inp], 0)
print("Done!")
