import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"

req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

#영화 순위, 영화 제목, 예매율, 개봉일자
#제목 title, percent?score?, txt-info
title = soup.select(".title")
percent = soup.select(".percent")
txt_info = soup.select(".txt-info strong")

results=[]
for title_a, percent_a, txt_info_a in zip(title, percent, txt_info):
    result = {
        "title": title_a.text.strip(),
        "percent": percent_a.text.strip(),
        "txt_info": txt_info_a.find(text=True, recursive=False).strip()
    }
    results.append(result)

for rank, item in enumerate(results, 1):
    title = item["title"]
    percent = item["percent"]
    txt_info = item["txt_info"]
    print(f"순위 : {rank}위")
    print(f"제목 : {title}")
    print(f"예매율 : {percent}")
    print(f"개봉일자 : {txt_info}")
    print()
    